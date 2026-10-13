#!/usr/bin/env python3
"""Check catalog packaging and calibration; never certify mathematical proofs."""
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'research-map'
load = lambda name: json.loads((OUT / name).read_text())
data = load('catalog.json')
inventory = load('upstream-inventory.json')
audit = load('source-audit.json')
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


try:
    import jsonschema
except ImportError:
    checks.append('jsonschema unavailable; required field and invariant checks run below')
else:
    jsonschema.Draft202012Validator(load('schema.json')).validate(data)
    checks.append('Draft2020-12 JSON schema')

families = data['families']
rows = data['manuscripts']
check('exact baseline', data['research_baseline_commit'] == 'e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f')
check('current upstream provenance', data['upstream_source_commit'] == audit['official_upstream']['remote_head'] == inventory['metadata']['revision'])
check('distinct family IDs', len({f['family_id'] for f in families}) == len(families) == 372)
check('exact taxonomy coverage', {f['family_id'] for f in load('taxonomy.json')['families']} == {f['family_id'] for f in families})
check('17 fields', len({f['field'] for f in families}) == 17)
check('unique records and source paths', len({r['record_id'] for r in rows}) == len({r['source_path'] for r in rows}) == len(rows) == 722)
check('active and withdrawal counts', Counter(r['catalog_status'] for r in rows) == {'active': 719, 'withdrawn': 3})
check('all withdrawals retained in family032', {r['family_id'] for r in rows if r['catalog_status'] == 'withdrawn'} == {'032'})
check('no solved labels granted', data['coverage']['famous_problem_solved_labels_awarded'] == 0)
check('no imported fresh upstream checks', all(r['formal_check_this_round'] == 'not_run' and r['established_acceptance'] == 'not_established' for r in rows))
check('hypothesis gaps explicit', all(r['hypotheses'] is None and r['hypotheses_status'] == 'not_exhaustively_extracted' for r in rows))
check('metadata audit count honest', data['coverage']['active_manuscripts_metadata_only'] == 719)
check('source equivalence receipts', all(r['byte_identical_to_historical_revision'] and r['saved_snapshot_matches_raw_plus_one_newline'] for r in audit['fresh_source_receipts']))
baseline = json.loads((ROOT / 'research/starter/catalog/inventory.json').read_text())
check('metadata path/abstract membership preservation',
      [(f['id'],m['path'],m['abstract']) for f in inventory['families'] for m in f['manuscripts']] ==
      [(f['id'],m['path'],m['abstract']) for f in baseline['families'] for m in f['manuscripts']])
for field, expected in inventory['discipline_counts'].items():
    check('counts for '+field, sum(f['field']==field for f in families)==expected['families'] and sum(r['field']==field and r['catalog_status']=='active' for r in rows)==expected['manuscripts'])
for row in rows:
    check('pinned sources '+row['record_id'], all(re.match(r'^https://github\.com/openai/math/(blob|tree)/[0-9a-f]{40}/', url) for url in row['source_urls']))
    check('family membership '+row['record_id'], any(f['family_id']==row['family_id'] and f['field']==row['field'] and f['subfield']==row['subfield'] for f in families))
history = load('version-history.json')
check('all27 version links preserved', len(history['changed_directory_versions']) == 27)
check('revision kinds13plus14', Counter(r['change_kind'] for r in history['changed_directory_versions']) == {'citation-only':13,'proof_statement_hypothesis_or_citation_correction':14})
with (OUT/'catalog.csv').open(newline='') as file:
    csv_rows = list(csv.DictReader(file))
check('CSV records match JSON', [r['record_id'] for r in csv_rows] == [r['record_id'] for r in rows])
html = (OUT/'index.html').read_text()
embedded = json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>', html, re.S).group(1))
check('HTML data matches catalog', embedded['manuscripts'] == rows and embedded['coverage'] == data['coverage'])
check('HTML has no thirdparty executable includes', not re.search(r'<script[^>]*\bsrc\s*=',html,re.I))
check('safe HTML dynamic text', 'innerHTML' not in html and 'textContent' in html and 'replaceChildren' in html)
check('supplemental coverage units', data['coverage']['targeted_major_claim_entries']==len(data['claim_scope_audits']) and data['coverage']['local_scoped_result_entries']==len(data['scoped_results']))
check('major claim overlays present', len(data['claim_scope_audits']) >= 15)
check('scoped result overlays present', len(data['scoped_results']) >= 10)
for file in OUT.glob('*'):
    if file.is_file():
        text = file.read_text()
        check('secret-pattern scan '+file.name, not re.search(r'(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{50,}|sk-proj-[A-Za-z0-9_-]{30,}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----)', text))
result = {'purpose':'catalog structural/source/security consistency; not mathematical or Lean verification',
          'checks_passed':len(checks),'checks':checks,
          'coverage':data['coverage'],
          'artifact_sha256':{name:hashlib.sha256((OUT/name).read_bytes()).hexdigest() for name in ['catalog.json','catalog.csv','FIELD-MAP.md','index.html','major-claims.json','scoped-results.json','taxonomy.json','source-audit.json']}}
(OUT/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks_passed':len(checks),'coverage':data['coverage']},indent=2))
