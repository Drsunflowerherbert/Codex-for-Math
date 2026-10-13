# Fixture benchmark for sparse certificate choices

This small experiment compares two transparent support enumerations on thirteen
built-in rational fixtures. It does not accept arbitrary LP input, classify
general LP status, find feasible points, or export certificates to another
component. No code is copied from or imported from `lp-certificates/`.
The mathematical support statements and their assumptions belong to the
surrounding study; finite fixture results are not proofs of those statements.

Run with Python 3.10 or later and its standard library only:

```sh
cd lp-sparse-discovery/benchmark
python3 benchmark.py > /tmp/lp-sparse-results.json
cmp /tmp/lp-sparse-results.json results.json
python3 -m unittest -v test_benchmark.py
```

`results.json` includes every fixture, exact rational weights, first-success and
full-enumeration counts, and the checked original-space equality weights where
applicable. Numbers are strings such as `18/11`, with no floating-point
approximation. The output contains no timestamps or timings and is reproducible
byte for byte under the same Python JSON formatting. These are ordinary Python
computations and tests, not Lean or other formal verification.

## The two choices

The reduced inequalities are `a_i dot z <= beta_i`. Bound fixtures supply
`c`, `delta`, and an exact feasible `z`, which is checked before enumeration.

- **Direct normal search:** enumerate independent subsets of normal columns
  `a_i`, up to their rank. Solve `sum lambda_i a_i = c` uniquely, require
  `lambda >= 0`, and test `sum lambda_i beta_i <= delta` directly.
- **Augmented target search:** enumerate independent subsets of columns
  `(a_i, beta_i)` together with one vertical column `(0, 1)`, up to the
  augmented rank. Solve the exact target equation `(c, delta)` with nonnegative
  coefficients. The vertical coefficient is the unused bound budget; it is not
  an added LP decision variable or a row slack for each constraint.

Contradiction fixtures only use augmented original-row columns, with target
`(0, -1)` and no vertical column. The target fixes the scale of an already
strictly negative combination. Their fixture labels describe the supplied
examples, rather than an LP classification service.

Both choices enumerate increasing support size followed by lexicographic input
indices. The empty subset is included. A full-column-rank test precedes every
solve; dependent subsets are skipped. RREF solves only systems with independent
columns, returning their unique solution or an inconsistency result. It never
chooses arbitrary zero values for free multiplier coordinates. `first_success`
stops at the first checked certificate; `exhaustive` visits the entire specified
finite family. Exhaustive counts include `sum_{j=0}^r binom(M,j)` attempted
subsets, including dependent ones, for `M` columns and rank `r`.

`subsets_attempted` counts candidates, including the empty support and dependent
supports. `independent_solves` excludes the dependent subsets but includes
inconsistent independent systems; it excludes the subsequent original-space
equality reconstruction. The rank-test count is one per attempted
subset; initial computation of the global rank is not in that counter.
`certificates_checked` counts accepted representations, including ones with zero
coefficients and repeated representations of the same certificate. Consequently
it is not a count of mathematically distinct certificates. Enumerated support
size and the positive inequality support can differ.

## Results worth inspecting

The table gives attempted subsets at first success and during full enumeration;
it measures search choices on these fixtures, not running speed or asymptotic
performance.

| Bound fixture | Direct first / full | Augmented first / full |
| --- | ---: | ---: |
| Sharp normal support, `k = 3` | 8 / 8 | 12 / 16 |
| Loose budget, `k = 2` | 4 / 4 | 8 / 8 |
| Duplicate and dependent normals | 5 / 16 | 5 / 42 |
| Cheaper redundant row | 3 / 7 | 3 / 15 |
| Rational equality reduction, `n = 3`, `k = 1` | 4 / 5 | 4 / 16 |
| Zero objective, positive budget | 1 / 3 | 4 / 7 |
| Zero objective, zero budget | 1 / 3 | 1 / 7 |
| Useful singleton last | 8 / 64 | 8 / 163 |
| Useful singleton first | 2 / 64 | 2 / 163 |

For the sharp contradiction with `k = 3`, all four row weights equal one and
the first success takes 16 subsets. The zero projected-row contradiction takes
2 subsets and one positive row. The rational contradiction takes 4 subsets and
has weights `(18/11, 20/11)`. The duplicate contradiction takes 6 subsets to
first success, of which 5 require independent solves; its full family has 7
subsets and 6 independent solves.

The expensive row in `cheaper-redundant-row` has normal `(1, 0)` and budget
`10`. The later row has normal `(2, 0)` and budget `2`. A target `(1, 0)` with
budget `1` needs the later row with weight `1/2`; retaining only the first
representative of a normal direction would lose this certificate.

The equality example supplies
`x0 = (1, 0, 2)`, `N = (-1, 1, 0)^T`, and equalities
`x1 + x2 = 1`, `x3 = 2`. The affine parametrization is checked to satisfy those
equalities and span their full nullspace. The bound uses the row
`x2 <= 2/3`, with weight one, and equality weights `(1, 1)` to recover
`x1 + 2*x2 + x3 <= 11/3` in the original three-dimensional space.
The implementation checks supplied `x0,N`; it does not implement a general
equality-elimination input pipeline or a retained-equality comparison.

## Limits and checks

The fixtures are deliberately small and selected, rather than a random or
representative workload. Exact rational rank and residual checks avoid floating
point tolerance choices, but rational bit sizes and combinatorial subset counts
can grow rapidly on larger inputs. No time, arithmetic-size, or memory budget
is imposed because the script only runs its fixed fixtures. Extending this code
to arbitrary data would require additional input, resource, and failure handling.

The tests check unique rational solves, rejection of dependent columns and
inconsistent systems, empty supports, known sharp weights, the budget-sensitive
redundant row, original equality identities, row-order effects, combinatorial
counts, rejection of false weights, and exact report reproduction. Independent
review is recorded separately by the study authors. Every bound fixture has a
checked feasible witness; no support claim for direct search is being inferred
from an infeasible input.
