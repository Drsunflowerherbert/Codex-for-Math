"use strict";
// Fixed reviewed commands from a separately extracted checkpoint. Imported
// record fields and receipt argv are never executed by this smoke test.
const fs=require("node:fs/promises"),path=require("node:path"),crypto=require("node:crypto"),assert=require("node:assert/strict");
const sha=b=>crypto.createHash("sha256").update(b).digest("hex");
async function main(toolkit,repository,output){
  toolkit=await fs.realpath(toolkit);repository=await fs.realpath(repository);output=path.resolve(output);await fs.mkdir(output);
  const {runProcess}=require(path.join(toolkit,"process.cjs"));
  const approval=JSON.parse(await fs.readFile(path.join(toolkit,"PUBLIC-SOURCES.json"),"utf8"));
  const sourceHashes=async()=>Object.fromEntries(await Promise.all(Object.keys(approval.files).map(async name=>[name,sha(await fs.readFile(path.join(toolkit,name)))])));
  const before=await sourceHashes();assert.deepEqual(before,approval.files);const phases=[];
  async function run(name,args){const phase=await runProcess(process.execPath,args,{cwd:toolkit,directory:output,name,timeoutMs:300000});phases.push(phase);assert.equal(phase.success,true,"consumer command failed: "+name);return JSON.parse(await fs.readFile(path.join(output,phase.evidence.stdout.path),"utf8"));}
  const inherited=await run("inherited-tests",[path.join(toolkit,"run-tests.cjs")]);
  assert.equal(inherited.synthetic.passed,78);assert.equal(inherited.acceptance.passed,60);assert.equal(inherited.mockCLI.passed,11);assert.equal(inherited.materializerMock.passed,8);
  const accept=await run("accept-pinned-bundle",[path.join(toolkit,"cli.cjs"),"accept-tangent",path.join(toolkit,"samples/tangent.bundle.json")]);assert.equal(accept.ok,true);
  const validate=await run("validate-relocated-tree",[path.join(toolkit,"cli.cjs"),"validate",path.join(toolkit,"samples/catalog.json"),path.join(toolkit,"samples/source-tree")]);assert.equal(validate.ok,true);
  const bundles=[];for(const name of ["a","b"]){const file=path.join(output,"bundle-"+name+".json");await run("bundle-"+name,[path.join(toolkit,"cli.cjs"),"bundle",path.join(toolkit,"samples/catalog.json"),repository,file]);bundles.push(await fs.readFile(file));}
  assert.deepEqual(bundles[0],bundles[1]);assert.equal(sha(bundles[0]),"841e041ac0e31b9263b440a81cb5fd525c81ff001e61db7f05661fbde1cd1966");
  const integrity=await run("verify-public-sources",[path.join(toolkit,"verify-public-sources.cjs")]);assert.equal(integrity.ok,true);
  const liveDirectory=path.join(output,"fresh-valid"),live=await run("fresh-consumer-live-valid",[path.join(toolkit,"live.cjs"),"run","valid",repository,liveDirectory]);assert.equal(live.locallyObservedLeanPass,true);assert.equal(live.checks.independentKernelReplay,"not_performed");
  const inspect=await run("inspect-fresh-consumer-receipt",[path.join(toolkit,"live.cjs"),"inspect-receipt",liveDirectory]);assert.equal(inspect.leanPass,false);assert.equal(inspect.locallyObservedLeanPass,false);
  const after=await sourceHashes();assert.deepEqual(before,after);
  const report={schema:"public-extracted-consumer-smoke/v1",runtime:process.version,platform:process.platform,toolkit,repository,output,relocated:true,productionSourcesBefore:before,productionSourcesAfter:after,productionSourcesUnchanged:true,phases,results:{inheritedTests:157,pinnedBundleAcceptance:true,relocatedSourceValidation:true,deterministicTangentBundleSha256:sha(bundles[0]),publicSourceIntegrity:integrity,freshLocallyObservedLeanPass:live.locallyObservedLeanPass,freshReceiptInspection:inspect},boundaries:{importedLeanPasses:0,independentKernelReplay:"not_performed",dependencies:"trusted_existing_pinned_olean_cache",nativeMRS:"unavailable_unvalidated",nativeMac:"not_tested"}};
  await fs.writeFile(path.join(output,"report.json"),JSON.stringify(report,null,2)+"\n",{flag:"wx"});console.log(JSON.stringify({ok:true,output,phases:phases.length,productionSourcesUnchanged:true,freshLocallyObservedLeanPass:true,importedReceiptLeanPass:false},null,2));return report;
}
if(require.main===module)main(...process.argv.slice(2)).catch(e=>{console.error(e);process.exitCode=1;});
module.exports={main};
