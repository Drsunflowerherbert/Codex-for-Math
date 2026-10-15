# E09 — Height integral over a paraboloid graph

## Problem

Let $D=\{(x,y)\in\mathbb R^2:x^2+y^2\leq1\}$ and

$$
S=\{(x,y,x^2+y^2):(x,y)\in D\}.
$$

For the height function $h:S\to\mathbb R$, $h(x,y,z)=z$, compute $\int_S h\,d\mathcal H^2$. Also compute the area of $S$.

## Data and hypotheses

All measures are positive scalar measures. The normalized Hausdorff measure has covering cost $\alpha_k(\operatorname{diam}U/2)^k$, with $\alpha_k=\mathcal L^k(B^k(0,1))$; it agrees with $\mathcal L^k$ on $k$-planes. Thus the cost for $\mathcal H^2$ is $(\pi/4)(\operatorname{diam}U)^2$, and $\mathcal H^0$ is counting measure.

Write $u:D\to\mathbb R$, $u(x,y)=x^2+y^2$, and $\Phi:D\to\mathbb R^3$, $\Phi(x,y)=(x,y,u(x,y))$. The domain $D$ is compact Borel. The map $\Phi$ is injective because its first two coordinates recover its input. The function $h$ is continuous with $0\leq h\leq1$ on $S$.

## Solution

Compute the derivative columns and their Gram matrix:

$$
\partial_x\Phi=(1,0,2x),\qquad
\partial_y\Phi=(0,1,2y),
$$

$$
(D\Phi)^T D\Phi=
\begin{pmatrix}1+4x^2&4xy\\4xy&1+4y^2\end{pmatrix}.
$$

Its determinant is

$$
(1+4x^2)(1+4y^2)-16x^2y^2=1+4x^2+4y^2.
$$

Hence the two-dimensional area factor is

$$
J_2\Phi(x,y)=\sqrt{1+4x^2+4y^2}
=\sqrt{1+|\nabla u(x,y)|^2}.
$$

Injectivity and the weighted area formula give

$$
\int_S h\,d\mathcal H^2
=\int_D h(\Phi(x,y))J_2\Phi(x,y)\,d\mathcal L^2(x,y)
=\int_D(x^2+y^2)\sqrt{1+4x^2+4y^2}\,dx\,dy.
$$

The function $h$ is defined on $S$; its pulled-back value is $h(\Phi(x,y))=u(x,y)$. Now use polar coordinates in the planar disk, including their separate Jacobian factor $r$:

$$
I=2\pi\int_0^1 r^3\sqrt{1+4r^2}\,dr.
$$

For $v=1+4r^2$, we have $r\,dr=dv/8$ and $r^2=(v-1)/4$, so

$$
\begin{aligned}
I&=\frac{\pi}{16}\int_1^5(v-1)v^{1/2}\,dv\\
&=\frac{\pi}{16}\left[\frac25v^{5/2}-\frac23v^{3/2}\right]_1^5\\
&=\frac{\pi}{16}\left(\frac{20\sqrt5}{3}+\frac4{15}\right)
=\boxed{\frac{\pi(25\sqrt5+1)}{60}}.
\end{aligned}
$$

Using weight $1$ instead gives

$$
\begin{aligned}
\mathcal H^2(S)
&=2\pi\int_0^1r\sqrt{1+4r^2}\,dr\\
&=\frac\pi4\int_1^5v^{1/2}\,dv
=\boxed{\frac{\pi(5\sqrt5-1)}6}.
\end{aligned}
$$

As a quick consistency check, $0<I<\mathcal H^2(S)$, as expected because the height lies between $0$ and $1$ and is strictly between them on a set of positive area.

## Why the theorem applies

On the convex disk, $|\nabla u|\leq2$, so $|u(p)-u(q)|\leq2|p-q|$ and $|\Phi(p)-\Phi(q)|\leq\sqrt5|p-q|$. Thus $\Phi$ is Lipschitz on $D$. Its image is compact Borel, its multiplicity is one, and the weight is nonnegative Borel. The explicit area factor is bounded by $\sqrt5$, so both pulled-back integrands are integrable on $D$. The polar coordinate change is applied to a bounded, nonnegative measurable function; its seam and origin have planar measure zero. The area formula handles the closed disk directly, so there is no need to assume an open parameter domain or discard the boundary without explanation.

## Pitfalls

- The projected integral $\int_D u\,dx\,dy=\pi/2$ differs from the surface integral. Projection omits the graph's area factor.
- There are two distinct factors after the two changes of variables: $\sqrt{1+4r^2}$ comes from graph area; $r$ comes from planar polar coordinates.
- The cross product $(-2x,-2y,1)$ can also compute the area factor, but only its norm enters this scalar integral. A signed vector flux would additionally require a chosen normal.

## Reusable technique

For a graph $z=u(x,y)$ with one point above each base point, pull the scalar weight back and multiply by $\sqrt{1+|\nabla u|^2}$. If the domain and pulled-back integrand are radial, use polar coordinates only after forming this graph factor.

Tags: `graph-area`, `weighted-surface-integral`, `gram-determinant`, `polar-coordinates`, `injective-area-formula`, `substitution`.

## Sources

- Leon Simon, [*Introduction to Geometric Measure Theory* (2018)](https://math.stanford.edu/~lms/ntu-gmt-text.pdf), Chapter 1, §2, definitions 2.1–2.2 and Theorem 2.6; Chapter 2, §3, definition 3.2, Theorem 3.3, Remark 3.4(2), and Example 3.5(3) (graph area factor). The Gram determinant, substitutions, and numerical constants above are derived here. Source ID: `simon-gmt`.
