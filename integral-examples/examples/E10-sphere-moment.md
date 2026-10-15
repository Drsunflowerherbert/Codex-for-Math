# E10 — A sphere's second moment and a spherical cap

## Problem

For $R>0$, let $S_R=\{(x,y,z)\in\mathbb R^3:x^2+y^2+z^2=R^2\}$. Compute the scalar integral of the function $h:S_R\to\mathbb R$, $h(x,y,z)=z^2$:

$$
\int_{S_R}h\,d\mathcal H^2.
$$

As a related application, compute the area of a cap of height $a\in[0,2R]$ defined by $z\geq R-a$.

## Data and hypotheses

Use normalized Hausdorff measure: the covering cost is $\alpha_k(\operatorname{diam}U/2)^k$, where $\alpha_k$ is the $k$-dimensional unit-ball volume. This makes $\mathcal H^k$ equal to $\mathcal L^k$ on $k$-planes; $\mathcal H^0$ is counting measure. Thus $\mathcal H^2$ has covering cost $(\pi/4)(\operatorname{diam}U)^2$ and is usual surface area on a smooth surface. The sphere and cap are compact Borel sets, and $h$ is continuous and nonnegative.

## Solution

Use the spherical map

$$
\Phi(\theta,\varphi)
=(R\sin\theta\cos\varphi,R\sin\theta\sin\varphi,R\cos\theta),
$$

on $D=(0,\pi)\times(0,2\pi)$. Its derivative columns are perpendicular, with lengths $R$ and $R\sin\theta$. Therefore

$$
J_2\Phi(\theta,\varphi)=R^2\sin\theta.
$$

The map is injective on $D$: $z/R$ determines $\theta\in(0,\pi)$, and the first two coordinates then determine the unique $\varphi\in(0,2\pi)$. Its image omits exactly the meridian

$$
M=\{(R\sin\theta,0,R\cos\theta):0\leq\theta\leq\pi\},
$$

including the poles. This omitted set is $\mathcal H^2$-null. Indeed, its displayed curve is $R$-Lipschitz; partitioning $[0,\pi]$ into $N$ intervals covers $M$ by $N$ sets of diameter at most $R\pi/N$. Their total normalized two-dimensional cost is at most $\pi^3R^2/(4N)$, tending to zero, while their maximum diameter also tends to zero.

The weighted area formula now gives

$$
\begin{aligned}
\int_{S_R}h\,d\mathcal H^2
&=\int_0^{2\pi}\int_0^\pi
R^2\cos^2\theta\,R^2\sin\theta\,d\theta\,d\varphi\\
&=2\pi R^4\int_0^\pi\cos^2\theta\sin\theta\,d\theta.
\end{aligned}
$$

With $v=\cos\theta$, $dv=-\sin\theta\,d\theta$,

$$
\int_0^\pi\cos^2\theta\sin\theta\,d\theta
=\int_{-1}^1v^2\,dv=\frac23,
$$

so

$$
\boxed{\int_{S_R}z^2\,d\mathcal H^2=\frac{4\pi R^4}{3}}.
$$

The same parametrization with weight $1$ gives $\mathcal H^2(S_R)=4\pi R^2$. A separate check uses coordinate symmetry: Hausdorff measure is unchanged by rotations, so the integrals of $x^2$, $y^2$, and $z^2$ are equal. Their sum is

$$
\int_{S_R}(x^2+y^2+z^2)\,d\mathcal H^2
=R^2\mathcal H^2(S_R)=4\pi R^4.
$$

For the cap, set $\theta_0=\arccos(1-a/R)$. The condition $z\geq R-a$ is $0\leq\theta\leq\theta_0$. Thus

$$
\mathcal H^2(\{q\in S_R:z(q)\geq R-a\})
=2\pi R^2\int_0^{\theta_0}\sin\theta\,d\theta
=\boxed{2\pi Ra}.
$$

This includes $a=0$ (a single point, area zero) and $a=2R$ (the entire sphere).

## Why the theorem applies

The map $\Phi$ extends smoothly to the closed rectangle $[0,\pi]\times[0,2\pi]$, with bounded derivative, hence is Lipschitz there and on $D$. The restricted domain $D$ is Borel and has multiplicity one on its image. Its Jacobian is bounded by $R^2$, while $h\circ\Phi$ is bounded by $R^2$ on a finite-measure rectangle. All scalar integrals are therefore finite. The missing meridian is null by the covering argument above. Nonnegative integrands justify the iterated integrations by Tonelli; finiteness also permits Fubini. Cap boundary latitudes are Lipschitz curves and hence $\mathcal H^2$-null by the same covering argument.

## Pitfalls

- The factor $R^2\sin\theta$ is essential. The angular parameter rectangle carries planar measure, not surface measure.
- The closed-rectangle parametrization is not injective at the seam or poles. Restricting to $D$ and proving that the omitted image is null resolves this explicitly.
- This scalar moment has no chosen orientation. For a vector field $G(q)=q$, the outward unit normal is $n(q)=q/R$ and the outward flux is $\int_{S_R}G\cdot n\,d\mathcal H^2=R\mathcal H^2(S_R)=4\pi R^3$. The inward normal reverses that flux, while the $z^2$ integral remains unchanged.

## Reusable technique

Compute a surface Jacobian from the Gram determinant or perpendicular tangent vectors. Separate chart overlap/null-image issues from the calculation. Use rotation symmetry to check coordinate moments, and express caps through their polar angle or height.

Tags: `sphere`, `surface-moment`, `spherical-cap`, `area-formula`, `null-seam`, `rotation-symmetry`, `scalar-versus-flux`.

## Sources

- Leon Simon, [*Introduction to Geometric Measure Theory* (2018)](https://math.stanford.edu/~lms/ntu-gmt-text.pdf), Chapter 1, §2, definitions 2.1–2.2 and Theorem 2.6; Chapter 2, §3, definition 3.2, Theorem 3.3, Remark 3.4(2), and Example 3.5(2) (surface measure and area formula). The chart, null-meridian proof, moment, cap computation, and symmetry check above are derived here. Source ID: `simon-gmt`.
