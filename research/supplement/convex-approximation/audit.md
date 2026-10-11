# Audit of finite-exponential analytic convex outer approximation

## Scope and result

This is a local audit and an elementary extension of the source lemma “Analytic convex outer approximation,” in `preprints_A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026_build_main.tex`, lines 457–511. It does not evaluate any other claim in that source. The arguments below use the displayed construction and direct reasoning; they make no novelty or formal-verification claim.

The proposed extension is valid, provided its parameters include **d ≥ 1, ε > 0, and 0 ≤ δ < √2**. A finite Euclidean δ-net of the unit sphere already supplies the directional hypotheses for coercivity and a positive-definite Hessian; adding coordinate axes is unnecessary. For d ≥ 2, a finite 0-net does not exist, so the δ = 0 endpoint is relevant only in dimension one.

Let K ⊂ ℝᵈ be nonempty, compact, and convex, let L = diam K, and let D ⊂ Sᵈ⁻¹ be a finite δ-net. Write N = |D| and

\[
 h_K(u)=\max_{k\in K}\langle u,k\rangle,
 \qquad c=1-\delta^2/2>0,
 \qquad s=\delta\sqrt{1-\delta^2/4}.
\]

Choose t > log N/ε and set

\[
 \Phi(x)=\sum_{u\in D}
 \exp\!\bigl(t(\langle u,x\rangle-h_K(u)-\varepsilon)\bigr),
 \qquad \Omega=\{\Phi<1\}.
\]

Then Ω is a bounded, nonempty, strictly convex open set containing K. Its closure is {Φ ≤ 1}. Its boundary is a regular real-analytic hypersurface, analytically diffeomorphic to Sᵈ⁻¹. In dimension one the latter statement means the boundary consists of two points. Moreover,

\[
 d_H(K,\overline\Omega)
 =\sup_{x\in\overline\Omega}\operatorname{dist}(x,K)
 \le \frac{\varepsilon+sL}{c}
 \le \frac{\varepsilon+\delta L}{1-\delta^2/2}.
\]

All of this remains valid when K has empty interior, including when K is a singleton.

## 1. The net condition gives positive spanning

For every unit vector v, choose u ∈ D with ‖u − v‖ ≤ δ. Since u and v are unit vectors,

\[
 \langle u,v\rangle
 =1-\tfrac12\|u-v\|^2\ge c>0.
\]

In particular, max(u ∈ D) ⟨u,v⟩ ≥ c uniformly in v. This implies that D spans ℝᵈ and that 0 lies in the interior of conv D. Equivalently, the convex hull of D contains the centered closed ball of radius c. The last formulation follows by comparing support functions, or by separating a point outside conv D.

Only the directional inequality is needed in the proofs below. The restriction δ < √2 makes its constant positive.

## 2. Inclusion, the inner tube, and full coercivity

For every k ∈ K, each summand of Φ(k) is at most e⁻ᵗε, so

\[
 \Phi(k)\le Ne^{-t\varepsilon}<1.
\]

Thus K ⊂ Ω, and Ω has nonempty ambient interior even if K does not.

There is a quantitative interior margin. Put

\[
 \eta=\varepsilon-\frac{\log N}{t}>0.
\]

For x ∈ ℝᵈ choose k ∈ K nearest to x and let r = ‖x − k‖. Since h_K(u) ≥ ⟨u,k⟩,

\[
 \Phi(x)\le N\exp(t(r-\varepsilon)).
\]

Consequently,

\[
 \{x:\operatorname{dist}(x,K)<\eta\}
 =K+B_{\mathrm{open}}(0,\eta)\subset\Omega,
 \qquad \operatorname{dist}(K,\Omega^c)\ge\eta.
\]

For full coercivity, fix k₀ ∈ K. If x = k₀ + rv with r ≥ 0 and ‖v‖ = 1, choose u ∈ D with ⟨u,v⟩ ≥ c. Also,

\[
 h_K(u)-\langle u,k_0\rangle
 =\max_{k\in K}\langle u,k-k_0\rangle\le L.
\]

One summand therefore gives the global lower bound

\[
 \Phi(x)\ge\exp\!\bigl(t(c\|x-k_0\|-L-\varepsilon)\bigr).
\]

It follows that Φ(x) → +∞ as ‖x‖ → ∞, uniformly over directions. This is full coercivity, not merely boundedness of the level-one sublevel. Every finite sublevel is compact. For example,

\[
 \{\Phi\le1\}\subset
 \overline B\!\left(k_0,\frac{L+\varepsilon}{c}\right).
\]

## 3. Hessian, strict convexity, and the closed sublevel

The function Φ is real analytic, and

\[
 \nabla^2\Phi(x)
 =t^2\sum_{u\in D}
 e^{t(\langle u,x\rangle-h_K(u)-\varepsilon)}uu^{\mathsf T}.
\]

For every nonzero v,

\[
 v^{\mathsf T}\nabla^2\Phi(x)v
 =t^2\sum_{u\in D}
 e^{t(\langle u,x\rangle-h_K(u)-\varepsilon)}
 \langle u,v\rangle^2>0,
\]

because D spans ℝᵈ and all weights are positive. Thus the Hessian is positive definite everywhere and Φ is strictly convex. Its sublevel Ω is convex and therefore connected.

Continuity gives closure Ω ⊂ {Φ ≤ 1}. For the converse, choose p ∈ K ⊂ Ω. If Φ(x) ≤ 1, then for 0 ≤ λ < 1,

\[
 \Phi((1-\lambda)p+\lambda x)
 \le(1-\lambda)\Phi(p)+\lambda\Phi(x)<1.
\]

Letting λ increase to 1 proves x ∈ closure Ω. Hence

\[
 \overline\Omega=\{\Phi\le1\},\qquad
 \partial\Omega=\{\Phi=1\}.
\]

The second identity follows since {Φ < 1} is open and every point of {Φ = 1} is in the closure but not in Ω. Strict convexity of Φ also proves strict convexity of the body: the open segment between any two distinct points of closure Ω lies in Ω.

On the compact closure Ω, the least Hessian eigenvalue has a positive lower bound. This compact-set conclusion must not be silently upgraded to a global uniform lower bound; see the cautions below.

## 4. Regularity and an analytic radial sphere parametrization

A critical point of a differentiable convex function is a global minimizer. Since some point of K has Φ-value below 1, ∇Φ cannot vanish at a point where Φ = 1. The analytic implicit function theorem therefore makes the boundary a regular real-analytic hypersurface.

Fix any p ∈ Ω. For v ∈ Sᵈ⁻¹, let fᵥ(r) = Φ(p + rv), r ≥ 0. This function starts below 1, is continuous, and tends to +∞ by coercivity. It therefore reaches 1 at some positive radius ρ(v).

At any positive root r of fᵥ(r) = 1, the supporting-line inequality for a differentiable convex function gives

\[
 f_v'(r)\ge\frac{f_v(r)-f_v(0)}r
 =\frac{1-\Phi(p)}r>0.
\]

Because fᵥ is convex, its derivative is nondecreasing; after such a root it stays positive. Hence there is exactly one positive root. In particular, at the boundary point x = p + ρ(v)v,

\[
 \langle\nabla\Phi(x),v\rangle
 \ge\frac{1-\Phi(p)}{\rho(v)}>0.
\]

This is the additional transversality needed for analytic radial parametrization. Define

\[
 F(v,r)=\Phi(p+rv)-1.
\]

In every analytic coordinate chart of Sᵈ⁻¹, F is real analytic, and its derivative in r is strictly positive at r = ρ(v). The analytic implicit function theorem gives a locally real-analytic radius function. Uniqueness patches these local functions into a global positive real-analytic ρ on the sphere. Thus

\[
 R:S^{d-1}\longrightarrow\partial\Omega,
 \qquad R(v)=p+\rho(v)v
\]

is an analytic bijection. Its inverse is the analytic radial projection

\[
 x\longmapsto\frac{x-p}{\|x-p\|},
\]

which is well defined near the boundary because p is interior. Therefore R is an analytic diffeomorphism. In dimension two this supplies a regular analytic Jordan parametrization, for example θ ↦ p + ρ((cos θ, sin θ))(cos θ, sin θ).

For d ≥ 2, the second fundamental form for the outward normal, with the convention that spheres have positive curvature, is

\[
 \mathrm{II}_x(w,w)
 =\frac{w^{\mathsf T}\nabla^2\Phi(x)w}{\|\nabla\Phi(x)\|}
 \quad(w\in T_x\partial\Omega).
\]

It is positive definite. Thus the constructed boundary has positive principal curvatures, a conclusion stronger than absence of boundary line segments.

## 5. Hausdorff estimate and the tangential improvement

Let x ∈ closure Ω \ K. Choose its nearest point w ∈ K, put r = ‖x − w‖ > 0, and ν = (x − w)/r. Convexity of K and minimality of w imply

\[
 \langle\nu,v-w\rangle\le0\qquad(v\in K).
\]

For completeness, expand ‖x − (w + q(v − w))‖² ≥ ‖x − w‖² for 0 < q ≤ 1, divide by q, and let q decrease to zero.

Choose μ ∈ D with ‖μ − ν‖ ≤ δ, and choose v ∈ K attaining h_K(μ). Since Φ(x) ≤ 1, each positive summand is at most 1; hence

\[
 \langle\mu,x\rangle\le h_K(\mu)+\varepsilon
 =\langle\mu,v\rangle+\varepsilon.
\]

Writing a = ⟨μ,ν⟩ ≥ c gives

\[
 ar=\langle\mu,x-w\rangle
 \le\langle\mu,v-w\rangle+\varepsilon.
\]

The immediate bound uses

\[
 \langle\mu,v-w\rangle
 =\langle\nu,v-w\rangle+
 \langle\mu-\nu,v-w\rangle\le\delta L,
\]

and proves exactly the proposed estimate r ≤ (δL + ε)/c.

For the improvement, decompose μ = aν + b with b perpendicular to ν. Since a ≥ c > 0, the normal contribution remains nonpositive. Also,

\[
 \|b\|=\sqrt{1-a^2}
 \le\sqrt{1-c^2}
 =\delta\sqrt{1-\delta^2/4}=s.
\]

Consequently,

\[
 \langle\mu,v-w\rangle
 =a\langle\nu,v-w\rangle+\langle b,v-w\rangle
 \le sL,
 \qquad r\le\frac{\varepsilon+sL}{c}.
\]

The remaining points of closure Ω lie in K and have distance zero. Since K ⊂ closure Ω, the one-sided bound is exactly a bound on Hausdorff distance.

## 6. Convergence and certified nesting

For arbitrary finite nets Dⱼ with δⱼ → 0, and arbitrary εⱼ → 0 satisfying the displayed positivity assumptions, choose any tⱼ > log |Dⱼ|/εⱼ. Then the preceding estimate implies d_H(K, closure Ωⱼ) → 0. No compatibility between the nets and no special tuning of tⱼ is needed for convergence.

This construction does not automatically make Ωⱼ nested. It does permit an explicit recursive nesting choice. Once Ωⱼ is fixed, put ηⱼ = εⱼ − log |Dⱼ|/tⱼ > 0. Choose the next parameters so that their certified outer error Eⱼ₊₁ satisfies

\[
 E_{j+1}<\eta_j/2.
\]

Then every point of closure Ωⱼ₊₁ has distance at most Eⱼ₊₁ from K, whereas Ωⱼ contains every point of distance less than ηⱼ. Thus

\[
 \overline\Omega_{j+1}\subset\Omega_j,
 \qquad
 \operatorname{dist}(\overline\Omega_{j+1},\Omega_j^c)
 \ge\eta_j-E_{j+1}>\eta_j/2.
\]

For the distance inequality, choose a nearest point in K to the point of closure Ωⱼ₊₁ and use the reverse triangle inequality against any point of Ωⱼᶜ. To ensure convergence as well as nesting, also require Eⱼ₊₁ < 2⁻ʲ, or any prescribed sequence tending to zero. These parameter choices exist because the explicit error tends to zero with δ and ε.

## 7. Ball geometry improves the angular order

Let K = closure B(a,R), R ≥ 0. Then h_K(u) = ⟨u,a⟩ + R. For x = a + rv in closure Ω, choose u ∈ D with ⟨u,v⟩ ≥ c. The individual support inequality gives rc ≤ R + ε. Therefore

\[
 d_H(\overline B(a,R),\overline\Omega)
 \le\frac{R+\varepsilon}{c}-R
 =\frac{\varepsilon+R\delta^2/2}{1-\delta^2/2}.
\]

For balls, the angular discretization error is quadratic in δ. Substitution of diam K = 2R in the general bound would miss this improvement.

For a more exact directional statement, let m(v) = max(u ∈ D) ⟨u,v⟩, and let r(v) be the boundary radius from a. It is the unique positive solution of

\[
 \sum_{u\in D}e^{t r(v)\langle u,v\rangle}
 =e^{t(R+\varepsilon)}.
\]

The elementary maximum/sum bounds imply

\[
 \frac{R+\varepsilon-\log N/t}{m(v)}
 \le r(v)\le\frac{R+\varepsilon}{m(v)}.
\]

The numerator in the lower bound is positive by the assumed choice of t.

## 8. Exact singleton and dimension-one examples

### Arbitrary direction set and a singleton

For K = {a}, the construction translates to

\[
 \Omega-a=\left\{y:\sum_{u\in D}e^{t\langle u,y\rangle}<e^{t\varepsilon}\right\}.
\]

Its radial boundary is exactly characterized by the preceding equation with R = 0. It need not be centered or centrally symmetric: ∇Φ(a) = t e⁻ᵗε Σ(u ∈ D)u, so a is the minimizer precisely when Σu = 0. Even vanishing of this vector sum does not by itself imply central symmetry.

Define the exact directional constant

\[
 c_D=\min_{v\in S^{d-1}}\max_{u\in D}\langle u,v\rangle>0.
\]

With D and ε fixed, the directional bounds above give

\[
 \frac{\varepsilon-\log N/t}{c_D}
 \le d_H(\{a\},\overline\Omega)
 \le\frac{\varepsilon}{c_D}.
\]

Hence this Hausdorff distance tends to ε/c_D as t → ∞. If δ is the actual covering radius of D, then c_D = 1 − δ²/2. Thus the singleton version of the proposed δ-only bound is asymptotically sharp.

### Coordinate directions: closed formulas

For D = {±e₁, …, ±e_d}, N = 2d and c_D = 1/√d. For K = {a}, the boundary equation becomes

\[
 \sum_{i=1}^d\cosh(t(x_i-a_i))=\frac{e^{t\varepsilon}}2.
\]

Its exact outer Euclidean radius, hence its exact Hausdorff distance from {a}, is

\[
 R_{\mathrm{out}}=
 \frac{\sqrt d}{t}\operatorname{arcosh}
 \left(\frac{e^{t\varepsilon}}{2d}\right).
\]

To verify the maximum, the function q ↦ cosh(t√q) is convex on q ≥ 0: its power series is Σₙ≥₀ t²ⁿqⁿ/(2n)!, with nonnegative second derivative. Jensen's inequality gives

\[
 \sum_i\cosh(ty_i)
 \ge d\cosh\!\left(t\|y\|/\sqrt d\right),
\]

with equality when all |yᵢ| are equal. These equal-coordinate points achieve the displayed radius. In particular R_out → √d ε as t → ∞.

The exact inradius is

\[
 R_{\mathrm{in}}=\frac1t\operatorname{arcosh}
 \left(\frac{e^{t\varepsilon}}2-d+1\right).
\]

Indeed, at fixed ‖y‖, the same convex function has maximal sum when all squared length is concentrated in one coordinate; the maximum is cosh(t‖y‖) + d − 1. Both arcosh arguments are greater than 1 because eᵗε > 2d.

For K = closure B(a,R) with the same coordinate directions, replace ε in both radius formulas by R + ε. In particular the exact Hausdorff error is

\[
 \frac{\sqrt d}{t}\operatorname{arcosh}
 \left(\frac{e^{t(R+\varepsilon)}}{2d}\right)-R.
\]

### Dimension one

If d = 1 and δ < √2, the sphere is S⁰ = {−1,1}, and every finite δ-net is exactly D = {−1,1}. Let K = [a,b], m = (a+b)/2, and L = b − a, allowing a = b. Then

\[
 \Phi(x)=2e^{-t(L/2+\varepsilon)}\cosh(t(x-m)).
\]

The open set is the interval (m − r,m + r), where

\[
 r=\frac1t\operatorname{arcosh}
 \left(\frac{e^{t(L/2+\varepsilon)}}2\right),
 \qquad
 d_H(K,\overline\Omega)=r-L/2.
\]

This error is positive and strictly less than ε. Positivity follows from eᵗε > 2 > 1 + e⁻ᵗᴸ; the upper bound follows from arcosh(eᴬ/2) < A for A > log 2. The two boundary points are a regular real-analytic zero-dimensional manifold, diffeomorphic to S⁰. Calling them a Jordan curve would be incorrect.

## 9. Linear angular error cannot be removed for arbitrary K

Define the finite-support polytope

\[
 P_0=\{x:\langle u,x\rangle\le h_K(u)\text{ for every }u\in D\}.
\]

Every point of P₀ has Φ-value at most Ne⁻ᵗε < 1, so **P₀ ⊂ Ω**. Any error already caused by finitely many support directions survives, regardless of how ε and t are tuned.

For an explicit flat-set example, take K = [−a,a] × {0}, a > 0. Choose an integer m divisible by 4, set θ = π/m, and let D consist of the m directions with angles (2j+1)π/m, 0 ≤ j < m. The directions nearest to each vertical normal straddle it at angles ±θ. The exact covering radius is δ = 2 sin(θ/2). The point

\[
 x_\theta=(0,a\tan\theta)
\]

belongs to P₀. In fact the positive-y support constraints require y ≤ a|u₁|/u₂, and their minimum is a tan θ; constraints with u₂ ≤ 0 are automatic for this point. Therefore xθ ∈ Ω and

\[
 d_H(K,\overline\Omega)\ge a\tan\theta
 =\tfrac12(\operatorname{diam}K)\tan\theta.
\]

As m → ∞, θ is asymptotic to δ. Hence a universal O(δ² diam K + ε) bound is impossible without additional geometry. This example explains why the ball estimate is a genuine special case.

## 10. Critical assumptions and false generalizations

1. **The net threshold matters.** At δ = √2 in ℝ², D = {±e₁} is a δ-net. For K = {0} and t > log 2/ε, Φ(x,y) = 2e⁻ᵗε cosh(tx). Its level-one sublevel is an unbounded strip and its Hessian is singular. Thus the bare δ-net hypothesis at this threshold cannot imply the theorem.

2. **Spanning and positive spanning are different.** The Hessian is positive definite exactly when span D = ℝᵈ. Coercivity holds exactly when 0 is interior to conv D. Necessity of the latter follows from separation: otherwise some nonzero v has ⟨u,v⟩ ≤ 0 for every u ∈ D, so Φ(x+rv) does not increase as r grows. If K ⊂ Ω, this also makes Ω unbounded. For example D = {e₁,−e₁,e₂} has a positive-definite Hessian but yields an unbounded sublevel extending downward.

3. **The strict t inequality is needed for a uniform inclusion guarantee.** At t = log N/ε and K = {a}, Φ(a) = 1, so K is not contained in the open set Ω. The stated hypotheses also require ε > 0; they are not meaningful as written at ε = 0.

4. **Positive Hessian is not global uniform strong convexity.** In ℝ² take the three directions (1,0), (−1/2,√3/2), and (−1/2,−√3/2), a net of exact covering radius 1. For K = {0}, at x = (r,0) the Hessian quadratic form in direction e₂ is (3/2)t²e⁻ᵗεe⁻ᵗʳ⁄², which tends to zero. The Hessian is positive definite at every point, but no uniform positive lower bound on all of ℝ² exists.

5. **Increasing t does not eliminate finite-direction error.** The inclusion P₀ ⊂ Ω proves this directly. For the unit ball and fixed coordinate directions in dimension d ≥ 2, letting ε decrease to zero and t increase subject to tε > log(2d) leaves the error tending to √d − 1. Refining directions, or choosing a geometry-specific adequate set, is essential.

6. **Convexity of K is essential for approximation to K itself.** The support function of an arbitrary compact set equals the support function of its convex hull. The construction therefore contains and approximates that convex hull, and cannot generally approximate a nonconvex K in Hausdorff distance. The projection-normal inequality also uses convexity.

7. **A singleton does not force a centered ball.** Arbitrary finite direction sets can yield asymmetric boundaries. Exact radial equations, or the coordinate-direction formulas, are the appropriate replacement for an unjustified rotational-symmetry claim.

8. **Topology depends on dimension.** In d = 2 the boundary is a Jordan curve; in general it is an analytic sphere Sᵈ⁻¹. For d = 1 it is two points, and in d ≥ 3 it should not be called a Jordan curve.

9. **Nesting is an extra choice, not a free consequence.** It follows from the inner-tube recursion above, not merely from δⱼ → 0 and εⱼ → 0.

These checks validate the local source construction and the stated higher-dimensional quantitative extension, within the parameter range and scope specified above.
