#!/usr/bin/env python3
"""Rebuild the first-edition map from pinned, attributed metadata and audit overlays.

No upstream proof code is executed. No mathematical status is inferred from titles.
"""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'research-map'
BASELINE = 'e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f'
LOCAL = f'https://github.com/Drsunflowerherbert/Codex-for-Math/blob/{BASELINE}/'


def read(name, default=None):
    p = OUT / name
    return json.loads(p.read_text()) if p.exists() else default


def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def first_sentence(text):
    # This is a visibly attributed metadata excerpt, never a reconstructed theorem.
    return text[:700] + (' [metadata excerpt truncated]' if len(text) > 700 else '')


def entries(value):
    if isinstance(value, list):
        return value
    return value.get('entries', value.get('results', [])) if value else []


inventory = read('upstream-inventory.json')
if inventory is None:
    inventory = json.loads((ROOT / 'research/starter/catalog/inventory.json').read_text())
revision = inventory['metadata']['revision']
tax = read('taxonomy.json', {})
tax_entries = tax if isinstance(tax, list) else tax.get('families', tax.get('entries', tax.get('mapping', {})))
if isinstance(tax_entries, list):
    tax_map = {str(x.get('family_id', x.get('id'))).zfill(3): x for x in tax_entries}
else:
    tax_map = tax_entries
claim_document = read('major-claims.json', {})
claims = entries(claim_document)
scoped_document = read('scoped-results.json', {})
scoped = entries(scoped_document)
changes = json.loads((ROOT / 'research/starter/catalog/revision_changes.json').read_text())
families = []
records = []

for family in inventory['families']:
    fid = family['id']
    assignment = tax_map.get(fid, {})
    if isinstance(assignment, str):
        assignment = {'subfield': assignment}
    subfield = assignment.get('subfield', 'Unassigned within field')
    families.append({
        'family_id': fid, 'field': family['discipline'], 'subfield': subfield,
        'taxonomy_basis': assignment.get('taxonomy_basis', 'unassigned'),
        'problem_family_title': family['title'],
        'author_family_summary': first_sentence(family.get('summary', '')),
        'source_url': family['source_url'], 'lean_scope_url': family.get('lean_scope_url'),
        'active_manuscript_count': len(family['manuscripts']),
        'distinct_problem_count': None,
        'warning': 'An upstream family groups manuscripts; it does not certify one distinct solved problem.'})
    for m in family['manuscripts']:
        path = m['path']
        gaps = ['Exact theorem statement and complete hypotheses not independently extracted for this catalog.',
                'No upstream Lean compilation, axiom audit or informal-to-formal correspondence check performed in this round.',
                'Independent mathematical validation and established acceptance not established by the inspected metadata.']
        if fid == '134':
            gaps.append('Source metadata conflict: family title says star height at most three; manuscript abstract says at most thirteen. Resolve against precise theorem before use.')
        if fid == '342':
            gaps.append('The upstream formalization manifest names the September23 Taming PDF, while the active manuscript is the corrected October6 version. Do not transfer verification across versions without correspondence review.')
        records.append({
            'record_id': 'manuscript-' + hashlib.sha256(path.encode()).hexdigest()[:16],
            'record_type': 'upstream_manuscript', 'family_id': fid,
            'field': family['discipline'], 'subfield': subfield,
            'problem_family_title': family['title'], 'manuscript_title': m['title'],
            'source_path': path, 'source_commit': revision,
            'statement_summary': first_sentence(m.get('abstract', '')),
            'statement_basis': 'attributed_author_abstract_metadata; not a checked theorem',
            'hypotheses': None, 'hypotheses_status': 'not_exhaustively_extracted',
            'result_kind': 'unassessed', 'result_kind_basis': None,
            'catalog_status': 'active', 'reliability_tier': 'R0_author_metadata_only',
            'evidence_review': 'metadata_only',
            'evidence_types': ['author_catalog_metadata'] + (['upstream_manifest_listing'] if m.get('formalization_source_listed') else []),
            'formalization_source_listed': bool(m.get('formalization_source_listed')),
            'formal_check_this_round': 'not_run',
            'independent_mathematical_validation': 'not_established',
            'established_acceptance': 'not_established',
            'informal_formal_correspondence': 'not_reviewed',
            'source_urls': [m['pdf_url'], m['readme_url'], family['source_url']],
            'lean_scope_url': family.get('lean_scope_url'),
            'version': {'date_label': m.get('directory_version_date'),
                        'prior_release_path': m.get('prior_release_path'),
                        'changed_since_initial': bool(m.get('manuscript_directory_changed_since_initial')),
                        'change_kind': m.get('change_kind'), 'version_note': m.get('version_note'),
                        'relation': 'upstream_catalog_version_link; not independently inferred result identity'},
            'withdrawal': None, 'verification_gaps': gaps,
            'dependencies': [], 'prerequisites': [],
            'learning_priority': 'L3_scope_review_before_reuse',
            'claim_index_refs': [str(c.get('claim_id', c.get('id', c.get('family_id')))) for c in claims if c.get('family_id') == fid],
            'scoped_library_refs': [str(s.get('result_id', s.get('id', s.get('title')))) for s in scoped if s.get('family_id', s.get('upstream_family_id')) == fid]})

for m in inventory['withdrawn']:
    f = next(x for x in families if x['family_id'] == m['family_id'])
    records.append({
        'record_id': 'manuscript-' + hashlib.sha256(m['path'].encode()).hexdigest()[:16],
        'record_type': 'upstream_manuscript', 'family_id': m['family_id'],
        'field': f['field'], 'subfield': f['subfield'], 'problem_family_title': f['problem_family_title'],
        'manuscript_title': m['title'], 'source_path': m['path'],
        'source_commit': inventory['metadata']['initial_revision'],
        'statement_summary': first_sentence(m.get('abstract', '')),
        'statement_basis': 'historical_author_abstract; withdrawn proof',
        'hypotheses': None, 'hypotheses_status': 'not_exhaustively_extracted',
        'result_kind': 'unassessed', 'result_kind_basis': None,
        'catalog_status': 'withdrawn', 'reliability_tier': 'RX_withdrawn_proof',
        'evidence_review': 'withdrawal_notice_review', 'evidence_types': ['author_withdrawal_notice'],
        'formalization_source_listed': False, 'formal_check_this_round': 'not_run',
        'independent_mathematical_validation': 'withdrawn_proof_not_supported',
        'established_acceptance': 'not_established', 'informal_formal_correspondence': 'not_reviewed',
        'source_urls': [m['archived_pdf_url'], m['current_notice_url']], 'lean_scope_url': None,
        'version': {'relation': 'historical_withdrawn_manuscript'},
        'withdrawal': {k: v for k, v in m.items() if k in ['withdrawn_notice_date','history_section_date','public_merge_utc','statement_truth_status']},
        'verification_gaps': ['The stabilization-trace sign error undermines the withdrawn proof; withdrawal does not disprove the statement.',
                              'Surviving family032 manuscripts require their own dependency review.'],
        'dependencies': [], 'prerequisites': [], 'learning_priority': 'L0_audit_dependency_risk',
        'claim_index_refs': [str(c.get('claim_id', c.get('id', c.get('family_id')))) for c in claims if c.get('family_id') == '032'],
        'scoped_library_refs': []})

coverage = {
    'fields': len(inventory['discipline_counts']), 'families': len(families),
    'active_manuscripts': sum(r['catalog_status'] == 'active' for r in records),
    'withdrawn_manuscripts': sum(r['catalog_status'] == 'withdrawn' for r in records),
    'catalog_records': len(records),
    'active_manuscripts_metadata_only': sum(r['catalog_status'] == 'active' and r['evidence_review'] == 'metadata_only' for r in records),
    'withdrawal_notices_reviewed': sum(r['evidence_review'] == 'withdrawal_notice_review' for r in records),
    'targeted_major_claim_entries': len(claims),
    'major_claim_entries_statement_or_scope_reviewed': claim_document.get('coverage', {}).get('claim_statement_or_scope_inspected_entries', 0),
    'major_claim_entries_catalog_only': claim_document.get('coverage', {}).get('catalog_only_entries', len(claims)),
    'major_claim_distinct_families': len(set(c['family_id'] for c in claims)),
    'local_scoped_result_entries': len(scoped),
    'local_scoped_groups_independent_spot_reviewed': scoped_document.get('coverage', {}).get('independent_catalog_spot_review_groups', 0),
    'local_scoped_groups_without_new_independent_spot_review': scoped_document.get('coverage', {}).get('groups_without_new_independent_spot_review', len(scoped)),
    'upstream_manuscripts_independently_mathematically_validated_this_round': 0,
    'upstream_formal_checks_this_round': 0,
    'famous_problem_solved_labels_awarded': 0,
    'version_directory_changes_recorded': len(changes['changed_directory_versions']),
    'version_changes_by_kind': dict(Counter(x['change_kind'] for x in changes['changed_directory_versions'])),
    'subfield_assignments': sum(f['subfield'] != 'Unassigned within field' for f in families),
    'count_units_note': 'Claim entries, scoped results, manuscripts, families and Lean declarations are distinct units; no deduplicated count of solved mathematical problems is available.'}
write('version-history.json', {
    'historical_source_commit': changes['metadata']['revision'],
    'latest_semantically_identical_source_commit': revision,
    'initial_source_commit': changes['metadata']['initial_revision'],
    'changed_directory_versions': changes['changed_directory_versions'],
    'withdrawn': inventory['withdrawn'],
    'warning': 'These are documented author revision histories, not exhaustive issues or proof validation.'})
write('coverage.json', coverage)
catalog = {'schema_version': '1.0.0',
           'edition': '2026-10-13 first edition; metadata-complete, mathematical-review partial',
           'research_baseline_commit': BASELINE, 'upstream_source_commit': revision,
           'historical_inventory_source': LOCAL + 'research/starter/catalog/inventory.json',
           'coverage': coverage, 'families': families, 'manuscripts': records,
           'claim_scope_audits': claims, 'scoped_results': scoped}
write('catalog.json', catalog)
columns = ['record_id','field','subfield','family_id','problem_family_title','manuscript_title','catalog_status','result_kind','reliability_tier','evidence_review','source_commit','source_path','statement_summary','hypotheses_status','formalization_source_listed','formal_check_this_round','independent_mathematical_validation','established_acceptance','informal_formal_correspondence','learning_priority','source_urls','version','verification_gaps','claim_index_refs','scoped_library_refs']
with (OUT / 'catalog.csv').open('w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns, lineterminator='\n')
    writer.writeheader()
    for row in records:
        writer.writerow({k: json.dumps(row[k], ensure_ascii=False) if isinstance(row[k], (dict,list)) else row[k] for k in columns})

lines = ['# Field and problem-family map — 13 October 2026', '',
         'This is a navigation map of author claims, versions and bounded study results. No famous problem receives a solved label in this edition. Read [the rubric](SCHEMA.md), [major claims](MAJOR-CLAIMS.md), [scoped results](SCOPED-RESULTS.md), and [source audit](SOURCES.md) before interpreting a title as a theorem.', '',
         f"Coverage: {coverage['active_manuscripts']} active manuscripts and {coverage['withdrawn_manuscripts']} withdrawn manuscripts in {len(families)} families across {coverage['fields']} fields. All active manuscript rows remain metadata-only. The separate {len(claims)} major-claim entries comprise {coverage['major_claim_entries_statement_or_scope_reviewed']} statement/scope/notice reviews and {coverage['major_claim_entries_catalog_only']} catalog-only entries; {len(scoped)} local scoped-result entries receive additional treatment. These counts do not measure solved problems.", '',
         '| Field | Families | Active manuscripts |', '|---|---:|---:|']
for field, count in inventory['discipline_counts'].items():
    lines.append(f"| {field} | {count['families']} | {count['manuscripts']} |")
for field in inventory['discipline_counts']:
    lines += ['', '## ' + field, '']
    subsets = sorted(set(f['subfield'] for f in families if f['field'] == field))
    for sub in subsets:
        lines += ['### ' + sub, '']
        for f in [x for x in families if x['field'] == field and x['subfield'] == sub]:
            fid = f['family_id']
            lines += [f"#### Family {fid}: {f['problem_family_title']}", '',
                      f"{f['active_manuscript_count']} active manuscript(s). Classification is provisional author-metadata inference. [Author catalog]({f['source_url']})."]
            if f['lean_scope_url']:
                lines[-1] += f" [Listed formalization scope]({f['lean_scope_url']}); no check performed here."
            if any(c.get('family_id') == fid for c in claims):
                lines += ['See the [targeted major-claim scope audit](MAJOR-CLAIMS.md).']
            if any(s.get('family_id', s.get('upstream_family_id')) == fid for s in scoped):
                lines += ['See the [separate scoped reusable results](SCOPED-RESULTS.md).']
            for row in [r for r in records if r['family_id'] == fid]:
                url = row['source_urls'][0]
                flag = 'WITHDRAWN — proof unsupported' if row['catalog_status'] == 'withdrawn' else 'author claim; pending statement/correspondence review'
                change = row['version'].get('change_kind')
                lines += [f"- [{row['manuscript_title']}]({url}) — {flag}" + (f'; version history: {change}' if change else '')]
            if fid == '134':
                lines += ['Metadata conflict: title says at most three, abstract says at most thirteen. Inspect the theorem before using a bound.']
            lines += ['']
(OUT / 'FIELD-MAP.md').write_text('\n'.join(lines).rstrip() + '\n')

payload = json.dumps({'coverage':coverage,'manuscripts':records}, ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
html = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Math research map · 13 October 2026</title><style>
body{font:16px system-ui,sans-serif;margin:0;color:#182b3b;background:#f4f6f8;overflow-wrap:anywhere}main{max-width:1200px;margin:auto;padding:30px}h1{font-size:32px}p{max-width:1000px;line-height:1.6}nav a{margin-right:20px;color:#164e8c}section{background:white;padding:20px;margin-top:20px;border:1px solid #d9e1e8;border-radius:12px}.controls{display:flex;gap:12px;flex-wrap:wrap}input,select,button{font:inherit;padding:10px;border:1px solid #8ca1b2;border-radius:6px}input{flex:1;min-width:240px}select{max-width:100%}article{border-top:1px solid #d9e1e8;padding:16px 0}h2{font-size:18px;margin:8px 0}.badge{font-size:13px;color:#735212}small{display:block;margin-top:8px;color:#476074}a{color:#164e8c}.summary{font-size:14px}button{cursor:pointer;margin-right:10px}details{margin-top:12px}summary{cursor:pointer}@media(max-width:600px){main{padding:18px}.controls>*{width:100%;min-width:0;box-sizing:border-box}nav a{display:inline-block;margin-bottom:8px}}
</style><main><h1>Math research map</h1><p>First edition · 13 October 2026. A source-pinned catalog of manuscripts and problem families, with a partial evidence audit. <strong>No famous problem is labelled solved here.</strong> Author claims, formal statements, kernel checks, independent validation and acceptance are separate evidence questions.</p><nav><a href="README.md">Guide</a><a href="FIELD-MAP.md">Field map</a><a href="MAJOR-CLAIMS.md">Major claims</a><a href="SCOPED-RESULTS.md">Reusable scoped results</a><a href="SCHEMA.md">Status rubric</a><a href="catalog.json">JSON</a><a href="catalog.csv">CSV</a></nav><section><p id="coverage"></p><label for="search">Search manuscript titles, family titles, summaries, or evidence gaps</label><div class="controls"><input id="search" type="search" placeholder="e.g. Hodge, Catalan, family 017"><select id="field" aria-label="Field"><option value="">All fields</option></select><select id="subfield" aria-label="Subfield"><option value="">All subfields</option></select><select id="status" aria-label="Status"><option value="">All statuses</option><option>active</option><option>withdrawn</option></select></div><p id="count" role="status"></p><button id="prev">Previous</button><button id="next">Next</button><div id="rows"></div></section></main><script id="data" type="application/json">''' + payload + r'''</script><script>
'use strict';const data=JSON.parse(document.getElementById('data').textContent),all=data.manuscripts,by=id=>document.getElementById(id);let page=0;const size=50;by('coverage').textContent=`${data.coverage.active_manuscripts} active manuscripts + ${data.coverage.withdrawn_manuscripts} withdrawn, ${data.coverage.families} families, ${data.coverage.fields} fields. ${data.coverage.targeted_major_claim_entries} targeted claim entries; ${data.coverage.local_scoped_result_entries} separate local scoped results. All active rows are metadata-only; zero upstream proofs newly checked.`;for(const id of ['field','subfield'])for(const val of [...new Set(all.map(r=>r[id]))].sort()){const op=document.createElement('option');op.value=val;op.textContent=val;by(id).append(op)}const searchable=all.map(r=>({r,t:JSON.stringify(r).toLowerCase()}));function element(tag,text,parent){const e=document.createElement(tag);e.textContent=text;parent.append(e);return e}function link(text,url,parent){if(!/^https:\/\/github\.com\//.test(url))return;const a=element('a',text,parent);a.href=url;a.rel='noopener noreferrer';a.target='_blank';parent.append(document.createTextNode(' · '))}function render(){const raw=by('search').value.toLowerCase();const fq=/^family\s+(\d{1,3})$/.exec(raw);const q=fq?'':raw;const rs=searchable.filter(({r,t})=>(!fq||r.family_id===fq[1].padStart(3,'0'))&&(!q||t.includes(q))&&(!by('field').value||r.field===by('field').value)&&(!by('subfield').value||r.subfield===by('subfield').value)&&(!by('status').value||r.catalog_status===by('status').value)).map(x=>x.r);page=Math.min(page,Math.max(0,Math.ceil(rs.length/size)-1));by('count').textContent=`${rs.length} matching manuscripts · page ${page+1} of ${Math.max(1,Math.ceil(rs.length/size))}`;by('prev').disabled=page===0;by('next').disabled=(page+1)*size>=rs.length;by('rows').replaceChildren();for(const r of rs.slice(page*size,(page+1)*size)){const a=element('article','',by('rows'));element('small',`${r.field} → ${r.subfield} → family ${r.family_id}`,a);element('h2',r.manuscript_title,a);element('div',`${r.catalog_status.toUpperCase()} · ${r.reliability_tier} · ${r.evidence_review}`,a).className='badge';element('p',r.statement_summary||'No abstract metadata.',a).className='summary';element('small','Attributed author metadata; complete hypotheses and theorem correspondence remain unreviewed.',a);const d=element('details','',a);element('summary','Evidence gaps and version history',d);element('p',r.verification_gaps.join(' '),d);element('p',JSON.stringify(r.version),d);const p=element('p','',a);r.source_urls.forEach((url,i)=>link(i===0?'Manuscript':'Source '+(i+1),url,p));if(r.lean_scope_url)link('Listed Lean scope',r.lean_scope_url,p)}}for(const id of ['search','field','subfield','status'])by(id).addEventListener(id==='search'?'input':'change',()=>{page=0;render()});by('prev').onclick=()=>{page--;render()};by('next').onclick=()=>{page++;render()};render();
</script></html>'''
(OUT / 'index.html').write_text(html)
print(json.dumps(coverage, indent=2))
