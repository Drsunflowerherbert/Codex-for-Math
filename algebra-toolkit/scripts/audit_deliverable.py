#!/usr/bin/env python3
"""Check local links, source separation, build diagnostics and PDF coverage."""
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import fitz

root=Path(__file__).resolve().parents[1]
errors=[]
def links(node):
    if isinstance(node,dict):
        if node.get('t') in ('Link','Image'):
            yield node['c'][-1][0]
        for value in node.values():yield from links(value)
    elif isinstance(node,list):
        for value in node:yield from links(value)

for path in root.rglob('*.md'):
    if '.build' in path.parts:continue
    parsed=json.loads(subprocess.check_output(
        ['pandoc','--from=markdown+tex_math_dollars+tex_math_single_backslash','--to=json'],
        input=path.read_text(),text=True))
    for target in links(parsed):
        if '://' in target or target.startswith('#'):continue
        local=target.split('#',1)[0]
        if local and not (path.parent/local).exists():
            errors.append(f'Broken file link: {path.relative_to(root)} -> {target}')

exact=json.loads((root/'evidence/exact-checks.json').read_text())
if exact['status']!='pass' or len(exact['checks'])!=18:
    errors.append('Exact-check evidence missing or unsuccessful')
if exact.get('script_sha256')!=hashlib.sha256((root/'scripts/check_examples.py').read_bytes()).hexdigest():
    errors.append('Exact-check script differs from executed evidence')
phase2=json.loads((root/'evidence/phase2-checks.json').read_text())
if phase2['status']!='pass' or phase2['chapter_check_groups']!=28 or phase2['source_erratum_check_groups']!=1:
    errors.append('Continuation-check evidence missing or unsuccessful')
if phase2['runner_sha256']!=hashlib.sha256((root/'scripts/check_phase2.py').read_bytes()).hexdigest():
    errors.append('Continuation runner differs from executed evidence')
for check in phase2['checks']:
    if check['script_sha256']!=hashlib.sha256((root/check['script']).read_bytes()).hexdigest():
        errors.append('Continuation script differs from evidence: '+check['script'])
build=json.loads((root/'evidence/pdf-build.json').read_text())
pdf=root/'algebra-structural-toolkit.pdf'
if hashlib.sha256(pdf.read_bytes()).hexdigest()!=build['pdf_sha256']:
    errors.append('PDF hash differs from build record')
if hashlib.sha256((root/'algebra-structural-toolkit.tex').read_bytes()).hexdigest()!=build['tex_sha256']:
    errors.append('LaTeX hash differs from build record')
for name,expected in build.get('input_sha256',{}).items():
    if hashlib.sha256((root/name).read_bytes()).hexdigest()!=expected:
        errors.append('Build input changed since compilation: '+name)
if not build.get('input_sha256'):
    errors.append('Build inputs are not bound to this PDF')
review=json.loads((root/'evidence/phase2-review.json').read_text())
if review['status']!='complete_reviewed' or review['remaining_blockers']:
    errors.append('Continuation review is incomplete')
if review['visual_inspection']['pdf_sha256']!=build['pdf_sha256']:
    errors.append('Visual inspection belongs to a different PDF')
for group in ['original_manuscript_sha256','guide_and_review_sha256']:
    for name,expected in review[group].items():
        if hashlib.sha256((root/name).read_bytes()).hexdigest()!=expected:
            errors.append('Reviewed file changed since the final record: '+name)
independent=review['independent_sylvester_check']
if hashlib.sha256((root/independent['script']).read_bytes()).hexdigest()!=independent['script_sha256']:
    errors.append('Independent review checker changed since execution')
diagnostics=(root/'evidence/latex-pass-3.log').read_text()
bad=re.findall(r'^.*(?:Overfull|Missing character|Warning|Error).*$',diagnostics,re.M)
errors.extend('LaTeX diagnostic: '+line for line in bad)
doc=fitz.open(pdf)
all_text='\n'.join(page.get_text() for page in doc)
flat=' '.join(all_text.split())
required=['Quotients, duality, and splitting','Operators as modules and polynomial projections',
  'Hom and tensor products','Free algebras, exterior powers, determinants, and minors',
  'Forms, adjoints, and the correct equivalence relation',
  'Exact sequences, extensions, and calibrated homological algebra',
  'Representations and semisimplicity','A concrete destination: Hadamard and Williamson foundations',
  'Source ledger and page conventions','Verification record, corrections, and limits',
  'A reconstructive map: from decompositions to their obstructions',
  'Invariant complements as a computable extension obstruction',
  'Repairing linear maps: spectral projection, separability, and averaging',
  'Integral spectral gluing: the lattice behind Fourier coordinates',
  'Compression, orthogonal ideals, and a common-lift obstruction',
  'Proof-level comparison: operators and multilinear constructions',
  'A selective reconstruction of Xi I and III: proof routes, prerequisites, and stopping tests',
  '基础代数']
for heading in required:
    if heading not in flat:errors.append('Missing PDF coverage: '+heading)
for page in doc:
    if not page.get_text().strip():errors.append('Blank PDF page')
# Only our own PDF is included. No source book/image/materialization metadata.
pdfs=[str(p.relative_to(root)) for p in root.rglob('*.pdf') if '.build' not in p.parts]
if pdfs!=['algebra-structural-toolkit.pdf']:errors.append('Unexpected PDF distribution: '+str(pdfs))
for path in root.rglob('*'):
    if '.build' in path.parts or not path.is_file():continue
    if path.name in ['transfers.json','hirsch-search.json'] or path.suffix in ['.png','.jpg']:
        errors.append('Unexpected private source material: '+str(path))
result={'timestamp_utc':datetime.now(timezone.utc).isoformat(),
  'status':'pass' if not errors else 'fail','errors':errors,'pdf_pages':len(doc),
  'required_sections_present':len(required),'local_file_links':'checked',
  'exact_check_groups':len(exact['checks']),'latex_final_pass_diagnostics':bad,
  'continuation_check_groups':phase2['chapter_check_groups']+phase2['source_erratum_check_groups'],
  'visually_inspected_pdf_pages':review['visual_inspection']['physical_pdf_pages'],
  'distributed_pdfs':pdfs,
  'scope':'Mechanical completeness and layout diagnostics, not mathematical theorem verification.'}
(root/'evidence/deliverable-audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
raise SystemExit(bool(errors))
