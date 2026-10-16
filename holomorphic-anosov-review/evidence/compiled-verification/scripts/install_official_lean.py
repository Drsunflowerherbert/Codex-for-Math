#!/usr/bin/env python3
"""Fetch official pinned Lean artifact, verify supplied digest, safely extract.
No repository setup code is executed by this installer.
"""
from pathlib import Path, PurePosixPath
import json,hashlib,time,urllib.request,tarfile,zstandard,platform
ROOT=Path(__file__).resolve().parents[1]
meta=json.loads((ROOT/'provenance/lean-release-metadata.json').read_text())
assert meta['tag_name']=='v4.35.0-rc1'
assert platform.machine()=='x86_64'
asset=next(a for a in meta['assets'] if a['name']=='lean-4.35.0-rc1-linux.tar.zst')
assert asset['browser_download_url'].startswith('https://github.com/leanprover/lean4/releases/download/v4.35.0-rc1/')
expected=asset['digest'].removeprefix('sha256:');assert len(expected)==64
archive=ROOT/'downloads'/asset['name']
start=time.time()
if not archive.exists():
    req=urllib.request.Request(asset['browser_download_url'],headers={'User-Agent':'Lean-pinned-verification'})
    total=0;last=0
    with urllib.request.urlopen(req,timeout=60) as response, archive.with_suffix('.partial').open('wb') as f:
        for chunk in iter(lambda:response.read(8*1024*1024),b''):
            f.write(chunk);total+=len(chunk)
            if total-last>=128*1024*1024:
                print('Downloaded',total,'bytes',flush=True);last=total
    archive.with_suffix('.partial').rename(archive)
h=hashlib.sha256()
with archive.open('rb') as f:
    for chunk in iter(lambda:f.read(8*1024*1024),b''):h.update(chunk)
actual=h.hexdigest()
assert archive.stat().st_size==asset['size'],(archive.stat().st_size,asset['size'])
assert actual==expected,(actual,expected)
print('Verified official SHA-256:',actual,flush=True)
extract=ROOT/'toolchains';prefix='lean-4.35.0-rc1-linux'
count=0
with archive.open('rb') as src, zstandard.ZstdDecompressor().stream_reader(src) as stream, tarfile.open(fileobj=stream,mode='r|') as tar:
    for member in tar:
        parts=PurePosixPath(member.name).parts
        assert parts and parts[0]==prefix,member.name
        assert not member.isdev(),member.name
        tar.extract(member,path=extract,filter='data');count+=1
result={'official_release_url':meta['html_url'],'tag':meta['tag_name'],'asset':asset['name'],'official_download_url':asset['browser_download_url'],'expected_bytes':asset['size'],'actual_bytes':archive.stat().st_size,'api_supplied_sha256':expected,'actual_sha256':actual,'digest_match':actual==expected,'safe_extraction_filter':'Python tarfile data filter; required single expected prefix; no devices','extracted_members':count,'duration_seconds':round(time.time()-start,3),'repository_setup_scripts_executed':False}
(ROOT/'provenance/toolchain-installation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
