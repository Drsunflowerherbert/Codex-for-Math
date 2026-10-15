# E06 — A logarithm from a positive double integral

## Problem

For $a,b>0$, calculate
$$
F(a,b)=\int_0^{\infty}\frac{e^{-ax}-e^{-bx}}{x}\,dx
$$
as a Lebesgue integral. Justify both the exchange of integrations and differentiation with respect to $b$.

## Data and hypotheses

The integration variable $x$ carries one-dimensional Lebesgue measure $\lambda^1$ on $(0,\infty)$. A parameter variable $t$ carries $\lambda^1$ on a finite interval. The expression $(e^{-ax}-e^{-bx})/x$ is the value at $x$ of a continuous function on $(0,\infty)$. Positivity of both parameters is essential for the tail estimate below. No value at $x=0$ is needed; assigning the limiting value $b-a$ there would not change the integral.

## Solution

**1. Represent the cancellation before integrating.** Suppose first $a\le b$. The fundamental theorem of calculus in the parameter gives, for $x>0$,
$$
\frac{e^{-ax}-e^{-bx}}{x}=\int_a^b e^{-tx}\,dt\ge0.
$$
The function $(x,t)\mapsto e^{-tx}$ is continuous and nonnegative. Tonelli therefore allows an exchange before finiteness has been established:
$$
\begin{aligned}
F(a,b)&=\int_0^{\infty}\int_a^b e^{-tx}\,dt\,dx\\
&=\int_a^b\int_0^{\infty}e^{-tx}\,dx\,dt
=\int_a^b\frac{1}{t}\,dt
=\log b-\log a.
\end{aligned}
$$
The inner integral is $1/t$ because $t\ge a>0$. The resulting logarithm is finite, so this also proves integrability. If $a>b$, apply this computation to $F(b,a)$ and use the pointwise negative sign; if $a=b$, the integrand is identically zero. In all cases,
$$
\boxed{F(a,b)=\log(b/a).}
$$

**2. Check absolute integrability directly.** Let $c=\min(a,b)>0$ and $d=|b-a|$. The same parameter representation with the endpoints ordered gives
$$
\left|\frac{e^{-ax}-e^{-bx}}{x}\right|
\le d e^{-cx}\le d\qquad(x>0).
$$
Thus the integral of the absolute value on $(0,1)$ is at most $d$. On $(1,\infty)$ one may also use
$$
\left|\frac{e^{-ax}-e^{-bx}}{x}\right|
\le e^{-ax}+e^{-bx},
$$
whose integral is finite. This makes the endpoint hypotheses visible without relying on the final formula.

**3. Differentiate under the integral with a local bound.** Fix $a>0$ and $b_0>0$, and write $q_b(x)=(e^{-ax}-e^{-bx})/x$. Its parameter derivative is
$$
\partial_b q_b(x)=e^{-bx}.
$$
For $b\in[b_0/2,3b_0/2]$,
$$
|\partial_b q_b(x)|\le e^{-b_0x/2},\qquad
\int_0^{\infty}e^{-b_0x/2}\,dx=2/b_0<\infty.
$$
For sufficiently small nonzero $h$, the ordinary mean value theorem bounds the difference quotient $(q_{b_0+h}(x)-q_{b_0}(x))/h$ by this same integrable function. These quotients converge pointwise to $e^{-b_0x}$. Dominated convergence yields
$$
\partial_b F(a,b_0)=\int_0^{\infty}e^{-b_0x}\,dx=1/b_0,
$$
in agreement with the logarithm. This is a proof of the exchange, rather than a deduction from the already-known answer.

## Why the theorem applies

Tonelli applies on the $\sigma$-finite Lebesgue product $(0,\infty)\times[a,b]$ to a nonnegative Borel function. Once its integral is finite, signed Fubini would also be available. For differentiation, the difference quotients are measurable, converge pointwise, and have a common $L^1$ majorant on a neighborhood of the chosen positive parameter; Hunter's dominated convergence theorem applies. The same argument works near any $b_0>0$; a uniform bound over all $b>0$ is unnecessary.

## Pitfalls

- The two terms $e^{-ax}/x$ and $e^{-bx}/x$ each have infinite integrals near zero. Writing their separate integrals and subtracting creates an undefined $\infty-\infty$.
- If $a=0<b$, then $(1-e^{-bx})/x$ has a divergent tail, so the stated finite formula does not extend to $a=0$.
- A bound on $q_b$ alone does not justify differentiating it. The proof controls its difference quotients through $\partial_b q_b$.

## Reusable technique

Turn a difference quotient or cancellation into an integral over a positive parameter kernel. Apply Tonelli before evaluating, then use a local integrable derivative bound for parameter differentiation. Tags: `frullani`, `tonelli`, `parameter-integral`, `differentiate-under-integral`, `cancellation`.

## Sources

- John K. Hunter, [*Measure Theory*](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf), Theorem 4.24 (dominated convergence) and Chapter 5 (product integration). Source ID: `hunter-measure`.
- Keith Conrad, [*Differentiating under the integral sign*](https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf), Theorem 12.3, for a classical sufficient differentiation theorem. The measurable version used here follows from the displayed difference-quotient proof. Source ID: `conrad-diff`.
