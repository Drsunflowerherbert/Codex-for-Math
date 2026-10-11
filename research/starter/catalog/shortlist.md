# Six reusable mathematical study targets

Source revision: fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb. All are proposed study scopes, not certified results or novelty claims.

## Family025: Exact-length Egyptian fractions and marker-preserving padding

For an integer k≥1, if 0<x<1 is a sum of exactly k positive integer-denominator unit fractions, then x has an exactly-k-term expansion with pairwise distinct integer denominators, all ≥2. Companion: if 1=Σ(i=1..r)1/n_i with 2≤n_1<⋯<n_r and r≥3, any chosen denominator m among the n_i can be retained in a distinct exactly-(r+1)-term expansion of 1.

Source: [elementary.tex, Lemma lem:distinct; prescribed.tex, Lemma lem:exact-marker-padding](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/build/elementary.tex).

### Prerequisites

- Induction and finite sorted denominator lists
- Elementary divisibility and prime/composite cases
- Well-founded termination via a finite-state increasing potential

### Expected reusable result

Independent proof, exact rational tests, a terminating rewrite specification, and boundary/collision cases including x=1 and a marked largest denominator.

**Bridge:** Number theory ↔ finite combinatorial rewriting and termination.

**Boundary:** Does not establish the manuscript's O(log log b) upper bound; these lemmas are classical/attributed supporting results.

**Formal scope:** Family025 scope lists short expansion, counting, and prescribed-denominator statements. Not compiled or matched to the individual lemma in this run.
[Scope note](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/025.md).

## Family084: Normalized periodic hitting implies global affine avoidance

Fix q∈(0,1). Suppose for each p∈(0,1) there exists open 1-periodic H⊂R, of density ρ(H)≤6p, such that every x∈R and t∈[1,2] has x+tq^n∈H for some n≥1. Then for every η∈(0,1) there exists compact E⊂[0,1] with m(E)>1−η and, for every x∈R and s≠0, some n≥1 satisfies x+sq^n∉E. The source uses p_k=(η/64)4^{−|k|}, C=⋃(k∈Z)(2^kH_k∪−2^kH_k), and m(C∩[0,1])≤7η/16.

Source: [02-periodic.tex, proof of main theorem assuming Proposition prop:periodic](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/build/sections/02-periodic.tex).

### Prerequisites

- Lebesgue measure and countable subadditivity
- Periodic density under dilation
- Dyadic normalization of a nonzero real scale
- Compactness of a closed subset of [0,1]

### Expected reusable result

Independent proof and generalized reduction for a prescribed null sequence or scale family, with explicit summable budgets. Keep construction of normalized hitting sets as a hypothesis.

**Bridge:** Analysis ↔ topology: measure budgeting, periodicity, and compact complements.

**Boundary:** Only the reduction is studied; existence of normalized hitting sets is a major separate premise.

**Formal scope:** Family084 Lean note covers only the September25 dyadic manuscript q=1/2, not this October5 arbitrary-q manuscript.
[Scope note](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/084.md).

## Family322: Radial contact in normed balls

Let X be a nonzero real normed space and ||c||<1. For every v∈S_X, the ray c+R_+v meets S_X at a unique c+ρ(v)v, with 1−||c||≤ρ(v)≤1+||c||. The radius function ρ:S_X→(0,∞) is continuous.

Source: [main.tex, Lemma lem:radial; supporting-functionals Lemma lem:support](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/build/main.tex).

### Prerequisites

- Norm convexity and triangle inequality
- One-dimensional intermediate value arguments
- Supporting functionals for a quantitative extension

### Expected reusable result

Independent proof, a quantitative modulus/Lipschitz bound with explicit dependence on distance of c to the boundary, and examples showing why the interior hypothesis matters.

**Bridge:** Topology of radial parametrizations ↔ convexity and Banach-space inequalities.

**Boundary:** No general Tingley extension theorem or alignment proposition is assumed or certified.

**Formal scope:** Family322 claims a unique real-linear extension for arbitrary nonzero real Banach spaces; the scope is real, not complex linearity. No Lean run performed.
[Scope note](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/322.md).

## Family374: Three-atom transport obstruction with exact distances

Let d≥2, ρ be uniform on [-1,1]^d, 0<a<1/2 and b=a/2. Put u_a=max{−x_1,x_1,a} and v_a=max{−x_1,x_1,a+bx_2}. Their gradient laws are μ_a=((1−a)/2)(δ_{−e1}+δ_{e1})+aδ_0 and ν_a=((1−a)/2)(δ_{−e1}+δ_{e1})+aδ_{be2}. The gradients are the unique quadratic optimal maps to their laws, W_2(μ_a,ν_a)^2=ab², W_1(μ_a,ν_a)=ab, and ||T_μa−T_νa||²_L2(ρ)=b/2+ab². Hence no uniform estimate with exponent α>1/3 can hold on this fixed source and target cube, even for three-atom targets.

Source: [sharpness.tex, Lemma cells:optimality and Proposition sharpness:exponent](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/build/source/sections/sharpness.tex).

### Prerequisites

- Finite maxima of affine functions and null hyperplanes
- Elementary Kantorovich dual inequality for a finite target
- Explicit transport couplings
- Fubini and slice probabilities on a cube

### Expected reusable result

Verify the identities directly; extract a reusable tilted-cell obstruction template. Separate this counterexample from the global one-third upper-bound proof.

**Bridge:** Convex analysis ↔ probability, optimal transport, and sharp Hölder exponents.

**Boundary:** The explicit lower-bound obstruction is independent of the claimed uniform global upper bound.

**Formal scope:** Family374 scope claims both one-third stability and the three-atom sharpness result; no local formal check performed.
[Scope note](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/374.md).

## Family005: Mixed moments and Taylor-contact cancellation

For nonnegative integers i,j define M(i,j)=∫_{−1}^1∫_0^1 [|t|/√(1−t²)]t^i s^j/(1−ts) ds dt and Z(i,j)=∫_0^1∫_0^1 t^i s^j/(1−ts) ds dt. Extend bilinearly to polynomials. Let G=Σ(j≥0)(−1)^j/(2j+1)². If P,D∈Q[t], L≥1 is an integer and tP(t)/√(1−t²)−D(t)=O(t^L) at t=0, then for every integer 0≤j<L, M(P,j)−(3/2)Z(D,j) belongs to Q+QG. Supporting identity: Z(i,i)=ζ(2)−H_i^(2), while Z(i,j)=(H_i−H_j)/(i−j) for i≠j.

Source: [foundations.tex, equations rational-decomposition and contact; Proposition prop:rationality (the polynomial-generalized lemma is an extraction)](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/foundations.tex).

### Prerequisites

- Absolute convergence and justified termwise integration
- Beta-type moments and central binomial coefficients
- Rational recurrences and harmonic numbers
- Taylor coefficient matching

### Expected reusable result

Verify mixed-moment recurrences and the two boundary constants, then prove the general cancellation lemma. Exact rational low-index checks may detect indexing errors; keep G symbolic.

**Bridge:** Real analysis ↔ rational arithmetic, special functions, and symbolic elimination.

**Boundary:** This is not a proof of Catalan's irrationality. The determinant, valuation, nonvanishing and energy arguments remain outside the study.

**Formal scope:** Family005 scope claims irrationality of Catalan's constant. The extracted generalized cancellation lemma has not been identified as a formal declaration here.
[Scope note](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/005.md).

## Family325: Positive-block energy and convex outer approximation

Primary lemma: if Δ=[[A,B],[B*,C]] is a finite complex positive-semidefinite block matrix, then 2||B||²_HS≤||A||²_HS+||C||²_HS. Scaling gives the stronger product bound ||B||²_HS≤||A||_HS||C||_HS. Companion target: every nonempty compact convex K⊂C has bounded open convex real-analytic Jordan neighborhoods Ω_δ with K⊂Ω_δ and sup(z∈closure Ω_δ)dist(z,K)≤δ(1+diam K)/(1−δ), for 0<δ<1, via finite direction nets and a log-sum-exp support barrier.

Source: [main.tex, section sec:matrix, 'The positive block comparison'; Lemma lem:approx and its proof](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/build/main.tex).

### Prerequisites

- Positive-semidefinite matrices, trace cyclicity and Hilbert–Schmidt norm
- Congruence and one-variable optimization for the product bound
- For the companion: support functions, finite sphere nets, convexity and the implicit function theorem

### Expected reusable result

Independent block-inequality proof with dimension-independent constants and equality/zero-block checks. Optionally extract the outer-approximation argument as a reusable planar topology/analysis lemma.

**Bridge:** Matrix inequalities ↔ noncommutative analysis; convex geometry ↔ smooth approximation.

**Boundary:** Neither supporting lemma establishes the complete Crouzeix constant-two theorem.

**Formal scope:** Family325 scope lists finite and infinite-dimensional inequalities and supporting statements. No build or exact support-lemma formal match performed.
[Scope note](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/325.md).

