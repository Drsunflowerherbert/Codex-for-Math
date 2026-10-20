# Quotients, duality, and splitting

## Conventions and the type of a map

Throughout the core, $k$ is a field and vector spaces are finite-dimensional
unless a paragraph explicitly removes that hypothesis. Rings are associative
with identity, modules are unital, and modules are left modules unless sides
are specified. A commutative ring is stated when tensor products are themselves
used as modules over that ring. The zero vector space is allowed.

For a linear map $f:V\to W$, $f$ is the map and $f(v)$ is its value at
$v\in V$. Write $\operatorname{im}f\subseteq W$ and
$\ker f\subseteq V$. Composition $g\circ f$ first applies $f$. An equality
between maps includes their domains and codomains; when a subspace is identified
with its image, the inclusion will be stated. This matters especially when
comparing an operator on a quotient with a restriction to a complement.

## Quotients: impose relations once

Let $U\subseteq V$ be a subspace. Define $v\sim w$ if $v-w\in U$ and
$V/U=\{v+U:v\in V\}$. Addition and scalar multiplication of cosets are
well defined because replacing representatives changes the result by an element
of $U$. Let $q:V\to V/U$, $q(v)=v+U$.

**Quotient principle.** For any vector space $X$ and linear map $f:V\to X$,
there is a unique linear map $\bar f:V/U\to X$ with
$\bar f\circ q=f$ if and only if $U\subseteq\ker f$.

**Proof.** Necessity follows from $q(u)=0$ for $u\in U$. Conversely set
$\bar f(v+U)=f(v)$. If $v-w\in U$, then $f(v)=f(w)$; hence this is
well defined. It is linear by the coset operations. Surjectivity of $q$ forces
uniqueness. $\square$

The construction has a concrete description, but its reusable content is the
factorization property. When constructing a map from a quotient, specify its
value on a representative and prove it annihilates the relations. When proving
two maps from the quotient equal, precompose with $q$.

**First isomorphism theorem.** If $f:V\to W$ is linear, then

$$V/\ker f\xrightarrow{\ \widetilde f\ }\operatorname{im}f,
\qquad \widetilde f(v+\ker f)=f(v)
$$

is a canonical isomorphism. It is surjective by definition of the image; its
kernel is zero by definition of $\ker f$. Thus rank–nullity follows from
dimension of a quotient, rather than being an isolated formula.

**Why universal objects are unique.** If $(Q,q)$ and $(Q',q')$ have the same
quotient property for $U\subseteq V$, there are unique maps
$a:Q\to Q'$ and $b:Q'\to Q$ satisfying $a q=q'$ and $b q'=q$.
Then $baq=q$, so uniqueness gives $ba=1_Q$; similarly $ab=1_{Q'}$.
Uniqueness means a unique isomorphism preserving the specified structure, not a
unique bare vector-space isomorphism.

Two useful reconstructions are

$$
U/(U\cap W)\cong (U+W)/W,
\qquad (V/U)/(W/U)\cong V/W\quad(U\subseteq W\subseteq V).
$$

For the first, restrict the quotient map $V\to V/W$ to $U$ and compute its
kernel. For the second, send $(v+U)+(W/U)$ to $v+W$ and apply the quotient
principle twice. These proofs explain the maps as well as the dimensions.

**Recognition signal.** Whenever a problem says “modulo,” identifies choices,
or asserts that a quantity depends only on an equivalence class, a quotient
factorization is present. If an operation is not compatible with the relation,
the quotient does not inherit that operation. For example, $T:V\to V$
induces $\bar T:V/U\to V/U$ precisely when $T(U)\subseteq U$.

## Duality: test vectors by scalar-valued maps

Define $V^*=\operatorname{Hom}_k(V,k)$. For $f:V\to W$ define

$$f^*:W^*\to V^*,\qquad f^*(\lambda)=\lambda\circ f.$$

Then $(g\circ f)^*=f^*\circ g^*$ and $1_V^*=1_{V^*}$.
The reversal is forced by the domains. In dual bases the matrix of $f^*$ is
the transpose of the matrix of $f$; complex conjugation is absent here.

The evaluation map is

$$\epsilon_V:V\to V^{**},\qquad
\epsilon_V(v)(\lambda)=\lambda(v).$$

If $e_1,\ldots,e_n$ is a basis with dual basis $e^1,\ldots,e^n$, then
$\epsilon_V(e_i)$ is the corresponding dual basis of $V^{**}$. Thus
$\epsilon_V$ is an isomorphism. It is natural: for $f:V\to W$,

$$f^{**}\circ\epsilon_V=\epsilon_W\circ f.$$

Indeed, evaluate either side at $v\in V$ and $\lambda\in W^*$; both give
$\lambda(f(v))$. The proof uses a basis to establish invertibility, but the
map itself uses no chosen basis.

There is generally no such preferred identification $V\cong V^*$. A basis
or a nondegenerate bilinear form provides one, and different choices provide
different maps. Naturality of the double dual should not be confused with a
metric on $V$.

For $U\subseteq V$ define its annihilator

$$U^\circ=\{\lambda\in V^*: \lambda(u)=0\text{ for every }u\in U\}.$$

The quotient principle identifies $(V/U)^*$ canonically with $U^\circ$:
pull back along $q$. Restriction to $U$ gives an exact sequence

$$0\longrightarrow(V/U)^*\xrightarrow{q^*}V^*
\xrightarrow{\mathrm{res}}U^*\longrightarrow0.$$

To prove surjectivity of restriction, extend a basis of $U$ to one of $V$,
and prescribe zero on the added vectors. The extension exists; it is usually
not unique. The sequence is canonical even though a chosen splitting is not.

It follows that $\dim U^\circ=\dim V-\dim U$. Under $V\cong V^{**}$,
$(U^\circ)^\circ=U$: inclusion is immediate, and the dimensions agree.
For $f:V\to W$,

$$\ker f^*=(\operatorname{im}f)^\circ,
\qquad \operatorname{im}f^*=(\ker f)^\circ.$$

The second identity follows by factoring a functional vanishing on $\ker f$
through $\operatorname{im}f$ and extending it to $W$. Consequently
$\operatorname{rank}f^*=\operatorname{rank}f$ and row rank equals column
rank. These are manifestations of testing a map by functionals.

**Boundary.** For infinite-dimensional algebraic vector spaces, dualization
of short exact sequences is still exact when bases and their usual choice
principles are available. But $V\to V^{**}$ need not be surjective and
$V^*\otimes W\to\operatorname{Hom}(V,W)$ generally has only finite-rank
maps in its image. Continuous duals in analysis form a different theory; the
algebraic extension argument need not preserve continuity.

## Direct sums and idempotents

The external direct sum $A\oplus C$ has inclusions $i_A,i_C$ and projections
$p_A,p_C$ satisfying

$$p_Ai_A=1_A,\quad p_Ci_C=1_C,\quad p_Ai_C=p_Ci_A=0,
\quad i_Ap_A+i_Cp_C=1_{A\oplus C}.$$

These equations are more useful than the ordered-pair notation: they allow
block matrices and maps to be reconstructed without coordinates. A finite
direct sum is both a product and a coproduct. For infinite families, the direct
sum consists of finitely supported tuples, whereas the product includes all
tuples; they are different constructions.

**Idempotent principle.** For an endomorphism $P:V\to V$, the equation
$P^2=P$ is equivalent to a decomposition

$$V=\operatorname{im}P\oplus\ker P$$

in which $P$ is projection onto the first summand.

**Proof.** Write $v=P(v)+(v-P(v))$; the second term lies in $\ker P$.
If $x=P(y)$ and $P(x)=0$, then $x=P^2(y)=P(y)=0$. Conversely projection
in a direct sum plainly satisfies $P^2=P$. $\square$

This works for modules over any ring. If $P$ commutes with an operator $T$,
both summands are $T$-invariant. Conversely a decomposition into $T$-invariant
summands gives a projection commuting with $T$. Thus finding a decomposition
can be translated into finding idempotents in a commutant.

**Failure of a tempting test.** Pairwise zero intersection of three subspaces
does not imply their sum is direct. In $k^2$, the lines spanned by $e_1$,
$e_2$, and $e_1+e_2$ have pairwise intersection zero, but satisfy a nontrivial
three-term relation. The right test is that the addition map
$\bigoplus_i U_i\to V$ be injective, or that
$U_i\cap\sum_{j\ne i}U_j=0$ for each $i$.

## Splitting: existence versus choice

A short exact sequence

$$0\longrightarrow A\xrightarrow{i}B\xrightarrow{p}C\longrightarrow0$$

means that $i$ is injective, $p$ is surjective, and $\ker p=\operatorname{im}i$.
It splits if there exists a linear section $s:C\to B$ with $p\circ s=1_C$.
In that case

$$F:A\oplus C\to B,\qquad F(a,c)=i(a)+s(c)$$

is an isomorphism preserving the inclusion and quotient maps.

**Proof.** If $F(a,c)=0$, apply $p$ to get $c=0$, then injectivity of $i$
gives $a=0$. For $b\in B$, the element $b-s(p(b))$ lies in $\ker p$,
so is $i(a)$ for a unique $a$. This also describes $F^{-1}$. A retraction
$r:B\to A$, $r i=1_A$, is equivalent: its kernel is a complement to
$i(A)$ and restricts under $p$ isomorphically to $C$. $\square$

Over a field, lift a basis of $C$ to $B$ to obtain $s$. Over a general ring,
the lifts may violate relations in $C$; that is the first source of extension
obstructions.

The set of sections, if nonempty, is an affine space under
$\operatorname{Hom}(C,A)$. For sections $s,s'$, $p(s'-s)=0$, so uniquely
$s'-s=i\circ h$ for $h:C\to A$. Conversely $s+i h$ is a section for any
$h$. This statement holds in module categories with the indicated Hom group.
It precisely locates the ambiguity.

There is no natural complement in general. In the split model $B=A\oplus C$,
the automorphism

$$u_h(a,c)=(a+h(c),c)$$

preserves $i$ and $p$ but sends the section $c\mapsto(0,c)$ to
$c\mapsto(h(c),c)$. Whenever $h\ne0$, no distinguished section can be
invariant under all such structure-preserving automorphisms. A chosen positive
inner product changes the problem: the orthogonal complement then becomes
canonical relative to that extra data.

## What to reconstruct and when

For an ordinary rank problem, first factor through the image. For constraints on
functionals, take annihilators. For a proposed decomposition, construct its
projections and check their equations. For an invariant subspace, ask explicitly
whether the desired complement must preserve an operator or a group action.
The underlying vector-space splitting proves less than an equivariant one.

The main source anchors are Xi II §§1.4–1.6 and 2.4 (printed pp. 14–24,
67–71; PDF pp. 20–30, 73–77), Grillet VIII.2–5 and X.1 (especially
X.1.5, printed p. 395, PDF p. 407), and Mac Lane III.1–2 for the broader
universal-property language. Proofs above are written out independently rather
than inferred from those references.
