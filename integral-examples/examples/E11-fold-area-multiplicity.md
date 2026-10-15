# E11 — A fold counts the image twice

## Problem

Let $A=[-1,1]\times[0,1]$ and define the map $F:A\to\mathbb R^2$ by
$$
F(u,v)=(u^2,v).
$$
Compute the image area, the integral of the area Jacobian over $A$, and the weighted integral
$$
\int_A (u^2+v)J_2F(u,v)\,d\mathcal L^2(u,v).
$$
Explain why an injective change-of-variables formula would give the wrong answer. Then recover the scalar integral of $h(x,y)=x+y$ over the image, counted once.

## Data and hypotheses

The domain and target measures are completed two-dimensional Lebesgue measure $\mathcal L^2$. We use normalized Hausdorff measure
$$
\mathcal H^k(E)=\lim_{\delta\downarrow0}\inf\left\{
\sum_j\frac{\alpha_k}{2^k}(\operatorname{diam}U_j)^k:
E\subseteq\bigcup_jU_j,\ \operatorname{diam}U_j<\delta\right\},
$$
where $\alpha_k$ is the volume of the unit ball in $\mathbb R^k$. Thus $\mathcal H^k$ agrees with $\mathcal L^k$ on a $k$-plane; $\mathcal H^0$ is counting measure.

The set $A$ is compact and Borel. The map $F$ is the restriction of a smooth map, and is Lipschitz on $A$: $|u^2-s^2|\leq2|u-s|$ for $u,s\in[-1,1]$ gives $|F(u,v)-F(s,t)|\leq2|(u,v)-(s,t)|$. The scalar function $h$ is continuous and nonnegative on the image. All integrals computed below are finite. The multiplicity is the function
$$
N(F,A,z)=\mathcal H^0\bigl(A\cap F^{-1}(\{z\})\bigr),
$$
not the map $F$ itself and not a chosen inverse branch.

## Solution

**1. Compute the image and every fibre.** The image is $Q=[0,1]\times[0,1]$. For $z=(x,y)\in Q$ with $x>0$, the fibre consists of the two distinct points
$$
A\cap F^{-1}(\{(x,y)\})=\{(\sqrt x,y),(-\sqrt x,y)\}.
$$
At $x=0$ it consists of the single point $(0,y)$, and outside $Q$ it is empty. Consequently $N=2$ on $(0,1]\times[0,1]$, $N=1$ on $\{0\}\times[0,1]$, and $N=0$ elsewhere. In particular $N=2$ at $\mathcal L^2$-almost every point of $Q$.

**2. Compute the area Jacobian.** Differentiating the map gives
$$
DF(u,v)=\begin{pmatrix}2u&0\\0&1\end{pmatrix},\qquad
J_2F(u,v)=\sqrt{\det(DF^TDF)}=|\det DF|=2|u|.
$$
The critical set is $\{0\}\times[0,1]$, where the rank drops to one. Its image is the left edge of $Q$; both sets have $\mathcal L^2$-measure zero. We do not need to define an inverse derivative there.

**3. Compare image area with the parameter integral.** The image area is
$$
\mathcal H^2(F(A))=\mathcal L^2(Q)=1.
$$
Direct integration, justified by Tonelli for the nonnegative Borel integrand, gives
$$
\int_A J_2F\,d\mathcal L^2
=\int_{-1}^1\int_0^1 2|u|\,dv\,du
=4\int_0^1u\,du=2.
$$
The area formula explains the factor:
$$
\int_A J_2F\,d\mathcal L^2
=\int_{\mathbb R^2}N(F,A,z)\,d\mathcal H^2(z)=2\mathcal L^2(Q).
$$
The extra unit is an entire second sheet, not an error caused by a negligible boundary.

**4. Keep the fibre sum in the weighted formula.** Write the source weight as $h\circ F$, whose value at $(u,v)$ is $u^2+v$. The weighted area formula gives
$$
\begin{aligned}
\int_A(h\circ F)J_2F\,d\mathcal L^2
&=\int_{\mathbb R^2}
\sum_{(u,v)\in A\cap F^{-1}(\{z\})}h(F(u,v))\,d\mathcal H^2(z)\\
&=\int_Qh(z)N(F,A,z)\,d\mathcal L^2(z)\\
&=2\int_0^1\int_0^1(x+y)\,dy\,dx=2.
\end{aligned}
$$
An independent direct calculation is
$$
\begin{aligned}
\int_{-1}^1\int_0^1(u^2+v)2|u|\,dv\,du
&=4\int_0^1\left(u^3+\frac u2\right)du\\
&=4\left(\frac14+\frac14\right)=2.
\end{aligned}
$$
Thus a substitution that simply writes this parameter integral as $\int_Qh$ loses multiplicity.

**5. Count the image once.** Restrict $F$ to $A_+=[0,1]\times[0,1]$. This restriction is injective, including its boundary. Its Jacobian may vanish at $u=0$; injectivity and Lipschitz regularity are still enough for the area formula. It follows that
$$
\int_Qh\,d\mathcal H^2
=\int_0^1\int_0^1(u^2+v)2u\,dv\,du=1.
$$
Alternatively, divide the original parameter integral by two: $N(F,A,F(u,v))=2$ away from $u=0$, and that exceptional line is null. For this particular map,
$$
\int_Qh\,d\mathcal H^2=\frac12\int_A(h\circ F)J_2F\,d\mathcal L^2=1.
$$
A constant divisor works here because the multiplicity is constant almost everywhere on the image. Variable multiplicity requires the actual fibre count.

## Why the theorem applies

The area formula applies to a Lipschitz map on a Lebesgue-measurable domain, with nonnegative measurable weights. Its target integral contains the sum over all preimages in that domain. Those hypotheses hold here, so absolute integrability need not be assumed before obtaining the nonnegative identity. Finiteness then follows from the explicit computations. For a signed weight one must separately check integrability, for example $\int_A|h\circ F|J_2F<\infty$, before subtracting positive and negative parts.

## Pitfalls

- The unsigned Jacobian is $2|u|$, not $2u$. Indeed $\int_A\det DF\,d\mathcal L^2=0$ by oddness: opposite orientations cancel. Scalar Hausdorff area is positive and does not cancel.
- Scalar Hausdorff integration supplies no normal vector. Vector flux requires an oriented normal and a dot product, in addition to the surface measure.
- Noninjectivity cannot be dismissed by deleting only the critical line: the two regular sheets still have the same image.
- The inverse branch $x\mapsto\sqrt x$ has an unbounded derivative near zero. That does not invalidate this forward Lipschitz area calculation.

## Reusable technique

Find the fibres before changing variables. Compute $J_kF$ using $\sqrt{\det(DF^TDF)}$; keep the explicit preimage sum; then either choose an injective sheet or correct for verified multiplicity. Tags: `area-formula`, `multiplicity`, `fold`, `noninjective-parametrization`, `unsigned-jacobian`, `orientation`.

## Sources

- Leon Simon, [*Introduction to Geometric Measure Theory*](https://math.stanford.edu/~lms/ntu-gmt-text.pdf), Chapter 2, §3, Theorem 3.3 and Remark 3.4(2), printed pp. 57–58; source ID `simon-gmt`. The same-dimensional specialization used here has target measure $\mathcal H^2=\mathcal L^2$. The worked fold and calculations above are original to this collection.
