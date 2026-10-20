# Representations and semisimplicity

## An action becomes a module

A representation of a group $G$ on a $k$-vector space is a homomorphism
$\rho:G\to\operatorname{GL}(V)$. Extend linearly to the group algebra
$k[G]$, whose elements are finite sums $\sum_g a_g g$ and whose product
extends the group law bilinearly. Then

$$\left(\sum_g a_g g\right)\cdot v=\sum_g a_g\rho(g)(v)$$

makes $V$ a $k[G]$-module. Conversely such a module restricts to a group
action because $g^{-1}$ supplies the inverse operator. Intertwining maps are
exactly module maps, invariant subspaces are submodules, and irreducible
representations are nonzero simple modules.

For the infinite cyclic group, $k[G]\cong k[t,t^{-1}]$; this describes an
invertible operator. For a cyclic group of order $m$,
$k[G]\cong k[t]/(t^m-1)$; its representations are operators satisfying
$T^m=1_V$. If $\operatorname{char}k$ does not divide $m$, the polynomial
$t^m-1$ is square-free, since its derivative is $mt^{m-1}$. Over a field
containing its roots, such operators are diagonalizable. Both separability and
the splitting field enter this elementary representation example.

## Maschke's averaging argument

**Theorem.** If $G$ is finite and $|G|$ is invertible in $k$, every
invariant subspace of a finite-dimensional representation has an invariant
complement. Hence every finite-dimensional representation is a direct sum of
irreducibles.

**Proof.** Let $U\subseteq V$ be invariant. Choose an ordinary linear
projection $P:V\to U$ with $P|_U=1_U$. Define

$$\overline P=\frac1{|G|}\sum_{g\in G}\rho(g)P\rho(g)^{-1}.$$

Each summand has image in $U$ and is the identity on $U$, so the average
does too; in particular $\overline P^2=\overline P$. Reindexing the sum
proves that $\overline P$ commutes with every $\rho(h)$. Therefore
$\ker\overline P$ is an invariant complement. If $V$ is not irreducible,
split it and repeat, decreasing dimensions. $\square$

The averaged projection depends on the original projection; the theorem asserts
existence, not a preferred decomposition. Over $\mathbb R$ or $\mathbb C$,
one can instead average a positive inner product. It remains positive because
a nonzero vector has a positive contribution in each summand. Its invariant
orthogonal complements prove complete reducibility with a geometric meaning.

**Characteristic failure.** In characteristic $p$, let a generator of
$C_p$ act on $k^2$ by $1+N$, where
$N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$. Since $N^2=0$,
$(1+N)^p=1$ in characteristic $p$ (also when $p=2$). This is a
representation with invariant line $ke_1$ and no invariant complement,
exactly as in the $k[t]/(t^2)$ example. Averaging would require $1/p$.

Finite-dimensional representations of infinite groups need not be semisimple
even over $\mathbb C$: send $n\in\mathbb Z$ to $1+nN$. The same
invariant line fails to split. Finite-dimensionality alone does not remove
extensions.

## Schur's lemma and the role of the field

If $S,T$ are irreducible representations, any intertwiner $f:S\to T$
is either zero or an isomorphism. Its kernel and image are invariant, and
irreducibility forces the result. Thus $\operatorname{End}_G(S)$ is a
division algebra over $k$.

If $k$ is algebraically closed and $S$ is finite-dimensional, every
endomorphism $f$ has an eigenvalue $\lambda$. The intertwiner
$f-\lambda1_S$ has nonzero kernel, so it is zero. Therefore
$\operatorname{End}_G(S)=k1_S$. Neither the algebraic-closure nor
finite-dimensional hypothesis should be suppressed.

Over $\mathbb R$, let $C_4$ act on the plane by a quarter-turn
$J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$. There is no real invariant
line, so the representation is irreducible, but its commuting endomorphisms
include all $aI+bJ$, a copy of $\mathbb C$. Thus “irreducible implies
scalar commutant” is false over $\mathbb R$.

For a finite-dimensional semisimple representation over an algebraically
closed field, let $S_i$ represent the distinct simple types occurring in
$V$. The evaluation map gives the canonical isotypic description

$$\bigoplus_i S_i\otimes_k\operatorname{Hom}_G(S_i,V)
\xrightarrow{\ \sim\ }V,\qquad s\otimes f\longmapsto f(s).$$

The group acts only on the first factor. To prove the map is an isomorphism,
choose a decomposition $V\cong\bigoplus_i S_i^{m_i}$ and use Schur's
lemma: the Hom space for $S_i$ is $k^{m_i}$ and contributes exactly that
summand. The map was specified without this decomposition, so invertibility
does not make the chosen copies canonical. The isotypic subspaces are intrinsic;
a basis of each multiplicity space is not. Their commutant is a product of
matrix algebras $\prod_i M_{m_i}(k)$ after choosing those bases.

## Duals and tensors of representations

Define the dual action by

$$\rho^\vee(g)(\lambda)=\lambda\circ\rho(g^{-1}).$$

The inverse compensates for reversal under duality, ensuring
$\rho^\vee(gh)=\rho^\vee(g)\rho^\vee(h)$. Plain transpose without
the inverse would reverse the group multiplication. In dual bases its matrix
is $\rho(g^{-1})^{\mathsf T}$, without complex conjugation.

For two representations, the diagonal tensor action is

$$g\cdot(v\otimes w)=\rho(g)(v)\otimes\sigma(g)(w).$$

Functoriality proves the group law. The canonical identification
$W\otimes V^*\cong\operatorname{Hom}(V,W)$ carries the action to
$f\mapsto\sigma(g)f\rho(g)^{-1}$. Its invariant vectors are the
intertwiners. This is a practical use of tensor variance, not merely an
alternative notation.

Characters are traces $\chi_V(g)=\operatorname{tr}\rho(g)$. Direct sums
and tensor products satisfy

$$\chi_{V\oplus W}=\chi_V+\chi_W,\qquad
\chi_{V\otimes W}=\chi_V\chi_W.$$

For finite groups over $\mathbb C$, characters determine isomorphism
classes; the full orthogonality theorem proving that statement is a cited
next step, not required to prove the two formulas. In modular characteristic
the ordinary complex character package cannot be copied without changes.

## From groups to Lie algebras: a short concrete bridge

For a differentiable representation of a matrix Lie group, differentiation at
the identity yields a Lie algebra representation
$d\rho:\mathfrak g\to\operatorname{End}(V)$ preserving brackets.
Tensor actions differentiate according to the product rule:

$$X\cdot(v\otimes w)=(X\cdot v)\otimes w+v\otimes(X\cdot w).$$

Thus the Lie algebra operator is $A\otimes I+I\otimes B$, whereas the
group operator is $\rho(g)\otimes\sigma(g)$. Confusing these two
formulas changes the representation. Dualization differentiates to
$X\cdot\lambda=-\lambda\circ d\rho(X)$.

Here is an explicit algebraic example over a characteristic-zero field.
On homogeneous polynomials of degree $m$ in $x,y$, set

$$E=x\frac{\partial}{\partial y},\qquad
F=y\frac{\partial}{\partial x},\qquad
H=x\frac{\partial}{\partial x}-y\frac{\partial}{\partial y}.$$

On the basis $v_j=x^{m-j}y^j$, $0\le j\le m$,

$$Ev_j=jv_{j-1},\qquad Fv_j=(m-j)v_{j+1},\qquad Hv_j=(m-2j)v_j,$$

with missing endpoint vectors interpreted as zero. Direct calculation gives
$[H,E]=2E$, $[H,F]=-2F$, and $[E,F]=H$. This defines a representation
of $\mathfrak{sl}_2$.

It is irreducible. The distinct eigenvalues $m-2j$ of $H$ allow polynomial
projections onto its individual weight spaces by interpolation. A nonzero
invariant subspace therefore contains some $v_j$. Repeated application of
$E$ reaches $v_0$, since the intervening integers are nonzero in
characteristic zero; repeated application of $F$ then reaches every $v_j$.
The argument explicitly explains where small positive characteristic can fail.

Over $\mathbb C$, these are all finite-dimensional irreducible
$\mathfrak{sl}_2$ representations. Hall §4.6 proves this classification
using a highest-weight vector and the commutator identity
$E F^jv=j(m-j+1)F^{j-1}v$ (printed pp. 96–101, PDF pp. 109–114).
The notes above prove the model and its irreducibility, while the exhaustion
statement is cited.

The associated $SU(2)$ representation is $\operatorname{Sym}^m\mathbb C^2$.
The element $-I$ acts by $(-1)^m$, so it descends through
$SU(2)\to SO(3)$ exactly when $m$ is even. Integrating a Lie algebra
representation and descending through a covering are extra global questions;
Lie algebra isomorphisms alone do not identify the corresponding groups or
their representations. Hall's group-versus-Lie-algebra sections and Xi III
§3.6 are useful precisely at this boundary.

**Selective sources.** Xi III §3.2 gives an actual averaging proof
(Theorem 3.20, printed pp. 109–111, PDF pp. 115–117), §3.7 constructs
dual and tensor representations (pp. 152–162, PDF pp. 158–168), and
§4.6 introduces $\mathfrak{sl}_2$ modules (starting p. 215, PDF p. 221).
Grillet IX.2 and IX.7 place these in semisimple module theory.
Hall §§4.3–4.7 gives the finite-dimensional Lie-theoretic version. Compact-group
averaging requires integration and continuity, whereas the finite-group proof
above requires only an invertible group order.

**Terminology warning.** Grillet IX.7 initially uses “irreducible” to mean
indecomposable, that is, admitting no nontrivial invariant direct-sum
decomposition (printed p. 381, PDF p. 393). He explicitly relates that
definition to indecomposable modules on p. 383 (PDF p. 395). This study and
Xi/Hall use the standard invariant-subspace definition, corresponding to a
simple module. They coincide in a semisimple setting, but not for a nontrivial
Jordan block. Thus Grillet IX.7.1, asserting a decomposition of every
finite-dimensional representation into his “irreducibles,” is not the
complete-reducibility theorem with the terminology of these notes. This is a
verified convention difference, not a mathematical counterexample to his stated
definition.
