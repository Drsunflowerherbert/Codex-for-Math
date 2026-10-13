"use strict";
// Self-contained actual Node/filesystem/Git tests. No Lean execution in this suite.
const fs=require('node:fs/promises'),path=require('node:path'),os=require('node:os'),assert=require('node:assert/strict');
const {execFile}=require('node:child_process'),exec=require('node:util').promisify(execFile);
const I=require('../io.cjs'),{processContract,leanMessages,markers}=require('../process-contract.cjs'),{runProcess}=require('../capture.cjs'),{checkGitSource}=require('../git-source.cjs');
const report={schema:'evidence-hardening-regression/v1',mode:'actual_Node_filesystem_Git_no_Lean',started:new Date().toISOString(),runtime:process.version,results:[]};
let root;async function test(name,f){try{const observed=await f();report.results.push({name,pass:true,observed:observed??null});}catch(e){report.results.push({name,pass:false,error:e.stack});}}
function phase(){return {name:'compile',executable:'/trusted/lean',argv:['--json'],cwd:'/trusted/work',environment:{LEAN_PATH:null,ELAN_HOME:null},started:'2026-10-13T01:00:00.000Z',finished:'2026-10-13T01:00:00.001Z',durationMs:1,termination:{kind:'exited',exitCode:0,signal:null,pid:1,processGroup:1},success:true,error:null,outputLimitBytes:4194304,evidence:{stdout:{path:'logs/compile.stdout',bytes:0,sha256:I.sha('')},stderr:{path:'logs/compile.stderr',bytes:0,sha256:I.sha('')}}};}
async function main(){
  root=await fs.mkdtemp(path.join(os.tmpdir(),'evidence-hardening-regression-'));
  await test('well_formed_process',()=>processContract(phase()));
  const mutations={exit_code_string:p=>p.termination.exitCode='0',exit_code_negative:p=>p.termination.exitCode=-2,signal_and_exit:p=>p.termination.signal='SIGTERM',pid_negative:p=>p.termination.pid=p.termination.processGroup=-1,process_group_mismatch:p=>p.termination.processGroup=2,error_on_success:p=>p.error='contradiction',duration_negative:p=>p.durationMs=-1,clock_reversed:p=>p.finished='2026-10-12T01:00:00.000Z',invalid_timestamp:p=>p.started='yesterday',noncanonical_timestamp:p=>p.started='2026-10-13',duration_contradiction:p=>p.durationMs=3000,output_cap_negative:p=>p.outputLimitBytes=-1,bytes_exceed_cap:p=>p.evidence.stdout.bytes=4194305,environment_shape:p=>p.environment='wrong',environment_extra:p=>p.environment.command='wrong',environment_value:p=>p.environment.LEAN_PATH=13,reused_channel:p=>p.evidence.stderr.path=p.evidence.stdout.path,extra_descriptor:p=>p.evidence.stdout.authentic=true,wrong_success:p=>p.success=false,unknown_termination:p=>p.termination.kind='passed',missing_exit:p=>p.termination.exitCode=null};
  for(const [name,mutate] of Object.entries(mutations))await test('reject_'+name,()=>{const p=phase();mutate(p);assert.throws(()=>processContract(p));});
  for(const [name,s] of Object.entries({duplicate_key:'{"a":1,"a":2}',decoded_duplicate:'{"a":1,"\\u0061":2}',nonfinite:'1e999',unpaired_surrogate:'"\\ud800"',prototype_key:'{"__proto__":1}',trailing:'{}{}'}))await test('strict_json_'+name,()=>assert.throws(()=>I.parseStrict(s)));
  const msg=JSON.stringify({severity:'information',data:'MATH_EVIDENCE_TARGET {"target":"Fixture.valid"}'})+'\n';
  await test('lean_marker_parse',()=>assert.equal(markers(leanMessages(Buffer.from(msg)),'MATH_EVIDENCE_TARGET ')[0].target,'Fixture.valid'));
  for(const [name,b] of Object.entries({error:Buffer.from('{"severity":"error","data":"failed"}\n'),truncated:Buffer.from('{'),text:Buffer.from('Build succeeded'),duplicate:Buffer.from('{"severity":"information","severity":"error","data":"hidden"}'),utf8:Buffer.from([0xff])}))await test('reject_lean_log_'+name,()=>assert.throws(()=>leanMessages(b)));
  const ioRoot=path.join(root,'io');await fs.mkdir(ioRoot);await fs.writeFile(path.join(ioRoot,'good'),'safe');const read=await I.reader(ioRoot);
  await test('regular_read',async()=>assert.equal(I.utf8(await read('good')),'safe'));
  await test('reject_path_escape',()=>assert.rejects(()=>read('../good')));
  await test('reject_size',()=>assert.rejects(()=>read('good',1)));
  await fs.symlink('good',path.join(ioRoot,'alias'));await test('reject_symlink',()=>assert.rejects(()=>read('alias')));
  await fs.link(path.join(ioRoot,'good'),path.join(ioRoot,'shared'));await test('reject_hardlink',()=>assert.rejects(()=>read('shared')));
  await exec('/usr/bin/mkfifo',[path.join(ioRoot,'pipe')]);await test('reject_FIFO_without_blocking',async()=>{const started=Date.now();await assert.rejects(()=>read('pipe'));assert.ok(Date.now()-started<1000);});
  await test('actual_capture_success',async()=>{const d=path.join(root,'capture-success');await fs.mkdir(d);const p=await runProcess(process.execPath,['-e','process.stdout.write("captured")'],{directory:d,cwd:d,name:'observed'});processContract(p);assert.equal(p.success,true);assert.equal(p.evidence.stdout.bytes,8);return p.termination;});
  await test('actual_capture_nonzero',async()=>{const d=path.join(root,'capture-failure');await fs.mkdir(d);const p=await runProcess(process.execPath,['-e','process.exit(7)'],{directory:d,cwd:d,name:'observed'});processContract(p);assert.equal(p.success,false);assert.equal(p.termination.exitCode,7);return p.termination;});
  await test('actual_capture_launch_failure',async()=>{const d=path.join(root,'capture-launch');await fs.mkdir(d);const p=await runProcess('/no/such/evidence-executable',[],{directory:d,cwd:d,name:'observed'});processContract(p);assert.equal(p.termination.kind,'launch_failed');assert.equal(p.termination.exitCode,null);return p.termination;});
  await test('actual_capture_timeout',async()=>{const d=path.join(root,'capture-timeout');await fs.mkdir(d);const p=await runProcess(process.execPath,['-e','setInterval(()=>{},1000)'],{directory:d,cwd:d,name:'observed',timeoutMs:100});processContract(p);assert.equal(p.success,false);assert.equal(p.termination.kind,'timeout');return p.termination;});
  const gitRoot=path.join(root,'git');await fs.mkdir(gitRoot);const git=async args=>(await exec('/usr/bin/git',args,{cwd:gitRoot})).stdout.trim();
  await git(['init','-q']);await fs.writeFile(path.join(gitRoot,'Dependency.lean'),'def audited : Nat := 1\n');await fs.writeFile(path.join(gitRoot,'.gitignore'),'.lake/\n');await git(['add','.']);const commit=async()=>git(['-c','user.name=Evidence Regression','-c','user.email=regression@example.invalid','commit','-q','-m','fixture']);await commit();const first=await git(['rev-parse','HEAD']);
  await test('git_clean_byte_identity',async()=>{const r=await checkGitSource(gitRoot,first);assert.equal(r.ok,true);assert.equal(r.leanPass,false);return {files:r.files.length,sourceClosureSHA256:r.sourceClosureSHA256};});
  for(const flag of ['assume-unchanged','skip-worktree']){
    await git(['update-index','--'+flag,'Dependency.lean']);await fs.writeFile(path.join(gitRoot,'Dependency.lean'),'def audited : Nat := 2\n');
    await test('git_hidden_modification_'+flag,async()=>{assert.equal(await git(['-c','core.fsmonitor=false','diff','--no-ext-diff','--no-textconv','--exit-code','HEAD','--']),'');await assert.rejects(()=>checkGitSource(gitRoot,first),/tracked source bytes differ/);});
    await fs.writeFile(path.join(gitRoot,'Dependency.lean'),'def audited : Nat := 1\n');await git(['update-index','--no-'+flag,'Dependency.lean']);
  }
  await fs.writeFile(path.join(gitRoot,'Dependency.lean'),'def audited : Nat := 2\n');await git(['add','.']);await commit();const replacement=await git(['rev-parse','HEAD']);await git(['replace',first,replacement]);await git(['reset','--soft',first]);
  await test('git_replacement_ref_rejected',()=>assert.rejects(()=>checkGitSource(gitRoot,first),/tracked source bytes differ/));
  await git(['replace','-d',first]);await git(['reset','--hard',first]);await fs.writeFile(path.join(gitRoot,'Shadow.lean'),'def shadow : Nat := 3\n');
  await test('git_untracked_import_rejected',()=>assert.rejects(()=>checkGitSource(gitRoot,first),/untracked Lean import/));
  report.finished=new Date().toISOString();report.total=report.results.length;report.passed=report.results.filter(r=>r.pass).length;report.failed=report.results.filter(r=>!r.pass);report.leanPasses=0;report.root=root;
  if(process.argv[2])await fs.writeFile(process.argv[2],JSON.stringify(report,null,2)+'\n',{flag:'wx'});console.log(JSON.stringify(report,null,2));process.exitCode=report.failed.length?1:0;
}
main().catch(e=>{console.error(e);process.exitCode=1;});
