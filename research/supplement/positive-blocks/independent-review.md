# Independent review: positive-block inequalities

**Verdict: passed; no mathematical corrections required.** This is an independent ordinary proof review, supported by an exact regression rerun. It is not formal kernel verification. The reviewed artifact hashes and per-theorem findings are recorded in `independent-review.json`.

## Proof audit

- **Gram identities and sum bound:** All dimensions are compatible, including rectangular off-diagonal blocks. Trace cycling gives the stated norm identities and real nonnegative mixed trace. Expanding the Hermitian Gram square proves the exact sum and weighted deficits without assuming commutation. The alternative identity using the Hermitian matrix `SJS` is also correct.
- **Product bound:** A zero diagonal norm forces the corresponding Gram factor, and hence `B`, to vanish. For positive diagonal norms, the reciprocal congruence leaves `B` unchanged and the optimizing scale gives the product bound. No inverse of a diagonal block is needed.
- **Nonzero equality:** The normalized deficit proves equality exactly when `Q=tP` in every Gram realization. Multiplying out the intrinsic block equation produces all three stated identities; taking the first identity's trace proves the converse. For a minimal Gram realization, `P+Q=(1+t)P` is positive definite. Consequently the proposed `U`, `V`, and `H=P` are well-defined, `U` and `V` are isometries, and their products recover all three blocks exactly. Conversely the normal form is PSD and has the claimed norms. The rank and rectangular-dimension restrictions follow automatically.
- **Sum equality and edge cases:** Sum equality is correctly characterized by equal Gram matrices, the intrinsic equation, or nonzero product equality with equal diagonal norms. If either diagonal block vanishes, sum equality requires the entire matrix to vanish. Rank-deficient blocks, redundant Gram rows, complex phases, and unequal block sizes cause no gap in these arguments.
- **Consequences:** The equal-rank result, positive-definite strictness, kernel inclusions, compression corollary, and equal-size unitary reformulation are correct. In the last reformulation, one can take `W=UV*`.
- **Sharp constants:** Scalar equality proves optimality, and zero padding extends it to every fixed PSD dimension. The fixed-dimensional positive-definite epsilon family added during review has eigenvalues `2-epsilon` and `epsilon` with multiplicity `p+q-1`; its norm ratios approach the same constants. This addresses the one suggested editorial clarification.

## Examples and reproducibility

The reviewed standard-library checker was copied to an isolated temporary directory and rerun without changing the study artifacts. All **16 named examples** (12 PSD, four non-PSD) and **180 seeded Gaussian-rational fixtures** passed. Regenerated examples were byte-identical to `exact-examples.json`, and the regenerated summary matched `checks.json` exactly.

The example narratives agree with their matrices, norms, ranks, gaps, and positivity certificates. In E16, `WW*=I_2` and `Y=2XW` imply `Q=4P`; the recorded squared norms `(39,624,156)`, sum gap `351`, equality parameter `4`, and rank `2` are correct. The non-PSD, equal-rank, equal-norm, and Loewner-order counterexamples support precisely their stated caveats. Finite examples remain regression evidence, not a proof of the universal theorem.

## Provenance, records, and limits

The local TeX snapshot matches the recorded byte count and SHA-256. Lines 434–445 contain the cited positive-block sum comparison. This verifies local provenance consistency; remote commit identity was not independently fetched. The theorem records agree with the proof, and all 15 dependency IDs are unique, resolve, and form an acyclic graph.

The original files retain their initial pending-review fields; this separate review records completion for their exact hashes. No source implementation was executed, package installed, publication or import performed, Lean theorem certified, or complete Crouzeix claim reviewed.
