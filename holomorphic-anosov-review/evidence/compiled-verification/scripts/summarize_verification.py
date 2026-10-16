#!/usr/bin/env python3
"""Summarize terminal evidence; does not run compiler/checker or alter sources."""
from pathlib import Path
import json,datetime,hashlib
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text())
required=['mathlib-cache','solution-build-four-threads','exact-statements-02','exact-definitions-02','selected-targets-replay-02']
steps={n:read('logs/'+n+'.json') for n in required}
assert all('exit_code' in s for s in steps.values()),'Every step must be terminal'
axioms=read('results/compiled-axiom-summary.json');source=read('results/source-and-artifact-manifest.json');export=read('logs/selected-targets-export.json');presence=read('results/export-target-presence.json');comp=read('logs/comparator-attempt.json')
assert all(steps[n]['exit_code']==0 for n in required if n!='selected-targets-replay-02')
assert export['exit_code']==0
replay=steps['selected-targets-replay-02'];replay_log=ROOT/'logs/selected-targets-replay-02.log'
replay_success=replay['exit_code']==0 and 'Lean default kernel accepts the solution' in replay_log.read_text()
assert (replay['exit_code']!=0) or replay_success,'Unexpected checker success output requires investigation'
# The separately recorded presence audit binds success to the completed selected export.
assert export['ndjson_sha256']==presence['export']['sha256'],presence.keys()
assert presence['accepted'] and all(t['exactly_one_present'] for t in presence['targets'])
summary={
 'recorded_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source_repository':'https://github.com/frenzymath/HolomorphicAnosov',
 'source_commit':'65f2b33a7309de661a8500e4642e5609a537a8ff',
 'manuscript':{'version':'arXiv:2609.37695v3, 13 October 2026','pages':19,'bytes':371989,'sha256':'3c8287bf41d153c7f0d0950b8a4b477546229333ee66ba7e9ae60e6a387920c6'},
 'toolchain':{'version':'4.35.0-rc1','commit':'86c6347c75e39ec18c40e25ed2143b71a6e04a0a','official_archive_sha256':'a299763401c3b9b8e19bcca26f8443b40ae24962c3c3ddee73b5c72194877f65','archive_matches_official_release_API_digest':True,'independent_signature_verification':False},
 'solution_build':{'status':'passed','exit_code':0,'local_modules':source['local_solution_closure_modules'],'lake_successful_jobs':13157,'challenge_built':source['challenge_artifact_exists'],'duration_seconds_final_resumed_run':steps['solution-build-four-threads']['duration_seconds'],'dependency_artifacts':'Official pinned Mathlib cache; not all Mathlib recompiled'},
 'compiled_harnesses':{'full_expected_type_assignments':8,'selected_definition_expansions':True,'statement_exit_code':0,'definition_exit_code':0,'source_files_modified':False,'not_recursive_challenge_solution_comparison':True},
 'axiom_lists':{'queried_declarations':len(axioms['declarations']),'all_exactly_standard_three':all(set(x['axioms'])=={'propext','Classical.choice','Quot.sound'} for x in axioms['declarations']),'standard_names':['propext','Classical.choice','Quot.sound'],'axiom_types_recursively_compared_to_challenge':False,'HS_explicit_in':['A','1.1','1.3'],'HS_not_a_premise_of':['1.2'],'HS_discharged':False},
 'official_comparator':{'status':'blocked_before_comparison','exit_code':comp['exit_code'],'reason':'bwrap: setting up uid map: Read-only file system','verdict':None,'sandbox_bypassed':False,'additional_unapproved_executable_installed':False},
 'selected_export':{'exit_code':0,'bytes':export['ndjson_bytes'],'sha256':export['ndjson_sha256'],'all_four_target_theorems_present_once':True,'presence_evidence':'export-target-presence.json','large_NDJSON_published':False},
 'raw_kernel_replay':{'status':'passed' if replay_success else 'incomplete_or_failed','step':'selected-targets-replay-02','exit_code':replay['exit_code'],'duration_seconds':replay['duration_seconds'],'resource_stop':replay['resource_stop'],'log_sha256':hashlib.file_digest(replay_log.open('rb'),'sha256').hexdigest(),'environment':'Fresh environment reconstructed from finalized selected proof export','kernel':'Official default Lean kernel, same implementation as compiler','independent_kernel_implementation':False,'comparator_equivalent':False,'axiom_allowlist_enforced_by_replay':False,'recursive_challenge_comparison':False},
 'preservation':{'all_4232_source_hashes_match_initial_audit':source['all_source_hashes_match_initial_audit'],'tracked_project_sources_unchanged':source['tracked_project_sources_unchanged'],'all_nine_dependency_heads_and_tracked_sources_unchanged':all(x['tracked_sources_unchanged'] for x in source['dependencies']),'root_lockfile_sha256':source['root_manifest_sha256'],'local_olean_files_hashed':source['artifact_files_hashed']},
 'failed_or_discarded_audit_attempts':['Controlled SIGTERM of initial two-thread build to resume same closure with four threads','Initial audit harnesses failed solely on unsupported pp.width; corrected external files passed as -02','Premature raw replay stopped and discarded; only replay-02 counts'],
 'connectivity_recovery':'Existing original build and artifacts confirmed intact after platform disconnect; no duplicate restart',
 'remaining_limits':['No official comparator verdict because host cannot establish runner user namespace','HomotopyTorusRigidity remains explicit premise in A,1.1,1.3','Compiled checks do not prove ordinary mathematical interpretation of definitions','Original Ghys surface-case inference and inaccessible Manning1974 recurrence proof remain source-audit limits','No independent kernel implementation or exhaustive foundational/dependency audit']
}
(ROOT/'results/verification-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:summary[k] for k in ['source_commit','solution_build','raw_kernel_replay','official_comparator']},indent=2))
