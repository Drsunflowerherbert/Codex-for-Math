#!/usr/bin/env python3
"""Regenerate spoiler-free views from the bounded collector catalogs."""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / 'catalogs'
SUBJECTS = ('analysis', 'algebra', 'geometry', 'topology', 'probability', 'combinatorics')
AUTHORED = {
    'yau-2014-written-individual-p1': 'reviewed ordinary proof; independent review accepted',
    'yau-2019-written-individual-p1': 'reviewed ordinary proof; independent review accepted',
    'yau-2023-written-main-p4': 'reviewed ordinary proof; independent review accepted',
}

def read(name):
    return json.loads((CAT / name).read_text())

def records():
    result = []
    yau = read('yau-analysis.json')
    papers = {p['paper_id']: p for p in yau['papers']}
    for p in yau['problems']:
        paper = papers[p['paper_id']]
        result.append(dict(
            id=p['problem_id'], contest='Yau', year=p['year'], stage=p['stage'],
            category=p['category'], original_number=p['number'],
            topic=p['title_editorial'], subjects=p['classification_editorial'],
            prerequisites=p['prerequisites_editorial'], difficulty=p['difficulty_editorial'],
            question_url=paper['official_index_url'], archive_member=paper['archive_member'],
            source_page=p['pdf_page_1_based'], language=paper['language'],
            source_access=paper['source_access_status'], source_sha256=paper['sha256'],
            statement_fidelity=p['original_conditions_status'],
            official_solution_availability=p['official_solution_availability'],
            official_solution_access=p['official_solution_access_status'],
            authored_solution_status=AUTHORED.get(p['problem_id'], 'not attempted in this edition'),
            source_issue= p.get('source_issue_id', ''),
        ))
    schw = read('schweitzer.json')
    docs = {d['url']: d for d in schw['source_documents']}
    for p in schw['problems']:
        d = docs[p['statement_url']]
        result.append(dict(
            id=p['problem_id'], contest='Schweitzer', year=p['year'], stage='archived competition',
            category='', original_number=str(p['number']), topic=p['editorial_topic'],
            subjects=p['subjects'], prerequisites=p['prerequisites'], difficulty=p['difficulty_estimate'],
            question_url=schw['archive_url'] if p['source_contains_solutions'] else p['statement_url'],
            archive_member='', source_page=p['statement_page'], language=d['language'],
            source_access=d['access_status'], source_sha256=d['sha256'],
            statement_fidelity=p['exact_statement_status'],
            official_solution_availability=p['official_solution_availability'],
            official_solution_access=p['solution_access_status'],
            authored_solution_status=p['authored_solution_status'],
            source_issue=p['errata_status'] if 'wording' in p['errata_status'] else '',
        ))
    for name in ('jarnik.json', 'imc.json'):
        d = read(name)
        for p in d['problems']:
            result.append(dict(
                id=p['id'], contest='Jarnik' if name == 'jarnik.json' else 'IMC',
                year=p['year'], stage=('Category II' if name == 'jarnik.json' else 'day '+str(p['day'])),
                category=p.get('category', ''), original_number=p['original_number'],
                topic=p['topic'], subjects=p['subjects'], prerequisites=p['prerequisites'],
                difficulty=p['difficulty'], question_url=p['source_url'], archive_member='',
                source_page=p['source_page'], language=p['language'],
                source_access=p.get('source_accessstatus', 'downloaded original question PDF'),
                source_sha256=p.get('source_sha256') or '', statement_fidelity=p['statement_fidelity'],
                official_solution_availability=p['official_solution_availability'],
                official_solution_access=p['official_solution_accessstatus'],
                authored_solution_status=p['authored_solution_status'], source_issue='',
            ))
    order = {'Yau': 0, 'Schweitzer': 1, 'Jarnik': 2, 'IMC': 3}
    return sorted(result, key=lambda p: (order[p['contest']], p['year'], p['stage'], p['category'], int(p['original_number'])))

def main():
    rows = records()
    columns = list(rows[0])
    with (ROOT / 'problems.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns, lineterminator='\n')
        writer.writeheader()
        for p in rows:
            writer.writerow({k: '; '.join(v) if isinstance(v, list) else v for k, v in p.items()})
    counts = Counter(p['contest'] for p in rows)
    subject_counts = Counter(s for p in rows for s in p['subjects'])
    manifest = dict(
        edition_date='2026-10-13', scope='bounded first edition, archive practice through 2025',
        detailed_problem_entries=len(rows), detailed_by_contest=dict(counts),
        fully_retrieved_source_problem_entries=sum(p['contest'] != 'Jarnik' for p in rows),
        indexed_source_only_provisional_entries=counts['Jarnik'],
        subject_memberships=dict(subject_counts), subject_membership_note='Multiple labels are allowed; totals overlap.',
        detailed_problem_ids=[p['id'] for p in rows],
        original_authored_attempt_count=len(AUTHORED), authored_status=AUTHORED,
        current_round_problem_content_included=False, third_party_papers_mirrored=False,
        limitations=[
            'Yau non-Analysis written members and oral Analysis members are inventory only.',
            'Schweitzer detailed topics before 2022 are not indexed; 2012 statements/solutions not located.',
            'Schweitzer2023 answer paper is explicitly unofficial, although organizer-hosted.',
            'Jarnik full archive/PDF retrieval returned HTTP503; detailed entries are provisional indexed-source metadata.',
            'IMC1994–2022 individual problems are not indexed; headers/links are inventoried.',
            'Official solution correctness is not reviewed; not-located search status never means nonexistent.',
        ],
        source_catalogs=['catalogs/yau-analysis.json', 'catalogs/yau-source-manifest.json', 'catalogs/schweitzer.json', 'catalogs/jarnik.json', 'catalogs/imc.json'],
    )
    (ROOT / 'coverage.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n')
    lines = ['# Subject navigation', '',
             'These are spoiler-free editorial subject memberships. Multi-subject entries',
             'appear in more than one section; counts overlap. Exact conditions remain in',
             'the linked original paper. Yau links open the archive landing page; select',
             'the recorded question member in its separate contest catalog.', '',
             'Jarník entries are provisional because direct PDF access is blocked.', '',
             '| Subject | Detailed memberships |', '| --- | --- |']
    lines += [f'| [{s}](#{s}) | {subject_counts[s]} |' for s in SUBJECTS]
    for subject in SUBJECTS:
        lines += ['', '## '+subject, '', '| ID / original number | Editorial topic | Preparation | Difficulty | Official questions |', '| --- | --- | --- | --- | --- |']
        for p in rows:
            if subject not in p['subjects']:
                continue
            topic=p['topic'].replace('|','\\|')
            prep='; '.join(p['prerequisites']).replace('|','\\|')
            lines.append(f"| `{p['id']}` / {p['original_number']} | {topic} | {prep} | {p['difficulty']} | [Source]({p['question_url']}) |")
    (ROOT / 'SUBJECTS.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'detailed_problem_entries': len(rows), 'by_contest': dict(counts), 'subject_memberships': dict(subject_counts)}, indent=2))

if __name__ == '__main__':
    main()
