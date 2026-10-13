# Independent proof review: three-atom transport obstruction

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](../PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

Reviewed on 2026-10-13 by an independent proof-review agent against the
research baseline `b1d6c20e2f02b484d09c5285e67d842b369f9df0`. This review
independently derives the finite-atomic calculations and checks their
assumptions. It is an ordinary mathematical review, not a Lean acceptance
report. The finite `p` necessary ceiling `p/[2(p+1)]`, its `W2`
specialization `1/3`, and the
separate fixed-positive-mass ceiling `1/2` are supported as stated below.
No correction to the baseline mathematical formulas was found.

## Material inspected and scope

The inspected material consists of:

- `research/starter/transport-stability/{proof.md,theorems.json}`;
- `research/supplement/transport-stability/{proof.md,theorems.json,check_exact_cases.py}`;
- `research/supplement/reviews/transport/{audit-report.md,optional-refinements.md,review-record.json}`;
- `research/supplement/catalog/sources/preprints_Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026_build_source_sections_sharpness.tex`.

The starter and supplement proof files are byte-identical, with SHA-256
`7d8445fc42103de171a2366da8f15a4cce3ddec37f5ea99d3b19738efea212cd`.
The supplied sharpness section has SHA-256
`f8732d68d0de8505d20f6c42aefce95d60b3e8363569681fa30632c997999590`,
matching its existing provenance record. Its stated upstream revision is
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` in `openai/math`.
This reviewer checked the local supplied source, without independently
refetching that upstream revision or reviewing the whole paper.

No `AGENTS.md` or `.agents/skills` files were found by a search under
`${WORKSPACE}` at the time of this review. All previous research files are
preserved. In particular, the existing portable theorem record's pending
review metadata is not edited by this review.

The intended meaning of `T_mu` is the unique **quadratic** optimal map
from the fixed source to `mu`; this meaning stays quadratic when the
target metric in the stability comparison is `Wp` for another `p`.
The comparison is the same-source map norm, not an optimization between
the target measures.

## Hypotheses and density audit

Fix an integer `d >= 2` and use Euclidean distance on `R^d`. Set

\[
K=Y=[-1,1]^d,\qquad
\rho=2^{-d}\mathbf 1_K\,dx.
\]

The source is a probability measure because `vol(K)=2^d`. Its Lebesgue
density equals `2^-d` almost everywhere on `K` and equals zero outside
`K`. Consequently both its upper and positive lower density bounds on
`K` can be taken to be `2^-d`, independently of every construction
parameter. It has a global upper density bound `2^-d`; it does not have
a positive lower density bound on all of `R^d`.

Assume

\[
0<b<a,\qquad a+b<1.\tag{H}
\]

These inequalities imply `0<a<1` and `0<b<1`, and guarantee that the
half-width `a+bt` stays strictly between zero and one for every
`t in [-1,1]`. They prevent both sign changes and clipping by the cube.
The following cell formulas cannot be used unchanged once these
restrictions are dropped.

The targets below are probability measures supported on three points.
They are singular with respect to Lebesgue measure: each gives positive
mass to a singleton, while a singleton has Lebesgue measure zero.
They therefore do not have Lebesgue densities or any finite Lebesgue
density bound. Claims about source density must not be restated as claims
about target density. No obstruction for a class of absolutely continuous
targets with uniform positive density bounds follows from this example.

## Quadratic map optimality, proved directly

Define

\[
u(x)=\max(-x_1,x_1,a),\qquad
v(x)=\max(-x_1,x_1,a+bx_2).
\]

Their slope lists are `(-e1,e1,0)` and `(-e1,e1,b e2)`. All are in the
fixed target container `Y`, and slopes within either list are distinct.
Choose the first maximizing slope on boundaries. The resulting maps
are Borel because each selection region is an intersection of finitely
many strict or nonstrict affine inequalities. Distinct-slope ties are
contained in finitely many affine hyperplanes, which are `rho`-null.
Off those sets the selected slope is the gradient of the finite affine
maximum.

For a general such maximum `w(x)=max_i(x dot y_i+c_i)`, set

\[
\phi(x)=|x|^2-2w(x),\qquad
\psi(y_i)=|y_i|^2+2c_i.
\]

Repeated slopes, if present in the general statement, are merged by
retaining their largest intercept. Direct expansion gives

\[
|x-y_i|^2-\phi(x)-\psi(y_i)
=2\bigl[w(x)-x\cdot y_i-c_i\bigr]\ge0.
\]

The graph plan of the selected map has zero gap and has its induced
target as second marginal. Every competing coupling of those marginals
integrates the same `phi+psi`, so this graph plan is optimal. All terms
are integrable here because both supports are bounded; in the more
general baseline lemma the finite source second moment and finite slope
set also suffice.

An optimal competing plan must have zero nonnegative gap almost
everywhere. Away from the null tie sets, this forces its target
coordinate to equal the sole maximizing slope. The plan is therefore
concentrated on the selected graph and, having first marginal `rho`,
equals its graph pushforward. This proves uniqueness of the whole
optimal plan, and hence of the map modulo `rho`-null sets. No assertion
about differentiability on the null boundaries is needed.

## Independent cell and joint-law derivation

Write

\[
A=\{|x_1|<a\},\qquad
B=\{|x_1|<a+bx_2\}.
\]

Up to null boundaries, `T=0` on `A` and `T=sign(x1)e1` elsewhere;
`S=b e2` on `B` and `S=sign(x1)e1` elsewhere. Conditional on `x2=t`,
the source's first coordinate has density `1/2` on `[-1,1]`, so an
interval `(-h,h)` has mass `h`. Hypothesis (H) makes this apply with
`h=a+bt`. Thus

\[
\rho(B\mid x_2=t)=a+bt,\quad
\rho(S=\pm e_1\mid x_2=t)=\frac{1-a-bt}{2}.
\]

Integrating against `dt/2` gives, with `m=(1-a)/2`,

\[
\mu=m\delta_{-e_1}+a\delta_0+m\delta_{e_1},\qquad
\nu=m\delta_{-e_1}+a\delta_{be_2}+m\delta_{e_1}.\tag{1}
\]

Both measures have exactly three distinct positive-mass atoms. The
unused `d-2` coordinates have normalized product mass one, so these
two-dimensional slice calculations hold in every fixed `d>=2`.

For `t>0`, `B` contains `A`; for `t<0`, `A` contains `B`. Each difference
has conditional mass `b|t|` on the relevant half of the `t` interval.
Consequently

\[
\rho(B\setminus A)=\rho(A\setminus B)=\frac b4,\quad
\rho(A\cap B)=a-\frac b4,\quad
\rho(A\triangle B)=\frac b2.\tag{2}
\]

Reflection in `x1` splits each reassignment equally between its two
sides. In the orders `(-e1,0,e1)` for `T` and `(-e1,b e2,e1)` for `S`,
the same-source coupling is therefore

\[
Q=\begin{pmatrix}
m-b/8 & b/8 & 0\\
b/8 & a-b/4 & b/8\\
0 & b/8 & m-b/8
\end{pmatrix}.\tag{3}
\]

Every entry is nonnegative under (H): `a-b/4>0`, and
`b<1-a` gives `m-b/8>3(1-a)/8>0`. Its row and column sums are
`(m,a,m)` and its total mass is one. This matrix is an exact finite
probability calculation reusable independently of the asymptotic family.

## Exact transport costs and a finite dual certificate

For every real finite `p>=1`, the diagonal matching coupling fixes the
outer atoms and moves the central atom from `0` to `b e2`. It costs
`a b^p`. Every first-target atom has second coordinate zero, so for every
coupling `pi`,

\[
\int |y-z|^p\,d\pi
\ge\int |y_2-z_2|^p\,d\pi
=\int |z_2|^p\,d\nu
=ab^p.
\]

The lower and upper bounds coincide:

\[
W_p(\mu,\nu)^p=ab^p,\qquad W_p(\mu,\nu)=a^{1/p}b.\tag{4}
\]

For clarity, this can also be written as a finite linear-program dual
certificate: assign source dual value zero to all three first-target
atoms, destination dual value `b^p` to `b e2`, and destination dual
value zero to each outer atom. These sums are below every corresponding
`p`-cost. The certificate objective is exactly `a b^p`, attained by the
matching plan. Thus no numerical optimizer is needed.

For finite `p`, equality in the coordinate bound forces the first
coordinates to agree, since raising nonnegative numbers to `p>0` is
strictly increasing and Euclidean distance equals the absolute second
coordinate difference only when all other coordinate differences vanish.
Those first coordinates identify the three matched atoms, proving unique
target-coupling optimality, including at `p=1`. No uniqueness of the
`W_infinity` optimizer is asserted. Its value is `b`, by the same
coordinate lower bound and the matching upper bound.

For `p=2`, the exact cost matrix is

\[
C=\begin{pmatrix}
0&1+b^2&4\\
1&b^2&1\\
4&1+b^2&0
\end{pmatrix}.\tag{5}
\]

The same-source map squared distance is the weighted sum of `C` with
`Q`. Equivalently, its first-coordinate difference has magnitude one
exactly on `A triangle B`, and its second-coordinate difference equals
`-b` on `B`. Orthogonality yields

\[
|T-S|^2=\mathbf1_{A\triangle B}+b^2\mathbf1_B
\quad\rho\text{-almost everywhere},
\]

\[
\|T-S\|_{L^2(\rho)}^2=\frac b2+ab^2.\tag{6}
\]

In particular, the same-source target coupling and the optimal
target-to-target coupling differ. Substituting the former cost for
`Wp` would invalidate the exponent calculation.

## Shrinking central mass and the finite-p ceiling

Set `b=a/2` and `0<a<1/2`. All of (H) holds. The explicit masses are
`((1-a)/2,a,(1-a)/2)`; the central atom mass tends to zero. The source,
its density bounds, dimension, target container, atom count, and minimum
within-target atom separation stay fixed. The separation is at least one:
outer-to-outer distance is two, central-to-outer distances are one in
`mu` and `sqrt(1+b^2)` in `nu`.

Equations (4) and (6) give

\[
W_p=\frac12a^{1+1/p},\qquad
D:=\|T-S\|_2=\frac12\sqrt a\sqrt{1+a^2}.
\]

For real `alpha>0`, using positive real powers,

\[
\frac{D}{W_p^\alpha}
=2^{\alpha-1}\sqrt{1+a^2}\,
a^{1/2-\alpha(1+1/p)}.\tag{7}
\]

Since `p>0`, the exponent of `a` is negative exactly when
`alpha>p/[2(p+1)]`. Taking `a_n=1/n`, integers `n>=3`, proves divergence
and excludes every finite constant uniform over these target pairs.
The constant may depend on the fixed dimension, cube, source, and fixed
`p`; it may not depend on the shrinking target atom mass. This proves
the necessary ceiling, with `1/3` for `p=2` and `1/4` for `p=1`.

An explicitly quantitative divergence witness is available. Let

\[
\delta=\alpha(1+1/p)-\frac12>0.
\]

Then the ratio at `a_n=1/n` is at least `2^(alpha-1) n^delta`. For any
proposed nonnegative constant `C`, choosing an integer

\[
n>\max\{2,(2^{1-\alpha}C)^{1/\delta}\}
\]

makes the ratio strictly exceed `C`. This exhibits the quantifiers
behind the no-uniform-estimate statement without relying on decimal
or finite-fixture evidence.

At the ceiling `alpha=p/[2(p+1)]`, this single family's ratio tends to
`2^(alpha-1)`, a finite positive value. For `p=2` that is `2^(-2/3)`.
These endpoint values do not supply an upper estimate on the full class,
nor do they prove global optimality of any exponent.

For root-free checking of the `W2` algebra, put `F=W2^2=a^3/4` and
`G=D^2=(a+a^3)/4`. Then

\[
\frac{G}{F^\alpha}
=4^{\alpha-1}(1+a^2)a^{1-3\alpha}.
\]

Since `(D/W2^alpha)^2=G/F^alpha`, this is the same obstruction.
An exact arithmetic certificate for the rational polynomial identities
does not itself establish this real-power asymptotic or the underlying
Euclidean-measure definitions.

## Fixed positive central mass: the separate one-half ceiling

Fix any `a0 in (0,1)` and let
`0<b<min(a0,1-a0)`. Now both targets have the fixed positive masses
`((1-a0)/2,a0,(1-a0)/2)`. Equations (4) and (6) instead give

\[
W_p=a_0^{1/p}b,\qquad
D=\sqrt b\sqrt{1/2+a_0b},
\]

\[
\frac{D}{W_p^\alpha}
=a_0^{-\alpha/p}\sqrt{1/2+a_0b}\,
b^{1/2-\alpha}.\tag{8}
\]

This diverges for `alpha>1/2`. For `W_infinity=b`, remove the factor
`a0^(-alpha/p)` and the same ceiling holds. At `alpha=1/2`, the ratio
has a finite positive limit; no matching upper bound is proved here.

The previous review's specialization `a0=1/4`, `0<b<1/4`, yields
fixed masses `(3/8,1/4,3/8)` and

\[
W_p=4^{-1/p}b,\qquad D^2=b/2+b^2/4,
\]

exactly as recorded. This family does **not** yield `1/3` for `W2` or
`1/4` for `W1`, because it lacks the extra shrinking-mass factor in
the target cost. It also gives essential-supremum discontinuity at the
fixed target `mu`: `B minus A` has positive mass and
`||T-S||_infinity=sqrt(1+b^2)` tends to one while the target distances
tend to zero.

## Required boundaries on later formalization and reporting

No required mathematical correction to the existing obstruction was
identified. The following qualifications are necessary when reporting
new machine-checkable work:

- A Lean theorem about a finite matrix with stated marginals and costs
  certifies that finite problem. To claim that Lean has accepted the
  full optimal-map obstruction, the bridge from cube measures and
  affine cells to that matrix, source-map optimality, and the real-power
  divergent sequence must also be kernel checked.
- Exact rational geometry, dual certificates, or exhaustive finite
  transport-polytope enumeration can certify rational fixtures. They
  do not automatically quantify over all real parameters or real `p`.
- The source density bounds are fixed and explicit; targets remain
  atomic. No positive target-density claim is supported.
- The shrinking family excludes exponents strictly above the stated
  ceiling; the fixed-mass family excludes exponents strictly above
  `1/2`. Neither proves a global upper estimate, uniqueness of an
  endpoint exponent, or mathematical novelty.
- No result from this review is a native Mac MRS integration or a Lean
  compilation claim. Prior review and source inspection are separate
  evidence levels from a newly executed proof checker.

This reviewer initially wrote only this scoped review file. The final
verification also adds the independent slice checker and its stdout file
under `reviews/`; no prior work or other agent's deliverable is edited.

## Review of the new Lean source and accepted statement scope

The new files `TransportSharpness/Finite.lean` and
`TransportSharpness/Obstruction.lean` were inspected in full. Independently
executed source checks on 2026-10-13 both returned exit status zero and no
stdout or stderr. From the scoped directory the exact commands were:

```sh
env PATH=${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin:$PATH ${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lake env lean TransportSharpness/Finite.lean
env PATH=${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin:$PATH ${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lake env lean TransportSharpness/Obstruction.lean
```

The inspected/checked source hashes were:

- `Finite.lean`: `2ca131e39877bb4ec3d0803de4b9bdfa21d7d2e2935f9777db0408aa3cadf18a`;
- `Obstruction.lean`: `ebb8d5361a6dce5ebc7e436d59750a58581030ca1d351e420f9280dcf83df0e1`.

The scoped configuration pins Lean `v4.24.0` and mathlib revision
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. These checks used the existing
package/build cache; this reviewer did not rebuild all dependency
sources or independently authenticate the compiler distribution. The
separate compiler-audit evidence describes the root agent's local
distribution-byte check. No new `axiom`, `sorry`, `admit`, or unsafe
proof escape is present in these inspected Lean source files.

The source interpretation is consistent with the proof above:

- `IsCoupling` states nonnegative entries and equal finite row/column
  marginals. `mass_sum` proves total mass one; `mass_positive` supplies
  strict atom masses only under `0<a<1`. `matching_coupling` allows the
  boundary cases `a=0` or `a=1`, where a three-positive-atom description
  is inapplicable.
- `sqCost` is explicitly the sum of squared coordinate differences in
  the two-dimensional atom lists. It does not silently use the default
  norm on Lean's product type. `finite_dual_lower_bound`,
  `quadratic_minimum`, and `pCost_minimum` give valid attained finite
  primal/dual optima. `pCost_minimum` assumes scalar `p>0`; invoking it
  as a usual Wasserstein statement requires `p>=1`. The files do not
  formally define an abstract Wasserstein distance.
- `commonSource_coupling` certifies the exact matrix (3) on `Admissible`.
  `commonSource_cost` proves its polynomial cost identity. The strict
  cost-comparison theorem is an unconditional algebraic statement for
  `b>0`; its interpretation as a comparison of actual couplings also
  uses the admissibility and nonnegativity theorem.
- `mapSize` and `targetDistance` are explicit real scalar definitions.
  `shrinking_exceeds_constant`, with `p>=1`, proves a strict violation
  for every proposed real constant and an admissible parameter `a`.
  `W2_exceeds_constant` correctly specializes the ceiling to `1/3`.
  The real-power divergence is thus accepted in the scalar model, not
  merely inferred from finite numerical samples.
- `fixed_mass_exceeds_constant` correctly fixes `a in (0,1)` and finds
  an admissible `b` for every exponent above `1/2`. Its theorem quantifies
  over all real scalar `p`, including Lean's totalized `1/p` at `p=0`.
  This stronger algebraic scope is consistent; only its restriction to
  `p>=1` has the Wasserstein interpretation used in the research claim.
- Finite optimizer uniqueness is not a stated theorem in the new Lean
  core. It remains the equality-case argument in the ordinary proof.
  Likewise the cell integration, cube measure, pushforwards, quadratic
  source-map optimality, and map/cost identification are not encoded
  in these files. No accepted finite theorem changes that boundary.

No new mathematical scope defect was identified. A claim that the full
measure-theoretic optimal-map theorem is kernel checked would exceed
the accepted statements; the finite/scalar core itself is supported.

The root agent reports a fresh fetch of the pinned upstream sharpness
section: 7662 bytes, SHA-256
`2c1682fe0dc4bd8da5883760a909271382ec2a63ef68e8334b5491bb0985c902`.
The retained local source is 7663 bytes with the recorded
`f8732d68...` hash. Their only reported byte difference is the local
copy's extra trailing newline. This preserves mathematical content,
but those files must not be described as byte-identical. The earlier
provenance discussion in this review concerns the retained local bytes;
the new provenance evidence should record the independent fetch and
newline distinction explicitly.

## Final derivation and computation review

The final `docs/derivation.md` and `docs/SOURCES.md` were read in full.
The derivation's hypotheses, scalar formulas, quantifiers and density
statements agree with this independent review. The distinction between
the shrinking-mass ceiling and fixed-mass ceiling is explicit and valid.
The sequence `a_n=1/n`, `n>=3`, has minimum target atom mass exactly
`1/n`; its dimension, source density bounds, target container, atom count
and separation stay fixed. For the fixed family `a0 in (0,1)`, the
uniform positive lower mass is `min(a0,(1-a0)/2)` and only `b` shrinks.
Endpoint limits, negative candidate constants, and strict quantifier
violations are described correctly. No endpoint upper estimate or
novelty claim is made.

The derivation explicitly identifies the accepted finite/scalar Lean
scope and leaves the measure-theoretic bridge as ordinary proof. Its
distinction between scalar `p>0` finite costs and metric `p>=1` is
correct. A minor clarification requested by this reviewer was applied:
the generic affine-maximum dual paragraph now merges repeated slopes
at their greatest intercept before assigning a single-valued dual
function. The actual counterexample already has distinct slopes, so
this wording clarification does not change its mathematics.

The source notes distinguish the retained local source from the fresh
upstream bytes by their one trailing newline and identify the trusted
cached-dependency and same-kernel replay boundaries. The source notes'
repository publication/privacy assertions belong to the root agent's
publication audit; this mathematical review is not a separate remote
publication check.

Final reviewed document and computation hashes:

- `docs/derivation.md`: `9112545adcc68fc31ce386c4a0982c071ea534f1bc99acce45dde8cb55c5c6ae`;
- `docs/SOURCES.md`: `bb3e9a14b625da252c431c57dce280ad371a511da68bacf69dae2059811f5248`;
- `scripts/check_exact.py`: `11f61293fc2f2aa0f20741fcd489a43baa5ff12b86848531128ff31ffbdfd651`;
- `tests/test_exact.py`: `14a87d52350eceec6a173e210bccd9b6f827af964b213eba0e5713aa32a82e95`.

### Independent code assessment

This reviewer read the expanded exact checker and its tests, rather than
relying only on its author's rerun. The following algorithmic conclusions
were checked directly:

1. Every affine-cell half-plane is derived by subtracting the actual
   slope/intercept pieces. Both comparisons for every outer cell are
   retained. Distinct slopes make their shared boundaries zero area.
2. Polygon clipping intersects each rational edge at the exact rational
   zero of its plane value. Boundary endpoints are retained by their
   outgoing edge, including when the preceding edge approaches from
   outside. Consecutive duplicate removal does not change area. The
   square's shoelace area is multiplied by density `1/4`, and the total
   joint mass is checked to be one.
3. Primal feasibility checks nonnegative entries, all row/column sums,
   and probability normalization. The finite dual certificate checks
   every cost inequality, equality of primal/dual objectives, and
   complementary slackness. For an even positive integer `p`, raising
   the squared Euclidean cost to integer `p/2` is exact rational
   arithmetic. Strict off-diagonal dual slacks leave exactly the
   diagonal zero-slack support and certify uniqueness for these
   fixtures. Enumeration is an additional check, not needed for
   optimality. Its five independent constraints and all 126 bases
   include degenerate vertices; the six-vertex equal-mass case prevents
   a mistaken universal ten-vertex claim.
4. For rational `p>=1`, `alpha>0`, the checker takes
   `L=lcm(denominator(2 alpha/p),denominator(2 alpha))`. Thus
   `A=2L alpha/p` and `B=2L alpha` are nonnegative integers and

   \[
   (D/W_p^\alpha)^{2L}
   =\frac{(b/2+ab^2)^L}{a^A b^B}.
   \]

   This follows from positive real powers and the independently
   proved `Wp=a^(1/p)b` formula. The program evaluates its rational
   consequence without a floating-point root. It does not pretend to
   solve a full irrational-cost LP for arbitrary rational `p`.
5. The dyadic witness searches compare this positive integer power
   strictly with `C^(2L)`. Since the ratio and `C` are positive, that
   comparison implies a strict violation of the original inequality.
   The checked integer growth exponent is `A+B-L>0` for the
   shrinking family and `B-L>0` for the fixed family. The elementary
   positive-growth argument supplies termination and stays distinct
   from the finite executed witnesses. Recomputing their polygon
   geometry tests even very small central masses.
6. Invalid parameter regimes, subcritical or endpoint counterexample
   claims, bad marginal/dual certificates, and floating-point inputs
   are rejected. The code's `require` checks remain active under
   Python optimization; it does not depend on removable `assert`
   statements for these certificates.

No code defect affecting the advertised finite calculations was found.

### Independent reruns and separate slice method

All commands below were independently executed in `transport-sharpness/`
using Python `3.12.14`, standard library only. They do not change code or
data files; the final command writes only its new reviewer stdout log.

```sh
python3 -B scripts/check_exact.py --verify
python3 -B -O -m unittest discover -s tests -v
python3 -B reviews/independent_slice_check.py > reviews/independent-slice-stdout.txt 2>&1
```

Results, all exit status zero:

- The verifier reproduced all three existing JSON reports byte for byte:
  13 named fixtures, 100 rational-grid cases, seven rejected inputs,
  and 48 exact candidate-constant violations.
- The optimized unittest suite ran 16 tests and returned `OK`. Its
  negative certificates and malformed-scope tests remained operative.
- The separate [independent slice check](independent_slice_check.py)
  matched all nine polygon joint masses for 131 distinct rational pairs,
  including clipped widths and negative tilts. Its
  [stdout](independent-slice-stdout.txt) records the exact result.

The independent method fixes the source-map intervals
`[-1,-a],[-a,a],[a,1]`, clamps the moving half-width to `[0,1]`, and
intersects them with `[-1,-h],[-h,h],[h,1]`. It integrates the nine
overlap lengths against `dt/4`. Breakpoints at raw half-width values
`0,a,1` exhaust every change of affine expression, so exact trapezoids
on those rational intervals give exact joint masses. It never calls
polygon clipping or inserts the claimed closed-form joint matrix into
the expected-value calculation. It imports the scoped geometry checker
only to obtain the polygon values being tested. The method is restricted
to `0<a<1`, as explicitly guarded; it permits zero, negative, and
clipping tilts for this verification. Its SHA-256 is
`fdeda1607f6336508f7ad8fe548db4a1510c0d2524cc4e3ca4618cdd07dc1b5e`.

Verified report SHA-256 values:

- `data/exact-cases.json`: `2f288083786720d116f4c3d7861a0beacb2d514613d1a428489f06894a113d1b`;
- `data/regression-grid.json`: `15f82ecb6b22e40b7d61bb59f622fbc47b0d60c2efcc6e38bcd4fd1f151ecee7`;
- `data/exponent-regressions.json`: `6f5730a11fe514c6f60e16268bce61795d98fce616e1741e58a262ad2a5de267`.

Final mathematical/computational review disposition: supported within
the stated finite/scalar and ordinary-proof boundaries, with no remaining
required mathematical correction. The review does not certify a global
upper stability estimate, native MRS import, or remote publication.
