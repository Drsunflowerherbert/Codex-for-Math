"use strict";
// Real signals sent to the CLI while an actual pinned Lean process is running.
const fs=require("node:fs/promises"),path=require("node:path"),os=require("node:os"),assert=require("node:assert/strict"),{spawn}=require("node:child_process");
const {inspectReceipt}=require("./live.cjs");
const pause=ms=>new Promise(resolve=>setTimeout(resolve,ms));
async function leanPid(directory){
  for(const id of (await fs.readdir("/proc")).filter(x=>/^\d+$/.test(x))){
    try{const argv=(await fs.readFile("/proc/"+id+"/cmdline")).toString("utf8").split("\0");
      if(path.basename(argv[0])==="lean"&&argv.some(x=>x===path.join(directory,"inputs/build/EvidenceHarness.lean")))return Number(id);
    }catch(e){if(!["ENOENT","ESRCH","EACCES"].includes(e.code))throw e;}
  }return null;
}
async function main(repo){
  assert.equal(process.platform,"linux");const base=await fs.mkdtemp(path.join(os.tmpdir(),"math-live-os-signals-")),results=[];
  for(const signal of ["SIGTERM","SIGINT","SIGKILL"]){
    const directory=path.join(base,signal.toLowerCase()),stdout=[],stderr=[];
    const cli=spawn(process.execPath,[path.join(__dirname,"live.cjs"),"run","valid",repo,directory],{cwd:__dirname,shell:false,stdio:["ignore","pipe","pipe"]});
    cli.stdout.on("data",b=>stdout.push(b));cli.stderr.on("data",b=>stderr.push(b));
    let complete=false;const completion=new Promise((resolve,reject)=>{cli.once("error",reject);cli.once("close",(code,s)=>{complete=true;resolve({exitCode:code,signal:s});});});
    const started=Date.now();let actualLeanPID=null;
    while(!complete&&Date.now()-started<20000){actualLeanPID=await leanPid(directory);if(actualLeanPID)break;await pause(5);}
    try{
      assert.ok(actualLeanPID,"actual Lean process must be observed before interruption");
      const sentAt=new Date().toISOString();assert.equal(cli.kill(signal),true);const termination=await completion;
      await fs.writeFile(path.join(base,signal+".cli.stdout"),Buffer.concat(stdout));await fs.writeFile(path.join(base,signal+".cli.stderr"),Buffer.concat(stderr));
      const attempt=JSON.parse(await fs.readFile(path.join(directory,"attempt.json"),"utf8"));
      assert.equal(attempt.locallyObservedLeanPass,false);
      if(signal==="SIGKILL"){
        assert.equal(termination.signal,"SIGKILL");await assert.rejects(inspectReceipt(directory),/ENOENT/);
        results.push({signal,sentAt,actualLeanPID,termination,attempt,receipt:"absent_and_rejected",locallyObservedLeanPass:false,cleanup:"test_harness_killed_remaining_observed_process_group"});
      }else{
        assert.equal(termination.exitCode,2);const receipt=JSON.parse(await fs.readFile(path.join(directory,"receipt.json"),"utf8"));
        assert.equal(receipt.reportedOutcome,"failed_or_incomplete");const p=receipt.phases.find(p=>p.name==="compile-evidence-helper");
        assert.equal(p.termination.pid,actualLeanPID);assert.equal(p.termination.kind,"interrupted");assert.equal(p.success,false);
        const inspection=await inspectReceipt(directory);assert.equal(inspection.leanPass,false);assert.equal(inspection.integrityStatus,"failed_or_incomplete_attempt");
        results.push({signal,sentAt,actualLeanPID,termination,leanTermination:p.termination,receipt:"failed_or_incomplete",inspection,locallyObservedLeanPass:false});
      }
    }finally{
      if(!complete)cli.kill("SIGKILL");
      if(actualLeanPID){for(const s of ["SIGTERM","SIGKILL"]){try{process.kill(-actualLeanPID,s);}catch(e){if(e.code!=="ESRCH")throw e;}await pause(20);}}
    }
  }
  const report={schema:"actual-live-cli-os-interruptions/v1",runtime:process.version,platform:process.platform,base,total:results.length,passed:results.length,results,independentKernelReplay:"not_performed"};
  await fs.writeFile(path.join(__dirname,"verification/live/os-interruptions.json"),JSON.stringify(report,null,2)+"\n");console.log(JSON.stringify(report,null,2));return report;
}
if(require.main===module)main(process.argv[2]).catch(e=>{console.error(e);process.exitCode=1;});
module.exports={main};
