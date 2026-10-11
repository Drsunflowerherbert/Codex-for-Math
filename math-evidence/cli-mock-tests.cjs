"use strict";
// These are contract tests with an injected in-memory filesystem, not Node filesystem tests.
async function runCLIMockTests(cliSource, modules, corpusText, catalogText, sourceFiles, hash, runtime = 'unspecified_JavaScript_with_mock_adapters') {
  const checks = [], reads = [], writes = [];
  const map = new Map(sourceFiles.map(([p,b])=>["/mem/"+p,Uint8Array.from(b)]));
  map.set("/catalog.json",modules.core.encodeUTF8(catalogText));
  map.set("/bundle.json",modules.core.encodeUTF8(corpusText));
  const symlinks = new Set();
  const existsDir = p => p==="/mem" || [...map.keys()].some(k=>k.startsWith(p+"/"));
  const identities=new Map();let nextInode=1;
  const stat = p => {if(!identities.has(p))identities.set(p,nextInode++);return {isFile:()=>map.has(p),isDirectory:()=>existsDir(p),isSymbolicLink:()=>symlinks.has(p),size:map.get(p)?.length||0,dev:1,ino:identities.get(p),mtimeMs:0,ctimeMs:0};};
  const fs = {
    realpath:async p=>{if (!map.has(p)&&!existsDir(p)) throw new Error("ENOENT");return p;},
    stat:async p=>stat(p),
    lstat:async p=>{if(!map.has(p)&&!existsDir(p))throw new Error("ENOENT");return stat(p);},
    open:async (p,flags)=>{
      reads.push({path:p,flags});if(!map.has(p))throw new Error("ENOENT");
      return {stat:async()=>stat(p),readFile:async()=>Uint8Array.from(map.get(p)),read:async(buffer,offset,length,position)=>{const data=map.get(p),bytesRead=Math.min(length,Math.max(0,data.length-position));buffer.set(data.subarray(position,position+bytesRead),offset);return {bytesRead,buffer};},close:async()=>{}};
    },
    writeFile:async (p,text,options)=>{
      if(options.flag!=="wx")throw new Error("test expected exclusive output creation");
      if(map.has(p))throw new Error("EEXIST");
      map.set(p,modules.core.encodeUTF8(text));writes.push(p);
    }
  };
  const path = {
    sep:"/",
    join:(...parts)=>parts.join("/").replace(/\/+/g,"/"),
    isAbsolute:p=>p.startsWith("/"),
    relative:(root,target)=>{
      const a=root.split("/"),b=target.split("/");while(a.length&&b.length&&a[0]===b[0]){a.shift();b.shift();}
      return [...a.map(()=>".."),...b].join("/");
    }
  };
  const crypto = {createHash:()=>{let bytes;return {update:b=>{bytes=b;return {digest:()=>hash(bytes)};}};}};
  const req=name=>({
    "node:fs/promises":fs,"node:fs":{constants:{O_RDONLY:0,O_NOFOLLOW:131072,O_NONBLOCK:2048}},
    "node:path":path,"node:crypto":crypto,
    "./core.cjs":modules.core,"./strict-json.cjs":modules.strict,"./bundle.cjs":modules.bundle,"./tangent-pins.cjs":modules.pins,"./bounded-io.cjs":require("./bounded-io.cjs")
  }[name]);
  const module = {exports:{}};
  new Function("module","require","Buffer",cliSource)(module,req,{from:s=>modules.core.encodeUTF8(s)});
  const cli=module.exports;
  const assert=(x,message)=>{if(!x)throw new Error(message);};
  async function pass(name,fn){await fn();checks.push({name,result:"passed"});}
  async function reject(name,fn){let rejected=false;try{await fn();}catch{rejected=true;}assert(rejected,name+" unexpectedly accepted");checks.push({name,result:"passed"});}
  await pass("validate command dispatch",async()=>{const r=await cli.main(["validate","/catalog.json","/mem"]);assert(r.ok&&r.summary.records===37,"wrong summary");});
  await pass("inventory command validates and reports historical statuses",async()=>{const r=await cli.main(["inventory","/catalog.json","/mem"]);assert(r.includes("Lean passes: 0")&&r.includes("lean=historical_report"),"wrong inventory");});
  await pass("inspect bundle dispatch",async()=>{const r=await cli.main(["inspect-bundle","/bundle.json"]);assert(r.ok&&r.summary.counts.leanPasses===0,"wrong bundle summary");});
  await pass("tangent acceptance dispatch",async()=>{const r=await cli.main(["accept-tangent","/bundle.json"]);assert(r.acceptance.records===37&&!r.acceptance.leanPass,"false pass");});
  await pass("bundle writes only explicit new output",async()=>{const r=await cli.main(["bundle","/catalog.json","/mem","/new-bundle.json"]);assert(r.ok&&writes.length===1&&writes[0]==="/new-bundle.json","wrong output");});
  await reject("bundle cannot overwrite",()=>cli.main(["bundle","/catalog.json","/mem","/new-bundle.json"]));
  await reject("unknown command rejected",()=>cli.main(["exec","echo","never-run"]));
  await reject("wrong argument count rejected",()=>cli.main(["validate","/catalog.json"]));
  await pass("containment uses path components",()=>{assert(cli.contained("/mem","/mem/ok")&&!cli.contained("/mem","/memory/escape"),"prefix containment flaw");});
  const file=sourceFiles[0][0];symlinks.add("/mem/"+file);
  await reject("source symlink contract rejects",()=>cli.main(["validate","/catalog.json","/mem"]));
  symlinks.clear();
  const malformed=JSON.parse(catalogText);malformed.records[0].command="echo never-run";
  map.set("/malformed.json",modules.core.encodeUTF8(JSON.stringify(malformed)));
  const before=reads.length;
  await reject("imported command fails before source reads",()=>cli.main(["validate","/malformed.json","/mem"]));
  assert(reads.length===before+1,"invalid command caused source reads"); // Only the explicit catalog was read.
  return {schema:"math-cli-mock-tests/v1",execution:runtime,
    passed:checks.length,failed:0,checks,nodeExecution:"not_performed",realFilesystemTests:"not_performed"};
}
module.exports = {runCLIMockTests};
