# Verified quantitative core

`Quantitative.lean` repairs and extends the recovered draft, using the ordinary
proof in [the existing study](../../research/supplement/convex-approximation/study.md), section 5. The recovered definitions needed a
noncomputable section, and the inner-product notation needed its correct scope.
The original elementary lemma proof text otherwise compiles.

The exact constants are `chordalCos δ = 1 - δ²/2` and
`chordalSin δ = δ sqrt(1 - δ²/4)`. For unit directions `u, ν` at chordal distance
at most δ, with δ² < 2, their inner product is at least `chordalCos δ > 0`.
The tangential component `u - inner u ν • ν` has norm at most `chordalSin δ`.

`support_displacement_le_chordalSin` takes `inner ν (v-w) ≤ 0` and `norm(v-w) ≤ L`.
It multiplies the normal inequality by the nonnegative coefficient `inner u ν`,
then bounds the remaining tangential inner product by Cauchy–Schwarz. This gives
`inner u (v-w) ≤ chordalSin δ * L`.

`local_outer_error` takes the explicit representation `x-w = r • ν`, with
`r ≥ 0`, and support slack `inner u x ≤ inner u v + ε`. It proves
`r ≤ (ε + chordalSin δ * L) / chordalCos δ`. The local theorem needs no compactness,
convexity, dimensionality, or positivity of ε beyond its visible algebraic hypotheses.

`OuterApprox.lean` composes this core with Geometry's support attainment and
nearest-point normality. Its main pointwise theorem `infDist_le_outerErrorBound`
requires a nonempty compact convex K, a finite chordal net D, `0 ≤ δ`, `δ² < 2`,
`0 ≤ ε`, and all finite support inequalities at x. It requires no ambient interior
or finite-dimensional assumption. Finite-dimensionality is used by Geometry only
to construct nets. The denominator is strictly positive under the stated interval.

`outer_set_subset_tube` supplies a set inclusion. `hausdorffDist_le_outerErrorBound`
additionally requires `K ⊆ C`; this hypothesis is explicit. The two `*_exact_outer_error`
corollaries expand the definitions and state the requested formula using
`0 ≤ δ < sqrt 2`:

    (ε + δ sqrt(1 - δ²/4) diam(K)) / (1 - δ²/2).

`outerErrorBound_le_simple` gives the weaker numerator `ε + δ diam(K)`.
These are upper bounds; no claim of optimality is made. The statements include
singletons and lower-dimensional compact convex sets because neither their proofs
nor the supporting Geometry API assumes nonempty ambient interior.

The finite support inequalities must be obtained from the exponential barrier by
its separate sublevel module. Quantitative statements by themselves do not establish
analyticity, boundary regularity, radial parametrization, or a nested sequence.

Verification for this subtask: direct compilation of Quantitative passed; Lake builds
of Quantitative and OuterApprox passed. The final OuterApprox build has no warnings.
The exact-type/axiom audit covers all 19 theorems in these two files and passes; every
reported dependency is limited to propext, Classical.choice, and Quot.sound. The source
scan finds no sorry, admit, or axiom declaration. Actual compiler output, unsuccessful
iterations, commands, hashes, and statuses are retained in logs/quantitative*. The fresh integrated build and independent final statement review are separate
evidence.
