# E15 — A parameter derivative misses a concentrating boundary layer

## Problem

On $x\in(0,1)$, for $t\ge0$, define
$$
f(t,x)=\begin{cases}\dfrac{t^2}{x^2+t^2},&t>0,\\0,&t=0,\end{cases}
\qquad I(t)=\int_0^1f(t,x)\,dx.
$$
Compare $I'_+(0)$ with $\int_0^1\partial_t^+f(0,x)\,dx$. Locate the precise missing hypothesis for differentiation under the integral sign.

## Data and hypotheses

The measure is Lebesgue measure $\lambda^1$ on $(0,1)$. For every $t$, $x\mapsto f(t,x)$ is Borel and satisfies $0\le f(t,x)\le1$. For each fixed $x>0$, $t\mapsto f(t,x)$ has right derivative at zero. We ask about a derivative of the **integral-valued function** $I$, not about a derivative of one fixed value $f(t,x)$.

## Solution

**1. Evaluate the integral before differentiating.** For $t>0$, substitute $x=tu$:
$$
I(t)=t\int_0^{1/t}\frac{1}{1+u^2}\,du=t\arctan(1/t),\qquad I(0)=0.
$$
It follows that
$$
I'_+(0)=\lim_{t\downarrow0}\frac{I(t)-I(0)}{t}
=\lim_{t\downarrow0}\arctan(1/t)=\frac\pi2.
$$

**2. Differentiate each fixed section.** For every fixed $x>0$,
$$
\partial_t^+f(0,x)=\lim_{t\downarrow0}\frac{f(t,x)-f(0,x)}{t}
=\lim_{t\downarrow0}\frac{t}{x^2+t^2}=0.
$$
Thus $\int_0^1\partial_t^+f(0,x)\,dx=0$, which differs from $I'_+(0)$.

**3. Find the boundary layer.** The difference-quotient functions are
$$
q_t(x)=\frac{t}{x^2+t^2}\ge0.
$$
They tend to zero at each fixed $x>0$, but
$$
\int_0^1q_t(x)\,dx=\arctan(1/t)\longrightarrow\pi/2.
$$
For $0<t\le1$ the interval $(0,t)$ already carries a fixed amount of mass:
$$
\int_0^t q_t(x)\,dx=\int_0^1\frac{du}{1+u^2}=\pi/4.
$$
This proves that the family of quotients has no common $L^1(0,1)$ majorant on any neighborhood $0<t<\delta$: otherwise absolute continuity of its integral would force the displayed integrals to tend to zero.

The derivative family also has no local common integrable majorant. For $t>0$,
$$
\partial_t f(t,x)=\frac{2tx^2}{(x^2+t^2)^2}.
$$
To avoid any uncountable exceptional-set issue, suppose $G\in L^1$ bounds this derivative for almost every $x$ for **each** $t\in(0,\delta)$. Take $t_j\downarrow0$ with $2t_j<1$. On $(t_j,2t_j)$, put $x=t_ju$ to obtain
$$
\int_{t_j}^{2t_j}\partial_t f(t_j,x)\,dx
=\int_1^2\frac{2u^2}{(1+u^2)^2}\,du>0,
$$
independent of $j$. Since $G$ dominates the integrand at these countably many parameters, absolute continuity again gives a contradiction. This even rules out bounds whose null exceptional set was initially allowed to depend on the parameter.

## Why the theorem applies

Ordinary dominated convergence **does** give $I(t)\to0$: $f(t,x)\to0$ and $|f(t,x)|\le1\in L^1(0,1)$. It says nothing about the derivative unless the quotients are controlled.

A precise sufficient differentiation rule is as follows. Let $(X,\mathcal A,\mu)$ be a measure space and $J$ an open real interval containing $t_0$. Assume $F(t,\cdot)$ is measurable for every $t\in J$, $F(t_0,\cdot)\in L^1(\mu)$, and there is a **common** full-measure set on which $t\mapsto F(t,x)$ is differentiable throughout $J$ and
$$
|\partial_tF(t,x)|\le G(x)\quad(t\in J),\qquad G\in L^1(\mu).
$$
Then $F(t,\cdot)\in L^1$ near $t_0$ and
$$
\left.\frac{d}{dt}\right|_{t=t_0}\int_XF(t,x)\,d\mu(x)
=\int_X\partial_tF(t_0,x)\,d\mu(x).
$$
Indeed the mean value theorem bounds the difference quotients by $G$, and dominated convergence proves the identity along every sequence of nonzero increments tending to zero. The same proof works for a right derivative at a left endpoint, using a half-interval and right differentiability at the endpoint. In this example the required bound fails exactly where $x$ and $t$ approach zero together.

## Pitfalls

- An integrable bound on $f$ is not an integrable bound on its parameter derivative or difference quotients.
- Differentiability at every fixed $x$ does not imply differentiation can pass through integration.
- A related warning for a different exchange is $v_n(x)=\sin(nx)/n$ on $[-1,1]$: $v_n\to0$ uniformly, but $v_n'(0)=1$ for all $n$, whereas the limit function has derivative $0$. Uniform convergence of functions alone does not justify exchanging a limit and a derivative.

## Reusable technique

Write the actual difference quotients and search for a common integrable bound. When the quotient concentrates, integrate it over a parameter-dependent shrinking interval to prove that no such bound exists. Tags: `differentiate-under-integral`, `boundary-layer`, `concentration`, `dominated-convergence`, `counterexample`.

## Sources

- John K. Hunter, [*Measure Theory*](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf), Theorem 4.24 (the DCT used in the proof). Source ID: `hunter-measure`.
- Keith Conrad, [*Differentiating under the integral sign*](https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf), Section 12 and Theorem 12.3, for classical hypotheses and a warning example. The measurable sufficient rule here is explicitly proved above; the present boundary-layer example is independently worked. Source ID: `conrad-diff`.
