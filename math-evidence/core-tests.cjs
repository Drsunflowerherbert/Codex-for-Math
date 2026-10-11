"use strict";
// Synthetic import tests; no Lean process is started.
async function runCoreTests(core, hashBytes, runtime = 'unspecified_JavaScript_runtime') {
  const clone = x => JSON.parse(JSON.stringify(x));
  const digest = s => hashBytes(core.encodeUTF8(s));
  const results = [];
  function fixture() {
    const snippets = {
      pi: "def PiDiophantine : Prop := True",
      parameter: "def parameter : Nat := 1",
      valid: "theorem valid (h : PiDiophantine) : True"
    };
    const texts = {
      "Fixture.lean": "namespace Fixture\n" + snippets.pi + "\n" + snippets.parameter + "\n" + snippets.valid + " := by trivial\nend Fixture\n",
      "lean-toolchain": "leanprover/lean4:v4.24.0\n",
      "lake-manifest.json": JSON.stringify({packages:[{name:"mathlib",type:"git",url:"https://github.com/leanprover-community/mathlib4",rev:"a".repeat(40)}]}) + "\n",
      "review.txt": "Ordinary review report for synthetic Fixture.valid; not a Lean receipt.\n",
      "experiment.txt": "Synthetic finite experiment: n in {1,2,3}; no universal claim.\n",
      "legacy.log": "Synthetic historical build report; not a new live run.\n"
    };
    const roles = {"Fixture.lean":"source","lean-toolchain":"toolchain","lake-manifest.json":"lockfile","review.txt":"review","experiment.txt":"experiment","legacy.log":"legacy_log"};
    const files = new Map(Object.entries(texts).map(([p,s])=>[p,core.encodeUTF8(s)]));
    const record=(id,kind,name,text)=>({
      id,kind,name,statement:{text,source_path:"Fixture.lean",source_excerpt:text,sha256:digest(text)},
      assumptions:[],dependencies:[],
      sources:[{url:"https://example.org/synthetic/Fixture.lean",revision:"b".repeat(40),locator:name}],
      review:{status:"not_reviewed",evidence:[]},experiments:[],
      lean:{status:"not_run",evidence:[],reason:"Synthetic fixture; no Lean run performed"}
    });
    const pi=record("pi","assumption","Fixture.PiDiophantine",snippets.pi);
    const parameter=record("parameter","definition","Fixture.parameter",snippets.parameter);
    const valid=record("valid","theorem","Fixture.valid",snippets.valid);
    valid.assumptions=["pi"];valid.dependencies=["parameter","pi"];
    valid.review={status:"review_reported",evidence:["review.txt"]};
    valid.experiments=[{claim:"Synthetic finite data exist",scope:"Only n in {1,2,3}; unverified report",evidence:["experiment.txt"]}];
    valid.lean={status:"historical_report",evidence:["legacy.log"],reason:"Historical log is an attachment, never a Lean pass"};
    const catalog={schema:"math-exchange/v1",project:{repository:"https://example.org/synthetic",revision:"b".repeat(40),branch:"fixtures",lean_toolchain:"leanprover/lean4:v4.24.0",mathlib_revision:"a".repeat(40)},
      files:Object.keys(texts).map(path=>({path,sha256:hashBytes(files.get(path)),role:roles[path]})),records:[pi,parameter,valid]};
    return {catalog,files,snippets};
  }
  function repin(f,path,bytes) {
    f.files.set(path, typeof bytes === "string" ? core.encodeUTF8(bytes) : bytes);
    f.catalog.files.find(x=>x.path===path).sha256=hashBytes(f.files.get(path));
  }
  async function test(name, mutate, expectedCode, options) {
    const f=fixture(); if(mutate)mutate(f);
    let reads=0,result,error;
    const reader=options?.reader || (p=>{reads++;if(!f.files.has(p))throw new Error("Fixture file missing");return f.files.get(p);});
    try { result=await core.validate(f.catalog,reader,options?.hasher || hashBytes); }
    catch(e){error=e;}
    const codes=error?.errors?.map(e=>e.code) || [];
    let pass=expectedCode ? error?.code==="VALIDATION_FAILED" && codes.includes(expectedCode) : result?.ok===true;
    if(options?.noReads && reads!==0)pass=false;
    if(options?.assert && !options.assert(result,error,f))pass=false;
    results.push({name,pass,expected:expectedCode||"accepted_without_Lean_pass",observedCodes:[...new Set(codes)],reads});
  }
  await test("valid_catalog_independent_status_counts",null,null,{assert:r=>r.summary.counts.leanPasses===0 && r.summary.counts.historicalLeanReports===1 && r.summary.counts.reviewReported===1 && r.summary.counts.experimentReports===1 && r.summary.topologicalOrder.indexOf("pi")<r.summary.topologicalOrder.indexOf("valid") && r.inventory.includes("Lean passes: 0")});
  await test("unreviewed_not_run_valid",f=>{f.catalog.records.forEach(r=>{r.review={status:"not_reviewed",evidence:[]};r.experiments=[];r.lean={status:"not_run",evidence:[],reason:"Never run"};});},null,{assert:r=>r.summary.counts.leanPasses===0});
  for(const status of ["pass","checked","kernel_verified","compilation_success"])
    await test("unsupported_lean_"+status,f=>f.catalog.records[2].lean.status=status,"unsupported_value",{noReads:true});
  await test("unsupported_ordinary_review_upgrade",f=>f.catalog.records[2].review.status="pass","unsupported_value",{noReads:true});
  await test("unknown_command_field_rejected",f=>f.catalog.records[2].command="touch /tmp/should-never-run","unknown_field",{noReads:true});
  await test("command_text_is_inert_prose",f=>f.catalog.records[2].lean.reason="`touch /tmp/should-never-run` is imported text only",null,{assert:r=>r.summary.counts.leanPasses===0});
  await test("missing_required_field",f=>delete f.catalog.records[2].assumptions,"missing_field",{noReads:true});
  await test("malformed_dependency",f=>f.catalog.records[2].dependencies=["bad/id"],"format",{noReads:true});
  await test("dead_dependency",f=>f.catalog.records[2].dependencies=["missing"],"dead_reference",{noReads:true});
  await test("dependency_cycle",f=>f.catalog.records[1].dependencies=["valid"],"dependency_cycle",{noReads:true});
  await test("assumption_dependency_cycle",f=>f.catalog.records[0].dependencies=["valid"],"dependency_cycle",{noReads:true});
  await test("self_dependency_cycle",f=>f.catalog.records[2].dependencies=["valid"],"dependency_cycle",{noReads:true});
  await test("duplicate_identifier",f=>f.catalog.records[1].id="pi","duplicate_id",{noReads:true});
  await test("duplicate_Lean_name",f=>f.catalog.records[1].name="Fixture.PiDiophantine","duplicate_name",{noReads:true});
  await test("duplicate_dependency",f=>f.catalog.records[2].dependencies=["parameter","parameter"],"duplicate_reference",{noReads:true});
  await test("assumption_wrong_kind",f=>f.catalog.records[2].assumptions=["parameter"],"assumption_kind",{noReads:true});
  await test("direct_assumption_not_declared",f=>f.catalog.records[2].assumptions=[],"undeclared_assumption",{noReads:true});
  await test("missing_manifest_evidence",f=>f.catalog.records[2].review.evidence=["absent.txt"],"missing_file_reference",{noReads:true});
  await test("review_wrong_evidence_role",f=>f.catalog.records[2].review.evidence=["legacy.log"],"evidence_role",{noReads:true});
  await test("experiment_wrong_evidence_role",f=>f.catalog.records[2].experiments[0].evidence=["review.txt"],"evidence_role",{noReads:true});
  await test("historical_wrong_evidence_role",f=>f.catalog.records[2].lean.evidence=["experiment.txt"],"evidence_role",{noReads:true});
  await test("historical_report_without_attachment",f=>f.catalog.records[2].lean.evidence=[],"type",{noReads:true});
  await test("not_run_with_old_log",f=>f.catalog.records[2].lean.status="not_run","inconsistent_status",{noReads:true});
  await test("review_report_without_attachment",f=>f.catalog.records[2].review.evidence=[],"type",{noReads:true});
  await test("experiment_without_evidence",f=>f.catalog.records[2].experiments[0].evidence=[],"type",{noReads:true});
  await test("missing_evidence_bytes",f=>f.files.delete("review.txt"),"file_read");
  await test("tampered_review_bytes",f=>f.files.set("review.txt",core.encodeUTF8("altered evidence")),"file_hash_mismatch");
  await test("tampered_experiment_bytes",f=>f.files.set("experiment.txt",core.encodeUTF8("altered experiment")),"file_hash_mismatch");
  await test("tampered_historical_log_bytes",f=>f.files.set("legacy.log",core.encodeUTF8("fake success")),"file_hash_mismatch");
  await test("empty_hash_matched_evidence",f=>repin(f,"review.txt",""),"empty_evidence");
  await test("source_drift_original_manifest",f=>f.files.set("Fixture.lean",core.encodeUTF8("altered source")),"file_hash_mismatch");
  await test("source_drift_repin_loses_statement",f=>repin(f,"Fixture.lean","namespace Fixture\ndef PiDiophantine : Prop := True\ndef parameter : Nat := 1\nend Fixture\n"),"source_excerpt_missing");
  await test("wrong_claim_detached_from_source",f=>f.catalog.records[2].statement.text="theorem valid (h : PiDiophantine) : False","statement_excerpt_mismatch",{noReads:true});
  await test("wrong_statement_text_and_excerpt",f=>{f.catalog.records[2].statement.text=f.catalog.records[2].statement.source_excerpt="theorem valid (h : PiDiophantine) : False";},"statement_hash_mismatch");
  await test("rehashed_wrong_statement_absent",f=>{const s=f.catalog.records[2].statement;s.text=s.source_excerpt="theorem valid (h : PiDiophantine) : False";s.sha256=digest(s.text);},"source_excerpt_missing");
  await test("wrong_declaration_short_name",f=>f.catalog.records[2].name="Fixture.other","declaration_heuristic",{noReads:true});
  await test("ambiguous_source_excerpt",f=>repin(f,"Fixture.lean",core.decodeUTF8(f.files.get("Fixture.lean"))+"\n"+f.snippets.valid+"\n"),"source_excerpt_ambiguous");
  await test("toolchain_bytes_drift",f=>repin(f,"lean-toolchain","leanprover/lean4:v4.25.0\n"),"toolchain_drift");
  await test("mathlib_lock_revision_drift",f=>repin(f,"lake-manifest.json",JSON.stringify({packages:[{name:"mathlib",type:"git",url:"https://github.com/leanprover-community/mathlib4",rev:"c".repeat(40)}]})),"mathlib_drift");
  await test("duplicate_mathlib_lock_entries",f=>repin(f,"lake-manifest.json",JSON.stringify({packages:[{name:"mathlib",type:"git",url:"https://github.com/leanprover-community/mathlib4",rev:"a".repeat(40)},{name:"mathlib",type:"git",url:"https://github.com/leanprover-community/mathlib4",rev:"a".repeat(40)}]})),"mathlib_drift");
  await test("malformed_lock_json",f=>repin(f,"lake-manifest.json","{"),"lockfile_parse");
  await test("unknown_toolchain_count",f=>f.catalog.files[1].role="source","toolchain_count",{noReads:true});
  await test("invalid_UTF8_source",f=>repin(f,"Fixture.lean",Uint8Array.from([0xc0,0x80])),"invalid_utf8");
  await test("unpaired_surrogate_input",f=>f.catalog.records[2].lean.reason="\ud800","invalid_json_data",{noReads:true});
  await test("unsafe_parent_path",f=>f.catalog.files[0].path="../Fixture.lean","unsafe_path",{noReads:true});
  await test("unsafe_absolute_path",f=>f.catalog.files[0].path="/Fixture.lean","unsafe_path",{noReads:true});
  await test("unsafe_backslash_path",f=>f.catalog.files[0].path="dir\\Fixture.lean","unsafe_path",{noReads:true});
  await test("windows_reserved_path",f=>f.catalog.files[0].path="NUL.lean","unsafe_path",{noReads:true});
  await test("case_collision",f=>f.catalog.files.push({...f.catalog.files[0],path:"fixture.lean"}),"duplicate_file",{noReads:true});
  await test("duplicate_file",f=>f.catalog.files.push(clone(f.catalog.files[0])),"duplicate_file",{noReads:true});
  await test("uppercase_hash_rejected",f=>f.catalog.files[0].sha256=f.catalog.files[0].sha256.toUpperCase(),"format",{noReads:true});
  await test("short_project_revision",f=>f.catalog.project.revision="main","format",{noReads:true});
  await test("source_branch_instead_of_exact_revision",f=>f.catalog.records[2].sources[0].revision="main","format",{noReads:true});
  await test("hash_adapter_malformed",null,"hash_adapter",{hasher:()=> "not-a-sha256"});
  await test("reader_wrong_type",null,"file_read",{reader:()=> []});
  await test("interrupted_reader_rejected",null,"file_read",{reader:()=>{throw new Error("Synthetic interrupted read: SIGTERM");}});
  await test("interrupted_log_stays_historical",f=>repin(f,"legacy.log","Synthetic build interrupted by SIGTERM; no exit success recorded.\n"),null,{assert:r=>r.summary.counts.leanPasses===0&&r.summary.counts.historicalLeanReports===1});
  await test("author_repin_is_not_revision_attestation",f=>repin(f,"Fixture.lean",core.decodeUTF8(f.files.get("Fixture.lean"))+"\n-- synthetic harmless source edit\n"),null,{assert:r=>r.summary.counts.leanPasses===0&&r.summary.statementBinding==="textual_excerpt_only"});
  await test("async_hash_and_reader",null,null,{hasher:async b=>hashBytes(b),reader:async p=>fixture().files.get(p),assert:r=>r.summary.counts.leanPasses===0});
  await test("uppercase_record_identifiers",f=>{f.catalog.records[0].id="Fixture.PiDiophantine";f.catalog.records[2].assumptions=["Fixture.PiDiophantine"];f.catalog.records[2].dependencies=["parameter","Fixture.PiDiophantine"];},null);
  await test("file_directory_prefix_collision",f=>f.catalog.files.push({path:"Fixture.lean/sub.lean",role:"source",sha256:"0".repeat(64)}),"path_prefix_collision",{noReads:true});
  await test("case_folded_prefix_collision",f=>f.catalog.files.push({path:"fixture.lean/sub.lean",role:"source",sha256:"0".repeat(64)}),"path_prefix_collision",{noReads:true});
  await test("fake_mathlib_repository",f=>repin(f,"lake-manifest.json",JSON.stringify({packages:[{name:"mathlib",type:"git",url:"https://example.org/fake-mathlib",rev:"a".repeat(40)}]})),"mathlib_drift");
  await test("non_git_mathlib",f=>repin(f,"lake-manifest.json",JSON.stringify({packages:[{name:"mathlib",type:"path",url:"https://github.com/leanprover-community/mathlib4",rev:"a".repeat(40)}]})),"mathlib_drift");
  await test("duplicate_lockfile_rev_key",f=>repin(f,"lake-manifest.json",'{"packages":[{"name":"mathlib","type":"git","url":"https://github.com/leanprover-community/mathlib4","rev":"'+"c".repeat(40)+'","rev":"'+"a".repeat(40)+'"}]}'),"lockfile_parse");
  await test("duplicate_decoded_lockfile_key",f=>repin(f,"lake-manifest.json",'{"packages":[{"name":"mathlib","type":"git","url":"https://github.com/leanprover-community/mathlib4","rev":"'+"c".repeat(40)+'","r\\u0065v":"'+"a".repeat(40)+'"}]}'),"lockfile_parse");
  await test("duplicate_lockfile_packages_key",f=>repin(f,"lake-manifest.json",'{"packages":[],"packages":[{"name":"mathlib","type":"git","url":"https://github.com/leanprover-community/mathlib4","rev":"'+"a".repeat(40)+'"}]}'),"lockfile_parse");
  await test("lockfile_unpaired_surrogate",f=>repin(f,"lake-manifest.json",'{"packages":[],"x":"\\ud800"}'),"lockfile_parse");
  await test("lockfile_nonfinite_number",f=>repin(f,"lake-manifest.json",'{"packages":[],"x":1e999}'),"lockfile_parse");
  await test("malformed_files_type",f=>f.catalog.files=null,"type",{noReads:true});
  await test("explicit_completeness_limitations",null,null,{assert:r=>r.summary.assumptionCompleteness==="not_established" && r.summary.dependencyCompleteness==="not_established" && r.summary.experimentScopeValidation==="not_established"});
  results.push({name:"unvalidated_inventory_not_exported",pass:!("inventory" in core),expected:"no_raw_inventory_API",observedCodes:[],reads:0});
  const f=fixture();
  const snapshotResult=await core.validate(f.catalog,p=>{f.catalog.records[2].lean.status="pass";return f.files.get(p);},hashBytes);
  results.push({name:"catalog_snapshot_resists_mutation_during_read",pass:snapshotResult.catalog.records[2].lean.status==="historical_report",expected:"snapshot_preserved",observedCodes:[],reads:f.catalog.files.length});
  const unicode = "ℝ π ∀ n : ℕ, 😀";
  results.push({name:"UTF8_roundtrip_unicode",pass:core.decodeUTF8(core.encodeUTF8(unicode))===unicode,expected:"exact_roundtrip",observedCodes:[],reads:0});
  results.push({name:"UTF8_astral_bytes",pass:[...core.encodeUTF8("😀")].join(",")==="240,159,152,128",expected:"RFC3629_bytes",observedCodes:[],reads:0});
  return {runtime,suite:"synthetic-core-adversarial-v1",total:results.length,passed:results.filter(r=>r.pass).length,failed:results.filter(r=>!r.pass),results};
}
module.exports = { runCoreTests };
if (require.main === module) {
  const core = require('./core.cjs');
  const { createHash } = require('node:crypto');
  const hash = bytes => createHash('sha256').update(bytes).digest('hex');
  runCoreTests(core, hash, 'Node.js').then(report => {
    process.stdout.write(JSON.stringify(report, null, 2) + '\n');
    process.exitCode = report.failed.length ? 1 : 0;
  }).catch(error => { console.error(error); process.exitCode = 1; });
}
