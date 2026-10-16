#!/usr/bin/env python3
"""Verify the public file manifest at an immutable GitHub commit.

Only downloads public content and computes hashes; does not execute downloaded code.
"""
import argparse,hashlib,json,re,urllib.request

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('commit',help='full 40-character commit SHA')
    ap.add_argument('--output',help='optional local JSON evidence file')
    args=ap.parse_args()
    if not re.fullmatch('[0-9a-f]{40}',args.commit):ap.error('a full lowercase commit SHA is required')
    base='https://raw.githubusercontent.com/Drsunflowerherbert/Codex-for-Math/'+args.commit+'/holomorphic-anosov-review/'
    def get(path):
        req=urllib.request.Request(base+path,headers={'User-Agent':'Mathematical-review-file-verifier'})
        with urllib.request.urlopen(req,timeout=60) as f:return f.read()
    manifest=get('SHA256SUMS')
    checks=[]
    for line in manifest.decode().splitlines():
        digest,path=line.split('  ',1)
        if not re.fullmatch('[0-9a-f]{64}',digest) or path.startswith('/') or '..' in path.split('/'):
            raise ValueError('Invalid manifest entry')
        data=get(path);actual=hashlib.sha256(data).hexdigest()
        checks.append({'path':path,'bytes':len(data),'expected_sha256':digest,'actual_sha256':actual,'match':actual==digest})
    result={'repository':'Drsunflowerherbert/Codex-for-Math','commit':args.commit,
            'method':'HTTPS download of immutable raw files; SHA-256 comparison with manifest',
            'manifest_sha256':hashlib.sha256(manifest).hexdigest(),
            'checked_files':len(checks),'all_match':all(c['match'] for c in checks),'files':checks}
    if args.output:
        with open(args.output,'w') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='files'},indent=2))
    if not result['all_match']:raise SystemExit(1)
if __name__=='__main__':main()
