# E14 — Lost integral mass: concentration, escape, and dilution

## Problem

Compare the limits and integrals of these measurable functions:
$$
f_n(x)=n\mathbf1_{(0,1/n)}(x)\quad(x\in(0,1)),\qquad
h_n(x)=\mathbf1_{(n,n+1)}(x)\quad(x\in\mathbb R).
$$
Explain why dominated convergence fails. Identify sufficient replacement hypotheses, keeping finite and infinite measure spaces distinct.

## Data and hypotheses

All measures are one-dimensional Lebesgue measure. The symbol $f_n$ denotes a function; $f_n(x)$ denotes its value. All three sequences used below consist of nonnegative Borel functions. Convergence in measure on a measure space means $\mu(\{|u_n-u|>\varepsilon\})\to0$ for each $\varepsilon>0$. “Locally in measure” on $\mathbb R$ means this on every bounded interval.

We use **value-tail uniform integrability** to mean
$$
\lim_{K\to\infty}\sup_n\int_{\{|u_n|>K\}}|u_n|\,d\mu=0.
$$
On finite measure spaces this is the usual uniform-integrability criterion. On infinite measure spaces some definitions additionally require spatial tightness; here that condition will always be stated separately.

## Solution

**1. Concentration on a shrinking set.** For each fixed $x\in(0,1)$, eventually $n>1/x$, so $f_n(x)=0$. Nevertheless
$$
\int_0^1 f_n(x)\,dx=n\lambda^1((0,1/n))=1.
$$
Thus $f_n\to0$ pointwise everywhere on its domain, while $\int f_n\not\to\int0$. It also converges in measure since, for $n>\varepsilon$,
$$
\lambda^1(\{f_n>\varepsilon\})=1/n\longrightarrow0.
$$
There is no common integrable majorant $G$: if $G\ge f_n$ almost everywhere for all $n$, take a common full-measure set by removing the countable union of exceptional sets. Then $\int_0^{1/n}G\ge1$ for every $n$, contradicting absolute continuity of the integral of an $L^1$ function as $1/n\to0$. Its value-tail integrals also show precisely what fails: for any $K$, choose an integer $n>K$ to obtain
$$
\int_{\{f_n>K\}}f_n\,dx=1.
$$

**2. Escape to infinity without large values.** For each $x\in\mathbb R$, $h_n(x)=0$ eventually, but $\int_{\mathbb R}h_n=1$. The functions are bounded by $1$, which is not integrable on $\mathbb R$. A common $L^1$ majorant is impossible because the intervals $(n,n+1)$ are disjoint and
$$
\int_{\mathbb R}G\,dx\ge\sum_{n=1}^{\infty}\int_n^{n+1}G\,dx\ge\sum_{n=1}^{\infty}1=\infty.
$$
Here value-tail uniform integrability holds: for $K\ge1$ every tail integral is zero. What fails is **spatial tightness**:
$$
\lim_{R\to\infty}\sup_n\int_{\{|x|>R\}}|h_n(x)|\,dx=1,
$$
not zero. Also $h_n\to0$ locally in measure but not in measure on all of $\mathbb R$, since $\lambda^1(\{h_n>1/2\})=1$.

**3. Even global convergence in measure is insufficient on an infinite space.** Set $r_n(x)=n^{-1}\mathbf1_{(0,n)}(x)$ on $\mathbb R$. Then $r_n\to0$ pointwise and uniformly, hence in measure, and $\int r_n=1$. Its values are at most $1$, so it is value-tail uniformly integrable. But for fixed $R>0$,
$$
\int_{\{|x|>R\}}r_n\,dx=\max(1-R/n,0),
$$
whose supremum over $n$ is $1$. Mass spreads out at smaller heights. This is why a finite-measure version of a theorem cannot silently be applied to $\mathbb R$.

## Why the theorem applies

Useful sufficient conditions are:

- On any measure space, if $u_n\to u$ almost everywhere and $|u_n|\le G$ almost everywhere for one $G\in L^1$, dominated convergence gives $\|u_n-u\|_1\to0$ and therefore convergence of integrals.
- On a **finite** measure space, if $u_n$ and $u$ are real measurable functions, $u_n\in L^1$, $u_n\to u$ in measure, and the sequence is value-tail uniformly integrable, then $u\in L^1$ and $\|u_n-u\|_1\to0$.
- On $\mathbb R$, for real measurable $u_n,u$ with $u_n\in L^1$, the same conclusion follows from local convergence in measure, value-tail uniform integrability, and spatial tightness $\lim_{R\to\infty}\sup_n\int_{|x|>R}|u_n|=0$.

For completeness, the finite-measure assertion follows by truncation: let $T_K(s)=\max(-K,\min(s,K))$ for real functions. On a finite space, convergence in measure gives
$$
\int|T_K(u_n)-T_K(u)|\le\varepsilon\mu(X)+2K\mu(\{|u_n-u|>\varepsilon\})\longrightarrow\text{at most }\varepsilon\mu(X).
$$
Uniform integrability controls $\|u_n-T_K(u_n)\|_1$ uniformly. A subsequence converges almost everywhere (choose error probabilities summable); Fatou bounds the corresponding tail for $u$ by the same uniform tail bound. Let $K\to\infty$ and then $\varepsilon\to0$. On $\mathbb R$, apply this finite-space argument on $[-R,R]$ and control its complement by spatial tightness. To bound the tail of $u$, choose a diagonal subsequence converging almost everywhere on each $[-m,m]$: at its $j$th step make the measure of the error set $\{|u_{n_j}-u|>1/j\}\cap[-j,j]$ less than $2^{-j}$. The summable-error argument gives almost-everywhere convergence on all of $\mathbb R$, and Fatou then bounds $\int_{|x|>R}|u|$ by the uniform tail bound. These are analytic hypotheses, not conclusions inferred from numerical samples.

## Pitfalls

Each $\int u_n$ being finite, or their values being uniformly bounded, is insufficient. Uniform convergence alone does not control integrals over an infinite-measure domain. No example contradicts Fatou: it only asserts $0=\int\liminf u_n\le\liminf\int u_n=1$ here.

## Reusable technique

Before moving a limit inside an integral, inspect large values on small sets and mass outside large bounded sets separately. Tags: `dominated-convergence`, `uniform-integrability`, `concentration`, `escape-to-infinity`, `tightness`, `counterexample`.

## Sources

- John K. Hunter, [*Measure Theory*](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf), Examples 4.18–4.20 (the standard concentration, dilution and escape families), Theorem 4.24 (dominated convergence), the following discussion of absolute continuity and uniform integrability, and Chapter 4's Fatou lemma. The computations and additional uniform-integrability/tightness analysis here are worked through explicitly. Source ID: `hunter-measure`.
- The uniform-integrability implications used here are proved in the paragraph above; the source is not being cited as containing this exact formulation or atlas.
