# Future Lean roadmap for analytic convex approximation

## Status and recommended first target

No Lean file has been created, imported, compiled, or kernel-checked for this study. No Mathlib API names or coverage have been verified. The labels below describe desired interfaces and milestones, not existing declarations. Do not replace difficult steps by new axioms or `sorry` and then describe the result as verified.

The best first formalization target is the quantitative finite-barrier core: containment, coercivity, convexity, compact closed sublevels, and the Hausdorff error. It is useful independently of the analytic Jordan-boundary conclusion and should be substantially more self-contained than the analytic implicit-function/manifold layer.

## Representation choices

Use a finite-dimensional real inner-product space \(E\), or start concretely with \(E=\mathbb R^d\), \(d\geq1\). Keep the angular radius and support slack as distinct parameters. A finite indexed family of directions is convenient for differentiating a finite sum, but distinguish it from a finite set: duplicates alter \(N\), the barrier, and the logarithmic interior margin. Either require injectivity of the family or consistently use its index cardinality.

One reusable intermediate hypothesis is a positive directional-cover constant:

- every direction \(u_i\) has norm one;
- \(c>0\);
- for every unit \(v\), some \(i\) has \(\langle u_i,v\rangle\geq c\).

The chordal-net theorem then derives this hypothesis with \(c=1-\delta^2/2\). This separates geometry of sphere nets from analytic properties of the barrier and avoids entangling square-root algebra with the first proof.

For support values, use the maximum of the continuous function \(x\mapsto\langle u,x\rangle\) on the nonempty compact set \(K\). Package both its upper-bound property and an attaining witness. Avoid relying on an unproved simplification of a supremum over an empty or unbounded image.

## Milestone 1 Finite nets and elementary identities

Prove or locate after inspecting the actual library:

1. Compactness of the unit sphere in a finite-dimensional real inner-product space.
2. Existence of a finite \(\delta\)-net for \(\delta>0\).
3. The unit-vector identity \(\langle u,v\rangle=1-\|u-v\|^2/2\).
4. A positive directional-cover constant implies spanning and nonempty index type.
5. It also implies at least two directions when \(d\geq1\), needed for the convenient \(2\log N/\varepsilon\) parameter choice.

The packing/cardinality estimate is optional and should not block the approximation theorem.

## Milestone 2 Barrier inequalities and compactness

Define the finite exponential sum explicitly. Prove positivity of every summand and the following reusable inequalities before using derivatives:

- \(\Phi(k)\leq N e^{-t\varepsilon}\) for \(k\in K\);
- \(\Phi(x)\leq N e^{t(\operatorname{dist}(x,K)-\varepsilon)}\);
- \(\Phi(x)\geq e^{t(c\|x-p\|-R_p-\varepsilon)}\) for fixed \(p\in K\);
- \(\Phi(x)\leq1\Rightarrow\langle u_i,x\rangle\leq h_K(u_i)+\varepsilon\).

Handle logarithm/exponential equivalences only under explicit \(t>0\), \(N>0\), and \(\varepsilon>0\) hypotheses. Derive continuity, boundedness of the closed level-one sublevel, and its compactness. The proof of coercivity can be represented first as the explicit lower bound, which is enough for subsequent compactness and radial existence.

## Milestone 3 Projection-normal geometry and error

For \(x\notin K\), obtain a nearest \(w\in K\) by compact minimization. Use the segment (w+a(v-w)) and expand the squared distance to prove

\[
\langle x-w,v-w\rangle\leq0\quad(v\in K).
\]

A general theorem about metric projection onto closed convex sets may be reusable if its exact assumptions are checked, but it is not necessary to use uniqueness or infinite-dimensional Hilbert-space projection machinery.

Next prove the simple bound

\[
\operatorname{dist}(x,K)\leq
\frac{\varepsilon+\delta\operatorname{diam}K}{1-\delta^2/2}.
\]

Guard division by \(\operatorname{dist}(x,K)>0\) and \(1-\delta^2/2>0\). Treat \(x\in K\) separately. After this milestone is complete, optionally formalize the sharper tangential decomposition \(u=a\nu+b\), \(b\perp\nu\), and its bound \(\|b\|\leq\delta\sqrt{1-\delta^2/4}\).

Package the result as a pointwise distance bound before moving to Hausdorff distance. This avoids unnecessary extended-real or empty-set cases in a Hausdorff-distance API. Only then use \(K\subset C\) and compact nonemptiness to identify the one-sided excess with the Hausdorff distance.

## Milestone 4 Convexity and boundary identities

Two reasonable proof routes exist:

- derive convexity directly from convexity of the scalar exponential composed with affine maps;
- calculate first and second derivatives, prove the Hessian quadratic form is positive, and obtain strict convexity by restriction to a line.

For strict convexity, the line-restriction proof has a transparent nonzero-direction hypothesis and avoids an unexplained matrix criterion. For an abstract inner-product space, represent the Hessian as a continuous bilinear form rather than prematurely choosing a matrix basis.

Prove

\[
\overline{\{\Phi<1\}}=\{\Phi\leq1\}
\]

by the explicit interpolation with a point of \(K\). This is a reusable lemma for a continuous convex function whose strict sublevel is nonempty. Derive the frontier identity afterward. Prove the strong strict-convexity statement that open chords between distinct closed-sublevel points lie in the open sublevel.

## Milestone 5 Nesting and continuous maxima

With the quantitative core available, nesting can be completed without analytic geometry:

1. Prove positive distance from a nonempty compact subset \(K\) to the complement of an open neighborhood.
2. Show a new closed outer neighborhood of error less than that distance lies in the previous open neighborhood.
3. Choose parameters recursively, either using the abstract distance or the explicit inner margin \(\eta_j\).
4. Prove errors tend to zero and both intersections equal \(K\).

The explicit geometric parameter schedule in study.md avoids a recursive choice of unknown distances and provides an independently checkable inclusion margin. The continuous-maxima consequence only needs uniform continuity on a common compact set and nearest points; it can be formalized before any smooth-boundary result.

## Milestone 6 Regular analytic boundary and radial topology

This is the main library-dependency risk. First inspect what the selected Lean/Mathlib revision actually offers for real analyticity, the real-analytic implicit function theorem, embedded submanifolds, analytic maps on spheres, and diffeomorphisms. Do not assume that a smooth inverse-function result automatically supplies real analyticity.

The proof can be decomposed into independent layers:

1. Finite sums of exponentials of affine maps are real analytic.
2. The supporting-gradient inequality implies \(\langle\nabla\Phi(x),x-p\rangle\geq1-\Phi(p)>0\) on the boundary.
3. For each unit \(v\), the scalar radial function has exactly one positive level-one root, by coercivity, the intermediate value theorem, and convexity.
4. Establish continuity of the root function and a homeomorphism with the sphere. One can use a direct quantitative/local argument or an appropriate implicit-function theorem whose hypotheses have been checked.
5. Apply the real-analytic implicit function theorem with nonzero radial derivative to obtain local analytic radius functions; glue by uniqueness.
6. Use the analytic radial projection as the inverse and verify the derivative of the parametrization is injective on tangent spaces.

For the planar specialization, a concrete regular periodic parametrization \(\gamma(a)=p+\rho(\cos a,\sin a)(\cos a,\sin a)\) may be less expensive than a general analytic-manifold interface. Prove its derivative norm squared is \(\rho'^2+\rho^2>0\) and injectivity modulo \(2\pi\). State explicitly which formal notion of “Jordan curve” is being used.

For \(d=1\), use the interval formula or the two-root argument. Do not force it through a connected-sphere or Jordan-curve lemma: \(S^0\) has two points.

## Suggested proof delivery sequence

1. A compiled finite-barrier core with a simple quantitative error bound.
2. A compiled nesting and continuous-maxima extension.
3. A compiled regular \(C^1\) or smooth boundary theorem if that is supported by the inspected infrastructure, labeled at its actual regularity level.
4. A separate real-analytic boundary and analytic sphere-parametrization theorem once the analytic IFT dependencies are available and checked.

Do not report the whole source lemma as Lean-verified if only the metric/convexity core compiles. Record the exact source revision, Lean version, dependency lock state, command, result, and theorem names for any future actual verification.
