# E05 — Two finite iterated sums and no signed double integral

## Problem

Let $\mathbb N=\{1,2,\ldots\}$ and define the function $a:\mathbb N^2\to\mathbb R$ by
$$
a(n,m)=\begin{cases}1&m=n,\\-1&m=n+1,\\0&\text{otherwise}.\end{cases}
$$
Compute both iterated sums. Explain exactly why their disagreement does not contradict Fubini's theorem, and what square partial sums do.

## Data and hypotheses

Each copy of $\mathbb N$ has the power-set $\sigma$-algebra and counting measure $\#$; the product is counting measure on $\mathbb N^2$. These spaces are $\sigma$-finite because $\mathbb N$ is a countable union of finite sets. Every function here is measurable. Write $a_{nm}=a(n,m)$ for a **value** of the function $a$. A signed Lebesgue integral is defined only if at least one of $\int a^+\,d(\#\otimes\#)$ and $\int a^-\,d(\#\otimes\#)$ is finite; an integrable real-valued function must satisfy $\int|a|<\infty$.

## Solution

**1. Sum each row first.** For every fixed $n$, only two entries are nonzero:
$$
\sum_{m=1}^{\infty}a_{nm}=a_{nn}+a_{n,n+1}=1-1=0.
$$
Consequently
$$
\sum_{n=1}^{\infty}\left(\sum_{m=1}^{\infty}a_{nm}\right)=\sum_{n=1}^{\infty}0=0.
$$
Every inner sum is absolutely convergent, and the resulting outer series is absolutely convergent.

**2. Sum each column first.** Column $m=1$ contains only $a_{11}=1$. For every $m\ge2$, its nonzero entries are $a_{mm}=1$ and $a_{m-1,m}=-1$. Thus
$$
\sum_{n=1}^{\infty}a_{n1}=1,\qquad
\sum_{n=1}^{\infty}a_{nm}=0\quad(m\ge2),
$$
and
$$
\sum_{m=1}^{\infty}\left(\sum_{n=1}^{\infty}a_{nm}\right)=1+\sum_{m=2}^{\infty}0=1.
$$
Again, every inner sum and the resulting outer series converge absolutely. What fails is absolute summability **before** cancellation:
$$
\sum_{n=1}^{\infty}\sum_{m=1}^{\infty}|a_{nm}|
=\sum_{n=1}^{\infty}2=+\infty.
$$
Indeed the positive diagonal and negative superdiagonal each contain infinitely many entries of magnitude $1$, so $\int a^+=\int a^-=+\infty$. The signed double integral $\int a\,d(\#\otimes\#)$ is undefined; neither iterated answer can be identified with it.

**3. Inspect finite rectangles.** For positive integers $N,M$,
$$
S_{N,M}=\sum_{n=1}^{N}\sum_{m=1}^{M}a_{nm}
=\min(N,M)-\min(N,M-1).
$$
Therefore $S_{N,N}=1$, whereas $S_{N,N+1}=0$. There is no limit as $N,M\to\infty$ independently. Taking $M\to\infty$ first gives $0$; taking $N\to\infty$ first gives $1$. A square exhaustion happens to select the second value, but it does not define a signed Lebesgue integral.

## Why the theorem applies

Tonelli's theorem applies to each of $|a|$, $a^+$ and $a^-$, because they are nonnegative measurable functions on $\sigma$-finite product spaces. It correctly gives infinite integrals. Signed Fubini requires $\sum_{n,m}|a_{nm}|<\infty$, which has explicitly failed. If instead a doubly indexed real or complex family $b_{nm}$ satisfies that bound, Fubini permits interchanging its sums and identifies both with the product integral.

## Pitfalls

- Absolute convergence of every row, every column, and even both series of already-summed values does not establish $\sum_{n,m}|a_{nm}|<\infty$.
- This is an iterated-summation counterexample, not a conditionally Lebesgue-integrable function. For real or complex functions, Lebesgue integrability entails absolute integrability. Ordinary conditionally convergent series use an ordering, which counting-measure integration does not supply.
- Never replace the undefined expression $+\infty-(+\infty)$ by zero after pairing entries.

## Reusable technique

Before exchanging signed sums or integrals, apply Tonelli to the absolute value. If it diverges, inspect positive and negative parts and the actual limiting convention. Tags: `counting-measure`, `signed-fubini`, `absolute-integrability`, `order-of-summation`, `counterexample`.

## Sources

- John K. Hunter, [*Measure Theory*](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf), Theorem 5.18 and Example 5.19 (Fubini and absolutely convergent double series), and Chapter 4 (signed integration). Source ID: `hunter-measure`.
- The matrix, explicit rectangular calculation, and exposition above were worked out for this collection; the source supports the theorem, not a copied exercise.
