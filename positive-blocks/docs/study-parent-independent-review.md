# Independent proof audit: positive-block Hilbert–Schmidt inequalities

## Decision

**Accepted for ordinary mathematical reuse, with no required corrections**, for the exact final artifacts fingerprinted below. This is a second, separate independent proof audit; it does not depend on the author's own checker or another reviewer's verdict.

The inequalities, exact gaps, scaling argument, complete equality conditions, rank consequences, sharp constants, compression corollary, and example arithmetic are correct within the stated finite-dimensional complex PSD scope. Neither formal kernel verification nor any complete Crouzeix theorem is established by this review.

Reviewed on 2026-10-11 UTC. Original author files were preserved. Initial and final snapshots, a copied author-checker rerun, and an independently written exact-arithmetic audit are kept beside this report.

## Scope and method

I read the full study, theorem/dependency records, provenance, author checker, check summaries, and source paragraph, then compared and inspected the final revision adding E16 and fixed-dimension positive-definite sharpness. Final file hashes match the author's supplied freeze hashes. I independently checked all stored example matrices using a separate standard-library `Fraction`-pair implementation, without importing the author checker or repository code.

The source was inspected as supplied local TeX. Its bytes and SHA-256 agree with both `provenance.json` and the pinned local catalog. Lines 434–445 contain precisely the positive-block trace comparison attributed to them. The source paragraph uses equally sized diagonal blocks; the study's rectangular generalization is separately justified. This review does not independently authenticate the remote Git commit beyond the supplied pinned catalog and snapshot.

## Mathematical audit

1. **Norm and Gram conventions.** All claims use unnormalized Hilbert–Schmidt norms. With `A=X*X`, `B=X*Y`, `C=Y*Y`, and auxiliary same-size `P=XX*`, `Q=YY*`, rectangular trace cyclicity gives `a²=tr(P²)`, `c²=tr(Q²)`, and `β=tr(PQ)`. The latter is real and nonnegative because it equals `||B||HS²`; no commutativity is assumed.

2. **Exact sum and weighted gaps.** Expanding the Hermitian square gives `a²+c²−2β=||P−Q||HS²` and `s²a²+s⁻²c²−2β=||sP−s⁻¹Q||HS²`. The alternative proof is sound: for `S=Δ^(1/2)` and signature matrix `J`, `S(JΔJ)S=(SJS)²` is PSD, so its trace is `||SJS||HS²`.

3. **Product inequality and scale.** Congruence by `diag(s^(1/2)I_p,s^(−1/2)I_q)` leaves `B` unchanged. Minimizing at `s=√(c/a)` gives `β≤ac`. The proof separates `a=0` or `c=0` first and correctly proves `B=0` there; no inversion of singular diagonal blocks is used.

4. **Exact product deficit.** For `a,c>0`, expansion verifies `ac−β=(ac/2)||P/a−Q/c||HS²`. Thus nonzero product equality is equivalent to `Q=(c/a)P` in every Gram factorization, including redundant-row realizations. The normalized formula is not asserted when either denominator vanishes.

5. **Intrinsic equality conditions.** With the fixed value `t=c/a>0`, multiplying out `Δ diag(tI_p,−I_q) Δ` gives exactly `tA²−BB*`, `tAB−BC`, its adjoint, and `tB*B−C²`. Gram equality implies its vanishing. Conversely, tracing its top-left block gives `β=t a²=ac`; tracing the bottom-right block works as well. Hence the stated intrinsic conditions are genuinely equivalent under the PSD and fixed-`t` assumptions, rather than merely necessary.

6. **Complete normal form.** In a minimal Gram realization, `P+Q=(1+t)P` is positive definite. Therefore `H=P`, `U=X*P^(−1/2)`, and `V=t^(−1/2)Y*P^(−1/2)` are well-defined, `U*U=V*V=I_r`, and direct multiplication yields `A=UHU*`, `B=√t UHV*`, `C=tVHV*`. The converse factorization is PSD and has the claimed norms. This includes rectangular blocks and all nonzero rank-deficient cases. Minimality is used only to invert the auxiliary Gram matrix.

7. **Zero cases and sum equality.** Product equality always holds when either diagonal block vanishes. Sum equality in those cases holds only for the all-zero matrix. Otherwise sum equality is product equality together with `a=c`, by the decomposition `(a−c)²+2(ac−β)`. The equivalent conditions `P=Q`, `ΔJΔ=0`, and the three block identities are valid.

8. **Ranks, kernels, and strictness.** The normal form gives all four equality ranks equal to `r≤min(p,q)`. Therefore full positive definiteness excludes equality. Positive definite diagonal blocks of unequal dimensions also exclude product equality. The kernel inclusions and the weaker rank bound for arbitrary PSD blocks follow directly from the Gram factors. The equal-dimension positive-definite unitary formulation has the correct orientation.

9. **Constants and counterexamples.** Scalar rank-one equality proves the optimal constants `2`, `1/2`, and `1` in their respective formulations. Zero-padding preserves fixed-dimension PSD sharpness. The final positive-definite fixed-dimension family has eigenvalues `2−ε` and `ε` with multiplicity `p+q−1`, and the claimed norm limits, so strictness does not improve the constants. The non-PSD, entrywise-test, and unasserted Loewner-bound counterexamples have the stated values. PSD is correctly stated as sufficient rather than characterized by these norm inequalities.

10. **Compression corollary and dependencies.** Applying the result to `[E F]*K[E F]` is valid, with Gram factors `K^(1/2)E` and `K^(1/2)F`. All 10 theorem records match the proof content. Their dependency graph has 5 background nodes, unique identifiers, valid references, and no cycles. The portable-schema and non-formalization caveats are accurate.

## Exact computation and example arithmetic

- My independent verifier passed all **16 named examples and 180 seeded Gram fixtures**.
- It checks the stored matrix entries, Gram factorizations, squared norms, ranks, sum and squared-product gaps, weighted gap identities at three rational scales, both directions of intrinsic equality tests, kernel/rank support conditions, and signed quadratic-form certificates.
- A copied run of the author's final checker reproduced `exact-examples.json` and `checks.json` **byte-for-byte**. The author originals were not executed in place or overwritten.
- For E16, `WW*=I₂` and `Y=2XW` give `Q=4P`. Since `det(X)=2−i`, the block matrix has rank two. Its `A` has squared HS norm `4+25+2·5=39`, hence `(a²,c²,β)=(39,624,156)` and sum gap `351`, agreeing with the final files.
- All arithmetic used here is exact rational or Gaussian-rational arithmetic, with no downloaded implementation, package installation, numerical eigensolver, or floating-point test.

These checks validate finite fixtures and serialization; the universal assertions are accepted on the mathematical proofs above, not by extrapolating the tests.

## Corrections and residual limits

No mathematical corrections are required. The author files intentionally retain their original `independent_review: pending` metadata and are frozen; this separate hash-bound report supplies the completed review state. Those original fields alone should not be used as a current aggregate review verdict.

This acceptance does not certify a native MRS schema/import, novelty, publication readiness, Lean compilation, source-to-Lean theorem matching, or the complete Crouzeix headline result.

## Accepted artifact fingerprints

| File | SHA-256 |
|---|---|
| study.md | fec0fdca335159320f13c572e34f77fa0dad3578ec76de4da6e4ae437a9c60af |
| theorem-records.json | 8276d9642256c65907271f84d3b2082f970909fc3b624cb1639c860e2649c203 |
| provenance.json | 5cbad41417223c1b106556ef68a09ef3f3d314ed762377b2dc86355dd95f0f85 |
| check_exact_examples.py | 056023a525bd5c855961ac8870afa9b6d868d7f9acada6a97efadb28caebbfde |
| exact-examples.json | 5e7f79ee684eb8f8d55a3f641e63fdad9abc5c3a37142679db023a6c8031bc51 |
| checks.json | d7aedbac738fe5bfdc864dd5ce3b2b4662243dfc4e44b20d32614939723a7aa4 |
| record-validation.json | 1921f0b27a9432fc31329fbc2dfcc0eb14a9abbee5254259acb9dfd252400a0b |

Inspected TeX SHA-256: `164f56cc3f5ecbfb65ddba0d0438cacf44f325919ef7dfb742d073c948fddabd` (35,175 bytes).

Independent audit script: `parent-check-examples.py`, SHA-256 `14b49462b0a45d7e797b211e26f92641452d60ef50da2c476758eb10a6e3de1f`.
