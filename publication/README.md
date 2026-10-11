# Publication record

This publication is based on exact commit
`d00a89dd9ce6c8ef782234d28c93e69cb712c947`, on branch
`codex/research-2026-10-11`. The original tangent files are unchanged.

[INPUT-ARCHIVES.json](INPUT-ARCHIVES.json) records supplied archive
fingerprints. All listed archives were retrieved and their SHA256 values verified
in this publication environment before extraction. Entry paths and file types
were inspected first; no traversal entries or symlinks were present. No archive
script was executed automatically.

[SOURCE-MAP.json](SOURCE-MAP.json) records each candidate's source hash and its
publication disposition for retained project inputs. The separate toolkit source
map covers every toolkit candidate. Exclusion records give filenames and reasons
without private contents. Modified files have original and published hashes.
[FILES.json](FILES.json) now binds the whole published repository, including
the original tangent tree, finite-field and guide additions, and positive-block
library and evidence toolkit. It excludes itself to avoid self-reference. Run
`python3 publication/verify.py` for exact file-set, byte/hash, provenance, pin
and explicit historical-status checks. It also works on extracted snapshots
with `--root <snapshot-directory>`. Dependencies and build caches are excluded.
Integrity checks establish byte consistency, not mathematical truth.

Historical supplied manifests, review hashes, commands, verdicts, and build
receipts describe the original supplied snapshots. They have not been rewritten
to make privacy edits appear independently reviewed. Their hashes can reference
omitted or sanitized files. Root archive manifests are explicitly named
`*.supplied.*`; nested historical records retain stable names and are subject
to this same interpretation. Use the publication manifest for the current tree.
No review verdict is upgraded by a new hash.

Radial v2's supplied successful receipt is preserved under
`radial-contact/evidence/supplied-v2/`; its current `evidence/validation.json`
records a separate publication build. Egyptian supplied receipts remain under
`egyptian-exact/evidence/`; fresh publication commands and logs are under
[evidence/](evidence/). Source and dependency pins remain byte-identical.

The Lean implementations' starter-input failures are historical provenance
limits. Both independently implemented supplied mathematical specifications.
Later successful archive retrieval does not retroactively certify that the
formalizers inspected the starter or that every ordinary record is equivalent
to a formal theorem.

The public set excludes launch instructions, private identifiers and transfer
metadata, cache/download diagnostics, the nested binary checkpoint, and the
original private packaging helper. No credentials, personal emails, screenshots,
account details, installed dependencies, or build binaries were found in the
retained publication set. Independent automated publication/privacy and
mathematical-status reviews inspected all initial candidates; their scope and
the final review are recorded in [REVIEW.md](REVIEW.md).

No overall license has been invented for the new research or Lean implementations.
Retained third-party text is separately attributed and accompanied by the
upstream license; see [THIRD-PARTY.md](../THIRD-PARTY.md).

## Finite-field library and techniques guide addition

The completed finite-field project and reviewed learning guide were added after
the initial publication. [FINITE-FIELD-GUIDE-FILES.json](FINITE-FIELD-GUIDE-FILES.json)
binds the historical `af92d20` batch; [FINITE-FIELD-GUIDE-SOURCE-MAP.json](FINITE-FIELD-GUIDE-SOURCE-MAP.json)
records retained, documentation-edited and omitted inputs. The nine library Lean
files and two Lean check files are byte-identical to the completed source archive.
The guide retains its reviewed 03:32 UTC text and has a separate dated status addendum.

Publication-only checks verified original archive fingerprints, all retained
source/evidence hashes, the 85-declaration name inventory, and the public file
allowlist. They did not rerun Lean or archived test programs. Supplied build and
axiom receipts describe the completed source snapshot and may refer to original
artifacts omitted from this privacy-reviewed minimal public set. Neither new
hashes nor the upload itself constitute another mathematical verification.

The earlier upload left the integrity command's directory scope unchanged.
This finalization expands it to every published root and includes the unchanged
original tangent tree. The batch manifest/source map remain unchanged historical
records; current bytes use `FILES.json`. File integrity grants no new Lean pass.

## Positive-block finalization

The supplied checkpoint contained compiled proofs and successful audits, but
its final written source verdict was unfinished. A separate independent
[finished review](../positive-blocks/reviews/final-source-review.md) now accepts
the requested core scope without a proof correction or unresolved gap. Fresh
project-source compilation, a separate compilation of all ten local modules,
142 type/axiom checks and exact examples passed; see
[POSITIVE-BLOCK-CHECKS.json](evidence/POSITIVE-BLOCK-CHECKS.json).

Proof sources and dependency pins are unchanged. Private handoff notes,
internal packaging helpers and a generic new-work license template are excluded
with their dispositions recorded. Historical command/path edits and their
original hashes stay separate from the new review and new compiler receipts.
The guide's original text and initial addendum remain unchanged; its
[later update](../learning-guide/STATUS-FINALIZATION-2026-10-11.md) records this
finished scope. No overall license or novelty claim has been added.

## Math evidence toolkit

The source-only [toolkit](../math-evidence/README.md) retains 86 reviewed original
source/doc/test candidates. All 5,833 input files have dispositions in
[TOOLKIT-SOURCE-MAP.json](TOOLKIT-SOURCE-MAP.json); archives, binaries, cached
inputs and raw receipt trees are excluded. New public manifests and derivative
reports are separately bound by the current whole-repository file manifest.

All 73 preserved inputs and 32 live-gate/fixture files are byte-identical. Seven
metadata/smoke/test-path adaptations and six documentation rewrites are recorded
by original and public hashes. Fresh public tests passed 283 cases across six
suites. Two source archives are byte-identical; their inspected extracted package
passed eight fixed consumer commands including a fresh valid Lean fixture and
integrity-only inspection returning no imported pass.

See [TOOLKIT-PACKAGE-CHECKS.json](evidence/TOOLKIT-PACKAGE-CHECKS.json) for actual
package/consumer evidence and the [historical summary](../math-evidence/verification/HISTORICAL-EVIDENCE.json)
for the earlier full tangent gate. Historical 32 ZIP checks differ from the 29
self-contained public cases. Trusted pinned dependency OLeans, host runtime,
same-kernel replay, monomorphic full gates, the unproved PiDiophantine premise
and unvalidated native Mac/MRS integration remain explicit limits.

## Convex approximation core

The [nine-module project](../convex-approximation/README.md) has accepted independent
source review and fresh project-source compilation, declaration/axiom checks and
portable reproduction. See [CONVEX-APPROX-CHECKS.json](evidence/CONVEX-APPROX-CHECKS.json),
[CONVEX-PORTABLE-CHECKS.json](evidence/CONVEX-PORTABLE-CHECKS.json) and their
[raw public logs](evidence/convex-approximation/). The supplied audit contains 145
inventoried declarations; the separate Plane abbreviation audit completes coverage
of 146 explicitly named declarations: 124 theorem/lemma statements, 20 definitions,
one structure and one abbreviation. Generated structure declarations are not
separately counted. Type printing has ordinary proof-argument pretty-printer
elisions; original source statements and independent statement review remain
inspectable. There is no programmed expected-type-equality gate for this project.

The compiled scope includes the exact quantitative outer estimate, actual barrier
derivatives, inner tube, coercivity, compact strictly convex sublevels, nonzero
level derivatives and an actual certified compactly nested approximation sequence,
including singleton/lower-dimensional examples. Analytic boundary charts and
sphere/Jordan parametrizations remain deferred. The source manuscript is broader.

All 132 original archive candidates have dispositions in the source map: 97
retained, including 75 unchanged copies and 22 metadata/path/routing edits; 35
omitted, including duplicate existing-study/source links. All 21 original Lean
source/audit and pin files are unchanged. Nested archives, recovery/draft handoffs,
tangent coordination metadata and the package helper are excluded. Existing
ordinary study and attributed source are linked. The failed first printer audit
remains exit 1; the corrected historical audit remains exit 0. Fresh logs and
reviews do not overwrite either supplied receipt. No overall license is invented.

## Final round status

All completed artifacts actually retrieved for this publication are included,
with final source/privacy/status reviews and separate fresh reproduction records.
The [mixed-moment finalization](PENDING-TRANSFER.json) was reported completed and
independently accepted in its separate task, but final source/evidence transfer
failed before an accessible artifact existed. Its reported fingerprint is not
a publisher-verified archive hash. Final transfer and publication remain pending;
no older checkpoint or ordinary study is promoted into the final proof project.
This round closes with that limitation explicitly preserved.
