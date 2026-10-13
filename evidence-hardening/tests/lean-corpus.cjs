"use strict";
// Actual pinned Lean; expected failures exercise gates rather than prove claims.
const fs=require('node:fs/promises'),path=require('node:path'),assert=require('node:assert/strict'),gate=require('../fixture-gate.cjs'),I=require('../io.cjs');
async function main(){
  const [binary,parent,reportPath]=process.argv.slice(2);I.need(binary&&parent&&reportPath,'Usage: node tests/lean-corpus.cjs LEAN EXISTING_PARENT NEW_REPORT');const root=await fs.mkdtemp(path.join(path.resolve(parent),'lean-corpus-'));
  const before=(await gate.sources()).digest,results=[],expected={valid:null,'hidden-assumption':'whole-type-and-axiom-audit','statement-drift':'whole-type-and-axiom-audit',specialization:'whole-type-and-axiom-audit','wrong-name':'whole-type-and-axiom-audit','definition-substitution':'definition-body-audit','transitive-drift':'definition-body-audit',sorry:'whole-type-and-axiom-audit','custom-axiom':'whole-type-and-axiom-audit','skip-kernel':'same-kernel-replay'};
  for(const [label,phase] of Object.entries(expected)){
    const directory=path.join(root,label);try{const r=await gate.run(label,binary,directory);assert.equal(r.ok,label==='valid');assert.equal(r.locallyObservedLeanPass,label==='valid');assert.equal(r.failedPhase,phase);assert.equal(r.targetCompilationObserved,true);assert.equal(r.verifiedBuild,true);
      if(['definition-substitution','transitive-drift'].includes(label))assert.ok(r.receipt.phases.find(p=>p.name==='whole-type-and-axiom-audit').success);
      if(label==='skip-kernel')assert.ok(r.receipt.phases.find(p=>p.name==='whole-type-and-axiom-audit').success);
      let imported=null;if(label==='valid'){imported=await gate.inspect(directory);assert.equal(imported.leanPass,false);assert.equal(imported.locallyObservedLeanPass,false);assert.equal(imported.freshness,'not_established');}
      results.push({label,pass:true,expectedPhase:phase,observedPhase:r.failedPhase,observedLiveFixturePass:r.locallyObservedLeanPass,failure:r.failure,imported,receiptSHA256:I.sha(await fs.readFile(path.join(directory,'receipt.json'))),phases:r.receipt.phases.map(p=>({name:p.name,termination:p.termination,success:p.success})),directory});
    }catch(e){results.push({label,pass:false,error:e.stack});}
    process.stdout.write(label+': '+(results.at(-1).pass?'passed':'FAILED')+'\n');
  }
  const after=(await gate.sources()).digest,report={schema:'actual-pinned-Lean-fixture-corpus/v1',testedUTC:new Date().toISOString(),runtime:process.version,binary,root,sourceDigestBefore:before,sourceDigestAfter:after,sourceUnchanged:before===after,results,total:results.length,passed:results.filter(r=>r.pass).length,failed:results.filter(r=>!r.pass),trust:{coreOLeans:'trusted_existing_cache',mathlib:'not_used',independentKernel:'not_performed',nativeMRS:'unavailable_unvalidated'}};
  assert.equal(before,after,'source changed during corpus');await fs.writeFile(reportPath,JSON.stringify(report,null,2)+'\n',{flag:'wx'});console.log(JSON.stringify({total:report.total,passed:report.passed,failed:report.failed,reportPath}));process.exitCode=report.failed.length?1:0;
}
main().catch(e=>{console.error(e);process.exitCode=1;});
