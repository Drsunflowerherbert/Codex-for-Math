# Forms, adjoints, and the correct equivalence relation

## Similarity, equivalence, and congruence classify different data

For an endomorphism $T:V\to V$, changing the basis by columns $S$ changes
its matrix from $A$ to $S^{-1}AS$. The source and target are the same
space and use the same changed basis: this is similarity.

For a map $f:V\to W$ with independently changed source and target bases,
the matrix becomes $Q^{-1}AP$. This is matrix equivalence; over a field its
only invariant is rank.

For a bilinear form $b:V\times V\to k$ with matrix $B$,
$b(x,y)=x^{\mathsf T}By$. The same change of vector basis in both arguments
gives $B\mapsto S^{\mathsf T}BS$, called congruence. It is not similarity.
The associated map

$$b^\flat:V\to V^*,\qquad b^\flat(v)(w)=b(v,w)$$

has a dual space as target; the two basis changes are linked by duality.
A nondegenerate form is exactly one for which this map is an isomorphism.
This identification depends on $b$.

For a Hermitian form over $\mathbb C$, this study uses the convention

$$h(x,y)=\overline{x}^{\mathsf T}Hy,$$

conjugate-linear in the first argument and linear in the second, with
$H=\overline H^{\mathsf T}$. The matrix changes by
$H\mapsto S^*HS$ where $S^*=\overline S^{\mathsf T}$.
The map $v\mapsto h(v,-)$ into the algebraic dual is conjugate-linear.
Xi's inner-product convention is linear in the first argument instead; translate
the convention rather than copying an adjoint formula unchanged.

**A decisive example.** Over $\mathbb R$, $I_2$ and $2I_2$ are
congruent via $S=\sqrt2 I_2$, but are not similar because they have different
eigenvalues. Similarly the real symmetric matrices
$\operatorname{diag}(1,-1)$ and $\operatorname{diag}(2,-2)$ have the same
inertia but different similarity classes. A theorem about Jordan form cannot
replace a theorem about forms.

## Symmetric forms and quadratic forms

Assume $\operatorname{char}k\ne2$. A symmetric bilinear form determines
$q(v)=b(v,v)$, and

$$b(v,w)=\frac{q(v+w)-q(v)-q(w)}2.$$

Thus symmetric forms and quadratic forms encode the same data in this
characteristic. In characteristic $2$, $b(v,v)$ can be identically zero for
a nonzero alternating form, and a quadratic form needs its own definition and
polarization theory. Dividing by $2$ conceals an essential hypothesis.

Every symmetric bilinear form over a field of characteristic different from
$2$ has a diagonal matrix in some basis. If $b\ne0$, polarization shows
there is $v$ with $b(v,v)\ne0$. Then for any $w$,

$$w=\frac{b(v,w)}{b(v,v)}v+
\left(w-\frac{b(v,w)}{b(v,v)}v\right)$$

is a decomposition into $kv$ and its $b$-orthogonal complement.
The sum is direct since $b(v,v)\ne0$. Induct on dimension. If the remaining
restriction is zero, it contributes a radical summand. This proof explains both
diagonalization and its field dependence: nonzero diagonal entries can be
rescaled only by squares available in $k$.

Over $\mathbb R$, rescale the nonzero coefficients to $+1$ or $-1$.
The numbers $(p,q,r)$ of positive, negative, and zero coefficients are unique
(Sylvester's law of inertia). To see uniqueness of $p$, the diagonal form has
a positive-definite subspace of dimension $p$. Any subspace of dimension
greater than $p$ meets the span of the negative and zero coordinate vectors
nontrivially by the dimension inequality, and hence cannot be positive definite.
Thus $p$ is the maximal dimension of a positive-definite subspace, an intrinsic
number. The same argument gives $q$, and $r$ is the dimension of the radical.

Over an algebraically closed field of characteristic different from $2$, every
nonzero coefficient is a square, so rank classifies symmetric forms up to
congruence. Over $\mathbb Q$ or a number field, rank alone does not:
square classes and further arithmetic invariants matter. “Diagonal” is not the
same as “classified.”

## Alternating forms and symplectic pairs

A bilinear form is alternating if $b(v,v)=0$ for all $v$. This implies
$b(v,w)=-b(w,v)$ in every characteristic. Conversely skew-symmetry implies
alternation only when $2\ne0$.

If $b\ne0$, choose $u,v$ with $b(u,v)\ne0$ and rescale to
$b(u,v)=1$. The span $P=\langle u,v\rangle$ has matrix
$\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ and is nondegenerate.
For any $w$ define

$$w'=w+b(v,w)u-b(u,w)v.$$

Then $b(u,w')=b(v,w')=0$, so $V=P\oplus P^\perp$.
Induction decomposes an alternating form into symplectic pairs and a zero
radical. Its rank is even, and a nondegenerate alternating space has even
dimension. This argument works in characteristic $2$ with the definition
of alternation retained.

The essential memory is the nondegenerate two-dimensional pair and the
orthogonal-complement induction, not a special sequence of row operations.

## Adjoint operators require a chosen form

Let $h$ be a nondegenerate Hermitian form on a finite-dimensional complex
space. There is a unique $T^\dagger$ such that

$$h(Tv,w)=h(v,T^\dagger w)\qquad(v,w\in V).$$

In a basis with Gram matrix $H$, its matrix is

$$[T^\dagger]=H^{-1}[T]^*H.$$

This proves existence and uniqueness and shows explicitly why the adjoint is
ordinary conjugate transpose only in an orthonormal basis. It also gives

$$\begin{gathered}
(ST)^\dagger=T^\dagger S^\dagger,\qquad
(aS+bT)^\dagger=\bar aS^\dagger+\bar bT^\dagger,\\
(T^\dagger)^\dagger=T.
\end{gathered}$$

For a nondegenerate real symmetric form the analogous formula is
$H^{-1}A^{\mathsf T}H$. The algebraic dual map $T^*$ is defined without
a form and has a different type; the adjoint uses the form to return to $V$.

If $h$ is positive definite, every subspace has a canonical orthogonal
complement relative to $h$. Moreover

$$U\text{ is }T\text{-invariant}
\quad\Longleftrightarrow\quad
U^\perp\text{ is }T^\dagger\text{-invariant}.$$

For example, if $u\in U$ and $w\in U^\perp$,
$h(u,T^\dagger w)=h(Tu,w)=0$. This is the mechanism behind invariant
orthogonal decompositions. For an indefinite nondegenerate form a subspace can
intersect its own orthogonal complement: the isotropic line
$\mathbb R(1,1)$ for $\operatorname{diag}(1,-1)$ does. Nondegeneracy of
the ambient form alone does not give a direct sum with every orthogonal
complement.

## The finite-dimensional spectral theorem, with the hypotheses visible

**Theorem.** On a finite-dimensional positive-definite complex inner-product
space, $T$ has an orthonormal eigenbasis if and only if
$TT^\dagger=T^\dagger T$.

**Proof.** One direction follows from a diagonal matrix and its conjugate
transpose. For the other, call $T$ normal. Any $N=T-\lambda1_V$ is
normal and

$$\|Nv\|^2=h(v,N^\dagger Nv)
=h(v,NN^\dagger v)=\|N^\dagger v\|^2.$$

Hence $Tv=\lambda v$ implies $T^\dagger v=\bar\lambda v$.
The complex characteristic polynomial has a root, so choose a unit eigenvector
$v$. The line $kv$ is invariant under both $T$ and $T^\dagger$;
its orthogonal complement is therefore also invariant under both. The
restrictions commute and are adjoints there, so induction gives the orthonormal
eigenbasis. $\square$

A self-adjoint operator has real eigenvalues: if $Tv=\lambda v$, then
$h(v,Tv)=\lambda\|v\|^2$ is real. A unitary operator has eigenvalues of
modulus $1$ by norm preservation. Real self-adjoint operators admit real
orthonormal eigenbases, for instance by complexifying and observing that real
eigenvalues yield real eigenspaces of the required dimensions. A real normal
operator need not have real eigenvectors: a planar rotation gives a $2\times2$
real block instead. The field and the positive metric are doing actual work.

The nonzero nilpotent matrix $\begin{pmatrix}0&1\\0&0\end{pmatrix}$
has a Jordan basis, but no orthonormal eigenbasis. It is not normal under the
standard positive inner product. A purely module-theoretic classification does
not replace the spectral theorem's metric conclusion.

## Gram matrices, least squares, and determinant bounds

For vectors $v_1,\ldots,v_r$ in a positive inner-product space, their Gram
matrix is $G=(h(v_i,v_j))$. If $X$ is the matrix with these vectors as
columns in an orthonormal basis, then $G=X^*X$. Thus

$$c^*Gc=\left\|\sum_jc_jv_j\right\|^2\ge0,$$

and $G$ is positive definite exactly when the vectors are independent.
This is the correct reason the normal-equations matrix $X^*X$ is invertible
for a full-column-rank least-squares problem. If $X$ is rank deficient,
the minimizer in coefficient space need not be unique, though the orthogonal
projection of the target onto $\operatorname{im}X$ is unique.

Gram–Schmidt writes independent vectors as $X=QR$ with orthonormal columns
of $Q$ and upper triangular $R$. Its diagonal entries are the lengths of
successive orthogonal residuals, so

$$\det G=\prod_j|r_{jj}|^2\le\prod_j\|v_j\|^2.$$

Dependent vectors give determinant zero, so the inequality holds in general.
Equality for nonzero vectors occurs precisely when all projections onto earlier
vectors vanish, equivalently the vectors are pairwise orthogonal. For a square
real matrix this yields Hadamard's determinant inequality
$|\det X|\le\prod_j\|v_j\|$. A sign matrix with orthogonal rows
attains the bound, linking metric geometry directly to the intended Hadamard
problem without using an unnecessary abstraction.

## Affine and projective information that must be retained

For an affine quadratic polynomial
$q(x)=b(x,x)+\ell(x)+c$ in characteristic different from $2$, a
translation $x=y+a$ changes its linear part to
$\ell+2b(a,-)$. If $b$ is nondegenerate one can choose a unique $a$
to cancel that part. If $b$ is degenerate, the component of $\ell$ on
the radical cannot be removed this way and controls further geometric types.
The constant and the permitted transformations also matter. Similarity invariants
of a coefficient matrix do not classify affine quadrics.

Projectivizing identifies nonzero scalar multiples of a vector, and homogeneous
quadratic equations are themselves defined up to nonzero scale. Real points,
signature, isotropic directions, and the distinction between affine and
projective transformations are information a general algebra text may not teach
in the same way as Xi II Chapters 4–5. Those chapters are selectively
deferable for the operator route; their geometric content is not thereby proved
replaceable.

**Source anchors.** Xi II §1.7 (printed pp. 25–43), Chapter 3 (pp. 85–160),
and Chapters 4–5 (pp. 161–262) supply forms, adjoints, metric examples,
orthogonal projection, and geometry. The normal spectral theorem is
Theorem 3.62 (printed pp. 126–128; PDF pp. 132–134). The book comparison
distinguishes these substantial results from the graduate books' module and
category-theoretic strengths.
