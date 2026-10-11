# Verified finite-direction convex approximation core

This is the completed Lean checkpoint built from the recovered October 11 drafts.
The root `ConvexApprox.lean` imports all nine delivered modules. All published core
proofs are complete. There are no project proof placeholders or new axioms.

## Main result and exact hypotheses

For a nonempty compact convex set K in a finite-dimensional nontrivial real
inner-product space, use a finite chordal δ-net D of unit directions,
0 ≤ δ < sqrt(2), positive independent slack ε and scale t, and

    N exp(-t ε) < 1, where N = D.card.

The finite sum Φ(x)=∑u∈D exp(t(⟪u,x⟫−hK(u)−ε)) has an open convex sublevel
Ω={Φ<1} containing K. C={Φ≤1} is compact and strictly convex, every open chord
of C lies in Ω, closure Ω=C, and frontier Ω={Φ=1}. The actual Fréchet derivative
is nonzero on level one. The barrier is smooth in every order and its actual
second derivative is positive on nonzero vectors at each point.

The explicit inner tube has radius η=ε−log(N)/t>0. Coercivity follows from a
compiled exponential lower bound. The compiled exact distance and Hausdorff bound is

    (ε + δ sqrt(1−δ²/4) diam(K))/(1−δ²/2).

Finite nets can contain any prescribed finite unit directions. Positive parameters
can be chosen for every requested positive error. An actual recursively selected
family has compact closures C(n+1)⊆Ω(n), vanishing error and Hausdorff distance,
and both intersections equal K. No ambient interior assumption on K is present.
Compiled examples include a planar segment proved to have empty ambient interior
and diameter one, and singleton radius bounds.

## Entry points

- `Approximation.lean`: supportBarrier_outer_approximation, exact pointwise/Hausdorff
  estimates, strict-convex closed set, regular level, inner tube and coercivity.
- `Nesting.lean`: exists_smooth_outer_approximation, nestedBarrierData_compactly_nested,
  nestedBarrierData_compact_closure, nestedBarrierData_intersections and
  nestedBarrierData_hausdorff_tendsto.
- `Barrier.lean`: generic CLM exponential barrier and reusable first/second derivatives.
- `Geometry.lean`, `Quantitative.lean`, `OuterApprox.lean`, `Sublevels.lean`,
  `Construction.lean`: geometry, exact error and parameter/sublevel infrastructure.
- `Examples.lean`: actual lower-dimensional and singleton applications.

## Verification and reproduction

Pinned Lean 4.24.0 compiler commit:
797c613eb9b6d4ec95db23e3e00af9ac6657f24b.
Pinned mathlib commit: f897ebcf72cd16f89ab4577d0c826cd14afaafc7.
All nine dependency commits and exact input/toolchain/lock hashes were checked.
The supplied receipts record compiler and clean cached-dependency identity.
Publication-source compilation reuses pinned dependency OLeans; it does not
rebuild the complete dependency library.

Put Lean/Lake 4.24.0 on PATH or set CONVEX_LEAN_BIN to its bin directory.
Source `scripts/environment.sh` after setting that variable (or placing Lean/Lake
on PATH). Run `lake exe cache get` if dependency caches are absent, then
`bash scripts/verify.sh /absolute/new-output-directory`. The output argument is
optional and defaults to `logs/current`; supplied historical logs are preserved.
The environment helper requires the chosen Lean/Lake 4.24.0 on PATH or an explicit
CONVEX_LEAN_BIN. Compiler and dependency caches are not distributed.

The final verification script removes only this project's own build products,
builds every root import freshly, checks exact types and axiom dependencies of all
145 inventoried declarations, and performs a source placeholder and pin audit.
Actual final logs and independent frozen-source review are under `logs/` and `notes/`.
Earlier failed development logs are retained and are not labeled passes.

## Input and scope

The recovered input checkpoint was 558,341 bytes, SHA-256
`c3c64e17ae69ef244c5355dd41a526b5ac810059f1b0e9353e7101591ea07aa3`.
Archive identity facts remain in `evidence/input-identity.json`. The recovered
ordinary study is already published at
[`research/supplement/convex-approximation`](../research/supplement/convex-approximation/README.md);
its revision-pinned upstream text and license are recorded by the existing corpus
catalog and third-party attribution. Private input archives, drafts, recovery
handoffs and duplicate ordinary study/source copies are omitted.

The supplied inventory checks 145 explicit declarations: 124 theorem/lemma
statements, 20 definitions and one structure. It omits the `Examples.Plane`
abbreviation. Fresh publication audits check the original 145 plus that
abbreviation separately: 146 explicitly named source declarations. Generated
structure projections are not claimed as separate inventoried entries.
See `../publication/evidence/CONVEX-APPROX-CHECKS.json` for fresh verification.

Deferred: analytic boundary manifold charts and sphere/Jordan parametrizations.
No globally uniform strong-convexity modulus, uniform curvature, optimal net size,
or verification of the source's headline result is claimed. The ordinary study
contains broader claims; it is provenance, not the compiled-library scope.
