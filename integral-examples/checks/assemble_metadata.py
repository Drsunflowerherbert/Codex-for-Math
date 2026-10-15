#!/usr/bin/env python3
"""Assemble normalized retrieval metadata, requiring independent review hashes."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW_GROUPS = {
    'review-E01-E04.md': ['E01', 'E02', 'E03', 'E04'],
    'review-E07-E10.md': ['E07', 'E08', 'E09', 'E10'],
    'review-E11-E13.md': ['E11', 'E12', 'E13'],
    'review-E05-E06-E14-E16.md': ['E05', 'E06', 'E14', 'E15', 'E16'],
}


def main():
    records = []
    for path in sorted((ROOT / 'reviews').glob('author-*-metadata.json')):
        records.extend(json.loads(path.read_text()))
    records.sort(key=lambda item: item['id'])
    expected = [f'E{n:02}' for n in range(1, 17)]
    if [item['id'] for item in records] != expected:
        raise SystemExit('Expected exactly one author record for each of E01–E16.')
    manifest = {}
    for record in records:
        if isinstance(record['hypotheses'], str):
            record['hypotheses'] = [record['hypotheses']]
        for field in ('topics', 'prerequisites', 'techniques'):
            record[field] = list(dict.fromkeys(record[field]))
        record['measure_normalization'] = (
            'L^n is complete Lebesgue measure; H^0 is counting measure; '
            'H^k uses omega_k/2^k times diameter^k and agrees with L^k on k-planes.')
        source = ROOT / record['file']
        sha = hashlib.sha256(source.read_bytes()).hexdigest()
        review_name = next(name for name, ids in REVIEW_GROUPS.items()
                           if record['id'] in ids)
        review = ROOT / 'reviews' / review_name
        if sha not in review.read_text():
            raise SystemExit(f'{record["id"]}: exact source hash absent from independent review.')
        record['verification'] = {
            'status': 'independently-reviewed',
            'review_file': f'reviews/{review_name}',
            'reviewed_sha256': sha,
            'identity_checks': 'checks/check-results.json',
            'formal_verification': 'none',
        }
        manifest[record['id']] = {
            'file': record['file'], 'sha256': sha,
            'independent_review': record['verification']['review_file'],
        }
    payload = {
        '$schema': './metadata.schema.json',
        'schema_version': '1.0',
        'collection': 'Concrete Lebesgue and Hausdorff Integral Applications',
        'language': 'en', 'created': '2026-10-15',
        'verification_note': 'Independent model review and concrete identity checks; no Lean or human peer review claimed.',
        'examples': records,
    }
    (ROOT / 'metadata.json').write_text(json.dumps(payload, indent=2, ensure_ascii=False) + '\n')
    index_fields = ('id', 'title', 'file', 'topics', 'prerequisites', 'techniques')
    index = {
        'schema_version': '1.0',
        'contains_solutions': False,
        'path_base': 'integral-examples/',
        'examples': [{key: row[key] for key in index_fields} for row in records],
    }
    (ROOT / 'index.json').write_text(json.dumps(index, indent=2, ensure_ascii=False) + '\n')
    (ROOT / 'reviews' / 'review-manifest.json').write_text(
        json.dumps({'scope': 'Exact independently reviewed Markdown sources.',
                    'examples': manifest}, indent=2) + '\n')
    # The problem-first index links to each separate solution, without its result.
    problem_index = ROOT / 'PROBLEMS.md'
    text = problem_index.read_text()
    for record in records:
        text = text.replace(f'| {record["id"]} |',
                            f'| [{record["id"]}]({record["file"]}) |')
    problem_index.write_text(text)
    print(f'Assembled {len(records)} reviewed examples and spoiler-light index.')


if __name__ == '__main__':
    main()
