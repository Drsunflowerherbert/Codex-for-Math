> Historical source review: mathematical statements and verdicts are retained. Quoted hashes identify the original supplied files, which may differ from privacy-normalized public receipts. Original/public hashes are recorded in `publication/SOURCE-MAP.json`; fresh publication checks are separate.

# Actual Z integrals

`MixedMoments/Zeta.lean` defines `MixedMoments.Zeta.Z i j` as the real Lebesgue integral of `t^i s^j / (1-ts)` against the product of Lebesgue measures restricted to `(0,1)`. The open intervals omit only null endpoint sets. `Z_eq_iterated` proves agreement with the source convention `∫ t in 0..1, ∫ s in 0..1, ...`.

All indices are natural numbers. No integrability or series-to-integral identity is assumed. The module proves:

- `integrable_kernel`: absolute integrability of every actual monomial Z kernel, including the corner singularity.
- `Z_eq_series`: `Z(i,j) = ∑' u, 1 / ((i+u+1)(j+u+1))`.
- `Z_diagonal`: `Z(i,i) = zeta2 - harmonic2(i)`.
- `Z_offDiagonal`: for `i ≠ j`, `Z(i,j) = (harmonic(i)-harmonic(j))/(i-j)`.
- `Z_symm` and the exact sign check `Z_zero_one : Z 0 1 = 1`.
- `Z_eq_zRationalPart`: agreement with the canonical exact rational array in `Rational.lean`, with a `zeta2` contribution precisely on the diagonal.
- `Z_eq_formalZ`: realization of the canonical three-coordinate Z array for any real Catalan parameter.
- `integrable_columnKernel`, `polynomialColumn_eq_sum`, and `polynomialColumn_eq_formalZ`: actual rational-polynomial columns are integrable and agree with their finite coefficient expansions and canonical coordinates.
- `integrable_polynomialKernel` and `polynomialIntegral_eq_sum`: the same unconditional finite expansion for rational polynomials in both variables.

The proof of integrability expands the kernel geometrically at every point of the open square. Each monomial is integrable and its integral is the displayed numerical series term. The terms are nonnegative and bounded by `1/(u+1)^2`, whose summability follows from mathlib's p-series theorem. `ENNReal.ofReal_tsum_of_nonneg`, `lintegral_tsum`, and finite total norm integral justify the exchange and integrability. Thus pointwise convergence is accompanied by an absolute-integrability argument; no endpoint convergence assertion is required.

The off-diagonal evaluation telescopes a fixed finite tail of reciprocals. Each tail term tends to zero, so the residual boundary term vanishes. The diagonal formula shifts an already summable square reciprocal series. `zeta2` is this series-defined constant, not an assumed Basel evaluation.

Validation command: `bash scripts/with-lean.sh lake env lean MixedMoments/Zeta.lean`. The module uses no `sorry`, `admit`, new axioms, or `native_decide`.

`lake build MixedMoments.Zeta` also succeeds. Axiom audits of the principal integral, decomposition, and polynomial-expansion theorems report only Lean's standard `propext`, `Classical.choice`, and `Quot.sound`.

## The independent M(0,1) boundary

`MixedMoments/BoundaryZeta.lean` additionally proves the actual boundary identity
`MixedMoments.BoundaryZeta.M_zero_one : MixedMoments.Analysis.M 0 1 = (3/2 : ℝ) * MixedMoments.Zeta.zeta2` without any boundary-value assumption.

It evaluates the paired inner integral for `0<t<1`, identifies the logarithmic marginal, and applies `intervalIntegral.integral_comp_mul_deriv'''` to `t ↦ sqrt(1-t²)`. This map is continuous on the closed unit interval, is an involution there, and has the required derivative only on the open interval. Target integrability comes from `Constants.intervalIntegrable_zetaLogKernel`; transformed integrability comes from the independently proved `Analysis.intervalIntegrable_pairedSlice01`. Endpoint values are checked explicitly and do not affect either integral. `Constants.integral_zetaLogKernel` then evaluates the nonnegative odd square reciprocal series as `(3/4)*zeta2`.

Validation command: `bash scripts/with-lean.sh lake env lean MixedMoments/BoundaryZeta.lean` succeeds.

`lake build MixedMoments.BoundaryZeta` also succeeds. Axiom audits of `integral_inner`, `integral_pairedSlice01`, `M_zero_one_eq_logIntegral`, and `M_zero_one` report only `propext`, `Classical.choice`, and `Quot.sound`.
