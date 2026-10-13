# Exact worked examples and counterexamples

These are ordinary rational calculations. All variables are free reals; row
order determines the displayed multiplier order. The identities may be checked
with integer arithmetic after clearing denominators. They are not Lean proofs,
and no result here changes the old certificate finder or its scope.

## 1. Dependent equalities and a one-row optimum in three variables

Maximize `2x-y+3z` subject to

```
x+2y+z <= 10,  -z <= 0,  2x+4y+2z <= 20,
x-y = 1,  y-z = 1,  x-z = 2.
```

The third equality is redundant; the equality rank is 2. Choose

```
x0=(2,1,0), N=(1,1,1)^T,
(x,y,z)=(2+t,1+t,t).
```

The projected inequalities are `4t<=6, -t<=0, 8t<=12`, and the objective
is `3+4t`. Thus d=k=1 although the original problem has three variables.
The optimum occurs at `t=3/2`, giving `(7/2,5/2,3/2)` and value 9.

Inequality weights `(1,0,0)` match projected objective 4. Recover equality
weights `(1,-2,0)`. Their full original-coordinate identity is

```
(x+2y+z) + (x-y) - 2(y-z) = 2x-y+3z,
10+1-2 = 9.
```

The candidate is feasible, so this bound is attained. Alternative inequality
weights `(0,0,1/2)` with the same equality weights give the same bound; support
size 1 does not imply uniqueness. The zero weight on the last dependent
equality is a choice of equality row basis, not a restriction on its sign.

## 2. Nonintegral input and multipliers

Maximize x subject to

```
2x+y <= 7/3,  x-y = 1/2.
```

Use `x0=(1/2,0)`, `N=(1,1)^T`. The reduced row is `3t<=4/3`, and the
objective is `1/2+t`. The projected multiplier is 1/3, and the recovered
equality multiplier is also 1/3:

```
(1/3)(2x+y) + (1/3)(x-y) = x,
(1/3)(7/3) + (1/3)(1/2) = 7/9+1/6 = 17/18.
```

The point `(17/18,4/9)` has `x-y=1/2`, `2x+y=7/3`, and attains that
bound. Rational nullspace elimination and the independent one-column solve
find these weights directly; a fixed grid of small integer weights would not.

## 3. A zero projected normal can be the whole contradiction

Consider `x-y=1/2` and `2x-2y<=3/4`. With the preceding x0,N, the
inequality becomes `0*t<=-1/4`, so k=0. Weight 4 normalizes its reduced
RHS to -1. Recover equality weight -8:

```
4(2x-2y) - 8(x-y) = 0,
4(3/4) - 8(1/2) = -1.
```

This is an infeasibility certificate with one inequality, attaining the k+1
bound. Dividing a row by the norm of its projected normal is undefined here;
dropping every zero projected row would lose the contradiction.

Pure inconsistent equalities are different: `x=0, 2x=1` with weights `(2,-1)`
already give `0=-1` and use no inequalities.

## 4. Sharp support in two dimensions

For `u<=1, v<=1`, maximizing `u+v` requires weights `(1,1)`; each objective
coordinate forces its own weight. The feasible point `(1,1)` attains value 2.
Here k=2 and inequality support 2 is necessary.

For `u<=0, v<=0, -u-v<=-1`, unit weights yield `0<=-1`. Normal matching
forces all three weights equal, and normalized RHS -1 forces each to be 1.
No one- or two-row contradiction exists: the proper subsets are feasible at
`(0,0)`, `(1,0)` or `(0,1)` as appropriate. Here k=2 and support 3 is
necessary. Lifted columns `(1,0,0),(0,1,0),(-1,-1,-1)` are independent,
although their projected normals are dependent. Requiring independent
projected normals for contradiction search would reject every nonzero witness.

## 5. Feasible optimum without a vertex

Maximize x in variables (x,y) subject only to `x=1`. The feasible affine line
has no extreme point: `(1,y)` is the midpoint of `(1,y-1)` and `(1,y+1)`.
The candidate `(1,0)` and equality weight 1 certify value 1 with zero
inequality weights. Equality elimination gives `q=0`; vertex enumeration is
unnecessary. An unbounded feasible set does not imply an unbounded objective.

For a different degeneracy, `x<=0, -x<=0` defines a point but certifying x<=0
needs one inequality. The support rank is not automatically the dimension of
the affine hull unless implied equalities are separately derived and accounted
for in the original-row certificate.

## 6. Normalized contradiction weights need not be unique

For `x<=0, x<=0, -x<=-1`, every

```
lambda=(t,1-t,1),  0<=t<=1,
```

has normal sum zero and RHS -1. At either endpoint it has support 2; in the
interior support 3. Its multiplier L1 norm is always 2. Thus RHS normalization,
minimum support, or minimum L1 norm need not give a unique certificate.

For objective x and rows `x<=1, 2x<=2`, all weights

```
lambda=(1-2t,t),  0<=t<=1/2
```

certify the optimum 1. The L1 norm is `1-t`, so it prefers the scaled second
row. Dividing that row by 2 makes the rows duplicates and all weights summing
to 1 have the same L1 norm. The mathematical halfspaces and optimum are
unchanged, but the norm-based choice changes with units. Minimum support is
still 1, with two choices.

## 7. Exact-RHS normalization can add an unnecessary row

For `x<=0, -x<=1`, every feasible x obeys the loose bound `x<=1`.
If a discovery rule insists on combined coefficient on x equal to 1 **and RHS
exactly 1**, it
must solve

```
lambda1-lambda2=1, lambda2=1,
```

giving weights `(2,1)` and support 2 although k=1. The direct bound test
accepts `(1,0)` with stronger RHS 0 and support 1. In a lifted conic model
the stronger certificate can instead use weight 1 on the vertical residual
generator `(0,1)`; that generator is not an original inequality.

Even stopping at the first augmented success can favor more original rows.
With rows `x<=3, x<=1` and target `x<=2`, the singleton lifted columns do
not match `(1,2)`. Append the vertical column last. In index order the pair
of original columns is tested before
either original column paired with the vertical residual. It yields weights
`(1/2,1/2)`, combined RHS 2, and two positive inequality weights. The later
second-row-plus-residual support gives weights `(0,1)` and residual 1, with
only one positive inequality weight. Direct normal search finds the stronger
one-row bound. Minimum total lifted-generator support and minimum original-row
support are different search objectives.

## 8. Arbitrary free-zero solves and coefficient grids miss witnesses

With normal columns -1 and 1, matching target 1 means
`-lambda1+lambda2=1`. Row reduction that sets the free lambda2 coordinate
zero returns `(-1,0)`, which fails nonnegativity. Nonnegative `(0,1)` exists.
The independent singleton containing the second column finds it. The failure
of one particular underdetermined solve is not nonexistence of a certificate.

For any positive integer D, maximizing x under `D x<=1` has the unique
inequality weight 1/D and optimum 1/D. A bounded denominator grid misses it
when D is too large. For `x+(1/1000)y<=1, -x<=0`, maximizing y has weights
`(1000,1000)`, giving bound 1000, attained at `(0,1000)`. The two normals are
independent with determinant 1/1000. The support is small while coefficient
size and numerical conditioning can be poor; treating that determinant as
zero would change the exact problem.

## 9. Vacuous implication and zero objective

The system `x<=0, -x<=-1` in variables (x,y) is empty. It logically implies
`y<=0`, but no combination of these normals matches `(0,1)`. It does have
an infeasibility certificate: weights `(1,1)` give RHS -1. The nonempty
assumption in the upper-bound existence and rank-reduction statements cannot
be removed by appealing to vacuous truth.

On any nonempty feasible set a zero objective is bounded by every nonnegative
delta using all-zero multipliers, and every feasible point attains objective
0. It is not bounded above by a negative delta. On the empty set that last
logical statement is vacuous; infeasibility must again be handled separately.
