# Independent proof review of the actual-measure target-cost bridge

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](../PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

This focused follow-up starts from published checkpoint
`40589436a45ddfd2cc8df8897e86b3185b83a107`. It reviews the new
`TransportSharpness/Measures.lean` against the original Euclidean
transport definitions and the retained finite/scalar calculation.
The earlier proof review and all previous source claims remain preserved.

The new mathematical specification and inspected source are supported.
The module promotes the two-dimensional target transport optimum from
finite arrays to an infimum over actual Borel coupling measures. It does
not promote the cube source, its affine-cell maps, or their map norm to
a formal measure-theoretic theorem.

## Definitions and the all-coupling domain

The types `Point = R x R` and `PointPair = Point x Point` use their
ordinary product Borel measurable spaces. The product Borel structure
on finite-dimensional real coordinates is the same Borel structure as
the Euclidean topology. No special finite-atomic measurable space is
substituted for the ambient space.

With `m=(1-a)/2`, the explicit expansion theorem identifies the actual
target measure as

\[
\lambda_{a,b}
=\operatorname{ofReal}(m)\delta_{(-1,0)}
 +\operatorname{ofReal}(a)\delta_{(0,b)}
 +\operatorname{ofReal}(m)\delta_{(1,0)}.
\]

Here coefficients are nonnegative extended reals and `ofReal` truncates
negative real values to zero. For `0<=a<=1`, no coefficient is changed
by truncation and their sum is one. Thus `atomicMeasure a 0` and
`atomicMeasure a b` are exactly the original probability targets in
dimension two, for any real `b`. The original cube example further
restricts the parameters by `Admissible a b`, ensuring in particular
`0<a<1` and `0<b<1`.

`IsMeasureCoupling a b gamma` states exactly

\[
(\mathrm{fst})_\#\gamma=\lambda_{a,0},\qquad
(\mathrm{snd})_\#\gamma=\lambda_{a,b}.
\]

It has no finite-array, finite-support, graph-plan, optimality, or cost
restriction on `gamma`. Its argument ranges over every actual measure
on `PointPair`. In the probability range, the first marginal equality
implies that every such coupling is a probability measure, as the new
theorem `actual_coupling_probability` establishes.

The infimum is a double indexed infimum in the complete lattice
`ENNReal`: first over every measure, then over every proof of its
coupling predicate. A measure that fails the predicate contributes the
empty infimum, which is infinity, and does not restrict the admissible
domain. The explicit matching coupling proves the admissible domain is
nonempty. No empty-set convention or restricted list of candidate
plans produces the claimed optimum.

## Coordinate cost and Euclidean compatibility

For a pair `(x,y)`, the source defines

\[
q(x,y)=(x_1-y_1)^2+(x_2-y_2)^2\ge0,
\qquad d_E(x,y)=\sqrt{q(x,y)}.
\]

This is the Euclidean coordinate distance. It avoids Lean's default
maximum norm on a product type. The accepted theorem
`measurePCost_eq_distancePower` proves that the cost integrand is

\[
\operatorname{ofReal}\bigl(q(x,y)^{p/2}\bigr)
=\operatorname{ofReal}\bigl(d_E(x,y)^p\bigr).
\]

The nonnegative integral `measureCost` is therefore the original
Euclidean `p`-cost of an actual plan for the intended range `p>=1`.
Both the cost and the projected cost are measurable. The lower-level
cost identity is correctly stated for all real scalar `p`; the
attainment and projection calculations use `p>0`. The case `p=0` must
not be inserted into their formulas: the zero-cost outer pairs would
have the totalized `0^0` value rather than zero.

There is no imported Wasserstein API in the new module. The accepted
objects are actual nonnegative coupling integrals, their unrestricted
infimum, and its cost root with the explicit Euclidean cost. Their
identification with the usual Wasserstein definition at `p>=1` follows
directly from the defining coupling formula. No separate general
metric-space Wasserstein theory is claimed.

## Independent derivation of the lower bound and attainment

Every atom of `lambda_(a,0)` has second coordinate zero. The first
marginal equality therefore implies `x2=0` almost everywhere for every
actual admissible `gamma`. This step is proved through `ae_of_ae_map`
with the measurable first-coordinate projection; it does not assume
the arbitrary plan is supplied as an atomic array.

On those almost-everywhere coupling points,

\[
y_2^2\le q(x,y).
\]

For `p>0`, raising both sides to `p/2` preserves their order. Applying
the monotone map `ofReal`, integrating, and using the second marginal
gives

\[
\begin{aligned}
\operatorname{cost}_p(\gamma)
&\ge\int \operatorname{ofReal}((y_2^2)^{p/2})\,d\gamma\\
&=\int \operatorname{ofReal}((y_2^2)^{p/2})\,d\lambda_{a,b}\\
&=\operatorname{ofReal}(ab^p),
\end{aligned}
\]

for `a>=0`, `b>=0`, `p>0`. At the target's outer atoms the integrand
vanishes; at its central atom it equals `ofReal(b^p)` by
`(b^2)^(p/2)=b^p`. Integration against the real nonnegative central
weight produces exactly the last expression. The proof uses ordinary
nonnegative Lebesgue integration; a hypothetical competing plan's
infinite cost causes no undefined subtraction or comparison.

The explicit matching measure is

\[
\gamma_*
=\operatorname{ofReal}(m)\delta_{((-1,0),(-1,0))}
 +\operatorname{ofReal}(a)\delta_{((0,0),(0,b))}
 +\operatorname{ofReal}(m)\delta_{((1,0),(1,0))}.
\]

Its two marginals are the required actual measures for every real
`a,b`, since both use the identical possibly truncated weights.
For `a>=0`, `b>=0`, `p>0` it has cost `ofReal(ab^p)`. The lower bound
and this attained upper bound prove

\[
\operatorname{transportPowerInf}(a,b,p)
=\operatorname{ofReal}(ab^p)<\infty.
\]

The infimum is finite before `toReal` is used. Consequently taking its
`1/p` real power is legitimate and the accepted equality

\[
\operatorname{transportPowerInf}(a,b,p).\operatorname{toReal}^{1/p}
=a^{1/p}b
\]

links it exactly to the retained scalar `targetDistance`. The root
formula also handles `a=0` or `b=0` without a positive-distance claim.

## Hypotheses and boundary cases

The declaration domains are mathematically consistent:

- Probability normalization and arbitrary-coupling probability use
  `0<=a<=1`; the target displacement `b` need not be bounded for these
  probability facts.
- The general projection, attained-cost, infimum and cost-root formulas
  use `a>=0`, `b>=0`, `p>0`. They omit `a<=1` and remain valid finite
  measure identities outside the probability range. For `a>1`, the
  outer weights are truncated to zero and the central weight has total
  mass `a`; those statements must not be called probability Wasserstein
  formulas without the additional upper bound.
- `actual_probability_transport` includes `0<=a<=1`, `b>=0`, `p>=1`
  and correctly combines both probability targets, an actual matching
  coupling, its probability property, attained cost, and the exact
  all-coupling infimum.
- At `a=0` only the two outer atoms have positive mass; at `a=1` only
  the central atom has positive mass. Exactly three positive atoms
  requires `0<a<1`. Their positions are distinct even when `b=0`;
  requiring `b>0` additionally ensures the two probability targets
  differ and their transport distance is positive.
- Without a bound on `b`, probability targets need not lie in the fixed
  cube. The original `Admissible` regime supplies that bound. The
  shrinking scalar witnesses and fixed-mass scalar witnesses both
  produce parameters in this regime.
- The formalized ambient dimension is two. The retained ordinary proof's
  extension to every fixed `d>=2` is a separate coordinate embedding
  and product-integration argument.

No hypothesis loss changes the original exponent conclusions. The new
root equality justifies replacing the scalar target distance by the
actual two-dimensional target cost root in those retained witnesses.
It does not by itself replace `mapSize` by an actual source-map norm.

## Independent Lean source check

The final inspected module has SHA-256
`808199ba3c1db1829950488399a63037f4497fd6203cddb334ced85060d5529d`.
The retained `Finite.lean` and `Obstruction.lean` hashes remain
`2ca131e39877bb4ec3d0803de4b9bdfa21d7d2e2935f9777db0408aa3cadf18a`
and `ebb8d5361a6dce5ebc7e436d59750a58581030ca1d351e420f9280dcf83df0e1`.
The new module contains 11 definitions/abbreviations and 19 theorems.
It declares no new axiom or proof placeholder, and no `sorry`, `admit`
or unsafe escape appears in the inspected source.

Independently executed from `transport-sharpness/` on 2026-10-13:

```sh
env PATH=${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin:$PATH ${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lake env lean TransportSharpness/Measures.lean
```

Result: exit status zero, with no stdout or stderr. This used the pinned
Lean `v4.24.0` compiler, mathlib revision
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, and existing cached imports.
The independent full-type/body/closure-replay evidence is supplied by
the separate follow-up Lean-review agent. This ordinary proof reviewer
does not claim to have rebuilt dependencies or implemented another
kernel.

## Preserved deferred obligations

The remaining proof boundary stays explicit:

- Formal construction and normalization of the uniform cube source and
  its density bounds;
- Formal Borel affine-cell maps, their null tie sets, and pushforwards;
- Formal source-to-target quadratic optimality and plan/map uniqueness;
- Formal cell integration and identification of the same-source joint
  measure with the retained matrix and `mapSize`;
- Formal higher-dimensional embedding/product integration;
- A general finite-array representation theorem for arbitrary actual
  atomic couplings, which this projection argument does not need.

The atomic targets remain singular. This follow-up supplies no positive
target-density theorem, smoothing argument, endpoint upper stability
bound, global optimality theorem, novelty claim or native MRS import.

## Final documentation disposition

The final `docs/followup-measure-bridge.md` was read in full, together
with the README follow-up notice. The document accurately presents the
actual atomic marginal measures, the unrestricted actual-coupling
predicate, explicit Euclidean cost, marginal projection argument,
matching attainment, complete infimum and finite cost-root equality.
It explicitly distinguishes the general nonprobability finite-measure
range `a>=0`, `b>=0`, `p>0` from the probability Wasserstein range
`0<=a<=1`, `b>=0`, `p>=1`. It states the `p=0` convention, zero atom
weights at `a=0,1`, positive-distance role of `b>0`, and dimension-two
coverage correctly. It keeps the actual uniform-source map norm as a
separate deferred Lean obligation.

Two wording clarifications requested during review have been applied
and checked: the all-coupling lower-bound section now includes `a>=0`
explicitly, and the old README deferred-integration description now
says "cube-source Lebesgue integration". Thus the new accepted target
cost integrals are not mistakenly included in that deferred scope.
Neither clarification changes a mathematical statement or Lean source.

Final reviewed hashes:

- `TransportSharpness/Measures.lean`:
  `808199ba3c1db1829950488399a63037f4497fd6203cddb334ced85060d5529d`;
- `docs/followup-measure-bridge.md`:
  `7c7202d469172c20f8d33acd8c3138b80a3e8ff919cc49853741bfa39df63df2`;
- `README.md`:
  `0ab929a2e0e4328cf887c78be049e8c184c95e507a898e7f65b10aa7bd35b678`.

This reviewer independently inspected all 30 new declarations
(11 definitions/abbreviations and 19 theorems) and directly checked the
module with the real pinned Lean compiler as recorded above. The
separate full-type/body/axiom/replay report owns its additional fresh
verification results and exact coverage; this ordinary mathematical
review does not substitute source inspection for those processes.
The final whitespace check `git diff --check` also passed.

Final verdict: the new actual-target transport-cost bridge and its
documentation are supported under their explicit hypotheses, with no
remaining required mathematical correction. The newly accepted actual
infimum and root equality supply a useful target-side bridge; a full
formal optimal-map modulus obstruction still requires the preserved
cube-source and map-norm obligations listed above. This review does
not certify remote publication, a global upper theorem, or a native
MRS integration.
