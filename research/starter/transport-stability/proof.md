# Three atom obstruction to uniform stability of optimal transport maps

## Result and scope

Fix a dimension \(d\geq2\). On the fixed cube \(K=Y=[-1,1]^d\), let
\(\rho=2^{-d}\mathbf 1_K\,dx\) be uniform probability. There are pairs
\((\mu_a,\nu_a)\) of three-atom probability measures in \(Y\), indexed by
\(0<a<1/2\), whose unique quadratic optimal transport maps satisfy

\[
W_2(\mu_a,\nu_a)^2=\frac{a^3}{4},\qquad
W_1(\mu_a,\nu_a)=\frac{a^2}{2},\qquad
\|T_{\mu_a}-T_{\nu_a}\|_{L^2(\rho)}^2=\frac{a+a^3}{4}.
\]

Consequently, no constant uniform over these targets can give an
\(L^2\)-map stability estimate with a power of \(W_2\) exceeding \(1/3\),
or a power of \(W_1\) exceeding \(1/4\). The proof below is elementary:
finite affine maxima give a direct quadratic-cost dual certificate,
and all remaining calculations are one-dimensional slice integrals.

This is an independently rederived ordinary mathematical proof of the
obstruction from the cited source. It does not prove any global upper
stability bound. No Lean compilation or kernel verification was run.
Independent review status is recorded separately in the theorem JSON.

## Definitions for an analysis student

All norms and dot products below are Euclidean. The vector \(e_j\) has
coordinate \(1\) in position \(j\) and \(0\) elsewhere. The symbol
\(\delta_y\) denotes unit point mass at \(y\), and \(\mathbf 1_E\) denotes
the indicator of a set \(E\).

For a Borel measurable map \(T\) and a probability measure \(\rho\), the
pushforward \(T_\#\rho\) is the law of \(T(X)\) when \(X\) has law
\(\rho\): explicitly, \(T_\#\rho(E)=\rho(T^{-1}(E))\). A transport plan,
or coupling, between \(\sigma\) and \(\tau\) is a probability measure
\(\pi\) on pairs \((x,y)\) whose first and second marginals are
\(\sigma\) and \(\tau\). Its quadratic cost is
\(\int|x-y|^2\,d\pi(x,y)\). A map transports \(\sigma\) to \(\tau\)
when \(T_\#\sigma=\tau\); its graph plan is
\((\mathrm{id},T)_\#\sigma\).

For finite \(p\geq1\), the \(p\)-Wasserstein distance is

\[
W_p(\sigma,\tau)=
\left(\inf_{\pi\in\Pi(\sigma,\tau)}
\int|x-y|^p\,d\pi(x,y)\right)^{1/p}.
\]

The \(L^2(\rho)\) distance between maps is
\(\|T-S\|_{L^2(\rho)}=(\int|T(x)-S(x)|^2\,d\rho(x))^{1/2}\).
It compares the maps at the same source point. It is generally larger
than the Wasserstein distance between their laws: the same-source plan
\((T,S)_\#\rho\) is only one admissible target coupling.

A uniform Hölder estimate with exponent \(\alpha\) means a finite
constant \(C\), independent of the target pair, such that
\(\|T_\mu-T_\nu\|_{L^2(\rho)}\leq C W_p(\mu,\nu)^\alpha\).
The constant may depend on fixed data such as \(d,K,Y,\rho\).

## A finite affine maximum gives a unique quadratic optimal plan

### Statement

Let \(\rho\) be a Borel probability measure on \(\mathbb R^d\),
absolutely continuous with respect to Lebesgue measure, with
\(\int|x|^2\,d\rho(x)<\infty\). For a positive finite integer \(N\),
vectors \(y_1,\ldots,y_N\in\mathbb R^d\), and real numbers
\(c_1,\ldots,c_N\), set

\[
u(x)=\max_{1\leq i\leq N}(x\cdot y_i+c_i).
\]

Select the smallest maximizing index and set \(T(x)\) equal to its
slope \(y_i\). Then \(T\) is Borel, \(T=\nabla u\) for
\(\rho\)-almost every \(x\), and \((\mathrm{id},T)_\#\rho\) is the
unique quadratic-cost optimal plan from \(\rho\) to
\(\lambda=T_\#\rho\). In particular, the optimal map is unique up to
\(\rho\)-null modifications.

### Proof

Write \(\ell_i(x)=x\cdot y_i+c_i\). The set on which the first maximizing
index is \(i\) is

\[
E_i=\bigcap_j\{\ell_i\geq\ell_j\}
\ \cap\ \bigcap_{j<i}\{\ell_i>\ell_j\}.
\]

This is Borel, being a finite intersection of closed or open affine
half-spaces. Thus the finite-valued map \(T\) is Borel.

For a repeated slope \(y\), retain only the largest intercept
\(c(y)=\max_{i:y_i=y}c_i\). This does not change \(u\) or any selected
slope. For distinct remaining slopes \(y\ne z\), their affine functions
tie only on

\[
\{x:x\cdot(y-z)=c(z)-c(y)\}.
\]

Because \(y-z\ne0\), this is an affine hyperplane. A finite union of
such hyperplanes has Lebesgue measure zero and hence \(\rho\)-measure
zero. Off that union the maximum has a unique slope and, by the strict
inequalities and continuity, the same affine function wins in a
neighborhood. Therefore \(u\) is differentiable there with gradient
\(T(x)\).

For every remaining slope \(y\), the defining maximum gives the
nonnegative slack

\[
s(x,y)=u(x)-x\cdot y-c(y)\geq0.
\]

All terms are integrable under any coupling of \(\rho\) and \(\lambda\).
Indeed, the finite slope set is bounded, \(|u(x)|\leq R|x|+M\) for
suitable finite \(R,M\), and a finite second moment implies a finite
first moment by Cauchy–Schwarz. The quadratic cost is also finite for
every such coupling. Expanding the square yields

\[
\int|x-y|^2\,d\pi
=\int|x|^2\,d\rho+\int|y|^2\,d\lambda
-2\int x\cdot y\,d\pi.
\]

The first two terms depend only on the marginals. Moreover,

\[
\int x\cdot y\,d\pi
\leq \int u\,d\rho-\int c(y)\,d\lambda(y),
\]

and the graph plan of \(T\) attains equality because \(T(x)\) is a
maximizing slope at every \(x\). This proves optimality directly.

For clarity, an explicit quadratic dual certificate is

\[
\phi(x)=|x|^2-2u(x),\qquad
\psi(y)=|y|^2+2c(y),\qquad
\phi(x)+\psi(y)\leq|x-y|^2.
\]

Here \(\psi\) only needs to be specified on the finite target support.
The cost minus the certificate equals \(2s(x,y)\).

If \(\pi\) is any optimal plan, it must attain the same cost as the
graph plan. Hence \(\int s\,d\pi=0\). Since \(s\geq0\), it vanishes
\(\pi\)-almost everywhere. The first marginal of \(\pi\) is \(\rho\),
so the hyperplane exceptional set has zero \(\pi\)-mass in the first
coordinate. At all other source points, zero slack forces \(y=T(x)\).
Thus \(\pi\) is concentrated on the graph of \(T\). A measure on that
graph with first marginal \(\rho\) is uniquely
\((\mathrm{id},T)_\#\rho\), proving uniqueness. \(\square\)

### Precise assumptions

Absolute continuity is sufficient because it makes every affine
hyperplane null. It can be weakened to the requirement that the finite
set of distinct-slope tie hyperplanes has \(\rho\)-measure zero.
Repeated slopes need not be excluded; merging them handles that case.
The source need not have convex or bounded support, nor a density
bounded above or below, for this lemma. Finite second moment keeps the
quadratic optimization finite. These observations concern this lemma,
not general stability theorems.

## The cube family and its target masses

We first calculate for the slightly wider parameter range

\[
0<b<a,\qquad a+b<1.
\tag{P}
\]

The requested family \(0<a<1/2,\ b=a/2\) satisfies (P). Define

\[
u(x)=\max\{-x_1,x_1,a\},\qquad
v(x)=\max\{-x_1,x_1,a+bx_2\}.
\]

The slopes of \(u\) are \(-e_1,e_1,0\), and those of \(v\) are
\(-e_1,e_1,be_2\). They are distinct within each maximum and lie in
\([-1,1]^d\). The source is absolutely continuous with bounded support,
so the lemma applies. Let \(T=\nabla u\), \(S=\nabla v\) off the tie
sets and use the first-index convention on those sets. Put
\(\mu=T_\#\rho\), \(\nu=S_\#\rho\). These are their unique quadratic
optimal maps from \(\rho\).

The two central cells, ignoring null boundaries, are

\[
A=\{|x_1|<a\},\qquad B=\{|x_1|<a+bx_2\}.
\]

By (P), \(0<a-b\leq a+bx_2\leq a+b<1\) throughout the cube. The
threshold is always positive and never clipped by the edge of the cube.
Therefore

\[
T(x)=\begin{cases}0&x\in A,\\
\operatorname{sign}(x_1)e_1&x\notin A,
\end{cases}\qquad
S(x)=\begin{cases}be_2&x\in B,\\
\operatorname{sign}(x_1)e_1&x\notin B.
\end{cases}
\]

Under \(\rho\), all coordinates are independent and uniform on
\([-1,1]\). Fix \(x_2=t\). An interval \((-h,h)\subset[-1,1]\) has
conditional probability \(h\), since its length is \(2h\) and the
density of \(x_1\) is \(1/2\). Thus

\[
\rho(B\mid x_2=t)=a+bt,
\qquad
\rho(S=\pm e_1\mid x_2=t)=\frac{1-a-bt}{2}.
\]

Averaging with the density \(dt/2\) gives

\[
\rho(B)=\frac12\int_{-1}^{1}(a+bt)\,dt=a,
\]

\[
\rho(S=\pm e_1)
=\frac12\int_{-1}^{1}\frac{1-a-bt}{2}\,dt
=\frac{1-a}{2}.
\]

The corresponding integrals for \(T\) have constant widths. Hence,
with \(m=(1-a)/2\),

\[
\boxed{\mu=m\delta_{-e_1}+a\delta_0+m\delta_{e_1},\qquad
\nu=m\delta_{-e_1}+a\delta_{be_2}+m\delta_{e_1}.}
\tag{1}
\]

Both laws have exactly three distinct atoms, all of positive mass.
For \(d>2\), integrating the remaining coordinates contributes
\(2^{d-2}\cdot2^{-(d-2)}=1\), so the same computations apply.

## Exact Wasserstein distances between the targets

The matching coupling

\[
\pi_*=m\delta_{(-e_1,-e_1)}+a\delta_{(0,be_2)}
+m\delta_{(e_1,e_1)}
\]

has cost \(ab^p\) for every finite \(p\geq1\).

Conversely, for any coupling \(\pi\) of \(\mu\) and \(\nu\), write
its two target variables as \(y,z\). Every \(y\) in the support of
\(\mu\) has \(y_2=0\). Therefore

\[
\int|y-z|^p\,d\pi
\geq\int|y_2-z_2|^p\,d\pi
=\int|z_2|^p\,d\nu(z)
=ab^p.
\]

Together with the matching upper bound, this proves

\[
\boxed{W_p(\mu,\nu)^p=ab^p,\qquad
W_p(\mu,\nu)=a^{1/p}b\quad(1\leq p<\infty).}
\tag{2}
\]

In particular, \(W_2^2=ab^2\) and \(W_1=ab\). There is no need to
solve a transport optimization numerically. In fact, the optimal
target coupling is unique for every such \(p\): equality in
\(|y-z|\geq|y_2-z_2|\) requires equality of every other coordinate.
The three possible first coordinates \(-1,0,1\) then force exactly
the three matched pairs of \(\pi_*\).

For completeness, \(W_\infty\), defined as the infimum over couplings
of the essential supremum of \(|y-z|\), equals \(b\). The central
target atom has positive mass and second coordinate \(b\), giving
the lower bound, and \(\pi_*\) attains it.

## Exact distance between the optimal maps

On a slice \(x_2=t\), the intervals defining \(A\) and \(B\) are
nested. Their lengths differ by \(2b|t|\), so their symmetric
difference has conditional probability \(b|t|\). Thus

\[
\rho(A\mathbin{\triangle}B)
=\frac12\int_{-1}^{1}b|t|\,dt=\frac b2.
\tag{3}
\]

More precisely,

\[
\rho(B\setminus A)=\frac12\int_0^1bt\,dt=\frac b4,
\qquad
\rho(A\setminus B)=\frac12\int_{-1}^0(-bt)\,dt=\frac b4,
\]

and \(\rho(A\cap B)=a-b/4\).

The first coordinate of \(T-S\) is zero off
\(A\mathbin{\triangle}B\), and has absolute value one on that
symmetric difference. Its second coordinate is \(-b\mathbf 1_B\).
All further coordinates vanish. Orthogonality therefore gives

\[
|T(x)-S(x)|^2
=\mathbf 1_{A\mathbin{\triangle}B}(x)+b^2\mathbf 1_B(x)
\quad\text{for }\rho\text{-almost every }x.
\]

Integrating (1) and (3) proves

\[
\boxed{\|T-S\|_{L^2(\rho)}^2=\frac b2+ab^2.}
\tag{4}
\]

An explicit joint mass matrix makes clear why this cost exceeds the
optimal target-to-target cost. Order the values of \(T\) as
\((-e_1,0,e_1)\) and those of \(S\) as \((-e_1,be_2,e_1)\). The
common-source coupling \((T,S)_\#\rho\) has matrix

\[
\begin{pmatrix}
m-b/8 & b/8 & 0\\
b/8 & a-b/4 & b/8\\
0 & b/8 & m-b/8
\end{pmatrix}.
\tag{5}
\]

The off-diagonal reassignment has total mass \(b/2\); it costs
approximately one per unit mass, rather than merely the central
displacement \(b^2\). In particular,

\[
\frac{\|T-S\|_{L^2(\rho)}^2}{W_2(\mu,\nu)^2}
=1+\frac{1}{2ab}.
\tag{6}
\]

## The exponent obstructions

Set \(b=a/2\), with \(0<a<1/2\). Equations (2) and (4) become

\[
W_p(\mu_a,\nu_a)=\frac12 a^{1+1/p},\qquad
\|T_{\mu_a}-T_{\nu_a}\|_{L^2(\rho)}
=\frac12\sqrt a\sqrt{1+a^2}.
\]

For every finite \(p\geq1\) and exponent \(\alpha>0\), their ratio is

\[
\frac{\|T_{\mu_a}-T_{\nu_a}\|_{L^2(\rho)}}
{W_p(\mu_a,\nu_a)^\alpha}
=2^{\alpha-1}\sqrt{1+a^2}\,
a^{\frac12-\alpha(1+1/p)}.
\tag{7}
\]

If \(\alpha>p/[2(p+1)]\), the power of \(a\) is negative. For example,
taking \(a_n=1/n\) for integers \(n\geq3\) makes the ratio tend to
\(+\infty\). Thus no uniform estimate with such an exponent exists,
even when both targets have exactly three atoms. Special cases are:

- \(p=2\): every \(\alpha>1/3\) is impossible;
- \(p=1\): every \(\alpha>1/4\) is impossible.

At the two endpoint exponents, the ratios in this particular example
have finite nonzero limits:

\[
\lim_{a\downarrow0}\frac{\|T_{\mu_a}-T_{\nu_a}\|_2}
{W_2(\mu_a,\nu_a)^{1/3}}=2^{-2/3},
\qquad
\lim_{a\downarrow0}\frac{\|T_{\mu_a}-T_{\nu_a}\|_2}
{W_1(\mu_a,\nu_a)^{1/4}}=2^{-3/4}.
\]

These endpoint computations do not prove a uniform upper estimate.
They only show the order reached along this one family.

## Further consequences of the same calculation

For every finite \(q\geq1\), the three nonzero cases of \(|T-S|\)
give the exact identity

\[
\|T-S\|_{L^q(\rho)}^q
=(a-b/4)b^q+\frac b4\left[1+(1+b^2)^{q/2}\right].
\tag{8}
\]

The terms correspond to \(A\cap B\), \(A\setminus B\), and
\(B\setminus A\), respectively. With \(b=a/2\),
\(\|T-S\|_{L^q}\sim(a/4)^{1/q}\) as \(a\downarrow0\), where
\(f\sim g\) means \(f/g\to1\). Consequently this same family rules
out a uniform \(L^q\)-map estimate in terms of \(W_p^\alpha\) whenever
\(\alpha>p/[q(p+1)]\). This is an obstruction only; no assertion of
sharp global upper exponents for arbitrary \(p,q\) is made here.

There is also a direct failure of \(L^\infty\) continuity. Since
\(\rho(B\setminus A)=b/4>0\),

\[
\|T-S\|_{L^\infty(\rho)}=\sqrt{1+b^2}\longrightarrow1,
\]

even though \(W_p(\mu_a,\nu_a)\to0\) for every finite \(p\) and
\(W_\infty(\mu_a,\nu_a)=b\to0\).

Finally, every pair of distinct atoms within either target stays at
least distance one apart. The example does not rely on atom collisions.
Its central mass \(a\), however, tends to zero; it does not disprove
stronger estimates restricted to targets whose atom masses have a
common positive lower bound.

## Why dimension one behaves differently

The construction needs a transverse coordinate \(x_2\) to tilt the
central cell while preserving its average width. More decisively, on
the line with uniform source \([-1,1]\), finite-atom targets satisfy
the exact identity

\[
\|T_\mu-T_\nu\|_{L^2(\rho)}=W_2(\mu,\nu).
\tag{9}
\]

Here is an elementary justification in the same finite-atom setting.
Order the target atoms increasingly and assign the leftmost source
interval the mass of the first atom, then the next interval the mass of
the second atom, and so forth. This increasing step map is the quantile
map \(T_\mu(x)=Q_\mu((x+1)/2)\), where
\(Q_\mu(t)=\inf\{y:\mu(( -\infty,y])\geq t\}\) for \(0<t<1\).
It is the gradient of a convex piecewise-affine function with finitely
many slopes: integrating the increasing step map gives such a convex
function, and its affine pieces, extended to the whole line, have that
function as their finite maximum. The lemma proves optimality and
uniqueness of this map from the atomless source.

It remains to see that pairing the two quantile maps is optimal
between their target laws. Suppose both targets are in a bounded
interval \([-M,M]\). For any coupling \((Y,Z)\), put
\(U=Y+M,V=Z+M\in[0,2M]\). Tonelli's theorem gives

\[
\mathbb E[UV]=\int_0^{2M}\int_0^{2M}
\mathbb P(U>s,V>t)\,ds\,dt
\leq\int_0^{2M}\int_0^{2M}
\min\{\mathbb P(U>s),\mathbb P(V>t)\}\,ds\,dt.
\]

Using both quantiles of one uniform variable attains this bound:
each threshold event is an upper interval of that same variable, so
the intersection has the smaller of the two probabilities. Thus the
quantile coupling maximizes \(\mathbb E[UV]\), equivalently
\(\mathbb E[YZ]\), and minimizes quadratic cost. This proves (9).
The contrast therefore holds for the same finite-atom target class as
the obstruction, without needing a general one-dimensional transport
theorem.

## Exact rational test cases

The companion script uses only Python's standard library and exact
fractions. It obtains all nine common-source coupling masses by clipping
the square with the actual affine cell inequalities and applying the
shoelace formula. Independently, it enumerates every basic feasible
vertex of the three-by-three target transport polytope and checks the
quadratic optimum. Each of the four cases has ten distinct vertices
and one minimizing vertex, the matching coupling. The \(W_1\) check
uses the exact coordinate lower-bound certificate and the matching
upper bound.

| \(a\) | \(b\) | outer mass each | \(W_1\) | \(W_2^2\) | \(\|T-S\|_2^2\) | source cost / target cost |
|---|---|---|---|---|---|---|
| \(2/5\) | \(1/5\) | \(3/10\) | \(2/25\) | \(2/125\) | \(29/250\) | \(29/4\) |
| \(1/4\) | \(1/8\) | \(3/8\) | \(1/32\) | \(1/256\) | \(17/256\) | \(17\) |
| \(1/10\) | \(1/20\) | \(9/20\) | \(1/200\) | \(1/4000\) | \(101/4000\) | \(101\) |
| \(1/100\) | \(1/200\) | \(99/200\) | \(1/20000\) | \(1/4000000\) | \(10001/4000000\) | \(10001\) |

These are reproducible finite checks, not a replacement for the proof
for all admissible real parameters. Run `python check_exact_cases.py`
to regenerate `exact-cases.json`.

## Assumptions and conclusions audit

1. The source is a probability measure: the cube volume is \(2^d\),
   canceled by the density \(2^{-d}\).
2. Absolute continuity removes every tie hyperplane. First-index choices
   on those null sets affect neither target laws nor \(L^q\) integrals.
3. All source and target second moments are finite because the supports
   are bounded. The finite-affine lemma therefore solves a finite-cost
   optimization problem, and its uniqueness assertion is meaningful.
4. The parameter restrictions keep every central interval inside the
   cube and its half-width positive. Without those conditions the
   displayed slice formulas can fail through clipping or sign changes.
5. The slopes are distinct within each of the two three-piece maxima.
   The targets have exactly three distinct positive-mass atoms for
   every parameter in the family, even though one mass vanishes in the
   limiting two-atom law.
6. The source, source support, target container, dimension, and number
   of target atoms remain fixed as \(a\downarrow0\). A stability
   constant depending only on these fixed data cannot absorb divergence.
7. Each source-to-target map is quadratically optimal. Their common-source
   target-to-target coupling is not optimal; confusing these facts would
   incorrectly identify the map distance with \(W_2\).
8. No global \(W_2^{1/3}\) upper bound, global \(W_1^{1/4}\) upper bound,
   or global \(p,q\) sharpness theorem is proved here. The corresponding
   powers are necessary limits supplied by this example.
9. No conclusion is asserted for stronger restricted target classes
   such as uniformly positive atom masses or uniformly regular target
   densities. The finite-atom dimension-one class instead has (9).
10. No new Lean theorem, successful Lean build, proof-kernel certificate,
    native MRS import, or publication is claimed.

## Provenance and portable artifacts

The source is family 374 in the public OpenAI mathematics repository,
revision `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`:

- [Sharpness section and finite affine maximum lemma](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/build/source/sections/sharpness.tex)
- [Repository scope description for family 374](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/374.md)

The local source section was read in full. Its SHA-256 is
`f8732d68d0de8505d20f6c42aefce95d60b3e8363569681fa30632c997999590`.
The repository's formalization scope description is a source claim;
this study did not audit or execute that formalization.

The accompanying `theorems.json` is a portable, explicit theorem record
with assumptions, dependencies, verification status, and nonclaims.
It uses a study-specific schema and has not been imported into MRS.
`exact-cases.json` contains exact rational fixtures, and
`check_exact_cases.py` regenerates them without third-party packages.
