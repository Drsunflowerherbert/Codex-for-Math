# Independent review — Yau 2023 written Analysis, Problem 4

**Spoilers:** this review discusses the answer and proof. The [authored solution](../solutions/yau-2023-analysis-p4.md) and [optional hints](../hints/yau-2023-analysis-p4.md) remain separate from the problem catalog.

**Problem ID:** `yau-2023-written-main-p4`.

**Verdict:** accepted in independent ordinary mathematical review on 2026-10-13 UTC. The interval-averaging proof, Fourier alternative, consequence about strong convergence, and separate hints all pass. No unresolved mathematical step was identified. This is an independent reading by an agent other than the author; it is not formal proof assistant verification or a human referee report.

## Independent source check

The reviewer separately read the extracted primary paper and rendered and visually inspected printed page 2, original Problem **4.**, from the [official written-paper archive](https://yau-contest.com/index/reldown?en=1&id=9). Exact member: `2010-2026历年笔试真题/2023/Analysis and differential equation.pdf`. The original assumptions are $2\pi$ periodicity, membership in $L^2([0,2\pi])$, and the dilations $x_n(t)=x(nt)$ indexed by positive integers. The authored setting preserves these conditions and the requested weak-convergence task. The paper does not specify real versus complex scalars; the proof handles either interpretation.

Source PDF SHA-256: `7c776d196d1ef100056e6ca70b1d56c390470faecf78a1158489d587410b44fb`.

No erratum affecting Problem 4 was identified in the inspected primary page. The statement that an official solution was not located is appropriately limited to the inspected archive and bounded searches.

## Mathematical checks

| Item | Independent finding |
| --- | --- |
| Mean and normalization | The mean is well-defined because $L^2$ on a finite interval is contained in $L^1$. Normalizing Lebesgue measure by $2\pi$ preserves the weak topology and correctly makes the mean a constant function. |
| Null-set representatives | The inverse image of a null set under $t\mapsto nt\pmod{2\pi}$ is a finite union of affine inverse images of null sets. Thus the dilation is well-defined on equivalence classes. Endpoint values do not affect any claim. |
| Cancellation on each interval | The change of variables traverses one complete period on each of the $n$ intervals and introduces the factor $1/n$. The centered function therefore integrates to zero on each interval. |
| Norm bound | The same changes of variables give exactly $\|y_n\|_2=\|y\|_2$, including the normalized measure factor. |
| Continuous test functions | Subtracting the left-endpoint value is justified by interval cancellation. The modulus-of-continuity bound and Cauchy–Schwarz yield $|\langle y_n,g\rangle|\le\|y\|_2\omega_g(2\pi/n)$. The proof does not require $g$ itself to be periodic. |
| Quantified weak convergence | The $C=0$ case is treated separately. For $C>0$, the continuous approximation and chosen $N$ make the two errors each smaller than $\varepsilon/2$ for all $n\ge N$. The monotonicity of $\omega_g$ justifies that quantifier. |
| Fourier alternative | The coefficient formula has the correct $1/n$ factor, conjugation convention, and root-of-unity phase. Mean zero handles frequency zero; for fixed nonzero $k$, the sum vanishes whenever $n>|k|$. Trigonometric-polynomial density and the uniform norm bound complete the proof. No pointwise Fourier convergence is assumed. |
| Strong-convergence consequence | The constant norm of $x_n-m$ proves strong convergence to the weak limit exactly when $x=m$ almost everywhere. |
| Hints and provenance | Each hint leads to a checked proof step. Hints and full proof are separate, explicitly authored, and linked to the original numbered problem. |

The density of continuous functions and of trigonometric polynomials in this $L^2$ space are standard theorems used explicitly. The solution's prerequisites should include these density facts; there is no unsupported exchange of limits and integrals. No additional generalization is claimed.

## Final reviewed artifact versions

- Authored solution SHA-256: `ea481b99d0e9bf556890ef5358603df52c4ef5e6c4d96047f5b3ab6b7e12bafd`.
- Hints SHA-256: `3325b5c90c3f8bb245faf457ca5d5f5aae9ead20d7f47f4c450a4acb576e2f31`.

These hashes identify the final files after checked math-delimiter, status, and review-link edits. Reviewer: agent `proof_2014`; author: agent `proof_2023`. Substantive proof changes require renewed review.
