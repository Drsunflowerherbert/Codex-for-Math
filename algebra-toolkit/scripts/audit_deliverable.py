#!/usr/bin/env python3
"""Check local links, source separation, build diagnostics and PDF coverage."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import fitz

root=Path(__file__).resolve().parents[1]
errors=[]
for path in root.rglob('*.md'):
    if '.build' in path.parts:continue
    for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
        if '://' in target or target.startswith('#'):continue
        local=target.split('#',1)[0]
        if local and not (path.parent/local).exists():
            errors.append(f'Broken file link: {path.relative_to(root)} -> {target}')

exact=json.loads((root/'evidence/exact-checks.json').read_text())
if exact['status']!='pass' or len(exact['checks'])!=18:
    errors.append('Exact-check evidence missing or unsuccessful')
build=json.loads((root/'evidence/pdf-build.json').read_text())
pdf=root/'algebra-structural-toolkit.pdf'
if hashlib.sha256(pdf.read_bytes()).hexdigest()!=build['pdf_sha256']:
    errors.append('PDF hash differs from build record')
if hashlib.sha256((root/'algebra-structural-toolkit.tex').read_bytes()).hexdigest()!=build['tex_sha256']:
    errors.append('LaTeX hash differs from build record')
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
  'distributed_pdfs':pdfs,
  'scope':'Mechanical completeness and layout diagnostics, not mathematical theorem verification.'}
(root/'evidence/deliverable-audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
raise SystemExit(bool(errors))
