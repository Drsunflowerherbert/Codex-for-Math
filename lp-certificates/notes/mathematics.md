# Rational linear-programming certificates

These notes prove the soundness of three small certificate forms. They do not
prove that a solver finds a certificate, that every relevant instance has one in
the accepted format, or that a failed verification classifies the problem.
The problem and certificate entries are rational; their mathematical conclusions
concern **all real feasible points**, not just rational points.

## 1. Keep the original variables

Let the original variables be a vector `x ∈ R^n`. Every variable is free unless
its bounds occur among the explicit rows. For example, `x_j ≥ 0` is a row, not
an implicit convention. The supported constraints are nonstrict inequalities
and equalities with rational coefficients. Strict inequalities and integer
restrictions are outside this model.

Normalize an original row as follows:

| Original row | Normalized row | Multiplier used below |
| --- | --- | --- |
| `a·x ≤ b` | `a·x ≤ b` | `λ ≥ 0` |
| `a·x ≥ b` | `(-a)·x ≤ -b` | `λ ≥ 0` on the flipped row |
| `e·x = f` | `e·x = f` | `μ ∈ Q`, either sign |

Both the coefficients and right-hand side of a `≥` row must be negated. On the
unflipped original rows, the corresponding signed coefficients would be `λ ≥ 0`
for `≤`, `-λ ≤ 0` for `≥`, and unrestricted `μ` for `=`. Keeping the normalized
nonnegative `λ` convention avoids mixing those sign rules in later arithmetic.

Write the normalized problem as

```
maximize c·x
subject to a_i·x ≤ b_i       (i = 1,...,m)
           e_k·x = f_k       (k = 1,...,p).
```

For minimization, replace the objective vector by `-c` and certify the resulting
maximization. A fixed additive objective constant affects the reported value but
does not change feasible points, optimizers, or an improving ray. Such a constant
is omitted from this toolkit's core model.

No transformation to positive and negative parts of `x` is needed. Nor do we add
slack or artificial decision variables. A **slack value** below means the
computed expression `b_i - a_i·x` at an existing point, not an additional variable.
The general affine LP model and the usual standard-form conversion appear in
[Boyd and Vandenberghe, §4.3, pp. 146–148](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=160).

## 2. The one reusable inequality

For rational multipliers `λ_i ≥ 0` and unrestricted rational `μ_k`, define

```
q = Σ_i λ_i a_i + Σ_k μ_k e_k,
B = Σ_i λ_i b_i + Σ_k μ_k f_k.
```

For every feasible real point `y`,

```
q·y = Σ_i λ_i (a_i·y) + Σ_k μ_k (e_k·y)
    ≤ Σ_i λ_i b_i       + Σ_k μ_k f_k
    = B.                                                    (1)
```

The inequality follows term by term: multiplication by a nonnegative number
preserves `a_i·y ≤ b_i`. Multiplication of `e_k·y = f_k` preserves an equality
for **every** sign of `μ_k`. Finite summation then preserves the bound. All
subsequent upper-bound and contradiction arguments are instances of (1).
This is the elementary certificate version of the weak-duality bound; see
[Boyd and Vandenberghe, §§5.1.3 and 5.2.2, pp. 216 and 225](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=230).

## 3. Optimality: an attained upper bound

An optimality certificate consists of a rational point `x*`, rational `λ ≥ 0`
and unrestricted rational `μ` satisfying all three checks:

1. `x*` satisfies every original constraint, equivalently every normalized row.
2. `Σ_i λ_i a_i + Σ_k μ_k e_k = c`, as an identity in every coordinate.
3. `Σ_i λ_i b_i + Σ_k μ_k f_k = c·x*`.

For any feasible real `y`, (1) and checks 2–3 give `c·y ≤ c·x*`. Since check 1
makes `x*` an attained feasible point, `x*` is a global maximizer. Nothing in
this proof assumes a vertex, an independent active set, a bounded feasible set,
a strictly feasible point, or unique multipliers.

It is insufficient to check the coefficient identity only after evaluation at
`x*`. For example, `x+y ≤ 1`, objective `x`, candidate `(1,0)`, multiplier `1`
gives the same value at that candidate but combines to `(1,1)`, not `(1,0)`.
Indeed, the feasible points `(t,1-t)` have arbitrarily large objective.

### Equality and complementary slackness

Assume feasibility of `y`, `λ ≥ 0`, and the coefficient identity `q=c`. Then

```
B - c·y = Σ_i λ_i (b_i - a_i·y).                           (2)
```

Equality-row terms cancel exactly, regardless of their multipliers' signs.
Every summand on the right of (2) is nonnegative. Consequently,

```
B = c·y
  iff λ_i (b_i - a_i·y) = 0 for every i
  iff λ_i > 0 implies a_i·y = b_i for every i.              (3)
```

For the forward implication, if one summand were positive then the finite sum
would be positive; thus each summand is zero. For the reverse implication, sum
the zero terms. The final equivalence uses `λ_i ≥ 0` and the nonnegative slack.
A strictly loose row has multiplier zero. A tight row **may** have multiplier
zero; the converse "tight implies positive multiplier" is false.

These equivalences concern a feasible point and a supplied coefficient
combination. They do not infer that multipliers exist from optimality. The
standard complementary-slackness discussion is
[Boyd and Vandenberghe, §5.5.2, pp. 242–243](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=256).

If one certificate is accepted, the same upper bound is tight at every other
optimal point, so (3) also holds at each such point. This follows directly from
the accepted bound; no additional duality theorem is required.

## 4. Infeasibility: a strict contradiction

An infeasibility certificate consists of rational `λ ≥ 0` and unrestricted
rational `μ` such that

```
Σ_i λ_i a_i + Σ_k μ_k e_k = 0,
Σ_i λ_i b_i + Σ_k μ_k f_k < 0.                            (4)
```

If a feasible real point existed, (1) would give `0 ≤ B < 0`, a contradiction.
The right-hand-side check is strictly negative. `B=0` provides no contradiction:
the all-zero multiplier vector exists for every instance.

This proves the implication **accepted certificate ⇒ infeasible**. The reverse
implication is a theorem of alternatives and is deliberately not part of this
proof. For primary background on alternatives, see
[Boyd and Vandenberghe, §5.8, pp. 259–263](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=273).
In particular, their stated Farkas alternative on p. 263 has a different
homogeneous strict-inequality form; one must justify a conversion before using
it as a completeness theorem for (4).

Equality-only inconsistencies are covered without splitting each equality into
two inequalities. For example, combine `x=0` with multiplier `1` and `x=1`
with multiplier `-1`: the result is `0=-1`.

## 5. Unboundedness: a feasible base and an improving direction

An unboundedness certificate consists of a rational feasible base `x0` and a
rational direction `d` satisfying

```
a_i·d ≤ 0 for every normalized inequality,
e_k·d = 0 for every equality,
γ = c·d > 0.                                             (5)
```

For every real `t ≥ 0`,

```
a_i·(x0+t d) = a_i·x0 + t(a_i·d) ≤ b_i,
e_k·(x0+t d) = f_k,
c·(x0+t d) = c·x0 + t γ.
```

Thus the ray stays feasible. Given any real proposed bound `M`, choose

```
t = max(0, (M - c·x0)/γ) + 1.
```

It is nonnegative and gives objective strictly greater than `M`. The feasible
objective values therefore have no real upper bound. For minimization, the
normalized objective is `-c`, so the original objective has no real lower bound.

A feasible base is essential: inconsistent equations `y=0` and `y=1`, objective
`x`, admit the formal direction `(1,0)` satisfying the homogeneous equalities
and improving the objective, but there is no feasible ray. A direction with
`c·d=0` likewise proves no objective unboundedness, even if the feasible set
extends indefinitely. Constraint directions and objective gain must both pass.

## 6. Small hand calculations

These are independent calculations, not an invocation of a certificate finder.
The executable examples and tests may use additional instances.

### A. Mixed directions, rational multipliers, and an equality

Maximize `3x+2y` subject to

```
x+y ≤ 4,
x ≥ 0,
y ≥ 0,
x-y = 0.
```

The candidate `(2,2)` is feasible and has value `10`. Put weight `5/2` on
`x+y ≤ 4`, zero on the normalized lower-bound rows, and weight `1/2` on
`x-y=0`. Directly,

```
(5/2)(x+y) + (1/2)(x-y) = 3x+2y ≤ (5/2)4 + (1/2)0 = 10.
```

To find these weights by hand, solve `λ+μ=3`, `λ-μ=2`, obtaining
`λ=5/2 ≥ 0`, `μ=1/2`. This is a useful guess-and-check procedure, not a
complete algorithm. The feasible set lies on the line `x=y`; no full-dimensional
interior or nondegenerate vertex is required.

For objective `x+3y` on the same rows, `λ=2`, `μ=-1` gives the upper bound
`8`, attained at `(2,2)`. The negative equality multiplier is necessary for
this two-row representation and is fully legitimate.

### B. Minimization without artificial variables

Minimize `y` subject to `x+y ≥ 3`, `x-y=1`, `x ≥ 0`, `y ≥ 0`.
The normalized objective is `(0,-1)`, and the first normalized row is
`-x-y ≤ -3`. Give it multiplier `1/2`, give the equality multiplier `1/2`,
and give the remaining inequalities multiplier zero. Then

```
(1/2)(-x-y) + (1/2)(x-y) = -y ≤ -3/2+1/2 = -1.
```

The feasible candidate `(2,1)` attains `-y=-1`. Therefore the original minimum
is `1`.

### C. Infeasibility in one line

The rows `x ≥ 1` and `x ≤ 0` normalize to `-x ≤ -1` and `x ≤ 0`.
Weights `(1,1)` produce `0 ≤ -1`. No objective or primal candidate is needed.
A single zero row `0 ≤ -1` is an equally valid contradiction certificate.

### D. An improving ray on a lower-dimensional feasible set

Maximize `x+2y` subject to `x ≥ 0` and `x-y=0`.
Choose `x0=(0,0)`, `d=(1,1)`. The normalized lower-bound row gives
`(-1,0)·d=-1 ≤ 0`, the equality gives `(1,-1)·d=0`, and objective gain is `3`.
Every `(t,t)` for `t ≥ 0` is feasible with objective `3t`.

### E. Redundant active rows and nonunique multipliers

Maximize `x` subject to `x ≤ 1`, `2x ≤ 2`, `x ≥ 0`.
At `x*=1`, both upper rows are tight and the lower row is loose. For every
rational `t ∈ [0,1/2]`,

```
λ = (1-2t, t, 0)
```

has nonnegative entries, combines the coefficients to `1`, and combines the
right-hand sides to `1`. Thus it certifies the same optimum. At `t=0`, the
second tight row has multiplier zero; at `t=1/2`, the first does. There are
more active rows than independent active normals. The certificate proof does
not divide by an active matrix or require it to be invertible.

### F. No vertex is needed

Maximize `x` subject only to `x=1`, with a second free variable `y`.
Every `(1,y)` is feasible and optimal; the feasible affine line has no extreme
point. An equality multiplier `1` on the row `(1,0)·(x,y)=1`, together with
candidate `(1,0)`, certifies value `1`. The feasible set is unbounded while
the objective is bounded and attained.

## 7. Scaling is representation, not a unique optimum principle

For a normalized inequality, replacing `(a_i,b_i)` by `(κ a_i,κ b_i)` with
rational `κ>0` preserves its feasible halfspace. Replace the corresponding
multiplier by `λ_i/κ` to preserve its contribution. Equality rows may instead
be scaled by any nonzero rational `κ`, with multiplier `μ_k/κ`. Negative
inequality scaling must reverse the inequality sign; zero scaling can erase
information and is not an equivalence.

Clearing each row's denominators by a positive common denominator is a valid
representation change. It can aid hand arithmetic, but its effect on multiplier
size depends on the chosen units. A certificate's denominators can also be
cleared in a written identity if the objective side is multiplied too.

An infeasibility certificate may be multiplied throughout by any positive
rational scalar. If its combined right-hand side is `B<0`, the choice
`-1/B>0` normalizes that right-hand side to `-1`. A direction certificate may
be scaled by any positive rational scalar; dividing by its gain `γ>0`
normalizes gain to `1`. Neither operation scales the feasible base.

For a fixed nonzero objective, one **cannot** arbitrarily multiply all optimality
multipliers by a scalar: the coefficient identity would become `q=κ c`, not
`q=c`. Scaling both objective and multipliers consistently describes a scaled
objective; positive scaling preserves the optimizing set but changes the value.

Even normalization to `B=-1` does not make infeasibility multipliers unique.
For `x ≤ 0`, a duplicate `x ≤ 0`, and `x ≥ 1`, the normalized coefficient rows
are `(1,1,-1)` and right-hand sides `(0,0,-1)`. Every

```
λ = (t, 1-t, 1),  0 ≤ t ≤ 1,
```

has coefficient sum zero and right-hand-side sum `-1`. Example E likewise
shows nonuniqueness among optimality certificates. Duplicate identical optimal
upper rows `x≤1`, `x≤1` allow every `(t,1-t)` with the same multiplier `L1`
norm `1`. Thus even minimizing that norm need not select a unique certificate.
Choosing sparse support, short integer coefficients, a preferred row order, or
a norm is an extra convention or optimization problem. There is no unique
"optimal normalization" implied by soundness or complementary slackness.

## 8. Boundaries and failure conditions

Zero rows, repeated rows, dependent equalities, empty row families, zero
objective vectors, and lower-dimensional feasible sets do not invalidate the
finite-sum proofs. With a zero objective, a feasible point and zero multipliers
give an optimality certificate; a strict positive-gain ray cannot exist. In zero
variables, feasibility is decided by constant rows and no improving ray exists.
Empty families use zero sums. None of these cases grants permission to skip
shape validation in an executable verifier.

The most consequential rejection checks are:

| Fault | Why rejection is necessary |
| --- | --- |
| A negative normalized inequality multiplier | `x≥0`, objective `x`, candidate `0`, multiplier `-1` on `-x≤0` would give a false upper bound. |
| Candidate feasibility omitted | For objective `x`, rows `x≤0`, `y≥1`, `(0,0)` attains the certified bound but is not a feasible optimizer. |
| Coefficients checked only at the candidate | Example following §3 has an unbounded objective despite apparent equality at `(1,0)`. |
| `≥` coefficients flipped but RHS retained | `x≥1` would become the weaker, inequivalent row `-x≤1`. |
| Infeasibility RHS permitted to be zero | Zero multipliers would "refute" every feasible system. |
| Ray gain permitted to be zero | An indefinitely feasible direction can leave the objective constant. |
| Feasible base omitted | The contradictory equalities in §5 still admit an improving homogeneous direction. |
| Truncated vectors or silently skipped rows | A coefficient identity or feasibility statement must cover every coordinate and every supplied row. |
| Rounded arithmetic or tolerance equality | A small nonzero rational residual is not an exact identity. |

The exact checker should reject malformed shapes and representations before
arithmetic, then evaluate the stated identities and order tests using rational
arithmetic. It should distinguish a malformed input from a well-formed but
invalid certificate. An approximate solver output must be reconstructed into
exact rational values and rechecked; closeness is not acceptance.

The Lean rational checks are `decide` computations on already typed normalized
`Problem ℚ n m k` values. Their soundness statements cast accepted rational
problem and certificate data into `ℝ` and quantify over all real feasible
points. The external Python JSON parser and its mixed-direction/minimization
normalization are independently written code. They are not formally extracted
from Lean, and no theorem identifies every parsed JSON object with a Lean
`Problem`. Trusting that interface is therefore a separate obligation; proving
the typed Lean checker sound does not by itself prove the external parser sound.

## 9. Explicit remaining obligations

The supplied forms prove soundness only. The following claims require additional
work and are not consequences of the present certificate checks:

- an algorithm always finds a certificate or correctly terminates;
- every infeasible rational LP has a rational certificate in form (4);
- every finite attained rational optimum has rational optimality multipliers;
- every unbounded instance has an accepted rational base and improving ray;
- proof of general LP strong duality or a theorem of alternatives;
- a formal end-to-end equivalence between an external parser/runtime and Lean
  definitions, unless separately established by an explicit theorem;
- integer, strict-inequality, nonlinear, or numerical-tolerance certificate forms.

No new axiom or admitted proof may stand in for those obligations. Executable
acceptance, hand calculation, source inspection, independent ordinary review,
and actual Lean kernel checking are separate evidence types. The published
evidence toolkit's fixed tangent plans cannot be relabeled as acceptance of an
LP theorem. Linux Lean evidence does not establish native Mac or installed MRS
integration.
