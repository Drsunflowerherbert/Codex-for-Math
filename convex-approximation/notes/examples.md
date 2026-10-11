# Compiled lower-dimensional examples

`ConvexApprox/Examples.lean` fixes the ordinary Euclidean plane
`EuclideanSpace ℝ (Fin 2)`. Its horizontal segment joins zero to the horizontal
unit vector. The file proves the segment is nonempty, compact, and convex, has
distinct endpoints and diameter exactly one, and has empty ambient interior.
The interior proof perturbs any prospective interior point in the vertical
direction inside an asserted open ball, contradicting its zero vertical coordinate.

The example also proves existence of a finite chordal net containing both signs
of both coordinate axes for every positive net radius. The approximation statements
therefore use an attainable net hypothesis, with the sharper threshold imposed
where a positive denominator is needed.

For this segment, finite support inequalities yield

`infDist x planarSegment ≤ (ε + δ * sqrt (1 - δ^2/4)) / (1 - δ^2/2)`.

The actual finite exponential support barrier additionally has compact closed
sublevels. Under positive scale and the strict cardinal margin, it contains the
segment in its open level-one sublevel and satisfies the same Hausdorff bound.
All parameters and the cardinal margin appear explicitly in the theorem types.

For a singleton `{p}` in the plane, the support inequality and actual barrier
sublevel corollaries give `‖x - p‖ ≤ ε / chordalCos δ`. This is an exact specialization
of the compiled general bound: the diameter term is zero. No interval formula,
hyperbolic-function optimization, or numerical check is used as evidence for these
Lean examples.

The successful final examples build and exact theorem type/axiom inspection are
saved in `logs/geometry-examples-build-03.log` and
`logs/geometry-examples-type-axiom-inspection.log`. Earlier saved passes cover the
standalone support-inequality examples before the actual barrier corollaries were
added. The final build imports `ConvexApprox.Approximation`, so the actual barrier
examples are checked against the delivered connected core.
