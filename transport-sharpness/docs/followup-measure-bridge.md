# Actual atomic measures and all-Borel-coupling target costs

This follow-up starts from the published checkpoint
`40589436a45ddfd2cc8df8897e86b3185b83a107` on the same assigned branch. It adds
[Measures.lean](../TransportSharpness/Measures.lean) while preserving the old
mathematical modules, root import, review harness, replay harness and verifier.
The focused addition proves an actual-measure target-cost bridge in dimension
two. The uniform cube source and its optimal maps are still separate deferred
Lean obligations.

## Actual definitions

The point type is `Point = ℝ × ℝ`, with its standard product Borel measurable
space. Its product topology has the usual Euclidean Borel sets. The metric
cost is specified explicitly by coordinates rather than using Lean's default
product max norm:

\[
q(y,z)=(y_1-z_1)^2+(y_2-z_2)^2,\qquad
r(y,z)=\sqrt{q(y,z)}.
\]

`euclideanSquared_nonnegative` proves `q>=0`, and
`measurePCost_eq_distancePower` proves that the nonnegative cost

\[
c_p(y,z)=\operatorname{ofReal}\bigl(q(y,z)^{p/2}\bigr)
\]

is exactly `ofReal(r(y,z)^p)`. Both this cost and the destination projection
cost are Borel measurable. These are literal Euclidean coordinate formulas;
no formal theorem about a pre-existing mathlib Wasserstein API is asserted.
The pinned mathlib source inspection found no such API to reuse.

For `m=(1-a)/2`, `atomicMeasure a b` is the actual Borel measure

\[
\nu_{a,b}=\operatorname{ofReal}(m)\delta_{(-1,0)}
+\operatorname{ofReal}(a)\delta_{(0,b)}
+\operatorname{ofReal}(m)\delta_{(1,0)}.
\]

The Lean expansion theorem matches those three weighted Dirac measures, and
`atomicMeasure_probability` proves their total mass is one when `0<=a<=1`.
The source marginal in the target-to-target problem is `mu_a=nu_(a,0)`.
It is an atomic target law, not the original cube source `rho`.

`IsMeasureCoupling a b gamma` requires exactly

\[
(\mathrm{fst})_\#\gamma=\mu_a,\qquad
(\mathrm{snd})_\#\gamma=\nu_{a,b}.
\]

Its argument ranges over **every Borel measure on Point × Point**. It does
not assume an atomic form, a finite-array representation, graph support,
or the desired cost value. `actual_coupling_probability` proves that these
marginal equalities force `gamma` to be probability when `0<=a<=1`.
Consequently the domain is exactly the usual probability-coupling domain in
that parameter range, even though the predicate is phrased as marginal
measure equalities.

## Lower bound for every actual coupling

Let `a>=0`, `b>=0` and `p>0`. Every point charged by `mu_a` has second coordinate
zero. `atomicMeasure_zero_second_ae` proves this a.e. statement, and
`coupling_zero_second_ae` transports it through the first-marginal equality:

\[
y_2=0\quad\text{for }\gamma\text{-almost every }(y,z).
\]

At those points, `q(y,z)>=z_2^2`. Monotonicity of positive real powers gives

\[
\operatorname{ofReal}((z_2^2)^{p/2})\le c_p(y,z).
\]

The second-marginal equality and mathlib's `lintegral_map` identify the
projected cost integral under `gamma` with the actual integral under
`nu_(a,b)`. Weighted Dirac integration gives

\[
\int^- \operatorname{ofReal}((z_2^2)^{p/2})\,d\nu_{a,b}
=\operatorname{ofReal}(ab^p).
\]

The outer values vanish because `p>0`; the central value uses the retained
proved identity `(b^2)^(p/2)=b^p` for `b>=0`. The core theorem
`actual_coupling_lower_bound` therefore proves

\[
\operatorname{ofReal}(ab^p)\le\int^- c_p\,d\gamma
\]

for every actual coupling. No theorem representing all Borel couplings by
finite arrays is needed for this argument.

## Matching attainment and infimum

The actual matching measure is

\[
\gamma_*=\operatorname{ofReal}(m)\delta_{((-1,0),(-1,0))}
+\operatorname{ofReal}(a)\delta_{((0,0),(0,b))}
+\operatorname{ofReal}(m)\delta_{((1,0),(1,0))}.
\]

`matchingMeasure_coupling` proves both actual map marginals.
`matchingMeasure_cost` proves its nonnegative integral cost is exactly
`ofReal(ab^p)`.

`transportPowerInf` is the infimum of that actual nonnegative integral over
all measures satisfying both marginal equalities. The matching witness
establishes a nonempty domain, and the all-coupling lower bound and attained
upper bound give

\[
\operatorname{transportPowerInf}(a,b,p)
=\operatorname{ofReal}(ab^p).
\]

`actual_transportPowerInf_finite` proves that infimum is finite. Finally
`actual_transportDistance_eq` proves

\[
\bigl(\operatorname{transportPowerInf}(a,b,p).\mathrm{toReal}\bigr)^{1/p}
=a^{1/p}b=\operatorname{targetDistance}(a,b,p).
\]

Thus the previous scalar target-distance formula now has a kernel-checked
link to the root of the actual all-Borel-coupling infimal Euclidean cost in
dimension two. Under `0<=a<=1`, `b>=0`, `p>=1`, this is the ordinary
`Wp(mu_a,nu_(a,b))` definition with its full coupling domain. The combined
`actual_probability_transport` theorem explicitly supplies both target
probabilities, matching coupling/probability, attained cost and infimum value.
It does not claim a built-in abstract Wasserstein metric or metric axioms.

## Exact domains and retained limits

The cost, lower bound, infimum and root identities hold for `a>=0`, `b>=0`,
`p>0`. Outside `a<=1`, negative outer coefficients are truncated by `ofReal`,
so those are equal-mass finite-measure statements. For example, when `a>1`
the actual measures have total mass `a`. They must not be described as
probability Wasserstein statements. The promoted probability theorem requires
`0<=a<=1` and `p>=1` explicitly. At `a=0` or `a=1` fewer positive atoms remain;
exactly three positive atoms requires `0<a<1`. Positive `b` makes the two
laws distinct and their distance positive. The exponent-zero convention is
not silently included: `p>0` is essential for the vanishing outer costs.

Formalized coverage is **dimension two**. The earlier ordinary product
argument still extends the example to each fixed `d>=2`, and the reviewed
shrinking-mass ceiling `p/[2(p+1)]` and fixed-mass ceiling `1/2` remain
unchanged. This follow-up does not identify `mapSize` with the L2 norm of an
actual uniform-source map. Remaining formalization tasks are the cube source
and density bounds, affine cells and null boundaries, actual source-to-target
pushforwards, optimality and uniqueness of the quadratic maps, the joint cell
matrix's identification with the same-source law, and higher-dimensional
integration. Finite-array representation and target optimizer uniqueness
remain unproved in Lean, though representation is unnecessary for the new
all-coupling target-cost argument.

No global positive upper estimate, endpoint optimality, novelty, bounded
target-density obstruction, broad optimal transport library, native Mac MRS
integration or independent kernel implementation is claimed.

## Reproduction and independent evidence

The old project root continues importing the preserved finite/scalar core.
Build the focused new module explicitly with the same official pins:

```sh
export ELAN_HOME=/workspace/Codex-for-Math/tangent-limit/.elan
export PATH="$ELAN_HOME/bin:$PATH"
lake build TransportSharpness.Measures
```

The independent follow-up checks use
[`FollowupReviewHarness.lean`](../scripts/FollowupReviewHarness.lean),
[`FollowupReplay.lean`](../scripts/FollowupReplay.lean), and a separate
[`verify.py`](../evidence/followup-lean-review/verify.py). The old verification
files and historical receipts are preserved. The new harness manually checks
all 30 new closed declaration types and 11 definition bodies, together with
the retained 48 types and 19 bodies. Replay covers the combined local closure
against the same imported `[Mathlib,EvidenceHarness]` baseline.

```sh
python3 -B evidence/followup-lean-review/verify.py \
  --lean /workspace/Codex-for-Math/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lean \
  --lake /workspace/Codex-for-Math/tangent-limit/.elan/bin/lake \
  --elan-home /workspace/Codex-for-Math/tangent-limit/.elan \
  --toolkit /workspace/transport-research/math-evidence
```

Exact final hashes, fresh commands/results, full-type/body/axiom/replay
coverage and remaining obligations are in the independent
[proof review](../reviews/followup-proof-review.md),
[Lean review](../reviews/followup-lean-review.md) and
[follow-up status](../FOLLOWUP-STATUS.json). The trust limits of the original
verification remain: official compiler member pins, pinned clean package
sources, trusted cached dependency OLeans/host runtime, same-kernel replay,
and no proof promotion from source inspection or stored reports alone.
