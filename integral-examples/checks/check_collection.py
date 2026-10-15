#!/usr/bin/env python3
"""Check collection completeness, retrieval metadata, review hashes and local links.

This is a structural/publication check, not a mathematical proof checker.
"""
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def main():
    data = json.loads((ROOT / 'metadata.json').read_text())
    records = data['examples']
    assert [row['id'] for row in records] == [f'E{n:02}' for n in range(1, 17)]
    sources = (ROOT / 'SOURCES.md').read_text()
    source_ids = set(re.findall(r'^## `([^`]+)`', sources, re.MULTILINE))
    manifest = json.loads((ROOT / 'reviews/review-manifest.json').read_text())['examples']
    required_headings = ['Problem', 'Data and hypotheses', 'Solution',
                         'Why the theorem applies', 'Pitfalls', 'Reusable technique', 'Sources']
    for row in records:
        path = ROOT / row['file']
        text = path.read_text()
        assert text.startswith('# ' + row['id']), path
        for heading in required_headings:
            assert f'## {heading}\n' in text, (path, heading)
        assert set(row['source_ids']) <= source_ids, row['id']
        for field in ('topics', 'prerequisites', 'techniques', 'hypotheses'):
            assert isinstance(row[field], list) and row[field], (row['id'], field)
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        verification = row['verification']
        assert sha == verification['reviewed_sha256'] == manifest[row['id']]['sha256'], row['id']
        assert sha in (ROOT / verification['review_file']).read_text(), row['id']
    snapshots = json.loads((ROOT / 'checks/source-references.json').read_text())
    assert {entry['source_id'] for entry in snapshots['sources']} == source_ids
    for entry in snapshots['sources'] + snapshots['auxiliary_source_snapshots']:
        assert re.fullmatch(r'[0-9a-f]{64}', entry['pdf_sha256'])
        assert entry['pdf_bytes'] > 0 and entry['http_head_status'] == 200
    index = json.loads((ROOT / 'index.json').read_text())
    assert index['contains_solutions'] is False
    assert [row['id'] for row in index['examples']] == [row['id'] for row in records]
    assert all('result' not in row and 'hypotheses' not in row for row in index['examples'])
    links_checked = 0
    for path in ROOT.rglob('*.md'):
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text()):
            if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', target) or target.startswith('#'):
                continue
            target = unquote(target.split('#')[0]).strip('<>')
            if target:
                resolved = (path.parent / target).resolve()
                # The report written by this very run need not pre-exist.
                if resolved != ROOT / 'checks/collection-check.json':
                    assert resolved.exists(), (path, target)
                links_checked += 1
    for query in [['--topic', 'coarea'], ['--technique', 'multiplicity'],
                  ['--prerequisite', 'dominated'], ['--text', 'concentration']]:
        output = subprocess.check_output(['python3', str(ROOT / 'find_examples.py'), *query], text=True)
        assert 'No matching' not in output, query
        assert '  result:' not in output, query
    identity = json.loads((ROOT / 'checks/check-results.json').read_text())
    # The concrete checker records its own pass/fail scope. Its details remain
    # separate from this structural check and from independent analytic review.
    assert identity['summary']['status'] == 'passed'
    assert identity['summary']['failed_checks'] == 0
    assert identity['summary']['examples'] == len(records)
    for row in records:
        identity_row = identity['examples'][row['id']]
        assert identity_row['status'] in ('passed', 'proof_only_no_computational_claim')
        for source in identity_row['source_files']:
            assert hashlib.sha256((ROOT / source['path']).read_bytes()).hexdigest() == source['sha256']
    assert hashlib.sha256((ROOT / identity['script']['path']).read_bytes()).hexdigest() == identity['script']['sha256']
    outputs = {}
    for name in ('pdf/guide.pdf', 'pdf/guide.tex', 'pdf/integral-examples.pdf',
                 'pdf/integral-examples.tex'):
        path = ROOT / name
        assert path.is_file() and path.stat().st_size > 1000, name
        outputs[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    pdf_build = json.loads((ROOT / 'checks/pdf-build.json').read_text())
    for build in pdf_build['builds']:
        for name, expected_hash in build['inputs'].items():
            assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected_hash, name
        assert outputs[build['pdf']] == build['pdf_sha256']
        assert outputs[build['latex']] == build['latex_sha256']
    git_root = ROOT.parent
    changed = subprocess.check_output(['git', 'diff', '--name-only',
        'e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f'], cwd=git_root, text=True).splitlines()
    untracked = subprocess.check_output(['git', 'ls-files', '--others',
        '--exclude-standard'], cwd=git_root, text=True).splitlines()
    assert all(name.startswith('integral-examples/') for name in changed + untracked), changed + untracked
    result = {'status': 'passed', 'scope': 'Structure, metadata, exact review hashes, retrieval smoke checks, local links and directory-only changes.',
              'example_count': len(records), 'local_links_checked': links_checked,
              'identity_check_file_loaded': True, 'outputs': outputs}
    (ROOT / 'checks/collection-check.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
