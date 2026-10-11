"use strict";
// Real process termination during extraction and bundle write. No Lean execution.
const fs=require("node:fs/promises");
const watch=require("node:fs").watch;
const path=require("node:path");
const crypto=require("node:crypto");
const {spawn}=require("node:child_process");
const assert=require("node:assert/strict");
const toolkit=path.resolve(__dirname,"../..");
const sha=b=>crypto.createHash("sha256").update(b).digest("hex");
async function runChild(args,signal,triggerParent,triggerFilename,insideTree=false) {
  let stdout="",stderr="",requested=false,trigger=null,child;
  const nestedWatchers=[];
  const terminate=(event,filename)=>{if(!requested){requested=true;trigger={event,filename:String(filename),timeUTC:new Date().toISOString()};child.kill(signal);}};
  const watcher=watch(triggerParent,(event,filename)=>{
    if(!requested&&String(filename)===triggerFilename){
      if(insideTree){const nested=watch(path.join(triggerParent,triggerFilename),(childEvent,childName)=>{if(/^f\d+\.txt$/.test(String(childName)))terminate(childEvent,path.join(triggerFilename,String(childName)));});nestedWatchers.push(nested);}
      else terminate(event,filename);
    }
  });
  child=spawn(process.execPath,args,{stdio:["ignore","pipe","pipe"]});
  child.stdout.on("data",b=>stdout+=b);child.stderr.on("data",b=>stderr+=b);
  const timer=setTimeout(()=>{if(!requested){trigger={event:"timeout",timeUTC:new Date().toISOString()};child.kill(signal);}},12000);
  const result=await new Promise((resolve,reject)=>{child.on("error",reject);child.on("close",(code,observedSignal)=>resolve({code,signal:observedSignal}));});
  clearTimeout(timer);watcher.close();for(const nested of nestedWatchers)nested.close();return {...result,requested,trigger,stdout,stderr};
}
async function ordinary(args) {
  const child=spawn(process.execPath,args,{stdio:["ignore","pipe","pipe"]});let stdout="",stderr="";child.stdout.on("data",b=>stdout+=b);child.stderr.on("data",b=>stderr+=b);const exit=await new Promise(resolve=>child.on("close",(code,signal)=>resolve({code,signal})));return {...exit,stdout,stderr};
}
async function inventory(root) {
  const list=[];async function walk(dir){for(const d of await fs.readdir(dir,{withFileTypes:true})){const p=path.join(dir,d.name);if(d.isDirectory())await walk(p);else list.push({path:path.relative(root,p),size:(await fs.lstat(p)).size});}}await walk(root);return list;
}
async function main() {
  const base=require("node:os").tmpdir();await fs.mkdir(base,{recursive:true});const work=await fs.mkdtemp(path.join(base,"interruption-")),results=[];
  for(const signal of ["SIGTERM","SIGINT"]) {
    const input=path.join(work,signal+"-distribution.json"),output=path.join(work,signal+"-extracted"),text="padding\n".repeat(1000);
    const distribution={schema:"math-companion-distribution/v1",files:Array.from({length:800},(_,i)=>({path:"f"+String(i).padStart(4,"0")+".txt",text,sha256:sha(Buffer.from(text))}))};
    const bytes=Buffer.from(JSON.stringify(distribution)+"\n");await fs.writeFile(input,bytes);
    const termination=await runChild([path.join(toolkit,"materialize.cjs"),input,sha(bytes),output],signal,work,path.basename(output),true);
    assert.equal(termination.requested,true);assert.equal(termination.signal,signal);assert.equal(termination.code,null);assert.equal(termination.stdout,"");
    const partial=await inventory(output);assert.ok(partial.length>0&&partial.length<800);
    const retry=await ordinary([path.join(toolkit,"materialize.cjs"),input,sha(bytes),output]);assert.equal(retry.code,2);assert.equal(retry.stdout,"");assert.deepEqual(await inventory(output),partial);
    results.push({name:"extraction-"+signal,pass:true,termination,expectedFiles:800,partialFiles:partial.length,partial,retry:{exit:retry.code,stderr:retry.stderr.trim()},successReceiptAbsent:true,leanExecution:"not_performed"});
  }
  const root=path.join(work,"bundle-root");await fs.mkdir(root);
  const statement="theorem valid : True",source="namespace Fixture\n"+statement+" := by trivial\nend Fixture\n"+"-- padding data\n".repeat(400000);
  const texts={"Fixture.lean":source,"lean-toolchain":"leanprover/lean4:v4.24.0\n","lake-manifest.json":JSON.stringify({packages:[{name:"mathlib",type:"git",url:"https://github.com/leanprover-community/mathlib4",rev:"a".repeat(40)}]})+"\n"};
  const roles={"Fixture.lean":"source","lean-toolchain":"toolchain","lake-manifest.json":"lockfile"};
  for(const [p,t] of Object.entries(texts))await fs.writeFile(path.join(root,p),t);
  const catalog={schema:"math-exchange/v1",project:{repository:"https://example.org/fixture",revision:"b".repeat(40),branch:"interrupt",lean_toolchain:"leanprover/lean4:v4.24.0",mathlib_revision:"a".repeat(40)},files:Object.keys(texts).map(p=>({path:p,role:roles[p],sha256:sha(Buffer.from(texts[p]))})),records:[{id:"valid",name:"Fixture.valid",kind:"theorem",statement:{text:statement,source_path:"Fixture.lean",source_excerpt:statement,sha256:sha(Buffer.from(statement))},assumptions:[],dependencies:[],sources:[{url:"https://example.org/source",revision:"b".repeat(40),locator:"Fixture.valid"}],review:{status:"not_reviewed",evidence:[]},experiments:[],lean:{status:"not_run",evidence:[],reason:"Never compiled; termination fixture"}}]};
  const catalogFile=path.join(work,"catalog.json");await fs.writeFile(catalogFile,JSON.stringify(catalog)+"\n");
  for(const signal of ["SIGTERM","SIGINT"]) {
    const output=path.join(work,signal+"-bundle.json");
    const termination=await runChild([path.join(toolkit,"cli.cjs"),"bundle",catalogFile,root,output],signal,work,path.basename(output));
    assert.equal(termination.requested,true);assert.equal(termination.signal,signal);assert.equal(termination.code,null);assert.equal(termination.stdout,"");
    const bytes=await fs.readFile(output),inspect=await ordinary([path.join(toolkit,"cli.cjs"),"inspect-bundle",output]);
    if(inspect.code===0)assert.equal(JSON.parse(inspect.stdout).summary.counts.leanPasses,0);else assert.equal(inspect.code,2);
    results.push({name:"bundle-"+signal,pass:true,termination,partialBytes:bytes.length,partialSHA256:sha(bytes),inspection:{exit:inspect.code,stdout:inspect.stdout,stderr:inspect.stderr},successReceiptAbsent:true,leanExecution:"not_performed"});
  }
  const report={schema:"real-os-interruption-review/v1",timeUTC:new Date().toISOString(),runtime:process.version,work,mode:"actual_Node_OS_signals_filesystem_watch_no_mock_adapters",command:"node verification/adversarial-review/interruption.cjs",total:results.length,passed:results.filter(r=>r.pass).length,results};
  await fs.writeFile(path.join(__dirname,"interruption-report.json"),JSON.stringify(report,null,2)+"\n");process.stdout.write(JSON.stringify(report,null,2)+"\n");
}
main().catch(e=>{console.error(e);process.exitCode=1;});
