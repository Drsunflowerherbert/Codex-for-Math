"use strict";
// A stricter integrity-only migration gate. Never executes imported argv.
const path=require('node:path');
const I=require('./io.cjs'),{need,keys,sha,reader,json,artifact,canonicalJSON:C,timestamp,absolute}=I;
const {processContract,leanMessages,markers}=require('./process-contract.cjs');
const {PLANS}=require('./vendor/live-plans.cjs'),baseline=require('./baseline.json');
const CODE=['live.cjs','live-plans.cjs','process.cjs','cli.cjs','bounded-io.cjs','hash-io.cjs','materialize.cjs','core.cjs','strict-json.cjs','bundle.cjs','tangent-pins.cjs','samples/catalog.json'];
const COMMIT='797c613eb9b6d4ec95db23e3e00af9ac6657f24b';
const MEMBERS={lean:{bytes:9024,sha256:'8fadc3ed92cc9decb94c96ee9c0876e91e03a3a5e69138f32114f02789e2766c'},'libleanshared.so':{bytes:193479936,sha256:'8cc9858cc57c52015ba6dd948bdbf7f05926b9b5fcead69a964f0ad61ddd79dd'},'libleanshared_1.so':{bytes:6232,sha256:'6ce912e300ad305bb38a362404544602e2229d072b78d75b1dd71c637e453c2c'},'libleanshared_2.so':{bytes:6232,sha256:'6ce912e300ad305bb38a362404544602e2229d072b78d75b1dd71c637e453c2c'},'libInit_shared.so':{bytes:6232,sha256:'6ce912e300ad305bb38a362404544602e2229d072b78d75b1dd71c637e453c2c'}};
const AXIOMS=['propext','Classical.choice','Quot.sound'];
function equal(a,b,m){need(C(a)===C(b),m);}
function member(v,n){need(v&&v.bytes===MEMBERS[n].bytes&&v.sha256===MEMBERS[n].sha256,'release member mismatch: '+n);}
function axioms(a){need(Array.isArray(a)&&new Set(a).size===a.length&&a.every(x=>AXIOMS.includes(x)),'unsupported axioms');}
function targets(rs,plan){
  need(Array.isArray(rs)&&rs.length===plan.targets.length,'target coverage');const seen=new Set();
  for(const r of rs){keys(r,['target','declarationKind','typeMatching','axioms','observedType','targetKernelReplay'],'target');const t=plan.targets.find(t=>t.name===r.target);need(t&&!seen.has(r.target),'duplicate/unexpected target');seen.add(r.target);
    need(r.declarationKind===(t.kind==='theorem'?'theorem':'definition')&&r.typeMatching==='closed_whole_type_kernel_definitional_equality'&&typeof r.observedType==='string'&&r.observedType.length>0&&r.targetKernelReplay==='separate_phase_required','target contract');axioms(r.axioms);}
}
function definitions(rs,plan){
  need(Array.isArray(rs),'definition array');equal(rs.map(r=>r.target).sort(),plan.targets.filter(t=>t.kind!=='theorem').map(t=>t.name).sort(),'definition coverage');
  for(const r of rs){keys(r,['target','definitionBodyMatching','axioms','status'],'definition');need(r.definitionBodyMatching==='kernel_definitional_equality'&&r.status==='definition_value_matched_not_a_proof_of_the_predicate','definition contract');axioms(r.axioms);}
}
function replay(rs,plan){
  need(Array.isArray(rs)&&rs.length===1,'replay coverage');const r=rs[0];keys(r,['scope','baseModules','targets','replayedDeclarations','independentKernelReplay'],'replay');
  need(r.scope==='local_declaration_closure_same_kernel_imported_dependency_baseline'&&r.independentKernelReplay==='not_performed'&&Number.isSafeInteger(r.replayedDeclarations)&&r.replayedDeclarations>=plan.targets.length,'replay contract');equal(r.baseModules,['Mathlib','EvidenceHarness'],'replay bases');equal(r.targets.slice().sort(),plan.targets.map(t=>t.name).sort(),'replay targets');
}
async function inspect(directory){
  const read=await reader(directory),r=await json(read,'receipt.json');
  keys(r,['schema','attempt','plan','started','finished','sourceRevision','repository','runDirectory','reportedOutcome','failure','checks','compiler','packages','sourcesBefore','sourcesAfter','workFiles','products','phases','targets','definitions','replay','boundaries'],'receipt');
  need(r.schema==='math-live-receipt/v1'&&Object.hasOwn(PLANS,r.plan),'unsupported receipt/plan');
  need(typeof r.attempt==='string'&&/^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$/.test(r.attempt),'invalid attempt UUID');
  const start=timestamp(r.started),finish=timestamp(r.finished);need(finish>=start&&absolute(r.repository)&&absolute(r.runDirectory),'receipt identity/times');
  need(r.sourceRevision==='d00a89dd9ce6c8ef782234d28c93e69cb712c947','unsupported project revision');
  need(r.reportedOutcome==='all_required_live_phases_succeeded'&&r.failure===null,'incomplete/failed receipts cannot be accepted as complete');
  const plan=PLANS[r.plan],tangent=path.join(r.repository,'tangent-limit'),work=path.join(r.runDirectory,'inputs/build'),cache=path.join(r.runDirectory,'cache');
  const attempt=await json(read,'attempt.json');keys(attempt,['schema','attempt','label','started','state','locallyObservedLeanPass'],'attempt marker');
  equal(attempt,{schema:'math-live-attempt/v1',attempt:r.attempt,label:r.plan,started:r.started,state:'in_progress',locallyObservedLeanPass:false},'attempt marker mismatch');
  keys(r.checks,['sourceIdentity','compilerIdentity','packageIdentity','compilation','expectedTypeMatching','axiomAudit','definitionBodyMatching','targetKernelReplay','independentKernelReplay'],'checks');
  for(const [k,v] of Object.entries(r.checks))need(v===(k==='independentKernelReplay'?'not_performed':k==='definitionBodyMatching'&&!plan.definitionHarness?'not_applicable':'passed'),'incomplete checks');
  equal(r.boundaries,{receiptAuthenticity:'not_established_by_hashes',importedReceiptCanGrantPass:false,assumptions:r.plan==='tangent'?'explicit_PiDiophantine_premise_remains_unproved':'fixture_specific',dependencyCompilation:'trusted_existing_pinned_olean_cache',sourceRevisionAttestation:'exact_published_project_file_pins',independentKernelReplay:'not_performed',nativeMRS:'unavailable_unvalidated'},'unsupported trust boundary');
  for(const k of ['packages','sourcesBefore','sourcesAfter','workFiles','products','phases','targets','definitions','replay'])need(Array.isArray(r[k])&&r[k].length<=1000,'invalid array '+k);
  const sourcePins=[...baseline.catalog.files.map(f=>({origin:'project',path:f.path,...baseline.toolkit['samples/source-tree/'+f.path]})),...[...new Set(CODE.concat(plan.toolkitFiles))].map(p=>({origin:'toolkit',path:p,...baseline.toolkit[p]}))];
  const expectedSources=sourcePins.map(s=>({...s,copyPath:'inputs/'+s.origin+'/'+s.path})).sort((a,b)=>a.copyPath.localeCompare(b.copyPath,'en'));
  for(const s of r.sourcesBefore)keys(s,['origin','path','copyPath','bytes','sha256'],'source');
  equal(r.sourcesBefore,expectedSources,'source closure differs from reviewed baseline');equal(r.sourcesAfter,r.sourcesBefore,'postflight sources differ');
  need(r.products.length===plan.modules.length+3+(plan.definitionHarness?1:0)&&r.workFiles.length===plan.modules.length+3+(plan.definitionHarness?1:0),'build artifact count');
  for(const p of r.phases)processContract(p);
  const descriptors=[...r.sourcesBefore.map(s=>({path:s.copyPath,bytes:s.bytes,sha256:s.sha256})),...r.workFiles,...r.products,...r.phases.flatMap(p=>Object.values(p.evidence))];
  let total=0;for(const d of descriptors){I.descriptor(d);total+=d.bytes;}need(total<=67108864,'receipt artifact closure exceeds 64 MiB');
  const seen=new Set(),bytes=new Map();
  for(const d of descriptors){
    need(!seen.has(d.path),'duplicate artifact');seen.add(d.path);bytes.set(d.path,await artifact(read,d));
  }
  const bindings=[...plan.modules.map(m=>({destination:m.destination,origin:r.plan==='tangent'?'project':'toolkit',source:m.source})),{destination:'EvidenceHarness.lean',origin:'toolkit',source:'lean/EvidenceHarness.lean'},{destination:'ExpectedTypes.lean',origin:'toolkit',source:plan.typeHarness},{destination:'Replay.lean',origin:'toolkit',source:plan.replayHarness},...(plan.definitionHarness?[{destination:'ExpectedDefinitions.lean',origin:'toolkit',source:plan.definitionHarness}]:[])];
  const expectedWork=bindings.map(b=>{const s=sourcePins.find(s=>s.origin===b.origin&&s.path===b.source);return {path:'inputs/build/'+b.destination,bytes:s.bytes,sha256:s.sha256};});
  equal(r.workFiles.slice().sort((a,b)=>a.path.localeCompare(b.path)),expectedWork.slice().sort((a,b)=>a.path.localeCompare(b.path)),'working source binding');
  equal(r.products.map(p=>p.path).sort(),[...plan.modules.map(m=>'cache/'+m.module.split('.').join('/')+'.olean'),'cache/EvidenceHarness.olean','cache/ExpectedTypes.olean','cache/Replay.olean',...(plan.definitionHarness?['cache/ExpectedDefinitions.olean']:[])].sort(),'product coverage');
  keys(r.compiler,['path','bytes','sha256','version','commit','runtimeLibraries'],'compiler');need(absolute(r.compiler.path)&&r.compiler.commit===COMMIT&&typeof r.compiler.version==='string'&&r.compiler.version.includes('version 4.24.0,')&&r.compiler.version.includes('commit '+COMMIT),'compiler identity');member(r.compiler,'lean');
  const lib=path.resolve(path.dirname(r.compiler.path),'../lib/lean');need(Array.isArray(r.compiler.runtimeLibraries)&&r.compiler.runtimeLibraries.length===4,'compiler library coverage');
  equal(r.compiler.runtimeLibraries.map(l=>l.path).sort(),Object.keys(MEMBERS).filter(n=>n!=='lean').map(n=>path.join(lib,n)).sort(),'compiler library paths');
  for(const l of r.compiler.runtimeLibraries){keys(l,['path','bytes','sha256'],'compiler member');member(l,path.basename(l.path));}
  equal(r.packages,baseline.lock.packages.map(p=>({name:p.name,revision:p.rev,origin:p.url,trackedSourceDiff:'clean',cacheEvidence:'trusted_existing_olean_cache_not_rebuilt'})),'package metadata differs from lock');
  const baseEnv={LEAN_PATH:null,ELAN_HOME:path.join(tangent,'.elan')},contracts=[];
  const add=(name,executable,argv,cwd,environment=baseEnv)=>contracts.push({name,executable,argv,cwd,environment});
  add('compiler-version',r.compiler.path,['--version'],tangent);add('compiler-commit',r.compiler.path,['--githash'],tangent);
  const packages=suffix=>{for(const p of baseline.lock.packages){const cwd=path.join(tangent,'.lake/packages',p.name),stem='package-'+p.name+'-';add(stem+'revision'+suffix,'/usr/bin/git',['-c','core.fsmonitor=false','rev-parse','HEAD'],cwd);add(stem+'origin'+suffix,'/usr/bin/git',['-c','core.fsmonitor=false','remote','get-url','origin'],cwd);add(stem+'tracked-diff'+suffix,'/usr/bin/git',['-c','core.fsmonitor=false','diff','--no-ext-diff','--no-textconv','--exit-code','HEAD','--'],cwd);}};
  packages('');add('dependency-search-path',path.join(tangent,'.elan/bin/lake'),['env','/usr/bin/printenv','LEAN_PATH'],tangent);
  const depPhase=r.phases.find(p=>p.name==='dependency-search-path');need(depPhase,'dependency phase missing');
  const depText=I.utf8(bytes.get(depPhase.evidence.stdout.path)).trim();need(!depText.includes('\n')&&depText.length>0,'malformed dependency search path');
  const rawPaths=depText.split(path.delimiter).map(p=>path.resolve(tangent,p));
  const projectOutput=path.join(tangent,'.lake/build/lib/lean'),dependencyPaths=rawPaths.filter(p=>p!==projectOutput);
  need(rawPaths.filter(p=>p===projectOutput).length===1,'project output path coverage');
  equal(dependencyPaths.slice().sort(),[...baseline.lock.packages.map(p=>path.join(tangent,'.lake/packages',p.name,'.lake/build/lib/lean')),lib].sort(),'dependency cache path coverage');
  const leanEnv={...baseEnv,LEAN_PATH:[cache,...dependencyPaths].join(path.delimiter)};
  const compile=(name,source,module)=>add(name,r.compiler.path,['--json','--root='+work,'-o',path.join(cache,module.split('.').join('/')+'.olean'),path.join(work,source)],work,leanEnv);
  compile('compile-evidence-helper','EvidenceHarness.lean','EvidenceHarness');
  plan.modules.forEach((m,i)=>compile('compile-target-'+i,m.destination,m.module));compile('expected-type-and-axiom-audit','ExpectedTypes.lean','ExpectedTypes');
  if(plan.definitionHarness)compile('definition-body-matching','ExpectedDefinitions.lean','ExpectedDefinitions');compile('target-kernel-replay','Replay.lean','Replay');packages('-post');
  equal(r.phases.map(p=>p.name),contracts.map(p=>p.name),'phase coverage/order');let previous=start;
  for(let i=0;i<r.phases.length;i++){
    const p=r.phases[i],c=contracts[i],times=processContract(p);need(times.success&&times.start>=previous&&times.end<=finish,'phase chronology or unsuccessful phase');previous=times.end;
    for(const k of ['executable','argv','cwd','environment'])equal(p[k],c[k],'phase '+p.name+' '+k+' differs from fixed command');
    need(p.outputLimitBytes===4194304,'unsupported baseline capture cap');const out=bytes.get(p.evidence.stdout.path),err=bytes.get(p.evidence.stderr.path);need(err.length===0,'unexpected stderr in complete receipt: '+p.name);
    if(p.name==='compiler-version')need(I.utf8(out).trim()===r.compiler.version,'version stdout mismatch');
    else if(p.name==='compiler-commit')need(I.utf8(out).trim()===COMMIT,'compiler commit stdout mismatch');
    else if(p.name.startsWith('package-')){const pkg=baseline.lock.packages.find(x=>p.name.startsWith('package-'+x.name+'-'));const text=I.utf8(out).trim();need(text===(p.name.includes('-revision')?pkg.rev:p.name.includes('-origin')?pkg.url:''),'package stdout mismatch');}
    else if(p.name!=='dependency-search-path')leanMessages(out);
  }
  const messages=name=>leanMessages(bytes.get(r.phases.find(p=>p.name===name).evidence.stdout.path));
  const ts=markers(messages('expected-type-and-axiom-audit'),'MATH_EVIDENCE_TARGET ');targets(ts,plan);equal(ts,r.targets,'target log binding');
  const rr=markers(messages('target-kernel-replay'),'MATH_EVIDENCE_REPLAY ');replay(rr,plan);equal(rr,r.replay,'replay log binding');
  if(plan.definitionHarness){const ds=markers(messages('definition-body-matching'),'MATH_EVIDENCE_DEFINITION ');definitions(ds,plan);equal(ds,r.definitions,'definition log binding');}else equal(r.definitions,[],'unexpected definition claims');
  return {ok:true,kind:'strict_v1_reported_integrity_only',evidenceFiles:seen.size,reportedOutcome:r.reportedOutcome,leanPass:false,locallyObservedLeanPass:false,freshness:'not_established',receiptAuthenticity:'not_established',formalProofAcceptance:'not_granted_by_import',dependencyCompilation:'trusted_external_cache_not_rebuilt',independentKernelReplay:'not_performed',nativeMRS:'unavailable_unvalidated'};
}
if(require.main===module)inspect(process.argv[2]).then(x=>console.log(JSON.stringify(x,null,2))).catch(e=>{console.error(JSON.stringify({ok:false,leanPass:false,locallyObservedLeanPass:false,error:e.message}));process.exitCode=2;});
module.exports={inspect,MEMBERS,COMMIT,targets,definitions,replay};
