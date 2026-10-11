"use strict";
// Independent actual Node, filesystem and CLI audit. This suite never invokes Lean.
// The two race probes interpose syscall ordering while retaining actual OS I/O.
const fs = require("node:fs/promises");
const path = require("node:path");
const crypto = require("node:crypto");
const {spawn, spawnSync} = require("node:child_process");
const assert = require("node:assert/strict");
const toolkit = path.resolve(__dirname,"../..");
const sha = b => crypto.createHash("sha256").update(b).digest("hex");
const clone = x=>JSON.parse(JSON.stringify(x));
const results=[];
let work,sequence=0;
async function sourceDigests() {
  const names=["core.cjs","strict-json.cjs","cli.cjs","bundle.cjs","materialize.cjs","tangent-pins.cjs","bounded-io.cjs"];
  return Object.fromEntries(await Promise.all(names.map(async name=>[name,sha(await fs.readFile(path.join(toolkit,name)))])));
}
const next = name => path.join(work,(++sequence)+"-"+name);
async function test(name,expected,fn,mode="actual_Node_CLI_filesystem") {
  try { const observed=await fn();results.push({name,expected,pass:true,mode,observed}); }
  catch(error){results.push({name,expected,pass:false,mode,error:String(error.stack||error)});}
}
async function cli(args,timeout=3000) {
  const child=spawn(process.execPath,[path.join(toolkit,"cli.cjs"),...args],{stdio:["ignore","pipe","pipe"]});
  let stdout="",stderr="",timedOut=false;
  child.stdout.on("data",b=>stdout+=b);child.stderr.on("data",b=>stderr+=b);
  const timer=setTimeout(()=>{timedOut=true;child.kill("SIGTERM");},timeout);
  const result=await new Promise((resolve,reject)=>{child.on("error",reject);child.on("close",(code,signal)=>resolve({code,signal}));});
  clearTimeout(timer);return {...result,timedOut,stdout,stderr};
}
function fixture() {
  const statement="theorem valid : True";
  const texts={"source/Fixture.lean":"namespace Fixture\n"+statement+" := by trivial\nend Fixture\n","lean-toolchain":"leanprover/lean4:v4.24.0\n","lake-manifest.json":JSON.stringify({packages:[{name:"mathlib",type:"git",url:"https://github.com/leanprover-community/mathlib4",rev:"a".repeat(40)}]})+"\n","review.txt":"Ordinary review report only.\n","experiment.txt":"Finite n=1,2,3 only.\n","legacy.log":"Historical compilation success, exit 0. Not rerun.\n"};
  const roles={"source/Fixture.lean":"source","lean-toolchain":"toolchain","lake-manifest.json":"lockfile","review.txt":"review","experiment.txt":"experiment","legacy.log":"legacy_log"};
  return {texts,catalog:{schema:"math-exchange/v1",project:{repository:"https://example.org/fixture",revision:"b".repeat(40),branch:"adversarial-fixture",lean_toolchain:"leanprover/lean4:v4.24.0",mathlib_revision:"a".repeat(40)},files:Object.keys(texts).map(p=>({path:p,role:roles[p],sha256:sha(Buffer.from(texts[p]))})),records:[{id:"fixture.valid",name:"Fixture.valid",kind:"theorem",statement:{text:statement,source_path:"source/Fixture.lean",source_excerpt:statement,sha256:sha(Buffer.from(statement))},assumptions:[],dependencies:[],sources:[{url:"https://example.org/fixture/source",revision:"b".repeat(40),locator:"Fixture.valid"}],review:{status:"review_reported",evidence:["review.txt"]},experiments:[{claim:"Finite checked data reported",scope:"n in {1,2,3}",evidence:["experiment.txt"]}],lean:{status:"historical_report",evidence:["legacy.log"],reason:"Historical log only; no new live run"}}]}};
}
async function diskFixture(mutate) {
  const f=fixture();if(mutate)mutate(f);
  const root=next("root"),catalog=next("catalog.json");await fs.mkdir(root);
  for(const [p,t] of Object.entries(f.texts)){await fs.mkdir(path.dirname(path.join(root,p)),{recursive:true});await fs.writeFile(path.join(root,p),t);}
  await fs.writeFile(catalog,JSON.stringify(f.catalog)+"\n");return {...f,root,catalog};
}
function reject(r,code) {assert.equal(r.code,2);assert.equal(r.signal,null);assert.equal(r.timedOut,false);assert.equal(r.stdout,"");if(code)assert.ok(JSON.parse(r.stderr).errors.some(e=>e.code===code),r.stderr);return {exit:r.code,codes:JSON.parse(r.stderr).errors.map(e=>e.code)};}
async function materialize(files,expectedFailure=true,rawOverride) {
  const input=next("distribution.json"),output=next("extracted");
  const data={schema:"math-companion-distribution/v1",files:files.map(f=>({path:f.path,text:f.text,sha256:f.sha256||sha(Buffer.from(f.text))}))};
  const raw=rawOverride||Buffer.from(JSON.stringify(data)+"\n");await fs.writeFile(input,raw);
  const r=spawnSync(process.execPath,[path.join(toolkit,"materialize.cjs"),input,sha(raw),output],{encoding:"utf8",timeout:3000});
  assert.equal(r.status,expectedFailure?2:0);if(expectedFailure){assert.equal(r.stdout,"");assert.equal(await fs.stat(output).then(()=>true,()=>false),false);}
  return {exit:r.status,stderr:r.stderr.trim(),input,output};
}
async function main() {
  const disposableBase=require("node:os").tmpdir();
  await fs.mkdir(disposableBase,{recursive:true});
  work=await fs.mkdtemp(path.join(disposableBase,"actual-work-"));
  const beforeSourceSHA256=await sourceDigests();
  await test("valid-historical-ordinary-experiment", "accepted; all evidence types separate; zero Lean passes",async()=>{
    const f=await diskFixture();const r=await cli(["validate",f.catalog,f.root]);assert.equal(r.code,0);const summary=JSON.parse(r.stdout).summary;assert.equal(summary.counts.leanPasses,0);assert.equal(summary.counts.historicalLeanReports,1);assert.equal(summary.counts.reviewReported,1);assert.equal(summary.counts.experimentReports,1);return summary.counts;
  });
  for(const status of ["pass","checked","compiled","kernel_verified","type_matched","success"]){await test("status-upgrade-"+status,"unsupported Lean status rejected",async()=>{const f=await diskFixture(f=>f.catalog.records[0].lean.status=status);return reject(await cli(["validate",f.catalog,f.root]),"unsupported_value");});}
  const recordMutations=[
    ["unknown-command",f=>f.catalog.records[0].command="touch /tmp/must-never-run","unknown_field"],
    ["absent-assumptions",f=>delete f.catalog.records[0].assumptions,"missing_field"],
    ["duplicate-record",f=>f.catalog.records.push(clone(f.catalog.records[0])),"duplicate_id"],
    ["dead-reference",f=>f.catalog.records[0].dependencies=["missing"],"dead_reference"],
    ["self-cycle",f=>f.catalog.records[0].dependencies=["fixture.valid"],"dependency_cycle"],
    ["review-no-evidence",f=>f.catalog.records[0].review.evidence=[],"type"],
    ["historical-no-evidence",f=>f.catalog.records[0].lean.evidence=[],"type"],
    ["wrong-review-role",f=>f.catalog.records[0].review.evidence=["legacy.log"],"evidence_role"],
    ["wrong-claim",f=>f.catalog.records[0].statement.text="theorem valid : False","statement_excerpt_mismatch"],
    ["source-tamper",f=>f.texts["source/Fixture.lean"]+="-- change\n","file_hash_mismatch"],
    ["review-tamper",f=>f.texts["review.txt"]="fake review\n","file_hash_mismatch"],
    ["historical-tamper",f=>f.texts["legacy.log"]="fake exit 0\n","file_hash_mismatch"],
    ["empty-review-repinned",f=>{f.texts["review.txt"]="";f.catalog.files.find(x=>x.path==="review.txt").sha256=sha(Buffer.alloc(0));},"empty_evidence"],
    ["manifest-case-collision",f=>f.catalog.files.push({...f.catalog.files[0],path:"SOURCE/Fixture.lean"}),"duplicate_file"],
    ["manifest-prefix-collision",f=>f.catalog.files.push({path:"source",role:"source",sha256:"0".repeat(64)}),"path_prefix_collision"],
    ["source-revision-branch",f=>f.catalog.records[0].sources[0].revision="main","format"]
  ];
  for(const [name,mutate,code] of recordMutations)await test(name,"rejected with "+code,async()=>{const f=await diskFixture(mutate);return reject(await cli(["validate",f.catalog,f.root]),code);});
  await test("historical-interrupted-log","accepted historical report; zero Lean pass",async()=>{const f=await diskFixture(f=>{f.texts["legacy.log"]="Historical process terminated SIGTERM; no exit success.\n";f.catalog.files.find(x=>x.path==="legacy.log").sha256=sha(Buffer.from(f.texts["legacy.log"]));});const r=await cli(["validate",f.catalog,f.root]);assert.equal(r.code,0);assert.equal(JSON.parse(r.stdout).summary.counts.leanPasses,0);return JSON.parse(r.stdout).summary.counts;});
  await test("embedded-command-prose","inert imported text; no marker created",async()=>{const marker=next("inert-marker");const f=await diskFixture(f=>f.catalog.records[0].lean.reason="$(touch "+marker+") and `touch "+marker+"` are inert prose");const r=await cli(["validate",f.catalog,f.root]);assert.equal(r.code,0);assert.equal(await fs.stat(marker).then(()=>true,()=>false),false);return {exit:r.code,markerAbsent:true,leanPasses:JSON.parse(r.stdout).summary.counts.leanPasses};});
  for(const name of ["source/Fixture.lean","review.txt","legacy.log"])await test("missing-"+name,"file_read rejection",async()=>{const f=await diskFixture();await fs.unlink(path.join(f.root,name));return reject(await cli(["validate",f.catalog,f.root]),"file_read");});
  for(const ancestor of [false,true])await test("static-source-symlink-"+(ancestor?"parent":"file"),"symlink rejected",async()=>{
    const f=await diskFixture(),outside=next("outside");await fs.mkdir(outside);await fs.writeFile(path.join(outside,"Fixture.lean"),f.texts["source/Fixture.lean"]);
    if(ancestor){await fs.rename(path.join(f.root,"source"),path.join(f.root,"original-source"));await fs.symlink(outside,path.join(f.root,"source"));}
    else{await fs.unlink(path.join(f.root,"source/Fixture.lean"));await fs.symlink(path.join(outside,"Fixture.lean"),path.join(f.root,"source/Fixture.lean"));}
    return reject(await cli(["validate",f.catalog,f.root]),"file_read");
  });
  await test("catalog-symlink","final catalog symlink rejected",async()=>{const f=await diskFixture(),link=next("catalog-link");await fs.symlink(f.catalog,link);return reject(await cli(["validate",link,f.root]));});
  await test("duplicate-decoded-JSON-key","duplicate key rejected",async()=>{const f=await diskFixture();await fs.writeFile(f.catalog,JSON.stringify(f.catalog).replace('"schema":"math-exchange/v1"','"schema":"bad","s\\u0063hema":"math-exchange/v1"'));return reject(await cli(["validate",f.catalog,f.root]));});
  await test("invalid-UTF8-catalog","malformed UTF8 rejected",async()=>{const f=await diskFixture();await fs.writeFile(f.catalog,Buffer.from([0xc0,0x80]));return reject(await cli(["validate",f.catalog,f.root]));});
  await test("deterministic-bundle-and-exclusive-output","identical byte bundles; existing output preserved",async()=>{const f=await diskFixture(),one=next("one.json"),two=next("two.json");assert.equal((await cli(["bundle",f.catalog,f.root,one])).code,0);assert.equal((await cli(["bundle",f.catalog,f.root,two])).code,0);const a=await fs.readFile(one),b=await fs.readFile(two);assert.deepEqual(a,b);reject(await cli(["bundle",f.catalog,f.root,one]));assert.deepEqual(await fs.readFile(one),a);assert.equal((await cli(["inspect-bundle",one])).code,0);return {bytes:a.length,sha256:sha(a),existingOutputPreserved:true};});
  for(const variant of ["tamper","missing","extra","duplicate","unsafe"]){await test("bundle-"+variant,"malformed evidence bundle rejected",async()=>{const f=await diskFixture(),output=next("bundle.json");assert.equal((await cli(["bundle",f.catalog,f.root,output])).code,0);const b=JSON.parse(await fs.readFile(output,"utf8"));if(variant==="tamper")b.files[0].hex="00";if(variant==="missing")b.files.pop();if(variant==="extra")b.files.push({path:"extra.txt",hex:"00",sha256:sha(Buffer.from([0]))});if(variant==="duplicate")b.files.push(clone(b.files[0]));if(variant==="unsafe"){b.files[0].path="../escape";b.catalog.files.find(f=>f.sha256===b.files[0].sha256).path="../escape";}await fs.writeFile(output,JSON.stringify(b));return reject(await cli(["inspect-bundle",output]));});}
  for(const unsafe of ["../escape","/absolute","a/../b","a/./b","a\\b","a//b","NUL.txt","COM1","trailing.","con/x","a:b","./x"]){await test("extract-path-"+unsafe,"unsafe portable path rejected before output creation",()=>materialize([{path:unsafe,text:"marker\n"}]));}
  for(const names of [["a","A"],["a","a/x"],["a","A/x"]])await test("extract-collision-"+names.join("-"),"case/prefix collision rejected before creation",()=>materialize(names.map(path=>({path,text:"marker\n"}))));
  await test("extract-entry-hash-mismatch","wrong entry bytes rejected before creation",()=>materialize([{path:"x",text:"one",sha256:sha(Buffer.from("two"))}]));
  await test("extract-byte-identity-and-inert-script","exact bytes extracted; imported script never executed",async()=>{const marker=next("execution-marker"),text="require('node:fs').writeFileSync("+JSON.stringify(marker)+",'bad');\n";const r=await materialize([{path:"nested/code.cjs",text},{path:"unicode.txt",text:"ℝ π ∀ n : ℕ 😀\n"}],false);assert.equal(await fs.readFile(path.join(r.output,"nested/code.cjs"),"utf8"),text);assert.equal(await fs.readFile(path.join(r.output,"unicode.txt"),"utf8"),"ℝ π ∀ n : ℕ 😀\n");assert.equal(await fs.stat(marker).then(()=>true,()=>false),false);return {...r,scriptMarkerAbsent:true};});
  await test("extract-existing-output","refuses existing directory and preserves marker",async()=>{const input=next("dist.json"),output=next("existing");await fs.mkdir(output);await fs.writeFile(path.join(output,"marker"),"preserve");const raw=Buffer.from(JSON.stringify({schema:"math-companion-distribution/v1",files:[]})+"\n");await fs.writeFile(input,raw);const r=spawnSync(process.execPath,[path.join(toolkit,"materialize.cjs"),input,sha(raw),output],{encoding:"utf8"});assert.equal(r.status,2);assert.equal(await fs.readFile(path.join(output,"marker"),"utf8"),"preserve");return {exit:r.status,markerPreserved:true};});
  await test("extract-unpaired-surrogate","invalid Unicode distribution rejected",()=>materialize([{path:"x",text:"\ud800"}]));
  await test("extract-duplicate-decoded-key","duplicate distribution field rejected",async()=>{const raw=Buffer.from('{"schema":"bad","schema":"math-companion-distribution/v1","files":[]}\n');return materialize([],true,raw);});
  await test("extract-invalid-UTF8","invalid source distribution UTF8 rejected before extraction",async()=>{const prefix=Buffer.from('{"schema":"math-companion-distribution/v1","files":[{"path":"x","text":"'),suffix=Buffer.from('","sha256":"'+sha(Buffer.from("\ufffd\ufffd"))+'"}]}\n');return materialize([],true,Buffer.concat([prefix,Buffer.from([0xc0,0x80]),suffix]));});
  await test("extract-parent-symlink","operator destination parent symlinks rejected",async()=>{const outside=next("parent-real"),link=next("parent-link"),input=next("parent-dist.json");await fs.mkdir(outside);await fs.symlink(outside,link);const raw=Buffer.from('{"schema":"math-companion-distribution/v1","files":[]}\n');await fs.writeFile(input,raw);const r=spawnSync(process.execPath,[path.join(toolkit,"materialize.cjs"),input,sha(raw),path.join(link,"new")],{encoding:"utf8"});assert.equal(r.status,2);assert.equal(await fs.stat(path.join(outside,"new")).then(()=>true,()=>false),false);return {exit:r.status,stderr:r.stderr.trim(),outsideUntouched:true};});
  await test("extract-unsupported-platform","unsupported extraction platform selector fails closed before root creation",async()=>{const {materialize:extract}=require(path.join(toolkit,"materialize.cjs")),input=next("platform-dist.json"),output=next("platform-root"),raw=Buffer.from('{"schema":"math-companion-distribution/v1","files":[]}\n');await fs.writeFile(input,raw);const descriptor=Object.getOwnPropertyDescriptor(process,"platform");let error;try{Object.defineProperty(process,"platform",{value:"darwin",configurable:true});await extract(input,sha(raw),output);}catch(e){error=e;}finally{Object.defineProperty(process,"platform",descriptor);}assert.ok(error);assert.equal(await fs.stat(output).then(()=>true,()=>false),false);return {error:String(error.message),actualHost:"Linux; platform branch simulated; no native Mac test",rootAbsent:true};},"actual_Node_filesystem_with_simulated_platform_selector");
  await test("extract-missing-descriptor-alias","missing /proc descriptor aliases fail closed before creation",async()=>{const {materialize:extract}=require(path.join(toolkit,"materialize.cjs")),input=next("alias-dist.json"),output=next("alias-root"),raw=Buffer.from('{"schema":"math-companion-distribution/v1","files":[]}\n');await fs.writeFile(input,raw);const originalStat=fs.stat;let error,hooked=false;fs.stat=async function(name,...args){if(/^\/proc\/self\/fd\/\d+$/.test(String(name))){hooked=true;throw new Error("injected descriptor alias unavailable");}return originalStat.call(fs,name,...args);};try{await extract(input,sha(raw),output);}catch(e){error=e;}finally{fs.stat=originalStat;}assert.equal(hooked,true);assert.ok(error);assert.equal(await fs.stat(output).then(()=>true,()=>false),false);return {hooked,error:String(error.message),rootAbsent:true};},"actual_Node_filesystem_with_unavailable_descriptor_alias_hook");
  await test("source-symlink-interleaving","symlink introduced after containment rejected",async()=>{
    const f=await diskFixture(),outside=next("race-outside");await fs.mkdir(outside);await fs.writeFile(path.join(outside,"Fixture.lean"),"outside marker\n");const {sourceReader}=require(path.join(toolkit,"cli.cjs"));const reader=await sourceReader(f.root),originalOpen=fs.open;let swapped=false,bytes,error;
    fs.open=async function(filename,...args){if(!swapped&&filename===path.join(f.root,"source/Fixture.lean")){swapped=true;await fs.rename(path.join(f.root,"source"),path.join(f.root,"source.original"));await fs.symlink(outside,path.join(f.root,"source"));}return originalOpen.call(fs,filename,...args);};
    try{bytes=await reader("source/Fixture.lean");}catch(e){error=e;}finally{fs.open=originalOpen;}
    assert.ok(error,"escaped source read: "+Buffer.from(bytes||[]).toString());return {swapped,error:String(error.message)};
  },"actual_Node_filesystem_with_syscall_ordering_hook");
  await test("extraction-symlink-interleaving","new output parent replaced during extraction cannot escape",async()=>{
    const {materialize:extract}=require(path.join(toolkit,"materialize.cjs"));const input=next("race-dist.json"),output=next("race-output"),outside=next("extract-outside");await fs.mkdir(outside);const text="escaped extraction marker\n",raw=Buffer.from(JSON.stringify({schema:"math-companion-distribution/v1",files:[{path:"d/x.txt",text,sha256:sha(Buffer.from(text))}]})+"\n");await fs.writeFile(input,raw);
    const originalWrite=fs.writeFile;let swapped=false,error;fs.writeFile=async function(filename,...args){if(!swapped&&(filename===path.join(output,"d/x.txt")||/^\/proc\/self\/fd\/\d+\/x\.txt$/.test(String(filename)))){swapped=true;await fs.rename(path.join(output,"d"),path.join(output,"d.original"));await fs.symlink(outside,path.join(output,"d"));}return originalWrite.call(fs,filename,...args);};
    try{await extract(input,sha(raw),output);}catch(e){error=e;}finally{fs.writeFile=originalWrite;}
    const escaped=await fs.stat(path.join(outside,"x.txt")).then(()=>true,()=>false);assert.equal(swapped,true,"race hook did not fire");assert.equal(escaped,false,"distribution written outside newly-created extraction root");assert.ok(error);return {swapped,escaped,error:String(error.message)};
  },"actual_Node_filesystem_with_syscall_ordering_hook");
  await test("extraction-root-symlink-interleaving","opened extraction root cannot be redirected by lexical root replacement",async()=>{
    const {materialize:extract}=require(path.join(toolkit,"materialize.cjs"));const input=next("root-race-dist.json"),output=next("root-race-output"),outside=next("root-extract-outside");await fs.mkdir(outside);const text="root escaped marker\n",raw=Buffer.from(JSON.stringify({schema:"math-companion-distribution/v1",files:[{path:"x.txt",text,sha256:sha(Buffer.from(text))}]})+"\n");await fs.writeFile(input,raw);
    const originalWrite=fs.writeFile;let swapped=false,error;fs.writeFile=async function(filename,...args){if(!swapped&&(filename===path.join(output,"x.txt")||/^\/proc\/self\/fd\/\d+\/x\.txt$/.test(String(filename)))){swapped=true;await fs.rename(output,output+".original");await fs.symlink(outside,output);}return originalWrite.call(fs,filename,...args);};
    try{await extract(input,sha(raw),output);}catch(e){error=e;}finally{fs.writeFile=originalWrite;}
    const escaped=await fs.stat(path.join(outside,"x.txt")).then(()=>true,()=>false);assert.equal(swapped,true,"race hook did not fire");assert.equal(escaped,false,"root swap redirected distribution write");assert.ok(error);return {swapped,escaped,error:String(error.message)};
  },"actual_Node_filesystem_with_syscall_ordering_hook");
  await test("extraction-parent-ancestor-symlink-interleaving","initial output parent ancestry cannot redirect root creation",async()=>{
    const {materialize:extract}=require(path.join(toolkit,"materialize.cjs")),input=next("ancestor-race-dist.json"),outer=next("ancestor-outer"),outside=next("ancestor-outside"),parent=path.join(outer,"selected"),output=path.join(parent,"output");
    await fs.mkdir(parent,{recursive:true});await fs.mkdir(path.join(outside,"selected"),{recursive:true});
    const text="outside ancestor marker\n",raw=Buffer.from(JSON.stringify({schema:"math-companion-distribution/v1",files:[{path:"x.txt",text,sha256:sha(Buffer.from(text))}]})+"\n");await fs.writeFile(input,raw);
    const originalLstat=fs.lstat;let swapped=false,error;
    fs.lstat=async function(filename,...args){if(!swapped&&(filename===parent||String(filename).match(/^\/proc\/self\/fd\/\d+\//)&&String(filename).endsWith("/"+path.basename(outer)))){swapped=true;await fs.rename(outer,outer+".original");await fs.symlink(outside,outer);}return originalLstat.call(fs,filename,...args);};
    try{await extract(input,sha(raw),output);}catch(e){error=e;}finally{fs.lstat=originalLstat;}
    assert.equal(swapped,true,"initial ancestor race hook did not fire");assert.equal(await fs.stat(path.join(outside,"selected/output/x.txt")).then(()=>true,()=>false),false,"initial ancestry swap redirected write");assert.ok(error);return {swapped,outsideWriteAbsent:true,error:String(error.message)};
  },"actual_Node_filesystem_with_syscall_ordering_hook");
  for(const where of ["JSON-input","manifest-source"]){await test("named-pipe-"+where,"special file promptly rejected before blocking; no success",async()=>{
    const f=await diskFixture(),fifo=where==="JSON-input"?next("input.fifo"):path.join(f.root,"source/Fixture.lean");if(where!=="JSON-input")await fs.unlink(fifo);const mk=spawnSync("mkfifo",[fifo]);assert.equal(mk.status,0);const r=where==="JSON-input"?await cli(["inspect-bundle",fifo],1200):await cli(["validate",f.catalog,f.root],1200);assert.equal(r.timedOut,false,"blocking named pipe required SIGTERM");return reject(r,where==="manifest-source"?"file_read":undefined);
  });}
  const afterSourceSHA256=await sourceDigests();
  const report={schema:"independent-adversarial-review/v1",timeUTC:new Date().toISOString(),runtime:process.version,platform:process.platform,work,toolkit,commands:["node verification/adversarial-review/real-adversarial.cjs"],beforeSourceSHA256,afterSourceSHA256,sourceUnchangedDuringRun:JSON.stringify(beforeSourceSHA256)===JSON.stringify(afterSourceSHA256),leanExecution:"not_performed_by_this_suite",nativeMRS:"unavailable_not_tested",total:results.length,passed:results.filter(r=>r.pass).length,failed:results.filter(r=>!r.pass),results};
  await fs.writeFile(path.join(__dirname,"latest-report.json"),JSON.stringify(report,null,2)+"\n");
  if(process.env.REVIEW_RUN_LABEL){assert.match(process.env.REVIEW_RUN_LABEL,/^[A-Za-z0-9_.-]+$/);await fs.writeFile(path.join(__dirname,process.env.REVIEW_RUN_LABEL+".json"),JSON.stringify(report,null,2)+"\n");}
  process.stdout.write(JSON.stringify({timeUTC:report.timeUTC,total:report.total,passed:report.passed,failed:report.failed},null,2)+"\n");
  process.exitCode=report.failed.length?1:0;
}
main().catch(e=>{console.error(e);process.exitCode=1;});
