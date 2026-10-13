# Independent final verification

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](../PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

The automated verification reviewer recommends publishing this scoped companion under the
limits below. No remaining blocker was found in the tested final production
sources. This reviewer authored only the independent test harnesses, this review,
and structured setup provenance; the reviewer did not edit production code.
Review findings were sent to the implementing agent for correction and retesting.

## Sources and execution

The research baseline was
`b1d6c20e2f02b484d09c5285e67d842b369f9df0`. The published `math-evidence/`
README, runbook, receipt protocol and limitations were read before execution.
Baseline report-writing tests ran in a disposable copy. Original tracked baseline
sources and the original `${PINNED_REPOSITORY}` checkout were preserved.

An isolated installation used the official Lean 4.24.0 archive with SHA-256
`b14f5e5159219dd1a1956c3b806813319f5e94ccd5bdfd56f54520609a5bb5ec`,
compiler commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`, and the baseline's
nine exact package commits, including mathlib
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The baseline selected-member audit
confirmed exact release-archive bytes for the compiler loader and four runtime
libraries. [Setup provenance](../evidence/toolchain-setup.json) records exact
download, checksum, extraction, local linking, source-clone and cache commands,
observed exits, log hashes and the preserved initial cache failure. The failure
was a missing release tag in a shallow ProofWidgets checkout; fetching tag
`v0.0.74` at the same pinned commit resolved it. Lake manifest bytes did not change.
No global installer, profile, credential or account changes were made.

Final executions used a disposable snapshot of the frozen companion. All tested
source bytes matched the corresponding current workspace files after testing.
The fixed source digest remained unchanged throughout the public Lean corpus,
independent receipt tests and runtime tests. Exact commands, observed exits,
source hashes, reported failures and captures are preserved in
[commands](../evidence/commands.json) and the reports below. Reports distinguish
actual execution from imported reported integrity.

## Final results

| Check | Actual result | Meaning |
| --- | --- | --- |
| [Public regression](../evidence/node-regression.json) | 49/49, exit 0 | Actual Node/filesystem/Git checks; no Lean acceptance |
| [Pinned Lean corpus](../evidence/lean-corpus.json) | 10/10, exit 0 | Every fixture reached its intended gate; only `valid` received fresh formal fixture acceptance |
| [Independent v1 receipt mutations](../evidence/independent-v1-receipts.json) | 57/57, exit 0 | Actually executed baseline valid receipt plus malformed mutations and an aged receipt; imports never grant a Lean pass |
| [Independent fixture receipt mutations](../evidence/independent-fixture-receipts.json) | 45/45, exit 0 | Complete current-policy fixture import, malformed mutations and an aged receipt; integrity only |
| [Independent runtime and policy checks](../evidence/independent-runtime.json) | 5/5, exit 0 | Actual observed Lean abort, actual timeout, preabort with no process, unpinned-source preflight rejection and stale-policy rejection |
| [Pinned package source checks](../evidence/pinned-package-sources.json) | 9/9, exit 0; 8,276 tracked entries | Byte identity against unreplaced Git trees; external caches remain trusted |

The fresh corpus separately reports `verifiedBuild`,
`targetCompilationObserved` and formal acceptance. All ten target compilations
had captured products and stable postflight evidence. Nine formally negative
fixtures nevertheless failed the expected whole-type/axiom, independent
definition-body, or same-kernel replay gate. Thus a successful build is not
silently promoted to a proof. The hidden section assumption is present in the
compiled full type; it is rejected by the type gate rather than by a compilation
error. Predicate substitution and transitive bound substitution both pass named
type checks and fail the separately specified body checks. The debugging
kernel-bypass fixture compiles and passes type/axiom checks but fails replay.

The positive fixture retains the premise `h : n = 2` in its identity theorem and
the premise `h : predicate` in its conditional theorem. The predicate body is
checked against `False`; `False → False` does not prove `False`.

Fresh baseline valid, general and tangent receipts also passed the final stricter
v1 inspector solely as reported integrity. The tangent closure contained 208
artifacts. Relocated and coherently aged receipts explicitly returned
`leanPass:false`, `locallyObservedLeanPass:false`,
`freshness:not_established` and no historical-event authentication.

## Baseline reproduction and corrected findings

[Baseline verification](../evidence/baseline-verification.json) records ten
documented ordinary commands, all exit 0: 89 public-source hashes; 157 inherited
checks (78 synthetic, 60 acceptance, 11 mock CLI and eight mock materializer);
69 actual filesystem adversarial checks; 29 ZIP adversarial checks; 16 packaging
checks; eight actual process checks; and four interruption checks. Source
validation and pinned bundle acceptance preserved 37 records, 26 selected files
and zero imported Lean passes. These ordinary suites do not provide Lean
acceptance.

Actual baseline live reproduction separately passed the 31-case mixed live and
receipt adversarial suite and three real running-Lean OS signal cases. The fresh
tangent run completed 70 phases, 37 target checks, four definition-body checks
and 59 local declaration replay entries. `PiDiophantine` remained an explicit
unproved premise.

Independent execution identified an inspector compatibility error in relative
versus absolute compile argv, a hidden-assumption fixture that initially failed
before the intended type gate, two legitimate apostrophe filenames in mathlib,
and a tracked Markdown symlink in Batteries. The implementing agent corrected
these and the final tests above verified the intended behavior. The Git checker
compares that documentation symlink's target bytes without following it. Earlier
failed attempts are retained as superseded evidence rather than counted as
successes. Separate adversarial review also reproduced FIFO blocking and Git
replacement-ref substitution; the final regression suite rejects both.

## Trust and deferred obligations

Independent review and execution are not an independent Lean kernel. Compilation
and local replay use the same official Lean implementation. Standalone fixtures
use trusted imported core OLeans and do not use mathlib; baseline tangent evidence
uses trusted external cached mathlib/dependency OLeans. Dependency sources were
checked bytewise but not rebuilt into those caches. Git object integrity and the
host runtime/filesystem remain trusted.

Receipt hashes establish byte consistency and binding to reviewed source policy,
not authentic historical execution, freshness, novelty or mathematical truth by
themselves. A completely coherent fabricated imported closure can still yield
reported integrity only. Arbitrary executable Lean imports, general polymorphic
targets, hostile-workspace isolation, independent kernel checking and cache
source rebuild remain outside this bounded work. Native Mac and installed MRS
integration are unvalidated and were not modified or claimed.

The final README and migration notes accurately preserve these distinctions.
New code has no newly assigned license; reused baseline material retains its
disclosed provenance. Publication requires the publication task's scoped privacy,
license, source-manifest and remote-commit checks; this reviewer made no push.
