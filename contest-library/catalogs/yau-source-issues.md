# Editorial observations on Yau source statements

**Spoilers:** this separate file contains counterexamples. These are editorial
observations, not an official errata sheet. Original assumptions and numbering
remain in the [official written archive](https://yau-contest.com/index/reldown?en=1&id=9),
linked from the [official Downloads page](https://yau-contest.com/en/lists-jxxg.html).
The exact member, source page and PDF hash for each paper are in
[yau-analysis.json](yau-analysis.json). Only the listed issues were checked;
an unflagged entry is not certified free of defects. No repaired problem statement
is substituted in the catalog.

## yau-source-2010-individual-p5

2010 individual Analysis P5, PDF page 1; member
`2010-2026历年笔试真题/2010/Analysis and differential equations individual.pdf`.

An integrable kernel alone does not ensure that its integral operator sends
continuous functions to continuous functions. With
$K(x,y)=\mathbf 1_{[0,1/2)}(x)$ and $f(y)=1$, the kernel is in
$L^1([0,1]^2)$ but
$Tf(x)=\int_0^1K(x,y)f(y)\,dy=\mathbf 1_{[0,1/2)}(x)$.
This has no continuous representative. Thus the printed assumptions do not
ensure the claimed continuity or subsequent compactness in $C([0,1])$.

## yau-source-2014-team-p3

2014 team Analysis P3, PDF page 1; member
`2010-2026历年笔试真题/2014/analysis2014(team).pdf`.

Under the usual single-valued interpretation, the asserted factorization of a
bounded analytic function on $r<|z|<R$ as $z^\alpha f(z)$, with $f$ analytic
on $|z|<R$, fails. Choose $0<r<R<\infty$ and $F(z)=e^{1/z}$.
Its absolute value is bounded by $e^{1/r}$ on the annulus. A single-valued
$z^\alpha$ around the annulus requires integer $\alpha$ wherever $f\ne0$,
so such a product has at worst a finite-order pole at zero. The chosen function
has an essential singularity there. No alternative multivalued convention is
silently imposed on the original question.

## yau-source-2015-team-p5

2015 team Analysis P5, PDF page 1; member
`2010-2026历年笔试真题/2015/team-analysis2015.pdf`.

The printed boundedness assumption on $T:H_1\to H_2$ and compactness of
$S:H_1\to H_2$ do not ensure a finite-dimensional cokernel for $T+S$.
Take $H_1=H_2=\ell^2$ and $T=S=0$. The zero operator is compact, while
$H_2/\operatorname{Im}(T+S)=\ell^2$ is infinite-dimensional.

## yau-source-2015-team-p6

2015 team Analysis P6(2), PDF page 1; same member as P5 above.

Uniformly bounded $L^2$ norms of harmonic functions on a bounded smooth domain
do not ensure an $L^2$-convergent subsequence on the whole domain. On the unit
disk, the real harmonic polynomials

$$
h_n(r,\theta)=\sqrt{\frac{2(n+1)}{\pi}}\,r^n\cos(n\theta),\qquad n\ge1,
$$

are smooth on its closure. Polar integration gives $\|h_n\|_2=1$ and
$\langle h_n,h_m\rangle=0$ for $n\ne m$. Thus
$\|h_n-h_m\|_2=\sqrt2$, which rules out every norm-convergent subsequence.
Convergence on strict interior subdomains would be a different assertion.

## yau-source-2016-team-p4

2016 team Analysis P4, PDF page 1 of the first Analysis section; member
`2010-2026历年笔试真题/2016/2016-team.pdf`.

For $T^2=\mathbb C/(\mathbb Z+i\mathbb Z)$, every translation
$[z]\mapsto[z+c]$ is a holomorphic automorphism. Distinct $c$ modulo the
lattice give uncountably many maps. Consequently the countable group
$SL(2,\mathbb Z)$ cannot be the full holomorphic automorphism group claimed
in the source. A mapping-class group or a group fixing the origin is a different
object; neither is substituted for the printed question.

## yau-source-2016-team-p5

2016 team Analysis P5, PDF page 1 of the first Analysis section; same member
as P4 above.

The definition $Ae_1=0$, $Ae_n=e_{n-1}/(n-1)$ for $n>1$ already gives the
nonzero eigenvector $e_1$ with eigenvalue zero. Thus the printed statement that
$A$ has no eigenvectors fails as written, independently of its later spectral
question.

## yau-source-2021-main-p4

2021 main Analysis P4, PDF page 1; member
`2010-2026历年笔试真题/2021/ExamPaper_21S/analysis_and_differential_21s.pdf`.

Under the standard convention that the zero polynomial is a polynomial, the
claim about infinitely many solutions of $e^z=P(z)$ needs an exclusion.
For $P\equiv0$ there are no solutions, since the exponential never vanishes.
This observation addresses that boundary case rather than the nonzero-polynomial
argument in the official solution.

## yau-source-2022-main-p2

2022 main Analysis P2, PDF page 1; member
`2010-2026历年笔试真题/2022/ExamPaper_2022/analysis_and_differential_22s.pdf`.

A nonempty open set need not be connected. Let
$U=D(0,1)\cup D(3,1)$, define $f(z)=z$ on the first disk and $f(z)=0$ on
the second. This defines a nonconstant holomorphic map $f:U\to U$ satisfying
$f\circ f=f$, under the printed assumptions. It is not the identity on the
second disk. The identity conclusion therefore requires an additional connectedness
or component-wise nonconstancy qualification; no such repair is made in the index.

## yau-source-2025-main-p4

2025 main Analysis P4, PDF pages 1–2; member
`2010-2026历年笔试真题/2025/analysis.pdf`.

The stated smooth closed-curve hypotheses allow a curve through the origin,
where the displayed differential form
$(x\,dy-y\,dx)/(x^2+y^2)$ is undefined. For example,
$\gamma(s)=(1+\cos(2\pi s),\sin(2\pi s))$ has continuously differentiable
coordinates and derivative magnitude $2\pi$, but $\gamma(1/2)=(0,0)$.
Avoidance of the origin is needed to define the form along the whole curve.
This does not settle how the remaining regular-homotopy assertion should be repaired.

## Source notation clarification: 2018 individual Problem 4

Independent visual inspection confirmed that the original formula uses the
**closed ball**, with an overbar. Text extraction lost that overbar. An initial
open-ball counterexample was discarded before publication; this problem has no
source-defect flag on that basis. The rendered original notation controls.
This clarification is not an official erratum.

The three original full solution attempts concern 2014 individual P1, 2019
individual P1 and 2023 main P4. None is among the flagged issues above. Their
conditions were separately checked against rendered source pages. These source
observations are limited integrity checks rather than further solved-problem batches.
