# Exact sequences, extensions, and calibrated homological algebra

## Exactness records how pieces fit

A sequence $A\xrightarrow{f}B\xrightarrow{g}C$ is exact at $B$ if
$\operatorname{im}f=\ker g$. The weaker condition $g\circ f=0$ only
gives containment. The quotient
$\ker g/\operatorname{im}f$ measures the difference.
For a short exact sequence of finite-dimensional vector spaces,
$\dim B=\dim A+\dim C$; the dimension identity alone does not specify
the maps or prove exactness.

An exact sequence of modules splits when its quotient map has a module-linear
section. A module $P$ is projective if every map $P\to C$ lifts across
every surjection $B\to C$. Equivalently every short exact sequence ending
in $P$ splits: apply the lifting property to $1_P$, or form the pullback
of a proposed map along the surjection. A module is projective if and only if
it is a direct summand of a free module. For the nontrivial direction, choose
a free surjection $F\to P$ and split it; for the converse, lift basis
vectors of a free module and restrict the lift to the summand.

All vector spaces over $k$ are free, hence projective. They are also injective:
a map defined on a subspace extends by a basis extension. Consequently

$$\operatorname{Ext}^j_k(V,W)=0,\qquad
\operatorname{Tor}^k_j(V,W)=0\qquad(j>0).$$

One may use the projective resolution concentrated in degree $0$ to see both
vanishings. They are statements about the coefficient ring $k$ and its
module category. They do not imply that every complex of vector spaces is
exact, nor that $\operatorname{Ext}_{k[t]}$ or
$\operatorname{Ext}_{k[G]}$ vanishes.

## The smallest equivariant nonsplitting example

Let $R=k[t]$, $M=R/(t^2)$, and $K=R/(t)$. Define

$$0\longrightarrow K\xrightarrow{i}M\xrightarrow{p}K\longrightarrow0,
\qquad i(a\bmod t)=at\bmod t^2,\quad
p(f\bmod t^2)=f\bmod t.$$

The maps are well defined and $R$-linear; the image of $i$ is exactly the
kernel of $p$. As vector spaces, the sequence splits via
$s(a)=a\bmod t^2$. As modules, it does not split. Any lift of $1\in K$
has the form $1+ct$ in $M$, and

$$t(1+ct)=t\ne0,$$

whereas $t\cdot1=0$ in $K$. Thus no module-linear section exists.
In the vector basis $(t,1)$, multiplication by $t$ has matrix
$\begin{pmatrix}0&1\\0&0\end{pmatrix}$. Its invariant line $kt$ has
no invariant complement. This is the exact same obstruction expressed as a
module extension, a failure of equivariant splitting, or a Jordan block.

The underlying vector-space splitting is useful, but forgetting the action has
discarded the information responsible for the obstruction.

## Extensions and the first Ext group, with an explicit computation

An extension of $M$ by $N$ is a short exact sequence
$0\to N\to E\to M\to0$. Two extensions are equivalent when an
isomorphism of their middle terms commutes with the specified inclusion and
quotient maps and is the identity on $N$ and $M$. Merely having isomorphic
middle modules is a weaker relation. The equivalence classes form
$\operatorname{Ext}^1_R(M,N)$ under Baer sum, with the split extension
as zero. The general equivalence with the derived-functor definition is cited
from Hilton–Stammbach III.1–2; we can construct the important cyclic case
directly.

Let $R$ be a commutative domain, $0\ne f\in R$, and $N$ an $R$-module.
The free resolution

$$0\longrightarrow R\xrightarrow{\times f}R
\longrightarrow R/(f)\longrightarrow0$$

is exact. Apply $\operatorname{Hom}_R(-,N)$. Evaluation at $1$
identifies the two Hom modules with $N$, and the induced map is
multiplication by $f$. Hence

$$\operatorname{Hom}_R(R/(f),N)=\ker(f:N\to N),
\qquad\operatorname{Ext}^1_R(R/(f),N)\cong N/fN,$$

and the positive Ext groups of degree greater than $1$ vanish for this first
argument. The injectivity of $\times f$ uses both the domain and
$f\ne0$ hypotheses; over a ring with zero divisors this two-term complex
may not be a resolution.

The extension meaning of $N/fN$ can be seen without the derived-functor
terminology. For an extension, choose $e\in E$ over $1\bmod f$.
Then $fe=i(n)$ for a unique $n\in N$. Replacing $e$ by $e+i(n_0)$
changes $n$ by $fn_0$. Conversely, for $n\in N$ define

$$E_n=(N\oplus Re)/R(-n,fe),$$

meaning the relation $fe=n$. The copy of $N$ injects because
$rf=0$ forces $r=0$. The quotient is $R/(f)$; every extension has this
form by expressing its elements using $N$ and a lift of $1$. Changes of
the lift give precisely the equivalences $n\sim n+fn_0$.
The zero class permits a lift killed by $f$, and therefore a section.
Pullback followed by addition of the two copies of $N$ sends classes
$[n],[n']$ to $[n+n']$, explaining the addition law.

For $R=k[t]$ and $N=K=R/(t)$ this gives

$$\operatorname{Ext}^1_{k[t]}(K,K)\cong k.$$

The class $a\in k$ has generators $u,e$ and relations
$tu=0$, $te=au$. If $a=0$ it is split. For every $a\ne0$, the middle
module is isomorphic to $R/(t^2)$, but the extension classes for different
$a$ remain different with the endpoints fixed. Thus an extension invariant
contains more information than an isomorphism class of a single operator.

## Tor detects lost injections

Tensor the same free resolution with $N$. Its positive homology is

$$\operatorname{Tor}^R_1(R/(f),N)=\ker(f:N\to N),\qquad
R/(f)\otimes_R N\cong N/fN.$$

The groups of degree greater than $1$ vanish for this first argument.
For $R=\mathbb Z$, $f=m\ne0$, and $N=\mathbb Z/n$,

$$\mathbb Z/m\otimes\mathbb Z/n\cong\mathbb Z/\gcd(m,n),
\qquad
\operatorname{Tor}^{\mathbb Z}_1(\mathbb Z/m,\mathbb Z/n)
\cong\mathbb Z/\gcd(m,n).$$

For the kernel, multiplication by $m$ on $\mathbb Z/n$ kills the subgroup
generated by $n/\gcd(m,n)$, which has that order. This supplies a simple
nonzero Tor example and explains the injection failure after tensoring the
multiplication-by-$m$ sequence.

An obstruction in Ext asks whether maps can lift or extend; an obstruction in
Tor asks what tensoring has collapsed. They are useful descriptions only when
the coefficient ring and the relevant sequence are retained.

## Complexes and homology over a field

A chain complex is a sequence of maps $d_n:C_n\to C_{n-1}$ satisfying
$d_{n-1}\circ d_n=0$. Define

$$Z_n=\ker d_n,\qquad B_n=\operatorname{im}d_{n+1},\qquad
H_n(C)=Z_n/B_n.$$

A chain map $f:C\to D$ satisfies
$d_n^D\circ f_n=f_{n-1}\circ d_n^C$. It carries cycles to cycles and
boundaries to boundaries, hence induces $H_n(f)$. The quotient property
constructs that map, and composition makes homology a functor.

**Why the field does not force zero homology.** The complex with a single
nonzero term $C_0=k$ has $H_0=k$. In a two-term complex
$0\to k^2\xrightarrow{d}k^2\to0$ with
$d(x,y)=(x,0)$, both $H_1$ and $H_0$ have dimension $1$. All vector-space
short exact sequences involved split; the map $d$ still need not have
maximal rank or have image equal to a prescribed cycle space.

In fact splitting gives a normal description of a complex. Choose complements

$$Z_n=B_n\oplus\mathcal H_n,\qquad
C_n=Z_n\oplus L_n.$$

Then $\mathcal H_n\cong H_n(C)$ and
$d_n:L_n\to B_{n-1}$ is an isomorphism: it is injective because
$L_n\cap\ker d_n=0$, and its image is all $B_{n-1}$.
Thus

$$C_n=B_n\oplus\mathcal H_n\oplus L_n,$$

with differential zero on $B_n\oplus\mathcal H_n$ and an isomorphism
from $L_n$ onto $B_{n-1}$. A complex is therefore a direct sum of its
homology with zero differential and two-term contractible pieces, after choices.
The decomposition does not say the homology summands are zero.

More explicitly let $j:\mathcal H\to C$ and $q:C\to\mathcal H$ be
inclusion and projection. Define $s_n:C_n\to C_{n+1}$ as the inverse of
$d_{n+1}:L_{n+1}\to B_n$ on $B_n$, and zero on
$\mathcal H_n\oplus L_n$. Then

$$d_{n+1}s_n+s_{n-1}d_n=1_{C_n}-j_nq_n.$$

This is a chain homotopy from the identity to the projection onto chosen
homology representatives. In particular an acyclic complex of vector spaces is
contractible. Neither the contraction nor representatives are generally natural.
Over $k[t]$, the required invariant complements can fail, so the same
decomposition need not exist in that module category.

## A connecting homomorphism is a controlled lifting construction

Let $0\to A\xrightarrow{i}B\xrightarrow{p}C\to0$ be a short exact
sequence of chain complexes, exact in every degree. If $c\in C_n$ is a
cycle, lift it to $b\in B_n$. Then
$p(d b)=d c=0$, so uniquely $d b=i(a)$ for $a\in A_{n-1}$.
Since $i(d a)=d^2b=0$, injectivity gives $d a=0$. Define

$$\delta:H_n(C)\to H_{n-1}(A),\qquad\delta([c])=[a].$$

A different lift changes $b$ by $i(a_0)$ and therefore changes $a$ by
$d a_0$, a boundary. Changing $c$ by a boundary and lifting its primitive
changes $b$ by a boundary in $B$, which does not alter $a$ except for
the preceding lift ambiguity. Thus $\delta$ is well defined and linear.

The resulting sequence

$$\cdots\to H_n(A)\to H_n(B)\to H_n(C)
\xrightarrow{\delta}H_{n-1}(A)\to H_{n-1}(B)\to\cdots$$

is exact. For example, $\delta([c])=0$ means $a=d a_0$; replacing
$b$ by $b-i(a_0)$ gives a cycle lifting $c$, so $[c]$ comes from
$H_n(B)$. Conversely a cycle lift plainly gives $\delta([c])=0$.
At $H_{n-1}(A)$, a cycle $a$ dies in $B$ precisely when
$i(a)=d b$; then $p(b)$ is a cycle and maps under $\delta$ to $[a]$.
At $H_n(B)$, if $p(b)=d c'$ lift $c'$ to $b'$ and observe that
$b-d b'$ lies in $i(A)$ and is a cycle. These checks prove exactness at
all three kinds of position.

This explains why exact sequences are not decorative notation: the connecting
map measures the obstruction to lifting a cycle as a cycle.

## A sensible stopping point for the homological toolkit

For ordinary finite-dimensional linear algebra, retain exactness, splitting,
the explicit $k[t]/(t^2)$ example, complexes, and the one-step resolution
calculations. Derived functors become worthwhile when a concrete functor fails
to be exact or an equivariant extension remains nonsplit. General spectral
sequences, derived categories, and long resolutions can be deferred until a
specific problem needs them.

For the Hadamard/Williamson direction, a common-lift obstruction is not
automatically an Ext class: sign constraints define a nonlinear finite set,
not a module extension with an identified coefficient category. Calling it
“homological” without constructing that category and obstruction would add a
label without mathematical content.

**Sources.** Grillet X.1, X.3, XI.2, XI.6, and XII.1–5 give the general
framework. Hilton–Stammbach III.1–4 (printed pp. 84–99; PDF pp. 95–110)
is especially useful for extension equivalence and computations; IV.1–4
(printed pp. 117–130; PDF pp. 128–141) supplies complexes, connecting maps,
homotopy, and resolutions. The cyclic extension construction and field-complex
decomposition above are fully derived so the reader can use the ideas before
reading a whole homological algebra text.
