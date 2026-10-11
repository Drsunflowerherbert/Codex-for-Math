# Independent statement review

An independent statement reviewer wrote this note and the
`logs/independent-review*` artifacts without changing the implementation.

## Initial review (source still in development)

The delivered theorem statements in `Geometry.lean`, `Quantitative.lean`, and
`Barrier.lean` were inspected against the recovered ordinary study. The original
study's analytic hypersurface and sphere parametrization claims are ordinary proof
evidence only, not claims licensed by these Lean modules.

- Compact support attainment and nearest-point supporting normality require
  `IsCompact K`, `K.Nonempty`, and (for normality) `Convex ℝ K`. They do not require
  `interior K` to be nonempty. This correctly permits singletons and compact convex
  subsets of proper affine subspaces.
- The chordal net is explicitly a finite set of unit vectors that covers every
  unit vector in ambient norm distance. Net construction requires finite
  dimensionality and strictly positive resolution. Quantitative conditional
  statements may allow resolution zero, without claiming that a finite zero-net
  exists in dimension at least two.
- The exact constants are `c = 1 - δ²/2` and
  `s = δ * sqrt (1 - δ²/4)`. The positive-denominator condition is `δ² < 2`;
  converting the displayed interval `δ < sqrt 2` also requires `0 ≤ δ`.
- The tangential estimate retains the sign of the nearest-point supporting
  normal and uses the positivity of the normal coefficient. The compact diameter
  bound is applied only to two actual points of K.
- Generic finite exponential sums have proved Fréchet derivatives, the exact
  second derivative, all-order `ContDiff`, convexity, and a nonnegative Hessian.
  Linear separation yields strict convexity and pointwise positive Hessian.
  Separation alone does not imply coercivity or a globally uniform positive
  Hessian lower bound.
- The strict-anchor hypothesis is visible in the regular-level, closure, and
  frontier statements. The nonzero derivative conclusion is a statement about
  the continuous linear map. It does not itself supply an analytic manifold or
  sphere parametrization.

The environment helper resolves Lean 4.24.0, compiler commit
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`. A direct independent invocation of
`lake env lean ConvexApprox/Geometry.lean` exited 0. This initial check does not
replace the final fresh full build or final frozen-source type/axiom audit.

## Final review

Frozen-source mathematical statement review: **pass, no mathematical blocker**.
The root imports all nine delivered modules. The supplied finalization build removed only
this project's `.lake/build`, rebuilt all nine modules and the root, and exited 0
without warnings (`logs/final-build.log`). The corrected independent compiler
audit also exited 0, with unchanged frozen source and pins.

The reusable main certificate is
`ConvexApprox.supportBarrier_outer_approximation`. Its ambient space is a
finite-dimensional nontrivial real inner-product space. Its geometric hypotheses
are exactly `IsCompact K`, `K.Nonempty`, and `Convex ℝ K`. It requires a finite
chordal net, `0 ≤ δ < sqrt 2`, independent positive support slack `ε`, positive
scale `t`, and the **strict** margin `D.card * exp(-t * ε) < 1`.
No positive diameter, ambient interior, or full affine dimension of K is assumed.

The exact delivered point-distance and Hausdorff bound is

    (ε + δ * sqrt(1 - δ²/4) * diam(K)) / (1 - δ²/2).

The denominator is positive under the displayed interval. The weaker numerator
`ε + δ * diam(K)` is a separate corollary. The Hausdorff theorem supplies the
necessary inclusion of K using the strict cardinal margin. The earlier generic
Hausdorff theorem instead keeps `K ⊆ C` as an explicit hypothesis. In the actual
barrier application the closed sublevel is nonempty and compact, so no empty-set
or infinite-distance convention is being used to simulate an approximation.

The explicit inner radius is `η = ε - log(D.card)/t`. The nonempty-net and positive
scale hypotheses needed for the logarithmic equivalence and positive radius are
visible. Every point with `Metric.infDist x K < η` belongs to the strict sublevel.
Support attainment and nearest-point attainment supply genuine witnesses; they
do not silently replace K by its convex hull or its affine hull.

The coercivity theorem uses the **positive covering inequality**
`c * norm(y) ≤ inner(u,y)`, with `c > 0`, and proves a full cobounded-to-atTop
limit, not merely boundedness of one sublevel. Every real closed sublevel is
compact in the proper-space generic API and in the finite-dimensional support
API. In contrast, linear separation alone supports strict convexity and the
positive Hessian, and is not used as a coercivity hypothesis.

The Hessian theorem is about the actual iterated Fréchet derivative and proves
positivity on each nonzero vector at each point. The generic modules also expose
the exact derivative and bilinear Hessian formulas. No globally uniform
strong-convexity modulus follows from these statements. All-order `ContDiff`,
strict convexity of the barrier, convexity of the open sublevel, strict convexity
of the closed sublevel as a set, and the stronger open-chord property are
delivered as actual named Lean theorems.

The closure and frontier are exactly the closed sublevel and the level-one set.
The actual Fréchet derivative is nonzero on level one. The strict anchor is
provided by K and the strict cardinal margin. These are the delivered boundary
and differential statements. **Analytic boundary charts, an embedded analytic
hypersurface, and a sphere parametrization remain deferred**; the ordinary study
contains proof guidance for them, but these modules do not claim their Lean
formalization. No curvature or limiting derivative claim is made.

`ConvexApprox.exists_outer_parameters_containing` selects strictly positive
resolution/slack/scale, preserves any prescribed finite unit family, and makes
the exact numerical error smaller than any `ρ > 0`. Its lack of compactness and
convexity assumptions is deliberate: it asserts numerical parameter selection
only. `exists_smooth_outer_approximation` then combines that selection with the
geometric hypotheses to produce actual compact outer approximations.

The delivered `nestedBarrierData` is an actual recursively selected sequence.
Each next error is below half the preceding **positive** tube margin and below a
vanishing target. The certified successor inclusion is between the next closed
sublevel and the preceding open sublevel. The family has compact closures,
errors tending to zero, actual Hausdorff distances tending to zero, and both
open and closed intersections equal to K. This is a margin certificate, not an
inference from parameter decay alone.

The examples are substantive lower-dimensional instances. A planar segment is
proved nonempty, compact, convex, of diameter one, and to have **empty ambient
interior**. Its actual support barrier satisfies compactness, strict inclusion,
and the exact Hausdorff bound. A planar singleton has its actual barrier radius
bounded by `ε / chordalCos δ`, with its diameter term eliminated exactly.

Dimension restrictions are consistent: the existential construction and nested
family require a nontrivial ambient space. Generic support/error lemmas are more
general. The conditional zero-resolution endpoint does not assert that a finite
zero-net exists in dimension at least two. No zero-dimensional sphere or
manifold convention is claimed.

## Independent compiler evidence

The independent inventory covers 145 named declarations, including all 124
theorems/lemmas, definitions, and the barrier-data structure. Every declaration
is checked with explicit parameters and universes; every declaration has its
transitive axiom dependencies inspected. The audit also checks all root imports,
scans the implementation for placeholders and new axiom declarations, and
compares source/pin hashes before and after the audit.

The first independent audit reached all declarations and found no theorem/type
failure, placeholder, or unexpected axiom, but exited 1 because my audit script
specified two unsupported formatting options (`pp.depth`, `pp.width`). Its
actual log, source and evidence are retained as `*-attempt01.*`. The options were
removed, with no implementation source change. The final corrected audit and
SHA256 manifest are `logs/independent-review-types-axioms.log` and
`logs/independent-review-final-evidence.json`. **The final corrected audit exited
0** for all 145 declarations. Only `propext`, `Classical.choice`, and `Quot.sound`
were observed; no `sorryAx`, new project axiom, or implementation placeholder was
found. Source and pin hashes were identical before and after the audit. There are
no remaining review blockers within the stated compiled scope.

Publication notice: reviewer task identity and internal coordination wording were omitted. The original review verdict, scope, failed/corrected audit distinction, source/pin hashes, dates and non-authorship disclosure remain unchanged in meaning. Fresh publication checks are separate.
