#!/usr/bin/env python3
"""Standalone official export of the four actual target proofs and dependencies.
This does not run or replace the sandboxed comparator.
"""
from pathlib import Path
import os,subprocess,time,json,hashlib,signal,shutil,datetime
ROOT=Path(__file__).resolve().parents[1]
status=json.loads((ROOT/'logs/solution-build-four-threads.json').read_text())
assert status['exit_code']==0 and not status['resource_stop'],'Solution build must first succeed'
prefix=ROOT/'toolchains/lean-4.35.0-rc1-linux/bin'
names=['HolomorphicAnosov.theorem_A','HolomorphicAnosov.theorem_1_1','HolomorphicAnosov.theorem_1_2','HolomorphicAnosov.theorem_1_3']
cmd=[str(prefix/'lake'),'env',str(prefix/'leanexport'),'HolomorphicAnosov.Targets.TheoremA','--']+names
env=os.environ.copy()
for key in list(env):
 if key.startswith('MATHLIB_CACHE_') or key in ['LEAN_PATH','LEAN_SRC_PATH','LEAN_SYSROOT']:env.pop(key,None)
env.update({'PATH':str(prefix)+os.pathsep+env.get('PATH',''),'LEAN_NUM_THREADS':'4','MATHLIB_NO_CACHE_ON_UPDATE':'1','MATHLIB_CACHE_DIR':str(ROOT/'cache/mathlib')})
out=ROOT/'exports/selected-targets.ndjson';err=ROOT/'logs/selected-targets-export.stderr.log';record=ROOT/'logs/selected-targets-export.json'
assert not record.exists(),'Never overwrite a previous run record'
start=time.time();peak=0;anon_peak=0;stop=None
with out.open('wb') as stdout,err.open('wb') as stderr:
 proc=subprocess.Popen(cmd,cwd=ROOT/'build',env=env,stdout=stdout,stderr=stderr,start_new_session=True)
 while proc.poll() is None:
  current=int(Path('/sys/fs/cgroup/memory.current').read_text());peak=max(peak,current)
  stats=dict(line.split() for line in Path('/sys/fs/cgroup/memory.stat').read_text().splitlines());anon_peak=max(anon_peak,int(stats['anon']))
  if anon_peak>12*1024**3:stop='Anonymous task memory exceeded12GiB'
  if shutil.disk_usage(ROOT).free<3*1024**3:stop='Workspace free disk below3GiB'
  if stop:os.killpg(proc.pid,signal.SIGTERM);break
  time.sleep(1)
 rc=proc.wait()
h=hashlib.sha256()
with out.open('rb') as f:
 for block in iter(lambda:f.read(8*1024*1024),b''):h.update(block)
result={'role':'Standalone selected-proof export, not comparator','command':cmd,'source_commit':'65f2b33a7309de661a8500e4642e5609a537a8ff','module':'HolomorphicAnosov.Targets.TheoremA','selected_targets':names,'started_at_utc':datetime.datetime.fromtimestamp(start,datetime.timezone.utc).isoformat(),'duration_seconds':round(time.time()-start,3),'exit_code':rc,'resource_stop':stop,'cgroup_peak_observed_bytes':peak,'cgroup_anon_peak_observed_bytes':anon_peak,'ndjson_bytes':out.stat().st_size,'ndjson_sha256':h.hexdigest(),'stderr_log':err.name,'stderr_sha256':hashlib.sha256(err.read_bytes()).hexdigest(),'stdout_stderr_kept_separate':True,'comparator_sandbox_bypassed':False,'limits':'No challenge/type/definition comparison, permitted-axiom enforcement, or independent-kernel implementation is supplied by this export.'}
record.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
raise SystemExit(rc if rc>=0 else 128-rc)
