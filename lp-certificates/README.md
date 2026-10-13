# Rational LP certificate toolkit

This directory provides an exact rational certificate checker, a checked
JSON-to-Lean export path, and Lean soundness proofs for linear programming over
the reals. It keeps the original variables, supports mixed inequality directions
and unrestricted equality multipliers, and adds no slack or artificial decision
variables. A small deterministic finder is explicitly incomplete. No completeness,
strong-duality, or proved parser-refinement theorem is claimed.

## Checked original-input exports

The follow-up represents original rational coefficients, row directions/order,
and objective sense in `InputProblem`. Normalization is computed and proved
sound inside Lean, including the original minimization ordering. The bridge emits
only fixed syntax and canonical integer/fraction literals, then requires actual
kernel acceptance and original-real soundness for every exported certificate.

```sh
python3 bridge.py check examples/optimal_mixed_redundant.json \
  examples/infeasible_mixed.json examples/unbounded_min_lower_dimensional.json \
  --output /tmp/checked-lp-new --lean-bin /absolute/lean-4.24.0-linux/bin
python3 bridge.py recheck /tmp/checked-lp-new \
  --output /tmp/rechecked-lp-new --lean-bin /absolute/lean-4.24.0-linux/bin
```

Each attempt rebuilds the task's Lean modules in a private cache. The package
binds exact input bytes, canonical rational values, generated problem/witness
source, expected statements, compiler/dependency identities, and outputs by
hashes. Recheck regenerates from strict original JSON and executes current
trusted numeric templates; it does not execute supplied Lean or saved commands.
Saved receipts remain historical evidence. The [checked-bridge notes](notes/checked-bridge.md)
describe supported Linux setup, bounded resources, malformed/tampered-input
checks, failure states, and the remaining parser/literal-fidelity boundary.

The [small exact finder](notes/incomplete-finder.md) can produce witnesses for
hand-sized examples. `found` requires exact Python verification; `unknown`
means the bounded search found no witness. A found witness can be passed through
the checked bridge for per-instance Lean acceptance.

## Use the checker

Python 3.12 and its standard library suffice:

```sh
cd lp-certificates
python3 verifier.py examples/optimal_mixed_redundant.json
python3 verifier.py examples/infeasible_mixed.json
python3 verifier.py examples/unbounded_min_lower_dimensional.json
python3 -m unittest discover -s tests -v
```

The first example certifies maximum `10`. The second combines `x<=0` and
`x>=1` to obtain `0<=-1`. The third certifies unbounded minimization along
`(1,0)+t(1,1)`. The [interface](notes/certificate-interface.md) gives the strict
JSON format, exact rational representations, normalized multiplier order, and
exit codes. The [mathematical notes](notes/mathematics.md) explain hand
calculation, equality conditions, complementary slackness, normalization,
scaling, and degenerate, redundant, and lower-dimensional cases.

## Lean claims and dependency pins

`LPCertificates/Core.lean` proves the weighted-constraint bound, weak duality,
optimality and infeasibility soundness, feasible improving rays and unboundedness,
the exact duality-gap identity, and complementary slackness. These theorems
require no rank, vertex, strict feasibility, or bounded-polyhedron hypothesis.

`LPCertificates/Rational.lean` supplies executable Boolean acceptance tests and
three theorems: `checkOptimal_sound_real`, `checkInfeasible_sound_real`, and
`checkUnbounded_sound_real`. Rational acceptance implies the claimed result
for **all real feasible points**. `Examples.lean` includes accepted and rejected
small examples proved using `decide +kernel`; no native evaluation oracle is
used. Its alternate weights on a redundant row illustrate nonunique
certificates.

- Lean: official `leanprover/lean4:v4.24.0`, compiler commit
  `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`.
- mathlib: official repository revision
  `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.
- All nine dependency revisions are locked in `lake-manifest.json`.

With that compiler on `PATH` and the pinned dependency caches available:

```sh
lake build
```

The saved cloud environment used the existing pinned compiler and linked the
existing clean dependency cache into this new project's `.lake/packages`.
No dependency source, binary, cache, or compiled product is published here.

## Fresh verification and independent review

The verification runner preserves each attempt in a newly created directory,
checks actual compiler and dependency identities, forces fresh project
compilation, audits all named definitions/theorems, then runs independent
whole-type and definition-body gates and same-kernel local replay using the
published `math-evidence/lean/EvidenceHarness.lean` unchanged. Its expected
real statements are spelled out as raw finite sums by the independent reviewer.

```sh
python3 scripts/verify.py --output /tmp/lp-verification-new \
  --lean-bin /absolute/lean-4.24.0-linux/bin \
  --cached-repository /absolute/Codex-for-Math
```

`--cached-repository` is optional and enables the published toolkit's pinned
release-member byte audit against the original saved Lean archive. The runner
also confirms that Lake selected the compiler actually audited. Without that
archive the receipt explicitly records that byte comparison was not performed.
The sibling published `math-evidence/` directory is required for these gates.
The runner clears only this project's generated `.lake/build` directory.

Independent reports are in `evidence/math-review.md`,
`evidence/computational-review.md`, and `evidence/formal-review.md`.
The [fresh first-checkpoint receipt](evidence/run-20261013T015800Z/receipt.json) records all
nine commands exiting `0`: 53 Python tests, fresh Lean compilation, 64 named
declaration audits, five body gates, three complete expected-type gates, and
same-kernel replay of 111 local declarations. Independent raw-row arithmetic
agrees on 72,900 bounded test documents. The fixtures include nine acceptances,
six mathematical rejections, and two malformed inputs. Stored logs document an
observed run; they do not perform a new Lean check when read.

That receipt belongs to the preserved first checkpoint commit `44329696`.
Its original hash bindings are unchanged; subsequent edits require the separate
follow-up receipts and reviews. The follow-up also fixes the reported very-large
integer formatting crash with explicit input/output budgets and fail-closed
formatting, and corrects the interface note: weighted slack products are not
emitted as separate output fields.

The [follow-up summary](evidence/followup-summary.md) records a fresh 143-test
suite with two explicit optional skips, 78 audited declarations, fourteen body
gates, and six complete type gates. Separate actual Lean runs passed for ten
author inputs, thirteen independently checked inputs, and a fresh relocated
one-input recheck. All nine accepted fixtures were exported and kernel checked;
a finder-produced witness was also checked. The complete portable packages,
exact commands/results, and unchanged-byte hashes are included in `evidence/`.

## Hypotheses, trust boundaries, and deferred obligations

Variables are free reals and all bounds are explicit rows. Inputs and witnesses
are rational; inequalities are nonstrict. There are no added mathematical
axioms or admitted proofs. The ordinary foundational Lean axioms are disclosed
in the declaration audit. Cached dependency oleans and the host runtime remain
trusted. Replay uses the same Lean kernel; it is not an independent kernel
implementation. The external Python/JSON parser and literal generator have no
formal refinement theorem to the typed Lean model. Original-row normalization
is proved in the typed mixed-input layer; per-exported-input kernel rechecking
is required by the checked bridge.

Complete certificate discovery, algorithmic termination/completeness, converses to the
certificate implications, strong duality, an extracted verified parser, integer
variables, strict constraints, and tolerance-based numerical certificates are
deferred. Rejection of a supplied certificate does not prove anything about
the problem's status. No unique optimal normalization is asserted. Primary
references and retrieval limits are in [sources](notes/sources.md).

This is Linux cloud evidence. Native Mac and installed MRS integration are not
claimed. The toolkit's fixed tangent plans are not presented as LP acceptance.

## Provenance and publication scope

Research baseline: `b1d6c20e2f02b484d09c5285e67d842b369f9df0` on the existing
`codex/research-2026-10-11` branch. Assigned new branch:
`codex/lp-certificates-2026-10-13`. This task publishes only `lp-certificates/`;
the original tangent checkout, shared publication manifests, and research branch
are unchanged. See `PROVENANCE.json` and `evidence/publication-review.md` for
observed scope, privacy/license inspection, and verification evidence.

`FOLLOWUP-PROVENANCE.json` and `evidence/followup-summary.md` describe the new
reviewed bridge, finder and fixes. The first checkpoint's evidence and manifest
retain their original meaning and hashes. The new scoped follow-up manifest
binds the later publication; no shared repository manifest is edited.

The proof code, checker, examples, notes, and runner are newly written for this
task; the evidence helper is referenced from the already published repository.
No third-party book/PDF text, dependency code, credentials, or private source
archive is included. The repository reports no overall license, and this task
assigns no new license. Existing third-party notices remain unchanged.
