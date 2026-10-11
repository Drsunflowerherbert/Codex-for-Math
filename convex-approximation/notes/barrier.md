# Finite continuous-linear-form exponential barrier

The recovered `BarrierDerivatives.lean` and `BarrierScratch.lean` have been integrated into
`ConvexApprox/Barrier.lean`, with one shared definition of `ConvexApprox.barrier`.
The resulting source compiles against the saved Lean 4.24.0 and mathlib
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7` pins. Final integrated build and independent statement review are separate; this note records the barrier component's verified scope.

## Exact generality

Let `E` be any real normed vector space, `ι` any finite type,
`L : ι → E →L[ℝ] ℝ` continuous linear forms, and `b : ι → ℝ` arbitrary real offsets.
The barrier is

`barrier L b x = ∑ i, exp (L i x - b i)`.

The generic API makes no finite-dimensional, completeness, nonempty-index, positive-scale,
compact-set, or ambient-interior assumption. The geometry module may instantiate `L` with
scaled inner-product forms. Empty finite index types are allowed, and their sum is zero.

## Compiled statements and proof ideas

- `hasFDerivAt_barrier`, `fderiv_barrier`, `barrierDeriv_apply`:
  `D barrier(x)[y] = ∑ i, exp(L i x - b i) * L i y`.
  Finite sums, continuous linear maps, and the exponential chain rule prove this formula.
- `hasFDerivAt_barrierDeriv`, `fderiv_barrierDeriv`, `fderiv_fderiv_barrier`,
  `barrierHessian_apply`, `barrierHessian_diag`:
  `D² barrier(x)[y,z] = ∑ i, exp(L i x - b i) * L i y * L i z`.
- `contDiff_barrier` proves `ContDiff ℝ n` for every `n : WithTop ℕ∞`.
- `barrierHessian_symmetric` and `barrierHessian_nonneg` prove symmetry and positive
  semidefiniteness at every point. The diagonal formula is a sum of positive exponential
  weights times squares.
- `barrierHessian_pos_of_exists` gives strict positivity for any `y` detected by one form.
  `barrierHessian_pos` gives positive definiteness under the visible hypothesis
  `∀ y : E, y ≠ 0 → ∃ i, L i y ≠ 0`.
- `convexOn_barrier` proves convexity on `Set.univ`. `strictConvexOn_barrier` proves strict
  convexity under the same separation hypothesis. The proof applies (strict) convexity of
  exponential to each affine form; one strict summand follows by separation of `x-y`.
- `barrier_supporting` proves
  `barrier x + barrierDeriv x (y-x) ≤ barrier y` by summing the elementary inequality
  `1+v ≤ exp v` after multiplying by a positive exponential weight.
- For arbitrary real level `c` and anchor `p` with `barrier p < c`,
  `barrierDeriv_apply_pos_of_level` proves
  `0 < barrierDeriv x (x-p)` whenever `barrier x = c`.
  Consequently `barrierDeriv_ne_zero_of_level` proves `barrierDeriv x ≠ 0`.
  This implication does not need the separation hypothesis.
- Under the same strict anchor, `closure_barrier_lt` proves
  `closure {x | barrier x < c} = {x | barrier x ≤ c}`. Continuity gives one inclusion;
  an open segment from `p` to any closed-sublevel point gives the other.
- `frontier_barrier_lt` then proves
  `frontier {x | barrier x < c} = {x | barrier x = c}`.

The strict anchor is essential for the last three implications. It is stated explicitly,
rather than being inferred from nonempty compact `K`. No ambient interior of `K` is needed
once the separate sublevel inclusion proof supplies such an anchor. For level one, set
`c := 1` and choose any point proved to lie in the open sublevel.

## Validation evidence

Commands were run from `project/` after sourcing `scripts/environment.sh`:

1. `lake env lean ConvexApprox/Barrier.lean`: exit 0, final direct-compiler output empty,
   saved in `logs/barrier-level-final.log`.
2. `lake build ConvexApprox.Barrier`: exit 0, 7351 jobs completed successfully,
   saved in `logs/barrier-build-final.log` (the barrier itself rebuilt).
3. `lake env lean logs/barrier-audit.lean`: exit 0; expanded exact theorem types and
   `#print axioms` output saved in `logs/barrier-audit.log`.
4. The source contains no `sorry`, `admit`, or `axiom` declaration/token.

The audit covers every theorem listed above. Every printed theorem depends only on
Lean/mathlib's standard `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or
project-specific axiom occurs. `logs/barrier-environment.log` records compiler identity,
mathlib commit, and the source/pin hashes. Initial failing direct-compiler logs are retained
truthfully as repair history (`barrier-initial.log`, `barrier-level-initial.log`); the final
successful runs are separate.

## Scope boundaries

This component proves pointwise positive-definite Hessian under separation, not a globally
uniform strong-convexity modulus. It proves smooth barrier and regular level by nonzero
Fréchet derivative, but no analytic hypersurface, manifold atlas, sphere parametrization,
principal-curvature theorem, or certified nesting construction. It does not establish
coercivity or compactness: those require the geometric positive-spanning hypotheses supplied
by the separate sublevels/geometry modules. No result silently assumes that the approximated
compact convex set has ambient interior.

Publication notice: the historical absolute scratch audit path was normalized to the retained `logs/barrier-audit.lean`; recorded outcomes and source fingerprints are unchanged.
