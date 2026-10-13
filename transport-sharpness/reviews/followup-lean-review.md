# Independent actual-measure follow-up review

This is a new review following the published checkpoint
`40589436a45ddfd2cc8df8897e86b3185b83a107`. The earlier finite/scalar review,
manual harness, replay file, driver and evidence remain preserved. The new
review owns `FollowupReviewHarness.lean`, `FollowupReplay.lean` and the separate
driver under `evidence/followup-lean-review/`.

**Final verification status:** two independently executed fresh Lean runs,
ordinary and Python `-O`, passed whole-type/body/axiom checking and local kernel
replay. Source inspection remains distinct from these observed checker
executions. No formal statement or assumption defect was identified.

## Independent semantic audit

The inspected `Measures.lean` extension imports the retained scalar core and
uses `Point = R x R` with its ordinary product Borel measurable space. Its
`atomicMeasure a b` is an actual sum of three weighted Dirac measures at the
existing locations `(-1,0)`, `(0,b)`, and `(1,0)`. Its coefficients are
`ENNReal.ofReal ((1-a)/2)`, `ENNReal.ofReal a`, and
`ENNReal.ofReal ((1-a)/2)`. The measure at `b=0` is the first target and the
measure at general `b` is the second target.
For `0<a<1` all three coefficients are strictly positive. The probability
theorems deliberately also allow `a=0` and `a=1`, where some coefficients
vanish; those boundary cases are not three-positive-atom examples.

`IsMeasureCoupling a b gamma` states exactly the two marginal identities:
`Measure.map Prod.fst gamma = atomicMeasure a 0` and
`Measure.map Prod.snd gamma = atomicMeasure a b`. It quantifies over arbitrary
`Measure (Point x Point)` values. It does not require the coupling to be a
finite matrix or assume any cost bound. The matching witness is a separate
actual Borel measure, obtained by putting each atom weight at the pair of its
unshifted and shifted locations. Both of its marginal identities are proved.

`euclideanSquared` is the explicit sum
`(x1-y1)^2 + (x2-y2)^2`, and `measurePCost p` is `ENNReal.ofReal` of that sum
raised to `p/2`. `measureCost` is its nonnegative Lebesgue integral. The product
type's default maximum norm is not used as the Euclidean transport cost.

`transportPowerInf a b p` is the actual infimum over all Borel measures with
the two actual marginal identities, not an infimum over finite arrays. The
second infimum binder ranges over proofs of the marginal predicate; an
inadmissible measure contributes the empty infimum, `top`. The matching
coupling proves that the domain is nonempty, so no empty-domain convention
produces the claimed finite value.

The all-coupling lower bound derives `x2=0` almost everywhere from the first
marginal, whose three atoms all have second coordinate zero. For those
coupling points, the squared Euclidean difference is at least `y2^2`.
Monotonicity of positive real powers, then `ENNReal.ofReal`, gives the
almost-everywhere projected-cost lower bound. The second marginal converts
the projected integral to the target's integral, which is exactly
`ENNReal.ofReal (a*b^p)`. This argument does not insert a finite-support
assumption on the arbitrary coupling.

The matching measure separately attains that exact value. The two bounds
therefore identify the all-coupling infimum. The emerging general scalar
theorems assume `a>=0`, `b>=0`, `p>0`. Their lack of `a<=1` is valid for the
larger family of finite measures defined with clipped `ofReal` weights, but
the probability interpretation additionally requires `a<=1`. Outside that
probability range the same formal definition must not be described as a
three-atom probability family. The intended Wasserstein range is `p>=1`;
positive `p<1` gives a valid infimal cost without the usual metric claim.
The infimum result also allows target heights beyond the fixed cube; the
counterexample family uses the earlier `Admissible` conditions and stays in
its required fixed target container.

The final probability-domain theorem assumes `0<=a<=1`, `b>=0`, and `p>=1`
and explicitly combines probability of both actual targets, both matching
marginal identities, probability of the matching measure, the matching cost
value, and the all-coupling infimum value. Separately,
`actual_coupling_probability` proves that every coupling satisfying these
probability marginals is itself a probability measure. Thus allowing arbitrary
measures in the infimum is equivalent to allowing the usual probability
couplings in this parameter range.

The final `euclideanDistance` definition is literally the square root of the
sum of squared coordinate differences. `measurePCost_eq_distancePower` equates
the integrand to `ENNReal.ofReal (euclideanDistance^p)`. Its scalar identity
permits all real `p`; the transport minimum theorems still assume `p>0` and
the probability specialization assumes `p>=1`.

`actual_transportPowerInf_finite` proves that the actual infimum is below
`top`. `actual_transportDistance_eq` identifies its real `p`-root with the
previously formalized scalar `targetDistance a b p`. The proof uses the exact
finite infimum before applying `toReal`, so it does not exploit `toReal top=0`
or a zero-distance convention for an infinite cost. Its hypotheses are
`a>=0`, `b>=0`, `p>0`, with the probability interpretation restricted as above.
This genuinely promotes the target transport calculation from finite arrays
to actual measure couplings. No semantic scope defect was found in the final
definitions or full theorem statements.

## Verification design and trusted boundary

The new manual harness compares closed whole declaration types and defining
bodies using the unchanged published `EvidenceHarness.lean`. Expected terms
are handwritten; no theorem is specialized or automatically reduced to an
instance. The retained original harness is separately fresh compiled and its
48 type checks and 19 body checks are combined with all 30 new declaration
checks and 11 new body checks: 78 closed whole types and 30 bodies in total.

The follow-up driver fresh compiles the unchanged helper, retained finite and
scalar modules, `Measures`, the retained root import module and original
harness, and the new harness/replay files into a new private cache. Existing
project oleans are excluded. It rejects proof escape tokens outside comments
and strings, audits transitive axiom closures, and uses the same Lean kernel
to replay the combined local declaration closure against imported
`[Mathlib, EvidenceHarness]`.

Compiler loader/runtime byte pins, Lean version/Git hash, and all nine cached
packages' HEAD/origin/clean tracked-source pins are checked before and after.
The driver also checks the retained published core, harness/replay and
historical driver byte-for-byte against the checkpoint. Sources, copied inputs,
configuration, helper, runner, products and captured outputs are checked for
changes. Guards use explicit failures and remain active under Python `-O`.
Every run owns a separate cache, runner snapshot, report and stdout/stderr
artifacts.

## Observed fresh evidence

The final independently reviewed source hashes are:

| File | SHA-256 |
| --- | --- |
| `TransportSharpness/Measures.lean` | `808199ba3c1db1829950488399a63037f4497fd6203cddb334ced85060d5529d` |
| `scripts/FollowupReviewHarness.lean` | `a7273542a7897b173a706b5fdda737f707409cbd4d28cf6f5da7dbd020d41292` |
| `scripts/FollowupReplay.lean` | `19074b426dc714a7ee582c77ef263d4f6a309ca4326800824f05902dca717190` |
| `evidence/followup-lean-review/verify.py` | `bf71ddb57c07e056c5a175dcb4c4a9605f31318483d539c91f53e5eb37ec102e` |

The first fresh follow-up execution ran on 2026-10-13 from `02:23:49` to
`02:26:14` UTC and passed. Its complete evidence is
`evidence/followup-lean-review/20261013T022349298872Z/report.json`.
All 72 retained phases exited zero. The observed checks accepted 78 closed
whole declaration types and 30 defining bodies, then replayed 113 local
declarations, including generated proof auxiliaries. The union of actual
transitive axiom closures was exactly `propext`, `Classical.choice`, and
`Quot.sound`; no `sorryAx` or custom axiom occurred.

The exact command, from the scoped directory, was:

```sh
python3 evidence/followup-lean-review/verify.py --lean /workspace/Codex-for-Math/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lean --lake /workspace/Codex-for-Math/tangent-limit/.elan/bin/lake --elan-home /workspace/Codex-for-Math/tangent-limit/.elan --toolkit /workspace/transport-research/math-evidence
```

A separate fresh optimized execution also passed, with the same final source
and driver hashes, the same 78 whole types, 30 bodies and 113 replayed local
declarations, and optimization level one recorded in its report:
`evidence/followup-lean-review/20261013T022709145274Z/report.json`.
It ran on 2026-10-13 from `02:27:09` to `02:29:17` UTC, with all 72 retained
phases exiting zero.
Its exact command was:

```sh
python3 -O evidence/followup-lean-review/verify.py --lean /workspace/Codex-for-Math/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lean --lake /workspace/Codex-for-Math/tangent-limit/.elan/bin/lake --elan-home /workspace/Codex-for-Math/tangent-limit/.elan --toolkit /workspace/transport-research/math-evidence
```

Both complete reports' source and captured-output hashes were independently
reinspected after execution, with no mismatch. The old checkpoint evidence and
driver were not modified or relabeled as runs of the follow-up implementation.

The report verifies compiler `4.24.0`, Git hash
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`, selected fixed loader/runtime
member bytes, and mathlib HEAD
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. All nine dependency packages matched
their manifest HEAD/origin pins with clean tracked source before and after.
Published checkpoint files, all copied and original sources, configuration,
helper, runner, compiled products and captured outputs passed postflight.
Exact subprocess argv/cwd/environment, timestamps, exit codes, separate
stdout/stderr hashes, and target/body/replay records are retained in each
report. Compiled binaries remain ignored private-cache artifacts.

These are custom scoped review reports using the published helper, not
`math-live-receipt/v1` receipts from the tangent-only runner. Stored hashes do
not authenticate past process events. Same-kernel replay does not supply an
independent kernel implementation or rebuild/replay imported dependency proof
bodies. Cached dependency oleans and host runtime remain explicit trusted
inputs. No native Mac MRS integration is claimed.

## Deferred obligations

The actual atomic-target transport cost is the intended promotion. The uniform
cube source, its Lebesgue density bounds, source-map pushforwards, affine-cell
integration, quadratic source-map optimality/uniqueness and identification of
the same-source matrix with the map norm remain outside this Lean module.
The earlier ordinary proof review supplies those mathematical bridges.

No global upper modulus estimate, endpoint optimality, atom smoothing,
positive target-density bound or novelty claim is supported by these files.
The actual targets remain singular atomic measures. Any extension from the
formalized two-dimensional targets to higher dimensions likewise retains its
ordinary mathematical embedding argument unless separately formalized.
