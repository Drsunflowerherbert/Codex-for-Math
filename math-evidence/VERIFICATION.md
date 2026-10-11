# Verification evidence and limitations

`verification/HISTORICAL-EVIDENCE.json` is a derivative summary of inspected
original evidence. It records original source/report hashes and preserves the
original 69 Node/filesystem, 32 ZIP, 31 live and eight extracted-consumer counts.
Raw receipt trees, input copies and compiled outputs were omitted; the derivative
is not a complete live receipt and grants no new Lean pass.

`verification/PUBLIC-VERIFICATION.json` records actual commands run on the cleaned
public source set, current source hashes, observed exits and exact tested counts.
Public ZIP tests contain 29 self-contained cases. The three original archive cases
are optional and are not silently counted. Mock tests remain labeled as mocks.
The adapted extracted smoke verifies public-source hashes and a fresh valid live
run; its eight-command workflow differs from the archived smoke.

`PUBLIC-SOURCES.json` binds the published source/doc/test set and excludes itself
and verification summaries. `verify-public-sources.cjs` verifies these byte hashes.
The repository-wide publication manifest binds every published file, including
this manifest and the derived reports. Hashes establish byte consistency and no
historical event authentication. A source manifest is not a mathematical verifier.

The production live gate, helper, fixed plans and expected harnesses are preserved
byte-for-byte. Private platform identities were removed only from archive/corpus
provenance metadata; smoke and adversarial paths were adapted for publication.
The source map records both original and public hashes. Historical implementation
approval hashes do not imply that changed files were tested as their original bytes.

Trust limits remain: clean pinned dependency OLeans and host runtime; same-kernel
local replay against imported dependencies; monomorphic full type/body targets;
explicit unproved `PiDiophantine`; no full dependency source rebuild, independent
kernel, native Mac, installed MRS, novelty or hostile-workspace sandbox claim.
Optional corpus imports grant zero Lean passes and preserve native statuses.
No license is invented for new toolkit code or third-party evidence.
