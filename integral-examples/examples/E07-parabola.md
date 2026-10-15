# E07 — A weighted integral on a parabolic arc

## Problem

Let $C=\{(t,t^2):0\leq t\leq1\}$. Compute the integral of the coordinate function $f:C\to\mathbb R$, defined by $f(x,y)=x$, with respect to arc length. Also compute the length of $C$.

## Data and hypotheses

The parametrization is $\gamma:[0,1]\to\mathbb R^2$, $\gamma(t)=(t,t^2)$. The curve $C$ is compact, and $f$ is continuous and nonnegative on $C$.

Throughout, $\mathcal L^k$ denotes Lebesgue measure. For an integer $k\geq1$, use the normalized Hausdorff measure

$$
\mathcal H^k(A)=\lim_{\delta\downarrow0}\inf\left\{\sum_{j=1}^{\infty}\frac{\alpha_k}{2^k}(\operatorname{diam}U_j)^k:
A\subseteq\bigcup_{j=1}^{\infty}U_j,\ \operatorname{diam}U_j<\delta\right\},
$$

where $\alpha_k=\mathcal L^k(B^k(0,1))$. Thus $\mathcal H^k$ on a $k$-plane agrees with $k$-dimensional Lebesgue measure, and $\mathcal H^0$ is counting measure. In particular, $\alpha_1=2$, so $\mathcal H^1$ here is ordinary arc length. The measure being integrated is the restriction $\mathcal H^1\mathbin{\vert}C$, not two-dimensional area measure.

## Solution

Differentiate the parametrization:

$$
\gamma'(t)=(1,2t),\qquad J_1\gamma(t)=|\gamma'(t)|=\sqrt{1+4t^2}.
$$

The first coordinate proves injectivity: if $\gamma(s)=\gamma(t)$, then $s=t$. The weighted area formula therefore gives

$$
\int_C f\,d\mathcal H^1
=\int_0^1 f(\gamma(t))|\gamma'(t)|\,dt
=\int_0^1 t\sqrt{1+4t^2}\,dt.
$$

Here $f$ is the function; $f(\gamma(t))=t$ is its value at the point $\gamma(t)$. With $u=1+4t^2$ and $du=8t\,dt$,

$$
\int_0^1 t\sqrt{1+4t^2}\,dt
=\frac18\int_1^5 u^{1/2}\,du
=\frac1{12}[u^{3/2}]_1^5
=\boxed{\frac{5\sqrt5-1}{12}}.
$$

For length, replace $f$ by the constant function $1$:

$$
\mathcal H^1(C)=\int_0^1\sqrt{1+4t^2}\,dt.
$$

Put $s=2t$. The identity

$$
\frac{d}{ds}\left(\frac12\bigl(s\sqrt{1+s^2}+\operatorname{arsinh}s\bigr)\right)
=\sqrt{1+s^2}
$$

yields

$$
\mathcal H^1(C)
=\frac{\sqrt5}{2}+\frac14\operatorname{arsinh}2
=\boxed{\frac{\sqrt5}{2}+\frac14\log(2+\sqrt5)}.
$$

## Why the theorem applies

The map $\gamma$ is $C^1$ on a neighborhood of $[0,1]$ and has bounded derivative there, hence is Lipschitz on this interval. Its domain is Borel. Its multiplicity is exactly one on $C$. The weighted area formula applies to the nonnegative Borel weight $f\circ\gamma$; the explicit integral is finite since $0\leq t\sqrt{1+4t^2}\leq\sqrt5$. Taking the constant weight also proves that $C$ has finite $\mathcal H^1$ measure.

## Pitfalls

- Integrating $t\,dt$ gives $1/2$, but this uses horizontal distance instead of arc length. The speed factor is necessary.
- The expression $\int_C f\,d\mathcal L^2$ would be zero: $C$ has two-dimensional Lebesgue measure zero. A Lipschitz arc can be covered by $N$ disks of radius proportional to $1/N$, with total area tending to zero.
- Reversing the traversal leaves this scalar Hausdorff integral unchanged. A vector circulation would include a signed tangent vector and can change sign.

## Reusable technique

For an injective Lipschitz curve, compose the scalar weight with the parametrization, then multiply by speed. Coordinate weights often turn a square-root integral into a direct substitution.

Tags: `hausdorff-normalization`, `weighted-arc-length`, `injective-area-formula`, `substitution`, `coordinate-moment`.

## Sources

- Leon Simon, [*Introduction to Geometric Measure Theory* (2018)](https://math.stanford.edu/~lms/ntu-gmt-text.pdf), Chapter 1, §2, definitions 2.1–2.2 and Theorem 2.6 (normalization); Chapter 2, §3, Theorem 3.3, Remark 3.4(2), and Example 3.5(1) (weighted area formula and arc length). The specific curve and computations above are worked out here. Source ID: `simon-gmt`.
