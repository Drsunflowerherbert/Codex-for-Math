"use strict";
// Byte integrity of the public source set; this never grants a Lean pass.
const fs=require("node:fs/promises"),path=require("node:path"),crypto=require("node:crypto"),assert=require("node:assert/strict");
async function main(){const root=__dirname,m=JSON.parse(await fs.readFile(path.join(root,"PUBLIC-SOURCES.json"),"utf8"));for(const [name,digest] of Object.entries(m.files)){assert.ok(/^[A-Za-z0-9_.-]+(?:\/[A-Za-z0-9_.-]+)*$/.test(name)&&!name.split("/").some(p=>p==="."||p===".."));const p=path.join(root,name);assert.equal((await fs.lstat(p)).isFile(),true);assert.equal(crypto.createHash("sha256").update(await fs.readFile(p)).digest("hex"),digest,name);}console.log(JSON.stringify({ok:true,checkedFiles:Object.keys(m.files).length,leanPass:false}));}
main().catch(e=>{console.error(e);process.exitCode=1;});
