# Independent computational review

Reviewed on 2026-10-13 UTC by the independent-verification agent. This reviewer
authored `tests/test_independent.py`, and did not author `verifier.py`, its fixture
files, or `tests/test_verifier.py`. The starting repository commit was
`b1d6c20e2f02b484d09c5285e67d842b369f9df0`.

## Result and scope

The final checker agrees with the independent raw-row arithmetic predicate on
all 15 well-formed published fixtures and all 72,900 documents in the bounded
exhaustive experiment below; the two malformed published fixtures are invalid.
Every semantic or schema failure case in this review is
rejected or invalid as appropriate. The combined Python suite passes: 53 tests,
exit code 0.

This establishes reproducible computational evidence for the reviewed Python
implementation. It is **not Lean acceptance**, a formal Python-to-Lean refinement
proof, a certificate-finding algorithm, or a proof of algorithmic completeness.
Lean compilation and theorem review are separate evidence obligations. The
experiment makes no claim about all rational inputs or performance on arbitrarily
large inputs.

## Independent calculation method

The test oracle uses `fractions.Fraction` directly on original JSON rows and the
original objective. It does not call the checker's parser, normalization,
dot-product function, or certificate helpers as an oracle. Its only checker
calls are to the public verification interfaces whose answers are compared.

For feasibility it evaluates each raw `<=`, `>=`, or `=` relation. For a supplied
combination it gives a `<=` row its supplied nonnegative weight, a `>=` row the
negative of its supplied nonnegative weight, and an equality row its unrestricted
weight. The arrays are traversed in the source order of their respective row
kinds. For optimality it compares the resulting raw combination with the original
objective for maximization or its negative for minimization, then checks the
attained bound. For infeasibility it checks a zero coefficient vector and a
strictly negative bound. For unboundedness it evaluates the raw homogeneous row
relations and checks an improvement of the original objective in the requested
direction. Variables have no implicit nonnegativity constraints.

For accepted witnesses, a second check evaluates actual feasible sample points
and original objective values. For rays it evaluates the proposed points
`base + t * direction` at `t = 0, 1/3, 1, 2, 100`, checking original rows and strict
objective improvement for positive `t`. These are bounded exact computations,
not numerical approximations or substitutes for soundness theorems.

## Bounded exhaustive experiment

Each raw one-dimensional row has coefficient `-1` or `1`, sense `<=`, `>=`, or
`=`, and right side `-1`, `0`, or `1`: 18 possible rows. Every ordered pair is
tested, including duplicate, redundant, incompatible and equality-containing
systems. For optimality both objective senses, coefficients `-1,0,1`, points
`-1,0,1`, and both row weights `-1,0,1` are tested. Negative inequality weights
must fail; negative equality weights remain permitted. Infeasibility tests all
row-weight pairs. Unboundedness tests both objective senses, objective
coefficients `-1,0,1`, base points `-1,0,1`, and directions `-1,0,1`.

| Form | Documents checked | Accepted by both calculations |
| --- | ---: | ---: |
| Optimal | 52,488 | 1,752 |
| Infeasible | 2,916 | 96 |
| Unbounded | 17,496 | 224 |
| Total | 72,900 | 2,072 |

For every accepted optimal witness the test checks all feasible points on the
rational grid `{k/2 : -4 <= k <= 4}` against its objective bound. For every
accepted infeasibility witness none of these grid points may be feasible. The
unbounded witnesses undergo the explicit ray checks described above. Agreement
and these extra sampled assertions passed with no discrepancy.

## Small fixtures recomputed

| Fixture | Original-data calculation |
| --- | --- |
| `optimal_mixed_redundant.json` | `1(1,1) + (3/4)(2,2) + (1/2)(1,-1) = (3,2)` and `4 + (3/4)8 = 10`; `(2,2)` is feasible and has value `10`. |
| `optimal_min_fraction_equality.json` | `3x=1` fixes `x=1/3`; objective `(3/2)x=1/2`. The unrestricted equality weight `-1/2` yields the lower-bound certificate after minimization orientation. |
| `infeasible_mixed.json` | The original requirements `x<=0` and `x>=1` combine to `0<=-1`. |
| `infeasible_equalities.json` | Twice `x+y=0` minus `2x+2y=1` gives zero coefficients and right side `-1`. |
| `infeasible_zero_variables.json` | The unique empty vector violates `0>=1`; its oriented row gives `0<=-1`. |
| `unbounded_min_lower_dimensional.json` | `(x,y)=(1+t,t)` satisfies `y>=0`, the redundant row `2y>=0`, and `x-y=1`; the original objective is `-2-t`. |
| `unbounded_max_no_rows.json` | No rows restrict the ray `x=2t`; its original objective is `t`. |
| `optimal_constant_no_rows.json` | The zero objective has value zero at every point, including `(7,-2/3)`. |
| `optimal_zero_variables.json` | The empty vector satisfies both zero rows and has value zero; the negative equality multiplier is harmless on a zero equality. |

The six published rejected fixtures and two invalid fixtures are independently
checked as well. The review additionally checks an interleaved sequence of
equalities and both inequality directions, a lower-dimensional segment with
zero objective, and a contradictory zero-dimensional equality.

## Scaling, degeneracy and failure coverage

Positive rational row rescaling is checked at `1/7`, `13/3`, and
`(10^40+1)/(10^30+3)`, while dividing the corresponding weight by the same factor.
This covers both optimization fixtures and both nonzero-dimensional infeasibility
fixtures, including negative equality weights. Positive ray rescaling preserves
the lower-dimensional minimizing ray; zero and negative scaling fail the
unboundedness requirements. The tiny exact value `1/(10^120+39)` still counts as
strict objective improvement and as a strict contradiction, while an optimal
coefficient mismatch of that same magnitude is rejected. No floating tolerance
is used.

The redundant optimal fixture admits at least three distinct valid inequality
weight arrays: `(5/2,0,0,0)`, `(0,5/4,0,0)`, and `(1,3/4,0,0)`, all with equality
weight `1/2`. This is an explicit example of nonunique certificates and does not
single out a unique optimal normalization.

Semantic failure tests cover a negative inequality weight even when the
coefficient and attained-bound identities hold, a wrong coefficient combination,
an unattained bound, an infeasible optimal point or ray base, a direction
violating an inequality or equality, a zero objective improvement, a zero ray,
and a nonstrict infeasibility contradiction. Empty row sets and zero variable
dimension are exercised separately.

Schema and CLI tests cover forbidden floats and booleans, malformed rational
strings, incorrect vector dimensions, missing or unknown fields, wrong field
types and senses, duplicate keys at root and nested positions, malformed JSON,
nonstandard `NaN`/`Infinity` constants, deeply nested JSON, and a missing input
file. CLI standard input is checked to return structured JSON with exit code
`0` for acceptance, `1` for rejection, and `2` for invalid input.

## Finding corrected during review

The initial checker raised an uncaught `RecursionError` when given
`'[' * 11000 + ']' * 11000`, instead of returning a structured invalid result.
This was a parser robustness issue, not a false acceptance. The reviewer sent
the exact reproduction to the checker author, who added `RecursionError` to
the JSON parsing exception handler. Both suites now have a deep-nesting
regression, and the CLI returns a structured invalid result with exit code `2` and
no traceback. No other implementation discrepancy was found in this review.

## Exact commands and final results

Commands ran from `/workspace/lp-research/lp-certificates` in the selected cloud
environment. This review used Python `3.12.14` and the standard library only.

```text
$ python3 --version
Python 3.12.14

$ git rev-parse HEAD
b1d6c20e2f02b484d09c5285e67d842b369f9df0

$ python3 -m unittest discover -s tests -p 'test_independent.py' -v
Ran 11 tests in 4.544s
OK
Independent exhaustive counts: {'optimal': 52488, 'infeasible': 2916, 'unbounded': 17496} accepted: {'optimal': 1752, 'infeasible': 96, 'unbounded': 224}
exit code: 0

$ python3 -m unittest discover -s tests -v
Ran 53 tests in 5.833s
OK
Independent exhaustive counts: {'optimal': 52488, 'infeasible': 2916, 'unbounded': 17496} accepted: {'optimal': 1752, 'infeasible': 96, 'unbounded': 224}
exit code: 0
```

The first independent run listed above preceded the addition of the tiny-rational
strictness test. The final combined run includes all 12 independent tests and
41 implementation-author tests.

Reviewed source snapshots:

```text
$ sha256sum verifier.py tests/test_verifier.py tests/test_independent.py
055c0ae11c1f1915ca26a15efc02976a46f4cbb651c75330e717f121dde16fb3  verifier.py
a2298c6aa68dd61bca9a15947026dcd0911d513735d24c0870ae2a746d54f0c2  tests/test_verifier.py
10eeef4b62462e5de2061569e1be9a2468fa5ada93056bb9bd63e3fe63874d40  tests/test_independent.py
```

No external service, Library operation, usage purchase, credential change,
commit, or push was performed by this reviewer. There is no computational
blocker in the reviewed scope. Remaining formal linkage and completeness
obligations must be stated separately by the research deliverable.
