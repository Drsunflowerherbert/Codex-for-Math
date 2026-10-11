# Independent final source, type, and axiom review

**Verdict: accepted within the requested positive-block scope, with no required proof corrections and no unresolved core proof gap.** This is a finished written review of the exact frozen production sources fingerprinted below. It completes the written-verdict step identified as unfinished in the checkpoint's `CONTINUATION.md`. The archived `reviews/final-source-review.md` remains historical in-progress material; its mere presence was not treated as acceptance.

The accepted scope is the finite-dimensional complex positive-block Hilbert–Schmidt inequalities, exact deficits, equality cases, intrinsic equations, full common-support normal-form existence and converse, rank consequences, compression results, and the exported sharpness examples. This verdict does not certify the complete Crouzeix theorem, novelty, publication, native theorem-record schema compatibility, or every ordinary claim in the supplied study.

## Independence and work performed

An independent finalization reviewer performed this inspection. This reviewer did not author or edit any production proof or earlier report. All ten production Lean files and all seven Lean review/audit companions were inspected. I reviewed all 142 elaborated public declaration types and their axiom records in the corrected archived audit, compared the declarations with a separately reconstructed source inventory, read the mathematical study and relevant source paragraph, and inspected the completion documentation, prior reviews, pin/provenance records, compilation receipts, exact-example summaries, and recovery records.

Own read-only Python inspection independently checked file hashes, source/import/declaration inventories, the audit-to-source correspondence, all compilation-log receipt hashes, the checkpoint manifest, and the study dependency graph. No source-owned Python script, Lean compiler, exact checker, repository command that mutates state, or external source program was executed by this reviewer. A fresh pinned build and fresh audits in the final repository belong to the publication finalizer and are separate evidence; this report does not claim that they have already run.

Earlier independence boundaries were preserved: the core reviewer authored `Basic.lean`, the normal-form reviewer authored `Gram.lean` and `Intrinsic.lean`, and the ordinary mathematics reviewer assisted with three normal-form helpers. Their reports remain supporting evidence, rather than substitutes for this independent full-source inspection.

## Exact source and audit coverage

The umbrella imports all nine production modules. Its complete local import closure consists of ten Lean files. The independently reconstructed inventory exactly matches all 142 entries in `reviews/final-source-audit.json`, the `#check @...`/`#print axioms` harness, and the corrected log's 142 type/axiom pairs. There are no missing or duplicate public declarations.

| Production source | Public theorems | Definitions | Private helper theorems |
|---|---:|---:|---:|
| `PositiveBlocks/Basic.lean` | 21 | 3 | 0 |
| `PositiveBlocks/Gram.lean` | 10 | 0 | 1 |
| `PositiveBlocks/Blocks.lean` | 30 | 0 | 0 |
| `PositiveBlocks/Intrinsic.lean` | 14 | 0 | 3 |
| `PositiveBlocks/Corollaries.lean` | 3 | 0 | 0 |
| `PositiveBlocks/Sharpness.lean` | 3 | 0 | 0 |
| `PositiveBlocks/NormalForm.lean` | 31 | 1 | 0 |
| `PositiveBlocks/Classification.lean` | 7 | 0 | 0 |
| `PositiveBlocks/Examples.lean` | 12 | 7 | 0 |
| `PositiveBlocks.lean` | 0 | 0 | 0 |
| **Total** | **131** | **11** | **4** |

Thus the project has 142 public named declarations, and 146 production named declarations when the four private theorem helpers are included. It has 135 named production theorem statements in total. Anonymous API checks in review companions are supplementary checks, not additional public library theorems. Private helpers were read and are used by audited public proofs, so their dependencies are included transitively in the public axiom audit.

Every one of the 142 archived public axiom records is exactly `[propext, Classical.choice, Quot.sound]`. None contains `sorryAx` or any additional axiom. A comment/string-aware whole-token scan of all 17 Lean files found no `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `extern`, `implemented_by`, `run_tac`, custom elaborator, macro, or initialization declaration in executable Lean source. The word `admit` in a normal-form documentation comment is ordinary prose. The seven review Lean companions contain only imports, printer settings, audit commands, and the displayed independent examples.

## Theorem assumptions and mathematical correspondence

`hsSq M` is the real part of `trace (Mᴴ * M)`, and `hsNorm M` is its real nonnegative square root. `hsSq_eq_sum` establishes the unnormalized entrywise sum of `Complex.normSq`; `hsNorm_sq`, zero detection, and real scaling follow correctly. `hsNorm_eq_frobenius` explicitly selects mathlib's Frobenius norm scope. No claim relies on a default matrix norm instance.

All matrices are complex. Index types are arbitrary finite types, with no common-size assumption on the two block dimensions. Core Gram identities, block Gram existence/iff, inequalities, weighted equality, and zero classification allow empty types and singular blocks. Some isometry and construction APIs carry explicit `DecidableEq` instances; these are computational typeclass parameters, not nonemptiness or invertibility assumptions. `gram_eq_zero_iff` requires only the finite row type. The factorization statements correctly keep the same row type for both factors.

For `A=XᴴX`, `B=XᴴY`, `C=YᴴY`, `P=XXᴴ`, `Q=YYᴴ`, write `a=hsNorm A`, `c=hsNorm C`, and `β=hsSq B`. Rectangular trace cycling and the real HS inner product prove the exact sum gap `a²+c²−2β=hsSq(P−Q)`. Nonnegativity and zero detection give the sum inequality and equality iff `P=Q`. The weighted product identity is `hsSq(c•P−a•Q)=2ac(ac−β)`. The inequality and iff proofs explicitly handle zero norms before canceling positive factors, yielding `β≤ac` and `β=ac ↔ c•P=a•Q` globally. This includes either one-zero diagonal case.

The normalized criterion `P/a=Q/c` and the exact normalized deficit `(ac−β)=(ac/2)hsSq(P/a−Q/c)` require and include both `a>0` and `c>0`. The duplicate Gram normalized-deficit declarations in `Intrinsic.lean` and `Corollaries.lean` have the same correct formula. The norm ratio is `c/a`, not its square. The reciprocal-weighted study identity follows by specializing the general expansion; the implementation's direct weighted-deficit proof of the product bound is valid without reproducing the study's optimizing-congruence proof.

Direct block consumer theorems require positivity of the **whole** `fromBlocks A B Bᴴ C`, not merely of `A` and `C`. Principal-square-root factorization supplies row type `m ⊕ n`; taking the two column submatrices gives all three factorization equations. The iff converse constructs an actual common Gram matrix. Arbitrary-factor wrappers quantify over every finite common row type and include all three equations, so their equality tests are independent of the chosen realization, including redundant rows. A zero diagonal forces `B=0`. Product equality then holds; sum equality with either zero diagonal forces all blocks to vanish.

The intrinsic product iff needs only `a>0`, and remains correct with `c=0`. Its polynomial form is `BBᴴ=(c/a)•A²`, `C²=(c/a)•(BᴴB)`, and `BC=(c/a)•AB`. Proportional Gram matrices give these equations; tracing the first equation alone gives `β=ac`. The division-free second equation correctly extends the study's inverse-ratio form to a zero right block. The intrinsic sum iff uses the three unscaled equations and no nonzero hypotheses; tracing its first two equations proves the reverse implication. Adjoint order and rectangular dimensions are correct throughout.

The common-support construction is present, rather than just its converse. `exists_posDef_compression` retains exactly the nonzero eigenvalues of the PSD row Gram matrix, proves they are strictly positive, obtains positive support cardinality from its nonzero hypothesis, and reindexes the selected unitary columns by `Fin k`. `exists_invSqrt` inverts only the positive-definite support square root. The support projection recovers each factor; rescaling `Y` by `(sqrt t)⁻¹` under `t>0` produces a factor with the same row Gram as `X`. The two compression lemmas prove both isometry identities and reconstruct all three blocks with coefficients `sqrt t` and `t`. No ambient diagonal or row Gram inverse is assumed.

`HasCommonSupportNormalForm` requires `k>0`, `H.PosDef`, `t>0`, `UᴴU=VᴴV=1`, and the displayed formulas `A=UHUᴴ`, `B=sqrt t•UHVᴴ`, `C=t•VHVᴴ`. Its converse proves full PSD and product equality. The Gram nonzero iff requires both factors nonzero; its global iff separates either zero factor. The block nonzero iff requires full PSD and both diagonals nonzero; its global iff is exactly `A=0 ∨ C=0 ∨ HasCommonSupportNormalForm A B C`. These zero branches are essential because a positive-dimensional positive-definite form cannot represent one-zero cases.

The rank results prove the three block ranks, and the full block rank, equal the positive support size, bounded by both ambient dimensions. The factor-rank consequence also bounds it by the common row dimension. The support can be indexed by `Fin A.rank`, and the scale can be fixed to `hsNorm C / hsNorm A`; the proof establishes the denominator nonzero before cancellation. Positivity of that ratio follows from the normal form's nonzero diagonals. The full block-rank proof uses an explicit left inverse of the stacked factor, so its weaker assumptions on the lower stacked part are sound.

Compression positivity is a genuine rectangular congruence. Factors `sqrt(S)U` and `sqrt(S)V` recover the compressed blocks, and both sharp estimates specialize correctly without isometry assumptions on `U,V`. Scalar examples prove the optimal universal product coefficient `1` and largest left sum coefficient `2`; zero-padded witnesses give squared norms `1,1,1` in every nonempty pair of dimensions. Those witness APIs explicitly require nonempty dimensions (or selected entries). The rectangular Lean fixture correctly has squared norms `17,17,17` and rank-two equality; zero and empty-column examples are exact.

## Formalization limits, rather than proof gaps

No proof placeholder, missing core implication, hidden positivity assumption, zero/rank degeneracy error, or coefficient error was found in the accepted source. The ordinary study is broader than the exported API. The following are not separately exported Lean theorems and must not be advertised as fully formalized merely because ingredients are available:

- Combined signature-matrix equations `Δ diag(tI,−I) Δ=0`, the alternative `SJS` trace proof, and a standalone right-square-only product equality criterion.
- General kernel inclusions and the general PSD off-diagonal rank bound outside equality.
- Standalone positive-definite strictness, unequal-dimension positive-definite strictness, and the equal-size unitary reformulation.
- Positive-definite limiting sharpness families/limit theorems and a separately named smallest right sum coefficient `1/2` theorem.
- A separately named reciprocal-weighted Gram gap or full complex mixed-trace equality/reality theorem; the exported identities use the real HS inner product and supply the expansion needed by the core proofs.

These are scope limits, not blockers to the requested inequalities, exact core deficits, complete zero/nonzero classification, intrinsic iff criteria, or common-support existence/converse. A positive-definite strictness extension allowing empty ambient types would need explicit nonempty left and right types; the current source makes no such unrestricted strictness claim.

## Receipts and provenance

The 73-file unpacked checkpoint has exactly the 72 files listed by `CHECKPOINT-SHA256.json` plus that manifest itself. Every listed byte count and SHA-256 matches, with no extra file. All ten production fingerprints match the archived fresh-build, final-source-audit, and recovery records. All ten independent compilation receipts have exit `0`; their empty log hashes match. The corrected declaration receipt has exit `0`, 136,050 log bytes, SHA-256 `1f3bcb4ce1c32c299cdb83a04484a29c934593614098514eaca1c91614ca795b`, and no error, warning, or `sorryAx` line. The separate initial audit failed solely on unknown printer option `pp.width`; its log remains separate historical failure evidence and was not counted as a passing run.

The archived author fresh build completed successfully at `2026-10-11T03:38:00.753478+00:00`, after deleting only project-generated build output; pinned dependency OLeans were reused. The archived independent compilation/audit record is dated `2026-10-11T03:42:59.786662+00:00`. These are inspected existing receipts, not fresh executions by this reviewer. Toolchain, Lake configuration, and manifest agree on Lean `leanprover/lean4:v4.24.0` and mathlib `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The manifest hash matches the archived toolchain receipt.

The study has ten theorem records and five background dependency nodes. Independently checked IDs are unique, all dependency references resolve, and the graph is acyclic. Its initial pending/ordinary-only metadata is preserved historical study metadata. Local study, records, exact-example data, and TeX hashes match the earlier reference reviews. The supplied 35,175-byte TeX paragraph at lines 434–445 states the equal-size positive-block sum comparison; the rectangular/product/equality extensions are separately justified in the study and formal source. Remote commit authentication was not performed. The input archive hash remains recorded provenance; this reviewer inspected the supplied bytes rather than downloading the archive.

Existing exact-example receipts report 16 named Gaussian-rational examples and 180 seeded fixtures. They are finite supplementary checks, not universal proofs, and were not rerun here. The tangent-preservation receipt is historical evidence inspected for consistency; this reviewer did not touch the tangent repository, final public repository, or either dependency cache.

## Frozen production fingerprints

| Source | SHA-256 |
|---|---|
| `PositiveBlocks/Basic.lean` | `aa32109f23367aecde51d21179015007577ecdcfdb9b50903251a46b09b7eb45` |
| `PositiveBlocks/Gram.lean` | `bb332f13fe9edadc82647f932f62c8a55399fd138b2647471f9f264daf27673d` |
| `PositiveBlocks/Blocks.lean` | `36dddf5ca7c8eb43080728e1ef13e9ccb9cb938c76dc0a98b1d5e900c60d9cb9` |
| `PositiveBlocks/Intrinsic.lean` | `dcaf52c30231c3c16f7d930cc0e689451e3c46f8263526b13bfe2ea9cdd311c7` |
| `PositiveBlocks/Corollaries.lean` | `7f020e5cbadb6f56de4fbbf649d2dba738d9d19b0a9e25b98ec5790b01bbc861` |
| `PositiveBlocks/Sharpness.lean` | `acf8f5c68b858290ccd28dc5c1b5a3b0af0f691b01fe7ae7064bd613c50b454f` |
| `PositiveBlocks/NormalForm.lean` | `32512a1aec69f99002b32155460b16336bddc656f352d34b4586e7bb2245ea8d` |
| `PositiveBlocks/Classification.lean` | `90864094f9a16fba4ecf3e0087529f43e112069e832f38413f342478daf7a12d` |
| `PositiveBlocks/Examples.lean` | `6d3c381ce5829a482385dacace066f9489baf8b3a310895112780c92df55b9eb` |
| `PositiveBlocks.lean` | `172a370711ed194392f1489e878d4a202e35e5d554e4c859f2c049b2396007b8` |

The companion source-coverage JSON gives per-file hashes, all named production declarations, private-helper coverage, raw elaborated public types with log locations, and each axiom set. The companion review JSON separates this completed source verdict from the separate publication-session verification. Documentation may now cite a finished source-review verdict for these exact fingerprints, while retaining the scope limits and the initial printer failure as historical evidence.

Publication note: reviewer identity and internal coordination wording were omitted. The verdict, mathematical scope, assumptions, source fingerprints and independence disclosures are preserved. The fresh publication results are separate records.
