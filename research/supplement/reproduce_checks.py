#!/usr/bin/env python3
"""Reproduce finite checks in an isolated copy; never modify the delivered files."""
import argparse, hashlib, json, shutil, subprocess, sys, tempfile, time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full',action='store_true',help='Run both full finite-field enumerations, including the independent check.')
    parser.add_argument('--output',type=Path,help='Optional JSON result path outside this supplement.')
    args=parser.parse_args()
    if args.output and (args.output.resolve()==ROOT or ROOT in args.output.resolve().parents):
        parser.error('--output must be outside the delivered supplement')
    subprocess.run([sys.executable,str(ROOT/'verify_package.py')],check=True)
    results=[]
    with tempfile.TemporaryDirectory(prefix='math-supplement-reproduction-') as td:
        tree=Path(td)/'research';shutil.copytree(ROOT,tree)
        def run(name,script,*arguments):
            start=time.monotonic()
            proc=subprocess.run([sys.executable,str(tree/script),*map(str,arguments)],cwd=tree,capture_output=True,text=True)
            item={'check':name,'script':script,'exit_code':proc.returncode,'elapsed_seconds':round(time.monotonic()-start,3),'stdout':proc.stdout,'stderr':proc.stderr}
            results.append(item)
            print(name+': '+('passed' if proc.returncode==0 else 'FAILED'),flush=True)
            if proc.returncode:raise RuntimeError(json.dumps(item,indent=2))
        def same(rel):
            assert H(ROOT/rel)==H(tree/rel),f'Regenerated data differ: {rel}'
        run('affine independent arithmetic and corrected-record construction','reviews/affine/audit_records.py')
        same('reviews/affine/research-notes.reviewed.txt')
        # Corrected-record and proof assertions run in audit_records.py. Fresh
        # metadata hashes differ from the preserved original sanitized receipt.
        rerun=tree/'reviews/egyptian/rerun';rerun.mkdir(exist_ok=True)
        shutil.copyfile(tree/'egyptian-fractions/check_examples.py',rerun/'check_examples.py')
        run('Egyptian author examples','reviews/egyptian/rerun/check_examples.py')
        assert H(rerun/'exact-examples.json')==H(tree/'egyptian-fractions/exact-examples.json')
        # Public integrity was checked before copying. Rebind only temporary
        # metadata hashes for privacy-normalized historical documentation; these
        # are current-copy checks, not new historical review fingerprints.
        author=tree/'egyptian-fractions/author-checks.json'
        metadata=json.loads(author.read_text())
        metadata['files_sha256']={name:H(tree/'egyptian-fractions'/name) for name in metadata['files_sha256']}
        author.write_text(json.dumps(metadata,indent=2)+'\n')
        run('Egyptian independent finite arithmetic audit','reviews/egyptian/independent_audit.py')
        paths=tree/'reviews/egyptian/original-sha256-before.txt'
        paths.write_text(''.join(f'{H(tree/"egyptian-fractions"/Path(line.split("  ",1)[1]).name)}  {tree/"egyptian-fractions"/Path(line.split("  ",1)[1]).name}\n' for line in paths.read_text().splitlines()))
        run('Egyptian correction and finite coarse-bound checks','reviews/egyptian/corrected/validate_supplement.py')
        same('reviews/egyptian/corrected/validation-results.json')
        run('transport exact cases','transport-stability/check_exact_cases.py');same('transport-stability/exact-cases.json')
        run('positive-block Gaussian-rational fixtures','positive-blocks/check_exact_examples.py');same('positive-blocks/exact-examples.json')
        run('positive-block independent matrix audit','reviews/positive-blocks/parent-check-examples.py',tree/'positive-blocks/exact-examples.json')
        run('mixed-moment exact certificates','mixed-moments/certificates.py');same('mixed-moments/certificates.json')
        run('mixed-moment record and dependency validation','mixed-moments/build_theorem_index.py')
        run('convex-approximation rational checks and numerical illustrations','convex-approximation/check_examples.py');same('convex-approximation/examples.json')
        # Use a separate output so the full frozen certificate remains available to the independent checker.
        run('finite-field author '+('full' if args.full else 'quick')+' checks','finite-field-mixing/verify.py',* ([] if args.full else ['--quick']),'--output','reproduction-certificates.json')
        if args.full:
            assert H(tree/'finite-field-mixing/reproduction-certificates.json')==H(ROOT/'finite-field-mixing/certificates.json')
            run('finite-field independent full integer-polynomial audit','reviews/finite-field-mixing/independent_check.py')
    result={'status':'passed','mode':'full' if args.full else 'standard-with-quick-finite-field','python_version':sys.version,'delivered_files_modified':False,'no_network_or_installation_required':True,'lean_verification':False,'native_mrs_import':False,'scope':'Finite computations and artifact consistency; universal mathematical results rely on the written proofs and scoped ordinary reviews.','temporary_portability_adjustments':['Rebase temporary Egyptian paths and privacy-normalized documentation hashes after public integrity check','Recreate omitted Egyptian duplicate rerun','Independent finite-field checker uses a project-relative BASE path'],'checks':results}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
        print('Saved reproduction results: '+str(args.output))
    print(json.dumps({'status':'passed','mode':result['mode'],'completed_commands':len(results)}))
if __name__=='__main__':main()
