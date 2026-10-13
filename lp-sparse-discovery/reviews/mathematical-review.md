# Independent ordinary mathematical review

Date: **2026-10-13 (UTC)**. Scope: `study.md`, `examples.md`, and the mathematical attribution and page references in `SOURCES.md`. This review was performed independently of the study's author. It is ordinary proof and arithmetic review, not Lean or other proof-assistant verification. The benchmark implementation and its recorded execution are reviewed separately.

**Conclusion:** no remaining mathematical blocker was found in the reviewed study and worked examples. The useful result is the distinction between normal-rank support for a valid bound on a nonempty feasible set and lifted-rank support for a contradiction. The assumptions and the scope of finite-search completeness are explicit.

## Reviewed claims

1. **Equality elimination and reconstruction.** The study first separates inconsistent equalities. After a consistent equality system is parametrized as `x=x0+Nz`, the projected certificate equations are equivalent to the original equations. In particular, `N^T(c-A^T lambda)=0` places the residual in `im E^T`, and the displayed identity

   ```
   b^T lambda+f^T mu = c^T x0+beta^T lambda
   ```

   correctly reconstructs the original constant. Dependent equality rows are allowed. The identity `rank(AN)=rank([A;E])-rank(E)` follows by restricting the span of the original row covectors to `ker E`; the kernel of this restriction is the row space of E. This is not the dimension of the feasible set's affine hull.

2. **Existence of a bound certificate.** The finitely generated lifted cone with the additional vertical generator is closed. The supplied closure proof is valid: dependence elimination gives independent support, finiteness gives a subsequence with fixed support, and the continuous inverse on the support's image gives convergent nonnegative coefficients. In the separation argument, a positive final separating coordinate produces a violating feasible point. A zero final coordinate produces an improving recession direction; the existing feasible base is essential in that case. Thus the study correctly proves the stated implication form under nonemptiness, rather than silently using vacuous validity on an empty set.

3. **The sharper bound support reduction.** For a dependence `Mh=0` on the positive support of an existing certificate, one can orient h to have nonnegative cost and a positive entry. If positive cost had no positive entry, `-h` would be a nonnegative dependence of negative cost, contradicting feasibility. Taking the minimum positive ratio preserves nonnegativity and normal matching, never increases the cost, and deletes at least one supported row. Repetition terminates with independent normal support, of size at most k. This proof does not assume strict feasibility, full dimension, a primal vertex, or uniqueness. It reduces an existing certificate; existence is established separately.

4. **Active-row restriction.** At a checked feasible optimizer, the nonnegative gap identity forces every supported row to be active. Dependence among active normals also preserves the constant exactly. The active-normal rank bound is therefore correct. This justifies pruning to active rows only for the stated candidate-optimality question; it does not justify pruning around an infeasible point.

5. **Contradiction support.** Normalizing a strictly negative combined constant to -1 is legitimate. Applying dependence elimination to `(a_i,beta_i)` preserves the nonzero target `(0,-1)` and yields independent lifted support of size at most `rho<=k+1`. When the reduced system is infeasible, its lifted span contains a nonzero vertical vector, so its dimension is exactly k+1. Independent projected normals cannot support a nonzero contradiction. The examples demonstrate that k+1 is genuinely necessary in general, including a zero-normal contradiction when k=0.

6. **Rationality.** With rational input, x0 and N can be chosen rational. The independent-support certificate weights solve a unique rational linear system and hence are rational, even when the initial existence argument supplied real weights. Equality recovery is another rational linear solve. The equality-only inconsistency statement now correctly qualifies rationality by rational input. No universal fixed coefficient or denominator grid follows from the support bounds.

7. **Finite exhaustive search.** Enumerating every independent normal support up to k, including the empty support, is complete for the specified valid-bound question when nonemptiness holds. Enumerating every independent lifted support up to rho is complete for the normalized contradiction question after consistent equality elimination. These are finite exact linear solves with the stated combinatorial bounds. The distinction between exhaustive failure and a search stopped by limits is correct. A truncated candidate list, floating-point rank test, or arbitrary free-zero solution of a dependent system would not inherit completeness. The old finder is not assigned any new completeness claim.

8. **Safe row pruning.** A projected zero row with negative budget is a contradiction and cannot be discarded. A zero row with nonnegative budget can be omitted for discovery because removing its weight does not change the normal sum and cannot worsen cost. For positive proportional dominance, if `a_i=t a_j` and `beta_i>=t beta_j`, replace weight `lambda_i` by adding `t lambda_i` to row j and delete row i's weight. This preserves the normal sum, does not increase cost or support size, and proves the stated pruning rule. Opposite rays and arbitrary dependent rows are not covered by this rule.

9. **First success and minimum positive support.** Under the stated nonemptiness and exhaustive-family assumptions, cardinality-first direct normal search returns minimum positive inequality support within the searched family. Any smaller certificate could first be sparsified to an independent support of no greater size and would already have been tested. A zero coefficient in the first successful support would similarly give a smaller accepted independent subset that was tested earlier. The bound check is `beta^T lambda<=eta`; no minimization of numerical cost, multiplier norm, or coefficient size is implied. Counting the vertical residual as an augmented generator changes the optimization criterion. With original rows `x<=3, x<=1`, target `x<=2`, residual appended last, and lexicographic support order, the two original lifted columns first succeed with weights `(1/2,1/2)`. The later second-row-plus-residual representation has one original inequality weight equal to 1 and residual 1. Both have total lifted-generator support 2, but their original inequality supports differ. This establishes the stated first-success counterexample for that ordering; reordering the generators can change which certificate appears first.

## Worked arithmetic and degeneracy checks

All nine worked-example sections were checked independently. The equality ranks, affine parametrizations, rational projected budgets, original-coordinate multiplier identities, feasible optimum candidates, and attained values agree. In particular:

- The three-variable example has equality rank 2, reduced normal rank 1, and optimum 9 at `(7/2,5/2,3/2)`.
- The nonintegral example has weights `1/3,1/3` and optimum `17/18`.
- The zero-projected-normal example has weights `4,-8` and combined constant -1.
- The sharp two-dimensional contradiction needs all three rows.
- The duplicate normalized contradiction has two distinct minimum-support endpoints and a constant multiplier L1 norm.
- The prescribed exact-RHS example needs two inequalities while the allowed stronger bound needs one.
- The added augmented first-success example has target `(1,2)`: the original-column pair gives `(1/2,1/2)`, while the stronger second-row certificate uses inequality weights `(0,1)` and vertical residual 1. Its order-dependent conclusion and the distinction between the two support objectives are correct.
- The free-zero failure, unbounded-denominator family, and small-determinant example correctly separate sparse support from arithmetic size and numerical rank decisions.
- The no-vertex, zero-objective, affine-dimension, and vacuous-implication examples correctly identify the necessary hypotheses.

## Reference check and evidence limits

The linked primary PDFs were independently opened and the cited mathematical statements and one-based PDF page references checked: Border's normalized alternative and rational Fredholm/Farkas statements; Bertsekas's nonzero-target conic theorem and proof, finite-value LP duality, and active-normal proof; and Boyd–Vandenberghe's equality parametrization with its independent-row qualification. No blocking attribution or page-number discrepancy was found.

Two small wording issues were identified during review and corrected before this conclusion: rational equality-only multipliers require rational input, and the denominator counterexample explicitly uses a positive integer D. The affine-dimension caveat was also checked in its final form.

This review establishes neither a proof-assistant theorem nor formal correctness of the experiment's Python implementation. It also does not claim a general LP solver, complete primal optimizer search, improving-ray discovery, or practical completion of arbitrarily large exact searches. No novelty claim is warranted or made.
