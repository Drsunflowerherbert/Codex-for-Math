# E02 — A measurable region whose entire boundary has positive area

## Problem

Construct a closed set $C\subset[0,1]$ with empty interior and $\mathcal L^1(C)=1/2$. For $E=C\times[0,1]$, determine its boundary and compute

$$
\int_E 2y\,d\mathcal L^2(x,y).
$$

Explain why simply discarding the boundary gives the wrong answer and why the zero extension of this integrand is not Riemann integrable on $[0,1]^2$.

## Data and hypotheses

All measures are Lebesgue measures $\mathcal L^1$ and $\mathcal L^2$. Start with $C_0=[0,1]$. At stage $n\geq1$, remove from the middle of each of the $2^{n-1}$ closed intervals in $C_{n-1}$ one open interval of length $4^{-n}$. Let $C_n$ be the remaining union of $2^n$ closed intervals and put

$$
C=\bigcap_{n=0}^{\infty}C_n.
$$

This is the Smith–Volterra construction specified by these exact lengths. The sets and integrands are explicit except for the infinite intersection defining $C$; no nonmeasurable choice is involved.

## Solution

**1. Check that every removal fits.** All component intervals of $C_n$ have equal length

$$
\ell_n=2^{-n-1}+2^{-2n-1}.
$$

For $n=0$ this is $1$. If the formula holds at stage $n-1$, the next component length is

$$
\frac{\ell_{n-1}-4^{-n}}2
=2^{-n-1}+2^{-2n-1}>0.
$$

In particular the removed middle interval is strictly shorter than its parent, so the construction is possible at every stage.

**2. Compute the measure by an explicit sum.** Removed intervals from different stages are disjoint. Their total length through stage $n$ is

$$
\sum_{k=1}^{n}2^{k-1}4^{-k}
=\frac12\sum_{k=1}^{n}2^{-k}
=\frac12(1-2^{-n}).
$$

Therefore

$$
\mathcal L^1(C_n)=\frac12+2^{-n-1},\qquad
\mathcal L^1(C)=\lim_{n\to\infty}\mathcal L^1(C_n)=\frac12.
$$

The limit follows from continuity from above of a measure, since $C_n$ decreases and $\mathcal L^1(C_0)=1<\infty$.

**3. Prove the interior is empty.** Suppose $C$ contained a nondegenerate interval $J$. For every $n$, the connected set $J$ would lie in one component interval of $C_n$, because distinct components are separated by a removed open interval. Hence the length of $J$ would be at most $\ell_n$ for every $n$. But $\ell_n\to0$, a contradiction. Since $C$ is closed and has empty interior, its complement is dense in $\mathbb R$.

**4. Find the boundary of $E$.** The set $E=C\times[0,1]$ is closed. It has empty interior: every open ball about a point of $E$ contains a point whose first coordinate lies outside $C$. Thus

$$
\partial E=\overline E\setminus E^{\circ}=E,
\qquad \mathcal L^2(\partial E)=\mathcal L^2(E)=\frac12.
$$

The last equality uses the measurable-rectangle formula $\mathcal L^2(C\times[0,1])=\mathcal L^1(C)\mathcal L^1([0,1])$.

**5. Integrate.** Extend the integrand to the square as $F(x,y)=2y\mathbf 1_C(x)$. It is Borel measurable and $0\leq F\leq2$, so Fubini applies:

$$
\begin{aligned}
\int_E2y\,d\mathcal L^2(x,y)
&=\int_0^1\mathbf 1_C(x)\left(\int_0^1 2y\,dy\right)dx\\
&=\int_0^1\mathbf 1_C(x)\,dx
=\boxed{\frac12}.
\end{aligned}
$$

Deleting the boundary would leave the empty set $E\setminus\partial E$, whose integral is $0$, not $1/2$.

**6. Compare with Riemann integration directly.** Take any rectangular partition of $[0,1]^2$. Every subrectangle of positive width contains a point whose first coordinate is outside $C$. Since $F\geq0$, its infimum on each such rectangle is $0$. Every lower Darboux sum is therefore $0$. Every upper Darboux step function is at least $F$, so its integral, equal to the corresponding upper sum, is at least $\int F\,d\mathcal L^2=1/2$. Upper and lower sums cannot approach a common value. Thus $F$ is not Riemann integrable on the square, although it is bounded and Lebesgue integrable.

## Why the theorem applies

Closedness establishes Borel measurability. Continuity from above needs the finite measure of the initial set; that hypothesis was checked. For the integral, the bounded Borel function $F$ on a finite-measure square is absolutely integrable, so Fubini applies. No assumption that the boundary is null is required by Lebesgue integration.

## Pitfalls

- “Boundary” does not imply “measure zero.” Here the entire positive-area set is its boundary.
- Empty interior does not imply zero measure.
- A bounded measurable function need not be Riemann integrable. The direct Darboux argument identifies the actual obstruction in this example.
- The stage-$n$ removal length $4^{-n}$ is the length of **each** of $2^{n-1}$ gaps, not their combined length.

## Reusable technique

Tags: `fat-Cantor-set`, `positive-boundary-measure`, `explicit-series`, `continuity-from-above`, `Fubini`, `Riemann-versus-Lebesgue`.

For a complicated closed region, calculate removed measure with a disjoint sum, check interior separately, and integrate through an indicator. Treat a proposed boundary deletion as a measure claim that needs proof.

## Sources

- John K. Hunter, [*Measure Theory*](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf), Proposition 1.12 (continuity of measures), Theorem 5.14 (product measure), and Theorem 5.18 (Fubini). Source ID: `hunter-measure`. The construction, interval-length formula, boundary proof, and Darboux argument are supplied here.
