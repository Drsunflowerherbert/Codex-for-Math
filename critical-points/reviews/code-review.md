# Independent implementation review

Reviewed on 15 October 2026 by the code-review agent, separately from the
implementation author and the regression-test author. This is an ordinary code
and computational review, not a formal verification or an external certification.

## Reviewed implementation

- File: [`../classifier.py`](../classifier.py)
- SHA-256: `a068f0b615cde9f24f2be1b986e52bddae238f29ba12c7d876d85a8cd1eb1b05`
- Result: **no correctness defect found in the reviewed implementation**.

The final rerun also checked these exact supporting files:

| File | SHA-256 |
| --- | --- |
| [`../test_classifier.py`](../test_classifier.py) | `a3499bf24379c12879dbcfc8d8049fbc4683522d7a97c27d0e27d45815f5d85a` |
| [`../independent_check.py`](../independent_check.py) | `ec986c8b493fe962b0fd050b65c0a0872629150e30e44b309ae35edce31b37ff` |
| [`../examples.json`](../examples.json) | `a42b30963b1737c4a5651887bdd78a4ebd4f463d326feb345216c59d56b9a832` |

The finite stopping theorems are mathematical dependencies of the implementation;
their literature hypotheses are reviewed separately. This review checked that
the program uses the stated bounds and interprets a truncated calculation
correctly. It does not replace the ordinary proof of those bounds.

## Static checks

1. All accepted arithmetic uses Python integers and `fractions.Fraction`.
   Floating-point coefficients and Boolean coefficients are rejected. Exponents
   must be nonnegative integers, and Boolean exponents are rejected. Duplicate
   monomials are combined exactly before stationarity, rank, and degree checks.
2. The normalization tests the full rank-one condition `a*c == b*b` together with
   a nonzero Hessian. If `c` is nonzero, the rational shear cancels the mixed and
   kernel-square terms. If `c` vanishes, rank one forces `b=0` and `a!=0`, so the
   swap is valid. The reported matrix maps normalized coordinates to original
   coordinates. The constant is removed and the sign reversal is recorded.
3. At coefficient order `n`, the recurrence divides by the nonzero transverse
   second derivative. The newly computed coefficient enters the critical
   equation only in its linear transverse term. Truncation of multiplication
   and composition does not use or manufacture higher-order coefficients.
4. A nonzero residual coefficient is classified from its exact sign and parity;
   a negative transverse eigenvalue correctly exchanges minima and maxima.
   The zero-residual case is classified as an extremum which is not strict.
5. The conservative order is `(d-1)**2 + 1`. The optional sharper order subtracts
   `d//2` only for `d>=3`; quadratic inputs retain order two. These are orders
   for the residual, so the extra one compared with a Milnor-number bound is
   present. Early stopping at the first nonzero residual coefficient is valid.
6. If a budget expires before the required order with a zero jet, the result is
   `unresolved`, `residual_identically_zero` is `null`, and isolation is `null`.
   Identity is asserted only after the full order has been computed. If a
   nonzero term is found, the identity flag is `false`, the complex isolation
   flag is `true`, and the reported Milnor number is its order minus one.
7. `critical_series` returns exact jets of length `order+1`, including order
   zero. It does not assert that either analytic series terminates. The
   classifier's sparse output includes all nonzero coefficients through its
   reported computed order. No neighborhood radius is asserted.

## Independent computational checks

The reviewer used Python with SymPy 1.14.0, separately from the implementation's
series-composition helpers. An exploratory audit script was kept outside the
deliverable in `/tmp`, so it did not change the implementation or its tests.
Its method and cases were:

- For every one of the 22 machine-readable examples, independently substitute
  the reported matrix into the original polynomial with SymPy and verify the
  exact normalized polynomial, original Hessian, and transverse derivative.
- Independently solve the critical equation one coefficient at a time using
  symbolic polynomial substitution and coefficient extraction, and compare
  both the critical graph and residual jets through order 12 for all 22
  examples. No implementation composition helper was used in that comparison.
- Compare both bound choices with every example's expected classification,
  leading order, and leading coefficient. For each nonzero residual, test a
  budget immediately before and at its leading order. For each zero residual,
  test immediately before and at the full stopping order.
- Use the fixed random seed `881005` to generate 24 rational polynomials with a
  nonzero rank-one quadratic part, cubic and quartic terms, both transverse
  signs, nonzero constants, and invertible rational coordinate mixtures.
  Check the exact normalization identities and independent critical/residual
  jets through order eight.
- Check zero and small budgets, the quartic order-eight transition, and rejected
  noninteger or negative budgets, including Boolean inputs.

All checks passed. In particular, the two quartics
`(y-x^2)^2 + y^4` and `(y-x^2)^2 - y^4` first have residual coefficients at order
eight, with coefficients `1` and `-1` respectively. The order-seven budget
returns `unresolved` for both.

The reviewer also reran the deliverable's reproducible checks from the repository
root:

```bash
python -m unittest discover -s critical-points -p 'test_*.py' -v
python critical-points/independent_check.py
python critical-points/classifier.py critical-points/examples.json --example quartic_minus --max-order 7
```

The regression suite passed all 18 test methods, including their parameterized
subtests. The independent symbolic script passed its exact stress-case
coefficient and resultant identities through order 18, the hidden negative
quartic example, and the zero residual with a nonconstant positive unit.

The final catalog and regression rerun include
`(1+x)^2*(y^2+x^3)`: its gradient has a common global component at `x=-1`, while
the origin is locally isolated with residual `(1+x)^2*x^3`, leading order three,
and Milnor number two. Both bound choices and the independent symbolic jet
calculation agree on this case. This checks that the program's local-isolation
conclusion does not require the global derivative polynomials to be coprime.

## Limits of this review

Finite tests do not prove every execution correct. Python, the rational-arithmetic
runtime, the parser, and reviewer judgment remain in the trust boundary. The
implementation supports rational coefficients; it does not provide a general
exact representation of arbitrary real coefficients. Large degrees and large
coefficient sizes can exhaust time or memory. The classification and identity
conclusions concern analytic germs at the origin, not a certified radius,
global behavior, or smooth flat inputs.
