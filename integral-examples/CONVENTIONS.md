# Measures, functions, and theorems used in this library

The examples are applications for an analysis student. Their proofs are written
out; the general integration theorems below are prerequisites, with sources in
[SOURCES.md](SOURCES.md). A computation check verifies an identity, not the
measurability or integrability hypotheses that justify it.

## Functions and values

A function is a map with a specified domain, codomain, and rule. For example,
$f:(0,1)^2\to\mathbb R$ is a function, $f(x,y)$ is its value at $(x,y)$,
and $f_x:y\mapsto f(x,y)$ is a section function. With a fixed integrand and
measure, the integral is a number (or an allowed extended value), not another
notation for the function. A parameter integral defines a new function, for
example $F:t\mapsto\int f_t\,d\mu$; $F(t)$ is its value. When a section
integral is defined only almost everywhere, a measurable version is chosen
before integrating that version in the outer variable.

## Lebesgue and counting measures

$\mathcal L^n$ denotes complete $n$-dimensional Lebesgue measure on
$\mathbb R^n$. A restricted integral $\int_E f\,d\mathcal L^n$ means integration
over the measurable set $E$ with the restricted measure. For finite-valued $f$
defined on all of $\mathbb R^n$, it equals $\int f\mathbf1_E\,d\mathcal L^n$.
Counting measure on $\mathbb N=\{1,2,\ldots\}$ turns integration into an explicit
sum. The Lebesgue and countable counting measure factors used in the product
theorems here are sigma-finite. This does not assert sigma-finiteness of
$\mathcal H^k$ on all of $\mathbb R^n$ when $k<n$; our curve and surface
examples use finite-measure or countably covered restrictions.

For real measurable $f$, set $f^+=\max(f,0)$ and $f^-=\max(-f,0)$. A finite
Lebesgue integral requires

$$
\int |f|\,d\mu=\int f^+\,d\mu+\int f^-\,d\mu<\infty.
$$

An extended signed integral is defined if at least one of the two terms is
finite. If both are infinite, their difference is undefined. An improper limit
or principal value must be named separately; its existence does not supply a
signed Lebesgue integral.

## Normalized Hausdorff measure

For an integer $k\geq1$, let $\omega_k=\mathcal L^k(B(0,1))$. We use

$$
\mathcal H^k(E)=\lim_{\delta\downarrow0}\inf\left\{
\sum_{i=1}^{\infty}\omega_k\left(\frac{\operatorname{diam}U_i}{2}\right)^k:
E\subseteq\bigcup_{i=1}^{\infty}U_i,\quad
\operatorname{diam}U_i\leq\delta\right\}.
$$

$\mathcal H^0$ is counting measure. This normalization makes
$\mathcal H^k$ agree with $\mathcal L^k$ on every $k$-plane, using an isometry
to identify that plane with $\mathbb R^k$. Thus $\mathcal H^1$ measures length
and $\mathcal H^2$ measures surface area. In particular $\omega_1=2$ and
$\omega_2=\pi$. Some books omit the factor $\omega_k/2^k$; their numerical
values must be rescaled before using these examples. All Hausdorff integrals
in this library use the convention in this paragraph.

## Tonelli and Fubini, including completion

For a nonnegative product-measurable function on sigma-finite measure spaces,
Tonelli permits either order of integration, including the value $+\infty$.
For a signed or complex product-measurable function, Fubini applies if the
absolute value has finite integral. It then gives finite section integrals
almost everywhere and equality of the two iterated integrals with the product
integral.

The product of two complete Lebesgue sigma-algebras need not be complete.
For $\mathcal L^{p+q}$-measurable sets or functions on $\mathbb R^{p+q}$, use
the completed-product versions: sections need be measurable only for almost
every parameter. A Borel set has Borel sections at every parameter; an arbitrary
Lebesgue-measurable set need not have measurable sections at every parameter.
The outer integral uses a measurable representative of the almost-everywhere
section-integral function. E03 proves this distinction directly with a null
envelope. No claim about all sections is inferred from completeness.

## Area with multiplicity

For a Lipschitz map $F:\mathbb R^m\to\mathbb R^n$ with $m\leq n$, write

$$
J_mF(x)=\sqrt{\det(DF(x)^TDF(x))},\qquad
N(F,A,z)=\#\{x\in A:F(x)=z\}.
$$

The derivative and Jacobian exist almost everywhere; set the Jacobian to zero
at the exceptional points where the derivative does not exist. For a measurable domain
$A$ and nonnegative Borel weight $h$ on the source, the weighted area formula is

$$
\int_A h(x)J_mF(x)\,d\mathcal L^m(x)
=\int_{\mathbb R^n}\left(\sum_{x\in A\cap F^{-1}(\{z\})}h(x)\right)
\,d\mathcal H^m(z).
$$

The sum is an extended nonnegative sum. With $h=1$ it counts multiplicity.
With a nonnegative Borel $w$ and $h=w\circ F$ it becomes $w(z)N(F,A,z)$,
with the nonnegative-integration convention $0\cdot\infty=0$. An injective parametrization
therefore computes the geometric scalar integral once. If multiplicity is
$q$ almost everywhere, the parameter integral counts it $q$ times. For signed
weights require finite absolute integral with this multiplicity. A map on a
bounded domain that is Lipschitz there can be extended to apply the formula;
the geometric parametrizations to which we apply area are also Lipschitz on a
suitable containing compact box. The Cantor staircase is an explicitly
excluded counterexample.

For a graph $F(u)=(u,g(u))$ with a scalar $C^1$ function $g$,
$J_mF=\sqrt{1+|\nabla g|^2}$. This factor is derived in the graph example.

## Coarea and division by a Jacobian

For a Lipschitz map $G:\mathbb R^n\to\mathbb R^m$, $n\geq m$, the coarea
Jacobian is

$$
J_mG(x)=\sqrt{\det(DG(x)DG(x)^T)}.
$$

For nonnegative Borel $h$, coarea says

$$
\int_{\mathbb R^n}h(x)J_mG(x)\,d\mathcal L^n(x)
=\int_{\mathbb R^m}\left(\int_{G^{-1}(\{t\})}h(x)
\,d\mathcal H^{n-m}(x)\right)\,d\mathcal L^m(t).
$$

Fiber statements and inner integrals have their usual almost-everywhere
meaning. Here $m=1$ gives $J_1G=|\nabla G|$. To recover an unweighted volume
integral, division by $J_mG$ is legitimate only on its positive set. Any
contribution from its zero set must be handled separately. E12 identifies and
disposes of its critical point explicitly. E13 shows why a singular continuous
map cannot be substituted into a Lipschitz area formula.

## Scalar integration and orientation

$\int_S w\,d\mathcal H^k$ has no orientation. A scalar curve parametrization
uses speed $|\gamma'(t)|$. A vector circulation uses
$\int F(\gamma(t))\cdot\gamma'(t)\,dt$; reversing traversal changes its sign.
Flux through an oriented surface is
$\int_S F\cdot\nu\,d\mathcal H^{n-1}$ with a chosen unit normal $\nu$.
Changing $\nu$ changes flux. Neither a tangent vector nor a normal vector is
part of Hausdorff measure itself.

## Convergence and differentiation

The version of monotone convergence used here concerns nonnegative increasing
measurable functions. Dominated convergence concerns measurable functions and
requires almost-everywhere convergence and one integrable
majorant for the entire sequence. Pointwise convergence, boundedness of each
individual function, or a uniform bound on the integrals alone is insufficient.
E14 gives concentration and escape examples with explicit sufficient repairs.
E15 states and proves a local domination criterion for differentiating an
integral. E16 explains how concentration can instead be used deliberately as an
approximate identity.
