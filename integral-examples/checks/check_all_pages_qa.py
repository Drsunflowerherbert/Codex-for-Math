#!/usr/bin/env python3
"""Validate recorded all-page visual QA coverage and exact PDF identities.

This checks the evidence record. It does not perform visual inspection.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    record = json.loads((ROOT / 'checks/pdf-all-pages-qa.json').read_text())
    total = 0
    for artifact in record['artifacts']:
        path = ROOT / artifact['pdf']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == artifact['pdf_sha256'], path
        pages = artifact['pages']
        assert [row['page'] for row in pages] == list(range(1, artifact['page_count'] + 1)), path
        for row in pages:
            assert row['disposition'] == 'pass', (path, row['page'])
            report = ROOT / row['review_file']
            assert report.is_file(), report
            assert artifact['pdf_sha256'] in report.read_text(), report
            assert len(row['rendered_image_sha256']) == 64, (path, row['page'])
        total += len(pages)
    assert total == record['total_pages_visually_inspected'] == 62
    print(f'PASS: exact PDF identities and recorded visual coverage for all {total} pages.')
    print('This validates recorded evidence; actual visual inspection is documented in the review files.')


if __name__ == '__main__':
    main()
