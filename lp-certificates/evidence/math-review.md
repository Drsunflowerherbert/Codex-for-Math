# Independent ordinary mathematical review

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](../PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

Reviewer role: independently inspect the certificate mathematics and boundary
conditions. This is an **ordinary mathematical review**, not a claim of Lean
acceptance or an independent kernel implementation. The reviewer wrote the
explanatory notes, so the notes themselves still benefit from another reader's
review. The certificate forms were supplied by the implementation owner and
were reviewed separately from their implementation.

Scope at initial review, 2026-10-13 UTC: normalized free-variable LPs; optimality
by nonnegative inequality/free equality combinations and an attained bound;
infeasibility by a zero coefficient combination with negative RHS; unboundedness
by a feasible base and improving feasible direction. Arithmetic is rational,
but all mathematical conclusions are over real feasible points.

## Findings

The three supplied forms are mathematically sound with their explicit
hypotheses. Proofs are given in `../notes/mathematics.md`, §§2–5. None requires
primal strict feasibility, independent rows, a vertex, a simplex basis, or
strong duality. The coefficient identity is a full vector identity. Equality
multipliers have no sign restriction. Every variable bound must be an explicit
row. The strict signs in the infeasibility RHS and improving objective gain
are essential.

Important implementation gates communicated to the implementation owner:

1. `≥` normalization flips coefficients **and** RHS.
2. Both the optimal candidate and the unboundedness base must be checked for
   feasibility against every row.
3. Truncated vectors, missing coordinates, and silently skipped constraints
   are invalid inputs, not valid weaker statements.
4. A `0` infeasibility RHS or `0` ray gain is insufficient.
5. Negative normalized inequality multipliers are unsound, whereas negative
   equality multipliers are legitimate.
6. Certificate verification proves no certificate-finding completeness claim.
7. Direct exact checks and ordinary review are separate from the Lean gate.

## Independently computed examples

| Instance | Certificate arithmetic | Conclusion |
| --- | --- | --- |
| Maximize `3x+2y`; `x+y≤4`, `x≥0`, `y≥0`, `x-y=0` | Candidate `(2,2)`; inequality weights `(5/2,0,0)` on normalized rows; equality weight `1/2`; coefficient combination `(3,2)`; RHS `10` | Global maximum `10`. |
| Same rows, maximize `x+3y` | Candidate `(2,2)`; weights `(2,0,0)` and equality weight `-1`; coefficient combination `(1,3)`; RHS `8` | Global maximum `8`; negative equality multiplier works. |
| Minimize `y`; `x+y≥3`, `x-y=1`, `x≥0`, `y≥0` | Normalize objective to `(0,-1)`; weights `(1/2,0,0)`; equality weight `1/2`; coefficient `(0,-1)`; RHS `-1`; candidate `(2,1)` | Original minimum `1`. |
| `x≥1`, `x≤0` | Normalized rows `-x≤-1`, `x≤0`; weights `(1,1)`; coefficient `0`, RHS `-1` | Infeasible. |
| `x=0`, `x=1` | Equality weights `(1,-1)`; coefficient `0`, RHS `-1` | Equality-only infeasibility. |
| Maximize `x+2y`; `x≥0`, `x-y=0` | Base `(0,0)`; direction `(1,1)`; normalized row directional value `-1`; equality directional value `0`; gain `3` | Objective unbounded above. |
| Maximize `x`; `x≤1`, `2x≤2`, `x≥0` | Candidate `1`; weights `(1-2t,t,0)` for any rational `0≤t≤1/2`; coefficient and RHS both `1` | Redundant and degenerate active rows cause no difficulty; multipliers nonunique. |
| Maximize `x`; `x=1`, free `y` | Candidate `(1,0)`; equality multiplier `1`; coefficient `(1,0)`, RHS `1` | Bounded objective on a feasible affine line with no vertex. |

These calculations were checked by expanding the stated scalar/vector identities.
They do not depend on floating point, source inspection of an optimizer, or a
duality theorem. A later executable test report must identify its actual test
instances rather than treating this table as an executed suite.

## Counterexamples to omitted hypotheses

| Omitted condition | Exact counterexample |
| --- | --- |
| Nonnegative inequality multipliers | For `x≥0`, maximize `x`, candidate `0`: assigning multiplier `-1` to normalized `-x≤0` gives false upper bound `x≤0`. |
| Candidate feasibility | Maximize `x` under `x≤0`, `y≥1`. Candidate `(0,0)` and weight `1` on `x≤0` attain bound `0`, but the candidate is infeasible. |
| Full coefficient identity | Maximize `x` under `x+y≤1`. Candidate `(1,0)` evaluates like the combined row, but feasible `(t,1-t)` make the objective unbounded. |
| Strict contradiction RHS | Zero multipliers combine to coefficient `0` and RHS `0` even for a feasible system. |
| Positive ray objective gain | For constant objective `0` under `x≥0`, base `0` and direction `1` form a feasible ray but no objective improvement. |
| Feasible unboundedness base | Objective `x` and inconsistent equalities `y=0`, `y=1` admit direction `(1,0)` but have no feasible points. |

## Normalization and nonuniqueness

Positive scaling of a normalized inequality is compensated by reciprocal
multiplier scaling. Equality rows admit any nonzero scaling. Positive scaling
of an infeasibility certificate preserves its contradiction and can make RHS
`-1`; positive scaling of a direction can make objective gain `1`. The feasible
base is not scaled. For a fixed nonzero objective, scaling optimality
multipliers alone changes the required coefficient identity.

Normalized RHS `-1` still does not select unique infeasibility multipliers:
duplicate `x≤0`, `x≤0` plus `x≥1` admit `(t,1-t,1)` for every rational
`0≤t≤1`. Duplicate upper rows `x≤1`, `x≤1` likewise admit optimality
multipliers `(t,1-t)` with the same `L1` norm. A unique or best normalization
requires an additional specified criterion and possibly a tie-breaking rule;
it is not implied by certificate soundness.

## Sources, commands, and present limits

`../notes/sources.md` records primary-source URLs, inspected book sections and
printed pages, exact download commands, the retrieved PDF hash, and unsuccessful
original Farkas access. No full original Farkas proof was inspected. All new
explanatory proofs and hand examples are independently written.

Independent workspace-instruction check:

```
find ${WORKSPACE} -name AGENTS.md -o -path '*/.agents/skills/*/SKILL.md'
```

Observed exit `0`, empty output. Existing evidence-protocol documents were read
with `cat`; their fixed tangent plans are not general LP acceptance plans.

## Follow-up inspection of the Lean mathematical interface

At 01:52 UTC, the reviewer read `LPCertificates/Core.lean` and
`LPCertificates/Rational.lean` and compared the definitions and theorem
statements with the reviewed mathematical conditions. Their exact source
SHA-256 values at inspection were:

```
5c9755bfdc0b11dcd680a2bfd42da61c5a73f2107cb8bb564be83821af2fb59a  LPCertificates/Core.lean
be5b7bf5c286303fef192404ddb6d2e07f8c3c7a5b794548740382b0722f5f94  LPCertificates/Rational.lean
```

The command `sha256sum LPCertificates/Core.lean LPCertificates/Rational.lean`
exited `0`; the displayed hashes match its first two output lines. This identifies
the inspected snapshot, not a promise that later revisions are covered.

`OptimalCertificate`, `InfeasibleCertificate`, and `RayCertificate` include the
required hypotheses. `optimal_sound`, `infeasible_sound`, and
`unbounded_sound` give exactly the sufficient conclusions. `duality_gap` and
`complementary_slackness` express the reviewed finite-sum identity and equality
iff zero individual weighted slacks. The generic field/order hypotheses support
the division by positive ray gain; the direct bound construction does not need
an Archimedean hypothesis.

The rational `checkOptimal`, `checkInfeasible`, and `checkUnbounded` definitions
decide those propositions on typed normalized values. Their three
`*_sound_real` theorem statements conclude optimality, infeasibility, and
unboundedness for the cast **real** problem; optimality and unboundedness
quantify over real points/bounds, not just rational ones. Source inspection
found no mismatch with the mathematical specification. This is still not
compiler acceptance or a transitive axiom audit; those belong to separate fresh
Lean evidence.

The Python JSON parser and its `≥`/minimization normalization are not formally
extracted from these checks. There is no parser-to-Lean equivalence theorem.
Typed Lean acceptance therefore leaves a trusted translation/interface gap for
the external checker. This review has not independently audited the whole
Python implementation; another verifier reviewer owns that work.

## Standalone exact arithmetic check

The following command was executed from `lp-certificates/` at 01:52 UTC. It
uses Python's standard-library `Fraction` directly, does not import the
production verifier, and checks the eight hand examples above. Its two sampled
families are also proved algebraically in the notes; the finite sample by itself
does not prove all family members.

```sh
python3 - <<'PY'
from fractions import Fraction as Q

def dot(a, x):
    assert len(a) == len(x)
    return sum((Q(u) * Q(v) for u, v in zip(a, x)), Q(0))

def combine(A, b, E, f, w, v, n):
    assert len(A) == len(b) == len(w)
    assert len(E) == len(f) == len(v)
    q = tuple(sum((Q(t) * Q(a[j]) for t, a in zip(w, A)), Q(0))
              + sum((Q(t) * Q(e[j]) for t, e in zip(v, E)), Q(0))
              for j in range(n))
    return q, dot(w, b) + dot(v, f)

def feasible(A, b, E, f, x):
    return all(dot(a, x) <= Q(r) for a, r in zip(A, b)) and all(
        dot(e, x) == Q(r) for e, r in zip(E, f))

A, b, E, f = [(1,1),(-1,0),(0,-1)], [4,0,0], [(1,-1)], [0]
for c, w, v, value in [((3,2),(Q(5,2),0,0),(Q(1,2),),10),
                        ((1,3),(2,0,0),(-1,),8)]:
    q, B = combine(A,b,E,f,w,v,2)
    assert q == c and B == value == dot(c,(2,2))
    assert feasible(A,b,E,f,(2,2)) and all(Q(t)>=0 for t in w)
A, b, E, f = [(-1,-1),(-1,0),(0,-1)], [-3,0,0], [(1,-1)], [1]
q, B = combine(A,b,E,f,(Q(1,2),0,0),(Q(1,2),),2)
assert q == (0,-1) and B == -1 == dot(q,(2,1))
assert feasible(A,b,E,f,(2,1))
assert combine([(-1,),(1,)],[-1,0],[],[],(1,1),(),1) == ((Q(0),),Q(-1))
assert combine([],[],[(1,),(1,)],[0,1],(),(1,-1),1) == ((Q(0),),Q(-1))
A, b, E, f = [(-1,0)], [0], [(1,-1)], [0]
x0, d, c = (0,0), (1,1), (1,2)
assert feasible(A,b,E,f,x0) and all(dot(a,d)<=0 for a in A)
assert all(dot(e,d)==0 for e in E) and dot(c,d)==3
for t in [Q(0),Q(1,4),Q(1,2)]:
    q, B = combine([(1,),(2,),(-1,)],[1,2,0],[],[],(1-2*t,t,0),(),1)
    assert q == (1,) and B == 1
assert combine([],[],[(1,0)],[1],(),(1,),2) == ((Q(1),Q(0)),Q(1))
assert feasible([],[],[(1,0)],[1],(1,0))
for t in [Q(0),Q(1,3),Q(1)]:
    assert combine([(1,),(1,),(-1,)],[0,0,-1],[],[],(t,1-t,1),(),1) == ((Q(0),),Q(-1))
print('PASS: 8 hand examples; redundant optimality and normalized infeasibility families checked at 3 rational members each')
PY
```

Observed exit `0`, stdout:

```
PASS: 8 hand examples; redundant optimality and normalized infeasibility families checked at 3 rational members each
```

No claim of Lean compilation, transitive axiom audit, kernel replay, or
end-to-end parser-to-Lean correspondence is made by this arithmetic command.
Completeness, finding algorithms, rational certificate existence, strong
duality, integer/strict/nonlinear variants, and native Mac/installed MRS
integration remain explicitly outside this review's established claims.
