# From an approximate root to an exact certificate

First edition, 15 October 2026. This is a study and a small exact verifier for a
classical sufficient criterion. It makes no claim of mathematical novelty or
Lean verification. The executable scope is square systems of polynomials with
rational coefficients over the real numbers.

An approximate answer is useful input to a proof, but is not yet a proof. This
toolkit turns a rational center, a rational box, and a rational matrix into
checkable inequalities which imply that **exactly one real zero lies in that
specified closed box**, together with an explicit bound on its distance from
the center. A rejected candidate means only that this particular test did not
certify it.

## 1. What the extra information does

Suppose a numerical calculation suggests that \(F(c)\) is small. Even an exact
small residual cannot on its own establish a nearby root. For example,
\(f(t)=t^2+\varepsilon\), with \(\varepsilon>0\), has residual
\(f(0)=\varepsilon\) and has no real zero. Also
\(g(t)=\varepsilon(t-1)\) has residual of magnitude \(\varepsilon\) at zero,
while its root stays distance one away. Multiplying equations by small
constants can shrink residuals without improving an approximation.

We need both inverse scale information and control of derivative variation on
a whole region. Choose a fixed matrix \(Y\), usually an exact rational
approximation to \(DF(c)^{-1}\), and consider the **map**

\[
T:B\longrightarrow\mathbb R^n,\qquad T(x)=x-YF(x).
\]

Here \(T\) is a function; \(T(c)=c-YF(c)\) is one vector. A small value of
\(YF(c)\) controls a first step, whereas a bound on \(DT\) controls the map
throughout the box. The matrix \(Y\) stays fixed as \(x\) varies. This map is
generally different from the Newton map \(x\mapsto x-DF(x)^{-1}F(x)\).

If \(Y\) is invertible, \(T(x)=x\) is equivalent to \(F(x)=0\). If it is
singular, this implication can fail: \(YF(x)=0\) need not imply \(F(x)=0\).
The verifier therefore checks invertibility exactly.

## 2. The certificate theorem

Let \(n\ge1\), \(c\in\mathbb R^n\), and \(r_i>0\). Define

\[
B=\prod_{i=1}^n[c_i-r_i,c_i+r_i],\qquad
\|v\|_r=\max_i\frac{|v_i|}{r_i}.
\]

Suppose \(F:U\to\mathbb R^n\) is continuously differentiable on an open set
\(U\) containing \(B\). Let \(Y\in\mathbb R^{n\times n}\) be invertible.
An interval matrix \(J\) is an array of closed real intervals such that

\[
\partial_jF_i(x)\in J_{ij}\quad\text{for every }x\in B.
\]

Using interval operations, form \(A=I-YJ\), and set

\[
M_{ij}=\max(|\inf A_{ij}|,|\sup A_{ij}|),\quad
d_i=|(YF(c))_i|,\quad
s_i=d_i+\sum_j M_{ij}r_j,
\]

\[
q=\max_i\frac{\sum_jM_{ij}r_j}{r_i},\qquad
\eta=\max_i\frac{d_i}{r_i}.
\]

**Theorem.** If

\[
\boxed{s_i\le r_i\text{ for every }i,\qquad q<1,}
\tag{C}
\]

then \(F\) has a unique zero \(\xi\) in the entire closed box \(B\). Moreover

\[
\boxed{\|\xi-c\|_r\le\min\left(1,\frac{\eta}{1-q}\right),\qquad
|\xi_i-c_i|\le r_i\min\left(1,\frac{\eta}{1-q}\right).}
\tag{E}
\]

All the quantities can be rational when the inputs and derivative enclosures
are rational. There is no appeal to a rounded decimal comparison with one.
The componentwise self-map test in (C) should not be replaced by the stronger
shortcut \(\eta+q\le1\): that shortcut is sufficient but may discard valid
certificates whose worst residual and derivative bounds occur in different
rows.

### Proof

First obtain a difference bound valid on the whole box. For any \(x,y\in B\),
their connecting segment lies in \(B\), since a box is convex. By the
fundamental theorem of calculus, component by component,

\[
T(x)-T(y)=\int_0^1\bigl(I-YDF(y+t(x-y))\bigr)(x-y)\,dt.
\]

The interval construction gives
\(|(I-YDF(z))_{ij}|\le M_{ij}\) for every \(z\in B\). Thus

\[
|T_i(x)-T_i(y)|\le\sum_j M_{ij}|x_j-y_j|,
\qquad \|T(x)-T(y)\|_r\le q\|x-y\|_r. \tag{1}
\]

There is generally no single intermediate point for which the familiar
scalar mean-value formula becomes a vector identity. The integral avoids
that incorrect substitution.

**Preserving the domain.** Since \(T(c)-c=-YF(c)\), for \(x\in B\),

\[
|T_i(x)-c_i|\le d_i+\sum_jM_{ij}|x_j-c_j|
\le s_i\le r_i.
\]

Hence \(T(B)\subseteq B\). This is the role of the first set of
inequalities. It ensures the iteration never leaves the region on which our
derivative bounds are valid.

**Existence.** Put \(x_0=c\) and \(x_{k+1}=T(x_k)\). Every iterate lies in
\(B\). Equation (1) implies, by induction,

\[
\|x_{k+1}-x_k\|_r\le q^k\eta.
\]

For \(m>k\), the triangle inequality and the geometric series give

\[
\|x_m-x_k\|_r\le\eta\sum_{j=k}^{m-1}q^j
\le\frac{q^k\eta}{1-q}.
\]

Here \(0\le q<1\), so the iterates form a Cauchy sequence. The weighted norm
is equivalent to the usual norm on \(\mathbb R^n\); a closed box is complete.
They converge to a point \(\xi\in B\). Continuity gives
\(T(\xi)=\lim_kT(x_k)=\lim_kx_{k+1}=\xi\). Invertibility of \(Y\) then
gives \(F(\xi)=0\).

**Uniqueness.** If \(u,v\in B\) are zeros, both are fixed points. Equation
(1) gives \(\|u-v\|_r\le q\|u-v\|_r\), which forces \(u=v\). This proves
uniqueness everywhere in \(B\), including its boundary.

**Error.** Apply (1) to \(\xi,c\):

\[
\|\xi-c\|_r\le\|T(\xi)-T(c)\|_r+\|T(c)-c\|_r
\le q\|\xi-c\|_r+\eta.
\]

Rearrangement proves the fraction in (E), and \(\xi\in B\) supplies the
additional bound one. This proves the theorem. The same argument also gives
\(\|\xi-x_k\|_r\le q^k\eta/(1-q)\) for its exact iterates. The executable
checker certifies the center bound; it does not compute an iteration history.

### What each hypothesis contributes

A continuous self-map of a nonempty compact convex box has a fixed point by
the Brouwer fixed-point theorem, even without contraction. Thus the self-map
inequalities alone, with invertible \(Y\), also suffice for existence via that
separate classical theorem. They do not establish uniqueness. The proof above
is a direct constructive proof of our combined criterion and does not require
Brouwer. The executable reports `certified` only for the combined criterion;
it is not a separate existence-only verifier.

Conversely, contraction without a self-map need not give a root in \(B\):
\(F(t)=t-2\), \(B=[-1,1]\), \(Y=1\) gives a constant map \(T(t)=2\) with
Lipschitz constant zero. Nonstrict self-inclusion is deliberate: for
\(F(t)=t-1\) on the same box the root is on the boundary and certification
with \(q=0\) is valid. Strict \(q<1\) is also deliberate: \(F=0\) and
\(Y=1\) give \(q=1\), a self-map, and infinitely many roots.

The derivative bound also forces \(DF(x)\) to be nonsingular at every
\(x\in B\). If \(DF(x)v=0\) for nonzero \(v\), then
\((I-YDF(x))v=v\), contradicting (1)'s matrix bound \(\|v\|_r\le q\|v\|_r\).
This criterion therefore cannot certify a multiple or singular root, even
when that root happens to be locally unique.

## 3. How intervals make the hypotheses computable

For rational intervals \([a,b]\) and \([u,v]\), use

\[
[a,b]+[u,v]=[a+u,b+v],\quad
[a,b][u,v]=[\min(au,av,bu,bv),\max(au,av,bu,bv)].
\]

Negation reverses and negates the endpoints. A nonnegative integer power is
monotone on the real line for odd powers; for positive even powers an
interval crossing zero has lower endpoint zero and upper endpoint
\(\max(a^k,b^k)\). The zeroth power is the constant interval \([1,1]\), also
when the input interval contains zero: this is evaluation of the constant
monomial. These rules enclose all possible point values.

A polynomial is supplied as coefficients and exponent vectors. Differentiate
each monomial exactly. Substitute the coordinate intervals of \(B\) into
those derivative polynomials to form \(J\). Induction over additions,
multiplications and powers proves the enclosure property required above.
Signed multiplication by entries of \(Y\) matters when forming \(A\).

The implementation uses Python's arbitrary size integers and `Fraction` for
every arithmetic endpoint and comparison. It performs no floating arithmetic
in the certificate calculation. Rational endpoints are exact, so no
rounding step is needed: the enclosure is outward by the algebraic interval
rules themselves. Decimal strings such as `"0.1"` and JSON numeric
coefficients are rejected; write `"1/10"`. An approximate decimal can suggest
a rational center, but the proof is for the rational input actually supplied.

Natural interval evaluation may overestimate a range. For example, evaluating
two appearances of the same variable independently loses correlation. This
can cause a false negative. It cannot create an accepted false certificate
provided the interval arithmetic and validation are implemented correctly.
The verifier recomputes the Jacobian enclosure and all bounds; it never
trusts a supplied residual, derivative matrix, or claimed answer.

## 4. Relation to interval Newton, Krawczyk and alpha theory

The mean-value enclosure

\[
K=c-YF(c)+(I-YJ)(B-c)
\]

contains \(T(B)\). This is an interval enclosure, usually larger than the
actual image of the map. Our symmetric estimate uses
\(K\subseteq c-YF(c)+\prod_i[-(Mr)_i,(Mr)_i]\) and checks that latter box
lies in \(B\). This is a conservative sufficient contraction test related to
Krawczyk methods. It is not a claim to implement every interval-Newton or
Krawczyk inclusion theorem. Rump's account gives a mean-value enclosure and
separate strict interior inclusion results; stronger conclusions require
their stated hypotheses, not merely a reference to the word Krawczyk.
[Rump (2010), §13, Theorems 13.1–13.3](https://www.tuhh.de/ti3/paper/rump/Ru10.pdf).

The historical methods are classical: see
[Krawczyk (1969)](https://doi.org/10.1007/BF02234767) and
[Moore (1977)](https://doi.org/10.1137/0714040). Our contribution here is an
educational, inspectable implementation and worked examples, not a new
certification theorem.

With \(DF(c)\) nonsingular, Smale's alpha theory uses an inverse-Jacobian
residual \(\beta=\|DF(c)^{-1}F(c)\|\) and higher derivative control
\(\gamma\). Here the cited formulation uses the Euclidean (Hermitian) norm
on \(\mathbb C^n\) and the specified induced higher-derivative operator norms,
rather than our weighted maximum norm. For a square polynomial system, the standard bound
\(\alpha=\beta\gamma<(13-3\sqrt{17})/4\) certifies quadratic Newton
convergence and distance at most \(2\beta\) to an associated root. Our bound
instead controls one fixed map throughout a specified real box and proves
uniqueness throughout that box; its convergence proof gives a geometric
rate. Alpha theory's association statement by itself is not a global
uniqueness assertion or a uniqueness assertion for an arbitrary input box.
The exact rational mode of `alphaCertified` is rigorous; arbitrary precision
floating arithmetic without controlled rounding is not automatically so.
[Hauenstein–Sottile, Theorem 2 and §4](https://arxiv.org/abs/1011.1091v2).

## 5. A reusable workflow and its limits

1. Write down the exact rational polynomial system you intend to certify.
   Check equation order and variable order; a certificate for a mistyped
   system is still a certificate for the mistyped system.
2. Obtain a candidate center by any method. Numerical root finding is a
   discovery aid and is outside the verifier's trust boundary.
3. Choose positive rational radii and a rational matrix close to the inverse
   Jacobian at the center. Unequal radii also choose the weighted norm.
4. Run the verifier, inspect the recomputed Jacobian intervals, residual step,
   self-map slack and \(q\). Read the error bound only on acceptance.
5. On failure, inspect whether residual scale, derivative variation, interval
   overestimation or singular behavior is the obstruction. A better center,
   smaller box, different scaling or different method may help; no remedy is
   guaranteed. Preserve the rejected output as a diagnostic, not a proof of
   nonexistence.

[EXAMPLES.md](EXAMPLES.md) gives complete arithmetic for two systems and
small-residual failures. [SCHEMA.md](SCHEMA.md) defines the executable input
contract. [VERIFICATION.md](VERIFICATION.md) records tests, review, and trust
limits.

The theorem permits general continuously differentiable maps when their
derivative enclosures are justified. This executable accepts only rational
polynomials, so domain and differentiability are automatic. Transcendental
functions, uncertain coefficients, non-square systems, complex roots,
automated global root enumeration, singular-root methods, certificate search
and continuation are outside this edition. Certification is local to the
closed box; other zeros may occur elsewhere. No finite test suite is a formal
proof of the Python interpreter or this program. Exact arithmetic, the
mathematical proof, source inspection, and adversarial testing play distinct
roles.
