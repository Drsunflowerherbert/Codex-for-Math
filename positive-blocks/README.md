# PositiveBlocks

The independent [final source review](reviews/final-source-review.md) accepts
the requested scope with no unresolved core proof gap. It completes the written
review that was unfinished in the supplied checkpoint. Historical receipts and
the historical completion report remain separate from fresh publication checks.

The production source contains 142 public declarations: 131 theorems and 11
definitions, plus four private helper theorems. Declaration counts refer to
these exact statements, not the surrounding manuscript.

A standalone Lean library for finite-dimensional complex positive block matrix
inequalities, exact deficits, and equality cases. It uses **unnormalized
Hilbert–Schmidt (Frobenius) norms**, not a default matrix norm. Rectangular
off-diagonal blocks, singular matrices, zero blocks, and empty finite index
types are allowed unless a theorem explicitly assumes otherwise.

The library formalizes one elementary supporting matrix argument. It does not
establish the complete Crouzeix theorem and makes no novelty claim.

## Toolchain and build

The toolchain is `leanprover/lean4:v4.24.0`. Mathlib is pinned to
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7` in both the Lake configuration and
the supplied manifest. With that Lean toolchain installed:

```sh
lake exe cache get
lake build
```

The delivered archive contains source, the pinned dependency manifest,
documentation, exact examples, review reports, and verification evidence.
Dependencies and machine-specific build caches are excluded. Fresh publication
checks reused clean dependency OLeans at the recorded exact revisions; project
sources were recompiled. See `../publication/evidence/POSITIVE-BLOCK-CHECKS.json`.

## Mathematical conventions

For `M : Matrix m n ℂ`,

```lean
hsSq M = (Matrix.trace (Mᴴ * M)).re
hsNorm M = Real.sqrt (hsSq M)
```

`hsSq_eq_sum` proves `hsSq M = ∑ i, ∑ j, Complex.normSq (M i j)`.
`hsNorm_sq` proves `hsNorm M ^ 2 = hsSq M`.
`hsNorm_eq_frobenius` identifies `hsNorm` with mathlib's explicitly selected
Frobenius norm instance.

For common-row rectangular factors `X : Matrix r m ℂ` and
`Y : Matrix r n ℂ`, set `A = Xᴴ * X`, `B = Xᴴ * Y`,
`C = Yᴴ * Y`, `P = X * Xᴴ`, and `Q = Y * Yᴴ`.
The central compiled statements are:

- `gram_sum_gap`: `hsSq A + hsSq C - 2 * hsSq B = hsSq (P - Q)`.
- `gram_product_le`: `hsSq B ≤ hsNorm A * hsNorm C`.
- `gram_sum_eq_iff`: sum equality holds exactly when `P = Q`.
- `gram_product_eq_iff`: product equality holds exactly when
  `hsNorm C • P = hsNorm A • Q`, including all zero cases.
- `gram_product_eq_iff_normalized`: if both diagonal norms are positive,
  product equality holds exactly when `(1 / hsNorm A) • P = (1 / hsNorm C) • Q`.
- `gram_product_deficit`: the squared norm of
  `hsNorm C • P - hsNorm A • Q` equals
  `2 * hsNorm A * hsNorm C * (hsNorm A * hsNorm C - hsSq B)`.

`exists_gram_of_posSemidef_fromBlocks` proves that every PSD matrix
`Matrix.fromBlocks A B Bᴴ C` has such factors with row type `m ⊕ n`, using its
principal positive square root. `posSemidef_fromBlocks_iff_exists_gram` proves
the converse as well. `block_hsNorm_product_le` is the direct consumer theorem:

```lean
(Matrix.fromBlocks A B Bᴴ C).PosSemidef →
  hsNorm B ^ 2 ≤ hsNorm A * hsNorm C
```

The block module also provides sum inequalities, exact gaps and equality
criteria for every supplied Gram factorization, existential equality criteria,
zero-diagonal conclusions, and compression corollaries.

## Equality and zero cases

Either zero diagonal block forces `B = 0`, so product equality holds.
The nonzero normalized criterion must be used only with positive diagonal
norms. Sum equality additionally requires equal diagonal norms; hence sum
equality with one zero diagonal block forces both to vanish.

The normal-form module proves invariance under rectangular isometries and the
converse for
`A = U * H * Uᴴ`, `B = Real.sqrt t • (U * H * Vᴴ)`,
`C = t • (V * H * Vᴴ)`, with `Uᴴ * U = 1`, `Vᴴ * V = 1` and `t ≥ 0`.
The predicate `HasCommonSupportNormalForm` uses positive support dimension,
positive-definite `H`, and `t > 0`. The **existence direction and converse are
both proved**. The complete PSD equality classification is

```lean
block_hsNorm_product_eq_iff_zero_or_commonSupportNormalForm h :
  (hsNorm B ^ 2 = hsNorm A * hsNorm C) ↔
    A = 0 ∨ C = 0 ∨ HasCommonSupportNormalForm A B C
```

The nonzero form has common rank at most `min (Fintype.card m) (Fintype.card n)`.
There are explicit support witnesses and a witness at the fixed parameter
`t = hsNorm C / hsNorm A`; the common support may have any positive rank.

One-zero cases need separate branches: they generally do not have that same
positive-definite common-support form. In particular an isometry from the
nonzero block's rank into the other block dimension may not exist.

## Source and evidence

The input was `openai-math-reviewed-supplement-2026-10-11.zip`, 523,782 bytes,
SHA-256
`9e03b1ce33dc5d5fa62ab9478b06998bcb0eb32635fc11bccac065223e892a74`.
The archive bytes, hash, positive-block manifest and supplied TeX snapshot
were verified.
The local TeX source hash and its supplied revision attribution are recorded in
`logs/input-verification.json`; independent remote authentication is not claimed.

The bundled study has ten theorem records, reviewed ordinary proofs, and 16
named exact examples plus 180 seeded Gaussian-rational fixtures. The inspected
author checker and independent verifier passed on copied material. These finite
checks supplement, and do not replace, the Lean proofs.

`logs/toolchain-verification.json` records actual Lean version, binary hashes,
mathlib HEAD and clean-source status. Final fresh-build logs, theorem types,
`#print axioms` output, source hashes and independent reviews are supplied with
the final artifact. Production proofs contain no `sorry`, `admit`, or new axioms.

The generic license template in the checkpoint does not establish authorized
licensing of this new proof code and is excluded. Retained upstream text keeps
its source attribution and the repository's existing upstream license. No
new overall license is assigned by publication.
