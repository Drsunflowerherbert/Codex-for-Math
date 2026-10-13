"use strict";
// Authored by the independent verification subagent; no production-code edits.
// Usage: node independent-fixture-import.cjs COMPANION_DIR ACTUAL_VALID_RECEIPT NEW_OUTPUT_DIR
const fs=require('node:fs/promises'),path=require('node:path'),crypto=require('node:crypto');
const source=process.argv[2],receiptSource=process.argv[3],out=process.argv[4];
const {inspect}=require(path.join(source,'fixture-gate.cjs'));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex'),clone=x=>JSON.parse(JSON.stringify(x));
const results=[];let sequence=0;
async function log(r,d,name,channel,text){const p=r.phases.find(p=>p.name===name),item=p.evidence[channel],bytes=Buffer.from(text);await fs.writeFile(path.join(d,item.path),bytes);item.bytes=bytes.length;item.sha256=sha(bytes);}
const cases=[
 ['uuid-mismatch',r=>r.attempt='a'.repeat(8)+'-aaaa-4aaa-8aaa-aaaaaaaaaaaa'],
 ['receipt-missing-phase',r=>r.phases.pop()],
 ['receipt-reordered-phase',r=>[r.phases[0],r.phases[1]]=[r.phases[1],r.phases[0]]],
 ['receipt-unknown-pass-field',r=>r.leanPass=true],
 ['receipt-upgraded-boundary',r=>r.boundaries.importedReceiptCanGrantPass=true],
 ['receipt-stale-source-digest',r=>r.sourceDigest='0'.repeat(64)],
 ['source-closure-omission',r=>r.sourceFiles.pop()],
 ['source-closure-repin',r=>r.sourceFiles[0].sha256='0'.repeat(64)],
 ['product-coverage-omission',r=>r.products.pop()],
 ['work-source-repin',r=>r.workFiles[0].sha256='0'.repeat(64)],
 ['runtime-member-repin',r=>r.compiler.members[0].sha256='0'.repeat(64)],
 ['core-cache-upgrade',r=>r.compiler.coreOLeanTrust='rebuilt_from_source'],
 ['pid-null',r=>{r.phases[0].termination.pid=null;r.phases[0].termination.processGroup=null;}],
 ['pid-string',r=>{r.phases[0].termination.pid='123';r.phases[0].termination.processGroup='123';}],
 ['pid-process-group-mismatch',r=>r.phases[0].termination.processGroup+=1],
 ['exit-code-string',r=>r.phases[0].termination.exitCode='0'],
 ['exit-code-out-of-range',r=>r.phases[0].termination.exitCode=256],
 ['exit-and-signal',r=>r.phases[0].termination.signal='SIGTERM'],
 ['timeout-success',r=>r.phases[0].termination.kind='timeout'],
 ['launch-failure-success',r=>r.phases[0].termination.kind='launch_failed'],
 ['success-error',r=>r.phases[0].error='simulated error'],
 ['bad-duration',r=>r.phases[0].durationMs+=10000],
 ['bad-output-limit',r=>r.phases[0].outputLimitBytes=1],
 ['bad-phase-time',r=>r.phases[0].started='2000-01-01T00:00:00.000Z'],
 ['argv-substitution',r=>r.phases[0].argv=['--githash']],
 ['argv-compile-source-substitution',r=>r.phases.find(p=>p.name==='compile-helper').argv[4]+='x'],
 ['cwd-substitution',r=>r.phases[0].cwd='/tmp'],
 ['executable-substitution',r=>r.phases[0].executable='/bin/true'],
 ['environment-substitution',r=>r.phases[0].environment.LEAN_PATH='/tmp'],
 ['environment-extra',r=>r.phases[0].environment.EXTRA='1'],
 ['log-reuse',r=>r.phases[0].evidence.stderr=clone(r.phases[0].evidence.stdout)],
 ['log-missing',async(r,d)=>fs.unlink(path.join(d,r.phases[0].evidence.stdout.path))],
 ['coherent-compiler-log-substitution',async(r,d)=>log(r,d,'compiler-commit','stdout','0'.repeat(40)+'\n')],
 ['coherent-stderr-substitution',async(r,d)=>log(r,d,'compile-helper','stderr','unexpected error\n')],
 ['coherent-malformed-json',async(r,d)=>log(r,d,'compile-helper','stdout','malformed\n')],
 ['coherent-error-json',async(r,d)=>log(r,d,'compile-helper','stdout',JSON.stringify({severity:'error',data:'error'})+'\n')],
 ['coherent-missing-type-marker',async(r,d)=>log(r,d,'whole-type-and-axiom-audit','stdout','')],
 ['coherent-missing-body-marker',async(r,d)=>log(r,d,'definition-body-audit','stdout','')],
 ['coherent-missing-replay-marker',async(r,d)=>log(r,d,'same-kernel-replay','stdout','')],
 ['record-axiom-upgrade',r=>r.records.targets[0].axioms=['sorryAx']],
 ['record-independent-kernel-upgrade',r=>r.records.replay[0].independentKernelReplay='passed'],
 ['record-body-upgrade',r=>r.records.definitions[0].status='proved_predicate'],
 ['attempt-pass-upgrade',async(r,d)=>{const p=path.join(d,'attempt.json'),a=JSON.parse(await fs.readFile(p));a.locallyObservedLeanPass=true;await fs.writeFile(p,JSON.stringify(a));}],
];
async function check(name,mutate,accepted=false){
 const dir=path.join(out,String(++sequence)+'-'+name);await fs.cp(receiptSource,dir,{recursive:true});const r=JSON.parse(await fs.readFile(path.join(dir,'receipt.json')));await mutate(r,dir);await fs.writeFile(path.join(dir,'receipt.json'),JSON.stringify(r));let result,error;try{result=await inspect(dir);}catch(e){error=e.message;}
 const passed=accepted?result?.ok===true&&result.leanPass===false&&result.locallyObservedLeanPass===false&&result.freshness==='not_established':typeof error==='string';results.push({name,expected:accepted?'reported_integrity_only_no_freshness_or_Lean_pass':'reject',passed,result,error});console.log(name+': '+(passed?'passed':'FAILED'));
}
async function main(){
 await fs.mkdir(out);const hashes=async()=>{const {SOURCE_NAMES}=require(path.join(source,'fixture-gate.cjs'));return Object.fromEntries(await Promise.all([...SOURCE_NAMES,'fixture-policy.json'].map(async p=>[p,sha(await fs.readFile(path.join(source,p)))])));};const before=await hashes();
 await check('fresh-valid-receipt-import',()=>{},true);for(const [name,mutate] of cases)await check(name,mutate);
 await check('coherently-aged-receipt',async(r,d)=>{const shift=s=>new Date(Date.parse(s)-365*86400000).toISOString();r.started=shift(r.started);r.finished=shift(r.finished);for(const p of r.phases){p.started=shift(p.started);p.finished=shift(p.finished);}const file=path.join(d,'attempt.json'),a=JSON.parse(await fs.readFile(file));a.started=r.started;await fs.writeFile(file,JSON.stringify(a));},true);
 const after=await hashes(),report={schema:'independent-fixed-fixture-import-tests/v1',source,receiptSource,argv:process.argv,sourceHashesBefore:before,sourceHashesAfter:after,sourceUnchanged:JSON.stringify(before)===JSON.stringify(after),total:results.length,passed:results.filter(r=>r.passed).length,failed:results.filter(r=>!r.passed),results,leanPassesGrantedByInspection:0};await fs.writeFile(path.join(out,'report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({total:report.total,passed:report.passed,failed:report.failed},null,2));process.exitCode=report.failed.length?1:0;
}
main().catch(e=>{console.error(e);process.exitCode=1;});
