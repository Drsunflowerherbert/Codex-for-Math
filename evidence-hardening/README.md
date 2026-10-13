# Evidence hardening companion

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

A self-contained Node companion to `math-evidence/` at research commit
`b1d6c20e2f02b484d09c5285e67d842b369f9df0`. It leaves that package unchanged.
No npm/Python dependency is added. Tested host: Linux, Node 24.19.0,
Python 3.12.14, official Lean 4.24.0 at
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`.

The independent [adversarial audit](reviews/adversarial-audit.md) identified
contradictory saved process evidence and Git index flags that hide changed source.
During review, FIFO blocking and Git replacement-ref substitution were also
reproduced and fixed. [Migration notes](MIGRATION.md) describe the stricter gate.
[Verification](VERIFICATION.md) records actual commands, counts and limits.

## What each command establishes

| Command | Successful result | Remaining boundary |
| --- | --- | --- |
| `inspect-v1.cjs RUN` | A complete v1 reported receipt matches fixed baseline sources, command descriptions, artifacts and log envelopes | No authentic historical event, freshness or Lean pass |
| `git-source.cjs PACKAGE EXACT_COMMIT` | Working tracked bytes match the unreplaced Git tree, despite index flags | Caller supplies the commit; origin, external caches and arbitrary import completeness are separate |
| `fixture-gate.cjs run LABEL LEAN NEW_RUN` | Fresh execution of a fixed reviewed fixture, including complete types, permitted axioms, independent expected definition bodies and local replay | Fixed monomorphic scope, trusted core OLeans, same Lean kernel |
| `fixture-gate.cjs inspect RUN` | A reported successful fixture receipt matches the current fixture policy and preserved evidence | Always `leanPass:false`, no new live observation or freshness |

`verifiedBuild` on a fresh fixture result requires successful target compilation,
error-free JSON logs, captured products and unchanged source/compiler/evidence.
`locallyObservedLeanPass` additionally requires the type, axiom, definition and
replay gates. Negative fixtures can have a verified build and fail formal
acceptance. Compilation never silently discharges a hypothesis.

## Reproduce

Run from this directory. Output parents must already exist; attempts and reports
use fresh paths and never resume an older success.

```sh
node tests/regression.cjs ${TEMP_ARTIFACT}
node inspect-v1.cjs /absolute/preserved-successful-v1-run
node git-source.cjs /absolute/package f897ebcf72cd16f89ab4577d0c826cd14afaafc7
node tests/lean-corpus.cjs /absolute/official-lean-4.24.0/bin/lean ${TEMP_DIR} ${TEMP_ARTIFACT}
node fixture-gate.cjs run valid /absolute/official-lean-4.24.0/bin/lean ${TEMP_ARTIFACT}
node fixture-gate.cjs inspect ${TEMP_ARTIFACT}
```

For the source check, use the actual package's independently reviewed full commit;
the example commit is mathlib's baseline pin. `baseline.json` preserves all nine
Lake pins. The checker hashes Git blob content directly, disables replacement
objects, reads every tracked regular file, and rejects untracked Lean imports or
products outside the explicit cache directories. Tracked Markdown symlinks are
compared as link-target bytes without following them. Other symlinks/submodules,
unsupported paths and oversized trees fail closed. Git object integrity and the
host filesystem are trusted. This command does not run Lean or receipt argv.

The fixture runner verifies five selected official release members before and
after execution. The independently verified installation archive SHA-256 is
`b14f5e5159219dd1a1956c3b806813319f5e94ccd5bdfd56f54520609a5bb5ec`.
It uses fresh local OLeans and excludes old project products. It neither installs
tooling nor downloads a cache. Read fixed fixture source before running it;
the negative `skip-kernel` fixture deliberately exercises Lean's debugging bypass.

## Corpus and proof scope

The positive fixture proves elementary arithmetic, a full implicit-binder
identity, and `False → False`; it also checks two definition bodies. The identity
retains `h : n = 2`. The conditional theorem retains `h : predicate` and the
predicate body is checked against `False`; no proof of `False` is asserted.

| Negative fixture | Intended rejection |
| --- | --- |
| `hidden-assumption` | The actual closed type contains an extra section hypothesis |
| `statement-drift` | The implicit-binder equality changes from 2 to 3 |
| `specialization` | The reference specializes a general declaration |
| `wrong-name` | The compiled namespace differs from the reviewed target |
| `definition-substitution` | Named type matching succeeds; independent predicate body fails |
| `transitive-drift` | An imported bound changes; the independent answer body fails |
| `sorry`, `custom-axiom` | Unapproved axiom closure |
| `skip-kernel` | Compilation/type/axiom checks pass; same-kernel replay rejects |

All local fixture dependencies, helpers, reference types/bodies and executing modules
are committed in `fixture-policy.json`. A source mutation under the unchanged
policy fails before an attempt starts. Inspection rejects stale policy digests.
An intentional change to policy is a new reviewed source version, never evidence
that an old receipt happened again. Repository commits bind the policy bytes;
unsigned hashes alone do not authenticate authorship or process history.

Core dependency OLeans remain trusted. The fixtures do not use mathlib. Actual
baseline tangent verification separately used the pinned mathlib cache and kept
its unproved `PiDiophantine` premise. No dependency source rebuild, independent
kernel, hostile Lean sandbox, native Mac/MRS integration or novel mathematical
theorem is claimed. Negative `sorry`, axiom and kernel-bypass files are regression
inputs only. Do not treat their compilation as a proof.

New code has no newly assigned license. Reused baseline files and modifications
are listed in [provenance](PROVENANCE.json); no dependency sources/binaries or
private original archives are redistributed.
