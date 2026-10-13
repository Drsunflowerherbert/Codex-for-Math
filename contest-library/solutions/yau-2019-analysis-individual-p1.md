# Yau 2019 written individual Analysis, Problem 1 — authored solution

**Spoiler:** this file contains the complete proof and equality case. The [hints](../hints/yau-2019-analysis-individual-p1.md) are separate.

**Status:** original authored solution accepted in [independent agent review](../reviews/yau-2019-analysis-individual-p1.md) by `proof_2023` on 2026-10-13. No unresolved mathematical step was identified. This is a reviewed ordinary proof, not an official contest solution; it has not been formalized in Lean.

Catalog identifier: `yau-2019-written-individual-p1`.

**Source:** S.-T. Yau College Student Mathematics Contests 2019, *Analysis and Differential Equations*, Individual, original label **1)**, page 1. The English paper was checked visually against the official [past-paper archive](https://yau-contest.com/en/lists-jxxg.html), [written archive download](https://yau-contest.com/index/reldown?en=1&id=9), member `2010-2026历年笔试真题/2019/Analysis2019-individual.pdf`. Retrieval: 2026-10-13 UTC. No official solution was located in the bounded archive checks; this does not establish that none exists. The third-party paper is linked, not mirrored here.

Private paper SHA-256: `48d82c28582e38e948f9d15ed0921314a9acec8417e3ec166734399fe35db047`. Downloaded archive SHA-256: `f2f027f4f4a2d67d3d88609fdb41362cb29550f078893cee353fc24eba42121d`; retrieval timestamp: `2026-10-13T04:38:28.667798+00:00`.

## Mathematical setting

Write

$$
M=\|u\|_\infty=\sup_{x\in[0,1]}|u(x)|.
$$

The paper assumes a strictly convex, real-valued function $F:\mathbb R\to\mathbb R$, a continuous function $u:[0,1]\to\mathbb R$, and $\int_0^1u(x)\,dx=0$. We prove

$$
\int_0^1F(u(x))\,dx\leq\frac{F(M)+F(-M)}2,
$$

with equality precisely when $u(x)=0$ for every $x\in[0,1]$.

## Proof

Because $u$ is continuous on a compact interval, $M$ is finite. A finite convex function on $\mathbb R$ is continuous; an elementary verification is given below. Thus $F\circ u$ is continuous and the integral exists.

If $M=0$, then $u(x)=0$ for every $x$. Both sides are $F(0)$, so equality holds.

Suppose $M>0$. For each real number $v\in[-M,M]$, put

$$
\theta(v)=\frac{v+M}{2M},\qquad
L(v)=\theta(v)F(M)+(1-\theta(v))F(-M).
$$

Here $0\leq\theta(v)\leq1$ and $v=\theta(v)M+(1-\theta(v))(-M)$. Convexity therefore gives $F(v)\leq L(v)$. In particular, for every $x\in[0,1]$,

$$
F(u(x))\leq L(u(x))
=\frac{F(M)+F(-M)}2
 +\frac{F(M)-F(-M)}{2M}u(x).
$$

Integrating this pointwise inequality and using the zero mean of $u$ proves the required bound.

We now show that the bound is strict when $M>0$. First, $u$ has a zero: if it had none, the intermediate value theorem would force a fixed sign, and compactness would give $\min_{[0,1]}|u|>0$, contradicting $\int_0^1u=0$. Choose $x_0\in[0,1]$ with $u(x_0)=0$. Strict convexity at the distinct endpoints $-M,M$ gives

$$
\delta=L(0)-F(0)=\frac{F(M)+F(-M)}2-F(0)>0.
$$

The function $h(x)=L(u(x))-F(u(x))$ is continuous, nonnegative everywhere, and satisfies $h(x_0)=\delta$. Hence there is an $\eta>0$ such that

$$
x\in[0,1],\quad |x-x_0|<\eta
\quad\Longrightarrow\quad h(x)>\delta/2.
$$

The interval $I=[0,1]\cap(x_0-\eta,x_0+\eta)$ has positive length $|I|$, even if $x_0$ is an endpoint. Consequently

$$
\frac{F(M)+F(-M)}2-\int_0^1F(u(x))\,dx
=\int_0^1h(x)\,dx
\geq\frac\delta2|I|>0.
$$

Thus every nonzero $u$ under the stated assumptions gives strict inequality, completing the equality classification.

## Elementary continuity fact used above

For any fixed $t\in\mathbb R$ and $0<a<1$, convexity gives

$$
a\bigl(F(t)-F(t-1)\bigr)
\leq F(t+a)-F(t)
\leq a\bigl(F(t+1)-F(t)\bigr).
$$

For the lower bound, express $t$ as the convex combination of $t+a$ and $t-1$ with weights $1/(1+a)$ and $a/(1+a)$. The upper bound is the convexity inequality between $t$ and $t+1$. Both bounds tend to zero as $a\downarrow0$. Replacing the endpoints by $t-1,t$ gives the analogous left-hand bounds. Therefore $F$ is continuous at every $t$, with no extra regularity assumption.

## Source fidelity and review record

- All domains, continuity and strict convexity assumptions, the zero mean, the supremum norm, and the requested equality case were checked against page 1 of the private research copy.
- No erratum affecting this problem was identified in the inspected source.
- The proof treats $M=0$ before dividing by $M$, and makes the positive-measure step in the strict inequality explicit.
- Independent review: [passed](../reviews/yau-2019-analysis-individual-p1.md), including a separate source check and the equality argument.

Editorial prerequisites: convexity, the intermediate value theorem, integration of continuous functions. Editorial difficulty: introductory contest analysis.
