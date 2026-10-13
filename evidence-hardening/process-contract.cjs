"use strict";
const {need,keys,absolute,timestamp,descriptor}=require('./io.cjs');
const signals=new Set(Object.keys(require('node:os').constants.signals));
function processContract(p){
  keys(p,['name','executable','argv','cwd','environment','started','finished','durationMs','termination','success','error','outputLimitBytes','evidence'],'process');
  need(typeof p.name==='string'&&/^[A-Za-z][A-Za-z0-9_.-]{0,100}$/.test(p.name)&&typeof p.executable==='string'&&p.executable.length>0&&Array.isArray(p.argv)&&p.argv.length<=100&&p.argv.every(s=>typeof s==='string'&&!s.includes('\0'))&&absolute(p.cwd),'invalid process identity');
  keys(p.environment,['LEAN_PATH','ELAN_HOME'],'environment');
  for(const v of Object.values(p.environment))need(v===null||(typeof v==='string'&&v.length<=32768&&!v.includes('\0')),'invalid environment value');
  const start=timestamp(p.started),end=timestamp(p.finished);
  need(end>=start&&Number.isSafeInteger(p.durationMs)&&p.durationMs>=0&&Math.abs(end-start-p.durationMs)<=2000,'contradictory process times');
  need(Number.isSafeInteger(p.outputLimitBytes)&&p.outputLimitBytes>=1&&p.outputLimitBytes<=16777216,'invalid output limit');
  keys(p.termination,['kind','exitCode','signal','pid','processGroup'],'termination');
  const t=p.termination;
  need(['exited','launch_failed','log_io_failure','interrupted','timeout','output_limit'].includes(t.kind),'unsupported termination kind');
  need(t.exitCode===null||(Number.isInteger(t.exitCode)&&t.exitCode>=0&&t.exitCode<=255),'invalid exit code');
  need(t.signal===null||signals.has(t.signal),'invalid signal');
  need(t.pid===null||(Number.isSafeInteger(t.pid)&&t.pid>0),'invalid PID');
  need(t.processGroup===t.pid,'contradictory process group');
  need(!(t.exitCode!==null&&t.signal!==null),'exit code and signal cannot both be set');
  if(t.kind==='exited')need(t.pid!==null&&((t.exitCode!==null&&t.signal===null)||(t.exitCode===null&&t.signal!==null)),'exited process missing exit evidence');
  if(t.kind==='launch_failed')need(t.exitCode===null&&t.signal===null,'launch failure has exit evidence');
  const success=t.kind==='exited'&&t.exitCode===0&&t.signal===null;
  need(typeof p.success==='boolean'&&p.success===success,'contradictory process success');
  need(p.error===null||(typeof p.error==='string'&&p.error.length>0),'invalid process error');
  need((['launch_failed','log_io_failure'].includes(t.kind))===(p.error!==null),'contradictory process error');
  keys(p.evidence,['stdout','stderr'],'process evidence');
  for(const c of ['stdout','stderr']){descriptor(p.evidence[c]);need(p.evidence[c].path==='logs/'+p.name+'.'+c,'reused or misnamed process log');}
  need(p.evidence.stdout.bytes+p.evidence.stderr.bytes<=p.outputLimitBytes,'captured bytes exceed process cap');
  return {start,end,success};
}
function leanMessages(bytes){
  const {utf8,parseStrict}=require('./io.cjs');
  return utf8(bytes).split('\n').filter(l=>l.trim()).map(l=>{
    const m=parseStrict(l);need(m&&typeof m==='object'&&typeof m.data==='string'&&['information','warning','error'].includes(m.severity),'malformed Lean JSON message');
    need(m.severity!=='error','Lean error in successful process log');return m;
  });
}
function markers(messages,prefix){return messages.filter(m=>m.data.startsWith(prefix)).map(m=>{need(m.severity==='information','marker severity');return require('./io.cjs').parseStrict(m.data.slice(prefix.length));});}
module.exports={processContract,leanMessages,markers};
