# Finite-field product-sum mixing

## 0. Result, provenance, and scope

**Four products suffice in the local argument under study.** Let $p$ be prime,

\[
H\subseteq\mathbb F_p,\qquad h=|H|\ge p^{3/4},
\]

and let $X_1,Y_1,\ldots,X_4,Y_4$ be independent uniform samples from $H$.
For every $t\in\mathbb F_p$,

\[
\Pr\!\left(\sum_{i=1}^4X_iY_i=t\right)
\ge {1\over p}\left(1-{(p-1)p^2\over h^4}\right)
\ge {1\over p^2}>0. \tag{0.1}
\]

Consequently every residue is a sum of four products from $H$, with
repetition allowed. This is a direct specialization of a classical bilinear
character bound and finite Fourier inversion, not a novelty claim.

The motivating source is the proof of `lem:rational-divisor-supply` in
OpenAI/math, family025, *Short Egyptian fractions*, specifically
`build/prescribed.tex`, lines 326–366, pinned to revision
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`:

- [Pinned source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/build/prescribed.tex#L326-L366)
- The complete local source has SHA-256
  `771d9da7e0181aad85eb620d4bacbb1726827db86249655850f0b63b20307432`,
  matching the catalog manifest.
- The source itself attributes the bilinear estimate to A. A. Glibichuk and
  S. V. Konyagin, *Additive properties of product sets in fields of prime
  order*, Proposition 1.1. Its statement was checked on page 2 of the
  [primary arXiv manuscript](https://arxiv.org/pdf/math/0702729).
- The same page notes a known three-product covering result under
  `|H| > p^(3/4) + 1`. The four-product result here is not asserted optimal.

The source chooses five independent products when $h>p^{3/4}$. Retaining
the exact number $p-1$ of nonzero frequencies shows that four already give
a positive margin. In the subsequent positive-divisor lift this saves one
rational summand per lifted prime: four instead of five. This study does
not propagate that saving into a global short-Egyptian-fraction constant,
alter the manuscript, or certify its separate prime-supply, asymptotic,
grouping, distinctness, or padding arguments.

All statements below have ordinary mathematical proofs. The computations
use original Python and exact integer/rational arithmetic. No Lean build,
kernel verification, native MRS import, or external peer-review status is
claimed. The portable theorem records are study data, not a native MRS
schema.

## 1. Conventions and finite probability spaces

Throughout, $p\ge2$ is prime. Identify $\mathbb F_p$ with residues modulo
$p$ when defining

\[
e_p(x)=\exp(2\pi i\widetilde x/p),
\]

where $\widetilde x$ is any integer representative. The value is independent
of the representative, and

\[
e_p(x+y)=e_p(x)e_p(y),\qquad
\overline{e_p(x)}=e_p(-x),\qquad |e_p(x)|=1.
\]

For nonempty subsets $A,B\subseteq\mathbb F_p$, put

\[
a=|A|,\quad b=|B|,\quad N=ab.
\]

The product random variable $U=XY$ means that $(X,Y)$ is uniform on the
Cartesian product $A\times B$. In particular $X,Y$ are independent and
each is uniform on its own set. The distribution of $U$ need not be
uniform on the product set $AB$.

For multiple pairs, the convenient probability space is

\[
\Omega=\prod_{i=1}^k(A_i\times B_i),\qquad
\Pr(\{\omega\})={1\over M},\quad
M=\prod_{i=1}^k |A_i||B_i|,
\]

with $k\ge1$. Thus all $2k$ coordinates are mutually independent.
The proofs only need independence inside each pair and independence of
the resulting $k$ products. Samples may repeat, zero may belong to a
set, and no multiplicative-subgroup condition is imposed.

For a field-valued random variable $Z$, use the characteristic-function
normalization

\[
\widehat\mu_Z(r)=\mathbb E\,e_p(rZ).
\]

This has $\widehat\mu_Z(0)=1$; the inverse formula has the factor $1/p$.

## 2. Additive-character orthogonality

**Lemma FF001.** For $d\in\mathbb F_p$,

\[
\sum_{x\in\mathbb F_p}e_p(dx)
=\begin{cases}p,&d=0,\\0,&d\ne0.\end{cases} \tag{2.1}
\]

**Proof.** For $d=0$, every summand is 1. For $d\ne0$, let
$z=e_p(d)$. Then $z^p=1$, $z\ne1$, and

\[
(1-z)\sum_{j=0}^{p-1}z^j=1-z^p=0.
\]

Since $1-z\ne0$, the sum is zero. This also proves

\[
\mathbf1_{\{z=t\}}
={1\over p}\sum_{r\in\mathbb F_p}e_p(r(z-t)) \tag{2.2}
\]

for every $z,t\in\mathbb F_p$. There is no limit or convergence issue.
□

Orthogonality itself holds in cyclic groups of composite order. What will
fail there is the inference that $r(b-b')\ne0$ whenever both factors are
nonzero. Section 8 gives a concrete failure of the full theorem in a
composite residue ring.

## 3. The rectangular bilinear character estimate

**Lemma FF002.** Let $A,B\subseteq\mathbb F_p$ be nonempty and
$r\in\mathbb F_p\setminus\{0\}$. Then

\[
\left|\sum_{x\in A}\sum_{y\in B}e_p(rxy)\right|
\le\sqrt{pab}. \tag{3.1}
\]

Consequently, for independent uniform $X\in A,Y\in B$,

\[
|\widehat\mu_{XY}(r)|\le\sqrt{p\over ab}. \tag{3.2}
\]

One may replace the right side of (3.2) by
$\min\{1,\sqrt{p/(ab)}\}$, using the triangle inequality for expectation.
We retain (3.2) for the clean cardinality criterion below.

**Proof.** Write

\[
T_x=\sum_{y\in B}e_p(rxy),\qquad S=\sum_{x\in A}T_x.
\]

Complex Cauchy–Schwarz and nonnegativity of squared moduli give

\[
|S|^2\le a\sum_{x\in A}|T_x|^2
\le a\sum_{x\in\mathbb F_p}|T_x|^2. \tag{3.3}
\]

Expanding the finite sum and using (2.1),

\[
\begin{aligned}
\sum_{x\in\mathbb F_p}|T_x|^2
&=\sum_{y,y'\in B}\sum_{x\in\mathbb F_p}e_p(rx(y-y'))\\
&=pb.
\end{aligned} \tag{3.4}
\]

Indeed, the $b$ diagonal pairs contribute $p$ each. For $y\ne y'$,
the prime-field property and $r\ne0$ give $r(y-y')\ne0$, so the inner
sum vanishes. Equations (3.3)–(3.4) yield $|S|^2\le pab$.
The expectation is $S/(ab)$; division by $a^2b^2$ gives (3.2).
□

For $A=B=H$, this becomes

\[
|\widehat\mu_{XY}(r)|\le {\sqrt p\over h}. \tag{3.5}
\]

### An exact algebraic witness for the Cauchy–Schwarz step

If the elements of $A$ are given any ordering, then

\[
pab-|S|^2
=a\sum_{x\notin A}|T_x|^2
 +\sum_{x<x',\ x,x'\in A}|T_x-T_{x'}|^2. \tag{3.6}
\]

To verify it, expand the second sum as
$a\sum_{x\in A}|T_x|^2-|\sum_{x\in A}T_x|^2$, then apply (3.4).
Every term on the right is nonnegative. The exact test program verifies
this identity in $\mathbb Z[z]/(1+z+\cdots+z^{p-1})$ for small primes,
with conjugation represented by $z\mapsto z^{-1}$. This checks a finite
collection of algebraic identities, not the universal theorem by itself.

## 4. Fourier inversion and finite product-sum mixing

**Lemma FF003.** For every field-valued random variable $Z$ on a finite
probability space and every $t\in\mathbb F_p$,

\[
\Pr(Z=t)={1\over p}\sum_{r\in\mathbb F_p}
 e_p(-rt)\widehat\mu_Z(r). \tag{4.1}
\]

**Proof.** Take expectations of (2.2), with $z=Z$. Interchanging the
finite sum and expectation is exact. □

**Theorem FF004.** Suppose $U_1,\ldots,U_k$ are independent
$\mathbb F_p$-valued random variables and, for every $r\ne0$,

\[
|\widehat\mu_{U_i}(r)|\le\beta_i\quad(1\le i\le k).
\]

Then, for every $t\in\mathbb F_p$,

\[
\left|\Pr(U_1+\cdots+U_k=t)-{1\over p}\right|
\le {p-1\over p}\prod_{i=1}^k\beta_i. \tag{4.2}
\]

In particular, if $ (p-1)\prod_i\beta_i<1$, every residue has strictly
positive probability.

**Proof.** Independence gives

\[
\begin{aligned}
\mathbb E\,e_p\!\left(r\sum_iU_i\right)
&=\mathbb E\prod_i e_p(rU_i)\\
&=\prod_i\mathbb E\,e_p(rU_i).
\end{aligned}
\]

The factorization can also be checked directly by expanding the finite
product probability measure. Separate the $r=0$ term in (4.1):

\[
\Pr\!\left(\sum_iU_i=t\right)-{1\over p}
={1\over p}\sum_{r\ne0} e_p(-rt)
   \prod_i\widehat\mu_{U_i}(r).
\]

There are exactly $p-1$ terms, $|e_p(-rt)|=1$, and the triangle
inequality proves (4.2). The left side is real before the absolute value;
we do not compare possibly complex individual Fourier coefficients with
real numbers. The lower bound

\[
\Pr\!\left(\sum_iU_i=t\right)
\ge {1-(p-1)\prod_i\beta_i\over p}
\]

is positive under the stated condition. □

### Different sets, nonzero coefficients, and a shift

**Theorem FF005.** Let $A_i,B_i\subseteq\mathbb F_p$ be nonempty,
$c_i\in\mathbb F_p\setminus\{0\}$, and $d\in\mathbb F_p$. Uniformly
sample the Cartesian product $\Omega$ in Section 1. With

\[
Z=d+\sum_{i=1}^k c_iX_iY_i,
\qquad M=\prod_i|A_i||B_i|,
\]

one has, for every $t\in\mathbb F_p$,

\[
\left|\Pr(Z=t)-{1\over p}\right|
\le {p-1\over p}\sqrt{p^k\over M}. \tag{4.3}
\]

Every residue occurs if

\[
M>(p-1)^2p^k. \tag{4.4}
\]

**Proof.** At frequency $r\ne0$, the $i$-th product is tested at the
nonzero frequency $rc_i$. Apply FF002 to each pair, multiply the bounds,
and apply FF004. The shift multiplies the Fourier transform by a unit
complex number and has no effect on its modulus. Since both sides are
nonnegative, squaring the strict condition
$(p-1)\sqrt{p^k/M}<1$ gives exactly (4.4). □

If some coefficient is zero, remove that summand and use the effective
number of nonzero summands and their corresponding sets. Arbitrary zero
coefficients cannot be retained while using (4.4).

## 5. The requested k-product criterion and exact counts

**Corollary FF006.** For fixed nonempty $A,B\subseteq\mathbb F_p$, put
$N=|A||B|$. Every residue is a sum of $k$ products $x_i y_i$, with
$x_i\in A,y_i\in B$, if

\[
(p-1)\left(\sqrt{p\over N}\right)^k<1. \tag{5.1}
\]

For $A=B=H$, this is precisely

\[
\boxed{\ (p-1)\left({\sqrt p\over h}\right)^k<1\ }. \tag{5.2}
\]

**Proof.** In FF005 take all $A_i=A$, all $B_i=B$, all $c_i=1$,
and $d=0$. □

The radical-free form of (5.1) is

\[
N^k>(p-1)^2p^k; \tag{5.3}
\]

the diagonal form is $h^{2k}>(p-1)^2p^k$. These are exactly equivalent
to the displayed sufficient criterion, not necessary conditions for
actual covering. When $h>\sqrt p$, (5.2) is also equivalent to

\[
k>{\log(p-1)\over\log(h/\sqrt p)}.
\]

This is a descriptive formula only; the test program uses (5.3), avoiding
floating-point errors at strict boundaries.

**Corollary FF007 (count form).** In the setting of FF005, let $C_t$ be
the number of tuples in $\Omega$ for which $Z=t$. Then

\[
\sum_t C_t=M,\qquad
|pC_t-M|\le(p-1)p^{k/2}\sqrt M, \tag{5.4}
\]

and therefore

\[
(pC_t-M)^2\le(p-1)^2p^kM. \tag{5.5}
\]

**Proof.** Each tuple has probability $1/M$, so $\Pr(Z=t)=C_t/M$.
Multiply (4.3) by $pM$, then square nonnegative quantities. The tuples
partition according to $t$, giving the sum identity. □

When (4.4) holds, the right side of (5.4) is strictly smaller than $M$,
so $pC_t>0$ and hence $C_t\ge1$. This is a fully finite existence
argument. It does not assert that a random search will find a witness in
one trial.

## 6. Why four works, including the endpoint

**Corollary FF008.** Let $A,B\subseteq\mathbb F_p$ be nonempty and
$N=|A||B|$. If

\[
N^2\ge p^3,
\]

then for four independent products and every residue $t$,

\[
\Pr\!\left(\sum_{i=1}^4X_iY_i=t\right)
\ge {1\over p}\left(1-{(p-1)p^2\over N^2}\right)
\ge {1\over p^2}. \tag{6.1}
\]

Equivalently their representation counts satisfy $C_t\ge N^4/p^2$.
In particular the conclusion holds for $A=B=H$ whenever
$h\ge p^{3/4}$, equivalently $h^4\ge p^3$.

**Proof.** Four powers of the rectangular bound give
$\beta^4=p^2/N^2\le1/p$. Thus

\[
(p-1)\beta^4\le {p-1\over p}=1-{1\over p}<1.
\]

Insert this into FF004. The probability bound and the count bound follow.
□

The criterion actually needs only

\[
N^2>(p-1)p^2,
\quad\text{or in the diagonal case}\quad
h^4>(p-1)p^2. \tag{6.2}
\]

This is slightly weaker than the density assumption used in the source.
The distinction between $h\ge p^{3/4}$ and $h>p^{3/4}$ does not yield
an additional integer case: equality would give $h^4=p^3$, impossible
for a prime $p$, since the exponent of $p$ in a fourth power is a
multiple of 4. Nevertheless the non-strict hypothesis is valid and shows
why no extra fifth product is required.

More generally, if $h\ge p^{1/2+\varepsilon}$, $\varepsilon>0$, and
$k\varepsilon\ge1$, the same proof gives a lower probability $1/p^2$.
At $\varepsilon=1/4$, the integer $k=4$ already meets the condition.
This is an immediate density corollary, not an optimal additive-basis
theorem.

## 7. Positive-divisor lifting and the strictly local saving

**Lemma FF009.** Let $Q$ be a positive integer and let $D$ be a
nonempty set of positive divisors of $Q$. Write $H$ for the image of
$D$ in $\mathbb F_p$. If there are $x_i,y_i\in H$, $1\le i\le k$,
with

\[
\sum_{i=1}^k x_iy_i=0\quad\text{in }\mathbb F_p,
\]

then there exist positive divisors $e_1,\ldots,e_k$ of $Q^2$ and a
positive integer $t$ such that

\[
p=\sum_{i=1}^k{e_i\over t}. \tag{7.1}
\]

**Proof.** Choose positive lifts $a_i,b_i\in D$ of $x_i,y_i$. Put
$e_i=a_ib_i$. Since $a_i,b_i\mid Q$,

\[
{Q^2\over e_i}=\left({Q\over a_i}\right)
                       \left({Q\over b_i}\right)\in\mathbb Z_{>0},
\]

so $e_i\mid Q^2$. The congruence says that $p\mid\sum_i e_i$.
The sum is strictly positive because all lifts are positive. Hence

\[
t={\sum_i e_i\over p}\in\mathbb Z_{>0},
\]

and division yields (7.1). Repetition causes no difficulty. □

**Corollary FF010 (local four-summand prime lift).** In FF009, if
$|H|^4\ge p^3$, one may take $k=4$. This follows by applying FF008 to
residue zero and then FF009.

For the motivating passage, $Q=P(u)$, $D$ is its set of positive
divisors, $H=A_p$, and the nonexceptional-prime hypothesis gives
$|H|>p^{3/4}$. FF008 supplies the zero-sum with **four** pairs. FF009
therefore uses four positive rational summands with the same common
positive integer denominator $t$.

The local audit checks exactly these interfaces:

1. The source samples residues uniformly from the image $H$, not from
   an unequal-multiplicity list of divisors. The proof matches this.
2. Positive lifts exist by the definition of $H$. Zero residues are
   permitted and still have positive integer lifts in $D$.
3. Every lifted product divides $P(u)^2$, with no squarefree assumption
   needed for the divisibility argument.
4. A positive multiple of $p$ produces a positive integer multiplier;
   there is no upper bound on that multiplier in the local step.
5. The source allows repeated rational summands. The probabilistic
   witness has no distinctness requirement.

Thus the only claimed quantitative change is **one fewer rational summand
per prime lifted: five to four, a 20% reduction at that local step**.
It also uses eight factor slots instead of ten. No combined prime-triple,
even-case, final unit-fraction length, or global asymptotic constant is
asserted here.

### Exact illustration with a nontrivial multiplier

Take $Q=30$, whose positive divisors have image
$H=\{1,2,3,5,6\}$ modulo 7. The size condition holds since
$5^4=625\ge7^3=343$. The four factor pairs

\[
(1,1),\ (1,1),\ (1,2),\ (2,5)
\]

give products $1,1,2,10$, all dividing $30^2$, with sum $14$.
The multiplier is $t=2$, and

\[
7={1\over2}+{1\over2}+{2\over2}+{10\over2}.
\]

This illustrates the rational-divisor interface, not a distinct unit-
fraction decomposition.

## 8. Hypothesis boundaries and counterexamples

Each arithmetic example below is asserted in `verify.py` and recorded in
`certificates.json`. More detail appears in `counterexamples.md`.

### The field property cannot be replaced by a composite residue ring

In $\mathbb Z/16\mathbb Z$, take
$H=\{0,2,4,6,8,10,12,14\}$. Then $h=8=16^{3/4}$. Every product is
divisible by 4, so sums of four products miss twelve residues. Yet the
formally substituted error factor is $15/16<1$. At nonzero frequency
$r=4$, every character $e_{16}(rab)$ equals 1, violating the claimed
field bound $\sqrt{16}/8=1/2$.

### Uniform marginals do not replace independence inside each pair

In $\mathbb F_5$, let $H=\mathbb F_5^*$, choose $X$ uniformly, and
set $Y=X^{-1}$. Both marginals are uniform on the four-element set,
which satisfies $4^4\ge5^3$. But $XY=1$ always. Four independent
copies of this dependent pair sum only to $4$.

### Independence between products is also used

In $\mathbb F_2$, let $X,Y$ be independent uniform samples from the
whole field and use $U_i=XY$ for every $1\le i\le4$. Each individual
product has exactly the correct marginal distribution, but their sum is
$4XY=0$. Residue 1 is missed.

### Cardinality alone does not bound nonuniform characteristic functions

In $\mathbb F_5$, let independent $X,Y$ each assign probability
$9/10$ to 0 and $1/40$ to each other residue. The support is the whole
field, but $XY$ has mass $99/100$ at 0 and $1/400$ at each nonzero
residue. For every nonzero frequency,

\[
\widehat\mu_{XY}(r)={99\over100}-{1\over400}={79\over80},
\]

which exceeds $1/\sqrt5$. This refutes the uniform-cardinality
probability bound, **not** qualitative covering: full positive support
gives the same possible tuples as uniform sampling. In general any
full-support choice of positive weights on the same Cartesian product
preserves existence of witnesses, although it changes their probabilities.

### Strict positivity cannot be inferred from a zero lower bound

For $p=2$, $A=\{0\}$, $B=\mathbb F_2$, and any $k\ge1$, one has
$(p-1)(\sqrt{p/(|A||B|)})^k=1$. Every product and sum is zero.
Thus replacing the strict criterion by “$\le1$” is false in general.
This does not affect FF008, whose factor is at most $(p-1)/p<1$.

### The sufficient criterion is not necessary, and small sets can fail

For $H=\{0,1\}\subseteq\mathbb F_5$, four products cover all residues:
each product can be 0 or 1, and the four-product counts are
$(81,108,54,12,1)$. The sufficient criterion fails. For the same set
in $\mathbb F_7$, the counts are $(81,108,54,12,1,0,0)$; residues
5 and 6 are absent. No size-free four-product theorem follows.

### Other omitted hypotheses

- Nonemptiness is required to define a uniform sample. Empty sets also
  make covering impossible.
- The frequency $r=0$ has characteristic value 1. The nontrivial bound
  need not hold there: with $H=\mathbb F_2$, $1>1/\sqrt2$.
- Nonzero coefficients are essential if all summands are counted in the
  threshold. Setting every coefficient to zero gives a constant sum,
  even if all sets are the whole field.
- Repetition is allowed. Requiring all four product values to be distinct
  is already impossible in $\mathbb F_2$, although its whole field meets
  the density hypothesis.
- Strictly positive integer lifts matter for the positive denominator.
  If only zero lifts were allowed, their sum would be zero and the
  proposed multiplier would not be positive. The source provides
  positive divisors, so this obstruction is absent there.

## 9. Exact computational evidence and reproducibility

Run from any directory:

```sh
python finite-field-mixing/verify.py
```

The default full suite uses only standard-library integers and
`fractions.Fraction`. It performs:

1. Exhaustive enumeration of every nonempty $H\subseteq\mathbb F_p$
   for $p=2,3,5,7,11,13,17$, with $k=1,\ldots,6$.
2. Exhaustive enumeration of every ordered pair of nonempty sets $A,B$
   for $p=2,3,5,7$, with the same six values of $k$.
3. Exact checks of (5.5), total tuple counts, and positive coverage
   whenever the strict integer criterion holds.
4. Exact checks of $p^2C_t\ge N^4$ for every tested four-product case
   satisfying $N^2\ge p^3$.
5. Exhaustive ordered sequences of two and three possibly different
   rectangular pairs over $\mathbb F_3$, checking FF005 in count form.
6. Exact symbolic sum-of-squares identities (3.6) for every nonempty
   pair $A,B$, every nonzero $r$, and $p=2,3,5$.
7. Independent direct tuple enumeration cross-checks for selected cases,
   counterexamples, a positive-divisor lift, and exact size thresholds.
8. Every nonzero coefficient vector and additive shift for selected
   three-pair examples over $\mathbb F_2$, $\mathbb F_3$, and $\mathbb F_5$.

The distribution counts are generated by finite convolution. If

\[
q(s)=|\{(a,b)\in A\times B:ab=s\}|,
\]

then $C_0(0)=1$, $C_0(t)=0$ otherwise, and

\[
C_{j+1}(t)=\sum_{s\in\mathbb F_p} C_j(t-s)q(s).
\]

This recurrence counts tuples directly. It uses neither numerical
complex exponentials nor approximate square roots. Strict thresholds
use integer powers. The source hash is checked against the pinned
manifest before a report is written.

See `certificates.json` for run results, sample counts, thresholds,
minimum four-product counts by set size, program hash, and explicit
counterexamples. The finite checks are regression evidence; the proofs
in Sections 2–7 establish the universal statements.

## 10. Portable theorem records and reuse

`theorems.json` records hypotheses, conclusions, dependencies, proof
locations, source connections, and verification limits for FF001–FF010.
The logical spine is:

\[
\text{orthogonality}
\Longrightarrow\text{bilinear bound},\qquad
\text{orthogonality}\Longrightarrow\text{Fourier inversion},
\]

\[
\text{independence + inversion + bilinear bound}
\Longrightarrow\text{product-sum mixing}
\Longrightarrow\text{four-product covering}
\Longrightarrow\text{local positive-divisor lift}.
\]

For reuse, check: prime modulus; nonempty sets; independent uniform
sampling for the stated quantitative bounds; nonzero coefficients if
present; the exact strict threshold; and whether the receiving argument
allows repetitions and positive rational summands. Distinct unit
fractions and global denominator-length bounds are separate interfaces.
