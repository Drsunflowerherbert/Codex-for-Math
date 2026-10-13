# Hints: Yau 2023 written Analysis, Problem 4

**Spoiler warning:** these hints reveal progressively more of an approach. The [complete authored solution](../solutions/yau-2023-analysis-p4.md) is a separate file.

**Status:** authored hints accepted in an independent ordinary mathematical review by agent proof_2014 on 2026-10-13; see the [review record](../reviews/yau-2023-analysis-p4.md). **Problem ID:** `yau-2023-written-main-p4`.

Find the original problem in the [official written-paper archive](https://yau-contest.com/index/reldown?en=1&id=9), member `2010-2026历年笔试真题/2023/Analysis and differential equation.pdf`, printed page 2, Problem 4. No official solution was located in the bounded search; absence is not established.

<details>
<summary>Hint 1: What weak convergence asks for</summary>

Fix one test function $h\in L^2([0,2\pi])$. You need to understand the integral of $x(nt)\overline{h(t)}$ for large positive integers $n$, rather than the values of $x(nt)$ at individual points.

</details>

<details>
<summary>Hint 2: The natural partition</summary>

Split $[0,2\pi]$ into the $n$ intervals of length $2\pi/n$. On each interval, $nt$ runs through one full period of $x$. Calculate both the integral and the $L^2$ norm by the substitution $s=nt-2\pi j$.

</details>

<details>
<summary>Hint 3: Start with a continuous test function</summary>

Subtract the mean of $x$. Its dilated version then has zero integral on every interval of the partition. For continuous $h$, subtract the value of $h$ at the left endpoint inside each interval. Bound the remainder by the modulus of continuity of $h$.

</details>

<details>
<summary>Hint 4: Reach every L² test function</summary>

Use density of continuous functions in $L^2$. The dilation leaves the $L^2$ norm unchanged, so Cauchy–Schwarz bounds the error of replacing the fixed test function by a continuous one, uniformly in $n$.

</details>

<details>
<summary>Alternative hint: Test one Fourier frequency</summary>

Test against $e^{ikt}$, with $k\in\mathbb Z$ fixed. After splitting into periods, a root-of-unity sum appears. For $k\ne0$, it vanishes once $n>|k|$. Then use density of trigonometric polynomials.

</details>
