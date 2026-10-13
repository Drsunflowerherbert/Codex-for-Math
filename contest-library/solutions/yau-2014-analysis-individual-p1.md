# Authored solution — Yau 2014, written individual Analysis, Problem 1

**Spoilers:** this file contains a complete proof. [Hints are separate](../hints/yau-2014-analysis-individual-p1.md).

**Canonical problem ID:** `yau-2014-written-individual-p1`.

**Status:** original proof accepted in [independent agent review](../reviews/yau-2014-analysis-individual-p1.md) by `proof_2019` on 2026-10-13. This is our authored note, not an official contest solution. An official solution was not located in the inspected archives and bounded official-domain search; that does not establish that none exists. No formal proof assistant verification is claimed.

**Source:** [official past-paper page](https://yau-contest.com/en/lists-jxxg.html), [official written-paper archive](https://yau-contest.com/index/reldown?en=1&id=9), member `2010-2026历年笔试真题/2014/analysis2014(individual).pdf`, page 1, original problem number 1. The PDF was visually checked against its extracted text. Retrieved 2026-10-13 UTC. PDF SHA-256: `28a65742bc442aa93ec795f8df37c339dd11ab041554d187891359f4cbca17c1`. The source PDF stays outside the published repository.

## Conditions and goal, in our notation

The function $f:\mathbb R\to\mathbb R$ is continuous. Put

$$
D:=\sup_{x,y\in\mathbb R}|f(x+y)-f(x)-f(y)|<\infty.
$$

The given positive-integer limit is $f(n)/n\to2014$. We will prove the stronger, explicit estimate

$$
\boxed{\ |f(x)-2014x|\le D\quad\text{for every }x\in\mathbb R.\ }
$$

## Proof

For each integer $k\ge0$, define the continuous function

$$
F_k(x):=2^{-k}f(2^kx)\qquad(x\in\mathbb R).
$$

Taking both arguments in the defect inequality equal to $2^kx$ gives

$$
|F_{k+1}(x)-F_k(x)|
=2^{-(k+1)}|f(2^{k+1}x)-2f(2^kx)|
\le D2^{-(k+1)}.
$$

Consequently, for all integers $n>m\ge0$ and every real $x$,

$$
|F_n(x)-F_m(x)|
\le D\sum_{k=m}^{n-1}2^{-(k+1)}
=D(2^{-m}-2^{-n}).
$$

For every fixed $x$, this proves that $(F_k(x))$ is a Cauchy sequence of real numbers. Define $A(x):=\lim_{k\to\infty}F_k(x)$. Letting $n\to\infty$ in the last estimate yields

$$
|A(x)-F_m(x)|\le D2^{-m}\qquad(m\ge0,\ x\in\mathbb R). \tag{1}
$$

Thus $F_m\to A$ uniformly, and $A$ is continuous. For clarity, the continuity follows directly from (1): given $x_0$ and $\varepsilon>0$, choose $m$ so that $2D2^{-m}<\varepsilon/2$, then choose $\delta>0$ so that $|F_m(x)-F_m(x_0)|<\varepsilon/2$ whenever $|x-x_0|<\delta$. The triangle inequality gives $|A(x)-A(x_0)|<\varepsilon$.

For all real $x,y$, the original defect estimate also gives

$$
|F_k(x+y)-F_k(x)-F_k(y)|\le D2^{-k}.
$$

Passing to the limit at these three arguments shows that $A(x+y)=A(x)+A(y)$. Additivity implies $A(0)=0$, $A(-x)=-A(x)$, and $A(q)=qA(1)$ for each rational number $q$. For any real $x$, choose rational numbers $q_j\to x$. Continuity then gives

$$
A(x)=\lim_{j\to\infty}A(q_j)=xA(1).
$$

The slope is fixed by the given integer limit, since $2^k$ is a positive integer and tends to infinity:

$$
A(1)=\lim_{k\to\infty}\frac{f(2^k)}{2^k}=2014.
$$

Finally, (1) with $m=0$ says $|A(x)-f(x)|\le D$ for every real $x$. Substituting $A(x)=2014x$ proves the claimed bound. $\square$

## Checked extensions

Exactly the same proof replaces $2014$ with any real number $L$, assuming $f(n)/n\to L$. It gives $\sup_x|f(x)-Lx|\le D$.

The constant $D$ cannot be reduced in general. For $f(x)=Lx+c$, the additive defect is the constant $-c$, so $D=|c|$, the required integer slope is $L$, and $\sup_x|f(x)-Lx|=|c|=D$.

**Editorial prerequisites:** completeness of $\mathbb R$, geometric series, continuity under uniform convergence, and rational approximation. **Editorial difficulty:** intermediate real analysis; the key discovery is the dyadic rescaling.
