# Authored solution: Yau 2023 written Analysis, Problem 4

**Spoiler warning:** this file contains the limit and a complete proof. The [hints](../hints/yau-2023-analysis-p4.md) are separate.

**Status:** original authored solution; accepted in an independent ordinary mathematical review by agent proof_2014 on 2026-10-13. See the [review record](../reviews/yau-2023-analysis-p4.md). No formal verification is claimed.

**Problem ID:** `yau-2023-written-main-p4`. **Official solution access:** none located in the inspected official archive and bounded domain checks; this does not establish that no official solution exists.

**Source:** [official past-paper archive](https://yau-contest.com/en/lists-jxxg.html), [written-paper ZIP](https://yau-contest.com/index/reldown?en=1&id=9), retrieved 2026-10-13 at 04:38:28 UTC. Exact member: `2010-2026历年笔试真题/2023/Analysis and differential equation.pdf`, printed page 2, Problem 4. The PDF was checked visually, including the period, space, argument (nt), and positive-integer indexing. PDF SHA-256: `7c776d196d1ef100056e6ca70b1d56c390470faecf78a1158489d587410b44fb`. No source correction is required for this problem.

The mathematical setup used below is a $2\pi$-periodic $L^2([0,2\pi])$ function $x$, with $x_n(t)=x(nt)$ for $n=1,2,\ldots$. We identify its weak limit. The paper does not specify real or complex scalars; the proof covers both.

## Conventions and answer

Write $d\mu(t)=dt/(2\pi)$ on $[0,2\pi]$, and use

$$
\langle f,h\rangle=\int_0^{2\pi} f(t)\overline{h(t)}\,d\mu(t),
\qquad \|f\|_2^2=\int_0^{2\pi}|f(t)|^2\,d\mu(t).
$$

Multiplying the usual $L^2$ inner product by a positive constant does not change weak convergence. In the real case the conjugate can be omitted.

The limit is the constant function with value

$$
m=\int_0^{2\pi}x(t)\,d\mu(t)
=\frac1{2\pi}\int_0^{2\pi}x(t)\,dt.
$$

An $L^2$ element is an equivalence class modulo null sets. Choose a measurable representative on $[0,2\pi)$ and extend it periodically to $\mathbb R$. For fixed positive integer $n$, the map $t\mapsto nt\pmod{2\pi}$ is affine on each of $n$ subintervals. Its preimage of a null set is therefore null. Thus the class of $x_n$ is independent of the chosen representative. Values at interval endpoints have no effect.

## Direct proof by averaging over intervals

Set $y=x-m$, so $\int y\,d\mu=0$, and let $y_n(t)=y(nt)=x_n(t)-m$. For $j=0,\ldots,n-1$, put

$$
I_{n,j}=\left[\frac{2\pi j}{n},\frac{2\pi(j+1)}{n}\right).
$$

The substitution $s=nt-2\pi j$, followed by periodicity, gives

$$
\int_{I_{n,j}}y(nt)\,dt
=\frac1n\int_0^{2\pi}y(s)\,ds=0.
\tag{1}
$$

Applying the same substitution to $|y|^2$ on every interval gives

$$
\|y_n\|_2^2
=\frac1{2\pi}\sum_{j=0}^{n-1}\frac1n
\int_0^{2\pi}|y(s)|^2\,ds
=\|y\|_2^2.
\tag{2}
$$

First let $g\in C([0,2\pi])$. Its modulus of continuity is

$$
\omega_g(\delta)=
\sup\{|g(t)-g(s)|:s,t\in[0,2\pi],\ |t-s|\leq\delta\},
$$

which tends to zero as $\delta\downarrow0$. Equation (1) allows us to subtract $g(2\pi j/n)$ on the $j$-th interval. Consequently,

$$
\begin{aligned}
|\langle y_n,g\rangle|
&=\left|\sum_{j=0}^{n-1}
\int_{I_{n,j}}y(nt)
\overline{\left(g(t)-g(2\pi j/n)\right)}\,d\mu(t)\right|\\
&\leq \omega_g(2\pi/n)\int_0^{2\pi}|y_n(t)|\,d\mu(t)\\
&\leq \omega_g(2\pi/n)\|y_n\|_2
=\omega_g(2\pi/n)\|y\|_2.
\tag{3}
\end{aligned}
$$

The second inequality is Cauchy–Schwarz, using $\mu([0,2\pi])=1$.

Now fix an arbitrary $h\in L^2([0,2\pi])$ and $\varepsilon>0$. If $C:=\|y\|_2=0$, the required pairing is already zero for every $n$. Otherwise, density of continuous functions in $L^2$ gives $g\in C([0,2\pi])$ such that

$$
\|h-g\|_2<\frac{\varepsilon}{2C}.
$$

Choose $N\geq1$ so that $\omega_g(2\pi/N)<\varepsilon/(2C)$. For every $n\geq N$, equations (2)–(3) and Cauchy–Schwarz imply

$$
\begin{aligned}
|\langle x_n-m,h\rangle|
&\leq |\langle y_n,h-g\rangle|+|\langle y_n,g\rangle|\\
&\leq C\|h-g\|_2+C\omega_g(2\pi/n)
<\varepsilon.
\end{aligned}
$$

This proves $x_n\rightharpoonup m$ in $L^2([0,2\pi])$.

## Alternative proof using trigonometric polynomials

This approach uses density of trigonometric polynomials in $L^2$, with the same norm bound (2). Its coefficient computation also explains why each fixed nonconstant frequency eventually disappears.

For an integer $k$, split the integral into the $n$ intervals and use the same substitution:

$$
\int_0^{2\pi}y(nt)e^{-ikt}\,d\mu(t)
=\frac1n\left(\sum_{j=0}^{n-1}e^{-2\pi i k j/n}\right)
\int_0^{2\pi}y(s)e^{-iks/n}\,d\mu(s).
\tag{4}
$$

For $k=0$, the integral on the right is zero because $y$ has mean zero. For $k\ne0$ and $n>|k|$, the root-of-unity sum is zero: its ratio is not 1 and its $n$-th power is 1. Thus, if $P(t)=\sum_{|k|\leq M}a_ke^{ikt}$, then

$$
\langle y_n,P\rangle=0\qquad(n>M).
$$

Given $h\in L^2$, $\varepsilon>0$, and $C=\|y\|_2>0$, choose such a $P$ with $\|h-P\|_2<\varepsilon/C$. For every $n>M$,

$$
|\langle y_n,h\rangle|
=|\langle y_n,h-P\rangle|
\leq C\|h-P\|_2<\varepsilon.
$$

The case $C=0$ was already covered. This proves the same weak limit without requiring a pointwise Fourier expansion of $x$.

## Consequence

Equation (2) also shows that $\|x_n-m\|_2=\|x-m\|_2$ for every $n$. Hence convergence to the weak limit is strong exactly when $x=m$ almost everywhere. This consequence uses no additional regularity assumption.

## Review record

- Author check: source page and numbering, null-set issue, integer-indexed change of variables, mean normalization, complex conjugation, density estimates, and the alternative coefficient formula checked on 2026-10-13.
- Independent review: agent proof_2014 accepted the direct proof, Fourier alternative, consequence, and hints on 2026-10-13; see the [review record](../reviews/yau-2023-analysis-p4.md).
- Unresolved mathematical steps: none identified in author and independent reviews; standard $L^2$ density theorems are used explicitly.
