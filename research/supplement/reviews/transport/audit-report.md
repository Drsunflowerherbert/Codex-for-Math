# Independent review of the three atom transport obstruction

Reviewed on 11 October 2026. This review covers the local proof, theorem records, exact arithmetic script, fixtures, and the supplied sharpness section. It finds no mathematical correction needed to the stated obstruction, exact formulas, or dimension-one identity. All four original arithmetic cases pass again and reproduce the fixture file byte for byte. The originals are unchanged.

Two separately proved refinements appear in [optional-refinements.md](optional-refinements.md). They are additions to the reviewed results, not silent changes to their hypotheses. The first shows that the fixed first-maximizer selection has a unique induced optimal plan even for singular source measures. The second records the weaker exponent obstruction and essential-supremum discontinuity that persist with fixed positive atom masses.

This is an ordinary mathematical review and a rerun of original exact arithmetic. It does not assess any global upper stability theorem, novelty, repository-wide correctness, or formal proof implementation.

## Material and provenance

The reviewed originals are:

- [proof.md](../../transport-stability/proof.md), 551 lines.
- [theorems.json](../../transport-stability/theorems.json), containing ten mathematical records.
- [check_exact_cases.py](../../transport-stability/check_exact_cases.py), 180 lines.
- [exact-cases.json](../../transport-stability/exact-cases.json), containing four rational cases.
- [The supplied sharpness section](../../catalog/sources/preprints_Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026_build_source_sections_sharpness.tex), read in full.

The local sharpness section has SHA-256 `f8732d68d0de8505d20f6c42aefce95d60b3e8363569681fa30632c997999590`, matching the record. Its stated upstream location is the [sharpness section at revision fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/build/source/sections/sharpness.tex). This review verifies the supplied local bytes and their mathematical content; it does not independently re-fetch the upstream revision or audit the surrounding paper. The original source proves the finite-affine lemma, target formulas for the chosen family, exact W1 and W2 distances, and the W2 exponent obstruction. The general-p, general-q, endpoint-ratio, essential-supremum, and dimension-one statements in the study are additional deductions checked here on their own merits.

## Finite affine duality and uniqueness

The lemma in proof.md lines 63–171 is valid as stated. A finite maximum of affine functions is finite and continuous. Its first-index cells are Borel because they use finitely many strict and non-strict affine inequalities. Repeated slopes can be merged by keeping the largest intercept without changing the function or the selected slope.

For distinct slopes, an equality of their affine values lies in a genuine affine hyperplane. Absolute continuity therefore makes the finite union of such sets null. Outside that union the winning affine function stays strictly above the others locally, and its slope is the gradient. This proves the claimed gradient identity without invoking a general transport existence theorem.

The dual inequality has the correct signs and normalization for the cost |x−y|²:

    phi(x) = |x|² − 2u(x)
    psi(y) = |y|² + 2c(y)
    |x−y|² − phi(x) − psi(y) = 2[u(x) − x·y − c(y)] ≥ 0.

Only values of psi on the finite target support are needed. Bounded slopes and intercepts imply |u(x)| ≤ R|x| + M. A finite source second moment implies a finite first moment; the dual terms and all competing quadratic costs are consequently finite. The graph plan attains equality, so weak duality alone gives optimality. Existence or attainment of a separate abstract dual problem is not required.

For any optimal plan, the nonnegative slack has integral zero and thus vanishes almost everywhere. With null tie hyperplanes, this forces the plan onto the selected graph. A Borel graph-supported plan with first marginal rho is exactly (id,T)#rho, establishing plan uniqueness, not just uniqueness within a chosen map class.

The assumptions are sufficient, with the following distinctions:

- Finite second moment prevents the quadratic problem from degenerating into comparisons of infinite costs.
- Hyperplane nullness is sufficient for the gradient statement and for the written uniqueness proof. In fact, nullness only of the active distinct-slope tie set would suffice for that argument.
- Absolute continuity and bounded or convex source support are not necessary for the narrower optimality claim.
- Under the fixed-priority rule, plan uniqueness can also be proved without tie nullness; see the separate refinement. This does not extend the gradient statement to singular sources.

## Central cells and their masses

Under 0 < b < a and a+b < 1, the half-width h(t)=a+bt is positive and below one for every t in [−1,1]. Hence the two central cells really are A={|x1|<a} and B={|x1|<a+bx2}, with no clipping or missing outer comparison. The source normalization 2^(−d) gives independent coordinates uniform on [−1,1].

For a fixed second coordinate t, the central conditional mass is h(t), while each outer conditional mass is (1−h(t))/2. Integrating against dt/2 yields central mass a and each outer mass m=(1−a)/2 for both targets. All three atoms have positive mass and distinct locations. The d−2 unused coordinates contribute a factor of one after normalization.

On a slice with t>0, B contains A; with t<0, A contains B. Therefore

    rho(B \ A) = b/4,
    rho(A \ B) = b/4,
    rho(A intersection B) = a−b/4.

Reflection in x1 splits each reassigned mass equally between its two sides. Thus the common-source joint matrix is

    [ m−b/8    b/8       0     ]
    [ b/8      a−b/4     b/8   ]
    [ 0        b/8       m−b/8 ].

The matrix is nonnegative, has the prescribed row and column sums, and agrees with the geometry. Null boundaries do not affect any displayed mass or integral.

## Exact target and map distances

For every finite p≥1, the matching target coupling has cost ab^p. Every point in the first target has second coordinate zero, so any coupling has cost at least the integral of |z2|^p against the second target, which is ab^p. Thus Wp^p=ab^p exactly.

Equality in the coordinate lower bound requires all other coordinate differences to vanish. Since the first coordinates −1,0,1 identify the corresponding three atoms uniquely, the matching target coupling is the only optimizer. This is a pointwise equality argument and does not rely on strict convexity of the p-cost; in particular, it works for p=1. For W-infinity the same coordinate lower bound gives b, attained by matching.

The quadratic target cost matrix, in minus/central/plus order, is

    [ 0       1+b²     4 ]
    [ 1       b²       1 ]
    [ 4       1+b²     0 ].

For the maps evaluated at one common source point, the first coordinate changes by absolute value one exactly on A symmetric-difference B; the second-coordinate difference is −b on B. Orthogonality gives

    |T−S|² = 1_(A symmetric-difference B) + b² 1_B,
    ||T−S||_2² = b/2 + ab².

Multiplying the joint matrix by the displayed cost matrix gives the same result. The common-source target coupling is not the optimal target coupling; confusing these two couplings would erase the obstruction.

For finite q≥1, the values of |T−S| on the three nonzero regions are b, 1, and sqrt(1+b²), respectively. Consequently the record

    ||T−S||_q^q = (a−b/4)b^q + (b/4)[1+(1+b²)^(q/2)]

is correct. The essential supremum is sqrt(1+b²), since B\A has positive mass. These facts hold throughout the stated two-parameter range.

## Exponent obstruction and its limits

For b=a/2 with 0<a<1/2,

    Wp = a^(1+1/p)/2,
    ||T−S||_2 = sqrt(a)sqrt(1+a²)/2,
    ||T−S||_2 / Wp^alpha
      = 2^(alpha−1)sqrt(1+a²)a^[1/2−alpha(1+1/p)].

The power of a is negative exactly when alpha>p/[2(p+1)]. This proves the claimed ceilings 1/3 for W2 and 1/4 for W1. The endpoint limits 2^(−2/3) and 2^(−3/4) also have the correct constants.

For each fixed finite q, the first term of the Lq identity is O(a^(q+1)), while the second is asymptotic to a/4. Thus ||T−S||_q is asymptotic to (a/4)^(1/q), giving the claimed necessary ceiling p/[q(p+1)]. No exchange of limits with q tending to infinity is used. The separate essential-supremum computation handles that case.

Dimension, source, source support, target container, and the number of atoms remain fixed. Within each target, pairwise atom distances are at least one. The central mass nevertheless tends to zero, so this particular sequence does not establish the same 1/3 or 1/4 ceilings on classes with a fixed positive lower mass bound.

The endpoint computations establish neither existence nor optimality of a positive global upper estimate. The additional fixed-mass refinement establishes only a different necessary ceiling, 1/2 for L2, and essential-supremum discontinuity. None of these examples supplies a global upper theorem.

## Dimension one

The finite-atomic dimension-one identity in proof.md lines 435–478 is correct. An increasing quantile step map from the uniform interval sends consecutive source intervals to the increasingly ordered target atoms. Extend the step map constantly beyond its outer intervals before integrating on the whole line; this makes explicit the harmless global extension implicit in the proof. Its integral is convex and piecewise affine with finitely many slopes, and is the maximum of its extended affine pieces. The finite-affine lemma proves source-to-target optimality and uniqueness.

For any two finite target laws, choose M containing both supports and set U=Y+M and V=Z+M. The layer-cake identity for E[UV] and the bound

    P(U>s,V>t) ≤ min(P(U>s),P(V>t))

are valid. Under the common quantile coupling, threshold events are nested upper intervals of one uniform variable, up to null endpoints. That coupling attains the bound for every pair of thresholds. It maximizes E[YZ] and therefore minimizes the quadratic cost. Its cost is exactly the same-source map L2 distance squared, proving the claimed identity. The actual source here is uniform and hence absolutely continuous; no unproved higher-dimensional claim about arbitrary atomless sources is being used.

## Sufficiency of the exact three by three enumeration

The script's arithmetic and enumeration methods are appropriate for the four fixtures.

1. Half-plane clipping uses the actual inequalities of the two central and outer cells. Under the parameter restrictions, the displayed single inequality for an outer cell implies its missing comparison with the opposite outer slope. Clipping retains boundary vertices and uses exact rational edge intersections; a zero endpoint is retained on its own outgoing edge. The shoelace sum is twice Euclidean area, so division by eight correctly divides area by the square's area four.
2. The target LP has nine nonnegative variables. Three row sums and the first two column sums are five independent constraints. Independence follows by examining a linear combination on the third-column entries first: all row coefficients vanish, and then both column coefficients vanish. The omitted last column sum follows from the equal total masses and is also checked explicitly.
3. Every vertex has linearly independent positive-support columns. Otherwise a nonzero null vector supported there allows small feasible positive and negative perturbations, contradicting extremality. That independent support can be extended to a five-column basis of the rank-five matrix. Allowing zero basic entries therefore includes degenerate vertices as well as vertices with five positive entries.
4. The script enumerates all 126 five-element subsets of nine columns, solves every invertible basis exactly, rejects negative solutions, and deduplicates the resulting feasible vectors. Singular bases are safely skipped. Hence it does enumerate every vertex of this particular transportation polytope, including the diagonal matching vertex with only three positive entries.
5. The polytope is nonempty and compact. A linear objective attains a minimum at a vertex; every optimal point is a convex combination of optimal vertices. Finding exactly one minimizing vertex therefore establishes uniqueness of the full LP minimizer for each tested instance, not just uniqueness among the enumerated list, once enumeration completeness is justified as above.

The W1 check is a coordinate-projection certificate, not an exhaustive W1 LP solve. That is sufficient: all first-target second coordinates are zero, so the projected cost depends only on the destination marginal, and the explicit matching plan attains the lower bound.

The script does not mechanically derive its half-plane descriptions from arbitrary affine maxima. Their agreement with the potentials was checked in the written review. Nor does it prove formulas for every real a,b, every dimension, or every p,q. The four fixtures all satisfy b=a/2. The two-parameter and higher-dimensional results rest on the written proof. The assertion of ten distinct vertices is scoped to these four inputs; it is not a universal count. For example, at a=1/3 the equal-marginal polytope is a scaled three by three doubly stochastic polytope and has the six scaled permutation vertices.

## Rerun results and recommended disposition

A byte-identical copy of the original script was run with Python 3.12.14 under [rerun/](rerun/). It uses only the standard library. No code was downloaded and no packages were installed. The four cases were a=2/5, 1/4, 1/10, and 1/100, each with b=a/2. Each yielded ten distinct vertices and one minimizing vertex, exactly the matching coupling. The generated JSON is byte-identical to the original. See [stdout.txt](rerun/stdout.txt) and [the regenerated fixtures](rerun/exact-cases.json).

No required mathematical correction is identified. The dimension-one global extension may be spelled out for readers, but it does not change the theorem. A future maintenance edit may replace the theorem JSON's pending independent-review status with a reference to this scoped review. That metadata change has deliberately not been applied to the originals. Keep all existing nonclaims and provenance qualifications, and do not describe this review as validating the paper's headline upper estimate.

The [review record](review-record.json) provides per-result dispositions, source hashes, computational limits, and the separate optional theorem statements.
