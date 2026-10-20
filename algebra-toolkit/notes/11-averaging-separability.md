# Repairing linear maps: spectral projection, separability, and averaging

An arbitrary vector-space complement rarely respects an operator or a group
action. There are two ways to repair it. One can solve a separate equation
for the complement, as in the Sylvester calculation, or construct a single
operation that repairs every linear map between modules for the algebra in
question. This chapter constructs the second operation explicitly.

The distinction matters. A particular extension may split even when no repair
defined by a separability tensor exists. Conversely, a repair operation for
modules over a quotient algebra says nothing about extensions whose middle
term is not a module over that quotient.

## Two identities that repair every linear map

Let $A$ be an associative unital algebra over a field $k$. For the moment,
suppose that finitely many elements $a_i,b_i\in A$ satisfy

$$
\sum_i a_i b_i=1,\qquad
\sum_i c a_i\otimes b_i=\sum_i a_i\otimes b_i c
\quad(c\in A).                                      \tag{A1}
$$

The tensor products in this displayed identity are tensor products of
$k$-vector spaces. The order of the two factors in $b_i c$ matters.
For left $A$-modules $M,N$ and a $k$-linear map $f:M\to N$, define

$$
\mathcal A_{M,N}(f)(v)=\sum_i a_i f(b_i v).            \tag{A2}
$$

No dimension assumption on $M$ or $N$ is needed: the sum defining the
repair is finite.

**Repair lemma.** The operation $\mathcal A_{M,N}$ is a $k$-linear
projection

$$
\operatorname{Hom}_k(M,N)\longrightarrow
\operatorname{Hom}_A(M,N).
$$

If $u:M'\to M$ and $v:N\to N'$ are $A$-linear, then

$$
\mathcal A_{M',N'}(vfu)=v\,\mathcal A_{M,N}(f)\,u.    \tag{A3}
$$

**Proof.** Apply the $k$-linear map
$a\otimes b\mapsto a f(bw)$ to the second identity in (A1). It gives

$$
c\,\mathcal A(f)(w)=\sum_i a_i f(b_i c w)
                  =\mathcal A(f)(cw),
$$

so the repaired map is $A$-linear. If $f$ was already $A$-linear,

$$
\mathcal A(f)(w)=\sum_i a_i b_i f(w)=f(w).
$$

These two assertions give $\mathcal A^2=\mathcal A$ and its stated image.
For (A3), move the $A$-linear maps $u,v$ through the scalar actions in
(A2). $\square$

Consider an exact sequence of $A$-modules

$$
0\longrightarrow U\xrightarrow{\iota}V
 \xrightarrow{\pi}W\longrightarrow0.
$$

Choose a $k$-linear section $s:W\to V$ of $\pi$. Then

$$
\pi\mathcal A(s)=\mathcal A(\pi s)
               =\mathcal A(1_W)=1_W.
$$

Thus $\mathcal A(s)$ is an $A$-linear section. A $k$-linear retraction
$r:V\to U$ of $\iota$ is repaired in the same way:
$\mathcal A(r)\iota=1_U$. Consequently every such exact sequence splits
as a sequence of $A$-modules. Ordinary vector spaces admit the initial
section by choosing a basis; finite-dimensionality is not the source of
this splitting theorem.

The identities also explain why averaging a projection works in Maschke's
proof. If $P:V\to V$ has image in an invariant submodule $U$ and is the
identity on $U$, each term in (A2) has image in $U$, and
$\mathcal A(P)|_U=1_U$. These facts imply
$\mathcal A(P)^2=\mathcal A(P)$.

**Boundary.** Averaging is not an algebra homomorphism on
$\operatorname{End}_k(V)$, and it does not preserve arbitrary
idempotents. Over $\mathbb Q$, let
$T=\operatorname{diag}(1,-1)$ and average by
$\mathcal A(f)=(f+TfT)/2$. It removes the off-diagonal entries. Hence

$$
\mathcal A(E_{12})=\mathcal A(E_{21})=0,\qquad
\mathcal A(E_{12}E_{21})=E_{11}.
$$

Moreover, the projection
$Q=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}$ averages to $I/2$,
which is not a projection. Its image was not $T$-invariant. The valid
repair argument uses the invariant target and the identity on that target;
it is not an assertion about arbitrary averages of idempotent matrices.

## What the tensor means

Write

$$
e=\sum_i a_i\otimes b_i^{\mathrm{op}}
\quad\text{in}\quad A^e=A\otimes_k A^{\mathrm{op}}.
$$

The superscript records the opposite multiplication. In $A^e$,

$$
(a\otimes b^{\mathrm{op}})(c\otimes d^{\mathrm{op}})
   =ac\otimes(db)^{\mathrm{op}}.
$$

It acts on $A$ by $(a\otimes b^{\mathrm{op}})x=axb$.
The multiplication map $\mu:A^e\to A$, $\mu(a\otimes b^{\mathrm{op}})=ab$,
is a homomorphism of $A$-bimodules, with the outer bimodule action on its
source. In general it is not a homomorphism of algebras.

The identities (A1) become

$$
\mu(e)=1,\qquad
(c\otimes1)e=(1\otimes c^{\mathrm{op}})e.             \tag{A4}
$$

They imply that
$\sigma(c)=(c\otimes1)e$ is an $A$-bimodule section of $\mu$.
Conversely, such a section gives (A4) on putting $e=\sigma(1)$.
An algebra with this property is called **separable over $k$**.
This is a condition on the algebra together with its ground field.

The name **separability idempotent** is literal:

$$
\begin{aligned}
e^2
 &=\sum_i(a_i\otimes1)(1\otimes b_i^{\mathrm{op}})e\\
 &=\sum_i(a_i b_i\otimes1)e=e.
\end{aligned}
$$

It need not be central in $A^e$. The outer-action identity (A4), rather
than centrality, is what the repair proof needs.

For commutative $A$, the opposite algebra is just $A$, and these
notations simplify. The next construction gives the tensor without choosing
an eigenbasis or passing to a splitting field.

## A divided difference constructs the polynomial repair

Let $m\in k[t]$ be monic of positive degree and suppose

$$
\gcd(m,m')=1.                                      \tag{A5}
$$

Set $S=k[t]/(m)$ and identify

$$
S\otimes_kS=k[x,y]/(m(x),m(y)).
$$

The expression

$$
q(x,y)=\frac{m(x)-m(y)}{x-y}
$$

is a polynomial: division here abbreviates the polynomial identity
$m(x)-m(y)=(x-y)q(x,y)$. The Euclidean algorithm supplies a polynomial
$h$ with $h(t)m'(t)\equiv1\pmod m$. Define

$$
e=q(x,y)h(y)
 =\frac{m(x)-m(y)}{x-y}\,m'(y)^{-1}
\quad\text{in }S\otimes_kS.                         \tag{A6}
$$

The inverse in this formula exists by (A5); it is an inverse in $S$,
not a rational function to be evaluated at a zero of its denominator.

In $S\otimes S$ we have
$(x-y)e=(m(x)-m(y))h(y)=0$. For any polynomial $f$,
$f(x)-f(y)$ is divisible by $x-y$, so

$$
(f(x)-f(y))e=0.
$$

This is precisely the second identity in (A4). The multiplication map
$\mu$ substitutes $x=y=\bar t$, and
$q(t,t)=m'(t)$; hence $\mu(e)=m'(\bar t)h(\bar t)=1$.
Formula (A6) therefore proves all the repair conclusions for $S$-modules.

More concretely, if $T_M$ and $T_N$ satisfy
$m(T_M)=m(T_N)=0$ and
$e=\sum_{i,j}c_{ij}x^i y^j$, then

$$
\mathcal A(f)=\sum_{i,j}c_{ij}T_N^i f T_M^j.         \tag{A7}
$$

The result satisfies $T_N\mathcal A(f)=\mathcal A(f)T_M$. It is a
polynomial construction in the two actions, defined over $k$.

Over a splitting field $K$, write
$m(t)=\prod_{j=1}^d(t-\lambda_j)$ with distinct $\lambda_j$, and let
$e_j(t)$ be the usual Lagrange idempotents. At the pair of roots
$(\lambda_r,\lambda_s)$, formula (A6) is $0$ when $r\ne s$ and $1$
when $r=s$. The evaluation description of
$K[t]/(m)\otimes_KK[t]/(m)$ therefore gives

$$
e=\sum_j e_j\otimes e_j,\qquad
\mathcal A(f)=\sum_j P_j^N fP_j^M,                 \tag{A8}
$$

where $P_j^M=e_j(T_M)$ and $P_j^N=e_j(T_N)$.
The operation keeps the maps between matching eigenspaces and deletes the
maps between different eigenspaces. This is the spectral meaning of the
tensor, but the divided-difference proof did not require roots in $k$.

In the commutative case the tensor is unique. Indeed, if $e,e'$ both
satisfy (A4), moving each factor of a term of $e$ across $e'$ gives
$ee'=\mu(e)e'=e'$. Interchanging them gives $e'e=e$, so commutativity
implies $e=e'$. Interchanging the two tensor factors produces another such
tensor, which is consequently the same tensor.

## Three calculations that can be reconstructed

For $m=t^2-1$ and $\operatorname{char}k\ne2$,
$q=x+y$ and $(2y)^{-1}=y/2$ in $S$. Thus

$$
e=\frac{1+xy}{2},\qquad
\mathcal A(f)=\frac{f+T_N fT_M}{2}.                 \tag{A9}
$$

The projections are $P_\pm=(I\pm T)/2$, and (A8) becomes
$P_+^NfP_+^M+P_-^NfP_-^M$.

For a non-diagonal example over $\mathbb Q$, put

$$
T=\begin{pmatrix}1&2\\0&-1\end{pmatrix},\qquad
U=\mathbb Q e_1,\qquad
P=\begin{pmatrix}1&3\\0&0\end{pmatrix}.
$$

Then $T^2=I$, $P$ projects onto $U$, and

$$
\mathcal A(P)=\frac{P+TPT}{2}
             =\begin{pmatrix}1&1\\0&0\end{pmatrix}.
$$

Its kernel is $\mathbb Q(-1,1)$, the desired invariant complement.
Equivalently, the quotient has operator $-1$; the ordinary section
$s(1)=(0,1)$ repairs to $(-1,1)$.

For $m=t^2+1$ over $\mathbb R$, write $J_M^2=J_N^2=-I$.
Now $(2y)^{-1}=-y/2$, so

$$
e=\frac{1-xy}{2},\qquad
\mathcal A(f)=\frac{f-J_N fJ_M}{2}.                \tag{A10}
$$

This extracts the complex-linear part of a real-linear map between complex
vector spaces. Its complementary part
$(f+J_N fJ_M)/2$ is complex-antilinear. On $\mathbb C$, a real-linear
map has the form $f(z)=az+b\bar z$; (A10) retains $az$. A real
eigenbasis is neither available nor needed.

For a cubic example over $\mathbb Q$, take $m=t^3-2$. Since
$(3y^2)^{-1}=y/6$,

$$
e=\frac{2+x y^2+x^2y}{6},\qquad
\mathcal A(f)=\frac{2f+T_N fT_M^2+T_N^2fT_M}{6}.   \tag{A11}
$$

Multiplying (A11) on the appropriate side by $T_N$ and $T_M$ gives

$$
6\bigl(T_N\mathcal A(f)-\mathcal A(f)T_M\bigr)
=2T_Nf-2fT_M+T_N^3fT_M-T_NfT_M^3=0,
$$

where the final cancellation uses both cubic relations. The repair can
therefore be checked before knowing the eigenvalues of a cubic operator.

Characteristic $2$ itself does not preclude a polynomial repair. For
$m=t^2+t+1$ over $\mathbb F_2$, the derivative is $1$ and
$q=x+y+1$. Thus
$e=1+x+y$ and
$\mathcal A(f)=f+T_N f+fT_M$.
This is a separable quadratic field example in the same characteristic
where $t^2-1$ fails.

## The derivative is the exact obstruction to this tensor

Condition (A5) is necessary as well as sufficient. A useful proof exposes
the role of derivations.

For a commutative $k$-algebra $S$ and an $S$-module $L$, a
$k$-derivation $D:S\to L$ is a $k$-linear map satisfying

$$
D(ab)=aD(b)+bD(a).
$$

Suppose $e=\sum_i a_i\otimes b_i$ satisfies (A4).
Apply $a\otimes b\mapsto aD(b)$ to
$(c\otimes1)e=(1\otimes c)e$. The two sides are

$$
c\sum_i a_iD(b_i)
\quad\text{and}\quad
c\sum_i a_iD(b_i)+\left(\sum_i a_i b_i\right)D(c).
$$

Therefore $D(c)=0$ for every $c$. A separability tensor kills all such
derivations.

For $S=k[t]/(m)$, however, formal differentiation defines

$$
D:S\longrightarrow k[t]/(m,m'),\qquad
D(\bar f)=\overline{f'}.                           \tag{A12}
$$

It is well-defined: replacing $f$ by $f+mh$ changes the derivative by
$m'h+mh'$, which is zero in the target. It obeys the product rule.
If $\gcd(m,m')\ne1$, its target is nonzero and $D(\bar t)=1\ne0$.
Consequently no tensor (A4) exists. We have proved

$$
\boxed{\ k[t]/(m)\text{ is separable over }k
       \iff \gcd(m,m')=1.\ }                       \tag{A13}
$$

This is the elementary content of the differential formula
$\Omega_{S/k}\cong S/(m')\,dt$: differentiating the relation $m(t)=0$
imposes exactly $m'(t)\,dt=0$. No differential-module formalism is needed
for the proof (A12).

For the smallest failure, take the dual numbers
$D_0=k[\epsilon]/(\epsilon^2)$. Write a putative tensor as

$$
e=a+b(\epsilon\otimes1)+c(1\otimes\epsilon)
  +d(\epsilon\otimes\epsilon).
$$

The relation
$(\epsilon\otimes1)e=(1\otimes\epsilon)e$
forces $a=0$ and $b=c$. Its product is then $2b\epsilon$, never $1$.
This argument works in every characteristic. In characteristic $2$,
$t^2-1=(t-1)^2$, so the involution algebra itself becomes this
counterexample after putting $\epsilon=t-1$.

## Splitting over one field is weaker than separability

For a monic polynomial $m$, factor it in $k[t]$ as
$m=\prod_i p_i^{r_i}$ with distinct monic irreducibles $p_i$.
The algebra $S=k[t]/(m)$ is semisimple precisely when every $r_i=1$.
Here is a proof that keeps the field issue visible.

If all $r_i=1$, the polynomial CRT identifies $S$ with the product of
the fields $k[t]/(p_i)$. Every $S$-module decomposes by these central
idempotents, and every submodule has a complement by taking a vector-space
complement over each component field.

If some $r_i\ge2$, consider the component $B=k[t]/(p_i^{r_i})$.
The quotient $B\to B/(p_i)$ has no $B$-linear section. The image of $1$
under such a section would be an element $v\equiv1\pmod{p_i}$ killed
by $p_i$. But $p_i v=0$ in $B$ forces $v$ to be divisible by
$p_i^{r_i-1}$, contradicting $v\equiv1\pmod{p_i}$. Extending this
module structure through the CRT projection gives a nonsplit sequence
of $S$-modules.

This semisimplicity criterion uses irreducible factorization over $k$.
It does not assert that the roots in an algebraic closure are distinct.
The derivative criterion (A13) imposes that stronger requirement.

For example, let

$$
k=\mathbb F_p(s),\qquad m(t)=t^p-s.
$$

Eisenstein at the prime $s$ in $\mathbb F_p[s]$, followed by Gauss's
lemma, proves that $m$ is irreducible over $k$. Thus
$S=k[t]/(m)$ is a field: every sequence of $S$-vector spaces splits.
Nevertheless $m'=0$, so (A12) is a nonzero derivation $S\to S$ and
no separability tensor exists.

For any fixed pair of modules, ordinary vector-space projections onto the
subspace of intertwiners may still be chosen. What fails here is the
separability-tensor construction, which repairs all pairs coherently as in
(A3).

Adjoin an element $\alpha$ with $\alpha^p=s$, and write
$K=k(\alpha)$. Then

$$
K\otimes_k S\cong K[t]/((t-\alpha)^p)
              \cong K[u]/(u^p).
$$

This algebra has a nonsplit sequence with middle term $K[u]/(u^2)$
and trivial one-dimensional end terms. The base change has exposed
nilpotent structure that was invisible to factorization over $k$.

In contrast, a tensor satisfying (A4) survives every extension of the
ground field. Its coefficients can be extended, and the same repair proof
still works. For the polynomial algebras here, separability is equivalent
to semisimplicity after every field extension. One direction follows from
base change of the tensor. For the other, a repeated root over a splitting
field gives a quotient by $(t-\lambda)^2$ and the nonsplitting example
above.

Over a perfect field, every irreducible polynomial is separable, so the
two criteria coincide. Over an imperfect field, “no repeated irreducible
factors in $k[t]$” and “coprime to the derivative” must be kept separate.

## Which extensions is the repair allowed to split?

The previous proof applies to exact sequences **of $S$-modules**.
It requires $m$ to annihilate the middle term, not merely the two end
terms.

Take $R=k[t]$ and $S=R/(t)\cong k$. The exact sequence

$$
0\longrightarrow k
 \xrightarrow{\ 1\mapsto\bar t\ }R/(t^2)
 \xrightarrow{\ \bar f\mapsto f(0)\ }k
 \longrightarrow0                                \tag{A14}
$$

has both end terms annihilated by $t$. It does not split as a sequence
of $R$-modules: any lift of $1$ in the quotient is $1+ct$, and
$t(1+ct)=t\ne0$. Its middle term is not an $S$-module, because $t$
does not act as zero there.

Thus the correct comparison is

$$
\operatorname{Ext}^1_S(k,k)=0,\qquad
\operatorname{Ext}^1_R(k,k)\cong k.
$$

The latter group is computed in the Sylvester/extension chapter. There is
no contradiction. Changing the scalar ring changes which middle terms
are eligible extensions.

This also locates the difference between two splitting mechanisms.
For operators with coprime minimal polynomials on the two end terms,
the Sylvester equation gives a unique invariant section of every
extension with those end actions. The repair in this chapter may allow
the end terms to share eigenvalues, but restricts the entire middle
operator to a separable annihilating polynomial. In that category an
invariant section exists, and its choices need not be unique.

## Maschke's sum is the same tensor construction

Let $G$ be a finite group and suppose $|G|$ is invertible in $k$.
In $A=k[G]$, put

$$
e_G=\frac1{|G|}\sum_{g\in G}
           g\otimes(g^{-1})^{\mathrm{op}}.          \tag{A15}
$$

Its product is $1$. For $h\in G$, reindexing by $r=hg$ gives

$$
\sum_g hg\otimes g^{-1}
 =\sum_r r\otimes r^{-1}h.
$$

Linear extension establishes (A1) for every element of $k[G]$.
The general repair lemma now reads

$$
\mathcal A(f)=\frac1{|G|}
  \sum_{g\in G}\rho_N(g)f\rho_M(g^{-1}).            \tag{A16}
$$

It repairs intertwiners, sections, and retractions simultaneously.
Maschke's invariant-complement theorem is the retraction case. No
irreducible-character theory, radical theory, or classification of
semisimple rings is needed for this proof.

There is also a short converse for the assertion that *every*
$k[G]$-module sequence splits. Give $k$ the trivial action and consider
the augmentation

$$
\varepsilon:k[G]\longrightarrow k,\qquad
\sum_g c_g g\longmapsto\sum_g c_g.
$$

An invariant vector in the left regular representation has all its
coefficients equal, since left multiplication acts transitively on the
group basis. Hence it is $c\sum_g g$. If $|G|=0$ in $k$, every such
vector has augmentation zero. An equivariant section would have to send
$1$ to an invariant vector of augmentation $1$, which is impossible.
Thus the division by $|G|$ marks a genuine obstruction for group algebras.

## A repair without division by a dimension

The group formula should not suggest that every separable algebra needs
the inverse of its dimension. Let $A=M_r(k)$ and denote its matrix units
by $E_{ij}$. For any characteristic,

$$
e=\sum_{i=1}^r E_{i1}\otimes E_{1i}^{\mathrm{op}}    \tag{A17}
$$

is a separability idempotent. Its product is
$\sum_i E_{ii}=I$. For $c=E_{ab}$, both sides of the centralizing
identity are $E_{a1}\otimes E_{1b}$; linearity proves the identity for
every matrix. The repair formula uses no denominator.

The associated module decomposition is equally concrete. Put
$L=E_{11}M$. Then

$$
k^r\otimes_k L\longrightarrow M,\qquad
e_i\otimes v\longmapsto E_{i1}v
$$

is an $A$-module isomorphism, with inverse

$$
m\longmapsto\sum_i e_i\otimes E_{1i}m.
$$

The matrix algebra acts on the $k^r$ factor. These formulas prove that
its modules are built from copies of the standard module, and show
directly why the conclusion still holds when the characteristic divides
$r$. This is the elementary matrix-unit case of the relation between
matrix algebras and their coefficient fields.

## The denominator also remembers integral gluing

The rational involution formula
$e=(1+xy)/2$ has an arithmetic boundary. Work over $\mathbb Z$ with
$A_{\mathbb Z}=\mathbb Z[t]/(t^2-1)$. Rationally its two eigenspaces
are separated by $(1\pm t)/2$. Integrally the evaluation map is

$$
A_{\mathbb Z}\longrightarrow\mathbb Z\oplus\mathbb Z,
\qquad a+bt\longmapsto(a+b,a-b).
$$

Its image consists exactly of pairs congruent modulo $2$; it has index
$2$. This is the resultant obstruction for $t-1$ and $t+1$ in the
integral CRT chapter.

There is no separability tensor over $\mathbb Z$ for this algebra.
Such a tensor would reduce modulo $2$ to one for
$\mathbb F_2[t]/((t-1)^2)$, contradicting the dual-number calculation.
Thus the rational denominator, the integral index, and the repeated root
modulo $2$ describe three aspects of the same failure in this example.
This does not mean that every rational repair of a particular map has
nonintegral coefficients; particular maps may already respect the action.
It means that the universal tensor repair cannot be defined integrally.

## Reconstructive exercises

1. Starting only from (A1), prove the repair lemma and repair both a
   section and a retraction. Explain precisely where the surrounding
   maps must be $A$-linear.
2. Derive (A9), (A10), and (A11) from the divided difference, without
   using eigenvectors. For (A11), verify directly that the repaired map
   intertwines the two cubic operators.
3. Prove that a commutative algebra has at most one separability tensor.
   Identify the tensor for $k^d$ and explain why it deletes maps between
   distinct direct factors.
4. Check that (A12) is independent of the representative of $\bar f$.
   Use it to prove the necessity in (A13). Why does this argument not
   prove that every nonseparable algebra has a nonsplit sequence of its
   own left modules over the original field?
5. Prove that (A14) is nonsplit, then identify the failed hypothesis in
   an attempted application of the repair for $S=k$.
6. Prove the augmentation converse to Maschke. Compare it with the
   denominator-free matrix-unit construction (A17).
7. Explain why the congruence $a+b\equiv a-b\pmod2$ is the entire
   integral obstruction for $\mathbb Z[t]/(t^2-1)$. Relate it to the
   reduction of the derivative $2t$ modulo $2$.

**Answer landmarks.** For 1, use the tensor identity to move the scalar
from the first slot to the input slot, then apply (A3). For 2, invert the
derivative modulo the polynomial before multiplying the divided
difference; the inverses are $y/2$, $-y/2$, and $y/6$, respectively.
For 3, $ee'=e'=e$, and for $k^d$ the tensor is
$\sum_j e_j\otimes e_j$. For 4, the ambiguity is $m'h+mh'$;
the inseparable field $\mathbb F_p(s)[t]/(t^p-s)$ disproves the proposed
stronger conclusion. For 5, $t$ kills both ends but not the middle.
For 6, the regular invariant vectors all have augmentation zero in
modular characteristic, whereas the product in (A17) is $I$ in every
characteristic. For 7, a pair $(u,v)$ reconstructs
$a=(u+v)/2$, $b=(u-v)/2$.

**Sources and scope.** These are standard algebraic mechanisms, presented
here with explicit reconstruction and boundary examples; no novelty claim
is intended. Marcelo Aguiar's original paper
[*A note on strongly separable algebras*, §§1–2](https://pi.math.cornell.edu/~maguiar/strongly.pdf)
states the separability-tensor identities and includes the group-algebra
and matrix-algebra examples. The paper's additional notion of *strong*
separability is not required for the repair lemma. The
[Stacks Project, Lemma 10.143.4](https://stacks.math.columbia.edu/tag/00U3)
identifies finite étale algebras over a field as finite products of finite
separable field extensions; its proof supplies a broader setting for the
polynomial criterion. The arguments above prove the formulas used here
without requiring that general theory. The source-comparison guide
separately locates the directly inspected textbook proofs of polynomial
decomposition and Maschke's theorem.
