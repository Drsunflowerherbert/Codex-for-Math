# Integral spectral gluing: the lattice behind Fourier coordinates

**Status and scope.** This is a local continuation of Chapter 9 at baseline
[a4a2879](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/a4a28796bdd63c5cbddbfba698c95d34728bd94c).
The CRT, resultant, cyclotomic,
and Fourier facts below are classical. The contribution of this chapter is
their organization into explicit reconstruction certificates, together with
small examples separating conditions that are easily conflated. No
literature novelty, search improvement, universal existence theorem, or new
Hadamard obstruction is asserted. The proofs are supplied here. The
[arithmetic proof comparison](../PROOF-COMPARISON-ARITHMETIC.md) identifies
the inspected textbook arguments and the additional integral gluing
proved in this chapter.

Chapter 9 identified Fourier diagonalization with CRT over a splitting
field. This chapter starts at the point where that description ceases to
remember enough: the original coefficients must be integers, and often
signs. An isomorphism of rational algebras need not identify their integral
lattices. Even an integral inverse need not have sign coefficients.
The central conclusion is Theorem 6A: once the full spectral norm
equations hold, sign reconstruction at every cyclic order is exactly
membership in a specified affine integral lattice. The prime-order
formulas and prime-power gluing explain how that lattice is tested.

Throughout, \(R=\mathbb Z[t]\), and
\[
 \mathcal A_m=\mathbb Z[z]/(z^m-1),\qquad
 X=\sum_{j=0}^{m-1}x_jz^j.
\]
The involution \(X^*=X(z^{-1})\) is defined modulo \(z^m-1\).
We use the Fourier convention
\(\lambda_r=X(\zeta_m^r)\); hence inverse Fourier coefficients use
\(\zeta_m^{-rj}\). The augmentation is
\(\epsilon(X)=X(1)=\sum_jx_j\), and \(1\) denotes the constant
polynomial, not the all-ones polynomial
\(T=1+z+\cdots+z^{m-1}\).

The dependency chain is short:

| Input | Reconstructive output | What remains to check |
| --- | --- | --- |
| Monic factors coprime over \(\mathbb Q\) | A rational CRT inverse and an exact finite integral defect | Membership in the integral image |
| An integral cyclotomic tuple | Rational coefficients with an explicit divisibility certificate | The coefficient lattice congruences |
| A tuple in that lattice | A unique integral row | Symmetry, normalization, and signs |
| Integral odd coefficients and exact total energy | Every coefficient is a sign | Any additional symmetry or normalization required by the construction |
| Coherent four-row spectral Gram equations | The full group-algebra Gram identity | Parity or another condition forcing signs |

## 1. The integral CRT defect is a finite module

**Theorem 1.** Let \(f,g\in\mathbb Z[t]\) be monic of positive degrees
\(r,s\), and assume \(\gcd_{\mathbb Q[t]}(f,g)=1\). There is an exact
sequence of \(R\)-modules
\[
 0\longrightarrow R/(fg)
 \xrightarrow{\alpha}R/(f)\oplus R/(g)
 \xrightarrow{\delta}R/(f,g)\longrightarrow0,                 \tag{1}
\]
where
\[
 \alpha(h)=(h\bmod f,h\bmod g),\qquad
 \delta(u,v)=u-v\bmod(f,g).
\]
The last map is an additive module map; it is generally not a ring map.
The first map is a ring injection, and its image has index
\[
 [R/(f)\oplus R/(g):\alpha(R/(fg))]
       =|\operatorname{Res}(f,g)|.                           \tag{2}
\]
In particular, rational coprimality gives an integral CRT isomorphism
exactly when the resultant is \(1\) or \(-1\).

**Proof of exactness.** Monic division makes all three principal
quotients free abelian groups in their usual power bases. If
\(h\in(f)\cap(g)\), write \(h=fu\) with \(u\in R\).
Rational coprimality implies \(g\mid u\) in \(\mathbb Q[t]\).
Divide \(u\) by the monic polynomial \(g\) in \(R\); uniqueness of
the rational remainder shows that the integral remainder is zero.
Thus \(h\in(fg)\), proving
\((f)\cap(g)=(fg)\) and the injectivity of \(\alpha\).

The difference map is well defined and surjective. If
\(u-v=af+bg\), then
\[
 h=u-af=v+bg
\]
maps to \((u\bmod f,v\bmod g)\). This proves exactness in the middle.
The reverse inclusion follows directly from the definitions. \(\square\)

The nontrivial part of (2) is a determinant computation over the integers,
not an application of field CRT.

**Determinant proof of the index formula.** Put
\(L_f=R/(f)\), with basis \(1,t,\ldots,t^{r-1}\), and let
\[
 M_g:L_f\longrightarrow L_f,\qquad h\longmapsto gh.
\]
Then
\[
 \operatorname{coker}M_g\cong R/(f,g).                       \tag{3}
\]
Over \(\mathbb Q\), the map \(M_g\) is invertible by Bézout's
identity, so its integral matrix has a nonzero determinant. An integral
square matrix \(M\) with nonzero determinant has cokernel of order
\(|\det M|\): integral row and column operations reduce it to Smith
normal form, whose nonzero diagonal entries multiply to that determinant
in absolute value.

For monic \(f\), the standard resultant convention gives
\[
 \det M_g=\operatorname{Res}(f,g)
         =\prod_{\alpha:f(\alpha)=0}g(\alpha),               \tag{4}
\]
with roots counted with multiplicity. To see the determinant identity,
extend scalars to an algebraic closure. Multiplication by \(t\) on
\(L_f\) has companion matrix with characteristic polynomial \(f\).
Triangularize that matrix; applying \(g\) gives diagonal entries
\(g(\alpha)\), including repeated roots.

This is also the Sylvester determinant computation. Consider the integral
map
\[
 S:R_{<s}\oplus R_{<r}\longrightarrow R_{<r+s},
       \qquad (a,b)\longmapsto af+bg.
\]
Use monic division by \(f\) to identify its target with
\(R_{<s}\oplus R_{<r}\), by \(qf+h\leftrightarrow(q,h)\).
This is an isomorphism of integral lattices. In these coordinates the
matrix of \(S\) has block form
\[
 \begin{pmatrix} I_s&Q\\0&M_g\end{pmatrix}.
\]
Thus its determinant is \(\det M_g\), up to the sign from the chosen
ordering of Sylvester columns and target basis. Consequently (3), (4),
and exactness of (1) give (2).

This argument also proves the claimed equivalence: the defect vanishes
exactly when its order is one, which is exactly \((f,g)=R\).
\(\square\)

Two cautions make the theorem more useful.

* Rational coprimality is weaker than integral comaximality. For
  \(f=t-1,\ g=t+1\), the defect is \(\mathbb Z/2\), and the image in
  \(\mathbb Z^2\) is \(\{(a,c):a\equiv c\pmod2\}\).
* The resultant gives the **order** of the defect, not its complete
  abelian-group structure. For \(f=t^2-1,\ g=t^2+1\),
  the defect is
  \[
    R/(2,t^2-1)\cong\mathbb F_2[t]/((t-1)^2),
  \]
  whose additive group is \((\mathbb Z/2)^2\), although the resultant
  is \(4\). Smith normal form gives the additional structure.

Monicity performs two jobs: it gives finite free power-basis lattices,
and it makes rational divisibility descend to integral divisibility.
Primitivity is enough for the latter job by Gauss's lemma; it does not
make the principal quotient a finite free abelian group. Without even
primitivity, injectivity can fail: \(f=2t\) and \(g=2(t-1)\) are
coprime over \(\mathbb Q\), but \(2t(t-1)\) belongs to
\((f)\cap(g)\) and not to \((fg)\).

**Corollary 2: several factors.** If the monic polynomials
\(f_1,\ldots,f_k\) are pairwise coprime over \(\mathbb Q\), the
evaluation map
\[
 R/(f_1\cdots f_k)\longrightarrow\bigoplus_i R/(f_i)
\]
is injective and has index
\[
 \prod_{i<j}|\operatorname{Res}(f_i,f_j)|.                  \tag{5}
\]

**Proof.** Apply Theorem 1 first to
\(F=f_1\cdots f_{k-1}\) and \(f_k\), and then refine the
\(R/(F)\) coordinate. Indices of nested finite-index lattices multiply.
The product-over-roots formula (4) gives
\(\operatorname{Res}(F,f_k)=\prod_{i<k}\operatorname{Res}(f_i,f_k)\).
Induction proves the assertion. \(\square\)

Formula (5) does **not** say that checking the original factor pairs
separately characterizes the image. Section 5 gives a small counterexample.

## 2. Prime cyclic order is a single fiber product

Let \(p\) be prime, \(\zeta=\zeta_p\), and
\[
 K=\mathbb Q(\zeta),\qquad O=\mathbb Z[\zeta],\qquad
 \pi=1-\zeta.
\]
We use the concrete order \(O\); no theorem identifying it with the full
ring of integers is needed here. The polynomial
\(\Phi_p(t)=1+t+\cdots+t^{p-1}\) is irreducible over \(\mathbb Q\):
after replacing \(t\) by \(t+1\), Eisenstein's criterion at \(p\)
applies. Hence \([K:\mathbb Q]=p-1\).

Reduction \(\zeta\mapsto1\) identifies
\[
 O/(\pi)\cong\mathbb Z/(\Phi_p(1))\cong\mathbb F_p.          \tag{6}
\]
Write \(\rho:O\to\mathbb F_p\) for this reduction.

**Theorem 3: exact prime gluing and reconstruction.** The map
\[
 \mathcal A_p\longrightarrow\mathbb Z\oplus O,\qquad
 X\longmapsto(a,b)=(X(1),X(\zeta))
\]
has image
\[
 \mathbb Z\times_{\mathbb F_p}O
       =\{(a,b):\rho(b)=a\bmod p\},                         \tag{7}
\]
of index \(p\). Its unique rational inverse has coefficients
\[
 \boxed{\displaystyle
 x_j=\frac{a+\operatorname{Tr}_{K/\mathbb Q}
                  (b\zeta^{-j})}{p}},\qquad 0\le j<p.      \tag{8}
\]
For \(a\in\mathbb Z,\ b\in O\), all the coefficients in (8) are
integers if and only if the single congruence in (7) holds.

**Proof of the image statement.** Apply Theorem 1 to
\(t-1\) and \(\Phi_p(t)\). Their common quotient is
\(\mathbb F_p\), and their resultant is \(\Phi_p(1)=p\).
There is also a direct construction. Write
\[
 b=B(\zeta),\qquad B\in\mathbb Z[t],\quad\deg B\le p-2,
 \qquad d=B(1).
 \]
If \(a\equiv d\pmod p\), set \(q=(a-d)/p\). Then
\[
 X(t)=B(t)+q\Phi_p(t)                                    \tag{9}
\]
has integral coefficients, degree less than \(p\), and prescribed
evaluations \(a,b\). Conversely any integral polynomial takes the same
residue at \(1\) and \(\zeta\) in the common quotient (6).

For arbitrary \(a\in\mathbb Q,\ b\in K\), the same construction with
a rational representative \(B\) proves existence and uniqueness of the
rational inverse.

**Proof of the trace formula.** The \(p-1\) embeddings are
\(\sigma_r(\zeta)=\zeta^r\), \(1\le r<p\), so
\[
 \operatorname{Tr}(\zeta^\ell)=
 \begin{cases}
 p-1,&p\mid\ell,\\
 -1,&p\nmid\ell.
 \end{cases}                                             \tag{10}
\]
For the rational inverse \(b=\sum_kx_k\zeta^k\), this gives
\[
 \operatorname{Tr}(b\zeta^{-j})
       =(p-1)x_j-\sum_{k\ne j}x_k=px_j-a.
 \]
This proves (8). Moreover, for every \(y\in O\),
\[
 \operatorname{Tr}(y)\equiv-\rho(y)\pmod p,                \tag{11}
\]
as follows by expanding \(y\) in its integral power basis and using
(10). Since \(\rho(\zeta^{-j})=1\), all \(p\) numerators in (8)
have the same residue \(a-\rho(b)\) modulo \(p\).
They are all divisible by \(p\) exactly when (7) holds.
\(\square\)

The prime \(2\) is included without modification. Here \(\zeta=-1\),
\(K=\mathbb Q\), and \(O=\mathbb Z\), so
\[
 a\equiv b\pmod2,\qquad
 x_0=(a+b)/2,\quad x_1=(a-b)/2.                            \tag{12}
\]
There is no extra factor of two in the field trace at this endpoint.

**A tuple that does not glue.** At \(p=3\), the pair
\((a,b)=(1,0)\) consists of algebraic integers and gives real symmetric
Fourier coordinates \((1,0,0)\). Its inverse is
\((1/3,1/3,1/3)\), because the congruence in (7) fails.
Thus neither algebraic integrality of each spectral coordinate nor
reality of all coordinates is enough.

## 3. Galois coherence, symmetry, normalization, and signs

One field element \(b\) encodes every nontrivial frequency:
\[
 \lambda_0=a,\qquad\lambda_r=\sigma_r(b)\quad(1\le r<p).
                                                               \tag{13}
\]
Those coordinates cannot be chosen independently. In particular, if
one chooses real values at conjugate frequency pairs without preserving
(13), the resulting coefficients may be real but irrational. At \(p=5\),
the proposed tuple
\[
 (\lambda_0,\lambda_1,\lambda_2,\lambda_3,\lambda_4)
       =(0,0,1,1,0)
\]
is real and invariant under \(r\mapsto-r\), and each listed value is
an algebraic integer. It cannot be the spectrum of a rational row:
\(\lambda_1=0\) would force every Galois conjugate of that field
coordinate to be zero.

Suppose from now on that \(a\in\mathbb Z,\ b\in O\) satisfy (7),
so \(X\) is already an integral row. The following are exact tests:
\[
 \begin{array}{rcl}
 X=X^* &\Longleftrightarrow& b=\overline b,\\[2mm]
 x_0=1&\Longleftrightarrow&a+\operatorname{Tr}(b)=p,\\[2mm]
 x_j\in\{-1,1\}\text{ for all }j
 &\Longleftrightarrow&
 a+\operatorname{Tr}(b\zeta^{-j})\in\{-p,p\}
       \text{ for all }j.                                \tag{14}
 \end{array}
\]
For the first equivalence, the evaluations of \(X^*\) are
\((a,\bar b)\), and rational CRT is injective. The other two statements
follow from (8). Since cyclotomic Galois automorphisms commute with
complex conjugation, \(b=\bar b\) also says that every
\(\sigma_r(b)\) is real.

The trace in (8) is the full trace from \(K\). If \(p\) is odd and
\(b=\bar b\), one may instead use \(K^+=\mathbb Q(\zeta+\zeta^{-1})\):
\[
 \operatorname{Tr}_{K/\mathbb Q}(b\zeta^{-j})
 =\operatorname{Tr}_{K^+/\mathbb Q}
       \bigl(b(\zeta^j+\zeta^{-j})\bigr).                  \tag{15}
\]
Indeed the relative trace from \(K\) to \(K^+\) sums a term and
its complex conjugate. The expression \(b\zeta^{-j}\) itself need
not be real; replacing its trace indiscriminately by twice a
real-subfield trace is invalid. Formula (15) does not apply at \(p=2\).

There is a useful substitute for checking all the sign conditions in
(14), provided parity and energy are checked exactly.

**Lemma 4: spectral parity for odd prime order.** For odd \(p\), an
integrally glued pair \((a,b)\) has every coefficient \(x_j\) odd if
and only if
\[
                 a\equiv1\pmod2,\qquad b\in2O.            \tag{16}
\]

**Proof.** If all coefficients are odd, write \(X=T-2N\) with
\(N\in\mathcal A_p\). Since \(T(1)=p\) and \(T(\zeta)=0\),
(16) follows. Conversely assume (16), and put
\[
 c=(p-a)/2\in\mathbb Z,\qquad d=-b/2\in O.
 \]
Because \(2\) is invertible modulo \(p\) and \(\rho(b)=a\),
\(\rho(d)=-a/2=(p-a)/2=c\) in \(\mathbb F_p\).
Theorem 3 therefore glues \((c,d)\) to an integral \(N\).
The evaluations of \(T-2N\) equal those of \(X\); injectivity gives
\(X=T-2N\), so all its coefficients are odd. \(\square\)

At \(p=2\), the exact replacement is
\[
 a+b\equiv a-b\equiv2\pmod4.                              \tag{17}
\]
Merely requiring \(a,b\) even fails: \((a,b)=(2,2)\)
glues to \((2,0)\).

**Lemma 5: parity and the minimum energy force signs.** If
\(X_1,\ldots,X_q\in\mathcal A_m\) have odd coefficients and
\[
                 \sum_{\ell,j}x_{\ell j}^2=qm,            \tag{18}
\]
then every coefficient of every row is \(1\) or \(-1\).

**Proof.** There are \(qm\) odd integers in the sum; each has square
at least one. Equality in their summed lower bound forces every square
to be one. \(\square\)

For one prime-order row, exact Parseval reads
\[
 a^2+\operatorname{Tr}(b\bar b)=p\sum_jx_j^2.              \tag{19}
\]
To prove it, expand
\(\sum_{r=0}^{p-1}|X(\zeta^r)|^2\); the geometric sum kills
each term \(x_jx_k\) with \(j\ne k\), and leaves
\(p\sum_jx_j^2\). The nontrivial frequencies give the trace term.
This is the positive quadratic trace form, not the multiplicative
field norm \(\operatorname{N}_{K/\mathbb Q}(b)\).

Consequently, at an odd prime, an integrally glued pair represents a
sign row exactly when
\[
 a\text{ is odd},\qquad b\in2O,\qquad
 a^2+\operatorname{Tr}(b\bar b)=p^2.                      \tag{20}
\]
Necessity follows from signs, and sufficiency follows from Lemmas 4–5.
To represent a **normalized symmetric** sign row, add
\(b=\bar b\) and \(a+\operatorname{Tr}(b)=p\).
These are finite exact certificates, not an assertion that a tuple with
prescribed extra Gram constraints exists.

**Energy and every individual spectral bound still do not suffice.**
At \(p=11\), take
\[
 x_0=1,\qquad x_{\pm1}=2,\qquad x_{\pm2}=-1,
 \qquad x_j=0\text{ otherwise}.                           \tag{21}
\]
This row is integral, normalized, and symmetric. Its augmentation is
\(a=3\), so even the necessary normalized sign-row congruence
\(a\equiv p\pmod4\) holds. Its energy is exactly
\(1+2\cdot4+2\cdot1=11\). Every Fourier value has the form
\[
 1+4\cos\theta-2\cos2\theta
      =3+4c-4c^2,\qquad -1\le c\le1.
 \]
The concave quadratic has maximum \(4\) at \(c=1/2\) and
minimum \(-5\) at \(c=-1\). Thus every Galois conjugate satisfies
\[
 |\lambda_r|^2\le25<44,
 \]
which is stronger than the individual bound required of a row in a
four-row order-eleven Gram identity. The pair
\[
 b=1+2(\zeta+\zeta^{-1})-(\zeta^2+\zeta^{-2}),\quad a=3
 \]
glues integrally, and (19) has the exact sign-row energy \(121\).
Nevertheless the row is not a sign row. Its failure is visible in
parity, not in the energy or these individual spectral inequalities.
No completion of this row is being asserted.

## 4. Full inverse Fourier divisibility for composite order

For general \(m\), take one coordinate
\[
 b_d\in O_d=\mathbb Z[\zeta_d]\qquad(d\mid m),
 \quad O_1=\mathbb Z.
 \]
Here the standard cyclotomic factorization and irreducibility give
\[
 \mathbb Q[z]/(z^m-1)\cong
       \prod_{d\mid m}\mathbb Q(\zeta_d).
 \]
The new issue is the integral image of this familiar rational
decomposition.

**Proposition 6: an integral inverse Fourier certificate.** Define
\[
 C_j=\sum_{d\mid m}
       \operatorname{Tr}_{\mathbb Q(\zeta_d)/\mathbb Q}
                 (b_d\zeta_d^{-j}),\qquad 0\le j<m.        \tag{22}
\]
Every \(C_j\) is an integer. The unique rational inverse tuple has
coefficients \(x_j=C_j/m\), and the tuple comes from
\(\mathcal A_m\) if and only if
\[
                         C_j\equiv0\pmod m
                         \quad(0\le j<m).                 \tag{23}
\]

**Proof.** Choose \(\zeta_d=\zeta_m^{m/d}\).
For a frequency \(r\) whose character has order \(d\), write
\(r=(m/d)u\) with \(u\) a unit modulo \(d\), and prescribe the
coherent value \(\lambda_r=\sigma_u(b_d)\). The zero frequency is
\(b_1\). Partitioning the ordinary inverse Fourier sum by character
order gives exactly (22). Orthogonality of the \(m\) characters
proves that the resulting \(x_j\) have the prescribed evaluations.
They are rational because (22) is a sum of traces.

Each trace is an integer: multiplication by
\(b_d\zeta_d^{-j}\) preserves the free integral power-basis lattice
\(O_d\), so its matrix has integer trace, equal to the field trace.
The coefficient criterion (23) now follows. \(\square\)

The certificate can contain redundant congruences; its advantage is that
it is exact and applies uniformly. It does not replace the task of
finding a tuple satisfying sign, symmetry, or Gram constraints. If signs
are required, one can check \(C_j\in\{-m,m\}\) directly.
Alternatively, after (23), check that every \(C_j/m\) is odd and
use the exact energy certificate of Lemma 5.

For odd \(m\), parity itself can be tested componentwise:
an already integrally glued tuple represents \(X\equiv T\pmod2\)
if and only if its components agree with those of \(T\) modulo
\(2O_d\). To justify the converse, reduce
\[
 z^m-1=\prod_{d\mid m}\Phi_d(z)
 \]
modulo \(2\). Its derivative is \(z^{m-1}\), relatively prime to
the polynomial, so the product is squarefree. Its displayed factors
are therefore pairwise coprime in \(\mathbb F_2[z]\), where ordinary
CRT is injective. This argument fails when \(m\) is even, precisely
as the \(p=2\) example already shows.

The following lattice formulation includes even order and avoids making
parity look like a collection of unrelated special cases. Keep the
cyclotomic factors **labelled by \(d\)** even when two underlying
number fields happen to be isomorphic. Set
\[
 M_m=\bigoplus_{d\mid m}O_d,\qquad
 L_m=\operatorname{image}(\mathcal A_m\longrightarrow M_m),
 \qquad J_m=(m,0,\ldots,0).
 \]
Thus \(J_m\) is the image of \(T\).

**Theorem 6A: the affine lattice and energy certificate, all orders.**
Let \(m\ge1\), and let four tuples \(b_\ell=(b_{\ell,d})\) belong to
\(M_m\). Assume the exact identities
\[
 \sum_{\ell=1}^4b_{\ell,d}\overline{b_{\ell,d}}=4m
       \quad\text{in }\mathbb Q(\zeta_d),\qquad d\mid m.   \tag{23a}
\]
Then the tuples reconstruct four sign rows with summed cyclic Gram
\(4m\,1\) if and only if
\[
                         b_\ell\in J_m+2L_m
                         \quad(1\le\ell\le4).             \tag{23b}
\]
Symmetry holds exactly when every component is fixed by complex
conjugation. Normalization \(x_{\ell0}=1\) holds exactly when
\[
             \sum_{d\mid m}\operatorname{Tr}(b_{\ell,d})=m.
                                                               \tag{23c}
\]
These last two conditions are additional requirements.

**Proof.** If \(b_\ell=J_m+2c_\ell\) with \(c_\ell\in L_m\),
the corresponding row is \(T+2Y_\ell\) with integral \(Y_\ell\).
Its coefficients are therefore odd integers. Apply every cyclotomic
embedding to (23a); all Fourier norm equations follow. Fourier
injectivity gives the full Gram identity. Its constant coefficient
is total energy \(4m\), so Lemma 5 forces signs. Conversely every sign
row has the form \(T+2Y_\ell\) with integral \(Y_\ell\), establishing
(23b). The symmetry test follows from the involution and injectivity;
(23c) is Proposition 6 at \(j=0\). This also covers \(m=1\), where
there is only the rational coordinate. \(\square\)

This certificate requires no separate assumption of integral gluing:
membership in the affine lattice already includes it. For practical
separation of the two tests, observe that
\[
                         mM_m\subseteq L_m.               \tag{23d}
\]
Indeed Proposition 6 reconstructs \(mb\) with coefficients \(C_j\),
which are integers. Thus \(M_m/L_m\) is annihilated by \(m\).
For odd \(m\), it has no nonzero two-torsion, and consequently
\[
 b\in J_m+2L_m
 \quad\Longleftrightarrow\quad
 b\in L_m\ \text{ and }\ b-J_m\in2M_m.                    \tag{23e}
\]
For the reverse implication, put \(c=(b-J_m)/2\in M_m\).
Both \(2c\) and \(mc\) lie in \(L_m\); an integer combination of
\(2\) and \(m\) equal to one gives \(c\in L_m\).
At odd order the component conditions in (23e) are exactly:
the augmentation coordinate is odd, and every \(d>1\) coordinate
belongs to \(2O_d\).

At even order one must retain the actual half-shift test
\((b-J_m)/2\in L_m\). For \(m=4\), take four copies of the
integral row \(2\cdot1=(2,0,0,0)\). Every row has energy \(4\),
every spectral coordinate is \(2\), and (23a) holds.
Each tuple lies in \(L_4\) and satisfies \(b-J_4\in2M_4\).
Nevertheless its half-shift reconstructs
\((1,-1,-1,-1)/2\), so (23b) fails and the rows are not signs.
This example does not impose normalization: the constant coefficient
is \(2\), showing again why (23c) is a separate condition.

Integral gluing cannot be dropped at odd order either. At \(m=3\)
take augmentation coordinates \((3,1,1,1)\) and nontrivial coordinates
\((0,2,2,2)\). These are odd/even as required, satisfy both exact
spectral Gram identities, and give individual rational row energies
\(3\). The first row reconstructs \((1,1,1)\); each of the other
three reconstructs \((5,-1,-1)/3\). Their failure is precisely the
prime gluing congruence \(1\not\equiv2\pmod3\).

If a procedure generates coefficient rows as signs from the outset,
their spectra automatically satisfy the integral and parity conditions.
In that setting the certificate explains existing structure; it is
not a new filter or a claimed speedup. No implementation claim about
the earlier search scripts is needed for this conditional observation.

## 5. Why separate pairwise compatibility loses a condition at order four

Factor
\[
 z^4-1=(z-1)(z+1)(z^2+1).
 \]
Write the three rational coordinates as
\[
 a=X(1),\qquad c=X(-1),\qquad b=X(i)=u+iv.
 \]
The inverse is
\[
 \begin{aligned}
 x_0&=(a+c+2u)/4,&x_1&=(a-c+2v)/4,\\
 x_2&=(a+c-2u)/4,&x_3&=(a-c-2v)/4.
 \end{aligned}                                           \tag{24}
\]
It follows that the exact integral image is
\[
 \boxed{a+c\equiv2u\pmod4,\qquad
        a-c\equiv2v\pmod4.}                              \tag{25}
\]
Indeed these congruences make the two displayed plus numerators
divisible by four; subtracting \(4u\) or \(4v\) proves the same for
the minus numerators. Necessity is immediate.

The evaluation matrix in coordinates \((a,c,u,v)\) is
\[
 E_4=\begin{pmatrix}
 1&1&1&1\\1&-1&1&-1\\1&0&-1&0\\0&1&0&-1
 \end{pmatrix},\qquad \det E_4=-8.
 \]
Thus the integral image has index \(8\). This agrees with (5),
since the three pairwise resultants each have absolute value \(2\).

Nevertheless, the common quotient for **each original factor pair**
is only \(\mathbb F_2\). The pairwise compatibility conditions are
\[
                  a\equiv c\equiv u+v\pmod2.              \tag{26}
\]
There are two independent mod-two equations, so this pairwise-compatible
lattice has index \(4\), not \(8\). For example,
\[
          (a,c,b)=(0,0,1+i)
 \]
passes (26), but its inverse is
\((1,1,-1,-1)/2\). Even the real tuple \((2,0,0)\) passes
(26) and reconstructs \((1,1,1,1)/2\).

The missing information has an explicit explanation. Glue \(a,c\)
first, requiring \(a\equiv c\pmod2\). Their integral polynomial
modulo \(z^2-1\) is \(A+Bz\), where
\[
 A=(a+c)/2,\qquad B=(a-c)/2.
 \]
The next gluing step is between \(z^2-1\) and \(z^2+1\).
Its common quotient is
\[
 \mathbb Z[z]/(z^2-1,z^2+1)
       \cong\mathbb F_2[z]/((z-1)^2),                     \tag{27}
\]
and the necessary and sufficient condition is
\[
                 b\equiv A+Bi\pmod{2\mathbb Z[i]}.
 \]
Its two coefficient conditions are exactly (25). Replacing the common
quotient (27) by its residue field \(\mathbb F_2\) discards a
nilpotent direction. Thus the failure of the naive pairwise test is
already visible in a ring of four elements.

Order nine gives another exact scale for the lattice issue:
\[
 z^9-1=\Phi_1\Phi_3\Phi_9,\qquad
 |\operatorname{Res}(\Phi_1,\Phi_3)|=3,\quad
 |\operatorname{Res}(\Phi_1,\Phi_9)|=3,\quad
 |\operatorname{Res}(\Phi_3,\Phi_9)|=9.
 \]
For the last equality, \(\Phi_9(\zeta_3)=3\), so its
multiplication map on the rank-two lattice \(O_3\) is \(3I\).
The integral cyclotomic image therefore has index \(81\).
This calculation is distinct from the order-nine compression fixture
in Chapter 9: an index of \(81\) neither proves nor disproves any
sign-lifting claim about that fixture.

### Prime-power gluing records a truncated Taylor expansion

There is an elementary general version of (27). Let \(p\) be prime,
\(a\ge1\), \(q=p^{a-1}\), and set
\[
 f=z^q-1,\qquad
 g=\Phi_{p^a}(z)=1+z^q+\cdots+z^{(p-1)q}.
 \]
Since \(g\equiv p\pmod f\),
\[
 (f,g)=(f,p),\qquad
 R/(f,g)\cong\mathbb F_p[z]/((z-1)^q)
              \cong\mathbb F_p[u]/(u^q).                 \tag{27a}
\]
Thus a lower-order integral row \(A\in\mathcal A_q\) and
an upper coordinate \(b=B(\zeta_{p^a})\in O_{p^a}\) glue
exactly when their images in this ring agree. This is a direct
application of Theorem 1, so it is both necessary and sufficient.
The defect of this stage has order \(p^q\).

To give all its conditions without factorial denominators, define
the Hasse derivative
\[
 D^{[k]}\!\left(\sum_jc_jz^j\right)(1)
       =\sum_{j\ge k}\binom jk c_j.
 \]
The binomial identity gives the exact expansion
\[
 C(1+u)=\sum_{k\ge0}D^{[k]}C(1)\,u^k.
 \]
Therefore the gluing conditions are precisely
\[
 D^{[k]}A(1)\equiv D^{[k]}B(1)\pmod p,
                 \qquad 0\le k<q.                       \tag{27b}
\]
They are independent of the chosen representatives: modulo \(p\),
\(f=(z-1)^q\) and \(g=(z-1)^{(p-1)q}\), so adding a
multiple of either defining relation does not change the relevant
truncated expansion.

The word “jet” here means only this finite list of coefficients of
\(C(1+u)\) modulo \(u^q\). It adds no constraints beyond equality
in (27a). On polynomials of degree less than \(q\), substitution
\(z=1+u\) is an invertible triangular integer basis change, with
inverse \(u=z-1\). Thus the jet congruences and the coefficient
congruences in the common quotient are equivalent descriptions.

At order \(9\), the final stage has \(q=3\), so it remembers
the constant, linear, and quadratic coefficients in
\(\mathbb F_3[u]/u^3\). Taking \(A=0\) and
\(b=(\zeta_9-1)^2\) passes the constant and linear tests but
fails the quadratic test. At order \(8\), taking \(A=0\) and
\(b=(\zeta_8-1)^2\) shows why ordinary derivatives are unsafe
in characteristic two: every positive ordinary derivative of
\((z-1)^2\) vanishes modulo two, as does its value at \(1\),
but its second Hasse derivative is \(1\).

Iterating the stage indices from \(1\) to \(p^a\) gives
\[
 [M_{p^a}:L_{p^a}]
       =p^{1+p+\cdots+p^{a-1}}.                          \tag{27c}
\]
For order \(9\), the full evaluation lattice has Smith invariants
\[
                    1,1,1,1,1,1,3,3,9.
 \]
For an explicit reduction, write a degree-less-than-nine polynomial
uniquely as \(B+C\Phi_9\), with \(\deg B<6\), \(\deg C<3\).
The \(\Phi_9\) coordinate is \(B\); since \(\Phi_9\) equals
\(3\) in both lower factors, subtracting the lower evaluations of
\(B\) leaves the block \(3E_3\), where \(E_3\) is the
order-three integral evaluation matrix. Its Smith invariants are
\(1,1,3\) (an entry and a two-by-two minor are units, and its
determinant has magnitude \(3\)). The full order-nine matrix is
therefore equivalent over integral unimodular basis changes to
\(I_6\oplus3E_3\), proving the displayed invariants.

## 6. What the joint Gram equations actually enforce

For integral or real coefficient rows, Fourier evaluation gives
\[
 \sum_{\ell=1}^{q}X_\ell X_\ell^*=qm\,1
 \quad\Longleftrightarrow\quad
 \sum_{\ell=1}^{q}|\lambda_{\ell,r}|^2=qm
       \quad\text{at every frequency }r.                 \tag{28}
\]
The reverse implication uses injectivity of the full complex Fourier
map. It requires a coherent spectrum for each row. Independent
feasibility intervals at different frequencies do not supply such rows.

For \(q=4\) at prime order, exact algebraic coordinates make (28)
particularly economical:
\[
 \sum_{\ell=1}^4a_\ell^2=4p,\qquad
 \sum_{\ell=1}^4b_\ell\bar b_\ell=4p
                    \quad\text{in }K.                   \tag{29}
\]
Applying every Galois embedding to the second identity gives every
nonzero-frequency equation. For symmetric rows one may replace
\(b_\ell\bar b_\ell\) by \(b_\ell^2\).
One equality proved **as an algebraic equality** in a faithful embedding
is enough; testing a numerical approximation or only an inequality at
one embedding is not the same thing.

**Corollary 7: an exact prime-order four-row sign certificate.**
Let \(p\) be odd, and choose four pairs
\((a_\ell,b_\ell)\in\mathbb Z\oplus O\).
They reconstruct a normalized symmetric Williamson quadruple if and
only if all of the following hold:

1. \(\rho(b_\ell)=a_\ell\bmod p\) for each row.
2. \(b_\ell=\bar b_\ell\) and
   \(a_\ell+\operatorname{Tr}(b_\ell)=p\) for each row.
3. Every \(a_\ell\) is odd and every \(b_\ell\) belongs to \(2O\).
4. The two exact Gram identities in (29) hold.

**Proof.** Necessity follows by evaluation of a normalized symmetric
sign quadruple. Conversely, condition 1 reconstructs integral rows,
condition 2 gives symmetry and normalization, and condition 3 gives
odd coefficients by Lemma 4. Condition 4 gives (28), whose constant
coefficient is total energy \(4p\). Lemma 5 makes every entry a sign.
The resulting group-algebra identity is exactly the Williamson
condition from Chapter 9. \(\square\)

This is an equivalent exact formulation, not a relaxation and not an
existence proof. Its value is that each obstruction has an identified
location: a lattice congruence, a linear condition, parity, or a
coupled quadratic identity.

**Even the full Gram identity does not force signs without a lower
bound on coefficient size.** In \(\mathcal A_3\), put
\[
 X_1=1-2z-2z^2,\qquad X_2=X_3=X_4=1.                     \tag{30}
\]
All four rows are integral, symmetric, and normalized by \(x_0=1\).
Writing \(S=z+z^2\), the relation \(S^2=2+S\) gives
\[
 X_1^2=1-4S+4(2+S)=9,\qquad
 \sum_{\ell=1}^4X_\ell X_\ell^*=12.
 \]
Their prime spectral coordinates are
\[
 (a_1,a_2,a_3,a_4)=(-3,1,1,1),\qquad
 (b_1,b_2,b_3,b_4)=(3,1,1,1).
 \]
They satisfy integral gluing, normalization, symmetry, and both equations
in (29), exactly. Yet the coefficient rows are
\((1,-2,-2)\) and three copies of \((1,0,0)\).
Their separate energies are \(9,1,1,1\); the example does not claim
to enforce energy \(3\) on each row. Condition 3 of Corollary 7 fails.
This example and (21) expose different missing constraints.

More generally, integrality, odd coefficients, and the full identity
(28) force signs at **any** order by Lemma 5. Oddness can be weakened
to the requirement that all integral coefficients be nonzero, but
nonzeroness has a less convenient spectral description.

**The nonsymmetric boundary.** Without symmetry, the exact norm
equations produce complementary circulant sign rows. They do not by
themselves justify the standard Williamson block array displayed in
Chapter 9. For that array its block \((1,2)\) in the Gram matrix is
\[
                  -AB^{\mathsf T}+BA^{\mathsf T}
                  -CD^{\mathsf T}+DC^{\mathsf T}.
 \]
Commutation of circulants does not make each term cancel its partner:
one sufficient extra condition is pairwise amicability
\(UV^{\mathsf T}=VU^{\mathsf T}\).
Symmetric circulants satisfy this automatically.

For a concrete check, at length three take first rows
\[
 A=(1,1,1),\quad B=C=(1,1,-1),\quad D=(1,-1,1).
 \]
The sum of their cyclic Gram matrices is \(12I_3\).
With the Chapter 9 convention \(P_{ij}=1\) when \(j=i+1\),
the standard block array nevertheless has Gram block \((1,2)\)
\[
 \begin{pmatrix}
 0&-4&4\\4&0&-4\\-4&4&0
 \end{pmatrix}\ne0.
 \]
Indeed \(D=B^{\mathsf T}\), while \(A\) commutes amicably with
every circulant; the offending block is \((B^{\mathsf T})^2-B^2\).
Thus Theorem 6A gives complementarity without symmetry, whereas
Corollary 7 deliberately retains symmetry to give a Williamson
quadruple and the stated block construction.

## 7. Negative supports retain the discrete information

For actual sign rows define
\[
 N_\ell=\sum_{x_{\ell j}=-1}z^j,\qquad
 r_\ell=\epsilon(N_\ell),\qquad R=\sum_{\ell=1}^4r_\ell.
 \]
Then \(X_\ell=T-2N_\ell\). The essential assertion is that the
coefficients of \(N_\ell\) lie in \(\{0,1\}\); it is **not**
the group-algebra equation \(N_\ell^2=N_\ell\).
Coefficientwise multiplication and cyclic convolution are different.

Using \(T^2=mT\) and \(TN_\ell=N_\ell T=r_\ell T\),
expansion gives
\[
 \sum_{\ell=1}^4X_\ell X_\ell^*=4m\,1
 \quad\Longleftrightarrow\quad
 \sum_{\ell=1}^4N_\ell N_\ell^*+(m-R)T=m\,1.              \tag{31}
\]
No symmetry is required for this equivalence. At a nonzero shift,
the equation says
\[
 \sum_{\ell=1}^4
    |\operatorname{supp}(N_\ell)\cap
          (\operatorname{supp}(N_\ell)+s)|=R-m.            \tag{32}
\]
At shift zero the equation holds automatically because the \(N_\ell\)
are indicators. Thus (31) is a joint system of cyclic difference
counts, not just four independent row conditions.

For odd \(m\), impose symmetry and normalization \(x_{\ell0}=1\).
Each negative support is a union of nonzero pairs \(\{j,-j\}\);
therefore every \(r_\ell\) is even and \(R\) is even. The row sums
satisfy
\[
 \epsilon(X_\ell)=m-2r_\ell\equiv m\pmod4,\qquad
                  2-m\le\epsilon(X_\ell)\le m.            \tag{33}
\]
These are necessary conditions. They do not characterize either
individual sign rows in spectral space or a joint solution.

Symmetry lets us replace \(N_\ell N_\ell^*\) by \(N_\ell^2\).
Reduce (31) modulo two. Since \(m\) and \(m-R\) are odd,
\[
             \sum_\ell N_\ell^2=T+1
                 \quad\text{in }\mathbb F_2[C_m].         \tag{34}
\]
In characteristic two, squaring sends
\(\sum n_jz^j\) to \(\sum n_jz^{2j}\).
Because \(m\) is odd, doubling permutes the residue classes, so this
map is an automorphism fixing \(T\) and \(1\).
Applying its inverse to (34) yields
\[
                        \sum_\ell N_\ell=T+1.            \tag{35}
\]
At every nonzero position an odd number of the four entries are
negative. Equivalently,
\[
                x_{1j}x_{2j}x_{3j}x_{4j}=-1
                         \qquad(j\ne0).                  \tag{36}
\]
This recovers the odd normalized symmetric Williamson product
condition with every ring and divisibility step visible.

The converse is absent: reducing (31) modulo two throws away its
integer difference counts. The order-nine fixture in Chapter 9,
and its separate continuation analysis, illustrates this loss.
The present argument does not need or re-run that enumeration.

At prime order the support coordinates are
\[
 \epsilon(N)=(p-a)/2,\qquad N(\zeta)=-b/2.                 \tag{37}
\]
Lemma 4 explains exactly when these data glue to an **integral**
\(N\). To obtain an actual negative support, its coefficients must
also lie in \(\{0,1\}\). A useful energy reformulation makes the
last issue explicit: if \(X=T-2N\) has integral \(N\), then
\[
 \sum_jx_j^2=m
 \quad\Longleftrightarrow\quad
 \sum_jn_j(n_j-1)=0.
 \]
Every summand on the right is nonnegative for integral \(n_j\);
equality is therefore equivalent to \(n_j\in\{0,1\}\) for all
\(j\). The same proof works after summing over several rows.

## 8. Hypotheses, failed replacements, and bounded conclusions

| Hypothesis or exact requirement | Tempting replacement | Counterexample or precise failure |
| --- | --- | --- |
| Integral comaximality | Coprimality over \(\mathbb Q\) | \(t-1,t+1\) have defect \(\mathbb Z/2\) |
| Monic/primitive control of divisibility | Arbitrary rationally coprime integral polynomials | \(2t,2(t-1)\): the product ideal is smaller than the intersection |
| Full Galois coherence | Independently chosen real algebraic-integer eigenvalues | The order-five tuple \((0,0,1,1,0)\) in Section 3 |
| Integral inverse Fourier congruences | Each cyclotomic coordinate is an algebraic integer | \((a,b)=(1,0)\) at \(p=3\) gives coefficients \(1/3\) |
| Simultaneous multi-factor gluing | All original pairwise tests | \((a,c,b)=(0,0,1+i)\) at order four |
| Parity plus exact energy | Exact energy, symmetry, normalization, and separate spectral upper bounds | The order-eleven row (21) |
| Parity plus full Gram | Full Gram, integrality, symmetry, and normalization | The order-three quadruple (30) |
| The affine lattice \(J_m+2L_m\) at even order | Integral gluing and componentwise congruence modulo \(2\) | Four copies of \(2\cdot1\) at order four satisfy every norm equation but fail the half-shift gluing test |
| Odd \(p\) in the componentwise parity lemma | The same mod-two conditions at \(p=2\) | \((a,b)=(2,2)\) gives \((2,0)\) |
| Symmetry or sufficient amicability for the stated Williamson array | Summed Gram equations for nonsymmetric circulant sign rows | The explicit order-three array in Section 6 has a nonzero off-diagonal Gram block |
| Odd \(m\) in the normalized product theorem | Arbitrary \(m\) | At \(m=2\), rows \((1,1),(1,1),(1,-1),(1,-1)\) satisfy the full Gram identity but have product \(+1\) at position \(1\) |
| Normalization in the stated product theorem | Symmetry alone | At \(m=3\), start with \((1,1,1)\) and three \((1,-1,-1)\); negate the first entire row. Gram and symmetry survive, while the nonzero-position products become \(+1\) |

None of these examples rules out a Hadamard matrix at any order.
They identify failures of specified implications and specified
representations. Conversely, Corollary 7 is sufficient precisely
because it restores the lost integral and discrete conditions.

## 9. Exercises with answers

**Exercise 1.** For \(f=t-1,\ g=t^2+t+1\), describe the image of
\(R/(fg)\) in \(\mathbb Z\oplus\mathbb Z[\zeta_3]\).
Reconstruct \((a,b)=(1,1+\zeta_3)\), and decide whether it is integral.

**Answer.** Write \(b=u+v\zeta_3\). The condition is
\(a\equiv u+v\pmod3\). Here \(u+v=2\), so the pair does not
glue. Formula (9) gives
\[
 X=(1+t)-\tfrac13(1+t+t^2)
   =\tfrac23+\tfrac23t-\tfrac13t^2.
 \]
This example also shows why taking a small integral power-basis
representative for \(b\) is not enough.

**Exercise 2.** At \(p=5\), reconstruct the pair
\[
 a=1,\qquad b=-2(\zeta+\zeta^{-1}).
 \]
Check symmetry, normalization, and signs by both direct coefficients
and the spectral tests.

**Answer.** The row is
\((1,-1,1,1,-1)\), since
\(X=T-2(z+z^4)\). Its sum is \(1\), its trace
\(\operatorname{Tr}(b)=4\), and \(\rho(b)=-4=1\) in
\(\mathbb F_5\). Also \(b=\bar b\), \(b\in2O\), and
\[
 \operatorname{Tr}(b^2)
 =4\operatorname{Tr}(\zeta^2+2+\zeta^{-2})
 =4(-1+8-1)=24.
 \]
Thus \(a^2+\operatorname{Tr}(b^2)=25\), as required by (20).

**Exercise 3.** Explain why a four-row prime spectral certificate
cannot check only \(\sum_\ell|b_\ell|^2\le4p\) in one complex
embedding, even when the \(b_\ell\) are individually integral.

**Answer.** The proposed inequality imposes neither equality nor the
augmentation equation, integral gluing, parity, normalization, or
coherent constraints at the other embeddings. The exact identity
\(\sum b_\ell\bar b_\ell=4p\) in \(K\) transports to all
embeddings; a numerical upper bound in one embedding does not.
The examples (21) and (30) show that even much stronger subsets of
the exact conditions can fail to force signs.

**Exercise 4.** Prove that the order-four defect has additive group
\(\mathbb Z/4\oplus\mathbb Z/2\), not \((\mathbb Z/2)^3\).

**Answer.** The cokernel of \(E_4\) has order \(8\). Its first
Smith invariant is \(1\), since it has an entry \(1\); the second
is \(1\), since a \(2\times2\) minor from rows \(1,3\) and
columns \(2,3\) has determinant \(-1\).
Every \(3\times3\) minor is even because \(E_4\) has rank \(2\)
modulo \(2\), and a \(3\times3\) minor (rows \(1,2,3\),
columns \(1,2,3\)) equals \(4\), while the minor using rows
\(1,3,4\), columns \(1,2,3\), equals \(2\).
Thus the third determinantal divisor is \(2\).
The Smith invariants are \(1,1,2,4\).

**Exercise 5.** Why does the positivity argument in Lemma 5 require
integrality or an equivalent lower bound? Give a real symmetric
normalized row of odd length with energy equal to its length that is
not a sign row.

**Answer.** At length \(5\), take
\((1,\sqrt2,0,0,\sqrt2)\). It is symmetric and normalized,
and its energy is \(1+2+2=5\), but its entries are not signs.
Without the integer odd/nonzero condition, an entry can have square
strictly between zero and one, and the minimum-energy proof does
not apply. The example itself also has zero entries and entries of
magnitude greater than one.

**Exercise 6.** Show directly that (35) is weaker than (31), without
using a search or the order-nine fixture.

**Answer.** At odd length \(m=5\), take \(N_1=T-1\) and
\(N_2=N_3=N_4=0\). These are normalized symmetric negative supports,
and their sum modulo two is \(T+1\), so (35) and (36) hold.
The corresponding row sums are \((-3,5,5,5)\), whose squared sum
is \(84\), not \(4m=20\). Thus the frequency-zero consequence of
(31) already fails.

## 10. Verification and source scope

The accompanying [checker](../scripts/check_integral_crt.py) uses exact integer and rational
arithmetic. All twelve check groups passed with SymPy 1.14.0: 129 prime
trace reconstructions (including \(p=2\)); 150 bounded coefficient
parity cases; all component-basis trace inverses at orders
\(1,2,3,4,5,6,8,9,10,11,12\); 81 order-four congruence cases;
66 prime-power gluing probes; Smith invariants at orders four and nine;
and the fixed energy, Gram, affine-lattice, and nonsymmetric-array
counterexamples and exercise calculations involving explicit rows.
The checks are consistency evidence for this exposition; the general
proofs above do not depend on testing finitely many cases.

The strongest formulation here is the all-order affine-lattice
certificate in Theorem 6A, with the normalized symmetric prime
specialization in Corollary 7. These reformulate classical identities
and elementary parity/energy reasoning; no novelty claim is made.
Independent mathematical reviews checked the all-order affine theorem,
the odd-order torsion argument, prime trace formula, even-order boundary,
order-four gluing, prime-power jets, order-nine Smith reduction, and
the nonsymmetric array counterexample. A separate computation using
Ramanujan sums verified both products of the trace-inverse and evaluation
matrices at eleven fixed orders. See the
[continuation review](../PHASE2-REVIEW.md) for the evidence boundary.

For the broader classical integral CRT theory, see Kamalakshya Mahatab
and Kannappan Sampath,
[“Chinese Remainder Theorem for Cyclotomic Polynomials in Z[X]”](https://arxiv.org/abs/1401.7696),
*Journal of Algebra* 435 (2015), 223–262. Their paper studies the full
cyclotomic cokernel and its Smith structure. The elementary special cases
and reconstruction certificates used here are proved explicitly above;
no claim is made that the inspected textbook passages already contain them.
