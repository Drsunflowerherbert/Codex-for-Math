# Independent mathematical review of the learning guide

Review date: 11 October 2026 UTC.

## Verdict

The nine methods, their displayed deductions, and their worked examples pass ordinary mathematical review under the hypotheses stated in the final guide. No unresolved mathematical blocker was found. The guide is suitable for a mathematics major with real analysis and some abstract algebra; its explicit warning that mixed moments require further measure-theory prerequisites is appropriate.

I read the complete guide, independently checked its calculations and implications, and consulted the accompanying studies and existing reviews where longer proofs are abbreviated. This is a review of the guide and its selected supporting arguments, not of the source manuscripts' headline conclusions.

## What was checked

1. **Tangent pointwise bounds:** the finite-denominator repair, pole-distance conversion, negative-exponent comparison, scaled limits, and the nonsharp absolute-convergence threshold are correct.
2. **Tangent packing:** the separate pole-distance and pair-spacing inputs, zero-multiplier case, two-sided harmonic packing, dyadic exponent, and unconditional divergence argument are correct. Sufficiency remains conditional on H.
3. **Egyptian fractions:** fixed-length finiteness, both rewrite identities and strict denominator-sum increments, arbitrary-choice termination, the worked cleanup and padding examples, and the coarse iterated maximum-denominator bound are correct. The displayed iteration follows directly from M_{j+1}+1 ≤ (M_j+1)²; this review checks that corollary, without reviewing a separate supplemental document in full.
4. **Finite-field mixing:** the Fourier normalization, factor pab in the bilinear estimate, p−1 nonzero frequencies, strict positivity, four-product criterion, and p=7 example are correct with the stated independence.
5. **Positive blocks:** both Gram deficit identities, rectangular dimensions, zero-block cases, equality distinction, stability estimate, and scalar examples are correct.
6. **Radial geometry:** existence and uniqueness, crossing inequality, radius and contact constants, joint perturbation bound, nonunit-direction example, and nonnegative-parameter residual certificate are correct without strict convexity or ambient compactness.
7. **Mixed moments:** the absolute-integrability majorant, valid-index moment recurrence, diagonal reduction, displayed constant decomposition, coefficient identity, and all four worked values are correct. Cancelling a specified coordinate does not require injectivity of evaluation; a surviving coordinate does not establish nonmembership in the smaller real span.
8. **Affine budgets:** the dyadic density cost, total weight 7/3, bound 7η/24, both dilation signs, compactness, and r>2 budget criterion are correct. The normalized hitting-set hypothesis remains an input.
9. **Transport obstruction:** the affine-slack optimality certificate, atom masses, symmetric-difference probability, both exact squared distances, and obstruction for exponents above 1/3 are correct. This does not prove the endpoint upper bound.

The optional convex-approximation continuation correctly distinguishes positive spanning from a uniform Hessian lower bound and retains finite-dimensional scope.

## Clarifications incorporated

The author incorporated these review corrections before acceptance:

- Line 128: explicitly require δ>0 in the abstract packing lemma.
- Line 208: define M_j as the largest denominator after j padding steps.
- Line 380: retain t≥0 in the radial residual certificate. Negative contact roots would invalidate an unrestricted assertion.
- Line 425: restrict the moment recurrence to i≥1, with m_{−1}=0.

## Evidence boundary

The guide separates ordinary proofs, finite exact checks, and reported formal builds. Its completed radial, Egyptian, and conditional tangent counts are attributed to the pinned publication evidence; the other three formal projects remain pending in the stated snapshot. It does not infer a proof of PiDiophantine or a headline manuscript from these counts. The Egyptian aggregate-exit-code limitation and the narrower formal scope of iterated padding are disclosed.

This review did not run Lean, execute repository programs, reproduce the finite regression suites or formal builds, or inspect every formal theorem type and axiom inventory. It does not establish novelty, external peer review, or correctness of unreviewed manuscript arguments.

## Reviewed version

Guide: `verified-techniques.md` in the same directory.

SHA-256: 89331a70131ad5c28c5a162ab7457b6ea85ce2ea192d35f6dfe7817b50bfd155
