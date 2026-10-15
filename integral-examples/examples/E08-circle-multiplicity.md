# E08 — Traversing a circle twice: multiplicity and orientation

## Problem

Let $C=\{(x,y)\in\mathbb R^2:x^2+y^2=1\}$ and let $w:C\to\mathbb R$ be the function $w(x,y)=x^2$. Compare

$$
\int_C w\,d\mathcal H^1
\quad\hbox{and}\quad
\int_0^{4\pi}w(\gamma(t))|\gamma'(t)|\,dt,
\qquad \gamma(t)=(\cos t,\sin t).
$$

Then compare these scalar integrals with the circulation of the vector field $F(x,y)=(-y,x)$.

## Data and hypotheses

Use normalized Hausdorff measure: $\mathcal H^k$ has covering cost $\alpha_k(\operatorname{diam}U/2)^k$, where $\alpha_k$ is the volume of the unit ball in $\mathbb R^k$. It agrees with $\mathcal L^k$ on $k$-planes; $\mathcal H^0$ counts points. Thus $\mathcal H^1\mathbin{\vert}C$ is ordinary length measure. The functions $w$ and $F$ are continuous, and $0\leq w\leq1$ on $C$.

The map $\gamma$ is Lipschitz on $A=[0,4\pi]$. Its image is the geometric set $C$, which has no record of how many times it was traversed.

## Solution

First compute the parameter integral. Since

$$
\gamma'(t)=(-\sin t,\cos t),\qquad |\gamma'(t)|=1,
\qquad w(\gamma(t))=\cos^2t,
$$

we obtain

$$
\int_0^{4\pi}w(\gamma(t))|\gamma'(t)|\,dt
=\int_0^{4\pi}\frac{1+\cos(2t)}2\,dt
=\boxed{2\pi}.
$$

This is a traversal integral. To understand its relation to the geometric integral, define

$$
N(q)=\mathcal H^0\bigl(\{t\in A:\gamma(t)=q\}\bigr).
$$

If $q\in C\setminus\{(1,0)\}$, there are exactly two preimages, one in $(0,2\pi)$ and one in $(2\pi,4\pi)$. At $(1,0)$ the preimages are $0,2\pi,4\pi$, so $N(1,0)=3$. Off $C$, $N=0$. The single exceptional image point has $\mathcal H^1$ measure zero. The weighted area formula therefore reads

$$
\begin{aligned}
\int_0^{4\pi}w(\gamma(t))|\gamma'(t)|\,dt
&=\int_C\sum_{t\in\gamma^{-1}(q)\cap A}w(q)\,d\mathcal H^1(q)\\
&=\int_C w(q)N(q)\,d\mathcal H^1(q)
=2\int_C w\,d\mathcal H^1.
\end{aligned}
$$

Consequently,

$$
\boxed{\int_C w\,d\mathcal H^1=\pi}.
$$

A single traversal $0\leq t\leq2\pi$ gives the same geometric answer directly: only the common endpoint is counted twice, and it is length-null.

For circulation, the integrand includes the velocity vector rather than its norm:

$$
F(\gamma(t))=(-\sin t,\cos t)=\gamma'(t),
\qquad F(\gamma(t))\cdot\gamma'(t)=1.
$$

Thus the double counterclockwise traversal has circulation

$$
\int_0^{4\pi}F(\gamma(t))\cdot\gamma'(t)\,dt=\boxed{4\pi},
$$

and a single counterclockwise traversal has circulation $2\pi$. A reversed single traversal has circulation $-2\pi$, whereas its scalar $w$-integral remains $\pi$. These circulation values are not integrals of the scalar function $w$.

Flux requires a chosen unit normal: it has the form $\int_C G\cdot n\,d\mathcal H^1$. For example, $G(x,y)=(x,y)$ has outward flux $2\pi$, since the outward normal is $n(q)=q$ and $G(q)\cdot n(q)=1$. Choosing the inward normal changes that flux to $-2\pi$. The positive measure $\mathcal H^1$ itself supplies neither a tangent orientation nor a normal orientation.

## Why the theorem applies

The domain $A$ is compact Borel and $\gamma$ is $C^1$ with bounded derivative. The nonnegative weight $t\mapsto w(\gamma(t))$ is Borel. Hence the weighted area formula applies even though $\gamma$ is not injective. Its fiber sum is explicit above. Integrability is also direct: the parameter integrand is bounded by $1$ on a finite interval. The same formula with weight $1$ shows $\mathcal H^1(C)=2\pi$, which justifies all bounded scalar and flux integrals used here.

## Pitfalls

- A parametrization's image alone does not determine its traversal integral. Multiplicity must be included.
- Multiplicity is a count, never a signed count in the scalar area formula. Opposite traversals add for scalar length even when their circulations cancel.
- Endpoint multiplicity is genuinely three at $(1,0)$ for the stated closed domain. Ignoring it is justified by its null image, not by claiming it is two everywhere.

## Reusable technique

Before using a noninjective parametrization, count its fibers. The area formula converts a parameter integral into an integral of an explicit sum over preimages. Treat orientation separately whenever a vector field is present.

Tags: `area-formula`, `multiplicity`, `noninjective-parametrization`, `scalar-versus-vector`, `circulation`, `flux`.

## Sources

- Leon Simon, [*Introduction to Geometric Measure Theory* (2018)](https://math.stanford.edu/~lms/ntu-gmt-text.pdf), Chapter 1, §2, definitions 2.1–2.2 and Theorem 2.6; Chapter 2, §3, Theorem 3.3 and Remark 3.4(2) (weighted fiber sum). The fiber count and vector comparisons above are direct computations. Source ID: `simon-gmt`.
