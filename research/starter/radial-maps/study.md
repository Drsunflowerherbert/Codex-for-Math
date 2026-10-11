# Radial contact with the unit sphere

## Scope and result

This study independently proves the radial-contact lemma from the pinned public OpenAI source and develops quantitative consequences. It concerns one supporting lemma only. It does not validate the source's headline claim about Tingley's problem, establish novelty, or report a Lean kernel check.

**Source fact.** Lemma 2.2 (`lem:radial`) asserts existence, uniqueness, continuity, and the radius bounds below. The pinned source is [main.tex, lines 135–143](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/build/main.tex#L135-L143), commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, blob `ab9bd82b388ec4e55a333d05c61c853b7941798b`. The source was read through the GitHub connector on 2026-10-11 UTC after ordinary web fetching failed.

**Independent derivation.** Everything proved here beyond that lemma's four assertions is a consequence developed for this study, not an attribution to the source and not a novelty claim. Proofs are mathematical arguments, not machine-certified proofs.

Let \(X\) be a real normed space, \(c\in X\), and \(r=\|c\|<1\). Write

\[
S_X=\{v:\|v\|=1\},\qquad a=1-r>0,\qquad U=1+r.
\]

For every \(v\in S_X\) there is exactly one positive scalar \(\rho_c(v)\) for which \(\|c+\rho_c(v)v\|=1\). Define

\[
P_c(v)=c+\rho_c(v)v.
\]

For fixed \(c\), the following global estimates hold in the norm-induced metric:

\[
a\le\rho_c(v)\le U,
\qquad
|\rho_c(v)-\rho_c(w)|\le \frac{U^2}{a}\|v-w\|,
\]
\[
\|P_c(v)-P_c(w)\|\le\frac{2U}{a}\|v-w\|.
\]

The radius constant \(U^2/a\) is the best uniform constant over all normed spaces and all centers of prescribed norm \(r\), for each \(0<r<1\). The contact-map constant is a valid upper bound; this study does not claim it is optimal. When \(r=0\), the exact statements are \(\rho_0\equiv1\) and \(P_0(v)=v\), so the radius Lipschitz constant is zero and the contact-map constant is one.

No completeness, finite dimension, strict convexity, smoothness, separability, or supporting-functional theorem is needed. If \(X=\{0\}\), its sphere is empty and the quantified statements about directions are vacuous. Assume \(X\ne\{0\}\) when a nonempty sphere is intended.

## 1 Independent proof of the source lemma

### R1 Existence

Fix \(v\in S_X\) and put \(h(t)=\|c+tv\|\) for \(t\ge0\). The reverse triangle inequality gives

\[
|h(t)-h(s)|\le\|(t-s)v\|=|t-s|.
\]

Thus \(h\) is continuous. We have \(h(0)=r<1\) and

\[
h(U)\ge\|Uv\|-\|c\|=U-r=1.
\]

The intermediate value theorem on the real interval \([0,U]\) supplies a root \(R>0\) of \(h(R)=1\). This argument uses compactness or continuity only in a one-dimensional real parameter, not compactness of the unit ball of \(X\).

### R2 Uniqueness

Suppose \(0<s<t\) both give norm one. Then

\[
c+sv=(1-s/t)c+(s/t)(c+tv).
\]

The triangle inequality and homogeneity give

\[
1=\|c+sv\|\le(1-s/t)r+s/t
=1-(1-s/t)(1-r)<1,
\]

a contradiction. Because \(c\) is interior, the contact parameter is strictly positive. Consequently the convention \(\mathbb R_+=[0,\infty)\) versus \((0,\infty)\) makes no difference here.

This is not an appeal to strict convexity. One endpoint in this convex combination has norm strictly below one; that is sufficient even when the sphere has flat faces.

### R3 Radius bounds

At the unique root \(R=\rho_c(v)\),

\[
1=\|c+Rv\|\le r+R,
\qquad
1=\|c+Rv\|\ge R-r.
\]

Therefore \(a\le R\le U\). In particular, division by \(R\) and by \(a\) is legitimate.

### R4 Continuity and the scalar compactness point

Suppose \(v_n\to v\) in \(S_X\), and put \(R_n=\rho_c(v_n)\). Every \(R_n\in[a,U]\). If a subsequence \(R_{n_j}\to L\), then

\[
\|R_{n_j}v_{n_j}-Lv\|
\le R_{n_j}\|v_{n_j}-v\|+|R_{n_j}-L|\to0.
\]

Hence \(\|c+Lv\|=1\), and uniqueness implies \(L=\rho_c(v)\). If the whole scalar sequence did not tend to this value, a subsequence would stay a fixed positive distance away. That subsequence has a convergent further subsequence in the compact real interval \([a,U]\), contradicting the preceding conclusion. Thus \(R_n\to\rho_c(v)\). Normed spaces are metric spaces, so sequential continuity is continuity.

This expands the compactness step in the source's proof. It does not require a convergent subsequence of the directions or of the contact points. The Lipschitz proof below independently implies continuity and can replace this argument.

## 2 Quantitative radial crossing

### D1 A lower bound on the rate of crossing

Let \(R=\rho_c(v)\). For \(0\le t\le R\), the same convex combination as above gives

\[
h(t)\le r+\frac{a}{R}t
=1-\frac{a}{R}(R-t).
\]

For \(t\ge R\), write \(c+Rv=(1-R/t)c+(R/t)(c+tv)\). When \(t>0\), rearranging its norm inequality gives

\[
h(t)\ge r+\frac{a}{R}t
=1+\frac{a}{R}(t-R).
\]

At \(t=R\) both formulas give equality. Consequently

\[
\boxed{\ |h(t)-1|\ge\frac{a}{R}|t-R|\quad(t\ge0).\ }
\tag{crossing}
\]

In particular, \(h(t)<1\) before contact and \(h(t)>1\) after contact. The function \(h\) itself need not be increasing before contact. The crossing estimate is the property actually needed.

### D2 Lipschitz radius and reciprocal radius

Let \(R=\rho_c(v)\), \(S=\rho_c(w)\), and \(\delta=\|v-w\|\). The reverse triangle inequality gives

\[
\big|\|c+Sv\|-1\big|
=\big|\|c+Sv\|-\|c+Sw\|\big|
\le S\delta.
\]

Applying (crossing) along \(v\) at \(t=S\) yields

\[
\boxed{\ |R-S|\le\frac{RS}{a}\delta.\ }
\tag{product bound}
\]

Therefore

\[
\boxed{\ \left|\frac1R-\frac1S\right|\le\frac1a\delta,\qquad
|R-S|\le\frac{U^2}{a}\delta.\ }
\]

These bounds do not assume differentiability of the norm. Example 3 proves sharpness of \(U^2/a\) for prescribed \(r>0\), and of \(1/a\) for the reciprocal radius in the same class. At \(r=0\), both functions are constant on \(S_X\).

### D3 Lipschitz radial contact

If \(R\ge S\), decompose \(Rv-Sw=S(v-w)+(R-S)v\). Interchange \(v,w\) for the other order. Thus

\[
\|P_c(v)-P_c(w)\|
\le\min(R,S)\delta+|R-S|
\le\left(\min(R,S)+\frac{RS}{a}\right)\delta.
\]

Using \(R,S\le U\) and \(a+U=2\),

\[
\boxed{\ \|P_c(v)-P_c(w)\|\le\left(U+\frac{U^2}{a}\right)\delta
=\frac{2U}{a}\delta.\ }
\]

### D4 A bi-Lipschitz parametrization of the sphere

For every \(x\in S_X\), \(\|x-c\|\ge1-\|c\|=a>0\). Define

\[
Q_c(x)=\frac{x-c}{\|x-c\|}.
\]

Uniqueness of contact implies \(P_c(Q_c(x))=x\), and directly \(Q_c(P_c(v))=v\). Hence \(P_c\) is a bijection from \(S_X\) onto \(S_X\) with inverse \(Q_c\).

For nonzero vectors \(b,d\), suppose \(\|b\|\ge\|d\|\). Then

\[
\left\|\frac b{\|b\|}-\frac d{\|d\|}\right\|
\le\frac{\|b-d\|}{\|b\|}
+\frac{|\|b\|-\|d\||}{\|b\|}
\le\frac{2\|b-d\|}{\|b\|}.
\]

Interchanging the vectors gives the symmetric denominator \(\max(\|b\|,\|d\|)\). Applied to \(b=x-c,d=y-c\), this proves

\[
\|Q_c(x)-Q_c(y)\|\le\frac2a\|x-y\|.
\]

Combining with D3,

\[
\boxed{\ \frac a2\|v-w\|\le\|P_c(v)-P_c(w)\|
\le\frac{2U}{a}\|v-w\|.\ }
\]

These estimates give a bi-Lipschitz homeomorphism. Neither displayed constant is asserted to be optimal.

## 3 Center perturbations and unnormalized directions

### D5 Joint estimates away from the boundary

Fix \(0\le q<1\), and suppose \(\|c\|,\|d\|\le q\). In this subsection only, write \(a_q=1-q\), \(U_q=1+q\). For \(v,w\in S_X\), put \(R=\rho_c(v)\), \(S=\rho_d(w)\), \(\eta=\|c-d\|\), and \(\delta=\|v-w\|\). Then

\[
\big|\|c+Sv\|-1\big|
\le\|(c-d)+S(v-w)\|\le\eta+S\delta.
\]

The crossing estimate for center \(c\), followed by its uniform bounds, gives

\[
\boxed{\ |\rho_c(v)-\rho_d(w)|
\le\frac{U_q}{a_q}\eta+\frac{U_q^2}{a_q}\delta.\ }
\]

Decomposing the difference of contact points gives

\[
\boxed{\ \|P_c(v)-P_d(w)\|
\le\frac2{a_q}\eta+\frac{2U_q}{a_q}\delta.\ }
\]

Thus both maps are jointly locally Lipschitz on the open unit ball of centers times the unit sphere; more precisely, they have the stated uniform bounds on each region \(\|c\|\le q<1\). No uniform constants independent of \(q\uparrow1\) can hold over all norms, as Example 3 shows.

### D6 Correct formulation for nonzero directions

If \(u\ne0\), define the unique contact parameter \(\tau_c(u)>0\) by \(\|c+\tau_c(u)u\|=1\). With \(\widehat u=u/\|u\|\),

\[
\tau_c(u)=\frac{\rho_c(\widehat u)}{\|u\|},\qquad
\frac a{\|u\|}\le\tau_c(u)\le\frac U{\|u\|}.
\]

For \(\lambda>0\), \(\tau_c(\lambda u)=\tau_c(u)/\lambda\), while the contact point \(\widetilde P_c(u)=c+\tau_c(u)u\) is unchanged. Negative scaling reverses the ray and is not covered by this identity. The zero direction gives the singleton \(c\), which has no sphere contact.

The proof of (crossing) uses no normalization once a contact parameter exists. Therefore, for \(u,z\ne0\),

\[
|\tau_c(u)-\tau_c(z)|
\le\frac{\tau_c(u)\tau_c(z)}a\|u-z\|
\le\frac{U^2}{a\|u\|\|z\|}\|u-z\|.
\]

Assume, for example, \(\|u\|\ge\|z\|\), and use

\[
\tau_c(u)u-\tau_c(z)z
=\tau_c(u)(u-z)+(\tau_c(u)-\tau_c(z))z.
\]

This gives the symmetric estimate

\[
\|\widetilde P_c(u)-\widetilde P_c(z)\|
\le\frac{2U}{a\max(\|u\|,\|z\|)}\|u-z\|.
\]

Consequently, on every set \(\|u\|\ge m>0\), the parameter is Lipschitz with constant \(U^2/(am^2)\), and the contact map is Lipschitz with constant \(2U/(am)\). Approaching \(u=0\) prevents such a uniform statement: \(\tau_c(\lambda u)=\tau_c(u)/\lambda\to\infty\).

## 4 Four worked examples and counterexamples

### Example 1 Exact radius bounds and the normalization trap

Take \(X=\mathbb R\) with its absolute-value norm and \(0\le c=r<1\). Its two unit directions satisfy

\[
\rho_c(1)=1-r=a,\qquad \rho_c(-1)=1+r=U.
\]

Indeed the contacts are \(+1\) and \(-1\), respectively. Both radius bounds are attained. On the two-point unit sphere, the best scalar Lipschitz constant is

\[
\frac{|(1+r)-(1-r)|}{|1-(-1)|}=r,
\]

much smaller than the general worst-case constant.

For a concrete normalization check, let \(c=1/2\) and \(u=2\). The ray equation is \(|1/2+2t|=1\), with unique positive solution \(t=1/4\). The unnormalized parameter is below \(1-\|c\|=1/2\); this is not a counterexample to the source because \(u\) is not unit. The correct lower bound is \(a/\|u\|=1/4\). For \(u=0\), there is no contact at all.

### Example 2 Hilbert formula and an infinite dimensional test

In a real Hilbert space, put \(b=\langle c,v\rangle\) and \(r=\|c\|<1\). The contact equation becomes

\[
t^2+2bt+r^2-1=0.
\]

Its roots have opposite signs, and the positive root is

\[
\boxed{\ \rho_c(v)=-b+\sqrt{b^2+1-r^2}.\ }
\]

For \(c=(1/2,0)\) in the Euclidean plane, the directions \((1,0)\), \((-1,0)\), \((0,1)\) have radii \(1/2\), \(3/2\), \(\sqrt3/2\), respectively. The last contact is \((1/2,\sqrt3/2)\), whose squared norm is one.

The formula also yields a sharper Hilbert-space estimate. On \(b\in[-r,r]\), the derivative of \(F(b)=-b+\sqrt{b^2+1-r^2}\) has absolute value at most \(1+r\): the ratio \(b/\sqrt{b^2+1-r^2}\) ranges in \([-r,r]\). By the real mean value theorem and Cauchy–Schwarz,

\[
|\rho_c(v)-\rho_c(w)|\le r(1+r)\|v-w\|.
\]

This is a valid Hilbert-specific estimate, not a claimed sharp constant. Its better behavior illustrates that the general bound is driven by geometry allowed in arbitrary norms.

For an infinite-dimensional check, take \(X=\ell_2(\mathbb N;\mathbb R)\), \(c=re_1\), and \(v=e_n\) for \(n\ge2\). Then

\[
\rho_c(e_n)=\sqrt{1-r^2},\qquad
P_c(e_n)=re_1+\sqrt{1-r^2}e_n.
\]

Distinct directions have distance \(\sqrt2\), and distinct contacts have distance \(\sqrt{2(1-r^2)}\). Neither sequence has a norm-convergent subsequence. All contacts and estimates remain valid; compactness of the ambient sphere was never assumed.

### Example 3 A square norm and sharp scalar constants

Take \(X=(\mathbb R^2,\|\cdot\|_\infty)\), \(0<r<1\), \(c=(r,-r)\), \(a=1-r\), \(U=1+r\), and

\[
v=(a/U,1),\qquad w_h=(a/U+h,1),\qquad0<h<2r/U.
\]

Both directions are unit, and \(\|v-w_h\|_\infty=h\). At \(t=U\),

\[
c+Uv=(1,1),\qquad \rho_c(v)=U.
\]

For \(w_h\), the first coordinate reaches \(1\) at

\[
S_h=\frac a{a/U+h}=\frac{aU}{a+Uh}<U.
\]

At that time the second coordinate is \(-r+S_h\in(-1,1)\), so this is the contact. Therefore

\[
\frac{|\rho_c(v)-\rho_c(w_h)|}{\|v-w_h\|_\infty}
=\frac{U^2}{a+Uh}\longrightarrow\frac{U^2}{a}.
\]

No smaller universal scalar Lipschitz constant can hold for a prescribed \(r>0\). Moreover,

\[
\frac{|1/S_h-1/U|}{\|v-w_h\|_\infty}=\frac1a,
\]

so the reciprocal-radius bound is attained exactly. The contacts are \((1,1)\) and \((1,-r+S_h)\); their distance is \(U-S_h\). Thus any universal contact-map Lipschitz constant must also be at least \(U^2/a\), although the upper bound proved here is \(2U/a\).

The restriction \(r>0\) matters: at \(r=0\), the interval \(0<h<2r/U\) is empty and the radius is constant. The same examples embed isometrically in \(\ell_\infty(\mathbb N)\) by appending zero coordinates.

Flat faces cause no difficulty. For instance, in this square norm, \(c=(1/2,0)\), \(v=(0,1)\) gives \(h(t)=\max(1/2,t)\), which is constant for \(0\le t\le1/2\) and has unique contact at \(t=1\). Alternatively, \(c=(-1/2,0)\), \(v=(1,0)\) gives \(h(t)=|t-1/2|\), decreasing before it increases, with contact at \(t=3/2\). A proof based on strict increase of \(h\) would therefore be invalid.

### Example 4 Boundary and exterior centers

**Boundary, flat face.** In the square norm let \(c=(1,0)\), \(v=(0,1)\). Then \(\|c+tv\|_\infty=1\) for every \(0\le t\le1\). There are infinitely many contacts, even if \(t=0\) is excluded. If instead \(v=(1,0)\), there is no positive-time contact, and \(t=0\) is the only closed-ray contact.

Defining an outermost closed-ray contact does not fix continuity in general. For \(v_0=(0,1)\) it has parameter \(1\); for \(v_\epsilon=(\epsilon,1)\), \(0<\epsilon\le1\), it has parameter \(0\), since the first coordinate immediately exceeds one. Yet \(v_\epsilon\to v_0\).

**Boundary, strictly convex sphere.** In the Euclidean plane, \(c=(1,0)\), \(v=(-1,0)\) gives contacts at \(t=0\) and \(t=2\); \(v=(0,1)\) gives only \(t=0\); \(v=(1,0)\) also gives only \(t=0\). Under the positive-ray convention, the latter two have no contact. Strict convexity cannot restore the all-directions assertion when the center is on the sphere.

**Exterior.** In the Euclidean plane, \(c=(2,0)\), \(v=(-1,0)\) gives contacts at \(t=1,3\), so uniqueness fails. The outward direction \(v=(1,0)\) has no contact. The unit tangent direction \(v=(-\sqrt3/2,1/2)\) gives

\[
\|c+tv\|_2^2-1=t^2-2\sqrt3t+3=(t-\sqrt3)^2,
\]

so it has exactly one contact, \(t=\sqrt3\). Outside the ball, zero, one, and two contacts are all possible even for a Euclidean sphere. The condition \(\|c\|<1\) is therefore essential to the universal theorem.

## 5 Residual certificates and a reusable numerical specification

This section specifies an algorithm mathematically. No numerical experiment, repository program, or formal proof checker was run.

For unit \(v\), the interval \([a,U]\) brackets the contact because \(h(a)\le1\) and \(h(U)\ge1\). By D1, its sign relative to one identifies which side of the root a trial point lies on, even when \(h\) is not globally monotone.

With exact norm evaluations, bisection maintains a valid closed bracket. A midpoint with norm exactly one solves the problem; a norm below one replaces the lower endpoint; a norm above one replaces the upper endpoint. After \(n\) bracket halvings, the interval width is \(2r/2^n\), and its midpoint has radius error at most \(r/2^n\). The corresponding contact-point error has the same norm bound because \(v\) is unit. If \(r=0\), the initial bracket is already the singleton \(\{1\}\).

For any nonnegative trial \(t\), (crossing) gives the posterior certificate

\[
\boxed{\ |t-\rho_c(v)|\le\frac{U}{a}\,\big|\|c+tv\|-1\big|.\ }
\]

If the norm is known only through an approximation \(\widehat h(t)\) with certified error at most \(\varepsilon\), use

\[
|t-\rho_c(v)|\le\frac{U}{a}\big(|\widehat h(t)-1|+\varepsilon\big).
\]

An approximate value whose error interval contains one cannot justify choosing a bisection side. Retain the bracket, improve the norm evaluation, or use the residual certificate. This separates a theorem from an unverified numerical output.

## 6 Assumption and dependency audit

- **Strict interior center:** used for \(a>0\), uniqueness, a positive lower radius bound, residual stability, and uniform Lipschitz constants. Example 4 shows failure at and beyond the boundary.
- **Unit direction:** needed for the displayed unscaled interval \([1-r,1+r]\). D6 gives the corrected statement for nonzero directions; Example 1 exposes the normalization error.
- **Convexity:** supplied automatically by a norm ball and used through the triangle inequality. Strict convexity is unnecessary.
- **Norm continuity:** follows from the reverse triangle inequality and is used for the intermediate value theorem. No continuity assumption has been added independently.
- **Completeness of \(X\):** not used. For example the same proof works on finitely supported real sequences with the inherited \(\ell_2\) norm, an incomplete normed space.
- **Dimension:** unrestricted. All scalar compactness is in a real interval. Example 2 explicitly avoids ambient compactness, and Example 3 embeds in an infinite-dimensional nonsmooth space.
- **Field:** stated for real normed spaces. A complex normed space regarded as a real normed space also satisfies the statement for real positive ray parameters; no complex-line assertion is made.
- **Hahn–Banach and supports:** not used, despite the supporting-functional lemma preceding Lemma 2.2 in the source.
- **Later source results:** attainment, chord alignment, fixed-point arguments, and the main sphere-isometry extension theorem are not dependencies of this study and have not been audited here.
- **Verification scope:** the source lemma is independently proved above; additional estimates are proved above and separately identified. An independent review, if supplied, is an argument review and does not constitute formal kernel checking.

Machine-readable theorem records and dependency edges are in `theorems.json`; the four examples are in `examples.json`; exact provenance and verification scope are in `provenance.json`. These are standalone study records rather than a claim of compliance with an unspecified external MRS schema.
