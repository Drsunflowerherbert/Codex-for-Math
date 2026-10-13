#!/usr/bin/env python3
"""Check all published repository files and explicit provenance/status invariants.

This checks file integrity. It does not compile Lean or certify mathematics.
"""
import argparse,hashlib,json,os,re,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
IGNORED={'.git','.lake','.elan','.cache','tooling','__pycache__','dist','lean-cache'}
ROUND_ROOTS={'lp-certificates','transport-sharpness','evidence-hardening','lp-sparse-discovery'}

def paths():
    for base,dirs,files in os.walk(ROOT,followlinks=False):
        dirs[:]=sorted(d for d in dirs if d not in IGNORED)
        for directory in dirs:
            assert not (Path(base)/directory).is_symlink(),str(Path(base)/directory)
        for f in sorted(files):
            p=Path(base)/f
            if f=='.git' or (p.name=='FILES.json' and p.parent==ROOT/'publication'):continue
            if p.suffix=='.pyc':continue
            yield p

def main():
    global ROOT
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=ROOT,help='Repository snapshot to check, including extracted copies without Git.')
    ROOT=parser.parse_args().root.resolve()
    manifest=json.loads((ROOT/'publication/FILES.json').read_text())
    actual={str(p.relative_to(ROOT)):p for p in paths()}
    expected=manifest['files']
    assert set(expected)==set(actual),{'missing':sorted(set(expected)-set(actual)),'extra':sorted(set(actual)-set(expected))}
    if (ROOT/'.git').exists():
        listed=subprocess.check_output(['git','ls-files','-z','--cached','--others','--exclude-standard'],cwd=ROOT)
        tracked={p.decode() for p in listed.split(b'\0') if p}
        tracked.discard('publication/FILES.json')
        assert tracked==set(actual),'Git publication file set differs from the whole-repository manifest.'
    for name,p in actual.items():
        assert not p.is_symlink(),name
        data=p.read_bytes();row=expected[name]
        assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256'],name
        assert p.suffix not in {'.zip','.pyc','.olean','.ilean','.so','.a','.o','.png','.jpg'},name
        text=data.decode('utf-8')
        assert not any(ord(c)<32 and c not in '\n\r\t' for c in text),name
        assert not re.search(r'libfile_[A-Za-z0-9]+|file_00000000[A-Za-z0-9]+|github_pat_[A-Za-z0-9_]{20,}|gh[opusr]_[A-Za-z0-9]{20,}|-----BEGIN (?:RSA |EC |OPENSSH |)PRIVATE KEY-----|oaiusercontent\.com|"download_url"\s*:|"transfer_id"\s*:',text),name
        if p.suffix=='.json':json.loads(text)
    mapping=json.loads((ROOT/'publication/SOURCE-MAP.json').read_text())
    unchanged_formal=0
    for row in mapping['files']:
        name=row.get('published_file')
        if not name:continue
        digest=hashlib.sha256(actual[name].read_bytes()).hexdigest()
        assert digest==row['published_sha256'],name
        if row['bundle'] in {'radial','egyptian','sharp','positive-blocks','convex','mixed-moment'} and (name.endswith('.lean') or Path(name).name in {'lake-manifest.json','lakefile.toml','lean-toolchain'}):
            assert digest==row['source_sha256'],('formal-source drift',name)
            unchanged_formal+=1
    # This immutable earlier batch is historical; its protected proof/pin files
    # remain exact sources. Current documentation bytes use FILES.json instead.
    for historical in mapping.get('historical_source_maps',[]):
        batch=json.loads((ROOT/historical).read_text())
        for row in batch['records']:
            name=row.get('public_path')
            if not name or not row.get('source_sha256'):continue
            if name.endswith('.lean') or Path(name).name in {'lake-manifest.json','lakefile.toml','lean-toolchain'}:
                assert hashlib.sha256(actual[name].read_bytes()).hexdigest()==row['source_sha256'],('historical formal-source drift',name)
                unchanged_formal+=1
    round_sources=round_protected=round_corrected=0
    for current_map in mapping.get('current_source_maps',[]):
        batch=json.loads((ROOT/current_map).read_text())
        assert batch['schema']=='october-13-publication-source-map/v1'
        components=batch['frozen_components']
        assert set(components)<=ROUND_ROOTS
        assert set(components)=={name.split('/')[0] for name in actual if name.split('/')[0] in ROUND_ROOTS},'Published round component missing from source map.'
        assert all(re.fullmatch('[0-9a-f]{40}',commit) for commit in components.values())
        seen=set()
        protected_pins={'lean-toolchain','lakefile.toml','lake-manifest.json','fixture-policy.json','baseline.json'}
        for row in batch['files']:
            source=row['source_file'];name=row['published_file']
            component=source.split('/')[0]
            assert component in components and row['source_commit']==components[component]
            assert name.startswith(component+'/') and name not in seen,name
            assert all(part not in {'.','..',''} for part in Path(source).parts+Path(name).parts),name
            seen.add(name)
            data=actual[name].read_bytes();digest=hashlib.sha256(data).hexdigest()
            assert digest==row['published_sha256'] and len(data)==row['published_bytes'],name
            assert row['source_mode'] in {'100644','100755'}
            assert re.fullmatch('[0-9a-f]{40}',row['source_blob'])
            assert re.fullmatch('[0-9a-f]{64}',row['source_sha256'])
            protected=Path(source).suffix in {'.lean','.py','.cjs'} or Path(source).name in protected_pins
            assert row['protected_source']==protected,name
            corrected=protected and row['action']=='publication_code_fix'
            if corrected:
                assert source==name=='lp-certificates/bridge.py',name
                fix=row['publication_fix']
                assert fix['current_sha256']==digest and fix['original_sha256']==row['source_sha256'],name
                assert fix['proof_sources_and_gates_changed'] is False,name
                round_corrected+=1
            elif protected or row['action'] in {'retained_unchanged','copied_and_renamed'}:
                assert digest==row['source_sha256'] and len(data)==row['source_bytes'],('round source drift',name)
                assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==row['source_blob'],name
            if protected:round_protected+=1
            if row['action']=='sanitized_metadata' and Path(name).suffix=='.json':
                derivative=json.loads(data)
                info=derivative['publication_derivative']
                if info.get('publication_profile')=='recheckable_lp_package_metadata':
                    assert re.fullmatch(r'lp-certificates/evidence/checked-(author-batch|independent-batch|relocated-recheck)/receipt.json',name),name
                    assert derivative['schema']==info['original_schema']=='lp-certificates-checked-bridge/v1',name
                else:
                    assert derivative['schema']=='publication-metadata-derivative/v1',name
                assert info['original_commit']==row['source_commit'] and info['original_sha256']==row['source_sha256'] and info['original_bytes']==row['source_bytes'],name
                assert info['new_mathematical_verification'] is False,name
            round_sources+=1
        generated=set(batch['generated_publication_files'])
        assert not seen&generated
        assert all(name.startswith(tuple(component+'/' for component in components)) for name in generated)
        assert seen|generated=={name for name in actual if name.split('/')[0] in components},'Incomplete current component source map.'
    original=manifest['unchanged_original_tangent_files']
    assert set(original)=={name for name in actual if name.startswith('tangent-limit/')}
    for name,digest in original.items():
        assert hashlib.sha256(actual[name].read_bytes()).hexdigest()==digest,('original tangent drift',name)
    projects=sorted(p for p in ROOT.iterdir() if p.is_dir() and (p/'lean-toolchain').is_file())
    for directory in projects:
        project=directory.name
        assert (ROOT/project/'lean-toolchain').read_text().strip()=='leanprover/lean4:v4.24.0'
        packages=json.loads((ROOT/project/'lake-manifest.json').read_text())['packages']
        assert all(re.fullmatch('[0-9a-f]{40}',p['rev']) for p in packages)
        assert next(p for p in packages if p['name']=='mathlib')['rev']=='f897ebcf72cd16f89ab4577d0c826cd14afaafc7'
    index=json.loads((ROOT/'research/supplement/STUDY-INDEX.json').read_text())
    assert sum(s['core_record_count'] for s in index['studies'])==index['core_record_total']==81
    assert all(s['lean_verification']=='not_performed' for s in index['studies'])
    print(json.dumps({'status':'passed','publication_files':len(actual),'original_tangent_files_unchanged':len(original),'unchanged_formal_source_and_pin_files':unchanged_formal,'october_13_source_dispositions':round_sources,'october_13_protected_sources':round_protected,'october_13_publication_source_fixes':round_corrected,'pinned_lean_projects':[p.name for p in projects],'ordinary_core_records':81,'scope':'Whole published repository integrity and explicit status/pin checks; no new mathematical proof certification.'},indent=2))

if __name__=='__main__':main()
