"use strict";
const core = require("./core.cjs");
const strict = require("./strict-json.cjs");
const bundle = require("./bundle.cjs");
const pins = require("./tangent-pins.cjs");
const {sha256:hash,utf8} = require("./test-hash.cjs");
async function runTests(corpus, runtime = "unspecified_JavaScript_runtime") {
  const checks = [];
  const assert = (condition,message) => { if (!condition) throw new Error(message); };
  const clone = value => strict.parseStrict(strict.canonicalJSON(value));
  const original = await bundle.readBundle(corpus,hash);
  const base = original.catalog, bytes = original.files;
  const reader = files => path => {
    if (!files.has(path)) throw new Error("missing fixture bytes");
    return Uint8Array.from(files.get(path));
  };
  async function pass(name,fn) { await fn(); checks.push({name,result:"passed"}); }
  async function reject(name,fn,code) {
    let caught = false;
    try { await fn(); } catch (e) {
      caught = true;
      if (code) assert(e.errors && e.errors.some(x=>x.code===code),"unexpected failure code for "+name);
    }
    assert(caught,"unexpected acceptance: "+name); checks.push({name,result:"passed"});
  }
  const validate = (catalog=clone(base),files=new Map(bytes)) => core.validate(catalog,reader(files),hash);
  const accepted = (catalog=clone(base),files=new Map(bytes)) => pins.acceptTangent(catalog,reader(files),hash);
  function mutatedFile(path,content,catalog=clone(base),files=new Map(bytes)) {
    const data=utf8(content);files.set(path,data);catalog.files.find(f=>f.path===path).sha256=hash(data);
    return {catalog,files};
  }
  const log="tangent-limit/logs/final-build.log";
  const main="TangentLimit.tan_div_cube_tendsto_zero";
  const review="tangent-limit/docs/independent-review.md";
  await pass("pinned 37 declarations and independent trust dimensions",async()=>{
    const r=await accepted();
    assert(r.records===37&&!r.leanPass,"wrong pinned summary");
    const v=await validate();assert(v.summary.counts.leanPasses===0,"a Lean pass was inferred");
    assert(v.summary.leanCompilation==="not_performed"&&v.summary.assumptionCompleteness==="not_established","trust boundary missing");
    assert(base.records.filter(r=>r.assumptions.includes("TangentLimit.PiDiophantine")).length===12,"conditional binder corpus changed");
  });
  await reject("missing attached evidence",async()=>{const f=new Map(bytes);f.delete(log);await validate(clone(base),f);},"file_read");
  await reject("tampered evidence with original digest",async()=>{const f=new Map(bytes);f.set(log,utf8("fabricated success"));await validate(clone(base),f);},"file_hash_mismatch");
  await reject("tampered source with original digest",async()=>{const f=new Map(bytes),p=base.records.find(r=>r.id===main).statement.source_path;f.set(p,utf8("theorem bogus : True := by trivial"));await validate(clone(base),f);},"file_hash_mismatch");
  await reject("empty evidence even with matching digest",async()=>{const m=mutatedFile(review,"");await validate(m.catalog,m.files);},"empty_evidence");
  await pass("self-consistent modified historical evidence is integrity only",async()=>{const m=mutatedFile(log,"self-authored historical log");await validate(m.catalog,m.files);});
  await reject("independent pins reject self-consistent modified evidence",async()=>{const m=mutatedFile(log,"self-authored historical log");await accepted(m.catalog,m.files);});
  await pass("generic metadata omission does not establish assumption completeness",async()=>{const c=clone(base);c.records.find(r=>r.id===main).assumptions=[];const r=await validate(c);assert(r.summary.assumptionCompleteness==="not_established","misleading completeness");});
  await reject("tangent pins reject omitted PiDiophantine metadata",async()=>{const c=clone(base);c.records.find(r=>r.id===main).assumptions=[];await accepted(c);});
  await reject("statement text hash drift",async()=>{const c=clone(base);c.records[0].statement.sha256="0".repeat(64);await validate(c);},"statement_hash_mismatch");
  await reject("unbound claimed statement",async()=>{const c=clone(base);c.records[0].statement.text="False";c.records[0].statement.sha256=hash(utf8("False"));await validate(c);},"statement_excerpt_mismatch");
  await reject("source excerpt drift",async()=>{const c=clone(base),s=c.records.find(r=>r.id===main).statement;s.text=s.source_excerpt=s.text.replace("nhds 0","nhds 1");s.sha256=hash(utf8(s.text));await validate(c);},"source_excerpt_missing");
  const alteredSource=()=> {
    const c=clone(base),r=c.records.find(r=>r.id===main),p=r.statement.source_path;
    const old=r.statement.text,changed=old.replace(" (h : PiDiophantine)","");
    const m=mutatedFile(p,core.decodeUTF8(bytes.get(p)).replace(old,changed),c);
    r.statement.text=r.statement.source_excerpt=changed;r.statement.sha256=hash(utf8(changed));r.assumptions=[];
    return m;
  };
  await pass("textually self-consistent invalid Lean source is never compilation",async()=>{const m=alteredSource(),r=await validate(m.catalog,m.files);assert(r.summary.leanCompilation==="not_performed","false compilation");});
  await reject("tangent pins reject coordinated source and statement drift",async()=>{const m=alteredSource();await accepted(m.catalog,m.files);});
  for (const status of ["passed","checked","kernel_verified","complete","interrupted"]) {
    await reject("unsupported Lean status "+status,async()=>{const c=clone(base);c.records[0].lean.status=status;await validate(c);},"unsupported_value");
  }
  await reject("imported commands rejected before any read",async()=>{
    const c=clone(base);c.records[0].command="touch should-never-execute";let calls=0;
    try {await core.validate(c,()=>{calls++;return new Uint8Array();},hash);}finally{assert(calls===0,"invalid imported command triggered reads");}
  },"unknown_field");
  await reject("interrupted imported receipt cannot upgrade status",async()=>{
    const c=clone(base);c.records[0].lean.receipt={exit_code:0,termination:"interrupted",claimed_status:"pass"};await validate(c);
  },"unknown_field");
  await reject("simulated interrupted reader gives failure not pass",async()=>{await core.validate(clone(base),()=>{throw new Error("simulated interruption");},hash);},"file_read");
  await reject("dead dependency",async()=>{const c=clone(base);c.records[0].dependencies=["Missing.theorem"];await validate(c);},"dead_reference");
  await reject("malformed dependency",async()=>{const c=clone(base);c.records[0].dependencies=["../escape"];await validate(c);},"format");
  await reject("dependency cycle",async()=>{const c=clone(base);c.records[0].dependencies=[c.records[1].id];c.records[1].dependencies=[c.records[0].id];await validate(c);},"dependency_cycle");
  await reject("duplicate identifiers",async()=>{const c=clone(base);c.records.push(clone(c.records[0]));await validate(c);},"duplicate_id");
  await reject("assumption reference has wrong record kind",async()=>{const c=clone(base);c.records.find(r=>r.id===main).assumptions=[c.records.find(r=>r.kind==="theorem"&&r.id!==main).id];await validate(c);},"assumption_kind");
  await reject("duplicate manifest path",async()=>{const c=clone(base);c.files.push(clone(c.files[0]));await validate(c);},"duplicate_file");
  await reject("case-colliding paths",async()=>{const c=clone(base),f=clone(c.files[0]);f.path=f.path.toUpperCase();c.files.push(f);await validate(c);},"duplicate_file");
  await reject("file directory prefix collision",async()=>{const c=clone(base),f=clone(c.files[0]);f.path=c.files[0].path+"/child.txt";c.files.push(f);await validate(c);});
  await reject("traversal path",async()=>{const c=clone(base);c.files[0].path="../escape";await validate(c);},"unsafe_path");
  await reject("absolute path",async()=>{const c=clone(base);c.files[0].path="/escape";await validate(c);},"unsafe_path");
  await reject("Windows reserved path",async()=>{const c=clone(base);c.files[0].path="CON.txt";await validate(c);},"unsafe_path");
  await reject("wrong evidence role",async()=>{const c=clone(base);c.files.find(f=>f.path===review).role="source";await validate(c);},"evidence_role");
  await reject("historical status without evidence",async()=>{const c=clone(base);c.records[0].lean.evidence=[];await validate(c);},"type");
  await reject("wrong toolchain bytes despite matching file digest",async()=>{const m=mutatedFile("tangent-limit/lean-toolchain","leanprover/lean4:v4.25.0\n");await validate(m.catalog,m.files);},"toolchain_drift");
  await reject("wrong mathlib revision",async()=>{const c=clone(base);c.project.mathlib_revision="0".repeat(40);await validate(c);},"mathlib_drift");
  await reject("ambiguous Lake lockfile duplicate key",async()=>{
    const p="tangent-limit/lake-manifest.json";let t=core.decodeUTF8(bytes.get(p));const rev=base.project.mathlib_revision;
    t=t.replace('"rev": "'+rev+'"','"rev":"'+rev+'","rev":"'+rev+'"');const m=mutatedFile(p,t);await validate(m.catalog,m.files);
  },"lockfile_parse");
  await reject("spoofed mathlib origin",async()=>{
    const p="tangent-limit/lake-manifest.json";const t=core.decodeUTF8(bytes.get(p)).replace("https://github.com/leanprover-community/mathlib4.git","https://example.com/fake.git");const m=mutatedFile(p,t);await validate(m.catalog,m.files);
  },"mathlib_drift");
  await reject("project branch label changed",async()=>{const c=clone(base);c.project.branch="main";await accepted(c);});
  await reject("project revision changed",async()=>{const c=clone(base);c.project.revision="0".repeat(40);await accepted(c);});
  await pass("deterministic byte bundle and complete round trip",async()=>{
    const a=await bundle.makeBundle(base,reader(bytes),hash),b=await bundle.makeBundle(clone(base),reader(bytes),hash);
    assert(a===b,"bundle nondeterminism");const restored=await bundle.readBundle(strict.parseStrict(a),hash);
    assert(strict.canonicalJSON(restored.catalog)===strict.canonicalJSON(base),"catalog changed");
    for(const [p,data] of bytes)assert(hash(restored.files.get(p))===hash(data),"bytes changed: "+p);
  });
  await reject("bundle missing file",async()=>{const b=clone(corpus);b.files.pop();await bundle.readBundle(b,hash);});
  await reject("bundle extra file",async()=>{const b=clone(corpus);b.files.push({path:"extra.txt",sha256:hash(utf8("x")),hex:"78"});await bundle.readBundle(b,hash);});
  await reject("bundle duplicate file",async()=>{const b=clone(corpus);b.files.push(clone(b.files[0]));await bundle.readBundle(b,hash);});
  await reject("bundle byte tamper",async()=>{const b=clone(corpus);b.files[0].hex="00"+b.files[0].hex.slice(2);await bundle.readBundle(b,hash);});
  await reject("bundle hex encoding invalid",async()=>{const b=clone(corpus);b.files[0].hex="zz";await bundle.readBundle(b,hash);});
  for(const [name,text] of [
    ["duplicate key",'{"x":1,"x":2}'],["escaped duplicate key",'{"x":1,"\\u0078":2}'],
    ["prototype key",'{"__proto__":1}'],["constructor key",'{"constructor":1}'],
    ["unpaired surrogate",'"\\ud800"'],["trailing content",'{} true'],["trailing comma",'[1,]'],
    ["leading zero",'01'],["nonfinite number",'1e400'],["nesting limit","[".repeat(66)+"0"+"]".repeat(66)]
  ]) await reject("strict JSON "+name,()=>strict.parseStrict(text));
  await pass("valid UTF8 and JSON Unicode",()=>{const s="π ℝ 🚀";assert(core.decodeUTF8(utf8(s))===s,"Unicode round trip");strict.parseStrict('"\\ud83d\\ude80"');});
  await reject("invalid UTF8 source bytes",async()=>{
    const c=clone(base),f=new Map(bytes),p=c.records[0].statement.source_path,invalid=Uint8Array.from([0xc0,0xaf]);
    f.set(p,invalid);c.files.find(x=>x.path===p).sha256=hash(invalid);await validate(c,f);
  },"invalid_utf8");
  await pass("reported finite computation remains separate from proof",async()=>{
    const c=clone(base),f=new Map(bytes),statement="theorem square_identity (n : Nat) : n * n = n * n";
    const source=utf8(statement+" := rfl\n"),observations=[0,1,2,3,4].map(n=>({n,square:n*n}));
    assert(observations.every(x=>x.square>=0),"experiment unexpectedly false");
    const evidence=utf8(strict.canonicalJSON({executor:"hosted_V8",domain:"n = 0,1,2,3,4",observations}));
    f.set("fixtures/Finite.lean",source);f.set("fixtures/squares.json",evidence);
    c.files.push({path:"fixtures/Finite.lean",sha256:hash(source),role:"source"},{path:"fixtures/squares.json",sha256:hash(evidence),role:"experiment"});
    c.records.push({id:"Fixture.square_identity",kind:"theorem",name:"Fixture.square_identity",
      statement:{text:statement,source_path:"fixtures/Finite.lean",source_excerpt:statement,sha256:hash(utf8(statement))},
      assumptions:[],dependencies:[],sources:[{url:"https://example.com/fixture",revision:c.project.revision,locator:"Fixture.square_identity"}],
      review:{status:"not_reviewed",evidence:[]},experiments:[{claim:"All five reported squares are nonnegative.",scope:"n = 0,1,2,3,4",evidence:["fixtures/squares.json"]}],
      lean:{status:"not_run",evidence:[],reason:"Lean fixture source is data; it has not been compiled."}});
    const r=await validate(c,f);assert(r.summary.counts.experimentReports===1&&r.summary.counts.leanPasses===0,"experiment became proof");
  });
  return {schema:"math-companion-tests/v1",execution:runtime,checks,
    passed:checks.length,failed:0,nodeExecution:"not_performed",filesystemTests:"not_performed",
    leanFixtureExecution:"not_performed",osProcessInterruptionTests:"not_performed",independentKernelReplay:"not_performed"};
}
module.exports = {runTests};
