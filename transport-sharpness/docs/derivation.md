# Audited three-atom transport exponent obstruction

This round continues the transport records at the verified research baseline
`b1d6c20e2f02b484d09c5285e67d842b369f9df0`. The following ordinary proof
and the independent [proof review](../reviews/proof-review.md) connect the
finite Lean core to the original Euclidean optimal-transport definitions.
The computation and formalization scopes are recorded separately below.

Fix an integer dimension `d >= 2`. Every distance and dot product is Euclidean.
For finite real `p >= 1`,

\[
W_p(\mu,\nu)^p=\inf_{\pi\in\Pi(\mu,\nu)}\int |y-z|^p\,d\pi(y,z).
\]

Here `T_mu` always denotes the unique **quadratic-cost** optimal map from the
fixed source to `mu`, including when the target comparison uses another `Wp`.
The map norm compares `T_mu(x)` and `T_nu(x)` at the same source point.

## Fixed source, probability and density bounds

Use the fixed source and target container

\[
K=Y=[-1,1]^d,\qquad \rho=2^{-d}\mathbf1_K\,dx.
\]

The volume of `K` is `2^d`, so `rho` is a probability. Its density has both
upper and positive lower bounds `2^-d` almost everywhere **on K**, independent
of all parameters. Globally its density lies between zero and `2^-d`; a
positive lower bound outside `K` is false. All moments needed here are finite.

The targets below are atomic and singular with respect to Lebesgue measure.
They have no Lebesgue densities, so the example provides no conclusion for a
class requiring bounded or positive target densities.

## Potentials and quadratic optimality

Assume throughout the two-parameter calculation that

\[
0<b<a,\qquad a+b<1.\tag{H}
\]

Define

\[
u(x)=\max\{-x_1,a,x_1\},\qquad
v(x)=\max\{-x_1,a+bx_2,x_1\}.
\]

Choose the first maximizing affine piece on ties. The selections `T,S` are
Borel, since their cells are finite intersections of affine strict and
nonstrict inequalities. Distinct slopes tie only on finitely many hyperplanes,
which are null for `rho`. Off these hyperplanes each map is the gradient of
its potential. Their slopes are respectively `(-e1,0,e1)` and `(-e1,b e2,e1)`.
They lie in `Y` and are distinct within each target.

For any finite affine maximum `w=max_i(x dot y_i+c_i)` with these null ties,
first merge repeated slopes, retaining their greatest intercept. Let `lambda`
be the selected slope map's law. The quadratic dual certificate is

\[
\phi(x)=|x|^2-2w(x),\qquad \psi(y_i)=|y_i|^2+2c_i.
\]

Indeed

\[
|x-y_i|^2-\phi(x)-\psi(y_i)
=2[w(x)-x\cdot y_i-c_i]\ge0.
\]

Every coupling of `rho,lambda` integrates the same dual expression, and the
selected graph has zero gap. This proves optimality directly. An optimal plan
has nonnegative gap of integral zero, hence zero gap almost everywhere. Away
from the null ties this forces the selected slope. The plan lies on the Borel
graph and its first marginal determines it uniquely. Thus `T,S` are the unique
quadratic optimal maps, modulo null changes, to their own target laws.
All terms are integrable because the source and target supports are bounded.
This argument does not require a separate existence theorem or claim that
the maps solve any source-to-target p-cost problem for p other than 2.

## Exact cell probabilities and joint law

Ignoring null boundaries, the central cells are

\[
A=\{|x_1|<a\},\qquad B=\{|x_1|<a+bx_2\}.
\]

Hypothesis (H) ensures `0<a-b <= a+bt <= a+b<1` for every `t in [-1,1]`.
No central interval is clipped by the cube. Conditional on `x2=t`, the first
coordinate is uniform with density `1/2` on `[-1,1]`. Therefore

\[
\rho(B\mid x_2=t)=a+bt,\qquad
\rho(S=\pm e_1\mid x_2=t)=\frac{1-a-bt}{2}.
\]

Averaging against `dt/2` gives central mass `a` and outer masses
`m=(1-a)/2`. The same calculation for `A` gives

\[
\mu=m\delta_{-e_1}+a\delta_0+m\delta_{e_1},\quad
\nu=m\delta_{-e_1}+a\delta_{be_2}+m\delta_{e_1}.\tag{1}
\]

All masses are positive and total one. The unused `d-2` coordinates integrate
to one under the normalized product measure.

For `t>0`, `B` contains `A`; for `t<0`, `A` contains `B`. Slice probabilities
of the differences are respectively `bt` and `-bt`. Integrating gives

\[
\rho(B\setminus A)=\rho(A\setminus B)=b/4,\quad
\rho(A\cap B)=a-b/4,\quad\rho(A\triangle B)=b/2.
\]

Reflection in `x1` splits each reassigned region equally. In minus, central,
plus order, the same-source coupling `(T,S)#rho` has matrix

\[
Q=\begin{pmatrix}
m-b/8&b/8&0\\
b/8&a-b/4&b/8\\
0&b/8&m-b/8
\end{pmatrix}.\tag{2}
\]

Its entries are nonnegative and its row and column sums are `(m,a,m)`.
The Lean core proves those properties on all real parameters satisfying (H).
The geometric identification of `Q` with the actual pushforward is the
ordinary slice proof above and independently checked exact polygon geometry.

## Exact finite target optimum

Matching the outer atoms to themselves and `0` to `b e2` gives cost `a b^p`.
Conversely every first-target point has second coordinate zero, so any coupling
satisfies

\[
\int|y-z|^p\,d\pi\ge\int |z_2|^p\,d\nu=a b^p.
\]

Consequently

\[
W_p^p=a b^p,\qquad W_p=a^{1/p}b\quad(1\le p<\infty).\tag{3}
\]

Equivalently, in the finite LP the row dual is zero and the column dual is
`(0,b^p,0)`. Every cost dominates this column value; the matching coupling
attains the dual objective. The finite core proves this lower bound and
attainment for every real `p>0`, with nonnegative `a,b` and `a<=1`; the metric
interpretation here remains restricted to `p>=1`.

For positive `b` and finite `p>=1`, equality in the coordinate bound requires
the first coordinates to coincide. They distinguish the three corresponding
atoms, so the matching coupling is unique. That uniqueness is an ordinary
proof here; it is also certified by strictly positive off-diagonal dual slacks
for the exact even-p fixtures, and is not a separate Lean theorem in this round.

## Exact same-source map distance

The first coordinate of `T-S` is zero off `A triangle B`, and has magnitude
one on that region. Its second coordinate is `-b` on `B` and zero elsewhere.
Thus

\[
|T-S|^2=\mathbf1_{A\triangle B}+b^2\mathbf1_B\quad\rho\text{-a.e.},
\qquad D^2:=\|T-S\|_{L^2(\rho)}^2=b/2+a b^2.\tag{4}
\]

The squared Euclidean cost matrix is

\[
C=\begin{pmatrix}0&1+b^2&4\\1&b^2&1\\4&1+b^2&0\end{pmatrix}.
\]

Its weighted sum with `Q` gives (4) again; this algebraic identity is proved
in Lean. The same-source coupling has cost strictly larger than the target
optimum by `b/2`. Each source-to-target map being optimal does not make that
same-source target-to-target coupling optimal.

## Shrinking atom mass: the finite-p ceiling

Set `b=a/2`, `0<a<1/2`. Then

\[
W_p=\frac12a^{1+1/p},\qquad D^2=\frac{a+a^3}{4},
\qquad D=\frac12\sqrt a\sqrt{1+a^2}.
\]

For every finite `p>=1` and real `alpha`,

\[
\frac{D}{W_p^\alpha}
=2^{\alpha-1}\sqrt{1+a^2}\,a^{1/2-\alpha(1+1/p)}.\tag{5}
\]

The exponent is negative exactly when `alpha>p/[2(p+1)]`. Taking `a_n=1/n`
for integers `n>=3` makes the ratio diverge to infinity. More explicitly, put
`delta=alpha(1+1/p)-1/2>0`; the ratio is at least `2^(alpha-1)n^delta`.
For any `C>=0`, an integer
`n>max(2,(2^(1-alpha)C)^(1/delta))` gives a strict violation.
Negative constants fail immediately because `D,Wp` are positive.

Thus no finite constant uniform over these targets can give
`D<=C Wp^alpha` above that ceiling. For `p=2` the ceiling is `1/3`; for `p=1`
it is `1/4`. Dimension, source, density bounds on `K`, container, number of
atoms, and minimum separation at least one stay fixed. For `a_n=1/n`, the
minimum atom mass is exactly `1/n` and tends to zero; each outer mass stays
at least `1/4`. A constant depending on a positive lower atom-mass bound is
not excluded by this shrinking-mass calculation.

At the ceiling the ratio tends to `2^(alpha-1)`. In particular its W2
endpoint limit is `2^(-2/3)`. This says only what happens along this family;
it establishes no global endpoint upper bound or optimality claim.

The kernel-checked `shrinking_exceeds_constant` proves the corresponding
all-real scalar statement for every `p>=1`, every `alpha` above the ceiling,
and every proposed real constant `C`. `W2_exceeds_constant` specializes it.
It constructs a real `a` by the growth of positive real powers. Identification
of those scalar quantities with (3) and the actual map norm uses the ordinary
Euclidean measure proof above.

## Fixed positive atom masses: a different one-half ceiling

Fix any `a0 in (0,1)`, and shrink `0<b<min(a0,1-a0)`. The target atom masses
are fixed at `((1-a0)/2,a0,(1-a0)/2)` and have positive common lower bound
`min(a0,(1-a0)/2)`. Equations (3)-(4) give

\[
W_p=a_0^{1/p}b,\qquad D^2=b/2+a_0 b^2,
\quad \frac{D}{W_p^\alpha}
=a_0^{-\alpha/p}\sqrt{1/2+a_0b}\,b^{1/2-\alpha}.
\]

This ratio diverges for `alpha>1/2`, is finite and positive at `1/2`, and
tends to zero for `alpha<1/2`. Hence this family gives only the separate
necessary `1/2` ceiling; it does not give a `1/3` ceiling for fixed masses.
The Lean scalar theorem `fixed_mass_exceeds_constant` verifies this
quantified obstruction on the admissible matrix domain. Its scalar `p`
parameter is unrestricted, while the Wasserstein conclusion requires `p>=1`.

The regression family uses `a0=1/4`: all targets have masses `(3/8,1/4,3/8)`.
For W2, `Wp=b/2` and `D^2=b/2+b^2/4`. At exponent `1/2` the squared ratio is
exactly `1+b/2`, tending to one. No matching positive upper estimate on any
fixed-mass class is proved.

## Formal and computational limits

The formal core covers probabilities as finite mass arrays, finite coupling
constraints, quadratic/every-real-positive-p primal-dual optimal values,
validity and cost of the candidate same-source matrix, real-power identities,
and both scalar exponent obstructions. Full expected types and definition
bodies are reviewed separately and locally replayed with the same Lean kernel.

Lebesgue normalization, hyperplane nullness, Borel map construction,
source-to-target dual integration and uniqueness, polygon-area identification,
higher-dimensional product integration, and the bridge from arbitrary Borel
couplings to finite arrays remain ordinary proofs. No Lean acceptance of those
measure-theoretic claims is asserted. Exact experiments use rational arithmetic
in dimension two, and cannot replace those arguments or establish novelty.
