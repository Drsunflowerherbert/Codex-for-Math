# Integrated finite-direction core

Let E be a real inner-product space, K a nonempty compact convex set, D a finite
chordal δ-net of the unit sphere, 0 ≤ δ < sqrt(2), ε > 0, and t > 0. Write
N = |D| and assume N exp(-t ε) < 1. Supports are attained maxima on K, and

    Φ(x) = ∑ u∈D exp(t (⟪u,x⟫ - supportValue K u - ε)),
    Ω = {x | Φ(x) < 1}, C = {x | Φ(x) ≤ 1}.

Approximation.lean proves the actual construction is smooth in every order,
strictly convex as a function, and has pointwise positive second derivative on
nonzero vectors. It proves every open chord of C lies in Ω and C is strictly convex
as a set. Ω is open and convex, and K is contained in Ω. The enclosure proof uses
exactly the strict cardinal margin; replacing it with equality would not suffice.

The explicit inner tube is

    {x | infDist(x,K) < ε - log(N)/t} ⊆ Ω.

The radius is positive under the strict cardinal margin. For any anchor p∈K,
a single positively covering direction gives

    exp(t ((1-δ²/2)‖x-p‖ - diam(K) - ε)) ≤ Φ(x).

Thus Φ tends to infinity on the cobounded filter. In a finite-dimensional ambient
space all closed sublevels are compact. Positive ambient dimension is expressed
by Nontrivial E, needed for a nonempty unit-sphere net; K itself may have empty
ambient interior.

Each summand is positive, so Φ(x)≤1 implies every finite support inequality
⟪u,x⟫≤supportValue K u+ε. Quantitative.lean and OuterApprox.lean compose attained
supports and nearest-point normality to obtain

    infDist(x,K), hausdorffDist(C,K)
      ≤ (ε + δ sqrt(1-δ²/4) diam(K))/(1-δ²/2).

The Hausdorff statement uses the proven containment K⊆C. The tangential constant
comes from the unit-vector identity ⟪u,ν⟫=1-‖u-ν‖²/2 and discarding the normal term
only after proving its coefficient is positive.

A strict anchor in K and convexity identify closure Ω=C and frontier Ω={Φ=1}.
The supporting-gradient inequality proves fderiv ℝ Φ x≠0 whenever Φ(x)=1.
These are compiled level and boundary statements. They do not by themselves
provide analytic manifold charts or a sphere parametrization.

Construction.lean selects positive δ, ε and t for arbitrary positive accuracy,
while permitting any prescribed finite unit directions. Nesting.lean packages the
hypotheses in BarrierData and actually recursively chooses each successor error
below half the preceding positive tube margin and below 1/(n+2). The inner tube
then certifies C(n+1)⊆Ω(n). Every C(n) is compact and is closure Ω(n); the errors
and Hausdorff distances tend to zero, and both intersections equal K. Decreasing
parameters alone is never used as an inclusion certificate.

Examples.lean proves a planar segment is nonempty, compact and convex, has diameter
one and empty ambient interior, then applies the actual barrier/error theorems.
Singleton radius corollaries have no diameter term.

# Truthful scope

Compiled scope is the finite-direction exponential barrier, finite nets and support
geometry, exact outer-error bound, arbitrary smooth outer approximation, regular
levels, compact closed sublevels and a certified nested sequence. It is a new
verified core assembled from the recovered drafts and reviewed ordinary proof,
not a claim that the interrupted run already passed.

Deferred: analytic boundary charts/manifold infrastructure and real-analytic sphere
or Jordan parametrizations. No theorem claims a globally uniform strong-convexity
modulus, uniform curvature, optimal net cardinality, or the source's headline result.
All project proofs are complete; deferred obligations appear only in prose.
