# Invariant complements as a computable extension obstruction

**Status and scope.** The extension classification, Sylvester criterion,
trace duality, Bézout argument, and Smith-form consequences below are classical
mathematics. The organization, connecting derivations, and worked examples are
original exposition, with no claim of research novelty. This chapter builds on
the operator-module translation in Chapter 2 and the cyclic extension
construction in Chapter 6. It supplies the missing machinery for an actual
invariant-complement problem: compute the obstruction, exhibit a certificate
when it is nonzero, construct a complement when it vanishes, and determine how
a nonzero obstruction joins cyclic blocks. Every main claim is proved below;
no new textbook proof-comparison claim is made here.

Throughout, $k$ is a field and $R=k[t]$. Let $U,W$ be finite-dimensional
$k$-spaces, with operators $A:U\to U$ and $B:W\to W$. Write $U_A,W_B$
for the corresponding $R$-modules. Several arguments work without finite
dimension; those extensions are identified explicitly. Matrices act on column
vectors, and $J_n(0)$ has ones on the **superdiagonal**.

## 1. The datum an invariant-subspace problem actually contains

Suppose an operator $T$ on $E$ preserves a specified subspace $U$. Its
restriction is $A$; its induced operator on $W=E/U$ is $B$. This gives
an exact sequence with specified endpoint identifications:

$$0\longrightarrow U_A\xrightarrow{i}E_T\xrightarrow{q}W_B
\longrightarrow0.\tag{1}$$

A $k$-linear section $s:W\to E$ exists because $k$ is a field. The map
$(u,w)\mapsto i(u)+s(w)$ identifies the underlying vector space with
$U\oplus W$. The defect of $s$ from being an $R$-linear map is

$$Ts(w)-s(Bw)=i(Cw),$$

for a unique $k$-linear map $C:W\to U$. Thus

$$T_C=\begin{pmatrix}A&C\\0&B\end{pmatrix}.\tag{2}$$

Every $C$ gives an extension, but $C$ depends on the chosen section.
Put

$$H=\operatorname{Hom}_k(W,U),\qquad
\delta_{A,B}:H\longrightarrow H,\quad \delta(h)=Ah-hB.\tag{3}$$

Replace $s$ by $s+i h$. Direct substitution gives

$$C\longmapsto C+Ah-hB=C+\delta(h).\tag{4}$$

Equivalently, with $P_h=\begin{pmatrix}1&h\\0&1\end{pmatrix}$,

$$P_h^{-1}T_CP_h=T_{C+\delta(h)}.\tag{5}$$

This conjugacy fixes the embedded $U$ and induces the identity on the
quotient $W$. It is much more restricted than arbitrary similarity.

For clarity about signs, an extension isomorphism written in the *direction*
$F_h:E_C\to E_D$, $F_h(u,w)=(u+hw,w)$, satisfies

$$F_hT_C=T_DF_h\quad\Longleftrightarrow\quad D=C-\delta(h).\tag{6}$$

There is no discrepancy between (4) and (6): $P_h$ maps the new coordinate
model to the old one. Both say that equivalent extensions have the same class
in $H/\delta H$.

### Complements, sections, and the solution set

Any vector-space complement to $U\oplus0$ is the graph

$$\Gamma_h=\{(hw,w):w\in W\}$$

of a unique $h\in H$: the quotient projection restricts to an isomorphism
from the complement to $W$. Applying $T_C$ to a graph vector shows

$$T_C(hw,w)=(Ahw+Cw,Bw)\in\Gamma_h
\quad\Longleftrightarrow\quad Ah-hB=-C.\tag{7}$$

Consequently the following are equivalent:

1. $U$ has a $T_C$-invariant complement;
2. (1) admits an $R$-linear section;
3. the Sylvester equation $\delta(h)=-C$ has a solution;
4. $[C]=0$ in $H/\delta H$.

If $h_0$ is one solution, every solution is

$$h_0+f,\qquad f\in\ker\delta
=\operatorname{Hom}_R(W_B,U_A).\tag{8}$$

The set of invariant complements is therefore either empty or an affine
space modeled on the intertwiners $W_B\to U_A$. It has no distinguished
origin until a complement is chosen. An invariant complement is unique
exactly when a solution exists and this intertwiner space is zero.

## 2. Why the cokernel is precisely the first Ext group

The preceding calculation is already a classification by endpoint-preserving
extension equivalence: any extension admits a linear section; any equivalence
fixing both endpoints must have the form $F_h$; (6) describes exactly when
it is $R$-linear. Two further derivations explain the group law and connect
this classification to a free resolution.

### A canonical one-step free resolution

Let $F=R\otimes_k W$. Define

$$\begin{aligned}
d_B:F&\longrightarrow F,&
d_B(t^j\otimes w)&=t^{j+1}\otimes w-t^j\otimes Bw,\\
\varepsilon:F&\longrightarrow W_B,&
\varepsilon(t^j\otimes w)&=B^jw.
\end{aligned}$$

Then

$$0\longrightarrow F\xrightarrow{d_B}F
\xrightarrow{\varepsilon}W_B\longrightarrow0\tag{9}$$

is exact. Here is a proof without a determinant calculation. If a nonzero
vector polynomial $z=\sum_{j=0}^m t^j\otimes w_j$ has $w_m\ne0$,
then the coefficient of $t^{m+1}$ in $d_Bz$ is $w_m$. Hence $d_B$
is injective. Surjectivity of $\varepsilon$ follows from
$\varepsilon(1\otimes w)=w$. Finally,

$$t^j\otimes w-1\otimes B^jw
=d_B\left(\sum_{\ell=0}^{j-1}t^{j-1-\ell}\otimes B^\ell w\right)
\qquad(j\ge1).\tag{10}$$

Thus every vector polynomial is congruent modulo $\operatorname{im}d_B$
to its constant evaluation; exactly the elements with evaluation zero lie in
the image. Choosing a basis of $W$ shows that $F$ is free over $R$.
In matrix notation $d_B=tI-B$.

An $R$-map $F\to U_A$ is uniquely specified by a $k$-map $h:W\to U$,
its value on $1\otimes W$. Precomposition with $d_B$ sends $h$ to

$$w\longmapsto Ah(w)-h(Bw)=\delta(h)(w).$$

Applying $\operatorname{Hom}_R(-,U_A)$ to the resolution gives

$$0\longrightarrow\operatorname{Hom}_R(W_B,U_A)
\longrightarrow H\xrightarrow{\delta}H
\longrightarrow\operatorname{Ext}^1_R(W_B,U_A)
\longrightarrow0,\tag{11}$$

and $\operatorname{Ext}^j_R(W_B,U_A)=0$ for $j\ge2$. In particular,

$$\boxed{\operatorname{Ext}^1_{k[t]}(W_B,U_A)
\cong\operatorname{coker}(h\mapsto Ah-hB).}\tag{12}$$

The sign in this identification can be checked on the extension itself.
Extend its chosen section $s$ to the $R$-map
$\widetilde s:F\to E_T$, $t^j\otimes w\mapsto T^js(w)$.
Then $\widetilde s\,d_B$ takes values in $i(U)$ and its value on
$1\otimes w$ is $i(Cw)$. Therefore the resolution cocycle is $C$,
not an unspecified sign of $C$.

This resolution and the cokernel computation remain valid for arbitrary
$k$-vector spaces, assuming the usual existence of bases. Finite dimension
will matter for the trace pairing and the dimension counts below.

### Baer addition becomes addition of upper-right blocks

Take $E_C$ and $E_D$. Their fiber product over $W$ consists of triples
$(u_1,u_2,w)$, and its operator is

$$(u_1,u_2,w)\longmapsto(Au_1+Cw,Au_2+Dw,Bw).$$

The Baer sum pushes out the kernel $U\oplus U$ along addition
$(u_1,u_2)\mapsto u_1+u_2$. Concretely quotient the fiber product by
$\{(u,-u,0):u\in U\}$. The resulting coordinate $(u_1+u_2,w)$ has
operator $T_{C+D}$. Hence

$$[E_C]+[E_D]=[E_{C+D}].\tag{13}$$

Pushout along $\lambda1_U$ similarly gives $[E_{\lambda C}]$.
Thus (12) respects the $k$-vector-space structure as well as the set of
extension classes. The zero class is the split sequence.

## 3. A complete certificate for failure: trace-dual intertwiners

A failed attempt to solve a matrix equation does not by itself explain why
it fails. Here the dual equation supplies a finite certificate.

Put $K=\operatorname{Hom}_k(U,W)$. There is a perfect bilinear pairing

$$K\times H\longrightarrow k,\qquad
\langle g,C\rangle=\operatorname{tr}_W(gC)
=\operatorname{tr}_U(Cg).\tag{14}$$

The two traces agree because both are $\sum_{i,j}g_{ij}C_{ji}$ in
bases. The pairing is nondegenerate: a matrix unit in one rectangular matrix
space reads a single entry of the other. This proof works in every
characteristic. In particular it does **not** require
$\operatorname{char}k\nmid\dim U$ or $\operatorname{char}k\nmid\dim W$.

For $h\in H$,

$$\begin{aligned}
\langle g,\delta(h)\rangle
&=\operatorname{tr}_W(gAh-ghB)\\
&=\operatorname{tr}_W((gA-Bg)h).
\end{aligned}\tag{15}$$

Thus the dual linear map is

$$\delta^\vee:K\to K,\qquad g\longmapsto gA-Bg.\tag{16}$$

Its kernel consists of the intertwiners in the **reverse direction**:

$$\ker\delta^\vee=\operatorname{Hom}_R(U_A,W_B).\tag{17}$$

Equation (15) proves that every $\delta(h)$ is annihilated by those
intertwiners. Conversely, a vector $C$ outside $\operatorname{im}\delta$
can be separated from that subspace by a linear functional: extend a basis of
the image by $C$ and prescribe the functional to be zero on the image and
one on $C$. The perfect pairing represents that functional by some $g$.
Equation (15) then forces $gA=Bg$. Hence

$$\boxed{\ C\in\operatorname{im}\delta
\iff \operatorname{tr}_W(gC)=0
\text{ for every }g:U\to W\text{ with }gA=Bg.\ }\tag{18}$$

In particular, a single $g$ satisfying

$$gA=Bg,\qquad \operatorname{tr}_W(gC)\ne0\tag{19}$$

certifies that $U$ has no invariant complement in $E_C$. A basis of the
reverse-intertwiner space suffices to test all witnesses. A complete vanishing
test, followed by solving $Ah-hB=-C$, gives a constructive complement.

The quotient pairing is perfect and identifies

$$\operatorname{Ext}^1_R(W_B,U_A)^*
\cong\operatorname{Hom}_R(U_A,W_B),\tag{20}$$

or equivalently, in finite dimension,
$\operatorname{Ext}^1_R(W_B,U_A)\cong
\operatorname{Hom}_R(U_A,W_B)^*$.
This identification uses the specified polynomial variable $t$ through (9).
It is independent of bases and of the section. Its endpoint orientation is
not optional: maps $W\to U$ parametrize changes of a splitting, while maps
$U\to W$ test the obstruction.

For completeness, the expected compatibility with endpoint maps follows
from traces. Pushing an extension out along $a:U\to U'$ replaces $C$
by $aC$ and pairs with $g':U'\to W$ as
$\operatorname{tr}(g'aC)$. Pulling back along $b:W'\to W$ replaces
$C$ by $Cb$ and
$\operatorname{tr}_{W'}(gCb)=\operatorname{tr}_W(bgC)$.
These identities explain the natural dual pairing; they do not identify a
vector space with its own dual without additional data.

## 4. Coprime annihilators give an explicit inverse

Suppose $a,b\in k[t]$ satisfy

$$a(A)=0,\qquad b(B)=0,\qquad u(t)a(t)+v(t)b(t)=1.\tag{21}$$

One often stops after using Bézout to prove that a complement exists. A
divided-difference identity constructs the actual solution of every
Sylvester equation.

For $b(t)=\sum_{j=0}^d b_jt^j$, define the polynomial

$$Q_b(x,y)=\sum_{j=1}^d b_j\sum_{\ell=0}^{j-1}x^{j-1-\ell}y^\ell.
\tag{22}$$

It satisfies

$$(x-y)Q_b(x,y)=b(x)-b(y).\tag{23}$$

The notation $(b(x)-b(y))/(x-y)$ abbreviates this polynomial identity;
no inversion of $x-y$ is being assumed. On $H$, let
$L(h)=Ah$ and $R_B(h)=hB$. These operators commute, even though there
is no meaningful product $AB$ when $U\ne W$. Therefore (23) gives

$$(L-R_B)Q_b(L,R_B)=L_{b(A)}-R_{b(B)}=L_{b(A)}.\tag{24}$$

Evaluating (21) at $A$ yields $v(A)b(A)=1_U$. Every operator involved
in (24) commutes with left multiplication by $v(A)$. It follows that

$$\boxed{\ \delta^{-1}(D)=v(A)
\sum_{j=1}^d b_j\sum_{\ell=0}^{j-1}A^{j-1-\ell}DB^\ell.\ }\tag{25}$$

Multiplying on either side by $\delta$ gives the identity; this is a
two-sided inverse, not merely a recipe for selected right-hand sides.
The unique invariant complement is the graph of
$h=-\delta^{-1}(C)$.

For example, if $A^2=0$ and $B=1_W$, use
$a=t^2$, $b=t-1$, and
$t^2-(t+1)(t-1)=1$. Equation (25) becomes

$$\delta^{-1}(D)=-(1_U+A)D,\qquad
h=(1_U+A)C.$$

Directly,
$A(1_U+A)C-(1_U+A)C=-C$. No Jordan basis is needed, and the formula
also works in characteristic two.

A less trivial exact check is $A=N$, $B=1+M$, where $N^2=M^2=0$.
Take $a=t^2$, $b=(t-1)^2$ and

$$(3-2t)t^2+(1+2t)(t-1)^2=1.$$

Then (25) reduces to

$$\delta^{-1}(D)=-D-ND+DM+2NDM.\tag{26}$$

The integers in this identity are interpreted in $k$; no division by two
or three occurs.

### A finite geometric inverse for distinct Jordan eigenvalues

Suppose $A=\lambda1_U+N$ and $B=\mu1_W+M$, with $N^a=0$,
$M^b=0$, and $d=\lambda-\mu\ne0$. On $H$, put
$K(D)=ND-DM$. Its two summands commute, so the binomial expansion shows
$K^{a+b-1}=0$: each term has either at least $a$ left factors $N$ or
at least $b$ right factors $M$. Since $\delta=d1_H+K$,

$$\delta^{-1}=\sum_{r=0}^{a+b-2}(-1)^r d^{-r-1}K^r,$$

where

$$K^r(D)=\sum_{\ell=0}^r(-1)^\ell\binom r\ell
N^{r-\ell}DM^\ell.$$

Multiplication by $d1_H+K$ telescopes to the identity, with the last term
zero by nilpotence. This is a finite algebraic identity, with no convergence
assumption. It works in every characteristic when $d\ne0$; cancellation
of binomial coefficients in small characteristic can shorten the nilpotence
bound without invalidating it. Formula (26) is its case $d=-1$, $a=b=2$.

### A coordinate-free description of the same complement

Let $E_T$ be any extension in (1) under (21). Since $b(B)=0$,
$b(T)E\subseteq U$; since $a(A)=0$, it follows that
$a(T)b(T)=0$. The candidate complement is

$$K=\ker b(T).\tag{27}$$

Indeed $b(A)$ is invertible with inverse $v(A)$, so $K\cap U=0$.
For any lift $e$ of $w\in W$, write $b(T)e=i(u)$ and replace $e$
by $e-i(v(A)u)$. This new lift lies in $K$. Thus $q|_K:K\to W$ is
an isomorphism and $E=U\oplus K$.

Every invariant complement is isomorphic to $W_B$, hence is killed by
$b(T)$ and lies in $K$; it must equal $K$. This proves uniqueness without
finite-dimensional dimension counting. Both this proof and (25) work for
arbitrary $k$-spaces with the stated coprime annihilators. Over a commutative
base ring the algebraic identities also hold, but arbitrary extensions need
not admit a section over that base ring; the block classification then needs
that additional hypothesis.

## 5. What a shared spectral factor does and does not imply

In finite dimension, take $a=m_A$ and $b=m_B$. The following are equivalent:

- $m_A$ and $m_B$ are coprime;
- $\delta_{A,B}$ is invertible;
- every extension of $W_B$ by $U_A$ splits, with a unique invariant complement;
- the spectra of $A$ and $B$ are disjoint over an algebraic closure of $k$.

Coprimality implies invertibility by (25). Invertibility is equivalent to
$\ker\delta=\operatorname{coker}\delta=0$ by finite-dimensional linear
algebra, and (8), (12) give the extension assertion. For the converse to
coprimality, suppose an irreducible $p$ divides both minimal polynomials.
The primary cyclic decompositions contain blocks $R/(p^a)$ and $R/(p^b)$
for some $a,b\ge1$. A nonzero map from the latter to the former sends
$1$ to $p^{\max(a-b,0)}$ modulo $p^a$. Extending it by zero on the other
blocks gives a nonzero $W_B\to U_A$ intertwiner, so $\delta$ is not
injective. Finally, two polynomials over a field share an irreducible factor
exactly when they have a common root in an algebraic closure, proving the
spectral equivalence.

The conclusion concerns **all possible $C$**. If a factor is shared,
some right-hand sides are obstructed, but a particular $C$ may still lie
in $\operatorname{im}\delta$. In particular $C=0$ always splits, and
nonzero coboundaries split as well. A common eigenvalue is not a certificate
for a particular nonsplitting extension; (19) is such a certificate.

Checking only eigenvalues *in the ground field* is insufficient. Over
$\mathbb R$ let

$$A=B=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad C=1_2.$$

Neither operator has a real eigenvalue, so their real-eigenvalue sets are
both empty. Nonetheless $g=1_2$ is a reverse intertwiner and
$\operatorname{tr}(gC)=2\ne0$: this extension does not split. The
shared factor is $t^2+1$.

Nor does separate semisimplicity of the endpoints suffice. For
$A=B=(\lambda)$, $\delta=0$; every $C\ne0$ gives a nonsplit Jordan
block of size two. Semisimplicity of the middle module would force every
submodule to split, but semisimplicity is not preserved by arbitrary extensions.

## 6. Cyclic extensions expose exactly how blocks are joined

Let $f,g\in R$ be nonzero monic polynomials, with
$U=R/(f)$ and $W=R/(g)$. The resolution
$0\to R\xrightarrow{g}R\to R/(g)\to0$ gives

$$\operatorname{Ext}^1_R(R/(g),R/(f))
\cong(R/(f))/g(R/(f))
\cong R/(f,g)=R/(\gcd(f,g)).\tag{28}$$

The following presentation retains the endpoint maps, which (28) alone could
hide. Let $u$ be the specified generator of $U$, and choose a lift $e$
of the specified generator of $W$. There is a polynomial $c$ such that

$$fu=0,\qquad ge=cu.\tag{29}$$

Conversely these relations define

$$E_c=\operatorname{coker}
\begin{pmatrix}f&-c\\0&g\end{pmatrix}.\tag{30}$$

Columns are relation vectors in the ordered generators $(u,e)$. The map
$R/(f)\to E_c$, $1\mapsto u$, is injective: if $(r,0)$ is a relation
combination $x(f,0)+y(-c,g)$, then $yg=0$; since $R$ is a domain and
$g\ne0$, $y=0$, so $f\mid r$. The quotient by this copy of $U$ is
$R/(g)$ generated by the image of $e$.

Replacing $e$ by $e+hu$ changes $c$ to $c+gh$ modulo $f$.
Therefore the extension class is precisely $c\bmod(f,g)$, with the
specified cyclic generators understood. The sequence splits exactly when
that residue is zero. This is a classifying statement with fixed endpoints;
it is not merely an assertion about the isomorphism type of $E_c$.

### Middle modules: a smaller invariant

The first Smith factor of the matrix in (30) is the monic polynomial

$$d_1=\gcd(f,g,c),$$

because its entries generate that ideal. Its determinant is $fg$, so the
second factor is $d_2=fg/d_1$. Since $d_1$ divides both $f$ and $g$,
$d_1^2\mid fg$, and hence $d_1\mid d_2$, as required. Thus

$$E_c\cong R/(d_1)\oplus R/(d_2).\tag{31}$$

A unit factor contributes the zero module. This is an application of the
Smith theorem already proved in Chapter 2. Row and column operations classify
the middle module; they need not preserve its specified submodule, quotient,
or their generators.

Consequently the residue $c\bmod\gcd(f,g)$ classifies the extension,
while $\gcd(f,g,c)$ determines the middle-module isomorphism type in this
cyclic situation. Different residues can have the same gcd and hence the same
middle module.

### Primary powers and an explicit Smith reduction

Fix a monic irreducible $p$ and positive integers $a,b$. Take
$f=p^a$, $g=p^b$. Define $v_p(0)=\infty$ and

$$m=\min(a,b),\qquad \nu=\min(a,b,v_p(c)).\tag{32}$$

Changing $c$ by a multiple of $p^m$ leaves this truncated valuation
unchanged. Equations (28) and (31) become

$$\operatorname{Ext}^1_R(R/(p^b),R/(p^a))\cong R/(p^m),\tag{33}$$

$$\boxed{\ E_c\cong R/(p^\nu)\oplus
R/(p^{a+b-\nu}).\ }\tag{34}$$

The following row and column operations exhibit the mechanism in (34).
When $\nu<m$, write $c=p^\nu q$, $P=p^{a-\nu}$,
$Q=p^{b-\nu}$. Then $(P,q)=1$, so choose $s,r\in R$ with
$sP+rq=1$. Both matrices below have determinant one, and

$$\begin{pmatrix}1&0\\rQ&1\end{pmatrix}
\begin{pmatrix}P&-q\\0&Q\end{pmatrix}
\begin{pmatrix}s&q\\-r&P\end{pmatrix}
=\begin{pmatrix}1&0\\0&PQ\end{pmatrix}.\tag{35}$$

Multiplying the middle matrix by $p^\nu$ produces exactly the Smith
factors $p^\nu$ and $p^{a+b-\nu}$. For $\nu=m$ the class is zero:
$c$ is divisible by $p^m$. If $a\le b$, add $(c/p^a)$ times column
one to column two; if $b\le a$, add $(c/p^b)$ times row two to row
one. This removes $-c$ and gives the split diagonal presentation, reordered
if necessary. These operations also cover $c=0$.

The three boundary behaviors deserve to be kept separate:

- **Zero class:** $\nu=m$, including $c=0$ and every
  $c\in p^mR$. The middle module is
  $R/(p^a)\oplus R/(p^b)$, and the specified sequence splits.
- **Unit residue:** $p\nmid c$, so $\nu=0$. The first Smith factor
  is $1$ and $E_c\cong R/(p^{a+b})$. Both cyclic lengths join into
  one. Here “unit” means a unit modulo $p^m$; $c$ need not be a constant
  unit of $k[t]$.
- **Intermediate valuation:** $0<\nu<m$. A cyclic piece of length
  $\nu$ remains, while the other has length $a+b-\nu$. For
  $p=t-\lambda$, these are the two Jordan block sizes. For irreducible
  $p$ of degree greater than one, these are elementary-divisor exponents;
  their $k$-dimensions are multiplied by $\deg p$.

The formulas keep total $k$-dimension $(a+b)\deg p$ fixed. They do
not say that arbitrary simultaneous matrix conjugation preserves the chosen
extension class.

## 7. Two size-two Jordan blocks: the full quotient calculation

Take $U=W=k^2$ and

$$A=B=N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
C=\begin{pmatrix}c_{11}&c_{12}\\c_{21}&c_{22}\end{pmatrix}.$$

For $h=\begin{pmatrix}x&y\\z&w\end{pmatrix}$,

$$Nh-hN=\begin{pmatrix}z&w-x\\0&-z\end{pmatrix}.\tag{36}$$

Thus $\operatorname{im}\delta$ is spanned by $E_{12}$ and
$E_{11}-E_{22}$. The two quotient coordinates are

$$\alpha=c_{21},\qquad \beta=c_{11}+c_{22}=\operatorname{tr}C.\tag{37}$$

Every class has the unique representative

$$C_{\alpha,\beta}=\begin{pmatrix}\beta&0\\\alpha&0\end{pmatrix}.
\tag{38}$$

For example, choose $z=c_{22}$ and $w-x=-c_{12}$ in (36);
then $C+\delta(h)=C_{\alpha,\beta}$. This works in every
characteristic, including two.

The reverse intertwiners are exactly $g=r1+sN$. Their pairings are

$$\operatorname{tr}(gC)=r\beta+s\alpha.\tag{39}$$

So the abstract trace criterion recovers precisely the two explicit quotient
coordinates. There is a complement if and only if $\alpha=\beta=0$.
In that case the solution space has dimension two, since
$\ker\delta=k1\oplus kN$.

To connect this computation with cyclic presentations, let
$u_1,u_2$ be the basis of $U$, with $Nu_2=u_1$; the cyclic generator
is $u=u_2$. Similarly choose $w_1,w_2$ in $W$ and let $e$ be the
coordinate lift $(0,w_2)$. As $B^2=0$,

$$T_C^2e=ACw_2+CBw_2
=(c_{11}+c_{22})u_1+c_{21}u_2
=(\alpha+\beta t)u.\tag{40}$$

Thus the identification with the cyclic Ext group is

$$[C]\longmapsto\alpha+\beta t\pmod{t^2},\qquad
\operatorname{Ext}^1_R(R/(t^2),R/(t^2))\cong R/(t^2).\tag{41}$$

The three module types now follow from (34):

| Extension coordinates | Representative $C$ | Middle-module Jordan type | $(\operatorname{rank}T,\operatorname{rank}T^2,\operatorname{rank}T^3)$ |
|---|---|---|---|
| $\alpha=\beta=0$ | $0$ | $J_2(0)\oplus J_2(0)$ | $(2,0,0)$ |
| $\alpha=0$, $\beta\ne0$ | $\beta E_{11}$ | $J_3(0)\oplus J_1(0)$ | $(2,1,0)$ |
| $\alpha\ne0$ | $\beta E_{11}+\alpha E_{21}$ | $J_4(0)$ | $(3,2,1)$ |

These are all possibilities, over every field. Several comparisons prevent
misreadings of the table:

- $C=E_{12}\ne0$ nevertheless represents the split class, since
  $E_{12}=\delta(\operatorname{diag}(0,1))$. A complement is the graph
  of $h=-\operatorname{diag}(0,1)$.
- $E_{11}$ and $E_{22}$ are the same extension class: their difference
  is $\delta(E_{21})$.
- $E_{21}$ and $E_{21}+E_{11}$ are distinct extension classes, with
  cyclic residues $1$ and $1+t$, but both have middle module $R/(t^4)$.
  This distinction persists over $\mathbb F_2$.
- $C=1_2$ gives the residue $2t$. The middle module is
  $J_3\oplus J_1$ if $\operatorname{char}k\ne2$, but the extension
  is split in characteristic two. In that characteristic
  $1_2=E_{11}-E_{22}=\delta(E_{21})$.

The last example does not invalidate the trace criterion. The pairing on
*all* rectangular matrices is nondegenerate in every characteristic; a
particular trace, or the pairing restricted to a smaller subspace, can vanish.

## 8. Self-extensions and the commutant: dimensions without false identities

Since $\delta:H\to H$ is an endomorphism of a finite-dimensional
space, rank–nullity gives

$$\dim_k\operatorname{Ext}^1_R(W_B,U_A)
=\dim_k\operatorname{Hom}_R(W_B,U_A).\tag{42}$$

This dimension equality alone supplies no preferred isomorphism between its
two sides. Trace duality supplies a different, precise statement: the dual of
Ext is the **reverse** Hom space in (20).

If $U_A=\bigoplus_iR/(f_i)$ and
$W_B=\bigoplus_jR/(g_j)$, the block decomposition of $\delta$, or
finite additivity of the resolution, gives

$$\operatorname{Ext}^1_R(W_B,U_A)
\cong\bigoplus_{i,j}R/(\gcd(f_i,g_j)).\tag{43}$$

The displayed coordinates depend on the chosen cyclic decompositions and
cyclic generators. The resulting dimension is intrinsic:

$$\dim_k\operatorname{Ext}^1_R(W_B,U_A)
=\sum_{i,j}\deg\gcd(f_i,g_j).\tag{44}$$

For a single module with elementary divisors $p^{a_{p,i}}$, this yields

$$\dim_k\operatorname{Ext}^1_R(V_T,V_T)
=\dim_k\operatorname{End}_R(V_T)
=\sum_p\deg(p)\sum_{i,j}\min(a_{p,i},a_{p,j}).\tag{45}$$

There is also the canonical duality, relative to the fixed $t$,

$$\operatorname{Ext}^1_R(V_T,V_T)
\cong\operatorname{End}_R(V_T)^*.\tag{46}$$

One must not replace the dual in (46) by the commutant itself merely by
writing a trace pairing *inside* the commutant. For $T=N=J_2(0)$,
that commutant is $k1\oplus kN$, and

$$\operatorname{tr}\bigl(N(r1+sN)\bigr)=0\quad\text{for all }r,s.$$

Its restricted trace form is degenerate in every characteristic. Yet $N$
detects the nonzero extension represented by $E_{21}$ because
$\operatorname{tr}(NE_{21})=1$. The duality pairs a commutant element
with a *quotient class of arbitrary matrices*, not necessarily with another
commutant element. This is why choosing a direct complement to
$\operatorname{im}\delta$ in the full matrix space is an extra choice.

A useful related calculation gives the same quotient another meaning. Over
the dual numbers $k[\epsilon]/(\epsilon^2)$, a first-order change of basis
$1+\epsilon h$ transforms $T+\epsilon C$ into

$$(1-\epsilon h)(T+\epsilon C)(1+\epsilon h)
=T+\epsilon(C+Th-hT).\tag{47}$$

Thus first-order perturbations modulo changes of basis that reduce to the
identity have the same quotient as self-extensions. This explains the
appearance of a commutator cokernel, but does not classify finite
perturbations or give a multiplication on Ext matching composition in the
commutant.

## 9. The determinant bridge: resultants and integral obstructions

For $m=\dim U$ and $n=\dim W$, column-by-column vectorization gives

$$[\delta_{A,B}]=1_n\otimes A-B^{\mathsf T}\otimes1_m.\tag{48}$$

With the convention
$\operatorname{Res}(f,g)=\prod_{f(\alpha)=0}g(\alpha)$ for monic
polynomials, roots counted with multiplicity, one has

$$\boxed{\det\delta_{A,B}
=\operatorname{Res}(\chi_A,\chi_B)
=\prod_{i=1}^m\prod_{j=1}^n(\alpha_i-\beta_j).}\tag{49}$$

Here $\alpha_i,\beta_j$ are the characteristic roots in an algebraic
closure. To prove this without diagonalizability or separability, extend the
field to an algebraic closure and triangularize $A,B$. Such a triangular
form follows by repeatedly choosing an eigenvector and passing to the quotient;
it does not require an eigenbasis. In (48), $B^{\mathsf T}$ is lower
triangular, so the matrix is lower block triangular with diagonal blocks
$A-\beta_j1_m$. Its determinant is
$\prod_j\det(A-\beta_j1_m)=\prod_{i,j}(\alpha_i-\beta_j)$.
Determinants are unchanged by scalar extension, proving (49) over $k$.
Repeated roots simply repeat factors in the product.

Now let $U=\mathbb Z^m$ and $W=\mathbb Z^n$, with integral operators
$A,B$. There are two different questions: splitting after tensoring with
$\mathbb Q$, and splitting as $\mathbb Z[t]$-modules. Because $W$ is
free over $\mathbb Z$, every underlying exact sequence of abelian groups
ending in $W$ splits. Thus the block and section calculations still apply,
with

$$\delta_{\mathbb Z}:\operatorname{Hom}_{\mathbb Z}(W,U)
\longrightarrow\operatorname{Hom}_{\mathbb Z}(W,U),\quad
h\longmapsto Ah-hB.\tag{50}$$

Moreover (9) remains a free $\mathbb Z[t]$-resolution: its leading-term
and telescoping proofs work verbatim, and
$\mathbb Z[t]\otimes_{\mathbb Z}W\cong\mathbb Z[t]^n$ is free.
Consequently, for these endpoints,

$$\operatorname{Ext}^1_{\mathbb Z[t]}(W_B,U_A)
\cong\operatorname{coker}\delta_{\mathbb Z}.\tag{51}$$

The first argument being free over $\mathbb Z$ is essential to this free
resolution argument. We are not asserting that $\mathbb Z[t]$ is a PID
or that every $\mathbb Z[t]$-module has a resolution of length one.

If the resultant in (49) is nonzero, $\delta_{\mathbb Q}$ is invertible.
The integer matrix $\delta_{\mathbb Z}$ is then injective with finite
cokernel, and integer Smith form gives

$$\left|\operatorname{coker}\delta_{\mathbb Z}\right|
=|\det\delta_{\mathbb Z}|
=|\operatorname{Res}(\chi_A,\chi_B)|.\tag{52}$$

Indeed a Smith diagonal $d_1,\ldots,d_{mn}$ identifies the cokernel with
$\bigoplus_i\mathbb Z/d_i\mathbb Z$; the product of its finite orders
is $|\prod_i d_i|=|\det\delta|$. Thus a nonzero resultant gives
unique rational splitting, whereas resultant $\pm1$ gives unique integral
splitting for every $C$. For a particular integral $C$ with nonzero
resultant, the unique rational solution $h=-\delta_{\mathbb Q}^{-1}C$
is integral exactly when that extension splits integrally. More generally,
Smith coordinates turn the integral solvability test into divisibility by the
$d_i$.

### The smallest lattice defect

Take $A=(0)$, $B=(2)$, $C=(1)$, so

$$T=\begin{pmatrix}0&1\\0&2\end{pmatrix},\qquad
\delta_{\mathbb Z}(h)=-2h.\tag{53}$$

The rational complement is uniquely the graph of $h=1/2$. But its class
in $\operatorname{coker}\delta_{\mathbb Z}=\mathbb Z/2\mathbb Z$
is nonzero, so the specified copy $U=\mathbb Z(1,0)$ has no invariant
integral complement. The integral points on the other eigenline are generated
by $(1,2)$, and

$$[\mathbb Z^2:\mathbb Z(1,0)+\mathbb Z(1,2)]=2.\tag{54}$$

The quotient projection sends this eigenline lattice to $2\mathbb Z$,
not onto $W=\mathbb Z$. Independent rational eigenvectors have produced
a sublattice of finite index, not a direct-sum decomposition of the specified
lattice. The resultant is
$\operatorname{Res}(t,t-2)=-2$, whose absolute value $2$ is the order
of the obstruction.

This also pinpoints the boundary of trace witnesses. Here the reverse equation
$gA=Bg$ forces $g=0$ over both $\mathbb Q$ and $\mathbb Z$.
There is no nonzero trace witness over either ring, yet the integral extension
is nonsplit. Linear functionals into $\mathbb Z$ cannot detect the torsion
cokernel $\mathbb Z/2$. Reducing (53) modulo two does expose it, but
complete integral tests use the Smith divisibility conditions, including
higher prime powers when present.

This is the same arithmetic distinction that appears in integral CRT:
polynomials can be coprime over $\mathbb Q[t]$ while the inverse or
Bézout coefficients require denominators. The resultant measures a finite
failure of invertibility on a lattice. Its nonvanishing is the field-level
splitting test; its absolute value need not be one.

## 10. Exercises with worked answers

**Exercise 1 — a split extension with many complements.** Let
$A=B=J_2(0)$ and $C=E_{12}$. Find every invariant complement, and
verify invariance without using the Ext terminology.

*Answer.* Equation (36) must equal $-E_{12}$, so $z=0$ and
$w-x=-1$, while $x,y$ are arbitrary. The complements are the graphs of

$$h=\begin{pmatrix}x&y\\0&x-1\end{pmatrix}.$$

For these matrices $Ah+C=hB$, hence
$T_C(hw,w)=(hBw,Bw)$ belongs to the same graph. Distinct $h$ give
distinct complements because projection to $W$ fixes the graph parameter.

**Exercise 2 — produce an obstruction witness.** Let $U=k^2$, $W=k$,
$A=J_2(0)$, $B=0$, and $C(1)=(c_1,c_2)^{\mathsf T}$.
Determine exactly when a complement exists. When it does not, provide a
one-line certificate.

*Answer.* Write $h(1)=(x,y)^{\mathsf T}$. Then
$\delta(h)(1)=(y,0)^{\mathsf T}$, so a complement exists exactly when
$c_2=0$, with $y=-c_1$ and $x$ arbitrary. The reverse intertwiner
$g=(0,1)$ satisfies $gA=0=Bg$, and
$\operatorname{tr}(gC)=c_2$. It certifies nonsplitting when $c_2\ne0$.
This example also makes the direction $g:U\to W$ visible from matrix sizes.

**Exercise 3 — compute a complement without solving entries.** Suppose
$A^3=0$ and $B=1_W$. Find the unique invariant complement for arbitrary
$C:W\to U$.

*Answer.* $\delta(h)=(A-1_U)h$, and
$(1_U-A)(1_U+A+A^2)=1_U$. Thus
$h=(1_U+A+A^2)C$ solves $\delta(h)=-C$. The same identity proves
uniqueness. This is the specialization of the divided-difference formula to
$b=t-1$.

**Exercise 4 — valuation controls the middle module.** Let
$U=R/(p^3)$ and $W=R/(p^5)$ for a monic irreducible $p$.
Classify the possible middle-module types, and count extension classes of
each type when $k=\mathbb F_q$ and $\deg p=d$.

*Answer.* The extension group is $R/(p^3)$; put $Q=q^d$.
There is one zero class, giving $R/(p^3)\oplus R/(p^5)$.
For $\nu=0,1,2$, the type is
$R/(p^\nu)\oplus R/(p^{8-\nu})$, and the number of classes of exact
valuation $\nu$ is

$$|p^\nu R/(p^3)|-|p^{\nu+1}R/(p^3)|
=Q^{3-\nu}-Q^{2-\nu}.$$

These counts refer to endpoint-preserving extension classes. Their sum with
the split class is $Q^3$. Each of the four rows of this classification
specifies one middle-module isomorphism type, so counting middle modules
would give four, not $Q^3$.

**Exercise 5 — the characteristic-two trap.** Over $\mathbb F_2$, let
$A=B=J_2(0)$ and $C=1_2$. Exhibit an invariant complement and reconcile
it with the fact that $C$ is invertible.

*Answer.* $\delta(E_{21})=1_2=-1_2$ in characteristic two. The graph
of $E_{21}$ is therefore invariant. More explicitly its basis consists of
$(u_2,w_1)$ and $(0,w_2)$; $T$ sends the first to zero and the second
to the first. Invertibility of the off-diagonal map is unrelated to whether
its class in $H/\delta H$ is zero.

**Exercise 6 — a larger self-extension count.** If
$T=J_3(0)\oplus J_1(0)$, determine the dimension of its self-extension
space. Explain why the answer is not yet a classification of middle modules.

*Answer.* Formula (45) gives $3+1+1+1=6$. These are six independent
parameters for extensions with the two copies of $V_T$ identified in advance.
Changing endpoint automorphisms or forgetting the inclusion and quotient
can identify different extension classes. Determining the isomorphism types
of the resulting eight-dimensional middle modules is a further problem;
the number six is not a number of Jordan types.

## 11. Hypotheses, failed shortcuts, and reconstructive output

| Claim or construction | Hypotheses actually used | Failed shortcut or boundary |
|---|---|---|
| Block form and section-change classification | A field, or an explicitly split underlying sequence over the base ring | An arbitrary exact sequence over $\mathbb Z$ need not admit such a section; $0\to\mathbb Z/2\to\mathbb Z/4\to\mathbb Z/2\to0$ is an example |
| One-step resolution (9) | $R=k[t]$ and a $k$-space $W$ | It is a one-variable resolution; it does not automatically compute extensions with two commuting operators |
| Complete trace witnesses and perfect Ext–Hom duality | Finite-dimensional spaces over a field | Infinite-dimensional endomorphisms have no general trace; a trace on the commutant alone can be degenerate |
| Explicit inverse (25) | Stated annihilators and a Bézout identity $ua+vb=1$ | Shared factors prevent a universal inverse but do not obstruct every individual $C$ |
| Spectral disjointness criterion | Finite dimension, eigenvalues taken over an algebraic closure | Empty real-eigenvalue sets can hide a shared irreducible quadratic |
| Cyclic Ext and Smith formulas | Nonzero $f,g\in k[t]$; fixed cyclic endpoint generators for the residue coordinate | Smith operations classify the middle module and may change endpoint data |
| Jordan interpretation of (34) | $p=t-\lambda$ | Higher-degree irreducibles give rational elementary divisors rather than Jordan blocks over $k$ |
| Equality of commutant and self-Ext dimensions | Finite dimension | Equal dimensions do not identify the spaces or their algebraic structures; the natural statement here is duality |
| Integral cokernel has order equal to absolute resultant | Finite free integral endpoints and nonzero resultant | Rational splitting can leave a finite lattice-index obstruction; rational trace tests do not detect it |

The reconstruction route is short enough to use repeatedly. Record the
specified submodule and quotient; choose any linear section and extract $C$.
Compute its class modulo $Ah-hB$, or test it against reverse intertwiners.
If the class vanishes, solve once and add every forward intertwiner to obtain
all complements. If annihilators are coprime, (25) solves immediately and the
complement is uniquely $\ker b(T)$. If an obstruction remains, cyclic
coordinates and Smith reduction explain what it does to the middle module.
This keeps four different outputs distinct: a yes-or-no splitting test, a
witness or complement, an extension class with fixed endpoints, and the
coarser isomorphism type obtained after forgetting those endpoints.

**Local validation.** The companion script `check_sylvester.py` checks the
section/equivalence signs, both sides of the Bézout inverse, the trace-adjoint
identity, all size-two Jordan extensions over $\mathbb F_2$ and
$\mathbb F_3$, representative polynomial Smith reductions over
$\mathbb Q[t]$, and the integral resultant/index bridge. These finite checks supplement the field-independent proofs;
they are not substitutes for the hypotheses or the general arguments.
