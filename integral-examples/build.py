#!/usr/bin/env python3
"""Build readable guide and complete worked collection using Pandoc/pdfLaTeX."""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(path, anchors):
    text = path.read_text()
    if path.parent.name == 'examples':
        example_id = path.name.split('-')[0]
        text = re.sub(r'^(# .+)$', r'\1 {#' + example_id + '}', text,
                      count=1, flags=re.MULTILINE)
    else:
        anchor = anchors.get(path.name)
        if anchor:
            text = re.sub(r'^(# .+)$', r'\1 {#' + anchor + '}', text,
                          count=1, flags=re.MULTILINE)

    def replace_link(match):
        label, target = match.group(1), match.group(2)
        if re.match(r'^[A-Za-z]+:', target) or target.startswith('#'):
            return match.group(0)
        name = Path(target.split('#')[0]).name
        if name in anchors:
            return f'[{label}](#{anchors[name]})'
        url = ('https://github.com/Drsunflowerherbert/Codex-for-Math/tree/'
               'codex/integral-examples-2026-10-15/integral-examples/' + target)
        return f'[{label}]({url})'

    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, text)


def build(name, paths, anchors, temporary):
    combined = temporary / f'{name}.md'
    included = {path.name for path in paths}
    local_anchors = {key: value for key, value in anchors.items() if key in included}
    combined.write_text('\n\n'.join(prepare(path, local_anchors) for path in paths))
    tex = ROOT / 'pdf' / f'{name}.tex'
    pdf = tex.with_suffix('.pdf')
    title = ('Concrete Lebesgue and Hausdorff Integral Applications'
             if name == 'integral-examples' else 'Integral Applications: Study Guide')
    common = ['pandoc', str(combined), '--from=markdown+tex_math_dollars',
              '--standalone', '--toc', '--number-sections',
              '--metadata', f'title={title}', '--metadata', 'date=15 October 2026',
              '-V', 'documentclass=article', '-V', 'geometry:margin=25mm',
              '-V', 'fontsize=11pt', '-V', 'colorlinks=true',
              '-V', 'linkcolor=blue', '-V', 'urlcolor=blue',
              '--lua-filter', str(ROOT / 'checks/pdf-format.lua')]
    subprocess.run(common + ['--to=latex', '--output', str(tex)],
                   cwd=ROOT, check=True, capture_output=True, text=True)
    # Long commit IDs and filenames remain readable without overflowing margins.
    latex = tex.read_text()
    def break_code(match):
        token = match.group(1)
        if len(token) >= 32 and not re.search(r'[./-]', token):
            token = r'\allowbreak{}'.join(token[i:i+8] for i in range(0, len(token), 8))
        else:
            token = re.sub(r'([./-])', lambda split: split.group(1) + r'\allowbreak{}', token)
        return r'\texttt{' + token + '}'
    latex = re.sub(r'\\texttt\{([A-Za-z0-9./-]+)\}', break_code, latex)
    latex = latex.replace('Parameters/convergence', r'Parameters/\allowbreak{}convergence')
    latex = re.sub(r'(?m)^Tags:(.*?)(?=\n\n)',
                   lambda match: r'\begingroup\small\raggedright Tags:' + match.group(1) + r'\par\endgroup',
                   latex, flags=re.DOTALL)
    tex.write_text(latex)
    # Compile the retained LaTeX itself, so the PDF is demonstrably its output.
    for _ in range(3):
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
             '-output-directory', str(temporary), str(tex)],
            cwd=ROOT, capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stdout[-12000:] + result.stderr[-2000:])
    shutil.copy2(temporary / pdf.name, pdf)
    log = (temporary / f'{name}.log').read_text(errors='replace')
    warnings = [line.strip() for line in log.splitlines()
                if 'Warning:' in line or 'Overfull' in line or 'Underfull' in line]
    return {'name': name, 'inputs': {str(p.relative_to(ROOT)): digest(p) for p in paths},
            'latex': str(tex.relative_to(ROOT)), 'latex_sha256': digest(tex),
            'pdf': str(pdf.relative_to(ROOT)), 'pdf_sha256': digest(pdf),
            'warnings': warnings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--guide-only', action='store_true')
    args = parser.parse_args()
    for tool in ('pandoc', 'pdflatex'):
        if not shutil.which(tool):
            raise SystemExit(f'Required build tool unavailable: {tool}')
    (ROOT / 'pdf').mkdir(exist_ok=True)
    anchors = {'README.md': 'start', 'PROBLEMS.md': 'problems',
               'CONVENTIONS.md': 'conventions', 'COUNTEREXAMPLES.md': 'atlas',
               'SOURCES.md': 'bibliography', 'VERIFICATION.md': 'verification'}
    anchors.update({path.name: path.name.split('-')[0]
                    for path in (ROOT / 'examples').glob('E*.md')})
    guide_paths = [ROOT / name for name in ('README.md', 'PROBLEMS.md',
                   'CONVENTIONS.md', 'COUNTEREXAMPLES.md', 'SOURCES.md')]
    full_paths = [ROOT / 'README.md', ROOT / 'PROBLEMS.md', ROOT / 'CONVENTIONS.md',
                  *sorted((ROOT / 'examples').glob('E*.md')),
                  ROOT / 'COUNTEREXAMPLES.md', ROOT / 'SOURCES.md',
                  ROOT / 'VERIFICATION.md']
    with tempfile.TemporaryDirectory(prefix='integral-examples-build-') as folder:
        temporary = Path(folder)
        records = [build('guide', guide_paths, anchors, temporary)]
        if not args.guide_only:
            if len(list((ROOT / 'examples').glob('E*.md'))) != 16:
                raise SystemExit('Expected exactly 16 examples before full build.')
            records.append(build('integral-examples', full_paths, anchors, temporary))
    evidence = {'scope': 'LaTeX/PDF compilation and source hashes; not mathematical proof.',
                'pandoc': subprocess.check_output(['pandoc', '--version'], text=True).splitlines()[0],
                'pdflatex': subprocess.check_output(['pdflatex', '--version'], text=True).splitlines()[0],
                'builds': records}
    (ROOT / 'checks' / 'pdf-build.json').write_text(json.dumps(evidence, indent=2) + '\n')
    for record in records:
        print(record['pdf'], record['pdf_sha256'])
        for warning in record['warnings']:
            print('  ' + warning)


if __name__ == '__main__':
    main()
