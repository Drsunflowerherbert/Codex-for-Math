"use strict";
const fs=require('node:fs/promises'),path=require('node:path'),crypto=require('node:crypto');
const {parseStrict,canonicalJSON}=require('./vendor/strict-json.cjs');
function need(v,m){if(!v)throw new Error(m);}
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function keys(o,ks,where){need(o&&Object.getPrototypeOf(o)===Object.prototype&&canonicalJSON(Object.keys(o).sort())===canonicalJSON(ks.slice().sort()),'invalid fields: '+where);}
function portable(p){return typeof p==='string'&&p.length<=512&&p.split('/').every(s=>/^[A-Za-z0-9_.'-]+$/.test(s)&&s!=='.'&&s!=='..'&&!s.endsWith('.')&&!/^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)/i.test(s));}
function absolute(p){return typeof p==='string'&&path.isAbsolute(p)&&path.normalize(p)===p&&!p.includes('\0');}
function utf8(b){return new TextDecoder('utf-8',{fatal:true}).decode(b);}
function timestamp(s){need(typeof s==='string'&&/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d{3}Z$/.test(s)&&Number.isFinite(Date.parse(s))&&new Date(s).toISOString()===s,'invalid canonical timestamp');return Date.parse(s);}
function descriptor(d){keys(d,['path','bytes','sha256'],'artifact');need(portable(d.path)&&Number.isSafeInteger(d.bytes)&&d.bytes>=0&&d.bytes<=33554432&&typeof d.sha256==='string'&&/^[a-f0-9]{64}$/.test(d.sha256),'invalid artifact descriptor');}
async function reader(root){
  root=path.resolve(root);need(await fs.realpath(root)===root,'root symlink/alias rejected');
  need((await fs.lstat(root)).isDirectory(),'root must be a directory');
  return async(p,limit=33554432)=>{
    need(portable(p),'unsafe relative path');let at=root;
    const parts=p.split('/');
    for(const [i,part] of parts.entries()){at=path.join(at,part);const st=await fs.lstat(at);need(!st.isSymbolicLink(),'symlink rejected: '+p);need(i===parts.length-1?st.isFile()&&st.nlink===1&&st.size<=limit:st.isDirectory(),'nonregular or oversized path: '+p);}
    const h=await fs.open(at,require('node:fs').constants.O_RDONLY|require('node:fs').constants.O_NOFOLLOW|require('node:fs').constants.O_NONBLOCK);
    try {const s=await h.stat();need(s.isFile()&&s.nlink===1&&s.size<=limit,'nonregular, shared, or oversized artifact: '+p);const b=await h.readFile();const after=await h.stat();need(b.length===s.size&&after.size===s.size&&after.mtimeMs===s.mtimeMs&&after.ctimeMs===s.ctimeMs,'file changed during read');return b;}finally{await h.close();}
  };
}
async function json(read,p){return parseStrict(utf8(await read(p)));}
async function artifact(read,d){descriptor(d);const b=await read(d.path);need(b.length===d.bytes&&sha(b)===d.sha256,'artifact changed: '+d.path);return b;}
module.exports={need,sha,keys,portable,absolute,utf8,timestamp,descriptor,reader,json,artifact,parseStrict,canonicalJSON};
