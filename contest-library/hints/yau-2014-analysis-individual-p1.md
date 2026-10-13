# Separate hints — Yau 2014, written individual Analysis, Problem 1

**Canonical problem ID:** `yau-2014-written-individual-p1`.

**Status:** accepted in [independent agent review](../reviews/yau-2014-analysis-individual-p1.md) by `proof_2019` on 2026-10-13; no formal verification is claimed.

**Spoilers:** open only after trying the [official problem paper](https://yau-contest.com/index/reldown?en=1&id=9), member `2010-2026历年笔试真题/2014/analysis2014(individual).pdf`, Problem 1, page 1. These hints are authored here and are not official contest material.

<details>
<summary>Hint 1: turn the bounded error into a shrinking error</summary>

Denote the finite defect bound by $D$. Compare $f(2x)$ with $2f(x)$, and try repeating the comparison at $2x,4x,\ldots$.

</details>

<details>
<summary>Hint 2: choose a rescaling with a summable error</summary>

Define $F_k(x)=2^{-k}f(2^kx)$. Prove that

$$
|F_{k+1}(x)-F_k(x)|\le D2^{-(k+1)}
$$

for every real $x$. The bound is independent of $x$, so the geometric tail also controls convergence uniformly.

</details>

<details>
<summary>Hint 3: identify the limiting function</summary>

Let $A(x)=\lim_kF_k(x)$. Show that $A$ is continuous, additive, and satisfies $|A(x)-f(x)|\le D$. A continuous additive real function is linear. Evaluate $A(1)$ using the given limit along the integers $2^k$.

</details>

The [complete authored solution](../solutions/yau-2014-analysis-individual-p1.md) is a separate spoiler file.
