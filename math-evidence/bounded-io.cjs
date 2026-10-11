"use strict";
// An allocation/read bound, including when a regular file grows concurrently.
async function readBounded(handle,maxBytes) {
  if(!Number.isSafeInteger(maxBytes)||maxBytes<0)throw new Error("invalid byte bound");
  const parts=[];let total=0;
  while(total<=maxBytes) {
    const buffer=new Uint8Array(Math.min(65536,maxBytes+1-total));
    const {bytesRead}=await handle.read(buffer,0,buffer.length,total);
    if(!Number.isInteger(bytesRead)||bytesRead<0||bytesRead>buffer.length)throw new Error("invalid filesystem read result");
    if(!bytesRead)break;
    total+=bytesRead;
    if(total>maxBytes)throw new Error("file exceeds bounded read size");
    parts.push(buffer.slice(0,bytesRead));
  }
  const result=new Uint8Array(total);let position=0;
  for(const part of parts){result.set(part,position);position+=part.length;}
  return result;
}
module.exports={readBounded};
