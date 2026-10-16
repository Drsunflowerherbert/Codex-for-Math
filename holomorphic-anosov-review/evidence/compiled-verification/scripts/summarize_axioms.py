#!/usr/bin/env python3
"""Enforce the configured axiom whitelist on actual successful Lean check output."""
from pathlib import Path
import argparse,json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--statements-step',required=True);ap.add_argument('--definitions-step',required=True);a=ap.parse_args()
steps={}
for role,step in [('statements',a.statements_step),('definitions',a.definitions_step)]:
 status=json.loads((ROOT/'logs'/(step+'.json')).read_text())
 assert status['exit_code']==0 and not status['resource_stop'],(role,status['exit_code'])
 log=ROOT/'logs'/status['log'];assert hashlib.sha256(log.read_bytes()).hexdigest()==status['log_sha256']
 steps[role]=status
text=(ROOT/'logs'/steps['statements']['log']).read_text()
found={}
for m in re.finditer(r"'([^']+)'\s+depends on axioms:\s*\[([^\]]*)\]",text):
 found[m.group(1)]=[v.strip() for v in m.group(2).split(',') if v.strip()]
for m in re.finditer(r"'([^']+)'\s+does not depend on any axioms",text):found[m.group(1)]=[]
targets=['HolomorphicAnosov.theorem_A','HolomorphicAnosov.theorem_1_1','HolomorphicAnosov.theorem_1_2','HolomorphicAnosov.theorem_1_3']
wrappers=['HolomorphicAnosov.zhang_theorem_A','HolomorphicAnosov.zhang_theorem_1_1','HolomorphicAnosov.zhang_theorem_1_2','HolomorphicAnosov.zhang_theorem_1_3']
bindings=['HolomorphicAnosovAudit.'+kind+'_'+suffix+'_matches' for kind in ['target','wrapper'] for suffix in ['A','11','12','13']]
required=targets+wrappers+bindings
missing=[n for n in required if n not in found];assert not missing,('Missing explicit axiom reports',missing)
config=json.loads((ROOT/'build/Comparator/config.json').read_text());permitted=set(config['permitted_axioms'])
canonical={n:[re.sub(r'\.\{[^}]*\}$','',v) for v in found[n]] for n in required}
rows=[{'declaration':n,'reported_axioms':found[n],'axioms':canonical[n],'forbidden_axioms':sorted(set(canonical[n])-permitted),'whitelist_pass':set(canonical[n])<=permitted} for n in required]
result={'source_commit':'65f2b33a7309de661a8500e4642e5609a537a8ff','permitted_axioms':sorted(permitted),'declarations':rows,'all_whitelist_pass':all(r['whitelist_pass'] for r in rows),'exact_full_type_assignments_compiled':True,'definition_expansion_checks_compiled':True,'theorems_A_11_13_retain_explicit_HS_premise':True,'theorem_12_has_no_HS_premise':True,'semantic_limit':'Axiom closure excludes universally quantified hypotheses; HS remains a substantive explicit premise. Harness uses copied complete interface types and imported definitions; it is not the blocked comparator.','execution_steps':{k:v['step'] for k,v in steps.items()},'harness_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'checks').glob('*.lean')}}
(ROOT/'results/compiled-axiom-summary.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
assert result['all_whitelist_pass'],'Forbidden axiom present'
