# Exact computation evidence and trust scope

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](../PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

The finite arithmetic supports the stated three-atom construction under
`0 < b < a` and `a + b < 1`. It separates its shrinking-mass ceiling
`p/[2(p+1)]` from the fixed-mass ceiling `1/2`. This document reviews the
computation component; it makes no Lean acceptance or global upper-bound claim.

## Prior records inspected

The computation worker read the following existing files before writing the
new verifier:

- `research/supplement/transport-stability/proof.md`;
- `research/supplement/transport-stability/check_exact_cases.py`;
- `research/supplement/reviews/transport/audit-report.md`;
- `research/supplement/reviews/transport/optional-refinements.md`;
- `research/supplement/reviews/transport/review-record.json`.

The checkout's branch was `codex/transport-sharpness-2026-10-13`, and
`git rev-parse HEAD` returned the required research baseline
`b1d6c20e2f02b484d09c5285e67d842b369f9df0` during development. Original records
were read but not edited. The new script prominently identifies its changes
from the old exact checker. The repository's stored upstream
`publication/upstream/OpenAI-math-LICENSE.txt` was inspected; it is Apache-2.0.
No dependency, downloaded source code, external service, Library operation,
credential operation, commit, or push was used by this computation worker.

## What the program actually computes

`scripts/check_exact.py` accepts any rational pair satisfying the strict
parameter restrictions. The default run executes 13 named pairs and all
100 admissible ordered pairs in the rational grid
`{n/d : 2 <= d <= 8, 1 <= n < d}` after deduplication. Passing a new rational
pair executes the same checks; these finite runs do not quantify over every
rational or real parameter.

The affine data are the actual slopes and intercepts of

```
u(x,t) = max(-x, a, x),
v(x,t) = max(-x, a + b t, x).
```

Every cell uses **all** pairwise affine comparisons, mechanically derived
by subtracting these coefficients. This includes each outer-versus-outer
comparison, removing the prior checker's reliance on a handwritten reduction.
The program clips `[-1,1]^2` by those rational half-planes, verifies that each
computed polygon vertex satisfies every comparison, and computes exact
shoelace areas. Multiplication by the explicit density `1/4` gives the nine
common-source masses. Closed cells share only distinct-slope tie lines; their
zero area is an ordinary geometric justification, while the executable check
also verifies the total joint mass is one.

The density is identically `1/4` on the fixed square and zero outside it. Thus
the lower and upper density bounds on the square are both `1/4`, independent
of `a,b`; globally the density is bounded above by `1/4`. No positive density
lower bound on all of Euclidean space is asserted. The executed dimension is
two; additional coordinates require the written normalized-product argument.

The row and column sums are computed from the polygons before they are
compared with `[(1-a)/2, a, (1-a)/2]`. Nonnegativity, probability normalization,
cube membership of all target atoms, and squared within-target separation
at least one are checked. The computed joint matrix is then compared with

```
[ m-b/8   b/8       0     ]
[ b/8     a-b/4     b/8   ],     m = (1-a)/2,
[ 0       b/8       m-b/8 ].
```

Multiplying the computed joint matrix by the independently constructed
Euclidean squared-cost matrix gives `D^2 = b/2 + a b^2` exactly. The script
does not replace this common-source cost with the target-to-target optimum.

## Finite transport certificates

For even integer `p >= 2`, the Euclidean cost matrix is rational:
`c_ij = (squared_distance_ij)^(p/2)`. The checker supplies the diagonal
matching matrix as a primal coupling, and the dual vectors

```
row_dual = [0, 0, 0],
column_dual = [0, b^p, 0].
```

It checks every inequality `row_dual_i + column_dual_j <= c_ij`, both
marginals of the primal, equality of primal and dual objectives `a b^p`,
and complementary slackness. This is a finite exact LP certificate requiring
no numerical optimization. The zero-slack support is checked to be exactly
the diagonal; positive off-diagonal slack forces uniqueness in the usual
finite weak-duality argument. The program verifies the finite inequalities;
their implication for all competing real-mass couplings is ordinary LP
reasoning, not a proof-kernel theorem.

As a separate cross-check, all 126 candidate five-column bases of the
three-by-three transportation constraints are enumerated with rational
Gaussian elimination. Feasible solutions are deduplicated, and the minimum
and unique minimizing vertex agree with the primal/dual certificate.
Named fixtures execute `p=2,4,6,8`; grid fixtures execute `p=2,4,6`.
Vertex counts are reported per input. In particular, equal masses `a=1/3`
give six vertices, while `a=3/5,b=399/1000` gives seven, so no universal count
of ten is claimed.

For `p=1`, the script checks the rational coordinate-projection inequalities
through squared distances and the matching cost `a b`. It does **not** compute
the generally irrational full Euclidean cost matrix or call this a rational
W1 LP solve. For arbitrary real `p >= 1`, the identity `Wp^p=a b^p` continues
to rest on the written coordinate-projection proof. No real-p executable
optimization is claimed.

## Exact counterexample regressions

For rational `p >= 1` and rational `alpha > 0`, choose a positive integer `L`
clearing the denominators of `2 alpha/p` and `2 alpha`. If the written real-p
identity is used, the ratio `R = D/Wp^alpha` satisfies

```
R^(2L) = (b/2 + a b^2)^L / [a^(2L alpha/p) b^(2L alpha)].
```

Every power on the right is a nonnegative integer, so the script checks it
with `Fraction` only. In particular, `R > C` is checked as
`numerator > denominator * C^(2L)` with no floating-point roots. This is an
exact rational consequence of the written distance identities, not an
independent proof of irrational Euclidean transport costs for rational `p`.

The shrinking-mass witnesses use `a=2^(-k), b=a/2`. The integer-powered lower
bound from `D^2 >= a/4` grows with exponent
`2L alpha/p + 2L alpha - L`, positive exactly above `p/[2(p+1)]`.
The fixed-mass witnesses use `a=1/4, b=2^(-k)`, and the corresponding growth
exponent is `2L alpha - L`, positive exactly above `1/2`. The script rejects
endpoint or subcritical inputs to its counterexample-witness API.

The default exponent data cover `p=1,3/2,2,3,4,7/2`, candidate constants
`C=1,2,10,100`, and both mass families, for 48 certified finite violations.
They also preserve powered ratios below, at, and above each ceiling at four
dyadic scales, for 36 scaling records. Each violating witness reruns the
affine-cell geometry at its actual parameters. Shrinking-family violations
use `alpha=1/2`; fixed-family violations use `alpha=3/5`. The API accepts
arbitrary rational exponents strictly above the relevant ceiling.

The ordinary proof is still needed to infer unbounded ratios from the
negative exponent, rather than from a finite list of violations. Endpoint
regressions do not establish a positive stability bound. The fixed-mass
records do not establish the stronger shrinking-mass obstruction.

## Negative and independent-method tests

Seven inadmissible inputs are rejected, including nonpositive tilt, negative
central mass, equality boundaries of the strict parameter regime, and clipped
widths. Two genuinely clipped examples are also computed using the raw affine
geometry: `a=1/4,b=1/2` has central mass `9/32`, and `a=3/4,b=1/2` has central
mass `23/32`, disagreeing with the advertised unclipped mass `a`. Rejection
of an equality boundary only restricts the claimed regime; it does not assert
that all displayed formulas fail at that boundary.

The 16 unit tests include an independent exact slice calculation of
`clamp(a+b t,0,1)`: rational breakpoints are inserted where the width hits
zero or one, then exact trapezoid integration is used. This agrees with the
polygon implementation for 25 additional signed-tilt/zero-tilt examples.
Tests also cover degenerate clipping boundaries, all affine comparisons,
original exact values, the six-vertex equal-mass case, deliberately incorrect
coupling marginals, negative mass, infeasible and suboptimal dual vectors,
unsupported odd-p rational cost execution, rational exponent denominator
clearing, and endpoint/subcritical counterexample rejection. Checks remain
active under `python3 -O` because `require` raises explicitly rather than
using optimization-removable assertions.

## Commands and observed results

Working directory: `${PROJECT_REPOSITORY}`. Interpreter:
`Python 3.12.14`. No packages were installed.

```
python3 transport-sharpness/scripts/check_exact.py
python3 transport-sharpness/scripts/check_exact.py --verify
python3 -O -m unittest discover -s transport-sharpness/tests -v
python3 transport-sharpness/scripts/check_exact.py --case 3/5 399/1000
python3 -B ${TEMP_ARTIFACT}/scripts/check_exact.py --output-dir ${TEMP_ARTIFACT}/data
python3 -B -O -m unittest discover -s ${TEMP_ARTIFACT}/tests -v
```

The complete generator and byte-identical verification returned exit zero
with 13 named fixtures, 100 grid cases, seven rejected inputs, and 48 exact
constant violations. The optimized-mode unittest command returned exit zero,
`Ran 16 tests` and `OK`. The single near-boundary case returned
`W2^2=477603/5000000`, `D^2=1475103/5000000`, masses `[1/5,3/5,1/5]`, and
seven enumerated vertices.

An additional rerun used byte-identical copies of the script and tests under
`${TEMP_ARTIFACT}/`, outside the checkout. It passed the
same 16 tests and regenerated all three mathematical JSON payloads with the
same SHA-256 hashes. The copy's outputs are preserved in
`data/isolated-rerun-stdout.txt` and `data/isolated-tests-stdout.txt`.

The initial default serialization attempt used unnecessarily large powered
fractions and exceeded Python's default 4,300-digit integer-string limit.
The default fixture exponents were simplified as described above, and the
complete final rerun passed. No floating approximation or interpreter-limit
change was introduced.

Inspect `data/verification-stdout.txt`, `data/tests-stdout.txt`, and
`data/source-hashes.json` for preserved output and byte-level provenance.
The three deterministic mathematical JSON payloads are
`data/exact-cases.json`, `data/regression-grid.json`, and
`data/exponent-regressions.json`.

This computation was authored and rerun by the delegated computation worker,
independently of the ordinary-proof and Lean workers. It is not a second-agent
review of its own implementation; another agent's separate rerun or review
must be recorded separately. The trusted scope is Python exact arithmetic,
the inspected algorithm, and the ordinary mathematical interpretations above.
No native Mac MRS integration, theorem novelty, global upper exponent,
paper-wide validation, new axiom, or Lean acceptance is asserted here.
