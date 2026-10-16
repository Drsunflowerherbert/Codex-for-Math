#!/usr/bin/env python3
"""Run one approved verification step with isolated settings and honest status."""
from pathlib import Path
import argparse,os,subprocess,time,json,hashlib,resource,signal,datetime
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('step');ap.add_argument('--cwd',default=str(ROOT/'build'));ap.add_argument('command',nargs=argparse.REMAINDER)
a=ap.parse_args();cmd=a.command
if cmd and cmd[0]=='--':cmd=cmd[1:]
assert cmd and '/' not in a.step
logpath=ROOT/'logs'/(a.step+'.log');statuspath=ROOT/'logs'/(a.step+'.json')
assert not statuspath.exists(),'Never overwrite prior run status; choose a new step name'
env=os.environ.copy()
for key in list(env):
    if key.startswith('MATHLIB_CACHE_') or key in ['LEAN_PATH','LEAN_SRC_PATH','LEAN_SYSROOT']:
        env.pop(key,None)
prefix=ROOT/'toolchains/lean-4.35.0-rc1-linux'
env.update({'PATH':str(prefix/'bin')+os.pathsep+env.get('PATH',''),'LEAN_NUM_THREADS':'2','MATHLIB_NO_CACHE_ON_UPDATE':'1','MATHLIB_CACHE_DIR':str(ROOT/'cache/mathlib')})
start=time.time();peak=0;stopped=False
print('Starting',a.step,flush=True)
with logpath.open('w') as log:
    proc=subprocess.Popen(cmd,cwd=a.cwd,env=env,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
    try:
        while proc.poll() is None:
            try:current=int(Path('/sys/fs/cgroup/memory.current').read_text());peak=max(peak,current)
            except OSError:pass
            if peak>14*1024**3:
                os.killpg(proc.pid,signal.SIGTERM);stopped=True;break
            time.sleep(1)
        rc=proc.wait()
    except BaseException:
        os.killpg(proc.pid,signal.SIGTERM);proc.wait();raise
result={'step':a.step,'command':cmd,'cwd':a.cwd,'started_at_utc':datetime.datetime.fromtimestamp(start,datetime.timezone.utc).isoformat(),'duration_seconds':round(time.time()-start,3),'exit_code':rc,'resource_stop':stopped,'cgroup_peak_observed_bytes':peak,'resource_sample_interval_seconds':1,'cgroup_memory_scope':'whole task environment, not exclusively the child','settings':{'LEAN_NUM_THREADS':'2','MATHLIB_NO_CACHE_ON_UPDATE':'1','MATHLIB_CACHE_DIR':str(ROOT/'cache/mathlib'),'inherited_cache_endpoint_overrides_removed':True,'source_dependency_lockfile_preserved':True},'log':logpath.name,'log_sha256':hashlib.sha256(logpath.read_bytes()).hexdigest()}
statuspath.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
raise SystemExit(rc if rc>=0 else 128-rc)
