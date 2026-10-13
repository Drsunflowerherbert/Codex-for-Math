"use strict";
const fs=require('node:fs/promises'),path=require('node:path');
const I=require('./io.cjs'),{need,keys,sha,canonicalJSON:C,reader,json,artifact,timestamp}=I;
const {runProcess}=require('./capture.cjs');
const {processContract,leanMessages,markers}=require('./process-contract.cjs');
const {MEMBERS,COMMIT,targets,definitions}=require('./inspect-v1.cjs');
const NORMAL=[{name:'EvidenceFixture.valid',kind:'theorem'},{name:'EvidenceFixture.identity',kind:'theorem'},{name:'EvidenceFixture.conditional',kind:'theorem'},{name:'EvidenceFixture.predicate',kind:'definition'},{name:'EvidenceFixture.answer',kind:'definition'}];
const LABELS=['valid','hidden-assumption','statement-drift','specialization','definition-substitution','transitive-drift','wrong-name','sorry','custom-axiom','skip-kernel'];
const SOURCE_NAMES=['fixture-gate.cjs','capture.cjs','io.cjs','process-contract.cjs','inspect-v1.cjs','baseline.json','vendor/strict-json.cjs','vendor/live-plans.cjs','lean/EvidenceHarness.lean','lean/Dependency.lean','lean/ExpectedTypes.lean','lean/SpecializedTypes.lean','lean/ExpectedDefinitions.lean','lean/Replay.lean','lean/BadTypes.lean','lean/BadReplay.lean','lean/lean-toolchain',...['valid','hidden-assumption','statement-drift','definition-substitution','transitive-drift','wrong-name','sorry','custom-axiom','skip-kernel'].map(l=>'lean/cases/'+l+'.lean')].sort();
function recipe(label){
  need(LABELS.includes(label),'unsupported fixed fixture');const bad=['sorry','custom-axiom','skip-kernel'].includes(label);
  return {label,dependency:label==='transitive-drift'?'lean/cases/transitive-drift.lean':'lean/Dependency.lean',fixture:'lean/cases/'+(['specialization','transitive-drift'].includes(label)?'valid':label)+'.lean',types:bad?'lean/BadTypes.lean':label==='specialization'?'lean/SpecializedTypes.lean':'lean/ExpectedTypes.lean',definitions:bad?null:'lean/ExpectedDefinitions.lean',replay:bad?'lean/BadReplay.lean':'lean/Replay.lean',targets:bad?[{name:'EvidenceFixture.incomplete',kind:'theorem'}]:NORMAL};
}
function equal(a,b,m){need(C(a)===C(b),m);}
async function sources(){
  const read=await reader(__dirname),policy=await json(read,'fixture-policy.json');keys(policy,['schema','compilerCommit','files'],'fixture policy');need(policy.schema==='fixed-evidence-fixtures/v1'&&policy.compilerCommit===COMMIT,'unsupported fixture policy');
  need(Array.isArray(policy.files),'policy files');equal(policy.files.map(f=>f.path).sort(),SOURCE_NAMES,'fixed source closure coverage');
  const data=new Map(),entries=[];for(const d of policy.files){data.set(d.path,await artifact(read,d));entries.push(d);}
  need(policy.files.find(f=>f.path==='lean/EvidenceHarness.lean').sha256===require('./baseline.json').toolkit['lean/EvidenceHarness.lean'].sha256,'helper differs from reviewed original');
  const b=await read('fixture-policy.json');data.set('fixture-policy.json',b);entries.push({path:'fixture-policy.json',bytes:b.length,sha256:sha(b)});
  return {entries,data,digest:sha(C(entries)),policy};
}
async function hashFile(p){
  const pre=await fs.lstat(p);need(pre.isFile()&&pre.size<=268435456,'nonregular release member');
  const h=await fs.open(p,require('node:fs').constants.O_RDONLY|require('node:fs').constants.O_NOFOLLOW|require('node:fs').constants.O_NONBLOCK);
  try{const s=await h.stat();need(s.isFile()&&s.size<=268435456,'unsupported release member');const crypto=require('node:crypto'),hash=crypto.createHash('sha256');for await(const b of h.createReadStream({autoClose:false}))hash.update(b);const after=await h.stat();need(after.size===s.size&&after.mtimeMs===s.mtimeMs&&after.ctimeMs===s.ctimeMs,'release member changed');return {path:p,bytes:s.size,sha256:hash.digest('hex')};}finally{await h.close();}
}
async function compilerIdentity(binary){
  const lean=await fs.realpath(binary),lib=path.resolve(path.dirname(lean),'../lib/lean'),members=[];
  for(const n of Object.keys(MEMBERS)){const m=await hashFile(n==='lean'?lean:path.join(lib,n));need(m.bytes===MEMBERS[n].bytes&&m.sha256===MEMBERS[n].sha256,'official selected compiler member differs: '+n);members.push(m);}
  return {path:lean,lib,commit:COMMIT,members,coreOLeanTrust:'trusted_existing_core_cache_not_rebuilt'};
}
function bindings(p){return [{source:'lean/EvidenceHarness.lean',destination:'EvidenceHarness.lean',module:'EvidenceHarness',phase:'compile-helper'},{source:p.dependency,destination:'Dependency.lean',module:'Dependency',phase:'compile-dependency'},{source:p.fixture,destination:'Fixture.lean',module:'Fixture',phase:'compile-fixture'},{source:p.types,destination:'ExpectedTypes.lean',module:'ExpectedTypes',phase:'whole-type-and-axiom-audit'},...(p.definitions?[{source:p.definitions,destination:'ExpectedDefinitions.lean',module:'ExpectedDefinitions',phase:'definition-body-audit'}]:[]),{source:p.replay,destination:'Replay.lean',module:'Replay',phase:'same-kernel-replay'}];}
function checkReplay(rs,p){
  need(rs.length===1,'replay marker coverage');const r=rs[0];keys(r,['scope','baseModules','targets','replayedDeclarations','independentKernelReplay'],'fixture replay');
  equal(r.baseModules,['Init','EvidenceHarness'],'fixture replay bases');equal(r.targets,p.targets.map(t=>t.name),'fixture replay targets');need(r.scope==='local_declaration_closure_same_kernel_imported_dependency_baseline'&&r.independentKernelReplay==='not_performed'&&Number.isSafeInteger(r.replayedDeclarations)&&r.replayedDeclarations>=p.targets.length,'fixture replay contract');
}
const boundaries={importedReceiptCanGrantPass:false,receiptAuthenticity:'not_established',independentKernelReplay:'not_performed',nativeMRS:'unavailable_unvalidated',coreDependencies:'trusted_existing_core_olean_cache',mathlib:'not_used_by_fixed_fixtures',arbitraryImports:'unsupported',assumptionCompleteness:'fixed_harness_scope_only'};
async function run(label,binary,output,options={}){
  need(process.platform==='linux','fixed live fixtures support Linux only');need(Object.keys(options).every(k=>['signal','timeoutMs'].includes(k)),'unsupported runner options');need(options.timeoutMs===undefined||(Number.isInteger(options.timeoutMs)&&options.timeoutMs>=1&&options.timeoutMs<=300000),'invalid fixture timeout');
  const plan=recipe(label),before=await sources(),directory=path.resolve(output),parent=path.dirname(directory);need(await fs.realpath(parent)===parent,'output parent alias');need(!directory.startsWith(__dirname+path.sep),'keep attempts outside companion');
  await fs.mkdir(directory);const attempt=require('node:crypto').randomUUID(),started=new Date().toISOString();
  const initial={schema:'fixture-attempt/v1',attempt,label,started,state:'in_progress',locallyObservedLeanPass:false};await fs.writeFile(path.join(directory,'attempt.json'),C(initial)+'\n',{flag:'wx'});
  const phases=[],products=[],workFiles=[],records={targets:[],definitions:[],replay:[]};let compiler=null,failure=null,closureUnchanged=false;
  async function write(p,b){await fs.mkdir(path.dirname(path.join(directory,p)),{recursive:true});await fs.writeFile(path.join(directory,p),b,{flag:'wx'});return {path:p,bytes:b.length,sha256:sha(b)};}
  const sourceFiles=[];for(const [p,b] of before.data)sourceFiles.push(await write('inputs/source/'+p,b));
  const work=path.join(directory,'inputs/build'),cache=path.join(directory,'cache');await fs.mkdir(cache);const bs=bindings(plan);
  for(const b of bs)workFiles.push(await write('inputs/build/'+b.destination,before.data.get(b.source)));
  const step=async(name,args,cwd,env)=>{need(!options.signal?.aborted,'attempt interrupted before '+name);const p=await runProcess(compiler.path,args,{cwd,directory,name,env,signal:options.signal,timeoutMs:options.timeoutMs||300000});phases.push(p);processContract(p);need(p.success,'phase '+name+' failed: '+p.termination.kind);const read=await reader(directory);need((await artifact(read,p.evidence.stderr)).length===0,'unexpected compiler stderr');return artifact(read,p.evidence.stdout);};
  try{
    compiler=await compilerIdentity(binary);const env={PATH:'/usr/bin:/bin',LEAN_PATH:[cache,compiler.lib].join(path.delimiter)};
    const version=I.utf8(await step('compiler-version',['--version'],work,env)).trim();need(version.includes('version 4.24.0,')&&version.includes('commit '+COMMIT),'compiler version mismatch');compiler.version=version;
    need(I.utf8(await step('compiler-commit',['--githash'],work,env)).trim()===COMMIT,'compiler commit mismatch');
    for(const b of bs){const product='cache/'+b.module+'.olean';const output=await step(b.phase,['--json','--root='+work,'-o',path.join(directory,product),path.join(work,b.destination)],work,env),messages=leanMessages(output);const read=await reader(directory),bytes=await read(product);products.push({path:product,bytes:bytes.length,sha256:sha(bytes)});
      if(b.phase==='whole-type-and-axiom-audit'){records.targets=markers(messages,'MATH_EVIDENCE_TARGET ');targets(records.targets,plan);}
      if(b.phase==='definition-body-audit'){records.definitions=markers(messages,'MATH_EVIDENCE_DEFINITION ');definitions(records.definitions,plan);}
      if(b.phase==='same-kernel-replay'){records.replay=markers(messages,'MATH_EVIDENCE_REPLAY ');checkReplay(records.replay,plan);}
    }
  }catch(e){failure=e.message;}
  try{
    if(compiler)equal((await compilerIdentity(binary)).members,compiler.members,'compiler bytes changed during run');
    equal((await sources()).entries,before.entries,'reviewed source closure changed during run');
    const read=await reader(directory);for(const d of [...sourceFiles,...workFiles,...products,...phases.flatMap(p=>Object.values(p.evidence))])await artifact(read,d);closureUnchanged=true;
  }catch(e){failure=failure||e.message;}
  if(options.signal?.aborted)failure=failure||'attempt interrupted';
  const ok=failure===null&&phases.length===bs.length+2&&phases.every(p=>p.success)&&records.replay.length===1;
  const receipt={schema:'fixed-fixture-receipt/v1',attempt,plan:label,started,finished:new Date().toISOString(),runDirectory:directory,reportedOutcome:ok?'all_fixed_fixture_gates_succeeded':'failed_or_incomplete',failure,sourceDigest:before.digest,sourceFiles,workFiles,products,compiler,phases,records,boundaries};
  await fs.writeFile(path.join(directory,'receipt.json'),C(receipt)+'\n',{flag:'wx'});
  // Only the new, observed execution can supply this positive fixture result.
  const targetCompilationObserved=['compile-helper','compile-dependency','compile-fixture'].every(n=>phases.find(p=>p.name===n)?.success&&products.some(p=>p.path==='cache/'+bs.find(b=>b.phase===n).module+'.olean'));
  return {ok,locallyObservedLeanPass:ok,verifiedBuild:closureUnchanged&&targetCompilationObserved,targetCompilationObserved,formalProofScope:ok?'fixed_fixture_targets_with_exact_harnesses':'not_accepted',conditionalTheorems:ok?['EvidenceFixture.identity requires h : n = 2','EvidenceFixture.conditional requires h : predicate; predicate is False; no proof of False is asserted']:[],independentKernelReplay:'not_performed',dependencyTrust:'core_olean_cache_not_rebuilt',mathlib:'not_used',directory,failure,failedPhase:phases.find(p=>!p.success)?.name||null,receipt};
}
async function inspect(directory){
  const read=await reader(directory),r=await json(read,'receipt.json'),current=await sources();
  keys(r,['schema','attempt','plan','started','finished','runDirectory','reportedOutcome','failure','sourceDigest','sourceFiles','workFiles','products','compiler','phases','records','boundaries'],'fixture receipt');
  need(r.schema==='fixed-fixture-receipt/v1'&&r.reportedOutcome==='all_fixed_fixture_gates_succeeded'&&r.failure===null,'incomplete fixture receipt cannot be accepted as complete');const plan=recipe(r.plan);
  need(/^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$/.test(r.attempt)&&I.absolute(r.runDirectory),'fixture identity');const started=timestamp(r.started),finished=timestamp(r.finished);need(finished>=started,'fixture chronology');
  equal(await json(read,'attempt.json'),{schema:'fixture-attempt/v1',attempt:r.attempt,label:r.plan,started:r.started,state:'in_progress',locallyObservedLeanPass:false},'fixture attempt binding');equal(r.boundaries,boundaries,'fixture boundaries');need(r.sourceDigest===current.digest,'stale fixture source commitment');
  equal(r.sourceFiles,current.entries.map(d=>({...d,path:'inputs/source/'+d.path})),'fixture source closure');
  const bs=bindings(plan),work=path.join(r.runDirectory,'inputs/build'),cache=path.join(r.runDirectory,'cache');
  need(Array.isArray(r.workFiles)&&r.workFiles.length===bs.length&&Array.isArray(r.products)&&r.products.length===bs.length&&Array.isArray(r.phases)&&r.phases.length===bs.length+2,'fixture artifact/phase count');
  for(const p of r.phases)processContract(p);
  const descriptors=[...r.sourceFiles,...r.workFiles,...r.products,...r.phases.flatMap(p=>Object.values(p.evidence))];let total=0;for(const d of descriptors){I.descriptor(d);total+=d.bytes;}need(total<=67108864,'fixture artifacts exceed 64 MiB');
  const seen=new Set(),bytes=new Map();for(const d of descriptors){need(!seen.has(d.path),'duplicate fixture artifact');seen.add(d.path);bytes.set(d.path,await artifact(read,d));}
  equal(r.workFiles,bs.map(b=>{const s=current.entries.find(s=>s.path===b.source);return {...s,path:'inputs/build/'+b.destination};}),'fixture work bindings');equal(r.products.map(d=>d.path),bs.map(b=>'cache/'+b.module+'.olean'),'fixture products');
  keys(r.compiler,['path','lib','commit','members','coreOLeanTrust','version'],'fixture compiler');need(I.absolute(r.compiler.path)&&r.compiler.lib===path.resolve(path.dirname(r.compiler.path),'../lib/lean')&&r.compiler.commit===COMMIT&&r.compiler.coreOLeanTrust==='trusted_existing_core_cache_not_rebuilt'&&typeof r.compiler.version==='string'&&r.compiler.version.includes('version 4.24.0,')&&r.compiler.version.includes(COMMIT),'fixture compiler identity');
  need(Array.isArray(r.compiler.members)&&r.compiler.members.length===5,'release member coverage');for(const [i,n] of Object.keys(MEMBERS).entries()){const m=r.compiler.members[i];keys(m,['path','bytes','sha256'],'release member');need(m.path===(n==='lean'?r.compiler.path:path.join(r.compiler.lib,n))&&m.bytes===MEMBERS[n].bytes&&m.sha256===MEMBERS[n].sha256,'release member differs from pin');}
  equal(r.phases.map(p=>p.name),['compiler-version','compiler-commit',...bs.map(b=>b.phase)],'fixture phase coverage');const env={LEAN_PATH:[cache,r.compiler.lib].join(path.delimiter),ELAN_HOME:null};let previous=started;
  for(let i=0;i<r.phases.length;i++){const p=r.phases[i],t=processContract(p);need(t.success&&t.start>=previous&&t.end<=finished,'fixture process chronology');previous=t.end;need(p.executable===r.compiler.path&&p.cwd===work&&p.outputLimitBytes===4194304,'fixture command identity');equal(p.environment,env,'fixture environment');
    equal(p.argv,i===0?['--version']:i===1?['--githash']:['--json','--root='+work,'-o',path.join(cache,bs[i-2].module+'.olean'),path.join(work,bs[i-2].destination)],'fixture argv');need(bytes.get(p.evidence.stderr.path).length===0,'fixture stderr');const out=bytes.get(p.evidence.stdout.path);if(i===0)need(I.utf8(out).trim()===r.compiler.version,'fixture version log');else if(i===1)need(I.utf8(out).trim()===COMMIT,'fixture commit log');else leanMessages(out);
  }
  keys(r.records,['targets','definitions','replay'],'fixture records');const messages=name=>leanMessages(bytes.get(r.phases.find(p=>p.name===name).evidence.stdout.path));
  const ts=markers(messages('whole-type-and-axiom-audit'),'MATH_EVIDENCE_TARGET ');targets(ts,plan);equal(ts,r.records.targets,'fixture target records');
  const ds=plan.definitions?markers(messages('definition-body-audit'),'MATH_EVIDENCE_DEFINITION '):[];if(plan.definitions)definitions(ds,plan);equal(ds,r.records.definitions,'fixture definition records');
  const rs=markers(messages('same-kernel-replay'),'MATH_EVIDENCE_REPLAY ');checkReplay(rs,plan);equal(rs,r.records.replay,'fixture replay records');
  return {ok:true,kind:'fixed_fixture_reported_integrity_only',leanPass:false,locallyObservedLeanPass:false,freshness:'not_established',receiptAuthenticity:'not_established',independentKernelReplay:'not_performed',dependencyTrust:'core_olean_cache_not_rebuilt'};
}
async function main(args){if(args[0]==='inspect'&&args.length===2)return inspect(args[1]);if(args[0]==='run'&&args.length===4){const abort=new AbortController(),onSignal=()=>abort.abort();process.on('SIGTERM',onSignal);process.on('SIGINT',onSignal);try{const r=await run(args[1],args[2],args[3],{signal:abort.signal});if(!r.ok)process.exitCode=2;return {...r,receipt:undefined};}finally{process.removeListener('SIGTERM',onSignal);process.removeListener('SIGINT',onSignal);}}throw new Error('Usage: node fixture-gate.cjs run FIXED_LABEL OFFICIAL_LEAN NEW_DIRECTORY | inspect DIRECTORY');}
if(require.main===module)main(process.argv.slice(2)).then(r=>console.log(JSON.stringify(r,null,2))).catch(e=>{console.error(JSON.stringify({ok:false,locallyObservedLeanPass:false,error:e.message}));process.exitCode=2;});
module.exports={run,inspect,recipe,sources,SOURCE_NAMES,LABELS,compilerIdentity};
