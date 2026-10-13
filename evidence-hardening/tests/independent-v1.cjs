"use strict";
// Authored by the independent verification subagent; no production-code edits.
// Usage: node independent-v1.cjs COMPANION_DIR ACTUAL_SUCCESS_RECEIPT NEW_OUTPUT_DIR
const fs=require('node:fs/promises'),path=require('node:path'),crypto=require('node:crypto'),assert=require('node:assert/strict');
const source=process.argv[2],receiptSource=process.argv[3],out=process.argv[4];
const {inspect}=require(path.join(source,'inspect-v1.cjs'));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const clone=x=>JSON.parse(JSON.stringify(x));
let sequence=0;
const results=[];
async function log(r,dir,name,channel,text){const p=r.phases.find(p=>p.name===name),d=p.evidence[channel],b=Buffer.from(text);await fs.writeFile(path.join(dir,d.path),b);d.bytes=b.length;d.sha256=sha(b);}
const mutations=[
 ['uuid-not-v4',r=>r.attempt='aaaaaaaa-aaaa-1aaa-8aaa-aaaaaaaaaaaa'],
 ['uuid-mismatch-attempt',async(r,d)=>{const p=path.join(d,'attempt.json'),a=JSON.parse(await fs.readFile(p));a.attempt='aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa';await fs.writeFile(p,JSON.stringify(a));}],
 ['attempt-pass-request',async(r,d)=>{const p=path.join(d,'attempt.json'),a=JSON.parse(await fs.readFile(p));a.locallyObservedLeanPass=true;await fs.writeFile(p,JSON.stringify(a));}],
 ['attempt-time-mismatch',async(r,d)=>{const p=path.join(d,'attempt.json'),a=JSON.parse(await fs.readFile(p));a.started='2000-01-01T00:00:00.000Z';await fs.writeFile(p,JSON.stringify(a));}],
 ['receipt-reversed-times',r=>r.finished='2000-01-01T00:00:00.000Z'],
 ['receipt-noncanonical-time',r=>r.started=r.started.replace('.','+00:00.')],
 ['unsupported-source-revision',r=>r.sourceRevision='a'.repeat(40)],
 ['unsupported-proof-pass-field',r=>r.leanPass=true],
 ['unsupported-independent-kernel',r=>r.checks.independentKernelReplay='passed'],
 ['unsupported-cache-rebuild',r=>r.boundaries.dependencyCompilation='rebuilt_from_source'],
 ['unsupported-native-mrs',r=>r.boundaries.nativeMRS='passed'],
 ['incomplete-phase',r=>r.phases.pop()],
 ['duplicate-phase',r=>r.phases[1]=clone(r.phases[0])],
 ['reordered-phases',r=>[r.phases[0],r.phases[1]]=[r.phases[1],r.phases[0]]],
 ['pid-null',r=>{r.phases[0].termination.pid=null;r.phases[0].termination.processGroup=null;}],
 ['pid-string',r=>{r.phases[0].termination.pid='123';r.phases[0].termination.processGroup='123';}],
 ['pid-negative',r=>{r.phases[0].termination.pid=-1;r.phases[0].termination.processGroup=-1;}],
 ['process-group-mismatch',r=>r.phases[0].termination.processGroup=r.phases[0].termination.pid+1],
 ['exit-code-plus-signal',r=>r.phases[0].termination.signal='SIGTERM'],
 ['invalid-signal',r=>r.phases[0].termination.signal='SIGFAKE'],
 ['exit-code-string',r=>r.phases[0].termination.exitCode='0'],
 ['exit-code-out-of-range',r=>r.phases[0].termination.exitCode=256],
 ['success-false',r=>r.phases[0].success=false],
 ['timeout-success',r=>r.phases[0].termination.kind='timeout'],
 ['launch-failed-success',r=>r.phases[0].termination.kind='launch_failed'],
 ['success-error',r=>r.phases[0].error='simulated I/O error'],
 ['phase-duration-string',r=>r.phases[0].durationMs='0'],
 ['phase-duration-disagrees',r=>r.phases[0].durationMs+=10000],
 ['phase-outside-attempt-time',r=>r.phases[0].started='2000-01-01T00:00:00.000Z'],
 ['phase-argv-substitution',r=>r.phases[0].argv=['--githash']],
 ['compile-argv-substitution',r=>{const p=r.phases.find(p=>p.name==='compile-evidence-helper');p.argv[p.argv.length-1]+='x';}],
 ['phase-cwd-substitution',r=>r.phases[0].cwd='/tmp'],
 ['phase-executable-substitution',r=>r.phases[0].executable='/bin/true'],
 ['phase-unknown-environment',r=>r.phases[0].environment.EXTRA='1'],
 ['phase-elan-environment-substitution',r=>r.phases[0].environment.ELAN_HOME='/tmp'],
 ['compile-leanpath-substitution',r=>r.phases.find(p=>p.name==='compile-evidence-helper').environment.LEAN_PATH='/tmp'],
 ['phase-output-cap-substitution',r=>r.phases[0].outputLimitBytes=4194303],
 ['phase-log-reuse',r=>r.phases[0].evidence.stderr=clone(r.phases[0].evidence.stdout)],
 ['phase-log-missing',async(r,d)=>fs.unlink(path.join(d,r.phases[0].evidence.stdout.path))],
 ['coherent-compiler-log-tamper',async(r,d)=>log(r,d,'compiler-commit','stdout','a'.repeat(40)+'\n')],
 ['coherent-stderr-tamper',async(r,d)=>log(r,d,'compiler-version','stderr','unexpected warning\n')],
 ['coherent-error-json-tamper',async(r,d)=>log(r,d,'compile-evidence-helper','stdout',JSON.stringify({severity:'error',data:'simulated compile error'})+'\n')],
 ['coherent-malformed-json-tamper',async(r,d)=>log(r,d,'compile-evidence-helper','stdout','malformed\n')],
 ['coherent-missing-target-marker',async(r,d)=>log(r,d,'expected-type-and-axiom-audit','stdout','')],
 ['coherent-missing-replay-marker',async(r,d)=>log(r,d,'target-kernel-replay','stdout','')],
 ['coherent-revision-log-tamper',async(r,d)=>log(r,d,'package-mathlib-revision','stdout','b'.repeat(40)+'\n')],
 ['coherent-origin-log-tamper',async(r,d)=>log(r,d,'package-mathlib-origin','stdout','https://example.org/substitution\n')],
 ['coherent-diff-log-tamper',async(r,d)=>log(r,d,'package-mathlib-tracked-diff','stdout','diff --git source-change\n')],
 ['source-closure-omission',r=>{r.sourcesBefore.pop();r.sourcesAfter=clone(r.sourcesBefore);}],
 ['source-closure-coordinated-repin',r=>{r.sourcesBefore[0].sha256='0'.repeat(64);r.sourcesAfter=clone(r.sourcesBefore);}],
 ['target-axiom-substitution',r=>r.targets[0].axioms=['sorryAx']],
 ['same-kernel-claim-upgrade',r=>r.replay[0].independentKernelReplay='passed'],
 ['runtime-member-coordinated-repin',r=>r.compiler.runtimeLibraries[0].sha256='0'.repeat(64)],
 ['package-revision-coordinated-repin',r=>r.packages[0].revision='a'.repeat(40)],
 ['failed-receipt-as-complete',r=>{r.reportedOutcome='failed_or_incomplete';r.failure='deliberate';}],
];
async function check(name,change,accept=false){
 const d=path.join(out,String(++sequence)+'-'+name);await fs.cp(receiptSource,d,{recursive:true});const r=JSON.parse(await fs.readFile(path.join(d,'receipt.json')));
 await change(r,d);await fs.writeFile(path.join(d,'receipt.json'),JSON.stringify(r));let result,error;
 try{result=await inspect(d);}catch(e){error=e.message;}
 const pass=accept?result?.ok===true&&result.leanPass===false&&result.locallyObservedLeanPass===false&&result.freshness==='not_established':typeof error==='string';
 results.push({name,expected:accept?'reported_integrity_only_no_fresh_pass':'reject',passed:pass,result,error});console.log(name+': '+(pass?'passed':'FAILED'));return d;
}
async function main(){
 await fs.mkdir(out,{recursive:false});
 const names=['inspect-v1.cjs','io.cjs','process-contract.cjs','baseline.json','vendor/live-plans.cjs','vendor/strict-json.cjs'];
 const hashes=async()=>Object.fromEntries(await Promise.all(names.map(async p=>[p,sha(await fs.readFile(path.join(source,p)))])));
 const before=await hashes();await check('actual-fresh-success-import',()=>{},true);
 for(const [name,change] of mutations)await check(name,change);
 await check('coherently-aged-receipt',async(r,d)=>{const shift=s=>new Date(Date.parse(s)-365*86400000).toISOString();r.started=shift(r.started);r.finished=shift(r.finished);for(const p of r.phases){p.started=shift(p.started);p.finished=shift(p.finished);}const p=path.join(d,'attempt.json'),a=JSON.parse(await fs.readFile(p));a.started=r.started;await fs.writeFile(p,JSON.stringify(a));},true);
 const after=await hashes(),report={schema:'independent-hardening-inspector-tests/v1',source,receiptSource,argv:process.argv,startedKernelTrust:'official_Lean_4.24.0_same_kernel_baseline_receipt',sourceHashesBefore:before,sourceHashesAfter:after,sourceUnchanged:JSON.stringify(before)===JSON.stringify(after),total:results.length,passed:results.filter(r=>r.passed).length,failed:results.filter(r=>!r.passed),results,leanPassesGrantedByInspection:0};
 await fs.writeFile(path.join(out,'report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({total:report.total,passed:report.passed,failed:report.failed},null,2));process.exitCode=report.failed.length?1:0;
}
main().catch(e=>{console.error(e);process.exitCode=1;});
