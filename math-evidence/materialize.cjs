"use strict";
// Materializes exact trusted distribution bytes. It does not execute imported file contents.
const fs = require("node:fs/promises");
const path = require("node:path");
const crypto = require("node:crypto");
const constants = require("node:fs").constants;
const {parseStrict} = require("./strict-json.cjs");
const {decodeUTF8,encodeUTF8} = require("./core.cjs");
const {readBounded} = require("./bounded-io.cjs");
const hash = b=>crypto.createHash("sha256").update(b).digest("hex");
const portable = s=>typeof s==="string"&&s.length>0&&s.length<=240&&
  /^[A-Za-z0-9_.-]+(?:\/[A-Za-z0-9_.-]+)*$/.test(s)&&
  s.split("/").every(p=>p!=="."&&p!==".."&&!p.endsWith(".")&&!/^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)/i.test(p));
async function writeNewTree(root,staged) {
  // Node has no openat API. Linux descriptor paths anchor every child operation
  // to an opened directory; other hosts fail closed instead of following races.
  if(process.platform!=="linux"||!constants.O_DIRECTORY||!constants.O_NOFOLLOW)
    throw new Error("secure extraction requires tested Linux directory descriptor paths");
  if(!path.isAbsolute(root)||root!==path.resolve(root)||root===path.parse(root).root)throw new Error("canonical absolute new extraction directory required");
  const parent=path.dirname(root), basename=path.basename(root), handles=[], dirs=new Map(), ancestors=[];
  const flags=constants.O_RDONLY|constants.O_DIRECTORY|constants.O_NOFOLLOW|constants.O_NONBLOCK;
  const anchored=(h,name)=>"/proc/self/fd/"+h.fd+"/"+name;
  const openDirectory=async name=>{
    const before=await fs.lstat(name);
    if(!before.isDirectory()||before.isSymbolicLink())throw new Error("extraction directory is not regular");
    const h=await fs.open(name,flags);handles.push(h);
    const stat=await h.stat();
    if(!stat.isDirectory()||stat.dev!==before.dev||stat.ino!==before.ino)throw new Error("extraction directory changed");
    return {h,stat};
  };
  const stableParents=async()=>{
    for(const item of ancestors){const now=await fs.lstat(item.path);
      if(now.isSymbolicLink()||!now.isDirectory()||now.dev!==item.stat.dev||now.ino!==item.stat.ino)throw new Error("extraction parent ancestry changed");}
  };
  try {
    if(await fs.realpath(parent)!==parent)throw new Error("extraction parent symlinks are rejected");
    let p=await openDirectory(path.parse(parent).root), lexical=path.parse(parent).root;
    ancestors.push({path:lexical,stat:p.stat});
    for(const component of parent.slice(lexical.length).split(path.sep).filter(Boolean)){
      p=await openDirectory(anchored(p.h,component));lexical=path.join(lexical,component);
      ancestors.push({path:lexical,stat:p.stat});
    }
    await stableParents();
    // Verify descriptor aliases are available before creating the output tree.
    const alias=await fs.stat("/proc/self/fd/"+p.h.fd);
    if(alias.dev!==p.stat.dev||alias.ino!==p.stat.ino||!alias.isDirectory())throw new Error("directory descriptor path unavailable");
    await fs.mkdir(anchored(p.h,basename)); // Exclusive new root; no overwrite.
    const base=await openDirectory(anchored(p.h,basename));dirs.set("",base);
    for(const f of staged) {
      const parts=f.path.split("/"),leaf=parts.pop();let key="",dir=base;
      for(const component of parts) {
        key=key?key+"/"+component:component;
        if(!dirs.has(key)) {
          const target=anchored(dir.h,component);
          await fs.mkdir(target);
          dirs.set(key,await openDirectory(target));
        }
        dir=dirs.get(key);
      }
      await fs.writeFile(anchored(dir.h,leaf),f.bytes,{flag:"wx"});
    }
    for(const [key,dir] of dirs) {
      const name=key?path.join(root,...key.split("/")):root;
      const now=await fs.lstat(name);
      if(now.isSymbolicLink()||!now.isDirectory()||now.dev!==dir.stat.dev||now.ino!==dir.stat.ino)
        throw new Error("extraction directory moved or changed; no completed extraction");
    }
    await stableParents();
  } finally {for(const h of handles.reverse())await h.close();}
}
async function materialize(input, expectedSHA256, output) {
  if(!/^[0-9a-f]{64}$/.test(expectedSHA256))throw new Error("explicit expected distribution SHA256 required");
  const stat=await fs.lstat(input);if(!stat.isFile()||stat.isSymbolicLink()||stat.size>32*1024*1024)throw new Error("distribution file size/type limit");
  const handle=await fs.open(input,constants.O_RDONLY|(constants.O_NOFOLLOW||0)|(constants.O_NONBLOCK||0));
  let raw;
  try {
    const opened=await handle.stat();
    if(!opened.isFile()||opened.dev!==stat.dev||opened.ino!==stat.ino||opened.size>32*1024*1024)throw new Error("distribution changed before read");
    raw=await readBounded(handle,Math.min(opened.size,32*1024*1024));
    const after=await handle.stat(),linked=await fs.lstat(input);
    if(linked.isSymbolicLink()||linked.dev!==opened.dev||linked.ino!==opened.ino||after.size!==opened.size||after.mtimeMs!==opened.mtimeMs||after.ctimeMs!==opened.ctimeMs)throw new Error("distribution changed during read");
  } finally {await handle.close();}
  if(raw.length>32*1024*1024||hash(raw)!==expectedSHA256)throw new Error("distribution bytes do not match independent expected SHA256");
  // Parsing follows exact whole-file hash matching. Only the packaged distribution is accepted.
  const data=parseStrict(decodeUTF8(raw));
  if(!data||data.schema!=="math-companion-distribution/v1"||Object.keys(data).sort().join("|")!=="files|schema"||
    !Array.isArray(data.files)||data.files.length>1000)throw new Error("unsupported distribution");
  const names=new Set(),staged=[];let total=0;
  for(const f of data.files) {
    if(!f||Object.keys(f).sort().join("|")!=="path|sha256|text"||!portable(f.path)||typeof f.text!=="string"||!/^[0-9a-f]{64}$/.test(f.sha256))throw new Error("invalid distribution entry");
    const folded=f.path.toLowerCase();
    if(names.has(folded))throw new Error("case-colliding distribution path");names.add(folded);
    const bytes=encodeUTF8(f.text);total+=bytes.length;
    if(total>16*1024*1024||hash(bytes)!==f.sha256)throw new Error("entry byte hash/size mismatch: "+f.path);
    staged.push({path:f.path,bytes});
  }
  for(const name of names){const parts=name.split("/");for(let i=1;i<parts.length;i++)if(names.has(parts.slice(0,i).join("/")))throw new Error("file/directory collision");}
  const root=path.resolve(output);
  await writeNewTree(root,staged);
  return {materialized:staged.length,root,sha256:expectedSHA256,executedImportedContents:false};
}
if(require.main===module) {
  if(process.argv.length!==5){console.error("Usage: node materialize.cjs DISTRIBUTION.json EXPECTED_SHA256 NEW_DIRECTORY");process.exitCode=2;}
  else materialize(...process.argv.slice(2)).then(x=>console.log(JSON.stringify(x,null,2))).catch(e=>{console.error(e.message);process.exitCode=2;});
}
module.exports={materialize,writeNewTree};
