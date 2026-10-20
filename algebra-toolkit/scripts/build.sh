#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")/.."
mkdir -p evidence .build
files=(READING-GUIDE.md notes/00-architecture.md
  notes/01-quotients-duality-splitting.md notes/02-operators-as-modules.md
  notes/03-hom-and-tensor.md notes/04-multilinear-and-determinants.md
  notes/05-forms-and-adjoints.md notes/06-exactness-and-homology.md
  notes/07-representations.md notes/08-bridges.md
  notes/09-hadamard-williamson-bridge.md COMPARISON.md SOURCES.md VERIFICATION.md)
python3 - "${files[@]}" <<'PY'
import pathlib,re,sys
text='\n\n'.join(pathlib.Path(p).read_text() for p in sys.argv[1:])
text=re.sub(r'[\u3400-\u9fff]+',lambda m:'\\CJKtext{'+m.group(0)+'}',text)
pathlib.Path('.build/print-source.md').write_text(text)
PY
pandoc .build/print-source.md --from=markdown+tex_math_dollars --to=latex \
  --standalone --number-sections --toc --toc-depth=2 \
  --metadata title='Algebra as a structural toolkit' \
  --metadata subtitle='Foundations, source comparisons, and a Hadamard/Williamson bridge' \
  --metadata author='Research notes for returning to algebra' \
  --metadata date='20 October 2026' \
  --variable documentclass=article --variable fontsize=11pt \
  --variable colorlinks=true --variable linkcolor='blue!45!black' \
  --variable urlcolor='blue!55!black' \
  --variable geometry:margin=24mm \
  --variable mainfont='Latin Modern Roman' \
  --variable sansfont='Latin Modern Sans' \
  --variable monofont='DejaVu Sans Mono' \
  --include-in-header=scripts/header.tex \
  --output=algebra-structural-toolkit.tex
for pass in 1 2 3; do
  xelatex -interaction=nonstopmode -halt-on-error -output-directory=.build \
    algebra-structural-toolkit.tex >"evidence/latex-pass-${pass}.log" 2>&1
done
cp -- .build/algebra-structural-toolkit.pdf algebra-structural-toolkit.pdf
python3 - <<'PY'
import json,pathlib,hashlib,datetime
import fitz
p=pathlib.Path('algebra-structural-toolkit.pdf')
d=fitz.open(p)
record={'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'pdf_pages':len(d),'pdf_bytes':p.stat().st_size,
        'pdf_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
        'tex_sha256':hashlib.sha256(pathlib.Path('algebra-structural-toolkit.tex').read_bytes()).hexdigest(),
        'pages_with_text':sum(bool(page.get_text().strip()) for page in d),
        'note':'Successful LaTeX compilation is layout evidence, not mathematical proof.'}
pathlib.Path('evidence/pdf-build.json').write_text(json.dumps(record,indent=2)+'\n')
print(f'Built {p}: {len(d)} pages.')
PY
