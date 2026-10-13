# Independent computational review

Reviewed on 2026-10-13 by a separate computational-review agent. This is an
ordinary mathematical and software review, with exact arithmetic tests; it is
not Lean verification or a machine-checked proof of the general theorems.

**Outcome:** no blocking defect found in the benchmark or the nine worked
example sections for their stated scope. The fixture experiment is useful
evidence for comparing these search choices. It does not establish general
solver completeness or performance.

## Scope and independent method

The reviewer read `benchmark/benchmark.py`, `benchmark/test_benchmark.py`,
`benchmark/README.md`, `benchmark/results.json`, `examples.md`, and the support
and search statements in `study.md`. No code from `lp-certificates/` was
imported, copied, or modified.

The reproducible companion [independent_check.py](independent_check.py) imports
the local benchmark's supplied fixtures and calls the implementation under
review. Its audit oracle does **not** use the implementation's `rref`,
`column_rank`, `independent_solution`, or `dot` functions. Instead, it finds
rank from exact determinant minors, solves an independent support with Cramer
rule on a nonzero square minor, then checks every equation, including any
remaining overdetermined rows. All arithmetic uses standard-library
`fractions.Fraction`.

This checker independently reproduces the recorded global ranks, attempted
subset counts, dependent-support rejections, inconsistent and negative
solutions, budget rejections, accepted-representation counts, first multiplier
vectors, and minimum positive inequality support observed. It also recomputes
all serialized original-coordinate equality identities. For both fixtures
with supplied `x0,N`, it checks equality satisfaction, full nullspace span,
projected rows and budgets, and the original feasible point where supplied.

The finite toy audit covers **all 5,040 inputs** with two or three rows in one
dimension, normal entries in `{-1,0,1}`, budgets in `{0,1}`, target coefficient
in `{-2,-1,0,1,2}`, and target budget in `{-1,0,1,2}`. The point zero is
feasible for every input. Across 10,080 exhaustive runs, both strategies agree
on certificate existence and minimum positive inequality support, and their
counts agree with the determinant oracle. This includes invalid target bounds,
zero rows, duplicates, zero objectives, empty supports, and dependent normals.
Thirteen additional searches check dimension zero, including the false
constant row `0<=-1`. Finite coverage of this family is not a theorem for
arbitrary dimensions, coefficients, or interfaces.

## Verification evidence

Run these commands from the repository root:

```sh
python3 -m unittest discover -s lp-sparse-discovery/benchmark -v
python3 lp-sparse-discovery/benchmark/benchmark.py > /tmp/lp-sparse-results.json
cmp lp-sparse-discovery/benchmark/results.json /tmp/lp-sparse-results.json
```

```sh
python3 lp-sparse-discovery/reviews/independent_check.py
```

The reviewer used Python 3.12.14. All 14 ordinary regression tests passed.
`cmp` succeeded, establishing byte-for-byte report reproduction. The
independent command completed with:

```json
{
  "fixture_runs_checked": 44,
  "original_identities_checked": 6,
  "affine_parametrizations_checked": 2,
  "finite_toy_inputs_checked": 5040,
  "toy_search_runs_checked": 10080,
  "additional_zero_dimensional_search_runs_checked": 13,
  "first_success_support_counterexample_runs_checked": 2,
  "independent_method": "determinant minors and Cramer rule; exact Fraction arithmetic"
}
```

Reviewed SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `benchmark/benchmark.py` | `375a36269dd53cd3b7350000c7de14bf95f29228aedef8f3fa8b2e6379b7b918` |
| `benchmark/results.json` | `c314baf34cb68412b97727e0dbfa75806cc9de3f2b71ba6bce7cc345c619b107` |
| `reviews/independent_check.py` | `3203514fdb12d1c6a8414e605650a77a0600b20f66630c8865dfb1c4f9d64937` |

## Exact example checks

The nine worked sections were checked directly in original coordinates.
Representative calculations that test the equality and normalization issues
are:

- Section 1: inequality weight `(1,0,0)` and equality weights `(1,-2,0)`
  combine to normal `(2,-1,3)` and RHS `10+1-2=9`. The displayed point
  `(7/2,5/2,3/2)` satisfies all three inequalities and equalities and attains 9.
- Section 2: both weights `1/3` combine the two normals to `(1,0)` and
  RHS `7/9+1/6=17/18`. The displayed point `(17/18,4/9)` is feasible and
  attains that value.
- Section 3: weights 4 and -8 give zero original normal and
  RHS `4(3/4)-8(1/2)=-1`. The pure-equality pair `(2,-1)` also gives zero
  normal and RHS -1.
- Section 4: the two-coordinate bound requires both unit weights. For the
  contradiction, normal cancellation forces all three weights equal, and RHS
  normalization makes each one. The stated witnesses certify every maximal
  proper subset feasible.
- Sections 6 and 7: the displayed multiplier families have their stated
  normal, RHS and L1 norm. The exact-RHS restriction gives `(2,1)` whereas
  the permitted stronger bound uses `(1,0)`.
- Section 8: `(0,1)` solves the free-zero counterexample; weight `1/D`
  solves the scaled single row. Weights `(1000,1000)` combine the two nearly
  dependent normals to `(0,1)` and RHS 1000, attained at `(0,1000)`.

The vertex-free line, the vacuous implication, and the zero-objective cases
also have the stated behavior. The editorial correction to say “combined
coefficient on x equal to 1” in section 7 was applied and checked, avoiding
reading “coefficient sum 1” as a sum of multipliers. The final first-success
counterexample added to `examples.md` section 7 and `study.md` section 5 was
also independently checked; its exact search behavior is reproduced by the
companion checker and explained below.

## Search interpretation and limits

The normal-independence pruning for the direct bound search relies on a
nonempty feasible set; every supplied bound fixture provides an exact witness.
The contradiction search correctly tests lifted-column independence instead:
nonzero contradiction normal columns are necessarily dependent. RREF only
solves independent selected columns and returns their unique solution or
inconsistency; it never treats one arbitrary free-zero assignment as a
nonexistence result.

The counters deliberately count attempted subsets and accepted
representations, not distinct certificates, runtime, or arithmetic bit cost.
The initial global-rank calculation and original equality reconstruction are
excluded from `rank_tests` and `independent_solves`, respectively, as documented.
Accepted supersets with zero coefficients explain repeated representations.

An additional exact counterexample clarifies first-success behavior. For
`x<=3, x<=1` and target `x<=2`, the direct search first accepts `(0,1)`,
with one inequality and RHS 1. The augmented columns, in input order, are
`(1,3),(1,1),(0,1)`. Its first successful pair is the first two columns,
giving weights `(1/2,1/2)` and two positive inequality weights. The one-row
certificate plus a vertical residual is enumerated later. Thus augmented
first success minimizes its enumerated generator cardinality and does not
necessarily minimize the number of positive original inequality weights.
The JSON's “minimum ... observed” wording correctly records this distinction.

The supplied benchmark is fixture-only and supplies its affine
parametrizations. It does not implement the general equality-elimination
pipeline, pure-equality contradiction discovery, LP status classification,
floating-point reconstruction, or resource-limited search. Assertions require
ordinary Python execution; use the documented commands without `-O`.
Exact arithmetic prevents tolerance-based mistakes in these checks, but it
does not limit coefficient growth or combinatorial work. General existence and
support claims remain ordinary mathematical arguments in `study.md`, reviewed
separately; finite test agreement does not formally verify them.
