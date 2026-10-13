# Sparse discovery of linear-programming certificates

This is an ordinary mathematical study of finite, nonstrict linear constraints
over free real variables, with rational data for the proposed exact search. It
studies certificate discovery for a specified upper bound or for infeasibility;
it is not a general LP solver. The results below are consequences of classical
linear algebra, finite conic geometry and theorems of alternatives. No novelty
claim or Lean verification is made. References are linked at the claims they
support and collected in [SOURCES.md](SOURCES.md).

The useful distinction is this: **after eliminating equalities, a valid upper
bound on a nonempty feasible set needs at most the rank of the projected
inequality normals; a contradiction can need one more inequality.** These are
bounds on nonzero inequality multipliers, not on the number of active rows or
on the size of their numerators and denominators.

## 1. Model and exact elimination of equality multipliers

Let

```
P = {x in R^n : A x <= b, E x = f},
```

where A has m rows and E has p rows. Variable bounds, if any, must be explicit
rows. Normalize each `>=` row by negating both sides; equality rows retain free
signed multipliers. Negating an objective converts minimization to maximization.
Nothing here applies directly to strict inequalities or integer variables.

A bound certificate for `c^T x <= delta` is

```
lambda >= 0,
A^T lambda + E^T mu = c,
b^T lambda + f^T mu <= delta.                         (1)
```

An infeasibility certificate replaces c by zero and the last check by a
strictly negative combined right-hand side. Weighted addition proves soundness
immediately; equality multipliers mu have either sign.

First use Gaussian elimination to test `E x=f` (exactly for rational data).
If inconsistent, there is a mu with `E^T mu=0, f^T mu=-1`, using
**zero inequalities**, and mu is rational when the data are rational. Indeed,
an inconsistent augmented row reduction produces a row dependence h with
`h^T E=0, h^T f != 0`; scale h by `-1/(h^T f)`. This is the Fredholm alternative;
see [Border, Theorems 3–5, printed p. 3](https://kcborder.caltech.edu/Notes/Alternative.pdf#page=3).
Do not attempt a nullspace parametrization of an inconsistent affine system.

Henceforth assume the equality system consistent. Choose a particular solution
x0 and a matrix N whose columns form a basis of `ker E`. Put

```
d = n-rank(E),  x=x0+N z,  z in R^d,
B = A N,       beta = b-A x0,
q = N^T c,     eta = delta-c^T x0,
k = rank(B) <= d.
```

The reduced system is `B z<=beta`, and the target bound is `q^T z<=eta`.
This affine substitution adds no slack or artificial decision variables; see
[Boyd–Vandenberghe, equality elimination, slide 4.35](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf#page=122).
All quantities can be rational when the data are rational. A nonorthonormal
nullspace basis is sufficient: exact rank, not Euclidean length, matters.

Write a_i for the transpose of row i of B and M for the matrix with these a_i
as columns. Then (1) is equivalent to finding

```
lambda >= 0,  M lambda=q,  beta^T lambda<=eta.          (2)
```

To recover mu, solve `E^T mu=c-A^T lambda`. Its right-hand side is orthogonal
to `ker E` by `M lambda=q`, so it lies in `im E^T`. Moreover,

```
f^T mu = x0^T E^T mu = c^T x0-lambda^T A x0,
b^T lambda+f^T mu = c^T x0+beta^T lambda.              (3)
```

Thus the cost check in (2) is exactly the original bound check, independent of
which solution mu is chosen. One can solve on any basis of the original
equality rows and assign zero to the remaining equality multipliers. This uses
at most `rank(E)` nonzero equality multipliers, but the support bounds below
count inequalities only. Always recheck (1) on the original rows.

The effective normal rank is intrinsic:

```
k = rank([A; E])-rank(E),
```

because restricting covectors to `ker E` has kernel the row space of E.
Replacing N by another basis does not change k. It may change arithmetic size.

## 2. Certificate existence is a separate theorem

For a finite real reduced system, the unrestricted-variable Farkas alternative
says exactly one of the following holds:

```
some z has Bz<=beta;
some lambda>=0 has M lambda=0 and beta^T lambda=-1.    (4)
```

The normalized negative right-hand side is legitimate because a strictly
negative certificate can be multiplied by a positive scalar. This exact form
is stated in [Border, Proposition 35, printed p. 17](https://kcborder.caltech.edu/Notes/Alternative.pdf#page=17).

If the reduced feasible set is **nonempty**, validity of `q^T z<=eta` is
equivalent to existence of (2). Here is a short justification of the
nontrivial direction, making the feasibility hypothesis explicit. Consider
the finitely generated cone

```
C = cone{(a_i,beta_i): i=1,...,m} + cone{(0,1)}.
```

It is closed. If `(q,eta)` were outside C, separation from a closed convex
cone would give `(u,t)` with

```
a_i^T u+beta_i t>=0 for all i,  t>=0,
q^T u+eta t<0.
```

If t>0, `z=-u/t` is feasible and has `q^T z>eta`. If t=0, `v=-u`
satisfies `Bv<=0, q^T v>0`. From a feasible base z0 the points `z0+s v`
eventually violate the proposed bound. Both contradict validity. Therefore
`(q,eta)` belongs to C, which gives (2), with one nonnegative residual
`eta-beta^T lambda`. This residual need not be introduced as a search variable.

For completeness, closedness here is elementary: conic dependence elimination
reduces each representation to linearly independent generators. There are
finitely many such supports. For a convergent sequence of cone points, pass to
a subsequence with fixed support; the injective linear map on that support has
a continuous inverse on its image, so its nonnegative coefficients converge
to a nonnegative representation of the limit. The empty support covers zero.
The dependence elimination is also proved in the next section. Background on
finite cones and separation is in
[Bertsekas, Lecture 3](https://ocw.mit.edu/courses/6-253-convex-analysis-and-optimization-spring-2012/3e2a100d7fa327637ed8e31771a22c18_MIT6_253S12_lec03.pdf)
and [Lecture 10](https://ocw.mit.edu/courses/6-253-convex-analysis-and-optimization-spring-2012/9f80ea2051c10cc0f8cf3839983c381a_MIT6_253S12_lec10.pdf).

If the feasible set is empty, a bound is logically true vacuously, but need
not have a certificate matching its objective normal. For example,
`x<=0, -x<=-1` in variables (x,y) implies `y<=0` vacuously, while every
constraint normal has y coordinate zero. Detecting infeasibility is a separate
alternative, not a justification for silently asserting (2).

## 3. Support-size reductions and their assumptions

### 3.1 Conic dependence elimination

For finitely many columns v_i, suppose `sum lambda_i v_i=w` with lambda>=0.
If columns on its positive support S are dependent, choose a nonzero h
supported on S with `sum h_i v_i=0`. Orient h to have a positive entry and set

```
t = min{lambda_i/h_i : h_i>0},
lambda' = lambda-t h.
```

Then lambda'>=0, the target w is unchanged, and at least one positive
coefficient becomes zero. Repeat until the supported columns are independent.
The support has at most the dimension of their span. For w=0 this may end
with the empty support. This is the usual conic Caratheodory reduction; see
[Bertsekas, Lecture 3, PDF pp. 8–9](https://ocw.mit.edu/courses/6-253-convex-analysis-and-optimization-spring-2012/3e2a100d7fa327637ed8e31771a22c18_MIT6_253S12_lec03.pdf#page=8).

### 3.2 Nonempty feasible set: at most k inequalities for an upper bound

Assume `Bz<=beta` has a feasible point. Start with any certificate (2).
If its supported **normal** columns a_i are dependent, take a nonzero h
supported there with Mh=0. We can orient h so that

```
beta^T h>=0 and some h_i>0.                            (5)
```

If the cost is zero, either orientation with a positive entry works. If its
cost is nonzero, orient to positive cost. That orientation cannot have all
entries nonpositive: otherwise w=-h>=0 would obey Mw=0 and
`beta^T w<0`, contradicting feasibility by `0=w^T Bz<=w^T beta`.

Use the preceding t and replace lambda by lambda-t h. Normal matching remains
true, nonnegativity remains true, support decreases, and

```
beta^T(lambda-t h)<=beta^T lambda<=eta.
```

Iteration produces a certificate with linearly independent normal support and
at most k nonzero inequality multipliers. This proof reduces a certificate;
the existence argument in section 2 is a different step. When q=0, nonemptiness
forces eta>=0 for a valid bound, and lambda=0 suffices.

The reduction preserves or improves an upper bound; it need not preserve an
arbitrarily prescribed exact combined RHS. For the feasible interval
`x<=0, -x<=1`, objective x and target delta=1, any weights matching both
normal 1 and exact RHS 1 solve `lambda1-lambda2=1, lambda2=1`, hence are
(2,1), using two rows despite k=1. Allowing a stronger RHS gives (1,0)
and bound 0<=1. An insistence on exact RHS equality can manufacture an
unnecessary extra support requirement.

### 3.3 Known feasible optimizer: only active rows are needed

Suppose z* is feasible and maximizes q^T z. Existence gives a certificate at
eta=q^T z*. The gap identity is

```
beta^T lambda-q^T z* = sum lambda_i(beta_i-a_i^T z*).
```

Its nonnegative terms must all vanish. Thus every positive multiplier is on an
active row. Dependence elimination among active normal columns preserves cost
exactly since `beta_i=a_i^T z*` there. The support is at most the rank of the
active projected normals, which can be smaller than k. No vertex, full
dimensionality, strict feasibility or unique optimizer is needed. Classical
active-normal optimality and LP duality are discussed in
[Bertsekas, Lecture 10, PDF pp. 8–9](https://ocw.mit.edu/courses/6-253-convex-analysis-and-optimization-spring-2012/9f80ea2051c10cc0f8cf3839983c381a_MIT6_253S12_lec10.pdf#page=8).
If a proposed point fails feasibility, this pruning is unjustified.

### 3.4 Infeasibility: at most k+1 inequalities, and the extra row is necessary

For a contradiction after consistent equality elimination, normalize
`beta^T lambda=-1`. Apply conic dependence elimination to the **lifted**
columns

```
v_i=(a_i,beta_i), target (0,-1).
```

The support is independent in the lifted space and has at most
`rho=rank([B beta])<=k+1`. If this reduced system is actually infeasible,
the negative vertical target lies in the span of the lifted columns; projecting
that span onto the normal space has rank k and a one-dimensional kernel, so
rho=k+1. The stronger normal-independent support condition from 3.2 is false
here: every nonzero contradiction has dependent normal columns.

Both general bounds are sharp. In k variables, `z_j<=1` and objective
`sum z_j` require all k normals. For infeasibility, use the k rows
`z_j<=0` and the row `-sum z_j<=-1`. Unit weights on all k+1 rows give
`0<=-1`. Removing the last row permits z=0; removing row j permits z_j=1
and all other coordinates zero. Thus no proper subset can support a
contradiction. The k=0 cases are consistent with the bounds: a valid constant
bound needs zero inequalities; a false constant row needs one.

With rational data, Gaussian elimination, independent-column solves and
equality recovery produce rational certificates. Even if existence initially
gives real multipliers, the independent support's unique solution to a rational
linear system is rational. This rationality conclusion
does not require choosing a rational point from a numerical approximation:
each finite independent linear solve has rational matrix and target.

## 4. A deterministic finite search for specified certificates

The following is a mathematical procedure with ideal exact rational arithmetic,
not a completeness claim for the old finder or for our benchmark's interface.

1. Normalize row directions and objective sense. Check equality consistency;
   if inconsistent, recover the pure equality contradiction. Otherwise compute
   rational x0,N,B,beta,q. Keep a map to every original row.
2. A projected zero row with beta_i<0 is an immediate one-inequality
   contradiction. Zero rows with beta_i>=0 can be omitted from discovery.
3. For a bound, enumerate subsets S of inequality rows in increasing
   cardinality, then lexicographic original-row order, including S empty.
   Use all rows, or the active rows of a separately checked feasible candidate
   when seeking its optimality certificate with target eta=q^T z*. Stop at
   the relevant normal rank.
   Skip dependent normal supports. Solve `M_S lambda_S=q` exactly; because
   the columns are independent, the solution, if it exists, is unique.
   Check lambda_S>=0 and beta_S^T lambda_S<=eta.
4. For infeasibility, enumerate supports up to rho, skip dependent **lifted**
   supports, solve `sum lambda_i(a_i,beta_i)=(0,-1)` exactly and check
   lambda>=0. Do not add a vertical residual generator to this search.
5. Recover equality multipliers, pad omitted entries with zero, and check the
   full original-coordinate combination and RHS. A bound plus a feasible
   point attaining it certifies optimality; a bound by itself does not establish
   attainment or feasibility.

There are at most `sum_{j=0}^k binomial(m,j)` bound supports and
`sum_{j=0}^{k+1} binomial(m,j)` contradiction supports before rank pruning.
For ideal rational arithmetic the procedure terminates, because every finite
linear solve terminates and there are finitely many supports. Sections 2–3
prove its certificate completeness under the stated assumptions, including
all ranks and zero cases; no denominator grid is involved. In the bound search,
all rows rather than a truncated heuristic list are needed for this statement.

For a consistent equality system, exhaustive contradiction failure means
feasibility by (4). Given nonemptiness, exhaustive bound failure means the
specified upper bound is invalid. A prematurely stopped search says neither.
An active-row search failing at a checked feasible point means that point is
not optimal only if enumeration was exhaustive and the exact assumptions hold.
These assertions concern the mathematical procedure, not a machine run with
unchecked input, timeouts, memory limits or an incomplete candidate list.

At hand scale, prefer zero/one-row checks, active-row pruning when justified,
then support-size order. Positive proportional projected rows admit safe
dominance pruning: if `a_i=t a_j`, t>0, and `beta_i>=t beta_j`, row j
implies row i. Remove i from discovery and retain j and its original index.
Equal-cost duplicates may be represented by a fixed earliest row. Arbitrary
dependence is not a reason to drop a row: dependent normals can have different
costs, and contradiction discovery depends on the costs. Heuristic reordering
changes early success counts but is complete only with a full fallback.

## 5. Limits, degeneracy and representation choices

- Choosing free coordinates zero in an underdetermined multiplier solve is
  not a nonnegativity decision procedure. For columns -1 and 1 and target 1,
  the equation `-lambda1+lambda2=1` has solutions `(0,1)` and `(t,t+1)`
  for t>=0, while setting the free lambda2=0 returns `(-1,0)`. Independent
  support enumeration avoids this particular ambiguity.
- A finite integer or denominator grid need not contain a certificate. On
  `D x<=1` for a positive integer D, objective x, the unique nonzero weight
  is 1/D. There is no universal
  fixed denominator bound as input D varies. Small support does not mean
  short arithmetic; exact bit growth and solve cost remain practical limits.
- Positive row scaling preserves feasible halfspaces and support, with inverse
  scaling of the corresponding weight. It changes multiplier norms and bit
  lengths. Clearing denominators is legitimate, but is a convention, not a
  unique optimum principle. Equality scaling may use any nonzero scalar.
- Fixed nonzero objective multipliers cannot all be rescaled arbitrarily:
  their normal sum would become a multiple of c. Infeasibility can be rescaled
  to RHS -1. That normalization does not ensure unique weights, as duplicates
  show in [examples.md](examples.md).
- Lower-dimensional feasible sets and lineality are allowed. A bounded
  objective can be attained on a set with no vertex. The procedure here does
  not enumerate primal vertices, and does not find improving rays or solve
  arbitrary full LP status classification. A bound candidate or a proposed
  optimizer still has to be supplied or obtained by other work.
- The rank k cannot be replaced by the dimension of the feasible set's affine
  hull without further derivations. With no explicit equalities, the rows
  `x<=0, -x<=0` define a singleton of affine dimension zero, but a certificate
  for `x<=0` still needs one inequality multiplier. Treating an implied
  equality as a free signed row changes the original certificate accounting.
- Numerical rank decisions and near-zero residuals are not exact rank or exact
  identities. Approximate support guesses may be useful, but require exact
  rational reconstruction and original-row verification. A tolerance-based
  successful search does not establish the results above.

Introducing the vertical residual column `(0,1)` makes a bound problem into a
single conic membership problem in lifted space. It is mathematically sound,
but increases the support cap to k+1 and counts the residual as a generator.
The direct normal search exploits feasibility and keeps the residual as a
computed inequality check. Neither construction needs primal slack variables,
artificial variables, splitting original free variables into positive parts, or
splitting each equality into two inequality rows.

Increasing support size selects minimum positive inequality support in the
direct search over all eligible supports, stopped at its first success. In augmented
search the ordering counts the residual generator too; its first success need
not minimize original inequality support. For `x<=3, x<=1` and target `x<=2`,
with the residual column appended last and lexicographic supports, the two-row
lifted support yields weights `(1/2,1/2)` before the second row
plus residual, even though weight `(0,1)` alone is a stronger bound. Thus
search counts and the simplicity of the resulting certificate are different
comparison criteria.

## 6. Evidence scope

The [worked examples](examples.md) use exact rational identities. The small
[benchmark](benchmark/README.md) compares support enumeration choices on
built-in fixtures; it does not expose a general problem parser, checked bridge
or general LP finder. Its full runs provide reproducible finite evidence, not
formal algorithm verification. Independent ordinary review is recorded in
[reviews/mathematical-review.md](reviews/mathematical-review.md).

The existing `lp-certificates/` at frozen commit
`032db09354d41b58c2e9211ed7e69024a3e74010` was inspected first. Its deliberately
incomplete finder, exact verification and Lean export bridge are preserved on
their own branch, with their original claims. This study neither modifies nor
copies them. It is based on research baseline
`b1d6c20e2f02b484d09c5285e67d842b369f9df0`, which does not contain that sibling
component; integrating the branches remains separate work.
