#!/usr/bin/env python3
"""Record source identity and actual compiled project artifacts after successful build."""
from pathlib import Path
import argparse,json,hashlib,subprocess,datetime
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--source-audit-json',type=Path,required=True);a=ap.parse_args()
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(8*1024*1024),b''):h.update(block)
 return h.hexdigest()
def git(args,path):return subprocess.check_output(['git']+args,cwd=path,text=True).strip()
status=json.loads((ROOT/'logs/solution-build-four-threads.json').read_text());assert status['exit_code']==0
source=ROOT/'build';assert git(['rev-parse','HEAD'],source)=='65f2b33a7309de661a8500e4642e5609a537a8ff'
assert git(['diff','--name-only','HEAD'],source)==''
audit=json.loads(a.source_audit_json.read_text());mismatches=[]
for data in audit['module_data'].values():
 if sha(source/data['path'])!=data['sha256']:mismatches.append(data['path'])
assert not mismatches,mismatches
arts=source/'.lake/build/lib/lean';rows=[]
for module in audit['closures']['Comparator.Solution']['local_modules']:
 f=arts/(module.replace('.','/')+'.olean');assert f.exists(),module
 files=[]
 for p in [f,Path(str(f)+'.private'),Path(str(f)+'.server')]:
  if p.exists():files.append({'path':p.relative_to(arts).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
 rows.append({'module':module,'source_sha256':audit['module_data'][module]['sha256'],'artifacts':files})
deps=[]
for dep in json.loads((source/'lake-manifest.json').read_text())['packages']:
 p=source/'.lake/packages'/dep['name'];actual=git(['rev-parse','HEAD'],p);diff=git(['diff','--name-only','HEAD'],p)
 assert actual==dep['rev'] and not diff,(dep['name'],actual,diff)
 deps.append({'name':dep['name'],'revision':actual,'tracked_sources_unchanged':True,'configuration_sha256':sha(p/dep['configFile'])})
result={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_commit':'65f2b33a7309de661a8500e4642e5609a537a8ff','tracked_project_sources_unchanged':True,'source_files_checked':len(audit['module_data']),'all_source_hashes_match_initial_audit':True,'initial_source_audit_json_sha256':sha(a.source_audit_json),'local_solution_closure_modules':len(rows),'artifact_files_hashed':sum(len(r['artifacts']) for r in rows),'challenge_artifact_exists':(arts/'Comparator/Challenge.olean').exists(),'root_manifest_sha256':sha(source/'lake-manifest.json'),'dependencies':deps,'project_module_artifacts':rows,'limits':'These binary hashes identify this execution. Upstream Mathlib artifacts were obtained from official cache, not all rebuilt from source. Hashes alone are not proof verification.'}
(ROOT/'results/source-and-artifact-manifest.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['dependencies','project_module_artifacts']},indent=2))
