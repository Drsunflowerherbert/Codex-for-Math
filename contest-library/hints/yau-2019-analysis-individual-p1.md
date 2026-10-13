# Yau 2019 written individual Analysis, Problem 1 — optional hints

These are original authored hints for original label **1)**, page 1 of the official 2019 individual Analysis paper. Open the paper through the [official archive](https://yau-contest.com/en/lists-jxxg.html). The complete [authored solution](../solutions/yau-2019-analysis-individual-p1.md) is a separate spoiler.

<details>
<summary>Hint 1: compare values of the convex function</summary>

Set $M=\|u\|_\infty$, and handle $M=0$ first. If $M>0$, express each number $v\in[-M,M]$ as a convex combination of $-M$ and $M$. Compare $F(v)$ with the secant line through their two function values.

</details>

<details>
<summary>Hint 2: use the mean-zero assumption</summary>

The coefficient of $F(M)$ in that convex combination is $(v+M)/(2M)$. Substitute $v=u(x)$, then integrate. What is the integral of this coefficient over $[0,1]$?

</details>

<details>
<summary>Hint 3: make the equality argument quantitative</summary>

When $M>0$, the continuity and zero mean of $u$ force $u$ to vanish somewhere. At that point strict convexity gives a strictly positive difference between the secant value and $F(u(x))$. Continuity preserves a positive difference on an interval of positive length.

</details>

Status: original authored hints accepted with the proof in [independent agent review](../reviews/yau-2019-analysis-individual-p1.md); not official contest material.
