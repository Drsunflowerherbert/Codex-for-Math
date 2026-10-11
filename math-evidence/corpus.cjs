"use strict";
// Lossless, data-only intake for the inspected supplement. This is not MRS or
// math-exchange/v1 conversion, and no reported native status grants a proof pass.
const fs=require("node:fs/promises"),path=require("node:path"),crypto=require("node:crypto");
const {sourceReader}=require("./cli.cjs"),{parseStrict,canonicalJSON}=require("./strict-json.cjs"),core=require("./core.cjs");
const digest=b=>crypto.createHash("sha256").update(b).digest("hex");
const REVISION="fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb";
const MANIFEST_SHA="cfd20fd78b1000e6fa00aa5ad867377ff78d4427e8d97da525af55419fdd3678";
const PROFILES=Object.freeze({
  "affine-avoidance":{file:"reviews/affine/mrs-provisional-records.reviewed.json",array:"records",id:"record_id",count:5,pattern:/^family084\.affine_avoidance\.[A-Za-z0-9_.-]+\.v2$/},
  "egyptian-fractions":{file:"reviews/egyptian/corrected/theorem-records.json",array:null,id:"id",count:6,pattern:/^EGY-00[1-6]$/},
  "transport-stability":{file:"transport-stability/theorems.json",array:"theorems",id:"id",count:10,pattern:/^374\.[A-Za-z0-9_]+$/,
    external:["Cauchy-Schwarz inequality","Euclidean distance dominates each coordinate difference","Fubini-Tonelli theorem","Fubini-Tonelli theorem for product probability","Tonelli theorem","finite affine hyperplanes are Lebesgue-null","nonnegative integrable function with zero integral vanishes almost everywhere","orthogonality of coordinate axes","quadratic norm expansion"],
    aliases:{"374.exact_map_L2 cell masses":"374.exact_map_L2"}},
  "positive-blocks":{file:"positive-blocks/theorem-records.json",array:"theorems",id:"id",count:10,pattern:/^PB[A-Z0-9_]+$/},
  "mixed-moments":{file:"mixed-moments/theorems.json",array:"theorems",id:"id",count:21,pattern:/^MM0[0-9]{2}$/},
  "convex-approximation":{file:"convex-approximation/theorem-records.json",array:null,id:"id",count:19,pattern:/^ACOA-0[0-9]{2}$/,
    standard:["STD-ANALYTIC-IFT","STD-CHOICE","STD-COMPACT-SEPARATION","STD-COMPACTNESS","STD-CONTINUITY","STD-CONVEXITY","STD-COSH","STD-DIFFERENTIATION","STD-DISTANCE","STD-EXP","STD-EXTREMA","STD-GRADIENT-SUPPORT","STD-INNER-PRODUCT","STD-IVT","STD-JENSEN","STD-PROJECTION-NORMAL","STD-SPHERE-MANIFOLD","STD-STRICT-CONVEXITY","STD-TRIGONOMETRY","STD-UNIFORM-CONTINUITY","STD-VOLUME-PACKING"]},
  "finite-field-mixing":{file:"finite-field-mixing/theorems.json",array:"theorems",id:"id",count:10,pattern:/^FF0[0-9]{2}$/}
});
const fail=(condition,message)=>{if(!condition)throw new Error(message);};
function relativeReference(base,reference){
  fail(typeof reference==="string"&&reference.length>0&&!reference.includes("\\")&&!reference.includes("\0")&&!path.posix.isAbsolute(reference),"unsafe relative attachment reference");
  const result=path.posix.normalize(path.posix.join(path.posix.dirname(base),reference.split("#")[0]));
  fail(core.isPortablePath(result),"attachment reference escapes the corpus or is not portable");return result;
}
function graph(document,profile,extraBackground=[]){
  const records=profile.array?document?.[profile.array]:document;
  fail(Array.isArray(records)&&records.length===profile.count,"record count/shape mismatch");
  const background=profile.array&&document.background!==undefined?document.background:[];
  fail(Array.isArray(background),"background nodes must be an array");
  const nodes=new Map(), edges=[];
  for(const [kind,rs] of [["record",records],["background",background],["external_record",extraBackground]])for(const record of rs){
    const id=kind==="record"?record?.[profile.id]:record?.id;
    fail(typeof id==="string"&&/^[A-Za-z0-9][A-Za-z0-9_.-]{0,199}$/.test(id)&&!nodes.has(id),"invalid/duplicate native identifier");
    if(kind==="record"){
      fail(profile.pattern.test(id),"unexpected profile identifier");
      const assumptions=record.hypotheses??record.assumptions,statement=record.statement??record.conclusion;
      fail(typeof record.title==="string"&&record.title.length>0&&Array.isArray(assumptions)&&assumptions.every(a=>typeof a==="string"&&a.length>0),"missing explicit native statement assumptions/title");
      fail(typeof statement==="string"?statement.length>0:statement&&typeof statement==="object"&&Object.keys(statement).length>0,"missing native statement/conclusion");
    }
    nodes.set(id,{record,kind});
  }
  for(const [id,{record,kind}] of nodes){
    const deps=record.dependencies??[];
    fail(Array.isArray(deps)&&deps.every(x=>typeof x==="string")&&new Set(deps).size===deps.length,"invalid/duplicate native dependencies");
    for(const raw of deps){
      const target=profile.aliases?.[raw]??raw;
      if(nodes.has(target))edges.push({from:id,raw,target,kind:kind==="external_record"?"preserved_external_record_dependency":"native_record_reference",interpretation:target===raw?"literal_identifier":"explicit_profile_alias_with_qualifier_preserved"});
      else {fail((profile.external??[]).includes(raw),"unresolved native dependency: "+raw);edges.push({from:id,raw,target:null,kind:"reported_standard_mathematics",interpretation:"unverified_external_premise"});}
    }
    if(record.standard_dependencies!==undefined){fail(Array.isArray(record.standard_dependencies)&&new Set(record.standard_dependencies).size===record.standard_dependencies.length,"invalid standard dependency list");for(const raw of record.standard_dependencies){fail((profile.standard??[]).includes(raw),"unknown standard dependency");edges.push({from:id,raw,target:null,kind:"reported_standard_mathematics",interpretation:"unverified_external_premise"});}}
  }
  const visited=new Set(),active=new Set(),order=[];
  function visit(id){fail(!active.has(id),"native dependency cycle");if(visited.has(id))return;active.add(id);for(const e of edges)if(e.from===id&&e.target)visit(e.target);active.delete(id);visited.add(id);order.push(id);}
  for(const id of nodes.keys())visit(id);
  return {records,background,edges,topologicalOrder:order};
}
function reportedFields(document,records){
  const results=[];
  function scan(value,pointer){
    if(!value||typeof value!=="object")return;
    for(const [k,v] of Object.entries(value)){
      const p=pointer+"/"+k.replaceAll("~","~0").replaceAll("/","~1");
      if(/verification|review|status|lean|kernel|formal|experiment|computation|native_mrs/i.test(k))results.push({pointer:p,value:v,authority:"preserved_report_only"});
      if(v&&typeof v==="object")scan(v,p);
    }
  }
  scan(document,"");return results;
}
function validateRevision(document,records){
  const revisions=[document?.source_revision,document?.source?.revision,document?.provenance?.revision,document?.source_metadata?.commit,...records.flatMap(r=>[r.source_revision,r.source_pin])].filter(v=>v!==undefined);
  fail(revisions.length>0&&revisions.every(v=>v===REVISION),"native source revision mismatch");
}
function attachmentReferences(document,records,profile,index,manifestBytes){
  const refs=[];
  const add=(pointer,raw,kind="contained_attachment",expectedHash=null,rootRelative=false)=>{
    if(raw===undefined)return;
    fail(typeof raw==="string"&&raw.length>0,"invalid native attachment reference");
    if(kind!=="contained_attachment"){
      const matchingSourcePaths=expectedHash?[...manifestBytes].filter(([,b])=>digest(b)===expectedHash).map(([p])=>p).sort():[];
      if(expectedHash)fail(matchingSourcePaths.length>0,"reported source digest absent from manifest closure");
      refs.push({pointer,raw,kind,normalizedPath:null,sha256:expectedHash,matchingSourcePaths,followed:false});return;
    }
    const normalizedPath=rootRelative?raw:relativeReference(profile.file,raw);
    fail(core.isPortablePath(normalizedPath)&&manifestBytes.has(normalizedPath),"missing manifest-backed attachment: "+normalizedPath);
    const b=manifestBytes.get(normalizedPath),sha256=digest(b);
    if(expectedHash)fail(sha256===expectedHash,"native attachment digest differs from preserved file: "+normalizedPath);
    refs.push({pointer,raw,kind,normalizedPath,bytes:b.length,sha256,followed:true});
  };
  add("index/final_notes",index.final_notes,"contained_attachment",null,true);
  index.review_evidence.forEach((r,i)=>add("index/review_evidence/"+i,r,"contained_attachment",null,true));
  records.forEach((r,i)=>{
    const p=(profile.array?"/"+profile.array:"")+"/"+i;
    for(const k of ["proof_file","artifact","proof_location"])add(p+"/"+k,r[k]);
    add(p+"/proof/file",r.proof?.file);
    (r.verification_evidence??[]).forEach((ref,j)=>add(p+"/verification_evidence/"+j,ref));
    add(p+"/verification/independent_review_artifact",r.verification?.independent_review_artifact);
    for(const k of ["file","report","audit_results"])add(p+"/review_evidence/"+k,r.review_evidence?.[k]);
    add(p+"/original_record_provenance/file",r.original_record_provenance?.file,"contained_attachment",r.original_record_provenance?.file_sha256??null);
    (r.source_links??[]).forEach((ref,j)=>add(p+"/source_links/"+j,ref,"reported_remote_reference"));
  });
  for(const k of ["provenance_file","original_artifact","independent_review_artifact"])add("/"+k,document?.[k]);
  (document?.review_log??[]).forEach((r,i)=>add("/review_log/"+i+"/report",r.report));
  add("/source_metadata/local_file",document?.source_metadata?.local_file,"contained_attachment",document?.source_metadata?.sha256??null);
  add("/provenance/source_local_relative",document?.provenance?.source_local_relative,"contained_attachment",document?.provenance?.source_sha256??null);
  for(const [k,v] of Object.entries(document?.artifacts??{}))add("/artifacts/"+k,v,k==="reproduce_fixtures"?"reported_command_never_executed":"contained_attachment");
  add("/source/local_snapshot",document?.source?.local_snapshot,"reported_legacy_absolute_path",document?.source?.sha256??null);
  for(const name of ["source","source_metadata","provenance"]){const s=document?.[name];if(s)for(const k of ["url","source_url","scope_description_url","lean_scope_url"])add("/"+name+"/"+k,s[k],"reported_remote_reference");}
  add("/source/path",document?.source?.path,"reported_repository_source_path");
  return refs;
}
async function importSupplement(root){
  const reader=await sourceReader(root),manifestBytes=await reader("MANIFEST-SHA256.json");
  fail(digest(manifestBytes)===MANIFEST_SHA,"supplement manifest independent pin mismatch");
  const manifest=parseStrict(core.decodeUTF8(manifestBytes));
  fail(manifest.schema==="research-supplement-sha256-manifest-v1"&&manifest.hash_algorithm==="SHA-256"&&manifest.self_excluded===true&&Array.isArray(manifest.files)&&manifest.files.length===106,"supplement manifest shape mismatch");
  const bytes=new Map(),files=[],seen=new Set();
  for(const entry of manifest.files){
    fail(core.isPortablePath(entry.file)&&!seen.has(entry.file.toLowerCase())&&Number.isSafeInteger(entry.bytes)&&entry.bytes>=0&&/^[a-f0-9]{64}$/.test(entry.sha256),"invalid manifest file entry");seen.add(entry.file.toLowerCase());
    const b=await reader(entry.file);fail(b.length===entry.bytes&&digest(b)===entry.sha256,"supplement file integrity mismatch: "+entry.file);bytes.set(entry.file,b);files.push({path:entry.file,bytes:entry.bytes,sha256:entry.sha256});
  }
  files.push({path:"MANIFEST-SHA256.json",bytes:manifestBytes.length,sha256:MANIFEST_SHA});
  const json=f=>{fail(bytes.has(f),"missing manifest-backed JSON");return parseStrict(core.decodeUTF8(bytes.get(f)));};
  const index=json("STUDY-INDEX.json");fail(index.schema==="portable-study-index-v1"&&index.core_record_total===81&&Array.isArray(index.studies)&&index.studies.length===7,"study index mismatch");
  const studies=[],allIds=new Set(),listed=new Set();
  for(const originalIndex of index.studies){
    const profile=PROFILES[originalIndex.id];fail(profile&&!listed.has(originalIndex.id)&&profile.file===originalIndex.portable_records&&profile.count===originalIndex.core_record_count,"unknown/duplicate study profile");listed.add(originalIndex.id);
    const document=json(profile.file),g=graph(document,profile);validateRevision(document,g.records);
    for(const r of g.records){const id=r[profile.id];fail(!allIds.has(id),"duplicate identifier across studies");allIds.add(id);}
    const references=attachmentReferences(document,g.records,profile,originalIndex,bytes),statusFields=reportedFields(document,g.records);
    const statusDiscrepancies=statusFields.filter(f=>f.pointer.endsWith("/independent_review")&&f.value==="pending"&&originalIndex.ordinary_review.includes("completed")).map(f=>({nativePointer:f.pointer,nativeReportedValue:f.value,indexPointer:"/ordinary_review",indexReportedValue:originalIndex.ordinary_review,resolution:"both_reports_preserved_neither_upgraded_or_reassessed"}));
    studies.push({id:originalIndex.id,nativeRecordFile:profile.file,nativeRecordFileSha256:digest(bytes.get(profile.file)),nativeDocument:document,nativeIndexEntry:originalIndex,graph:{edges:g.edges,topologicalOrder:g.topologicalOrder,backgroundNodes:g.background},attachmentPaths:[...new Set(references.filter(r=>r.normalizedPath).map(r=>r.normalizedPath))].sort(),attachmentReferences:references,reportedStatusFields:statusFields,statusDiscrepancies,nativeSchemaTranslation:{attempted:false,allOriginalFieldsPreserved:true,droppedFields:[],statusMapping:"none",nativeMRSMapping:"none"},importedLeanPasses:0,ordinaryReviewConclusion:"not_reassessed_by_import"});
  }
  const optionalFile="reviews/egyptian/corrected/coarse-padding-bound-records.json",optional=json(optionalFile);
  const optionalProfile={array:null,id:"id",count:2,pattern:/^EGY-COR-00[12]$/};
  const eg=studies.find(s=>s.id==="egyptian-fractions").nativeDocument;
  const og=graph(optional,optionalProfile,eg);validateRevision(optional,optional);
  fail(optional.every(r=>r.independent_review_status==="not_separately_reviewed"&&r.lean_status==="not_run"),"optional additions review boundary changed");
  return {schema:"research-collection/v1",kind:"lossless_profiled_data_intake",archiveIdentity:{bytes:523782,sha256:"9e03b1ce33dc5d5fa62ab9478b06998bcb0eb32635fc11bccac065223e892a74"},sourceRevision:REVISION,files:files.sort((a,b)=>a.path.localeCompare(b.path,"en")),coreRecordCount:allIds.size,studies,optionalAdditions:{nativeRecordFile:optionalFile,nativeRecords:optional,graph:{edges:og.edges,topologicalOrder:og.topologicalOrder},count:2,ordinaryReview:"not_separately_reviewed",importedLeanPasses:0},boundaries:{commandsExecuted:false,leanExecuted:false,importedLeanPasses:0,nativeMRSImported:false,nativeMRSIntegration:"unavailable_unvalidated",mathematicalTruth:"not_established_by_schema_graph_or_hash_checks",reportedStatuses:"preserved_verbatim_not_upgraded",legacyAbsolutePaths:"preserved_as_reported_text_never_followed",dependencyCompleteness:"not_established"}};
}
async function main(argv){
  fail(argv.length===3&&argv[0]==="import-supplement","Usage: node corpus.cjs import-supplement EXTRACTED_ROOT NEW_OUTPUT.json");
  const result=await importSupplement(argv[1]),output=canonicalJSON(result)+"\n";
  await fs.writeFile(argv[2],output,{flag:"wx"});
  return {ok:true,kind:result.kind,coreRecords:result.coreRecordCount,studies:result.studies.length,optionalUnreviewedRecords:result.optionalAdditions.count,files:result.files.length,bytes:Buffer.byteLength(output),sha256:digest(Buffer.from(output)),importedLeanPasses:0,nativeMRSImported:false};
}
if(require.main===module)main(process.argv.slice(2)).then(r=>process.stdout.write(JSON.stringify(r,null,2)+"\n")).catch(e=>{process.stderr.write(JSON.stringify({ok:false,message:e.message,importedLeanPasses:0})+"\n");process.exitCode=2;});
module.exports={PROFILES,graph,relativeReference,importSupplement,reportedFields,validateRevision,attachmentReferences};
