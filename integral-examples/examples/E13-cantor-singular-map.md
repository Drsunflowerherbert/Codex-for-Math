# E13 — A singular map loses all its increase under differentiation

## Problem

Construct a continuous nondecreasing map $C:[0,1]\to[0,1]$ with $C(0)=0$, $C(1)=1$, and $C'=0$ almost everywhere. Compare
$$
\int_0^1|C'(x)|\,dx
\quad\text{with}\quad
\int_{\mathbb R}\mathcal H^0\bigl(C^{-1}(\{y\})\bigr)\,dy.
$$
Explain exactly why the Lipschitz area formula and the fundamental theorem for absolutely continuous functions cannot be applied to $C$. Use the construction to exhibit concentration that prevents exchanging a derivative limit with an integral, even though the functions themselves converge uniformly.

## Data and hypotheses

The source and target use completed one-dimensional Lebesgue measure $\mathcal L^1$. Normalized $\mathcal H^1$ equals $\mathcal L^1$ on a line; the covering normalization in dimension $k\geq1$ is $\alpha_k(\operatorname{diam}U)^k/2^k$. The measure $\mathcal H^0$ counts points, so an infinite fibre has value $+\infty$.

Derivatives will be used as almost-everywhere defined functions. Any undefined values on an explicitly identified null set may be assigned zero to obtain a measurable representative. This convention does not assert differentiability there. All finite-stage approximations below are piecewise linear and absolutely continuous; their limit will fail absolute continuity.

## Solution

**1. Build the set and the approximations.** Let $K_0=[0,1]$. Obtain $K_{n+1}$ from $K_n$ by removing the open middle third of each component interval. The set $K_n$ has $2^n$ disjoint closed component intervals, each of length $3^{-n}$. Thus
$$
\mathcal L^1(K_n)=2^n3^{-n}=\left(\frac23\right)^n.
$$
The compact Cantor set $K=\bigcap_{n=0}^{\infty}K_n$ is null by continuity of finite measure from above. It therefore has empty interior, because every nondegenerate interval has positive Lebesgue measure.

Define $C_n$ to be the continuous nondecreasing function that is constant on each gap removed by stage $n$, rises linearly by $2^{-n}$ on each component interval of $K_n$, and satisfies $C_n(0)=0$. These rules uniquely determine it, with $C_n(1)=1$. For example $C_0(x)=x$, while $C_1$ rises from $0$ to $1/2$ on $[0,1/3]$, is constant $1/2$ on $[1/3,2/3]$, and rises to $1$ on $[2/3,1]$.

All later approximations retain the endpoint values of every stage-$n$ component interval. Within such an interval both $C_m$ and $C_n$, for $m\geq n$, remain between endpoint values separated by $2^{-n}$; on previously removed gaps they agree. Therefore
$$
\sup_{x\in[0,1]}|C_m(x)-C_n(x)|\leq2^{-n}\qquad(m\geq n).
$$
The sequence converges uniformly to a continuous nondecreasing function $C$. The endpoint values persist, so $C(0)=0$, $C(1)=1$, and the intermediate value theorem gives $C([0,1])=[0,1]$. This construction avoids all ambiguity of ternary expansions at interval endpoints.

**2. Compute the almost-everywhere derivative.** Every $x\in[0,1]\setminus K$ lies in an open gap removed at a finite stage. All sufficiently late $C_n$, and hence $C$, are constant on that gap. Thus $C'(x)=0$ at every such $x$. Since $\mathcal L^1(K)=0$, $C'=0$ almost everywhere. Assigning zero on $K$ yields the zero function as a measurable representative, and therefore
$$
\int_0^1|C'|\,d\mathcal L^1=0,
\qquad C(1)-C(0)=1.
$$
We do not claim that $C'$ exists at every point of $K$.

**3. Compute the multiplicity on the target.** Let $P$ be the set of constant values of $C$ on its deleted open gaps. There are countably many gaps, so $P$ is countable; these plateau values are dyadic rationals. If two points $a<b$ satisfy $C(a)=C(b)=y$, monotonicity forces $C$ to be constant on $[a,b]$. Because $K$ has empty interior, $(a,b)$ contains part of a deleted gap, so $y\in P$. Consequently every $y\in[0,1]\setminus P$ has exactly one preimage, using surjectivity for existence. Every $y\in P$ has infinitely many preimages, including an entire gap. Thus the counting function $N$ has values
$$
N(C,[0,1],y)=
\begin{cases}
1,&y\in[0,1]\setminus P,\\
+\infty,&y\in P,\\
0,&y\notin[0,1].
\end{cases}
$$
It is measurable, and the infinite values on the countable null set $P$ do not change its nonnegative Lebesgue integral. Hence
$$
\int_{\mathbb R}N(C,[0,1],y)\,dy=1\ne0=\int_0^1|C'|\,dx.
$$
This is a failed extension of the Lipschitz area identity to a continuous, almost-everywhere differentiable map.

**4. Identify the exact regularity failure.** On the leftmost stage-$n$ interval, $C(3^{-n})-C(0)=2^{-n}$. The corresponding difference quotient is $(3/2)^n$, so no finite Lipschitz constant exists.

Absolute continuity fails directly as well. For the $2^n$ basic intervals $[a_{n,j},b_{n,j}]$ at stage $n$,
$$
\sum_{j=1}^{2^n}(b_{n,j}-a_{n,j})=(2/3)^n\longrightarrow0,
\qquad
\sum_{j=1}^{2^n}|C(b_{n,j})-C(a_{n,j})|
=\sum_{j=1}^{2^n}2^{-n}=1.
$$
Taking $\varepsilon=1/2$ contradicts the defining absolute-continuity condition for every proposed $\delta>0$.

There is also an image-of-null-set obstruction. Every plateau value has a preimage at a gap endpoint belonging to $K$, while any preimage outside $K$ lies in a gap. Together with surjectivity this proves $C(K)=[0,1]$. Thus this map sends a null set to a set of measure one. In contrast, a Lipschitz map on a line sends null sets to null sets: cover the source null set by intervals of arbitrarily small total length, then cover their images by intervals whose lengths are at most the Lipschitz constant times those lengths. Discarding a source null set is therefore unsafe for this singular map.

**5. See concentration in the derivatives.** At all but finitely many breakpoints,
$$
C_n'(x)=\left(\frac32\right)^n\mathbf1_{K_n}(x).
$$
Choose the displayed right side as an almost-everywhere representative, denoted $q_n$. Then
$$
\int_0^1q_n(x)\,dx
=\left(\frac32\right)^n\left(\frac23\right)^n=1,
\qquad q_n\longrightarrow0\quad\mathcal L^1\text{-almost everywhere}.
$$
Thus $\int\lim q_n=0$ while $\lim\int q_n=1$. The mass stays inside a bounded interval and concentrates on the shrinking sets $K_n$ containing the null set $K$; it does not escape to infinity.

There is no common integrable dominator. If $q_n\leq G$ almost everywhere for $G\in L^1$, then $\int_{K_n}|G|\geq1$ for every $n$. Dominated convergence applied to $|G|\mathbf1_{K_n}\to0$ almost everywhere would instead give $\int_{K_n}|G|\to0$, a contradiction. The sequence also fails uniform integrability, since $\mathcal L^1(K_n)\to0$ but $\int_{K_n}q_n=1$.

## Why the theorem applies

The continuity-of-measure, uniform-limit, and nonnegative integration arguments used in the construction have their stated hypotheses. The area formula is used only as a comparison theorem: its Lipschitz hypothesis fails for $C$, so its equality is not asserted. The absolute-continuity fundamental theorem similarly does not apply to $C$.

A useful positive replacement is the following. If $F_n$ are absolutely continuous on $[0,1]$, $F_n(0)\to a$, $F_n'\to q$ almost everywhere, and $|F_n'|\leq G\in L^1$ almost everywhere, then dominated convergence gives
$$
\sup_{x\in[0,1]}\left|F_n(x)-a-\int_0^xq(t)\,dt\right|
\leq |F_n(0)-a|+\int_0^1|F_n'-q|\,dt\longrightarrow0.
$$
Here $q\in L^1$ because $|q|\leq G$ almost everywhere, and the limit is absolutely continuous with derivative $q$ almost everywhere. This is a precise sufficient condition for retaining derivatives under the limit; the Cantor approximations violate the domination condition.

## Pitfalls

- Uniform convergence of functions does not supply domination of their derivatives.
- An almost-everywhere zero derivative alone does not make a continuous function constant. Absolute continuity restores that conclusion.
- An infinite multiplicity at countably many target values is harmless for this target integral; a null source set with a full-measure image is a different issue.
- This does not contradict a smooth Sard theorem: $C$ is not a smooth map, and the exceptional domain set cannot be removed while preserving its image measure.

## Reusable technique

Track where derivative mass lives, not just the pointwise limit. Check absolute continuity or the actual regularity required by area/change-of-variables formulas; test whether null source sets can have large images. Tags: `singular-map`, `cantor-function`, `absolute-continuity`, `area-formula-failure`, `concentration`, `dominated-convergence-failure`, `uniform-integrability`, `derivative-limit`.

## Sources

- John K. Hunter, [*Measure Theory*](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf), Example 2.14 (Cantor-set nullity), Example 2.37 (singular Cantor measure), and the opening of Chapter 6, printed pp. 19, 31, 63; source ID `hunter-measure`. These give background on the standard set and the absolute-continuity obstruction; the construction and calculations above are supplied explicitly.
- Leon Simon, [*Introduction to Geometric Measure Theory*](https://math.stanford.edu/~lms/ntu-gmt-text.pdf), Chapter 2, §3, Theorem 3.3 and Remark 3.4(2), printed pp. 57–58; source ID `simon-gmt`. The Lipschitz area theorem is the precise formula whose unjustified extension is disproved here.
