"use strict";
const fs=require("node:fs/promises");
const path=require("node:path");
const crypto=require("node:crypto");
const {PLANS,TRUSTED_FILES}=require("./live-plans.cjs");
const {runProcess}=require("./process.cjs");
const {readRegular,readJSON,sourceReader,contained}=require("./cli.cjs");
const {acceptTangent}=require("./tangent-pins.cjs");
const {parseStrict,canonicalJSON}=require("./strict-json.cjs");
const {decodeUTF8,isPortablePath}=require("./core.cjs");
const {writeNewTree}=require("./materialize.cjs");
const {hashRegular}=require("./hash-io.cjs");
const hash=b=>crypto.createHash("sha256").update(b).digest("hex");
const REVISION="d00a89dd9ce6c8ef782234d28c93e69cb712c947";
const COMPILER_COMMIT="797c613eb9b6d4ec95db23e3e00af9ac6657f24b";
// Exact Linux release member pins, independently compared with the published
// installer-pinned .tar.zst by toolchain-audit.py. Host libc and imported oleans
// remain trusted dependencies outside this selected-member byte attestation.
const RELEASE_MEMBERS={
  lean:{bytes:9024,sha256:"8fadc3ed92cc9decb94c96ee9c0876e91e03a3a5e69138f32114f02789e2766c"},
  "libleanshared.so":{bytes:193479936,sha256:"8cc9858cc57c52015ba6dd948bdbf7f05926b9b5fcead69a964f0ad61ddd79dd"},
  "libleanshared_1.so":{bytes:6232,sha256:"6ce912e300ad305bb38a362404544602e2229d072b78d75b1dd71c637e453c2c"},
  "libleanshared_2.so":{bytes:6232,sha256:"6ce912e300ad305bb38a362404544602e2229d072b78d75b1dd71c637e453c2c"},
  "libInit_shared.so":{bytes:6232,sha256:"6ce912e300ad305bb38a362404544602e2229d072b78d75b1dd71c637e453c2c"}
};
const CODE_FILES=["live.cjs","live-plans.cjs","process.cjs","cli.cjs","bounded-io.cjs","hash-io.cjs","materialize.cjs","core.cjs","strict-json.cjs","bundle.cjs","tangent-pins.cjs","samples/catalog.json"];
const allowedAxioms=new Set(["propext","Classical.choice","Quot.sound"]);
function requireValue(condition,message){if(!condition)throw new Error(message);}
function checkReleaseMember(name,item){
  const expected=RELEASE_MEMBERS[name];
  requireValue(expected&&item.bytes===expected.bytes&&item.sha256===expected.sha256,"compiler/kernel bytes differ from pinned Linux release member: "+name);
}
function checkCompilerRelease(compiler){
  requireValue(compiler&&compiler.commit===COMPILER_COMMIT&&typeof compiler.version==="string"&&compiler.version.includes("version 4.24.0,")&&
    Array.isArray(compiler.runtimeLibraries)&&compiler.runtimeLibraries.length===4,"successful receipt compiler runtime evidence incomplete");
  checkReleaseMember("lean",compiler);
  const expected=Object.keys(RELEASE_MEMBERS).filter(n=>n!=="lean").sort();
  requireValue(canonicalJSON(compiler.runtimeLibraries.map(i=>path.basename(i.path)).sort())===canonicalJSON(expected),"compiler kernel library coverage incomplete");
  for(const item of compiler.runtimeLibraries)checkReleaseMember(path.basename(item.path),item);
}

function leanMessages(bytes) {
  const lines=decodeUTF8(bytes).split("\n").filter(x=>x.trim());
  return lines.map(line=>{
    const m=parseStrict(line);
    requireValue(m&&typeof m==="object"&&typeof m.data==="string"&&["information","warning","error"].includes(m.severity),"unsupported Lean message");
    requireValue(m.severity!=="error","Lean emitted an error message");
    return m;
  });
}
function parseMarkers(bytes,prefix) {
  return leanMessages(bytes).filter(m=>m.data.startsWith(prefix)).map(m=>{
    requireValue(m.severity==="information","evidence marker is not an information message");
    return parseStrict(m.data.slice(prefix.length));
  });
}
function checkTargets(records,plan) {
  requireValue(records.length===plan.targets.length,"expected-type/axiom evidence name coverage incomplete");
  const seen=new Set();
  for(const r of records) {
    const target=plan.targets.find(t=>t.name===r.target);
    requireValue(target&&!seen.has(r.target),"unexpected or duplicated target evidence");seen.add(r.target);
    requireValue(r.declarationKind===(target.kind==="theorem"?"theorem":"definition"),"declaration kind mismatch");
    requireValue(r.typeMatching==="closed_whole_type_kernel_definitional_equality"&&typeof r.observedType==="string"&&r.observedType.length>0,"unsupported type matching evidence");
    requireValue(Array.isArray(r.axioms)&&new Set(r.axioms).size===r.axioms.length&&r.axioms.every(a=>allowedAxioms.has(a)),"unapproved or malformed axiom evidence");
    requireValue(r.targetKernelReplay==="separate_phase_required","unsupported target replay request");
  }
}
function checkDefinitions(records,plan) {
  const expected=plan.targets.filter(t=>t.kind!=="theorem").map(t=>t.name).sort();
  requireValue(canonicalJSON(records.map(r=>r.target).sort())===canonicalJSON(expected),"definition body evidence coverage incomplete");
  for(const r of records)requireValue(r.definitionBodyMatching==="kernel_definitional_equality"&&r.status==="definition_value_matched_not_a_proof_of_the_predicate"&&
    Array.isArray(r.axioms)&&r.axioms.every(a=>allowedAxioms.has(a)),"unsupported definition body evidence");
}
function checkReplay(records,plan) {
  requireValue(records.length===1,"kernel replay evidence is absent or duplicated");
  const r=records[0];
  requireValue(r.scope==="local_declaration_closure_same_kernel_imported_dependency_baseline"&&r.independentKernelReplay==="not_performed"&&
    canonicalJSON(r.baseModules)===canonicalJSON(["Mathlib","EvidenceHarness"])&&
    canonicalJSON(r.targets.slice().sort())===canonicalJSON(plan.targets.map(t=>t.name).sort())&&
    Number.isSafeInteger(r.replayedDeclarations)&&r.replayedDeclarations>=plan.targets.length,"unsupported or incomplete kernel replay evidence");
}
async function sources(repo,plan) {
  const projectReader=await sourceReader(repo),toolkitReader=await sourceReader(__dirname);
  const catalog=await readJSON(path.join(__dirname,"samples/catalog.json"));
  // Separate fixed pins must approve the exact published source tree. Generic
  // coordinated source/catalog hash edits cannot authorize execution.
  await acceptTangent(catalog,projectReader,hash);
  const entries=[],bytes=new Map();
  for(const f of catalog.files) {
    const b=await projectReader(f.path);
    requireValue(hash(b)===f.sha256,"published source changed: "+f.path);
    const key="project/"+f.path;bytes.set(key,b);
    entries.push({origin:"project",path:f.path,copyPath:"inputs/"+key,bytes:b.length,sha256:hash(b)});
  }
  for(const name of [...new Set(CODE_FILES.concat(plan.toolkitFiles))].sort()) {
    const b=await toolkitReader(name);
    if(TRUSTED_FILES[name])requireValue(hash(b)===TRUSTED_FILES[name],"trusted Lean fixture/harness changed: "+name);
    const key="toolkit/"+name;bytes.set(key,b);
    entries.push({origin:"toolkit",path:name,copyPath:"inputs/"+key,bytes:b.length,sha256:hash(b)});
  }
  entries.sort((a,b)=>a.copyPath.localeCompare(b.copyPath,"en"));
  return {entries,bytes};
}
function sourceIdentity(entries){return canonicalJSON(entries.map(e=>({origin:e.origin,path:e.path,bytes:e.bytes,sha256:e.sha256})));}
async function artifact(reader,portable) {
  const bytes=await reader(portable);return {path:portable,bytes:bytes.length,sha256:hash(bytes)};
}
function exactKeys(value,keys,where) {
  requireValue(value&&typeof value==="object"&&!Array.isArray(value)&&canonicalJSON(Object.keys(value).sort())===canonicalJSON(keys.slice().sort()),"invalid receipt fields: "+where);
}
function expectedPhaseNames(plan,lock) {
  const packageNames=suffix=>lock.packages.flatMap(p=>["revision","origin","tracked-diff"].map(k=>"package-"+p.name+"-"+k+suffix));
  return ["compiler-version","compiler-commit",...packageNames(""),"dependency-search-path","compile-evidence-helper",
    ...plan.modules.map((m,i)=>"compile-target-"+i),"expected-type-and-axiom-audit",
    ...(plan.definitionHarness?["definition-body-matching"]:[]),"target-kernel-replay",...packageNames("-post")];
}
function validateReceiptStructure(r) {
  exactKeys(r,["schema","attempt","plan","started","finished","sourceRevision","repository","runDirectory","reportedOutcome","failure","checks","compiler","packages","sourcesBefore","sourcesAfter","workFiles","products","phases","targets","definitions","replay","boundaries"],"receipt");
  requireValue(r.schema==="math-live-receipt/v1"&&Object.prototype.hasOwnProperty.call(PLANS,r.plan),"unsupported receipt/plan");
  requireValue(/^[0-9a-f-]{36}$/.test(r.attempt)&&r.sourceRevision===REVISION&&path.isAbsolute(r.repository)&&path.isAbsolute(r.runDirectory),"invalid receipt identity");
  requireValue(Number.isFinite(Date.parse(r.started))&&Number.isFinite(Date.parse(r.finished))&&Date.parse(r.finished)>=Date.parse(r.started),"invalid receipt times");
  requireValue(["all_required_live_phases_succeeded","failed_or_incomplete"].includes(r.reportedOutcome)&&
    (r.failure===null||typeof r.failure==="string"),"unsupported receipt status");
  exactKeys(r.checks,["sourceIdentity","compilerIdentity","packageIdentity","compilation","expectedTypeMatching","axiomAudit","definitionBodyMatching","targetKernelReplay","independentKernelReplay"],"checks");
  for(const [key,value] of Object.entries(r.checks))requireValue(
    key==="independentKernelReplay"?value==="not_performed":["not_performed","passed","failed","not_applicable"].includes(value),"unsupported check status");
  exactKeys(r.boundaries,["receiptAuthenticity","importedReceiptCanGrantPass","assumptions","dependencyCompilation","sourceRevisionAttestation","independentKernelReplay","nativeMRS"],"boundaries");
  requireValue(r.boundaries.importedReceiptCanGrantPass===false&&r.boundaries.independentKernelReplay==="not_performed"&&r.boundaries.nativeMRS==="unavailable_unvalidated", "unsupported receipt trust request");
  for(const key of ["packages","sourcesBefore","sourcesAfter","workFiles","products","phases","targets","definitions","replay"])requireValue(Array.isArray(r[key])&&r[key].length<=1000,"invalid receipt array: "+key);
  for(const s of r.sourcesBefore.concat(r.sourcesAfter)) {
    exactKeys(s,["origin","path","copyPath","bytes","sha256"],"source");
    requireValue(["project","toolkit"].includes(s.origin)&&isPortablePath(s.path)&&s.copyPath==="inputs/"+s.origin+"/"+s.path,"invalid copied source identity");
  }
  const seen=new Set();
  for(const p of r.phases) {
    exactKeys(p,["name","executable","argv","cwd","environment","started","finished","durationMs","termination","success","error","outputLimitBytes","evidence"],"phase");
    requireValue(typeof p.name==="string"&&!seen.has(p.name)&&Array.isArray(p.argv)&&p.argv.every(x=>typeof x==="string")&&typeof p.executable==="string"&&path.isAbsolute(p.cwd),"invalid phase identity");seen.add(p.name);
    exactKeys(p.termination,["kind","exitCode","signal","pid","processGroup"],"termination");
    requireValue(["exited","launch_failed","log_io_failure","interrupted","timeout","output_limit"].includes(p.termination.kind),"unsupported process termination");
    requireValue(p.success===(p.termination.kind==="exited"&&p.termination.exitCode===0&&p.termination.signal===null),"contradictory process success");
    exactKeys(p.evidence,["stdout","stderr"],"phase evidence");
    for(const channel of ["stdout","stderr"])requireValue(p.evidence[channel].path==="logs/"+p.name+"."+channel,"phase evidence cannot reuse another log");
  }
}
async function runLive(label,repository,output,options={}) {
  requireValue(Object.prototype.hasOwnProperty.call(PLANS,label),"unsupported trusted plan; imported plans are never executed");
  requireValue(Object.keys(options).every(k=>["signal","timeoutMs"].includes(k)),"unsupported live runner option");
  requireValue(options.timeoutMs===undefined||(Number.isInteger(options.timeoutMs)&&options.timeoutMs>=1&&options.timeoutMs<=900000),"invalid live phase timeout");
  const plan=PLANS[label],repo=await fs.realpath(repository),requested=path.resolve(output),tangent=path.join(repo,"tangent-limit");
  const parent=await fs.realpath(path.dirname(requested));
  requireValue(parent===path.dirname(requested),"live output parent symlinks are rejected");
  const directory=path.join(parent,path.basename(requested));
  requireValue(!contained(tangent,directory),"live output must not be inside the published tangent project");
  requireValue(process.platform==="linux","this live runner is actually tested on Linux; other hosts are unsupported");
  const attempt=crypto.randomUUID(),started=new Date().toISOString(),phases=[],products=[],checks={
    sourceIdentity:"not_performed",compilerIdentity:"not_performed",packageIdentity:"not_performed",compilation:"not_performed",
    expectedTypeMatching:"not_performed",axiomAudit:"not_performed",definitionBodyMatching:"not_performed",targetKernelReplay:"not_performed",independentKernelReplay:"not_performed"};
  // Initial directory/marker creation shares the anchored extraction primitive;
  // parent aliases cannot redirect this first mutation into the proof project.
  await writeNewTree(directory,[{path:"attempt.json",bytes:Buffer.from(JSON.stringify({schema:"math-live-attempt/v1",attempt,label,started,state:"in_progress",locallyObservedLeanPass:false})+"\n")}]);
  let before=null,after=null,workFiles=[],compiler=null,packages=[],targets=[],definitions=[],replay=[],failure=null,lock=null;
  const env={...process.env,ELAN_HOME:path.join(tangent,".elan")};
  for(const key of ["LEAN_PATH","LEAN_SRC_PATH","LEAN_OPTS","LEAN_SYSROOT","ELAN_TOOLCHAIN","LEAN_TOOLCHAIN","LAKE_HOME"])delete env[key];
  for(const key of Object.keys(env))if(key.startsWith("LD_")||key.startsWith("GIT_"))delete env[key];
  env.PATH=path.join(env.ELAN_HOME,"bin")+path.delimiter+(process.env.PATH||"/usr/bin:/bin");
  const step=async(name,executable,argv,cwd,childEnv=env)=>{
    requireValue(!options.signal?.aborted,"live attempt interrupted before phase "+name);
    const r=await runProcess(executable,argv,{cwd,directory,name,env:childEnv,signal:options.signal,timeoutMs:options.timeoutMs||300000});
    phases.push(r);
    requireValue(r.success,"phase "+name+" ended "+r.termination.kind+" with exit "+r.termination.exitCode);
    return readRegular(path.join(directory,r.evidence.stdout.path),r.outputLimitBytes);
  };
  const inspectPackages=async suffix=>{
    const observed=[];
    for(const pkg of lock.packages) {
      requireValue(isPortablePath(pkg.name)&&!pkg.name.includes("/")&&pkg.type==="git"&&/^[0-9a-f]{40}$/.test(pkg.rev),"unsupported pinned package identity");
      const pkgDir=path.join(tangent,".lake/packages",pkg.name),stem="package-"+pkg.name+"-";
      const git=(name,args)=>step(stem+name+suffix,"/usr/bin/git",["-c","core.fsmonitor=false",...args],pkgDir);
      const rev=decodeUTF8(await git("revision",["rev-parse","HEAD"])).trim();requireValue(rev===pkg.rev,"actual package revision mismatch: "+pkg.name);
      const origin=decodeUTF8(await git("origin",["remote","get-url","origin"])).trim();
      requireValue(origin.replace(/\.git$/,"")===pkg.url.replace(/\.git$/,""),"package origin mismatch: "+pkg.name);
      await git("tracked-diff",["diff","--no-ext-diff","--no-textconv","--exit-code","HEAD","--"]);
      observed.push({name:pkg.name,revision:rev,origin,trackedSourceDiff:"clean",cacheEvidence:"trusted_existing_olean_cache_not_rebuilt"});
    }
    return observed;
  };
  try {
    before=await sources(repo,plan);
    const staged=[...before.bytes].map(([name,bytes])=>({path:name,bytes}));
    const addBuild=(original,destination,origin)=>{
      const b=before.bytes.get(origin+"/"+original);requireValue(b,"missing reviewed build source");
      staged.push({path:"build/"+destination,bytes:b});workFiles.push({path:"inputs/build/"+destination,bytes:b.length,sha256:hash(b)});
    };
    for(const m of plan.modules)addBuild(m.source,m.destination,label==="tangent"?"project":"toolkit");
    addBuild("lean/EvidenceHarness.lean","EvidenceHarness.lean","toolkit");
    addBuild(plan.typeHarness,"ExpectedTypes.lean","toolkit");
    addBuild(plan.replayHarness,"Replay.lean","toolkit");
    if(plan.definitionHarness)addBuild(plan.definitionHarness,"ExpectedDefinitions.lean","toolkit");
    await writeNewTree(path.join(directory,"inputs"),staged);
    const leanCandidates=[path.join(env.ELAN_HOME,"toolchains/v4.24.0/bin/lean"),path.join(env.ELAN_HOME,"toolchains/leanprover--lean4---v4.24.0/bin/lean")];
    let lean;
    for(const candidate of leanCandidates){try{lean=await fs.realpath(candidate);break;}catch(e){if(e.code!=="ENOENT")throw e;}}
    requireValue(lean,"official pinned Lean installation unavailable");
    const binary=await readRegular(lean,33554432);
    checkReleaseMember("lean",{bytes:binary.length,sha256:hash(binary)});
    const libdir=path.resolve(path.dirname(lean),"../lib/lean"),runtimeLibraries=[];
    for(const name of ["libleanshared.so","libleanshared_1.so","libleanshared_2.so","libInit_shared.so"]){const item=await hashRegular(path.join(libdir,name));checkReleaseMember(name,item);runtimeLibraries.push(item);}
    const version=decodeUTF8(await step("compiler-version",lean,["--version"],tangent)).trim();
    requireValue(version.includes("version 4.24.0,")&&version.includes("commit "+COMPILER_COMMIT),"actual compiler identity differs from pin");
    const commit=decodeUTF8(await step("compiler-commit",lean,["--githash"],tangent)).trim();requireValue(commit===COMPILER_COMMIT,"compiler Git hash mismatch");
    compiler={path:lean,bytes:binary.length,sha256:hash(binary),version,commit,runtimeLibraries};checks.compilerIdentity="passed";
    lock=parseStrict(decodeUTF8(before.bytes.get("project/tangent-limit/lake-manifest.json")));
    packages=await inspectPackages("");
    checks.packageIdentity="passed";
    const lake=path.join(env.ELAN_HOME,"bin/lake");
    const pathText=decodeUTF8(await step("dependency-search-path",lake,["env","/usr/bin/printenv","LEAN_PATH"],tangent)).trim();
    const originalOutput=path.join(tangent,".lake/build/lib/lean");
    const dependencyPaths=pathText.split(path.delimiter).map(p=>path.resolve(tangent,p)).filter(p=>p!==originalOutput);
    requireValue(dependencyPaths.length===lock.packages.length+1&&dependencyPaths.every(p=>path.isAbsolute(p)),"unsupported Lake dependency search path");
    for(const pkg of lock.packages)requireValue(dependencyPaths.includes(path.join(tangent,".lake/packages",pkg.name,".lake/build/lib/lean")),"dependency search path missing pinned package");
    requireValue(dependencyPaths.includes(libdir),"core dependency search path differs from actual pinned compiler");
    const work=path.join(directory,"inputs/build"),cache=path.join(directory,"cache");await fs.mkdir(cache);
    const leanEnv={...env,LEAN_PATH:[cache,...dependencyPaths].join(path.delimiter)};
    const compile=async(name,source,module)=>{
      const olean="cache/"+module.split(".").join("/")+".olean";await fs.mkdir(path.dirname(path.join(directory,olean)),{recursive:true});
      await step(name,lean,["--json","--root="+work,"-o",path.join(directory,olean),path.join(work,source)],work,leanEnv);
      products.push(await artifact(await sourceReader(directory),olean));
    };
    await compile("compile-evidence-helper","EvidenceHarness.lean","EvidenceHarness");
    for(let i=0;i<plan.modules.length;i++) {
      const m=plan.modules[i];await compile("compile-target-"+i,m.destination,m.module);
    }
    checks.compilation="passed";
    await compile("expected-type-and-axiom-audit","ExpectedTypes.lean","ExpectedTypes");
    const typePhase=phases[phases.length-1];
    targets=parseMarkers(await readRegular(path.join(directory,typePhase.evidence.stdout.path),typePhase.outputLimitBytes),"MATH_EVIDENCE_TARGET ");
    checkTargets(targets,plan);checks.expectedTypeMatching="passed";checks.axiomAudit="passed";
    if(plan.definitionHarness) {
      await compile("definition-body-matching","ExpectedDefinitions.lean","ExpectedDefinitions");
      const p=phases[phases.length-1];definitions=parseMarkers(await readRegular(path.join(directory,p.evidence.stdout.path),p.outputLimitBytes),"MATH_EVIDENCE_DEFINITION ");
      checkDefinitions(definitions,plan);checks.definitionBodyMatching="passed";
    } else checks.definitionBodyMatching="not_applicable";
    await compile("target-kernel-replay","Replay.lean","Replay");
    const replayPhase=phases[phases.length-1];replay=parseMarkers(await readRegular(path.join(directory,replayPhase.evidence.stdout.path),replayPhase.outputLimitBytes),"MATH_EVIDENCE_REPLAY ");
    checkReplay(replay,plan);checks.targetKernelReplay="passed";
  } catch(e){failure=String(e.message);}
  try {
    if(before) {
      if(compiler)checks.compilerIdentity="not_performed";
      if(packages.length)checks.packageIdentity="not_performed";
      after=await sources(repo,plan);
      requireValue(sourceIdentity(before.entries)===sourceIdentity(after.entries),"source or trusted runner changed during attempt");
      const reader=await sourceReader(directory);
      for(const item of before.entries)requireValue(hash(await reader(item.copyPath))===item.sha256,"copied source changed: "+item.copyPath);
      for(const item of workFiles)requireValue(hash(await reader(item.path))===item.sha256,"compiled working source changed: "+item.path);
      if(compiler) {
        try {
          requireValue(hash(await readRegular(compiler.path,33554432))===compiler.sha256,"compiler binary changed during attempt");
          for(const item of compiler.runtimeLibraries){const current=await hashRegular(item.path);requireValue(current.sha256===item.sha256&&current.bytes===item.bytes,"Lean kernel runtime library changed during attempt");}
          checks.compilerIdentity="passed";
        } catch(e){checks.compilerIdentity="failed";throw e;}
      }
      if(lock&&packages.length===lock.packages.length&&!options.signal?.aborted) {
        try {
          const packageAfter=await inspectPackages("-post");
          requireValue(canonicalJSON(packageAfter)===canonicalJSON(packages),"package identity changed during attempt");
          checks.packageIdentity="passed";
        } catch(e){checks.packageIdentity="failed";throw e;}
      } else checks.packageIdentity="failed";
      // A missing/tampered capture is a failure even after a successful command.
      for(const p of phases)for(const item of Object.values(p.evidence))requireValue(hash(await reader(item.path))===item.sha256,"phase evidence changed: "+item.path);
      for(const item of products)requireValue(hash(await reader(item.path))===item.sha256,"compiled product changed: "+item.path);
      checks.sourceIdentity="passed";
    }
  } catch(e){checks.sourceIdentity="failed";failure=failure||String(e.message);}
  if(options.signal?.aborted&&!failure)failure="live attempt interrupted";
  const required=["sourceIdentity","compilerIdentity","packageIdentity","compilation","expectedTypeMatching","axiomAudit","targetKernelReplay"];
  const locallyObservedLeanPass=!failure&&!options.signal?.aborted&&required.every(k=>checks[k]==="passed")&&
    ["passed","not_applicable"].includes(checks.definitionBodyMatching)&&phases.every(p=>p.success);
  const receipt={schema:"math-live-receipt/v1",attempt,plan:label,started,finished:new Date().toISOString(),
    sourceRevision:REVISION,repository:repo,runDirectory:directory,reportedOutcome:locallyObservedLeanPass?"all_required_live_phases_succeeded":"failed_or_incomplete",failure,
    checks,compiler,packages,sourcesBefore:before?.entries||[],sourcesAfter:after?.entries||[],workFiles,products,phases,targets,definitions,replay,
    boundaries:{receiptAuthenticity:"not_established_by_hashes",importedReceiptCanGrantPass:false,
      assumptions:label==="tangent"?"explicit_PiDiophantine_premise_remains_unproved":"fixture_specific",dependencyCompilation:"trusted_existing_pinned_olean_cache",
      sourceRevisionAttestation:"exact_published_project_file_pins",independentKernelReplay:"not_performed",nativeMRS:"unavailable_unvalidated"}};
  await fs.writeFile(path.join(directory,"receipt.json"),canonicalJSON(receipt)+"\n",{flag:"wx"});
  return {ok:locallyObservedLeanPass,locallyObservedLeanPass,attempt,plan:label,directory,checks,failure,receipt};
}

async function inspectReceipt(directoryName) {
  const directory=await fs.realpath(directoryName),reader=await sourceReader(directory),r=await readJSON(path.join(directory,"receipt.json"));
  validateReceiptStructure(r);
  const evidence=[],paths=new Set();
  for(const item of [...r.sourcesBefore.map(s=>({path:s.copyPath,bytes:s.bytes,sha256:s.sha256})),...r.workFiles,...r.products,
    ...r.phases.flatMap(p=>Object.values(p.evidence))]) {
    requireValue(isPortablePath(item.path)&&!paths.has(item.path)&&Number.isSafeInteger(item.bytes)&&item.bytes>=0&&/^[0-9a-f]{64}$/.test(item.sha256),"invalid or duplicate receipt artifact");
    paths.add(item.path);const bytes=await reader(item.path);
    requireValue(bytes.length===item.bytes&&hash(bytes)===item.sha256,"receipt evidence missing or changed: "+item.path);evidence.push(item.path);
  }
  if(r.reportedOutcome==="all_required_live_phases_succeeded") {
    const plan=PLANS[r.plan],catalog=await readJSON(path.join(directory,"inputs/toolkit/samples/catalog.json"));
    await acceptTangent(catalog,p=>reader("inputs/project/"+p),hash);
    const expectedSources=[...catalog.files.map(f=>"project/"+f.path),...[...new Set(CODE_FILES.concat(plan.toolkitFiles))].map(p=>"toolkit/"+p)].sort();
    requireValue(canonicalJSON(r.sourcesBefore.map(s=>s.origin+"/"+s.path).sort())===canonicalJSON(expectedSources)&&
      sourceIdentity(r.sourcesBefore)===sourceIdentity(r.sourcesAfter),"successful receipt source closure absent or changed");
    for(const s of r.sourcesBefore)if(s.origin==="toolkit"&&TRUSTED_FILES[s.path])requireValue(s.sha256===TRUSTED_FILES[s.path],"receipt trusted Lean source differs from fixed pin");
    const buildBindings=[...plan.modules.map(m=>({destination:m.destination,origin:r.plan==="tangent"?"project":"toolkit",source:m.source})),
      {destination:"EvidenceHarness.lean",origin:"toolkit",source:"lean/EvidenceHarness.lean"},
      {destination:"ExpectedTypes.lean",origin:"toolkit",source:plan.typeHarness},
      {destination:"Replay.lean",origin:"toolkit",source:plan.replayHarness},
      ...(plan.definitionHarness?[{destination:"ExpectedDefinitions.lean",origin:"toolkit",source:plan.definitionHarness}]:[])];
    const expectedWork=buildBindings.map(b=>"inputs/build/"+b.destination).sort();
    requireValue(canonicalJSON(r.workFiles.map(f=>f.path).sort())===canonicalJSON(expectedWork),"successful receipt build input coverage incomplete");
    for(const binding of buildBindings){
      const source=r.sourcesBefore.find(s=>s.origin===binding.origin&&s.path===binding.source),
        work=r.workFiles.find(w=>w.path==="inputs/build/"+binding.destination);
      requireValue(source&&work&&source.bytes===work.bytes&&source.sha256===work.sha256,"compiled working bytes differ from preserved reviewed source: "+binding.destination);
    }
    const expectedProducts=[...plan.modules.map(m=>"cache/"+m.module.split(".").join("/")+".olean"),"cache/EvidenceHarness.olean","cache/ExpectedTypes.olean","cache/Replay.olean",...(plan.definitionHarness?["cache/ExpectedDefinitions.olean"]:[])].sort();
    requireValue(canonicalJSON(r.products.map(f=>f.path).sort())===canonicalJSON(expectedProducts),"successful receipt compilation products incomplete");
    const lock=parseStrict(decodeUTF8(await reader("inputs/project/tangent-limit/lake-manifest.json")));
    requireValue(canonicalJSON(r.phases.map(p=>p.name))===canonicalJSON(expectedPhaseNames(plan,lock)),"successful receipt phase coverage incomplete");
    requireValue(r.failure===null&&r.phases.every(p=>p.success)&&Object.entries(r.checks).every(([k,v])=>k==="independentKernelReplay"?v==="not_performed":k==="definitionBodyMatching"?v===(plan.definitionHarness?"passed":"not_applicable"):v==="passed"),"successful receipt has failed or incomplete checks");
    checkCompilerRelease(r.compiler);
    const phaseBytes=async name=>reader(r.phases.find(p=>p.name===name).evidence.stdout.path);
    const targetRecords=parseMarkers(await phaseBytes("expected-type-and-axiom-audit"),"MATH_EVIDENCE_TARGET ");
    checkTargets(targetRecords,plan);requireValue(canonicalJSON(targetRecords)===canonicalJSON(r.targets),"stored target audit differs from captured messages");
    const replayRecords=parseMarkers(await phaseBytes("target-kernel-replay"),"MATH_EVIDENCE_REPLAY ");
    checkReplay(replayRecords,plan);requireValue(canonicalJSON(replayRecords)===canonicalJSON(r.replay),"stored kernel replay differs from captured messages");
    if(plan.definitionHarness){const defs=parseMarkers(await phaseBytes("definition-body-matching"),"MATH_EVIDENCE_DEFINITION ");checkDefinitions(defs,plan);requireValue(canonicalJSON(defs)===canonicalJSON(r.definitions),"stored definition audit differs from captured messages");}
    else requireValue(r.definitions.length===0,"unexpected definition body claim");
  }
  // Imported bytes can establish only internal integrity, never the historical
  // authenticity of process events or a new locally observed Lean pass.
  return {ok:true,kind:"receipt_integrity_only",integrityStatus:r.reportedOutcome==="all_required_live_phases_succeeded"?"complete_reported_execution_closure":"failed_or_incomplete_attempt",reportedOutcome:r.reportedOutcome,evidenceFiles:evidence.length,
    locallyObservedLeanPass:false,leanPass:false,receiptAuthenticity:"not_established",independentKernelReplay:"not_performed"};
}
async function main(argv) {
  const [command,...args]=argv;
  if(command==="inspect-receipt"&&args.length===1)return inspectReceipt(args[0]);
  if(command==="run"&&args.length===3) {
    const abort=new AbortController(),onSignal=()=>abort.abort();process.on("SIGINT",onSignal);process.on("SIGTERM",onSignal);
    try {const r=await runLive(args[0],args[1],args[2],{signal:abort.signal});if(!r.ok)process.exitCode=2;return {...r,receipt:undefined};}
    finally {process.removeListener("SIGINT",onSignal);process.removeListener("SIGTERM",onSignal);}
  }
  throw new Error("Usage: node live.cjs run TRUSTED_PLAN REPOSITORY_ROOT NEW_RUN_DIRECTORY | inspect-receipt RUN_DIRECTORY");
}
if(require.main===module)main(process.argv.slice(2)).then(r=>console.log(JSON.stringify(r,null,2))).catch(e=>{console.error(JSON.stringify({ok:false,locallyObservedLeanPass:false,message:e.message}));process.exitCode=2;});
module.exports={runLive,inspectReceipt,leanMessages,checkTargets,checkDefinitions,checkReplay,validateReceiptStructure};
