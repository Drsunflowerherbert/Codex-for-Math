"use strict";
// Byte comparison against git tree objects ignores index-stat optimizations.
const fs=require('node:fs/promises'),path=require('node:path'),crypto=require('node:crypto');
const {execFile}=require('node:child_process'),{promisify}=require('node:util');
const exec=promisify(execFile),I=require('./io.cjs');
async function checkGitSource(directory,revision){
  I.need(typeof revision==='string'&&/^[a-f0-9]{40}$/.test(revision),'exact SHA1 revision required');
  const root=await fs.realpath(directory),read=await I.reader(root),env={...process.env};for(const k of Object.keys(env))if(k.startsWith('GIT_'))delete env[k];
  const git=async args=>(await exec('/usr/bin/git',['--no-replace-objects','-c','core.fsmonitor=false',...args],{cwd:root,env,encoding:'buffer',maxBuffer:16777216,timeout:60000})).stdout;
  I.need(I.utf8(await git(['rev-parse','HEAD'])).trim()===revision,'package HEAD differs from pin');
  const tree=I.utf8(await git(['ls-tree','-r','--full-tree','-z',revision])).split('\0').filter(Boolean);
  I.need(tree.length>0&&tree.length<=40000,'git tree size unsupported');const files=[],tracked=new Set(),links=new Set();let total=0;
  for(const item of tree){const m=/^(100644|100755|120000) blob ([a-f0-9]{40})\t(.+)$/.exec(item);I.need(m&&I.portable(m[3]),'unsupported tree entry (submodule/path)');
    let b;
    if(m[1]==='120000'){
      {
        I.need(m[3].endsWith('.md'),'only documentation symlink metadata is supported');let at=root;const parts=m[3].split('/');
        for(const [i,part] of parts.entries()){at=path.join(at,part);const st=await fs.lstat(at);I.need(i===parts.length-1?st.isSymbolicLink():st.isDirectory()&&!st.isSymbolicLink(),'changed symlink ancestry');}
        b=await fs.readlink(at,{encoding:'buffer'});links.add(m[3]);
      }
    }else b=await read(m[3]);total+=b.length;I.need(total<=536870912,'source closure size limit');
    const actual=crypto.createHash('sha1').update(Buffer.from('blob '+b.length+'\0')).update(b).digest('hex');
    I.need(actual===m[2],'tracked source bytes differ from git tree: '+m[3]);tracked.add(m[3]);files.push({path:m[3],kind:m[1]==='120000'?'documentation_symlink_target_bytes':'regular_file_bytes',bytes:b.length,sha256:I.sha(b)});
  }
  let visited=0;
  async function walk(at,rel=''){
    for(const d of await fs.readdir(at,{withFileTypes:true})){
      I.need(++visited<=80000,'worktree entry limit');if(['.git','.lake','.cache','.elan'].includes(d.name))continue;
      const p=rel?rel+'/'+d.name:d.name;I.need(!d.isSymbolicLink()||links.has(p),'worktree symlink unsupported: '+p);
      if(d.isDirectory())await walk(path.join(at,d.name),p);
      else if(/\.(lean|olean|ilean|ir)$/.test(d.name))I.need(tracked.has(p),'untracked Lean import/product outside cache: '+p);
    }
  }
  await walk(root);files.sort((a,b)=>a.path.localeCompare(b.path,'en'));
  return {ok:true,kind:'tracked_source_byte_identity',revision,files,sourceClosureSHA256:I.sha(I.canonicalJSON(files)),leanPass:false,formalProofAcceptance:'not_performed',externalCaches:'excluded_and_trusted',importClosureCompleteness:'not_established_for_arbitrary_Lean'};
}
if(require.main===module)checkGitSource(process.argv[2],process.argv[3]).then(r=>console.log(JSON.stringify(r,null,2))).catch(e=>{console.error(JSON.stringify({ok:false,leanPass:false,error:e.message}));process.exitCode=2;});
module.exports={checkGitSource};
