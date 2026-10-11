# Finite directions and compact convex geometry

`ConvexApprox/Geometry.lean` reuses Sections 1 and 5 of the recovered reviewed study.
It imports mathlib only, so both the exponential-barrier and quantitative modules
can depend on it without a cycle.

The hypotheses are explicit. Support maxima and nearest-point normality work in an
arbitrary real inner-product space. The set must be nonempty and compact, and the
normality conclusion also requires convexity. No ambient interior, full affine
dimension, or positive diameter is assumed; singletons and lower-dimensional convex
sets are covered by the same statements.

`supportValue K u` is the supremum of the real support functional's image. The
support-value theorems always require nonempty compact `K`, establish attainment,
and bound every member of `K` by this value. Its definition outside those hypotheses
is not used as a geometric support theorem.

`nearest_point_normal` provides a nearest point `w ∈ K`, the equality
`Metric.infDist x K = ‖x - w‖`, and the normal inequality
`⟪x - w, v - w⟫ ≤ 0` for every `v ∈ K`. It uses mathlib's compact attainment and
convex projection characterization. Nearest-point uniqueness is unnecessary.

`IsChordalNet D δ` says all members of the finite set `D` are unit vectors and every
unit vector is within norm distance at most `δ` of a member. In finite dimension,
`exists_chordalNet_containing` constructs such a net for every `δ > 0`, containing
any prescribed finite unit family. This allows adding both signs of coordinate axes
without a choice of coordinate-space API. It uses a finite ball subcover of the
compact unit sphere; it makes no packing-number claim.

The exact unit-direction lower bound is `1 - δ^2/2`. It scales to
`(1 - δ^2/2) * ‖v‖ ≤ ⟪u,v⟫` for a member `u ∈ D` whenever `v ≠ 0`.
When `δ^2 < 2`, this gives a strictly positive inner product, point separation,
and a zero common orthogonal kernel. In finite dimension it proves
`Submodule.span ℝ (D : Set E) = ⊤`.

Positive dimension is represented by `[Nontrivial E]` exactly where needed:
nonemptiness of the net and the theorem `2 ≤ D.card`. The net construction itself
also works in dimension zero, where the unit sphere can be empty. It does not claim
that the zero-dimensional sphere is nonempty or that a net there has two elements.

Fresh verification: `source scripts/environment.sh && lake build ConvexApprox.Geometry`
completed successfully; see `logs/geometry-build-05.log`. The initial unsuccessful
compiler attempts remain saved separately and are not treated as passes.
`logs/geometry-type-axiom-inspection.lean` records an exact type and axiom inspection
of every delivered geometry theorem; its actual compiler output is saved in the
matching `.log`. The only reported axioms are Lean's ordinary `propext`,
`Classical.choice`, and `Quot.sound` (or subsets); no theorem uses `sorryAx` or a new
project axiom.

No analytic manifold, optimal covering size, full coercivity criterion, or curvature
claim is made by this module.
