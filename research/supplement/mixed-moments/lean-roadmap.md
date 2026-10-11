# Future Lean formalization roadmap

## Status and scope

This is a proposed implementation plan for the extracted mixed-moment theorem. No Lean code has been compiled, no library theorem names have been verified, and no existing formal declaration has been matched to this result. All names below are proposed local names rather than claims about available APIs.

The target should be the polynomial cancellation theorem and its dependencies. Catalan irrationality, the manuscript's determinant, and valuation arguments should remain outside this module.

## 1 Separate the rational algebra from real analysis

Use two layers.

1. A rational algebra layer defines central binomial coefficients, moments, boundary recurrences, rational arrays, and a formal three-coordinate value type. It proves the recurrence and coefficient identities over \(\mathbb Q\).
2. A real analytic layer defines the actual integrals and constants, proves convergence and boundary values, and proves that the rational formal values evaluate to the integrals.

The final theorem then follows from the exact coefficient identity and vanishing of a finite Taylor jet. This separation avoids importing unjustified uniqueness or independence of the constants into otherwise elementary rational calculations.

Suggested namespace: `MixedMoments`. Suggested files: `Rational.lean`, `Integrability.lean`, `BoundaryValues.lean`, `Decomposition.lean`, and `TaylorCancellation.lean`. These are a proposed layout only.

## 2 Make partial indices explicit

Define `central : ℕ → ℚ` by the finite binomial formula. Do not use real-valued subscripts such as `(i-j)/2` in the actual implementation.

Define an integer-difference kernel conceptually as

- zero when the difference is negative;
- zero when it is odd;
- `central (difference / 2)` otherwise.

The actual choice between an integer-indexed kernel and a predicate-plus-natural-index definition should be made after checking the available parity APIs. Avoid truncated natural subtraction: `i - j` as a natural number would silently turn negative differences into zero and produce incorrect exceptional terms.

For `m_{-1}`, either use a separate extended moment on integers or isolate the boundary case so the main moment function stays natural-indexed. A separate `momentExt` with a proof of agreement on nonnegative indices is safer than allowing arbitrary negative indices without a domain invariant.

## 3 Rational definitions and finite proofs

The algebra layer should include the following proposed declarations:

- `central_succ_ratio`: the central binomial ratio.
- `moment_even` and `moment_odd`: rational closed formulas.
- `moment_recurrence`: with the index-one convention handled explicitly.
- `minusBoundary` and `plusBoundary`: well-founded or parity-split recursive arrays.
- `hStar`: parity-split rational normalization.
- `hStar_step` and both boundary closed-form theorems.
- `mRationalPart` and `zRationalPart`: the exact finite formulas.
- `formalM` and `formalZ`: a structure of three rational coordinates.
- `formalM_diagonal`, `formalZ_diagonal`, and the boundary recurrences.
- `polynomialDefect`: the finite convolution of coefficients with `central`.
- `formal_entry_zeta_coordinate`: equality of the formal coordinate with three halves times the defect.

Before any division, prove denominator nonzeroness in the intended field. In particular, the plus boundary recurrence starts at index two. For its closed form, the empty sum at index zero must not be replaced by an expression involving division by zero.

A structure `{ rational : ℚ, catalan : ℚ, zetaTwo : ℚ }` with componentwise addition and scaling is sufficient. There is no need to quotient by real relations among constants.

## 4 Integrability of the real kernels

Choose a consistent measure-theoretic representation, such as integrals over interval sets with Lebesgue measure, before proving Fubini statements. Specify a measurable extension at endpoints and at `(t,s)=(1,1)`; changes on null sets must not affect the result.

Define the weight on the open interval and use indicators or restricted measures to avoid claiming differentiability of the square root outside its natural domain. Main proof tasks:

- Measurability of the kernels and polynomial factors.
- The logarithmic bound for the integrated absolute kernel.
- Integrability near zero and near one, proved on separate intervals.
- `Integrable` for the two-variable kernel and bounded polynomial multiples.
- Fubini for the two integration orders.
- Summability of integrated absolute values of the signed geometric expansion for M.
- Tonelli for the nonnegative Z expansion.

It may be simpler to establish nonnegative majorant integrability first and derive the signed cases by domination. Do not rely only on pointwise geometric convergence.

The existing library may already have logarithm-times-power endpoint integrability. Verify actual declarations and their hypotheses during implementation; none are assumed by name in this plan.

## 5 The basic real moments

Prove the parity result by reflection. Evaluate the zero moment by a substitution. Obtain the even recurrence by integrating the derivative of \(t^{2r}\sqrt{1-t^2}\) on truncated intervals and passing to the endpoints with justified limits, or use a beta-integral library result if its exact hypotheses are available.

The first route follows the independent proof here and needs fewer special-function facts. Explicitly prove `moment_tendsto_zero` by dominated convergence before using it for telescoping tails.

Link the real moment to the cast of the rational moment by induction. Keep coercion lemmas localized rather than repeatedly unfolding factorial expressions in real-analysis proofs.

## 6 The two constants

Define Catalan as the absolutely convergent real series of odd reciprocal squares with alternating signs. Define zeta two as the positive reciprocal-square series.

For the Catalan start:

1. Split the t-integral at zero.
2. Integrate in s to get the log ratio.
3. Use the sine and half-angle substitutions on truncated intervals.
4. Reduce to the integral of `-log x / (1+x^2)` on `(0,1)`.
5. Prove absolute summability of the termwise integrals and exchange the series.

For the zeta start, prefer the shorter direct route:

1. Pair the positive and negative t-halves.
2. Integrate s explicitly.
3. Substitute `x = sqrt (1-u^2)`.
4. Expand `1/(1-x^2)` with nonnegative terms.
5. Use Tonelli and split zeta two into its even and odd terms.

The target is `M 0 1 = (3/2) * zetaTwo`. There is no need to formalize arcsine squared or the Basel evaluation for the cancellation theorem. The optional pi identity can be a later independent file.

## 7 Boundary recurrences and decomposition

Prove recurrences first for finite partial sums, with explicit tail terms. Then take limits using moment decay and the already established series identities. This follows the transparent finite telescoping calculations and avoids informal subtraction of divergent harmonic series.

Prove the minus and plus boundary decompositions by induction or parity-split induction. Check plus indices zero, one, and two explicitly: at index two, the coefficient of the zero-index boundary is zero, which is why the G term does not persist along the positive even plus boundary.

Use finite diagonal reduction to obtain `realM_eq_eval_formalM`. Obtain `realZ_eq_eval_formalZ` from the harmonic formulas. Define evaluation as a linear map from the three-coordinate rational structure to reals. Do not prove, request, or assume injectivity.

## 8 Express Taylor contact in two theorem interfaces

The easiest algebraic core should take a finite coefficient-vanishing hypothesis directly:

For every `j < L`, `polynomialDefect P D j = 0`.

Under that hypothesis, prove the cancellation result and the rational-polynomial-test-function corollary.

A second analytic-facing theorem should convert the user's big-O assumption into this finite jet condition. Two viable approaches are:

- formal power series plus an analytic identification of the series for inverse square root;
- an analytic Taylor expansion near zero with coefficients explicitly computed from the central binomial recurrence.

The proof only requires that the first L coefficients vanish. Avoid overbuilding a global analytic-function framework if a finite expansion with a controlled remainder suffices.

For a one-sided big-O formulation, choose the filter explicitly. Analyticity near zero makes the one-sided condition sufficient, but it should not be silently converted into a two-sided statement without a lemma.

## 9 Final theorem and output witnesses

A strong final interface should produce witnesses, not only membership:

There exist rational numbers `a b` such that

`M(P,j) - (3/2) * Z(D,j) = a + b * catalan`.

The witnesses are the exact finite sums `A_j` and `B_j` from Section 11 of `study.md`. A second theorem may restate this as membership in the rational span of one and Catalan.

For a polynomial Q in the second variable, expose the weaker paired-defect condition as an optional theorem. The degree-less-than-L corollary then follows from support and the contact hypothesis.

## 10 Regression cases and implementation checks

Use the exact examples in `certificates.json` as regression targets:

- `M(0,0) = 4G` and `M(0,1) = (3/2)ζ(2)`.
- `M(1,0) = 2`, `M(0,2) = 2`, and `M(2,0) = 1 + 2G`.
- `Z(0,1) = 1` and `Z(1,1) = ζ(2) - 1`.
- For P = 1, D = t, L = 3, the first three entries are `4G - 3/2`, `3/2`, `5/4`.
- The j = 3 entry is `3ζ(2)/4 - 1/8`; tests must not assert zero formal coordinate there.
- A negative difference passed to the central kernel yields zero, not `central 0`.
- Empty sums and zero polynomials behave correctly.

The Python certificates are finite exact arithmetic tests. Importing their output would not replace proof of the quantified Lean lemmas.

## 11 Completion criteria for a future formalization

A future implementation should count as complete only after:

1. All declarations compile in a recorded Lean and library revision.
2. The exact intended theorem statement is present with the rational-coefficient, contact, and index hypotheses.
3. No admitted results or unreviewed axioms have been introduced.
4. The analytic integrals are linked to the algebraic arrays, rather than only defining new arrays named after the integrals.
5. The theorem depends on no Catalan irrationality or independence assumption.
6. The final build log, declaration names, and dependency inspection are recorded.

None of these formal completion checks has been performed in this study.
