# Compiled verification evidence: distribution record

These are normalized public copies of audit-owned scripts/harnesses, notes,
execution metadata, artifact/source hash manifests, and complete text logs.
Original execution records remain private. `publication-manifest.json` records
each original-file SHA-256 and each published-copy SHA-256, prefix replacement
counts, and the terminal replay status. It makes no new mathematical claim.

`$VERIFY_ROOT`, `$SOURCE_AUDIT`, `$REVIEW_ROOT`, and `$WORKSPACE_ROOT` replace
private absolute paths. Status metadata labels raw log hashes `original_*` and
adds `published_normalized_*` hashes for the copies actually distributed here.
The original and normalized hashes can coincide if no log bytes changed.
System executable paths and public source URLs/commit hashes are retained.

No toolchain, build tree, dependency checkout, cache, downloaded archive,
generated proof export, source PDF/OCR/full article, private identifier or key
is included. The omitted 2,385,351,648-byte proof export is identified by SHA-256
`2864d2b33f4020c69b5093af94e365da0866c5add9a3d580ef16421a2ab17276`.
Artifact/source manifests contain hashes and relative names, not those sources.
The audit harnesses reproduce complete expected interfaces and selected
definition checks; they contain no upstream proof bodies. Their print logs
are diagnostic output, not copies of the upstream repository.

Historical provenance/harness-author statements that a particular inspection
subtask did not run Lean describe that subtask. Actual execution and its limits
are recorded in `deliverables/verification-method.md` and the status/log files.
`kernel-replay-plan.md` is a preparatory plan; actual commands/status take
precedence. Legacy standalone comparator/Landrun metadata mentioned by the
provenance research note is deliberately omitted from this distribution.

Failed, stopped and discarded attempts are retained with their explanations.
The configured comparator remains blocked by its required Bubblewrap UID-map
setup, independently of the direct replay outcome. A same-kernel raw replay
does not replace comparator comparison/allowlisting or discharge the explicit
`HomotopyTorusRigidity` premise of Theorems A, 1.1 and 1.3.

For reruns, use a fresh workspace containing only `scripts/` and `checks/`,
then follow `deliverables/verification-method.md`. The scripts derive their
verification root from `Path(__file__)`. Do not run over saved evidence or
reinterpret normalized status records as original raw logs.
