# E04 — Two finite iterated integrals, but no signed Lebesgue integral

## Problem

On $Q=(0,1)^2$, define the real-valued function

$$
f(x,y)=\frac{x^2-y^2}{(x^2+y^2)^2}.
$$

Compute both iterated integrals. Determine whether $\int_Q f\,d\mathcal L^2$ exists as a signed Lebesgue integral, and explain exactly which hypothesis prevents use of signed Fubini.

## Data and hypotheses

The measure on $Q$ is the restriction of planar Lebesgue measure $\mathcal L^2$. Inner and outer one-variable integrals use $\mathcal L^1$. The function $f$ is continuous on the open square, so it is Borel measurable. Its singularity is approached as $(x,y)\to(0,0)$, although that point is outside $Q$.

For a real-valued measurable function, put $f^+=\max(f,0)$ and $f^-=\max(-f,0)$. The signed Lebesgue integral is $\int f^+-\int f^-$ only when these two quantities are not both infinite. A finite signed Lebesgue integral requires $\int|f|<\infty$.

## Solution

**1. Integrate with respect to $y$ first.** Fix $x\in(0,1)$. As a function of $y\in[0,1]$, the formula extends continuously and is bounded, so this section is absolutely integrable. Direct differentiation gives

$$
\frac{\partial}{\partial y}\left(\frac{y}{x^2+y^2}\right)
=\frac{x^2-y^2}{(x^2+y^2)^2}.
$$

Consequently

$$
\int_0^1 f(x,y)\,dy
=\left[\frac{y}{x^2+y^2}\right]_{y=0}^{y=1}
=\frac1{1+x^2},
$$

and the resulting outer function is integrable:

$$
\int_0^1\left(\int_0^1f(x,y)\,dy\right)dx
=\int_0^1\frac{dx}{1+x^2}
=\boxed{\frac\pi4}.
$$

**2. Integrate with respect to $x$ first.** For each fixed $y\in(0,1)$, the section is again continuous and bounded on $[0,1]$. This time

$$
\frac{\partial}{\partial x}\left(-\frac{x}{x^2+y^2}\right)
=\frac{x^2-y^2}{(x^2+y^2)^2}.
$$

Thus

$$
\int_0^1 f(x,y)\,dx=-\frac1{1+y^2},
$$

and

$$
\int_0^1\left(\int_0^1f(x,y)\,dx\right)dy
=-\int_0^1\frac{dy}{1+y^2}
=\boxed{-\frac\pi4}.
$$

Every section used here is integrable, not just almost every section. That still does not establish joint absolute integrability.

**3. Prove both sign parts have infinite integral by explicit disjoint rectangles.** If $0<y<x/2$, then

$$
x^2-y^2\geq\frac34x^2,
\qquad (x^2+y^2)^2\leq\frac{25}{16}x^4,
\qquad f(x,y)\geq\frac{12}{25x^2}>0.
$$

For each integer $n\geq0$, take

$$
R_n=\bigl(2^{-n-1},2^{-n}\bigr)
\times\bigl(0,2^{-n-2}\bigr).
$$

These rectangles are pairwise disjoint and lie in $\{0<y<x/2\}\cap Q$. On $R_n$, $x<2^{-n}$, so

$$
f^+(x,y)\geq\frac{12}{25}2^{2n},
\qquad \mathcal L^2(R_n)=2^{-2n-3}.
$$

For every positive integer $N$, monotonicity of the nonnegative integral yields

$$
\begin{aligned}
\int_Qf^+\,d\mathcal L^2
&\geq\sum_{n=0}^{N-1}
\frac{12}{25}2^{2n}\mathcal L^2(R_n)\\
&=\sum_{n=0}^{N-1}\frac3{50}
=\frac{3N}{50}.
\end{aligned}
$$

Letting $N\to\infty$ proves $\int_Qf^+=\infty$. Since $f(y,x)=-f(x,y)$, the transposed rectangles give the identical bound for $f^-$. Hence

$$
\int_Q f^+\,d\mathcal L^2
=\int_Q f^-\,d\mathcal L^2=\infty,
\qquad \int_Q|f|\,d\mathcal L^2=\infty.
$$

The expression $\int_Qf$ is therefore **undefined as a signed Lebesgue integral**, rather than equal to either iterated value or to zero.

**4. Identify another prescription, without confusing it with a Lebesgue integral.** On $(\varepsilon,1)^2\subset Q$, where $0<\varepsilon<1$, the function is bounded and antisymmetric under exchanging coordinates. Fubini is valid on that truncated square, and

$$
\int_{(\varepsilon,1)^2}f\,d\mathcal L^2=0.
$$

Thus this particular symmetric limiting prescription gives zero. The disagreement with the two iterated values records dependence on the truncation procedure; it supplies no value for the undefined signed Lebesgue integral.

## Why the theorem applies

The one-dimensional computations use the fundamental theorem of calculus on continuous sections. Fubini applies on each truncated square because the integrand is bounded there. It does **not** apply on $Q$: joint absolute integrability fails by Step 3. Tonelli remains valid separately for the nonnegative functions $f^+$, $f^-$, and $|f|$, with value $\infty$ where indicated. It never legitimizes subtracting $\infty-\infty$.

## Pitfalls

- Finite iterated **signed** integrals do not replace the hypothesis $\int_Q|f|<\infty$.
- Cancellation inside each section can conceal infinite joint positive and negative masses.
- Symmetry gives an integral of zero only after the existence of that integral has been justified, or for a specifically stated finite truncation.
- Defining a value for $f$ at the missing origin would not repair the divergence in its neighborhood.

## Reusable technique

Tags: `signed-Fubini-failure`, `absolute-integrability`, `positive-negative-parts`, `dyadic-rectangles`, `cancellation`, `truncation-dependence`.

Before exchanging signed integrals, estimate $|f|$ or its sign parts. A sequence of disjoint regions each carrying a fixed positive mass proves divergence with an explicit sum, even when direct polar integration is inconvenient. A sufficient repair is to impose $f\in L^1(Q)$; local boundedness away from the singularity is insufficient.

## Sources

- John K. Hunter, [*Measure Theory*](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf), Definition 4.8 (signed integral), Theorem 5.18 (Fubini), and Theorem 5.21 (completed Lebesgue measures). Source ID: `hunter-measure`. The primitive identities and dyadic-rectangle lower bounds are checked directly above.
