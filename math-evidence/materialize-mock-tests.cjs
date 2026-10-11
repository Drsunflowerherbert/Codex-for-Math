"use strict";
async function runMaterializeMockTests(source,core,strict,hash,runtime="unspecified_JavaScript_with_mock_adapters") {
  const checks=[],paths=new Set(["/"]),writes=new Map(),inodes=new Map([["/",2]]),descriptors=new Map();let mkdirCalls=0,raw,nextFD=17,nextInode=3;
  function bytes(text){const b=core.encodeUTF8(text);b.toString=()=>core.decodeUTF8(b);return b;}
  const fakeStat=(p="input")=>({isFile:()=>p==="input",isDirectory:()=>paths.has(p),isSymbolicLink:()=>false,size:p==="input"?raw.length:0,dev:1,ino:p==="input"?1:inodes.get(p),mtimeMs:0,ctimeMs:0});
  function resolveAlias(p){const m=/^\/proc\/self\/fd\/(\d+)(?:\/(.*))?$/.exec(p);if(!m)return p;if(!descriptors.has(Number(m[1])))throw new Error("EBADF");return (descriptors.get(Number(m[1]))+"/"+(m[2]||"")).replace(/\/+/g,"/").replace(/\/$/,"")||"/";}
  const fs={stat:async p=>fakeStat(resolveAlias(p)),lstat:async p=>fakeStat(resolveAlias(p)),readFile:async()=>raw,realpath:async p=>resolveAlias(p),
    open:async p=>{p=resolveAlias(p);if(p!=="input"&&!paths.has(p))throw new Error("ENOENT");const fd=nextFD++;descriptors.set(fd,p);return {fd,stat:async()=>fakeStat(p),readFile:async()=>raw,read:async(buffer,offset,length,position)=>{if(p!=="input")throw new Error("cannot read directory");const bytesRead=Math.min(length,Math.max(0,raw.length-position));buffer.set(raw.subarray(position,position+bytesRead),offset);return {bytesRead,buffer};},close:async()=>{descriptors.delete(fd);}};},
    mkdir:async(p,options)=>{p=resolveAlias(p);mkdirCalls++;if(paths.has(p)&&!options?.recursive)throw new Error("EEXIST");paths.add(p);inodes.set(p,nextInode++);},
    writeFile:async(p,data,options)=>{p=resolveAlias(p);if(options.flag!=="wx"||writes.has(p))throw new Error("overwrite");writes.set(p,Uint8Array.from(data));}};
  const path={sep:"/",isAbsolute:p=>p.startsWith("/"),parse:p=>({root:p.startsWith("/")?"/":""}),resolve:p=>"/"+p.replace(/^\/+/,""),join:(...p)=>p.join("/").replace(/\/+/g,"/"),
    dirname:p=>p.slice(0,p.lastIndexOf("/"))||"/",basename:p=>p.slice(p.lastIndexOf("/")+1)};
  const crypto={createHash:()=>({update:b=>({digest:()=>hash(b)})})};
  const req=name=>({"node:fs/promises":fs,"node:fs":{constants:{O_RDONLY:0,O_DIRECTORY:65536,O_NOFOLLOW:131072,O_NONBLOCK:2048}},"node:path":path,"node:crypto":crypto,"./strict-json.cjs":strict,"./core.cjs":core,"./bounded-io.cjs":require("./bounded-io.cjs")}[name]);
  const m={exports:{}};new Function("module","require","Buffer","process",source)(m,req,{from:bytes},{platform:"linux"});
  const create=(files=[{path:"README.md",sha256:hash(core.encodeUTF8("text\n")),text:"text\n"}])=>{
    raw=bytes(strict.canonicalJSON({schema:"math-companion-distribution/v1",files})+"\n");return hash(raw);
  };
  async function pass(name,fn){await fn();checks.push({name,result:"passed"});}
  async function reject(name,fn,noWrites=true){const prior=mkdirCalls;let caught=false;try{await fn();}catch{caught=true;}if(!caught)throw new Error("unexpected acceptance "+name);if(noWrites&&mkdirCalls!==prior)throw new Error("invalid distribution started creating directories");checks.push({name,result:"passed"});}
  await pass("exact trusted bytes materialize without executing contents",async()=>{const d=create();const r=await m.exports.materialize("input",d,"new");if(r.materialized!==1||r.executedImportedContents||hash(writes.get("/new/README.md"))!==hash(core.encodeUTF8("text\n")))throw new Error("wrong materialization");});
  await reject("existing root rejected",async()=>{const d=create();await m.exports.materialize("input",d,"new");},false);
  await reject("wrong whole-file digest rejected before writes",async()=>{create();await m.exports.materialize("input","0".repeat(64),"digest");});
  await reject("traversal path rejected despite matching whole-file digest",async()=>{const d=create([{path:"../escape",sha256:hash(core.encodeUTF8("x")),text:"x"}]);await m.exports.materialize("input",d,"traversal");});
  await reject("entry digest drift rejected",async()=>{const d=create([{path:"x.txt",sha256:"0".repeat(64),text:"x"}]);await m.exports.materialize("input",d,"entry");});
  await reject("case-colliding output rejected",async()=>{const f={path:"X.txt",sha256:hash(core.encodeUTF8("x")),text:"x"},d=create([f,{...f,path:"x.txt"}]);await m.exports.materialize("input",d,"case");});
  await reject("parent-file conflict rejected",async()=>{const f={path:"x",sha256:hash(core.encodeUTF8("x")),text:"x"},d=create([f,{...f,path:"x/child"}]);await m.exports.materialize("input",d,"prefix");});
  await reject("unknown distribution fields rejected",async()=>{raw=bytes('{"schema":"math-companion-distribution/v1","files":[],"command":"never-run"}');await m.exports.materialize("input",hash(raw),"unknown");});
  return {schema:"math-materializer-mock-tests/v1",execution:runtime,passed:checks.length,failed:0,checks,realFilesystemTests:"not_performed"};
}
module.exports={runMaterializeMockTests};
