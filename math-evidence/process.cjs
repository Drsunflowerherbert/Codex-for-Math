"use strict";
const fs=require("node:fs/promises");
const path=require("node:path");
const crypto=require("node:crypto");
const {spawn}=require("node:child_process");
const {readRegular}=require("./cli.cjs");
const hash=b=>crypto.createHash("sha256").update(b).digest("hex");

// Only the trusted live runner and its process tests call this module. The v1
// exchange importer never calls it or supplies executable/argv/Lean expressions.
async function runProcess(executable,argv,options) {
  const {cwd,directory,name,env=process.env,signal,timeoutMs=300000,maxOutputBytes=4194304}=options;
  if(!/^[A-Za-z][A-Za-z0-9_.-]{0,100}$/.test(name)||!Number.isInteger(timeoutMs)||timeoutMs<1||timeoutMs>900000||
     !Number.isInteger(maxOutputBytes)||maxOutputBytes<1||maxOutputBytes>16777216)
    throw new Error("invalid process capture options");
  if(process.platform!=="linux"&&process.platform!=="darwin")throw new Error("process group capture requires a Unix host");
  await fs.mkdir(path.join(directory,"logs"),{recursive:true});
  const relative={stdout:"logs/"+name+".stdout",stderr:"logs/"+name+".stderr"};
  const handles={};
  try {
    handles.stdout=await fs.open(path.join(directory,relative.stdout),"wx");
    handles.stderr=await fs.open(path.join(directory,relative.stderr),"wx");
  } catch(e) {for(const h of Object.values(handles))await h.close();throw e;}
  const started=new Date().toISOString(),clock=performance.now();
  let child,reason=null,launchError=null,writeError=null,total=0,queue=Promise.resolve(),escalation=Promise.resolve();
  let exitCode=null,exitSignal=null;
  const stop=kind=>{
    if(reason)return;
    reason=kind;
    if(!child?.pid)return;
    const kill=s=>{try{process.kill(-child.pid,s);}catch(e){if(e.code!=="ESRCH")writeError=String(e.message);}};
    kill("SIGTERM");
    // Escalate even if the leader exits first: descendants can close inherited
    // pipes and continue running. The whole process group is cancelled.
    escalation=new Promise(resolve=>setTimeout(()=>{kill("SIGKILL");resolve();},200));
  };
  const accept=(channel,data)=>{
    const allowed=Math.max(0,maxOutputBytes-total),bytes=data.subarray(0,allowed);
    total+=bytes.length;
    queue=queue.then(()=>handles[channel].writeFile(bytes)).catch(e=>{writeError=String(e.message);stop("log_io_failure");});
    if(data.length>allowed)stop("output_limit");
  };
  const onAbort=()=>stop("interrupted");let timer;
  try {
    if(signal?.aborted)reason="interrupted";
    else {
      child=spawn(executable,argv,{cwd,env,shell:false,detached:true,stdio:["ignore","pipe","pipe"]});
      child.stdout.on("data",b=>accept("stdout",b));child.stderr.on("data",b=>accept("stderr",b));
      signal?.addEventListener("abort",onAbort,{once:true});
      if(signal?.aborted)onAbort();
      timer=setTimeout(()=>stop("timeout"),timeoutMs);
      await new Promise(resolve=>{
        child.once("error",e=>{launchError=String(e.message);});
        child.once("close",(code,s)=>{exitCode=code;exitSignal=s;resolve();});
      });
    }
  } catch(e){launchError=String(e.message);}
  finally {
    clearTimeout(timer);signal?.removeEventListener("abort",onAbort);
    await escalation;await queue;
    for(const h of Object.values(handles))await h.close();
  }
  const evidence={};
  for(const channel of ["stdout","stderr"]) {
    const bytes=await readRegular(path.join(directory,relative[channel]),maxOutputBytes);
    evidence[channel]={path:relative[channel],bytes:bytes.length,sha256:hash(bytes)};
  }
  const kind=launchError?"launch_failed":writeError?"log_io_failure":reason||"exited";
  return {name,executable,argv:argv.slice(),cwd,environment:{LEAN_PATH:env.LEAN_PATH||null,ELAN_HOME:env.ELAN_HOME||null},
    started,finished:new Date().toISOString(),durationMs:Math.round(performance.now()-clock),
    termination:{kind,exitCode,signal:exitSignal,pid:child?.pid||null,processGroup:child?.pid||null},
    success:kind==="exited"&&exitCode===0&&exitSignal===null,
    error:launchError||writeError||null,outputLimitBytes:maxOutputBytes,evidence};
}
module.exports={runProcess};
