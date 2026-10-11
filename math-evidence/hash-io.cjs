"use strict";
const fs=require("node:fs/promises");
const constants=require("node:fs").constants;
const crypto=require("node:crypto");
async function hashRegular(filename,maxBytes=1073741824) {
  const before=await fs.lstat(filename);
  if(!before.isFile()||before.isSymbolicLink()||before.size>maxBytes)throw new Error("not a bounded regular hash source");
  const h=await fs.open(filename,constants.O_RDONLY|constants.O_NOFOLLOW|constants.O_NONBLOCK);
  try {
    const opened=await h.stat();
    if(!opened.isFile()||opened.dev!==before.dev||opened.ino!==before.ino||opened.size!==before.size)throw new Error("hash source identity changed");
    const buffer=new Uint8Array(65536),sha=crypto.createHash("sha256");let total=0;
    while(total<=opened.size) {
      const length=Math.min(buffer.length,opened.size+1-total);
      const {bytesRead}=await h.read(buffer,0,length,total);
      if(!bytesRead)break;total+=bytesRead;
      if(total>opened.size)throw new Error("hash source grew during bounded read");
      sha.update(buffer.subarray(0,bytesRead));
    }
    const after=await h.stat(),linked=await fs.lstat(filename);
    if(total!==opened.size||linked.isSymbolicLink()||linked.dev!==opened.dev||linked.ino!==opened.ino||
      after.size!==opened.size||after.mtimeMs!==opened.mtimeMs||after.ctimeMs!==opened.ctimeMs)throw new Error("hash source changed during read");
    return {path:filename,bytes:total,sha256:sha.digest("hex")};
  } finally {await h.close();}
}
module.exports={hashRegular};
