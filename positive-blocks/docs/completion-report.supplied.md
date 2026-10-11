# Completion report

**Recovery status:** this document describes the compiled source coverage.
At the supplied checkpoint, the final written verdict was unfinished. This
historical report records compiled source coverage; the later final review and
fresh publication checks are separate records.

The requested core and the full nonzero common-support normal form are Lean
proofs in this library. Zero cases are classified separately and exactly.
The supplied study is an ordinary mathematical reference; its historical
verification metadata is preserved and does not describe the new Lean work.

## Scope of formalization

| Study record | Formal source and scope |
|---|---|
| PB0, Gram trace identities | `Basic.lean`: trace/sum norm definitions, rectangular Gram swapping and mixed trace identity. |
| PB1, sum gap and bound | `Gram.lean`, `Blocks.lean`: exact unweighted gap, sharp sum bound, equality iff equal row Gram matrices; weighted expansion follows from `hsSq_weighted_sub`. |
| PB2, product bound | `Gram.lean`, `Blocks.lean`: product inequality with exact zero branches. The formal proof uses the weighted deficit rather than reciprocal congruence optimization. |
| PB3_PRODUCT, equality | `Gram.lean`, `Classification.lean`, `NormalForm.lean`: weighted/normalized Gram iff, positive common-support normal form iff, zero alternatives, rank-indexed fixed-ratio witness. `Intrinsic.lean`: three intrinsic block equations, including equivalence with the first equation alone. The signature-matrix equation is not a separately exported theorem. |
| PB3_SUM, equality | `Gram.lean`, `Corollaries.lean`, `Intrinsic.lean`: equality iff equal row Gram matrices; iff product equality plus equal diagonal norms; iff three intrinsic block equations. The signature-matrix equation is not separately exported. |
| PB3_DEFICIT | `Corollaries.lean` and `Intrinsic.lean`: exact normalized deficit under positive diagonal norms. |
| PB3_RANK | `NormalForm.lean`, `Classification.lean`: equal positive support/block/factor ranks and support bounds; full block rank is proved in the common-support representation. Positive-definite strictness is a remaining corollary, not separately exported. |
| PB3_KERNEL | Zero-block conclusions are proved. General kernel inclusions and the arbitrary-PSD rank bound are not separately exported. |
| PB4_SHARPNESS | `Examples.lean`: scalar sharpness and optimal universal coefficients. `Sharpness.lean`: zero-padded equality witnesses for every nonempty pair of dimensions. Positive-definite limiting families are retained as ordinary study arguments and exact regression examples, not Lean limit theorems. |
| PB5_COMPRESSION | `Blocks.lean`: PSD compression, product/sum estimates, and equality criteria for explicit factors. |

These unexported corollaries are optional extensions, not blockers to the
requested inequality, exact identity, normalized equality condition, or complete
common-support normal form.

## The key assumptions

Matrices are complex and index types carry `Fintype` instances. Core identities,
inequalities, Gram representations, and zero classifications allow empty types.
Normalized equalities and normalized deficits require strictly positive diagonal
norms. The common-support predicate uses `k > 0`, `H.PosDef`, `t > 0`,
`Uᴴ * U = 1`, `Vᴴ * V = 1`, and the three displayed block formulas.
Nonempty ambient types are required for the fixed-dimension sharpness witnesses.
No invertibility assumption is made on either original diagonal block.

Actual elaborated theorem types and `#print axioms` output are in the reviewer
audit files. Those outputs, rather than summaries here, are authoritative about
all implicit typeclass arguments.

## Evidence

The fresh project build removes this project's generated `.lake/build` and
recompiles its source against clean pinned mathlib dependencies. A separate
reviewer recompiles the import closure into a different output directory and
records every public theorem's actual type and axiom set. The mathematical
review, independent core review, independent normal-form review, and final
source review disclose their authorship boundaries.

The Lean examples check scalar sharpness, a complex scalar squared norm,
rectangular rank-two positivity and equality, zero matrices, and empty columns.
Both inspected Python exact checkers passed 16 named cases and 180 seeded
Gaussian-rational Gram fixtures; these are finite regression evidence only.

Retained historical toolchain and source fingerprints, build results and
reviewer results are in `logs/` and `reviews/`. Internal checkpoint and
repository-preservation records were omitted from publication. The current
source map records these exclusions without their contents.

The work is confined to this elementary finite-dimensional supporting lemma.
It asserts no Crouzeix headline result, research novelty, publication, or native
schema import. This supplied report predates publication.
