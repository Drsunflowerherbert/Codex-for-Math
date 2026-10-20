# Hom and tensor products

## Hom records maps and variance

$\operatorname{Hom}_k(V,W)$ is a vector space under pointwise operations.
Maps $a:V'\to V$ and $b:W\to W'$ induce

$$\operatorname{Hom}(V,W)\to\operatorname{Hom}(V',W'),
\qquad f\longmapsto b\circ f\circ a.$$

The source variable reverses arrows and the target variable preserves them.
For modules over a noncommutative ring, $\operatorname{Hom}_R(M,N)$ is
always an abelian group but generally has no natural left $R$-module structure.
Commutativity or specified bimodule actions must be supplied before treating
it as one.

The kernel universal property gives left exactness. For a short exact sequence
$0\to A\xrightarrow{i}B\xrightarrow{p}C\to0$ of $R$-modules,

$$0\to\operatorname{Hom}_R(X,A)\xrightarrow{i\circ-}
\operatorname{Hom}_R(X,B)\xrightarrow{p\circ-}
\operatorname{Hom}_R(X,C)$$

is exact. A map $X\to B$ killed by $p$ factors uniquely through $i$.
There need not be surjectivity at the right: lifting the identity of $C$
would be a section of $p$. Dually,

$$0\to\operatorname{Hom}_R(C,X)\to\operatorname{Hom}_R(B,X)
\to\operatorname{Hom}_R(A,X)$$

is exact. A map on the submodule $A$ need not extend to $B$.
Over a field both failures disappear, by choosing a splitting. The resulting
exactness is canonical; its proof need not make a canonical choice.

## Tensor universality and a construction

A tensor product of vector spaces $V,W$ is a vector space $V\otimes_k W$
together with a bilinear map
$\tau:V\times W\to V\otimes_k W$ such that every bilinear map
$\beta:V\times W\to X$ factors uniquely as

$$\beta=\widetilde\beta\circ\tau,
\qquad \widetilde\beta:V\otimes_k W\to X\text{ linear}.$$

Write $v\otimes w=\tau(v,w)$. The pair, not the bare vector space, is the
universal object.

For existence, take the free vector space on symbols $[v,w]$ and quotient by
the span of all bilinearity relations:

$$\begin{gathered}
\relax[v+v',w]-[v,w]-[v',w],\quad
[v,w+w']-[v,w]-[v,w'],\\
[av,w]-a[v,w],\quad[v,aw]-a[v,w].
\end{gathered}$$

Every bilinear $\beta$ extends linearly from the symbols and annihilates these
relations, hence factors through the quotient. The symbols span, giving
uniqueness. Universal uniqueness is proved by composing the two comparison maps,
as for quotients.

If $(e_i)$ and $(f_j)$ are bases, then $(e_i\otimes f_j)$ is a basis.
Spanning follows by expansion. For independence, the coefficient maps
$\beta_{ij}(v,w)=e^i(v)f^j(w)$ induce linear functionals on the tensor
product extracting each coefficient of a finite relation. This proof works for
infinite algebraic bases too, because each vector and tensor uses only finite
sums. It does not assert that dual bases span the whole algebraic dual in that
case.

**Recognition signal.** A bilinear expression should usually be turned into a
linear map on a tensor product before choosing coordinates. A formula on pure
tensors defines a linear map only after its bilinearity or balancing has been
checked. Pure tensors span; they are not generally all the elements.

For instance, $e_1\otimes f_1+e_2\otimes f_2$ is not pure when the two
displayed pairs are independent. Under coefficient matrices it has rank $2$,
whereas a pure tensor has entries $v_iw_j$ and rank at most $1$.

## Functorial maps, symmetry, and associativity

For $a:V\to V'$ and $b:W\to W'$, bilinearity gives the unique linear map

$$a\otimes b:V\otimes W\to V'\otimes W',\qquad
(a\otimes b)(v\otimes w)=a(v)\otimes b(w).$$

Checking on pure tensors proves
$(a'\otimes b')\circ(a\otimes b)=(a'\circ a)\otimes(b'\circ b)$.
The same method gives canonical isomorphisms

$$\begin{gathered}
V\otimes W\cong W\otimes V,\qquad
(U\otimes V)\otimes W\cong U\otimes(V\otimes W),\\
k\otimes V\cong V,\qquad
(U\oplus V)\otimes W\cong(U\otimes W)\oplus(V\otimes W).
\end{gathered}$$

These identify objects by specified maps; they are not literal equalities of
set-theoretic constructions. Associativity is especially transparent by observing
that both iterated tensor products represent trilinear maps.

In chosen product bases, the matrix of $a\otimes b$ is the Kronecker product.
If $A$ is $n\times n$ and $B$ is $m\times m$,

$$\operatorname{tr}(A\otimes B)=\operatorname{tr}(A)\operatorname{tr}(B),
\quad \det(A\otimes B)=\det(A)^m\det(B)^n.$$

For trace, sum the diagonal entries $a_{ii}b_{jj}$. For determinant, write
$A\otimes B=(A\otimes I_m)(I_n\otimes B)$; the second factor is a
direct sum of $n$ copies of $B$, and the first is conjugate by the basis
permutation $e_i\otimes f_j\mapsto f_j\otimes e_i$ to a direct sum
of $m$ copies of $A$. This proves the identity over every field and also
over commutative rings. No diagonalization hypothesis is required.

## Currying and the Hom–tensor adjunction

There is a canonical isomorphism, with no finite-dimensional hypothesis,

$$\operatorname{Hom}_k(U\otimes V,W)
\cong\operatorname{Hom}_k(U,\operatorname{Hom}_k(V,W)).$$

It sends $F$ to the map $u\mapsto(v\mapsto F(u\otimes v))$.
Conversely a linear $g:U\to\operatorname{Hom}(V,W)$ yields the bilinear
map $(u,v)\mapsto g(u)(v)$, hence a unique $F$. These operations are
inverse, and pre/postcomposition proves naturality in all variables.

One can remember this as: “a linear map out of a tensor is a bilinear map,
and a bilinear map is a linear family of linear maps.” The adjunction is the
precise version of that sentence, not an extra theorem to memorize separately.

For modules over a commutative ring $R$ the same formulas work. Over a
noncommutative ring one uses a right module and a left module and tracks the
remaining bimodule actions. A correct underlying abelian-group version is

$$\operatorname{Hom}_{\mathbb Z}(M\otimes_R N,A)
\cong\operatorname{Hom}_{R^{\mathrm{op}}}
\bigl(M,\operatorname{Hom}_{\mathbb Z}(N,A)\bigr),$$

where $M$ is right $R$, $N$ is left $R$, and
$(\phi\cdot r)(n)=\phi(rn)$ gives the Hom group its right action.
The tensor represents biadditive maps satisfying
$\beta(mr,n)=\beta(m,rn)$, called balanced maps. Two arbitrary left
modules over a noncommutative ring cannot simply be tensored over $R$ using
the commutative formulas.

## Finite-dimensional Hom as a tensor and trace as evaluation

Define

$$\Theta:W\otimes V^*\to\operatorname{Hom}(V,W),\qquad
\Theta(w\otimes\lambda)(v)=\lambda(v)w.$$

If $V$ is finite-dimensional, its inverse sends
$f$ to $\sum_i f(e_i)\otimes e^i$. Indeed evaluation at
$v=\sum_i e^i(v)e_i$ recovers $f(v)$. Conversely applying the inverse
to a pure tensor recovers it. The inverse expression is basis-independent
because it is the inverse of a specified canonical map. $W$ need not be
finite-dimensional for this result.

For $W=V$, compose $\Theta^{-1}$ with the evaluation contraction
$v\otimes\lambda\mapsto\lambda(v)$. This defines trace invariantly,
and the basis formula is $\operatorname{tr}T=\sum_i e^i(T(e_i))$.
The tensor corresponding to $1_V$ is $\sum_i e_i\otimes e^i$;
it is basis-independent even though each summand is not.

Composition of rank-one maps is

$$\Theta(v\otimes\lambda)\circ\Theta(w\otimes\mu)
=\lambda(w)\Theta(v\otimes\mu).$$

Taking traces gives $\lambda(w)\mu(v)$ in either order. Rank-one maps
span all endomorphisms, so $\operatorname{tr}(ST)=\operatorname{tr}(TS)$.
This is an evaluation identity, which explains why trace is invariant under
similarity and why every commutator has trace zero. The converse is not needed
here, and in positive characteristic trace of the identity can be zero without
the identity being zero.

For infinite-dimensional $V$, every tensor in $W\otimes V^*$ still maps
to a finite-rank operator, and every finite-rank operator arises this way.
The canonical map is injective: express a tensor with linearly independent
$W$-components and use coordinate functionals to show its coefficients vanish
if the operator vanishes. Thus its image is exactly the finite-rank maps.
When $V=W$ is infinite-dimensional the identity is a concrete obstruction to
surjectivity.

This also exposes the issue in Xi II's remark after Theorem 6.19, printed
p. 278 (PDF p. 284). The preceding definition uses **all** multilinear
forms on $V^p\times(V^*)^q$. For $p=q=1$, evaluation
$(v,\lambda)\mapsto\lambda(v)$ is such a form, but it cannot be a
finite sum $\sum_i\alpha_i(v)\lambda(w_i)$: that would represent
$1_V$ as a finite-rank map. The finite-dimensional theorem is sound; its
unqualified infinite-dimensional extension needs to be withdrawn or the tensor
space restricted. The printed remark and definition were both checked as page
images, so this is a mathematical correction, not an OCR inference.

## Exactness, quotients, and change of scalars

Over a field, tensoring is exact. One proof chooses a splitting of a short exact
sequence and uses distribution over direct sums. Alternatively a basis of $W$
identifies $-\otimes W$ with a direct sum of copies of the original map.
These are proofs of a canonical exactness statement, not canonical splittings.

Over a commutative ring, tensoring is always right exact:

$$A\xrightarrow{f}B\longrightarrow C\longrightarrow0
\quad\Longrightarrow\quad
A\otimes N\xrightarrow{f\otimes1}B\otimes N
\longrightarrow C\otimes N\longrightarrow0.$$

To see the kernel, take the quotient of $B\otimes N$ by the image of
$A\otimes N$. Bilinear maps from $B\times N$ vanishing on that image
are precisely the ones factoring through $C\times N$. The quotient and
$C\otimes N$ therefore satisfy the same universal property.
In particular

$$(M/U)\otimes_R N\cong
(M\otimes_R N)/\operatorname{im}(U\otimes_R N).$$

The word “image” matters: the induced map $U\otimes_R N\to M\otimes_R N$
need not be injective. For $0\to\mathbb Z\xrightarrow{\times2}
\mathbb Z\to\mathbb Z/2\to0$, tensoring with $\mathbb Z/2$ turns
the first displayed map into zero. Thus a tensor product does not always
preserve subobjects. A module for which tensoring preserves all short exact
sequences is called flat.

If $L/k$ is a field extension, $L\otimes_k V$ has an $L$-action
$a(b\otimes v)=ab\otimes v$. A $k$-basis $(e_i)$ gives an $L$-basis
$(1\otimes e_i)$, so dimension over the **new** field remains $\dim_k V$.
The map $v\mapsto1\otimes v$ is injective, and scalar extension is exact.
A real operator may acquire eigenvectors after extending to $\mathbb C$;
its complexified invariant decomposition need not descend to real one-dimensional
subspaces. The coefficient field is part of every classification statement.

**Sources.** Xi II §6.2, especially Definition 6.11, Theorem 6.15, and
Examples 6.13–6.14 (printed pp. 273–278; PDF pp. 279–284), contains actual
tensor universality and its applications. Grillet XI.5–8 (printed
pp. 434–456; PDF pp. 446–468) supplies balanced products, general exactness,
dual modules, and flatness. The concrete calculations here show why that extra
generality matters.
