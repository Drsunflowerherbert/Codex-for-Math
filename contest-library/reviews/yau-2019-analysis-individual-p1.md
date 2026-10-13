# Independent review: Yau 2019 written individual Analysis, Problem 1

**Spoiler warning:** this review discusses the proof and equality case.

**Verdict:** accepted in ordinary mathematical review on 2026-10-13 by agent proof_2023, independently of the author, agent proof_2019. No unresolved mathematical step was identified. This review is not formal verification, a Lean proof, or an official contest solution.

The reviewed files are the [authored solution](../solutions/yau-2019-analysis-individual-p1.md) and [progressive hints](../hints/yau-2019-analysis-individual-p1.md). Canonical problem identifier: yau-2019-written-individual-p1.

## Exact reviewed versions

SHA-256 of the final solution bytes:

    27e2793e357f212da35bf79a7c2df03e0833ca16785e93e8d3e98142ea8656fc

SHA-256 of the final hint bytes:

    e92938b1dbbf533b2a3db7a3416aa78db63dd929f090887e95c65e8752832fe9

These hashes were recomputed after the author made only status and review-link updates to the accepted mathematical draft. Subsequent content changes require renewed review.

## Source check

The reviewer independently rendered and inspected printed page 1 of the English 2019 individual Analysis paper, original problem label 1), in the [official written-paper ZIP](https://yau-contest.com/index/reldown?en=1&id=9), available from the [official archive index](https://yau-contest.com/en/lists-jxxg.html). The local research-copy member is:

    2010-2026历年笔试真题/2019/Analysis2019-individual.pdf

The independently recomputed PDF SHA-256 is:

    48d82c28582e38e948f9d15ed0921314a9acec8417e3ec166734399fe35db047

Archive retrieval was recorded as 2026-10-13T04:38:28.667798+00:00. The check confirmed the domains, real values, strict convexity, continuity of the input function, mean-zero condition, definition of the supremum norm, inequality direction, and requested equality classification. No correction to these source conditions was needed. Availability of an official solution remains “not located in the bounded archive search,” rather than “does not exist.”

## Mathematical checks

1. The case of zero supremum norm is handled before any division. The compact-domain continuity assumption makes the supremum finite and forces the input function to be identically zero in that case.
2. A finite strictly convex function on the real line is convex and continuous. The author's elementary right-hand bounds follow from the stated convex combinations. The corresponding left-hand bounds, for $0<a<1$, are

   $$
   a\bigl(F(t)-F(t+1)\bigr)
   \leq F(t-a)-F(t)
   \leq a\bigl(F(t-1)-F(t)\bigr).
   $$

   They also tend to zero. Thus no unstated differentiability or continuity assumption on the convex function is required.
3. For positive supremum norm, the coefficients of the two endpoint values lie in the unit interval and reconstruct each value of the input function. Convexity therefore bounds the composed function by the secant line. Integrating the affine term and using the zero mean yields the stated inequality.
4. A continuous mean-zero input function has a zero. If it had no zero, connectedness would give a fixed sign, and compactness would give a strictly positive minimum absolute value, contradicting the zero integral.
5. Strict convexity at the two distinct endpoint arguments gives a strictly positive gap at that zero. The gap is a continuous nonnegative function; its value stays above half the positive gap on a relative interval of positive length. This remains true when the zero lies at an endpoint of the domain. The displayed integral lower bound is therefore strictly positive.
6. These checks prove equality exactly for the identically zero input function. No additional equality case, alternate proof, or unchecked generalization is asserted.
7. The three hints follow the accepted proof in increasing detail. They remain in a separate file, and the solution is clearly labeled as a spoiler. GitHub-compatible math delimiters are present.

The positive-gap estimate is qualitative in its neighborhood size but explicit in its quantifiers; the proof does not assert a uniform gap over all admissible inputs.
