"use strict";
const assert=require("node:assert/strict");
const fs=require("node:fs/promises");
const path=require("node:path");
const os=require("node:os");
const {runProcess}=require("./process.cjs");
async function main() {
  const directory=await fs.mkdtemp(path.join(os.tmpdir(),"math-process-tests-")),results=[];
  const run=(name,code,options={})=>runProcess(process.execPath,["-e",code],{cwd:directory,directory,name,...options});
  let r=await run("valid","process.stdout.write('out');process.stderr.write('err')");
  assert.equal(r.success,true);assert.equal(r.evidence.stdout.bytes,3);assert.equal(r.evidence.stderr.bytes,3);results.push(r);
  r=await run("nonzero","process.stdout.write('partial');process.exitCode=7");assert.equal(r.success,false);assert.equal(r.termination.exitCode,7);results.push(r);
  r=await run("timeout","process.stdout.write('started');setInterval(()=>{},1000)",{timeoutMs:200});assert.equal(r.success,false);assert.equal(r.termination.kind,"timeout");assert.ok(r.evidence.stdout.bytes>0);results.push(r);
  const controller=new AbortController();setTimeout(()=>controller.abort(),200);
  r=await run("interrupt","process.stdout.write('started');setInterval(()=>{},1000)",{signal:controller.signal});assert.equal(r.success,false);assert.equal(r.termination.kind,"interrupted");results.push(r);
  r=await run("outputlimit","process.stdout.write('x'.repeat(200000));setInterval(()=>{},1000)",{maxOutputBytes:1024});assert.equal(r.success,false);assert.equal(r.termination.kind,"output_limit");assert.ok(r.evidence.stdout.bytes<=1024);results.push(r);
  r=await runProcess(path.join(directory,"absent-executable"),[],{cwd:directory,directory,name:"launchfail"});assert.equal(r.success,false);assert.equal(r.termination.kind,"launch_failed");results.push(r);
  const already=new AbortController();already.abort();r=await run("alreadyaborted","throw Error('never launched')",{signal:already.signal});assert.equal(r.success,false);assert.equal(r.termination.pid,null);results.push(r);
  const childCode="process.on('SIGTERM',()=>{});process.stdout.write('child '+process.pid+'\\n');setInterval(()=>{},1000)";
  const parentCode="const {spawn}=require('node:child_process');spawn(process.execPath,['-e',"+JSON.stringify(childCode)+"],{stdio:['ignore','inherit','inherit']});process.stdout.write('parent '+process.pid+'\\n');setInterval(()=>{},1000)";
  r=await run("descendants",parentCode,{timeoutMs:400});assert.equal(r.success,false);assert.equal(r.termination.kind,"timeout");
  const text=await fs.readFile(path.join(directory,r.evidence.stdout.path),"utf8"),childPID=Number(/child (\d+)/.exec(text)?.[1]);assert.ok(childPID>0);
  let alive=true;try{process.kill(childPID,0);}catch(e){if(e.code==="ESRCH")alive=false;else throw e;}
  if(alive){const status=await fs.readFile('/proc/'+childPID+'/status','utf8');assert.match(status,/State:\s+Z/);}
  r.descendantTermination=alive?"terminated_zombie_waiting_for_host_reaper":"absent";results.push(r);
  const report={schema:"actual-process-tests/v1",runtime:process.version,platform:process.platform,directory,total:results.length,passed:results.length,results};
  await fs.writeFile(path.join(__dirname,"verification/live/process-tests.json"),JSON.stringify(report,null,2)+"\n");
  console.log(JSON.stringify({total:report.total,passed:report.passed,directory},null,2));
}
main().catch(e=>{console.error(e);process.exitCode=1;});
