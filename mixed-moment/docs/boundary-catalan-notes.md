> Historical source review: mathematical statements and verdicts are retained. Quoted hashes identify the original supplied files, which may differ from privacy-normalized public receipts. Original/public hashes are recorded in `publication/SOURCE-MAP.json`; fresh publication checks are separate.

# Actual Catalan boundary evaluation

`MixedMoments/BoundaryCatalan.lean` proves the unconditional theorem

```lean
MixedMoments.Analysis.M_zero_zero_eq_catalan :
  MixedMoments.Analysis.M 0 0 = 4 * MixedMoments.Constants.catalan
```

Here `Analysis.M` is the actual iterated Lebesgue integral defined in
`Integrals.lean`, and `Constants.catalan` is the usual convergent rational
reciprocal-square series defined in `Constants.lean`. The theorem does not
assume an integral evaluation, a boundary recurrence, irrationality, or
independence of constants.

The proof uses the previously proved equality
`Analysis.M_zero_zero_eq_logIntegral`, obtained by reflection and explicit
evaluation of the inner integrals. Its marginal is

```text
g(t) = (log(1+t) - log(1-t)) / sqrt(1-t²).
```

The rational substitution

```text
t = cayley(x) = (1-x²)/(1+x²)
```

is globally continuous and differentiable, reverses the endpoints `0,1`, and
carries the open unit interval into itself. On that interval the file proves

```text
sqrt(1-cayley(x)²) = 2x/(1+x²),
log(1+cayley(x)) - log(1-cayley(x)) = -2log(x),
cayley'(x) = -4x/(1+x²)².
```

Consequently `g(cayley(x)) * cayley'(x)` equals
`-4 * (-log(x)/(1+x²))`. The negative sign agrees with the reversed endpoints.

The substitution is applied with
`intervalIntegral.integral_comp_mul_deriv'''`, whose integrability requirements
are explicitly discharged. The original marginal is integrable because the
actual mixed-moment kernel is absolutely integrable. Its integrability on the
image follows from inclusion in the closed unit interval. The transformed
integrand is integrable by the independently proved logarithmic Catalan-kernel
integrability. Continuity is asserted only on the open image, where both log
arguments and the square root denominator are positive. Lean's total endpoint
values are checked separately and do not substitute an endpoint into an
unproved convergent expression.

The final evaluation uses
`Constants.integral_catalan_kernel_interval`, which proves
`∫₀¹ -log(x)/(1+x²) dx = Constants.catalan` by absolutely summable termwise
integration.

Validation command from the project directory:

```bash
bash scripts/with-lean.sh lake build MixedMoments.BoundaryCatalan
```

Environment: Lean `4.24.0`, mathlib revision
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. No admitted proof, custom axiom, or
`native_decide` is used in this module.
