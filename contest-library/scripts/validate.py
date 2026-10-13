#!/usr/bin/env python3
"""Check bounded catalog integrity. This is not a mathematical proof checker."""
import argparse
import csv
import hashlib
import json
import re
import zipfile
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

import build_index

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_HOSTS = {'yau-contest.com', 'www.bolyai.hu', 'jarnik.osu.cz', 'vjimc.osu.cz', 'www.imc-math.org.uk'}
SHA = re.compile(r'^[0-9a-f]{64}$')


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check_private_sources(yau_manifest, schw, imc):
    counts = Counter()
    zip_paths = {}
    for a in yau_manifest['archives']:
        path = a['personal_research_copy']
        require(digest(path) == a['sha256'], 'Yau archive byte hash mismatch')
        zip_paths[a['archive_id']] = path
        counts['yau_archives'] += 1
    for archive_id, path in zip_paths.items():
        with zipfile.ZipFile(path) as z:
            for m in yau_manifest['members']:
                if m['archive_id'] != archive_id:
                    continue
                if m.get('sha256'):
                    require('/2026/' not in m['archive_member'], 'Current member must not be read')
                    value = hashlib.sha256(z.read(m['archive_member'])).hexdigest()
                    require(value == m['sha256'], 'Yau past member hash mismatch')
                    counts['yau_past_members'] += 1
                else:
                    # Central-directory metadata only: do not open the excluded member.
                    require('/2026/' in m['archive_member'], 'Unexpected unhashed past member')
                    counts['yau_excluded_name_only_members'] += 1
    for d in schw['source_documents']:
        require(digest(d['local_personal_research_copy']) == d['sha256'], 'Schweitzer PDF byte hash mismatch')
        counts['schweitzer_pdfs'] += 1
    snapshot = schw['archive_snapshot']
    require(digest(snapshot.get('local_personal_research_copy', '/tmp/contest-library-research/schweitzer/hub.html')) == snapshot['sha256'], 'Schweitzer hub byte hash mismatch')
    counts['schweitzer_hubs'] += 1
    for a in imc['archives']:
        require(digest(a['source_index_local_path']) == a['source_index_sha256'], 'IMC index byte hash mismatch')
        counts['imc_index_html'] += 1
        for p in a['papers']:
            if p.get('download'):
                d = p['download']
                require(digest(d['local_path']) == d['sha256'], 'IMC PDF byte hash mismatch')
                counts['imc_pdfs'] += 1
    return dict(counts)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--private-sources', action='store_true', help='Also hash retained personal source copies under /tmp; unavailable to a normal public clone.')
    args = parser.parse_args()
    yau = build_index.read('yau-analysis.json')
    yau_manifest = build_index.read('yau-source-manifest.json')
    schw = build_index.read('schweitzer.json')
    jarnik = build_index.read('jarnik.json')
    imc = build_index.read('imc.json')
    rows = build_index.records()
    require(len(rows) == 236 and len({p['id'] for p in rows}) == 236, 'Detailed count/IDs')
    require(Counter(p['contest'] for p in rows) == {'Yau': 152, 'Schweitzer': 42, 'Jarnik': 12, 'IMC': 30}, 'Contest counts')
    for p in rows:
        require(p['year'] <= 2025, 'Current year problem in detailed index')
        require(p['subjects'] and set(p['subjects']) <= set(build_index.SUBJECTS), 'Subject vocabulary')
        require(p['prerequisites'], 'Missing editorial preparation')
        require(p['difficulty'] in {'entry advanced', 'advanced', 'very advanced', 'unassessed'}, 'Difficulty vocabulary')
        require(urlsplit(p['question_url']).hostname in ALLOWED_HOSTS, 'Non-primary question source')
        require('solution' not in p['question_url'].lower() and 'prob_sol' not in p['question_url'].lower(), 'Spoiler URL in question view')
        require(not p['source_sha256'] or SHA.fullmatch(p['source_sha256']), 'Invalid source hash')
    require(len(yau['papers']) == 26, 'Yau paper count')
    actual_yau_years = Counter(p['year'] for p in yau['problems'])
    expected_yau_years = {**{y: 12 for y in range(2010, 2018)}, 2018: 11, 2019: 10, **{y: 6 for y in range(2020, 2024)}, 2024: 5, 2025: 6}
    require(actual_yau_years == expected_yau_years, 'Yau year coverage')
    for paper in yau['papers']:
        ps = [p for p in yau['problems'] if p['paper_id'] == paper['paper_id']]
        require(len(ps) == paper['problem_count'] == len(paper['covered_problem_numbers']), 'Yau paper numbering/count')
        require({p['number'] for p in ps} == set(paper['covered_problem_numbers']), 'Yau original numbering mismatch')
        require(all(p['pdf_page_1_based'] in paper['analysis_pdf_pages_1_based'] for p in ps), 'Yau section page bounds')
    require(sum('source_issue_id' in p for p in yau['problems']) == 9, 'Final Yau editorial source issue count')
    p2018 = next(p for p in yau['problems'] if p['problem_id'] == 'yau-2018-written-individual-p4')
    require('source_issue_id' not in p2018 and 'closed ball' in p2018['source_notation_clarification'], 'Closed-ball source fidelity')
    require(len(yau['official_solution_papers']) == 3, 'Yau official solution paper inventory')
    require(len(schw['papers']) == 17 and len(schw['problems']) == 42, 'Schweitzer detailed scope')
    require(sum(p['problem_count_observed'] for p in schw['papers']) == 171, 'Schweitzer observed number coverage')
    p2012 = next(p for p in schw['papers'] if p['year'] == 2012)
    require(p2012['problem_count_observed'] == 0 and p2012['problem_count_claimed'] == 11, 'Schweitzer2012 claim/observation separation')
    require(any(e.get('problem_id') == 'schweitzer-2023-p08' for e in schw['errata']), 'Missing source-qualified2023P8 warning')
    require(len(jarnik['archives']) == 32 and len(jarnik['category_ii_problem_link_years']) == 26 and len(jarnik['category_ii_solution_link_years']) == 16, 'Jarnik inventory')
    require(jarnik['downloaded_original_pdf_count'] == 0, 'Jarnik must not claim PDF retrieval')
    require(all(p['source_sha256'] is None for p in jarnik['problems']), 'Jarnik must not invent source PDF hashes')
    require(len(imc['archives']) == 32 and imc['downloaded_original_pdf_count'] == 12, 'IMC inventory')
    coverage = json.loads((ROOT / 'coverage.json').read_text())
    require(coverage['detailed_problem_ids'] == [p['id'] for p in rows], 'Stale coverage view')
    with (ROOT / 'problems.csv').open(newline='') as f:
        csv_rows = list(csv.DictReader(f))
    require([p['id'] for p in csv_rows] == [p['id'] for p in rows], 'Stale CSV view')
    registry = json.loads((ROOT / 'authored-solutions.json').read_text())
    require(len(registry['solutions']) == 3, 'Original attempt batch exceeds bounded scope')
    for p in registry['solutions']:
        require(p['author_agent'] != p['reviewer_agent'], 'Review is not independent')
        require(p['status'] == 'reviewed ordinary proof; accepted', 'Unaccepted proof eligible for publication')
        proof = ROOT / p['solution_path']
        hint = ROOT / p['hints_path']
        review = ROOT / p['review_path']
        require(digest(proof) == p['solution_sha256'], 'Accepted solution hash changed')
        require(digest(hint) == p['hints_sha256'], 'Accepted hint hash changed')
        require(digest(review) == p['review_sha256'], 'Review record hash changed')
        review_text = review.read_text()
        require(p['solution_sha256'] in review_text and p['hints_sha256'] in review_text, 'Final version absent from independent review')
        require('pending' not in proof.read_text().lower(), 'Pending review in published solution')
    prohibited = {'.pdf', '.zip', '.doc', '.docx', '.tex', '.png', '.jpg', '.jpeg'}
    for path in ROOT.rglob('*'):
        if not path.is_file() or '__pycache__' in path.parts:
            continue
        require(not path.is_symlink(), 'Unexpected symlink')
        require(path.suffix.lower() not in prohibited, 'Third-party body/media present in public collection')
        text = path.read_text()
        require(not re.search(r'sk-[A-Za-z0-9_-]{20,}', text), 'Potential credential found')
        require(('source_' + 'thread_id') not in text, 'Private delegation identity found')
        if path.suffix == '.md':
            for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
                if target.startswith(('https://', 'http://', '#')):
                    continue
                target = target.split('#')[0]
                if target:
                    require((path.parent / target).resolve().exists(), f'Broken local link: {path.relative_to(ROOT)} -> {target}')
    for name in ('PROBLEMS.md', 'PRACTICE.md', 'SUBJECTS.md', 'catalogs/yau-analysis.md', 'catalogs/schweitzer.md', 'catalogs/jarnik.md', 'catalogs/imc.md'):
        text = (ROOT / name).read_text()
        require('## Proof' not in text and '## Hint 1' not in text and '**Verdict:**' not in text, 'Proof/hint content in default view')
    sums = ROOT / 'SHA256SUMS'
    if sums.exists():
        for line in sums.read_text().splitlines():
            sha, name = line.split('  ', 1)
            require(digest(ROOT / name) == sha, 'Published byte inventory mismatch: '+name)
    result = {'status': 'passed', 'detailed_entries': 236, 'retrieved_source_entries': 224, 'provisional_entries': 12, 'accepted_original_proofs': 3, 'mathematical_truth_automatically_checked': False}
    if args.private_sources:
        result['private_source_hash_checks'] = check_private_sources(yau_manifest, schw, imc)
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
