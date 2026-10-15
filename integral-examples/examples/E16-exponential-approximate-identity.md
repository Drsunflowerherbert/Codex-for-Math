# E16 — An exponential kernel retrieves a boundary value

## Problem

Let $g:[0,\infty)\to\mathbb R$ be bounded and Borel measurable, and suppose it is right-continuous at $0$. Prove
$$
\lim_{n\to\infty}\int_0^{\infty}ne^{-nx}g(x)\,dx=g(0).
$$
Give a direct error estimate, and identify why applying dominated convergence in the original variable would be unsafe.

## Data and hypotheses

The measure is one-dimensional Lebesgue measure on $[0,\infty)$. Choose $M\ge0$ with $|g(x)|\le M$ for all $x\ge0$. The kernel function is $k_n:x\mapsto ne^{-nx}$; its value at $x$ is $k_n(x)$. It satisfies
$$
k_n\ge0,\qquad\int_0^{\infty}k_n(x)\,dx=1,\qquad
\int_\delta^{\infty}k_n(x)\,dx=e^{-n\delta}\quad(\delta>0).
$$
Every displayed integral of $k_ng$ is absolutely convergent because $\int|k_ng|\le M$. The value $g(0)$ is recoverable under the stated continuity assumption; Lebesgue integration by itself ignores a single point.

## Solution

**1. Rescale the moving kernel.** The substitution $u=nx$, with $dx=du/n$, gives
$$
\int_0^{\infty}ne^{-nx}g(x)\,dx
=\int_0^{\infty}e^{-u}g(u/n)\,du.
$$
For each fixed $u\ge0$, right-continuity gives $g(u/n)\to g(0)$. Moreover
$$
|e^{-u}g(u/n)|\le Me^{-u},\qquad
\int_0^{\infty}Me^{-u}\,du=M<\infty.
$$
Dominated convergence now applies on the fixed $u$-domain and gives
$$
\lim_n\int_0^{\infty}e^{-u}g(u/n)\,du
=g(0)\int_0^{\infty}e^{-u}\,du=g(0).
$$

**2. Obtain a direct epsilon and tail proof.** For any $\varepsilon>0$, choose $\delta>0$ such that $|g(x)-g(0)|<\varepsilon$ when $0\le x<\delta$. Normalization of $k_n$ yields
$$
\begin{aligned}
\left|\int_0^{\infty}k_n(x)g(x)\,dx-g(0)\right|
&\le\int_0^\delta k_n(x)|g(x)-g(0)|\,dx
 +\int_\delta^{\infty}k_n(x)|g(x)-g(0)|\,dx\\
&\le\varepsilon+2M e^{-n\delta}.
\end{aligned}
$$
For this fixed $\delta$, the tail tends to zero. Then let $\varepsilon\downarrow0$.

**3. A useful convergence rate.** If, additionally, $|g(x)-g(0)|\le Lx$ for every $x\ge0$ (in particular if $g$ is globally $L$-Lipschitz), then
$$
\left|\int_0^{\infty}k_n(x)g(x)\,dx-g(0)\right|
\le L\int_0^{\infty}ne^{-nx}x\,dx
=\frac Ln\int_0^{\infty}ue^{-u}\,du=\frac Ln.
$$
The last integral is $1$ by integration by parts. If only a local Lipschitz bound holds for $0\le x<\delta$, the same split gives the valid bound $L/n+2Me^{-n\delta}$.

## Why the theorem applies

The rescaled integrands $u\mapsto e^{-u}g(u/n)$ are Borel, converge pointwise, and have the explicit common $L^1$ majorant $Me^{-u}$. These are precisely the dominated-convergence hypotheses. The substitution is a positive linear change of variables, so its Jacobian is $1/n$; it is valid for these absolutely integrable measurable functions.

In the original variable $k_n(x)\to0$ for every $x>0$, while $\int k_n=1$. Hence no common $L^1$ function dominates all $k_n$. More directly, if $G\ge k_n$ almost everywhere for all $n$, then
$$
\int_0^{1/n}G\,dx\ge\int_0^{1/n}ne^{-nx}\,dx=1-e^{-1},
$$
contradicting absolute continuity of an $L^1$ integral. Rescaling resolves the concentration instead of incorrectly ignoring it. In measure language the probability measures $k_n(x)\,dx$ converge weakly against bounded continuous test functions on $[0,\infty)$ to the unit point mass at $0$; they do not converge to the zero measure merely because their densities tend to zero almost everywhere.

## Pitfalls

- Do not infer the limit integral is zero from $ne^{-nx}g(x)\to0$ for $x>0$: a common integrable bound has not been supplied.
- If right-continuity is removed, the answer need not equal the chosen value at zero. For $g(0)=1$ and $g(x)=0$ for $x>0$, every integral is zero.
- Boundedness and continuity at zero supply different parts of the proof: boundedness controls the far tail, while continuity identifies the limit near the boundary.

## Reusable technique

For a normalized concentrating kernel, either rescale to a fixed kernel and use DCT, or split into a small neighborhood and an exponentially small tail. Tags: `approximate-identity`, `dominated-convergence`, `rescaling`, `boundary-value`, `error-bound`, `laplace-kernel`.

## Sources

- John K. Hunter, [*Measure Theory*](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf), Theorem 4.24 (dominated convergence) and Chapter 4's absolute continuity of the integral. Source ID: `hunter-measure`.
- The exponential-kernel calculation, estimates, and rate are proved directly above; no distributional formalism is required.
