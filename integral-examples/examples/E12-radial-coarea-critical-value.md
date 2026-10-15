# E12 — Coarea for squared distance, including the critical value

## Problem

Let $D=\{(x,y)\in\mathbb R^2:x^2+y^2\leq1\}$ and define $g:\mathbb R^2\to\mathbb R$ by $g(x,y)=x^2+y^2$. For a nonnegative Borel function $\phi:[0,1]\to[0,\infty]$, prove
$$
\int_D\phi(g(x,y))\,d\mathcal L^2(x,y)
=\pi\int_0^1\phi(t)\,dt.
$$
Use coarea, making the treatment of $g^{-1}(\{0\})$ explicit. Also compute $\int_D|\nabla g|\,d\mathcal L^2$ and determine exactly when the radial singularity $(x^2+y^2)^a$ is integrable.

## Data and hypotheses

Planar integration uses completed Lebesgue measure $\mathcal L^2$. The level sets carry normalized $\mathcal H^1$, so their measure is ordinary arc length. In general our normalization uses the covering cost $\alpha_k(\operatorname{diam}U)^k/2^k$, with $\alpha_k$ the unit $k$-ball volume; it gives $\mathcal H^k=\mathcal L^k$ on a $k$-plane and $\mathcal H^0$ equal to counting measure.

The map $g$ is smooth on $\mathbb R^2$, the disk is Borel, and its one-dimensional coarea Jacobian is
$$
J_1g(x,y)=|\nabla g(x,y)|=2\sqrt{x^2+y^2}.
$$
The weight $\phi$ may be unbounded, and either side of the requested formula may be $+\infty$. No signed cancellation is permitted in this extended nonnegative statement. A value assigned to a function at the single point $(0,0)$ will not change its $\mathcal L^2$ integral.

## Solution

**1. Describe the levels and the critical set.** Put $r=\sqrt{x^2+y^2}$. For $0<t\leq1$ the level in $D$ is the circle of radius $\sqrt t$:
$$
D\cap g^{-1}(\{t\})=\{(\sqrt t\cos\theta,\sqrt t\sin\theta):0\leq\theta<2\pi\}.
$$
Its normalized $\mathcal H^1$ measure is $2\pi\sqrt t$. One can check this by the injective arc parametrization on $[0,2\pi)$: the speed is $\sqrt t$, so its length is $\int_0^{2\pi}\sqrt t\,d\theta$. At $t=0$ the level is the singleton $\{(0,0)\}$, whose $\mathcal H^1$ measure is zero. Outside $[0,1]$ the level in $D$ is empty.

The only critical point is $(0,0)$ because $\nabla g=(2x,2y)$. The only critical value is therefore $0$. Here this is a direct calculation, requiring no appeal to Sard's theorem. The regular levels are circles; the exceptional level is a point. Treating it separately avoids a division by zero.

**2. First apply coarea without dividing.** The weighted coarea formula for this smooth scalar map is
$$
\int_{\mathbb R^2}w(z)|\nabla g(z)|\,d\mathcal L^2(z)
=\int_{\mathbb R}\left(\int_{g^{-1}(\{t\})}w(z)\,d\mathcal H^1(z)\right)dt
$$
for nonnegative Borel $w$, with the usual convention that the product is zero where the Jacobian is zero. Taking $w=\mathbf1_D$ gives
$$
\int_D|\nabla g|\,d\mathcal L^2
=\int_0^1 2\pi\sqrt t\,dt
=\frac{4\pi}{3}.
$$
The value of the inner integral at $t=0$ is exactly zero. The value at the endpoint $t=1$ does not affect its one-dimensional Lebesgue integral.

**3. Divide only on the regular part.** Define a Borel function $w:\mathbb R^2\to[0,\infty]$ by
$$
w(z)=
\begin{cases}
\displaystyle\frac{\phi(g(z))}{2|z|},&z\in D\setminus\{0\},\\[4pt]
0,&z=0\text{ or }z\notin D.
\end{cases}
$$
On $D\setminus\{0\}$ one has $wJ_1g=\phi\circ g$. At zero the two functions may have different values, but this is a $\mathcal L^2$-null set. Consequently their nonnegative Lebesgue integrals agree, even if $\phi(0)=+\infty$.

For $0<t\leq1$, $w$ is constant on the level circle, with value $\phi(t)/(2\sqrt t)$. Hence the inner level integral is
$$
\int_{g^{-1}(\{t\})}w\,d\mathcal H^1
=\frac{\phi(t)}{2\sqrt t}\,2\pi\sqrt t
=\pi\phi(t).
$$
At $t=0$, the definition $w(0)=0$ makes the inner integral zero. Thus coarea proves
$$
\int_D\phi\circ g\,d\mathcal L^2
=\int_{(0,1]}\pi\phi(t)\,dt
=\pi\int_0^1\phi(t)\,dt.
$$
Only the integrals ignore the endpoints; no claim that $1/|\nabla g|$ is defined at every point has been made.

**4. Read off useful consequences.** For a real exponent $a$, assign any finite value at the origin to the function $z\mapsto|z|^{2a}$ if its literal formula is undefined there. On $(0,1]$ use $\phi(t)=t^a$, and assign $\phi(0)=0$. The preceding identity gives
$$
\int_D|z|^{2a}\,d\mathcal L^2(z)
=\begin{cases}
\displaystyle\frac{\pi}{a+1},&a>-1,\\[4pt]
+\infty,&a\leq-1.
\end{cases}
$$
In particular $|z|^{-1}$ is integrable on the disk, with integral $2\pi$, whereas $|z|^{-2}$ is not. The divergence occurs throughout arbitrarily small neighborhoods of zero; changing the value at zero cannot repair it.

For $0\leq a_0<b_0\leq1$, taking $\phi=\mathbf1_{(a_0,b_0)}$ gives the annular area $\pi(b_0-a_0)$ for $a_0<|z|^2<b_0$. Equivalently, if a random point is uniform in $D$ with probability measure $\pi^{-1}\mathcal L^2|_D$, its squared radius is uniform on $[0,1]$. These are both consequences of the same pushforward identity, not additional assumptions about polar coordinates.

## Why the theorem applies

The locally Lipschitz weighted coarea theorem applies to $g$ on $\mathbb R^2$, with the Borel weights above. Its Jacobian is the norm of the gradient because the target dimension is one. This polynomial is smooth and locally Lipschitz; global Lipschitz continuity on all of $\mathbb R^2$ is unnecessary. If using a formulation requiring a globally Lipschitz map, use $G(z)=\min\{|z|^2,4\}$. The function $r\mapsto\min\{r^2,4\}$ is $4$-Lipschitz on $[0,\infty)$, and $z\mapsto|z|$ is $1$-Lipschitz, so $G$ is globally $4$-Lipschitz and agrees with $g$ on a neighborhood of $D$.

For signed Borel $\phi$ with $\int_0^1|\phi(t)|\,dt<\infty$, first apply the nonnegative identity to $|\phi|$. This proves absolute integrability on $D$; applying the formula to $\phi^+$ and $\phi^-$ then gives the signed identity. If both sign parts have infinite integral, their difference is undefined.

## Pitfalls

- Coarea gives a factor $|\nabla g|=2r$, not its reciprocal. A reciprocal appears only because we deliberately choose a compensating weight on the regular part.
- A critical level need not be a regular curve. Its contribution must be checked, rather than parametrized as though its dimension were unchanged.
- The critical point being null does not by itself establish integrability of a singular weight near it; the power computation supplies the needed neighborhood estimate.
- These are scalar integrals over levels. No orientation or vector flux occurs.

## Reusable technique

For an integral depending on a scalar map $g$, compute the geometry of $g^{-1}(\{t\})$ and the coarea Jacobian, isolate the critical set, and choose a compensating weight only where the Jacobian is nonzero. Tags: `coarea`, `level-sets`, `radial-integral`, `critical-value`, `singular-weight`, `pushforward-measure`.

## Sources

- Leon Simon, [*Introduction to Geometric Measure Theory*](https://math.stanford.edu/~lms/ntu-gmt-text.pdf), Chapter 2, §7, Theorem 7.3, Remark 7.4(1), and Theorem 7.5, printed pp. 76, 80; source ID `simon-gmt`. The weighted coarea identity is the theorem used; the critical point and all integrals in this example are computed directly. Chapter 2, §3, Example 3.5(1) connects normalized $\mathcal H^1$ with arc length.
