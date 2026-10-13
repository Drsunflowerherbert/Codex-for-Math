# Independent review — Yau 2014 written individual Analysis, Problem 1

**Spoiler:** this review discusses the proof. The [authored solution](../solutions/yau-2014-analysis-individual-p1.md) and [optional hints](../hints/yau-2014-analysis-individual-p1.md) are separate from the problem catalog.

Canonical identifier: `yau-2014-written-individual-p1`.

**Verdict:** passed independent agent review on 2026-10-13 UTC. The reviewed proof establishes the contest's boundedness claim and the stronger estimate $|f(x)-2014x|\leq D$ for every real $x$. No unresolved mathematical step was identified. This is an independent mathematical reading by an agent other than the author, not formal proof assistant verification or a human referee report.

## Source check

The reviewer independently rendered and visually inspected page 1 of the private PDF, original label **1.**, from the [official written archive](https://yau-contest.com/index/reldown?en=1&id=9), member `2010-2026历年笔试真题/2014/analysis2014(individual).pdf`. The real domain and codomain, continuity, uniformly bounded additive defect, integer-indexed slope limit, and requested bounded deviation all match the solution's setting. The stronger constant estimate is explicitly presented as an authored strengthening.

Source PDF SHA-256: `28a65742bc442aa93ec795f8df37c339dd11ab041554d187891359f4cbca17c1`.

## Mathematical checks

| Step | Independent finding |
| --- | --- |
| Dyadic rescaling | $F_k(x)=2^{-k}f(2^kx)$ is continuous and its successive difference is at most $D2^{-(k+1)}$. The exponent and factor are correct. |
| Tail estimate and limit | The geometric sum is exactly $D(2^{-m}-2^{-n})$; the resulting limit exists pointwise and satisfies the global error bound $D2^{-m}$. |
| Continuity | The error bound is uniform on all of $\mathbb R$. The included $\varepsilon$-$\delta$ argument correctly proves continuity of the limit; it also covers $D=0$. |
| Additivity | Rescaling the defect by $2^{-k}$ and taking limits at the three fixed arguments gives exact additivity. |
| Linearity | Additivity determines rational values, and continuity extends the formula to every real argument, including negative arguments and zero. |
| Slope | The sequence $2^k$ lies among the positive integers and tends to infinity, so the stated integer limit gives $A(1)=2014$. |
| Final estimate | Taking $m=0$ gives $|f(x)-A(x)|\leq D$, hence the claimed boundedness with an explicit bound. |
| Generalization | Replacing $2014$ with any real $L$ changes only the slope identification; the same proof remains valid. |
| Sharpness | For $f(x)=Lx+c$, the defect is $-c$, its supremum is $|c|$, and the deviation is exactly $|c|$. This validates the claimed sharpness of the coefficient of $D$. |
| Hints | Each hint matches a valid step of the proof. The hints are in a separate file and do not claim official provenance. |

No correction is required for mathematical validity or source fidelity. No erratum affecting this problem was identified in the inspected source. The record makes no broader claim about the existence of official solutions.

## Reviewed artifact versions

- Accepted authored solution SHA-256: `670bc7e34e2cdb4447ae83060a1d5e1e489bc6f78af5081e9a5bd751285cd77e`.
- Accepted hints SHA-256: `d8771ffee6e17679919689a828fac1b029d6f1f4f20a1f8bb6b5ca8085e97d3a`.

Reviewer: independent agent `proof_2019`; author: agent `proof_2014`. The reviewer also inspected the later delimiter conversion and status/review-link edits and confirmed that they do not alter the mathematics. These hashes identify the accepted artifact bytes after those edits. Substantive proof changes require renewed review.
