#!/usr/bin/env python3
"""Fetch only lockfile-listed Git sources at exact revisions; run no setup hooks."""
from pathlib import Path
import json,subprocess,hashlib,time,urllib.parse
ROOT=Path(__file__).resolve().parents[1];build=ROOT/'build'
manifest=build/'lake-manifest.json';before=hashlib.sha256(manifest.read_bytes()).hexdigest()
rows=[]
with (ROOT/'logs/dependencies-fetch.log').open('w') as log:
    def run(args,cwd):
        log.write('$ '+' '.join(args)+'\n');log.flush()
        subprocess.run(args,cwd=cwd,check=True,stdout=log,stderr=subprocess.STDOUT)
    for dep in json.loads(manifest.read_text())['packages']:
        parsed=urllib.parse.urlparse(dep['url'])
        assert parsed.scheme=='https' and parsed.netloc=='github.com'
        assert parsed.path.split('/')[1] in ['leanprover','leanprover-community']
        rev=dep['rev'];assert len(rev)==40 and all(c in '0123456789abcdef' for c in rev)
        dest=build/'.lake/packages'/dep['name'];dest.mkdir(parents=True,exist_ok=True)
        start=time.time()
        if not (dest/'.git').exists():
            run(['git','-c','core.hooksPath=/dev/null','init'],dest)
            run(['git','remote','add','origin',dep['url']],dest)
        run(['git','-c','core.hooksPath=/dev/null','fetch','--depth=1','origin',rev],dest)
        run(['git','-c','core.hooksPath=/dev/null','checkout','--detach','FETCH_HEAD'],dest)
        actual=subprocess.check_output(['git','rev-parse','HEAD'],cwd=dest,text=True).strip();assert actual==rev
        config=dest/dep['configFile']
        rows.append({'name':dep['name'],'url':dep['url'],'expected_revision':rev,'actual_revision':actual,'matches':True,'config_file':dep['configFile'],'config_sha256':hashlib.sha256(config.read_bytes()).hexdigest(),'elapsed_seconds':round(time.time()-start,3)})
        print('Fetched',dep['name'],actual,flush=True)
assert hashlib.sha256(manifest.read_bytes()).hexdigest()==before
(ROOT/'provenance/dependency-installation.json').write_text(json.dumps({'root_source_commit':'65f2b33a7309de661a8500e4642e5609a537a8ff','manifest_sha256':before,'manifest_unchanged':True,'method':'Git fetch depth1 exact lockfile revisions; detached checkouts; no update/setup hooks','dependencies':rows},indent=2)+'\n')
