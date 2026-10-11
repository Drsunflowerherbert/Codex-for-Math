# Independent review of the common-support normal form

Verdict: accepted for the frozen `PositiveBlocks/NormalForm.lean` source below. No remaining blocker was found in the existence construction, its converse, the complete zero/nonzero equality classification, or the support/rank consequences.

This reviewer authored `Gram.lean` and `Intrinsic.lean`, and did not edit `NormalForm.lean`. The review is independent of the normal-form author's implementation. It is not a separate independent authorship audit of the imported Gram lemmas.

## Frozen source and verification

- Source: `PositiveBlocks/NormalForm.lean`.
- SHA-256: `32512a1aec69f99002b32155460b16336bddc656f352d34b4586e7bb2245ea8d`.
- Independently ran `lake env lean PositiveBlocks/NormalForm.lean`: exit 0, no errors or warnings. The command's output is recorded in `logs/gram-author-normal-form-compile.log`.
- Ran `lake build PositiveBlocks.NormalForm`: successful.
- Independently checked declaration types and axiom dependencies through `reviews/normal-form-axioms.lean`: exit 0. Results are recorded in `logs/gram-author-normal-form-axioms.log`.
- Rechecked the source SHA-256 after the commands; it was unchanged.

The checked major declarations depend only on `propext`, `Classical.choice`, and `Quot.sound`. The audit includes support compression, inverse square root, the normal-form constructor, both equality equivalences, norm/positivity converse, block/support rank, canonical support indexing, and the fixed norm-ratio witness. There are no `sorry` or `admit` proof placeholders, new axioms, `native_decide`, unsafe proof substitutions, or external proof implementations in the reviewed source. The word `admit` occurs only as ordinary prose in a documentation comment.

## Mathematical checks

`exists_posDef_compression` removes exactly the zero eigenvalues of a PSD row Gram matrix. Its nonzero hypothesis proves that the retained index type has positive cardinality. The selected unitary columns are isometric, the retained diagonal matrix is positive definite, and reindexing by `Fin k` preserves the reconstruction. This construction therefore handles rank-deficient ambient matrices without requiring an ambient inverse.

`exists_invSqrt` inverts the positive square root of this positive-definite compression. The only inverse is on the nonzero support matrix, not on potentially singular diagonal blocks. The proof obtains a Hermitian `L` with `L * H * L = 1`.

The projection lemma recovers both factors from the support of their row Gram matrices. For `Y * Yᴴ = t • (X * Xᴴ)` with `t > 0`, the construction rescales `Y` by `1 / sqrt t`. The resulting factor shares `X`'s row Gram matrix. The compression helpers then prove both isometry identities and all three exact reconstruction equations. In particular, the off-diagonal coefficient is `sqrt t`, and the right diagonal coefficient is `t`.

The converse uses a genuine positive-semidefinite congruence and Hilbert–Schmidt invariance under rectangular isometries. The complete equality theorem includes either zero factor as a separate branch; it does not apply the positive-support form to a one-zero case. An explicit empty-row instantiation of that theorem compiled in the independent audit.

The rank lemmas show that the support dimension fits both block dimensions and that the three block ranks and the full block-matrix rank coincide. `exists_rank_witness` indexes the support by `Fin A.rank`. The initially existential scale is made canonical by `exists_normRatio_witness`, which fixes it to `hsNorm C / hsNorm A`; the proof first establishes the denominator is nonzero. Thus the delivered API includes the precise scale used in PB3, rather than only a freely chosen positive scalar.

## Scope

The reviewed statements concern finite complex matrices and unnormalized Hilbert–Schmidt quantities. The constructor assumes proportional row Gram matrices; the equality equivalences use Gram blocks. The complete project supplies the PSD block-factorization wrappers. This review does not claim a full formalization of the surrounding Crouzeix theorem or any mathematical novelty.
