#!/usr/bin/env python3
"""Check all published repository files and explicit provenance/status invariants.

This checks file integrity. It does not compile Lean or certify mathematics.
"""
import argparse,hashlib,json,os,re,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
IGNORED={'.git','.lake','.elan','.cache','tooling','__pycache__','dist','lean-cache'}

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
        if row['bundle'] in {'radial','egyptian','sharp','positive-blocks'} and (name.endswith('.lean') or Path(name).name in {'lake-manifest.json','lakefile.toml','lean-toolchain'}):
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
    print(json.dumps({'status':'passed','publication_files':len(actual),'original_tangent_files_unchanged':len(original),'unchanged_formal_source_and_pin_files':unchanged_formal,'pinned_lean_projects':[p.name for p in projects],'ordinary_core_records':81,'scope':'Whole published repository integrity and explicit status/pin checks; no new mathematical proof certification.'},indent=2))

if __name__=='__main__':main()
