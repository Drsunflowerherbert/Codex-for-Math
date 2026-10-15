# Rank-one critical points of bivariate polynomials

This study gives a complete local classification of a real polynomial at a
stationary point whose Hessian has rank one. The executable procedure accompanying
it uses exact rational arithmetic. The mathematics is classical splitting-lemma
and plane-curve singularity theory; no new theorem is claimed here.

**Verification status.** The arguments below are ordinary mathematical proofs,
with explicit literature checks for the degree bounds. The accompanying program
and regression tests provide computational evidence about its implementation.
Neither the proofs nor the implementation have been verified in Lean or another
proof assistant. No explicit neighborhood radius is asserted.

## 1. Hypotheses and rational normalization

Let

\[
f\in\mathbb R[u,v],\qquad \nabla f(0,0)=0,\qquad
\operatorname{rank}H_f(0,0)=1.
\]

Write \(d=\deg f\); necessarily \(d\geq2\). Local comparisons are with
\(f(0,0)\), so subtracting that constant is essential before discussing the curve
defined by the zero level. A *saddle* here means that every neighborhood of the
origin contains points with values above and below \(f(0,0)\). A *non-strict
minimum* below means a local minimum which is not strict, and similarly for a
maximum.

There is no need to compute eigenvectors or introduce irrational numbers. Write
the Hessian, after interchanging \(u,v\) if needed, as

\[
H=\begin{pmatrix}a&b\\b&c\end{pmatrix},\qquad c\ne0.
\]

Such a nonzero diagonal entry exists: if both diagonal entries vanished, the
rank-one condition \(ac-b^2=0\) would also force \(b=0\). Put

\[
\sigma=\operatorname{sign}(c),\qquad
T(x,y)=\left(x,y-\frac bc x\right),\qquad
F(x,y)=\sigma\bigl(f(T(x,y))-f(0,0)\bigr).
\]

The possible preliminary interchange is part of \(T\). Since \(a=b^2/c\), a
direct matrix multiplication gives

\[
H_F(0)=\begin{pmatrix}0&0\\0&\lambda\end{pmatrix},
\qquad \lambda=\sigma c>0.
\]

The map \(T\) is invertible and preserves degree. For rational input all its
entries, all coefficients of \(F\), and \(\lambda\) are rational. The sign
\(\sigma\) records the sign of the unique nonzero Hessian eigenvalue: the rank-one
matrix has its nonzero eigenvalue of the same sign as any nonzero diagonal
entry. A minimum of \(F\) is a minimum of \(f\) if \(\sigma=1\), and a maximum
of \(f\) if \(\sigma=-1\). Saddles are unchanged by this sign reversal.

## 2. The critical graph and a local splitting, including the zero case

Set \(h=F_y\). Since \(h(0)=0\) and \(h_y(0)=\lambda\ne0\), the real analytic
implicit function theorem supplies a unique analytic germ \(\phi\), with
\(\phi(0)=0\), such that

\[
F_y(x,\phi(x))=0.
\]

Moreover, \(\phi'(0)=-F_{yx}(0)/F_{yy}(0)=0\). Define the analytic residual

\[
g(x)=F(x,\phi(x)).
\]

The chain rule and the normalized Hessian show that
\(g(0)=g'(0)=g''(0)=0\). Thus a nonzero residual has a first term
\(a_mx^m\) with \(m\geq3\).

Taylor's formula in the transverse variable gives an exact local identity:

\[
F(x,\phi(x)+t)=g(x)+t^2 A(x,t),
\qquad
A(x,t)=\int_0^1(1-s)
 F_{yy}(x,\phi(x)+st)\,ds.
\]

Here \(A\) is real analytic and \(A(0,0)=\lambda/2>0\). It is therefore positive
on some neighborhood. The positive analytic square root of \(A\) exists there.
The coordinate change

\[
z=t\sqrt{A(x,t)}
\]

has nonzero derivative in \(t\) at the origin and hence is locally invertible.
Consequently

\[
\boxed{F=g(x)+z^2}
\]

in local real analytic coordinates. This proof does **not** assume an isolated
critical point. In particular, it applies when \(g\equiv0\).

The usual splitting lemma supplies the broader theoretical setting. Theorem 11
of [Marais and Steenpass, version 3, Section 3](https://arxiv.org/pdf/1303.7114v3)
is stated for formal real power series and assumes an isolated singularity.
It also records the signs of the nondegenerate squares. We use the direct
analytic argument above for the non-isolated case, rather than extend that
theorem beyond its stated hypotheses. Their Section 2.2 discusses the Milnor
number and right equivalence; convergence needed for local inequalities follows
here from the analytic implicit function theorem, not merely from a formal
coordinate calculation.

## 3. Complete classification

The following table classifies the original polynomial. For a nonzero residual,
write \(g(x)=a_mx^m+O(x^{m+1})\), \(a_m\ne0\).

| Residual | Positive nonzero Hessian eigenvalue | Negative nonzero Hessian eigenvalue |
| --- | --- | --- |
| \(g\equiv0\) | Non-strict local minimum | Non-strict local maximum |
| \(m\) even and \(a_m>0\) | Strict local minimum | Strict local maximum |
| \(m\) odd | Saddle | Saddle |
| \(m\) even and \(a_m<0\) | Saddle | Saddle |

The residual in this table is always the residual of the **normalized** \(F\),
which includes the factor \(\sigma\).

**Proof.** A nonzero analytic one-variable function has the sign of its first
nonzero term sufficiently near zero. An even positive first term gives
\(g(x)>0\) for all sufficiently small nonzero \(x\). Thus \(g(x)+z^2>0\)
at every nearby point other than the origin. An odd first term gives both signs
along \(z=0\). An even negative first term gives negative values along \(z=0\),
while \(x=0,z\ne0\) gives positive values. These are saddles. If \(g\equiv0\),
then \(F=z^2\geq0\), and every point on \(z=0\) has the same value as the origin,
so the minimum is not strict. Local analytic coordinate changes preserve all
these conclusions; multiplying by \(\sigma\) gives the table. This also proves
that the table is exhaustive. In particular, an analytic rank-one critical
point cannot be a non-strict extremum with a nonzero residual. \(\square\)

When \(g\equiv0\), the original critical graph is a curve of critical points:
\(F_y(x,\phi(x))=0\), and the chain rule gives
\(F_x(x,\phi(x))=g'(x)=0\). Its points have value zero for \(F\).

## 4. Exact coefficient computation

For rational input, the series of \(\phi\) and \(g\) have rational coefficients.
Write

\[
h(x,y)=\lambda y+R(x,y),\qquad
\phi(x)=\sum_{n\geq2}c_nx^n,
\]

where every term of \(R\) has total degree at least two. If
\(p_{n-1}=\sum_{j=2}^{n-1}c_jx^j\), the recurrence is

\[
\boxed{c_n=-\frac{[x^n]h(x,p_{n-1}(x))}{\lambda}},
\qquad n\geq2.
\]

To justify it, insert \(p_{n-1}+c_nx^n\) into \(h\). The only contribution of the
new coefficient to order \(n\) is \(\lambda c_nx^n\). Every other occurrence is
multiplied by a positive-order expression. This determines one coefficient at a
time, with division only by the known nonzero rational \(\lambda\).

For any chosen \(N\), compute \(p_N\) through degree \(N\) and then compute

\[
G_N(x)=F(x,p_N(x))\pmod{x^{N+1}}.
\]

Because \(p_N=\phi+O(x^{N+1})\), substitution into the polynomial shows that
\(G_N=g\pmod{x^{N+1}}\). Thus the first nonzero coefficient found in \(G_N\)
is the exact first coefficient of \(g\). Merely finding a long run of zero
coefficients does not prove identity; the next section supplies the finite
stopping certificate for polynomial input.

## 5. Why a finite degree bound is sufficient

### 5.1 The local Milnor-number calculation

Complexify the normalized polynomial and the analytic implicit graph. Let
\(\mathcal O=\mathbb C\{x,y\}\) denote convergent power-series germs at the
origin. The implicit function theorem also holds holomorphically, and

\[
h(x,y)=U(x,y)(y-\phi(x)),\qquad U(0,0)=\lambda\ne0.
\]

For example, this factorization follows by integrating \(h_y\) between
\(\phi(x)\) and \(y\). The factor \(U\) is a unit. Therefore substitution on the
graph identifies

\[
\mathcal O/(F_y)\simeq\mathbb C\{x\}.
\]

Under this identification \(F_x\) maps to \(g'\), since
\(g'=F_x(x,\phi)+F_y(x,\phi)\phi'=F_x(x,\phi)\). Hence

\[
\boxed{\mathcal O/(F_x,F_y)\simeq\mathbb C\{x\}/(g')}.
\]

If \(g\ne0\) has order \(m\), then \(g'=x^{m-1}V(x)\) for a unit \(V\), so
this quotient has complex dimension \(m-1\). In the usual definition this is
the local complex Milnor number:

\[
\boxed{\mu_0(F)=m-1.}
\]

It is finite, and the complex critical point is isolated: on the unique nearby
graph \(F_y=0\), the equation \(F_x=0\) reduces to \(g'=0\), whose only
sufficiently nearby zero is \(x=0\). Thus the centered curve \(F=0\) has an
isolated singularity at the origin, precisely the local hypothesis needed below.
If \(g\equiv0\), the quotient instead has infinite dimension and the critical
curve is non-isolated. These arguments establish isolation over \(\mathbb C\),
rather than assume that isolation over \(\mathbb R\) would suffice.

### 5.2 A conservative bound, with the global common-factor issue removed

Suppose \(g\ne0\), and put \(P=F_x\), \(Q=F_y\). Both polynomials are nonzero:
\(Q_y(0)=\lambda\), and \(P\equiv0\) would force \(g'\equiv0\) and then
\(g\equiv0\). They have degrees at most \(d-1\).

It is unsafe simply to assert that \(P,Q\) have no global common factor. They
can have a common factor which does not vanish at the origin. Divide out their
global greatest common divisor, writing \(P=DA\), \(Q=DB\), with coprime
\(A,B\in\mathbb C[x,y]\). The local isolation just proved forces \(D(0)\ne0\):
a nonconstant complex factor vanishing at the origin would supply a curve of
common zeros of \(P,Q\) through it. Thus \(D\) is a local unit and

\[
\mu_0(F)=\dim_{\mathbb C}\mathcal O/(A,B)=i_0(A,B).
\]

The globally coprime curves \(A=0\), \(B=0\) satisfy Bézout's theorem. Their
local intersection multiplicity at the origin is at most the total projective
intersection number, so

\[
\boxed{\mu_0(F)\leq \deg A\deg B\leq(d-1)^2.}
\]

No hypothesis that all critical points of \(F\) are globally isolated has been
used. For example, \(F=(1+x)^2(y^2+x^3)\) has Hessian
\(\operatorname{diag}(0,2)\) at the origin. Its critical graph there is
\(\phi=0\), and \(g=(1+x)^2x^3\) has order three, so the origin is an isolated
complex critical point and a real saddle. Nevertheless, both derivatives share
the factor \(1+x\), and the entire distant line \(x=-1\) consists of critical
points. That common factor is a unit at the origin, exactly as the proof allows.

Combining the bound with \(m=\mu_0(F)+1\) gives a conservative cutoff

\[
N_{\mathrm B}(d)=(d-1)^2+1.
\]

If all coefficients of \(g\) through this degree vanish, then \(g\equiv0\):
otherwise its first nonzero degree would simultaneously exceed and be bounded
by \(N_{\mathrm B}(d)\). This contrapositive supplies an identity certificate;
it is not a numerical tolerance test.

### 5.3 Płoski's sharper bound and its exact applicability

[Płoski, version 1, Theorem 1.1, PDF page 2](https://arxiv.org/pdf/1305.5102v1)
assumes a complex polynomial of degree \(d>1\), an isolated singularity of its
zero curve at the origin, and \(\operatorname{ord}_0F<d\). It proves

\[
\mu_0(F)\leq(d-1)^2-\lfloor d/2\rfloor.
\]

For our centered rank-one polynomial \(\operatorname{ord}_0F=2\). When
\(d\geq3\) and \(g\ne0\), Section 5.1 verifies the complex isolation hypothesis,
and \(2<d\) verifies the remaining strict inequality. Thus an optional sharper
cutoff is

\[
\boxed{N_{\mathrm P}(d)=(d-1)^2-\lfloor d/2\rfloor+1,\quad d\geq3.}
\]

For \(d=2\), normalized \(F=\lambda y^2/2\), so \(g\equiv0\) directly; the
strict inequality in Płoski's theorem does not apply. The paper's exceptional
homogeneous concurrent-line case cannot occur for \(d\geq3\) here because the
order is two. Its separate equality-characterization Theorem 1.4 excludes
\(d=4\); that exclusion does **not** occur in Theorem 1.1. Neither bound requires
an irreducible curve or isolated singularities everywhere in the affine or
projective plane. These are upper bounds, not a claim of optimality within every
degree of the rank-one subclass.

## 6. Worked examples and the quartic stress test

For \(F=y^2+x^3\), the graph is \(\phi=0\) and \(g=x^3\), so the origin is a
saddle. For \(F=y^2+x^4\), it is a strict minimum. Reversing the sign of the
whole latter polynomial gives a strict maximum with a negative nonzero Hessian
eigenvalue. For \(F=(y-x^2)^2\), the graph is exactly \(\phi=x^2\) and
\(g\equiv0\), so the minimum is not strict.

A cubic can already hide a fourth-order residual:

\[
F=y^2+x^2y,\qquad \phi=-x^2/2,\qquad g=-x^4/4.
\]

This is a saddle. The graph detects negative values even though the restriction
to \(y=0\) vanishes identically.

The requested quartic family is more demanding. For \(s\in\{1,-1\}\), let

\[
F_s=(y-x^2)^2+s y^4.
\]

Its total degree is four and its Hessian is \(\operatorname{diag}(0,2)\). The
critical-graph equation is

\[
\phi+2s\phi^3=x^2,
\qquad
\phi=x^2-2s x^6+12x^{10}-96s x^{14}+O(x^{18}).
\]

On this graph, \(\phi-x^2=-2s\phi^3\), and hence

\[
g_s=s\phi^4+4\phi^6
    =s x^8-4x^{12}+24s x^{16}+O(x^{20}).
\]

An independent consistency check is
\(g_s'=F_{s,x}(x,\phi)=8s x\phi^3\), which gives the same coefficients.
Thus the plus case is a strict minimum and the minus case is a saddle, with
residual order eight in both cases. Their local complex Milnor number is seven.
This attains the sharper quartic cutoff \(N_{\mathrm P}(4)=8\) and shows why
checking only through the polynomial's own degree is incomplete. In the plus
case, positivity also follows immediately from the original sum of squares;
this provides a separate check of that classification.

## 7. Completeness and representation limits

The classification theorem holds for real analytic germs with rank-one Hessian,
but a general analytic germ has no degree parameter supplying either cutoff.
A first nonzero residual coefficient, when found, still settles the result.
An arbitrarily long finite zero jet alone does not decide identity for arbitrary
analytic input: \(y^2\) and \(y^2\pm x^{2k}\) agree to any prescribed lower
finite order when \(k\) is large enough.

For smooth inputs, even the entire Taylor series need not determine the answer.
Let \(q(0)=0\) and \(q(x)=\exp(-1/x^2)\) for \(x\ne0\). The three smooth
functions \(y^2+q(x)\), \(y^2-q(x)\), and \(y^2\) have the same Taylor series
at the origin and the same rank-one Hessian. They have, respectively, a strict
minimum, a saddle, and a non-strict minimum. This is why flat smooth functions
must not be treated as zero analytic residuals by a Taylor-series procedure.

The finite exact algorithm has a complete representation contract for
\(\mathbb Q[u,v]\): finitely many monomials, integer exponents, and exact rational
coefficients. Equality, Hessian rank, coefficient signs, and divisions are then
decidable exactly. The same reasoning can extend to exactly represented real
algebraic coefficients with exact sign and equality operations. It does not
provide a uniform exact classifier for unspecified arbitrary real coefficients,
floating-point approximations, or arbitrary black-box analytic functions.

Finally, the conclusions are local at the given stationary point. The existence
proofs supply some sufficiently small neighborhood, but computing a certified
radius would require additional bounds or real-algebraic certification and is
outside this first edition.
