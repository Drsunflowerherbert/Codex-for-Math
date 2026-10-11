# Independent mathematical review: positive block inequalities

Reviewer: `the project author`.


Initial mathematical review was completed independently before reading the supplied study. The completed Lean statements and proofs were reviewed on 2026-10-11 at 03:35 UTC; the exact reviewed source hashes appear below. Fresh build and axiom verification belong to a separate reviewer.

## Scope, evidence, and independence

Reviewed source: `docs/study-study.md`.

SHA-256: `fec0fdca335159320f13c572e34f77fa0dad3578ec76de4da6e4ae437a9c60af`.

I independently derived the Gram identity, product inequality, equality conditions, and common-support construction. I subsequently compared the study's PB0–PB5 arguments and its theorem records with those derivations. I have not relied on the study's earlier independent-review artifacts as evidence for my conclusions.

My production edits are limited to this report. I also tested three small mathlib API lemmas in the separate scratch file `ReviewNormalSupport.lean`, to identify an economical support construction for the implementation author. That scratch file compiled successfully with Lean 4.24.0. The implementation author incorporated this assistance into `unitary_columns_isometry`, `restrict_diagonal_support`, and `projection_fixes_factor`. I do not present review of those helper implementations as independent of their authorship. My mathematical derivation of the main claims preceded this assistance. The separate final-source reviewer independently checks the resulting library; I do not claim to have independently compiled the complete library.

## Mathematical conclusion

The study's mathematical claims are correct under its stated finite-dimensional complex PSD assumptions and its explicit use of the unnormalized Hilbert–Schmidt norm. No mathematical correction is required. The principal claims remain valid for empty index types, except that strictness and nonzero normal-form statements need the corresponding nonemptiness/nonzero hypotheses described below.

Let `X` have size `r × m`, let `Y` have size `r × n`, and put

\[
A=X^*X,\quad B=X^*Y,\quad C=Y^*Y,\quad P=XX^*,\quad Q=YY^*.
\]

Write \(a=\|A\|_F\), \(c=\|C\|_F\), and \(\beta=\|B\|_F^2\). Here the norm is unnormalized: its square is the sum of squared absolute values of all entries.

### Trace and gap identities

Rectangular trace cyclicity gives

\[
\|P\|_F^2=a^2,\qquad \|Q\|_F^2=c^2,\qquad
\operatorname{Re}\operatorname{tr}(PQ)=\beta.
\]

Neither commutation nor invertibility of `P,Q` is required. In fact the last trace is real and nonnegative because it is the squared norm of `B`. Expanding the squared norm gives

\[
a^2+c^2-2\beta=\|P-Q\|_F^2.
\]

The sum inequality follows, and sum equality is equivalent to `P=Q`. The weighted identity in PB1 is the same expansion after replacing `P,Q` by `sP,s⁻¹Q`; its stated assumption `s>0` is sufficient.

### Product inequality and all zero cases

Hilbert–Schmidt Cauchy–Schwarz gives \(\beta\le ac\). Equivalently, the following identity proves the inequality without appealing to its abstract equality theorem:

\[
\|cP-aQ\|_F^2=2ac(ac-\beta).
\]

If `a,c>0`, its left side is nonnegative and its positive multiplier can be canceled. If `a=0`, then `A=0`, hence `X=0` and `B=0`; the same argument applies with `c=0`. Thus product equality holds whenever either diagonal norm vanishes, including when the other diagonal block is nonzero.

The division-free equality characterization is valid without nonzero hypotheses:

\[
\beta=ac\quad\Longleftrightarrow\quad cP=aQ.
\]

With `a,c>0`, this is equivalent to

\[
P/a=Q/c,\qquad Q=tP,\qquad t=c/a>0.
\]

The exact normalized deficit is consequently

\[
ac-\beta=(ac/2)\|P/a-Q/c\|_F^2.
\]

This checks both the ratio orientation and the factor `1/2` in PB3_DEFICIT. The parameter `t` is the ratio of the diagonal HS norms, not their squares.

### Intrinsic block conditions

For \(\Delta=\left(\begin{smallmatrix}A&B\\B^*&C\end{smallmatrix}\right)\) and `t=c/a>0`, multiplication gives

\[
\Delta\operatorname{diag}(tI,-I)\Delta=
\begin{pmatrix}
tA^2-BB^*&tAB-BC\\
tB^*A-CB^*&tB^*B-C^2
\end{pmatrix}.
\]

When `Q=tP`, this matrix is zero by the common Gram factorization. Conversely, the trace of its top-left block gives \(\beta=ta^2=ac\). Thus the intrinsic equivalences asserted in PB3_PRODUCT are correct, including the sufficiency of its first diagonal identity alone under the stated PSD and fixed-ratio assumptions. The case `t=1` gives the sum-equality identities.

### Common-support normal form

Assume `a,c>0` and product equality. Let \(k=\operatorname{rank}P\). Then `k>0`; `Q=tP` implies the same support and rank for `Q`.

Choose an isometry \(W:\mathbb C^k\to\mathbb C^r\) onto \(\operatorname{ran}P\), and define

\[
H=W^*PW,\quad U=X^*WH^{-1/2},\quad
V=t^{-1/2}Y^*WH^{-1/2}.
\]

The matrix `H` is Hermitian positive definite. Direct multiplication yields `U*U=V*V=I`. Since the support projection `WW*` fixes both `X` and `Y`, one obtains

\[
A=UHU^*,\qquad B=\sqrt t\,UHV^*,\qquad C=tVHV^*.
\]

This also follows from the study's minimal-row Gram factorization. The inverses apply only to the positive definite support matrix, not to the possibly singular ambient blocks. Choosing eigenvectors of `P` makes `H` diagonal with strictly positive entries, although diagonal `H` is unnecessary for the claim.

Conversely, the displayed form, `H>0`, `t>0`, and isometric `U,V` give a PSD block matrix and

\[
a=\|H\|_F,\quad c=t\|H\|_F,\quad \beta=t\|H\|_F^2=ac.
\]

The dimensions obey \(1\le k\le\min(m,n,r)\). The normal form forces all of `A,B,C,Δ` to have rank `k`.

The one-zero cases must be separate. A form with positive `t`, positive-definite `H`, and nonzero support cannot represent either of them. Merely allowing `t=0` does not repair the full statement: if `C=0` and `rank A>n`, an isometry `V` from the support of `A` into the `n`-dimensional space does not exist. Both-zero blocks admit a zero-dimensional form when that convention is allowed, but a definition requiring `k>0` correctly excludes them.

### Remaining study claims

The rank restrictions, kernel inclusions, fixed-dimension sharpness examples, and PSD compression corollary follow as stated. Positive definiteness of the entire block matrix makes product equality impossible when both block dimensions are positive. If the Lean library permits empty types, a product-strictness theorem must retain nonempty left and right index types: with an empty left block and a positive definite right block, both sides of the product inequality are zero. No such issue arises for the non-strict inequalities.

The study correctly distinguishes full-block PSD from separate positivity of `A,C`; the latter does not imply either bound. It also correctly avoids claiming a Loewner-order inequality from a trace inequality or an original-block stability theorem from the exact normalized Gram deficit.

## Completed Lean statement and proof audit at 03:35 UTC

The inspected production files were `PositiveBlocks/Basic.lean`, `Gram.lean`, `Blocks.lean`, `NormalForm.lean`, `Classification.lean`, `Intrinsic.lean`, `Corollaries.lean`, `Sharpness.lean`, `Examples.lean`, and their umbrella imports. This is a mathematical sign-off for the precise source snapshot below; any subsequent changed statements require an additional check. It is distinct from the final-source reviewer's fresh build and axiom audit.

- `hsSq`, `hsNorm`, and `hsInner` use real parts of complex traces and an explicit real square root. `hsNorm_eq_frobenius` selects `Matrix.Norms.Frobenius` locally. This avoids accidentally using another matrix norm instance.
- `gram_sum_gap`, `gram_sum_le`, and `gram_sum_eq_iff` express the intended identity, inequality, and equality condition with compatible rectangular dimensions.
- `gram_product_deficit`, `gram_product_le`, and `gram_product_eq_iff` express the intended division-free deficit and equality classification, including zero factors. Their proofs explicitly handle vanishing norms before canceling positive factors.
- `gram_product_eq_iff_normalized` correctly requires both diagonal norms to be positive and normalizes `P` by `a` and `Q` by `c`.
- `exists_gram_of_posSemidef_fromBlocks` and its iff use the full-block PSD assumption and a common row index `m ⊕ n`. This construction works with singular blocks and empty index types.
- The block zero lemmas assume full-block PSD and the appropriate vanishing diagonal block. The compression statement uses a Hermitian/PSD common matrix and takes adjoints in the correct order.
- `HasCommonSupportNormalForm` requires `k>0`, `H.PosDef`, `t>0`, and both isometry equations. Its displayed block equations have the correct square-root and `t` factors. Explicit bounds `k≤card m,n` are implicit consequences of its isometries, not additional mathematical assumptions.
- The normal-form converse is mathematically sound, and its existence direction is now present and reviewed as detailed below.

### Completed normal-form construction and classification

`exists_posDef_compression` selects exactly the nonzero eigenvalues of a PSD matrix, proves their positivity from PSD, and restricts its unitary eigenvector matrix to those columns. Its support cardinality is positive because the original matrix is nonzero. Reindexing this subtype by `Fin k` preserves the isometry and reconstruction identities. This is a valid proof for singular matrices and does not insert an ambient invertibility assumption.

`exists_invSqrt` applies inversion only to the positive definite support matrix's square root. The two compression helpers correctly use the Hermitian inverse square root and the identity `L * H * L = 1`. `hasCommonSupportNormalForm_of_gram_proportional` first rescales `Y` to `Z=(sqrt t)⁻¹ • Y`; its positive-`t` assumption justifies the inverse and gives `Z*Zᴴ=X*Xᴴ`. The support projection consequently fixes both factors, and all three reconstructed blocks have the claimed coefficients.

`gram_product_eq_iff_commonSupportNormalForm` assumes both factors are nonzero and derives the positive scale `hsNorm (Yᴴ*Y) / hsNorm (Xᴴ*X)`. Its converse uses norm invariance under the two rectangular isometries. `gram_product_eq_iff_zero_or_commonSupportNormalForm` explicitly separates either zero factor. These match the independent mathematical classification exactly.

`block_hs_product_eq_iff_commonSupportNormalForm` and its norm version require full-block PSD and both nonzero diagonal blocks. `block_hs_product_eq_iff_zero_or_commonSupportNormalForm` and its norm version retain full-block PSD and correctly state the complete alternatives `A=0 ∨ C=0 ∨ HasCommonSupportNormalForm A B C`. PSD ensures the zero alternatives imply `B=0`; the theorem is not silently asserting this for arbitrary blocks.

`normalForm_ranks`, `HasCommonSupportNormalForm.rank_eq`, and the block classification rank corollaries prove equality and positivity of the three block ranks together with both dimension bounds. `gram_product_eq_rank_eq` additionally checks that the common rank fits the common row dimension. `normalForm_block_rank` and `HasCommonSupportNormalForm.block_rank` prove the full block matrix has this same rank: the stacked factor has the explicit left inverse `[Uᴴ,0]`, which is sufficient even without an isometry assumption on its lower part.

`HasCommonSupportNormalForm.exists_rank_witness` fixes the support size to `A.rank`; `exists_normRatio_witness` additionally fixes its scalar to `hsNorm C / hsNorm A`. Its cancellation is justified by the previously proved nonvanishing of `A`. The resulting ratio is positive because the normal form also makes `C` nonzero. `block_hsNorm_product_eq_exists_bounded_normalForm` makes the positive support size and upper bound by both block dimensions explicit.

### Intrinsic equality conditions, deficits, and sharpness

`gram_product_eq_iff_mul_conjTranspose` and `block_hs_product_eq_iff_mul_conjTranspose` correctly derive equality from the trace of the left square identity at the fixed ratio `c/a`. Their only norm assumption is `a>0`; no positivity of `c` is needed. The triple-identity versions use `C*C=(c/a) • (Bᴴ*B)`, which is equivalent to the study's inverse-ratio form when `c>0` and remains valid when `c=0`. This is a correct strengthening of the study statement, not a missing hypothesis.

`gram_sum_eq_iff_intrinsic` and `block_hs_sum_eq_iff_intrinsic` have the correct adjoint order and require no nonzero hypotheses. In the reverse direction, tracing the first two square identities gives the sum equality; the third intertwining identity is a necessary additional conclusion in the iff.

Both normalized-deficit theorems in `Intrinsic.lean` and `Corollaries.lean`, and the arbitrary-Gram wrapper, use the correct factors `ac/2`, `1/a`, and `1/c`, with both positivity assumptions present. `block_sum_eq_iff_product_eq_and_norms_eq` combines nonnegativity of the product deficit with `(a-c)^2≥0` and remains valid in the simultaneous-zero case.

The block and compression wrappers in `Blocks.lean` preserve the full PSD or explicit common-Gram assumptions. In particular, their arbitrary-Gram statements cover every finite common row type; they do not restrict equality to a minimal or square realization.

`Examples.product_coefficient_ge_one` and `Examples.sum_coefficient_le_two` obtain the claimed universal coefficient bounds from the scalar PSD equality witness. `Sharpness.exists_sharp_block` correctly assumes both ambient index types are nonempty and supplies zero-padded equality witnesses in every such pair of dimensions. The rectangular rank-two fixture has the intended phase and squared HS norms `17,17,17`.

The broader study also discusses positive-definite asymptotic sharpness, standalone kernel inclusions, and the single combined equation `Δ diag(tI,-I) Δ=0`. Those broader claims are mathematically sound, but I do not count them as separately exported Lean theorems merely because their ingredients are present. The completed core requested here—norm identity and inequalities, normalized and zero equality cases, intrinsic block identities, full common-support existence and converse, common ranks, dimension bounds, and the canonical norm ratio—is directly present in the reviewed source.

**Disposition: accepted mathematically.** No unresolved assumption error, rank-degeneracy gap, coefficient error, or missing direction remains in the reviewed core theorem statements and proofs. Build success and permitted axiom dependencies are assessed separately by the final-source audit.

### Reviewed source fingerprints

Paths are relative to `.`.

```text
aa32109f23367aecde51d21179015007577ecdcfdb9b50903251a46b09b7eb45  PositiveBlocks/Basic.lean
bb332f13fe9edadc82647f932f62c8a55399fd138b2647471f9f264daf27673d  PositiveBlocks/Gram.lean
36dddf5ca7c8eb43080728e1ef13e9ccb9cb938c76dc0a98b1d5e900c60d9cb9  PositiveBlocks/Blocks.lean
32512a1aec69f99002b32155460b16336bddc656f352d34b4586e7bb2245ea8d  PositiveBlocks/NormalForm.lean
90864094f9a16fba4ecf3e0087529f43e112069e832f38413f342478daf7a12d  PositiveBlocks/Classification.lean
dcaf52c30231c3c16f7d930cc0e689451e3c46f8263526b13bfe2ea9cdd311c7  PositiveBlocks/Intrinsic.lean
7f020e5cbadb6f56de4fbbf649d2dba738d9d19b0a9e25b98ec5790b01bbc861  PositiveBlocks/Corollaries.lean
acf8f5c68b858290ccd28dc5c1b5a3b0af0f691b01fe7ae7064bd613c50b454f  PositiveBlocks/Sharpness.lean
6d3c381ce5829a482385dacace066f9489baf8b3a310895112780c92df55b9eb  PositiveBlocks/Examples.lean
172a370711ed194392f1489e878d4a202e35e5d554e4c859f2c049b2396007b8  PositiveBlocks.lean
```
