# Bridges to arithmetic, algebraic geometry, and differential topology

These sections explain how the same constructions lead outward. They are
selective derivations and prerequisite diagnoses, not compressed substitutes for
the destination books. The Hadamard/Williamson bridge follows separately and
uses only the directions that have a concrete role there.

## Finite extensions as linear algebra: trace and norm

Let $L/k$ be a finite field extension of degree $n$. Every $a\in L$
defines the $k$-linear multiplication map

$$m_a:L\to L,\qquad m_a(x)=ax.$$

Define $\operatorname{Tr}_{L/k}(a)=\operatorname{tr}(m_a)$ and
$N_{L/k}(a)=\det(m_a)$. Since $m_{ab}=m_a\circ m_b$ and
$m_{a+b}=m_a+m_b$, norm is multiplicative and trace is $k$-linear.
For $c\in k$, $m_c=c1_L$, so trace is $nc$ and norm is $c^n$.
The map $a\mapsto m_a$ is faithful: evaluate at $1$ to recover $a$.

For $L=k(\alpha)$ with monic minimal polynomial
$f(t)=t^n+a_{n-1}t^{n-1}+\cdots+a_0$, multiplication by $\alpha$
has the companion matrix of $f$. Hence

$$\operatorname{Tr}_{L/k}(\alpha)=-a_{n-1},\qquad
N_{L/k}(\alpha)=(-1)^n a_0.$$

If $L/k$ is separable, let $\Omega$ be an algebraic closure of $k$.
The primitive-element theorem writes $L=k(\alpha)$; it is cited here,
not assumed for inseparable extensions. The polynomial $f$ has distinct roots
$\alpha_1,\ldots,\alpha_n$, and

$$\Omega\otimes_k L\cong\Omega[t]/(f)
\cong\prod_{i=1}^n\Omega$$

by scalar extension and Chinese remaindering. Multiplication by $a$ becomes
diagonal with entries $\sigma_i(a)$ for the $n$ embeddings
$\sigma_i:L\to\Omega$. Trace and determinant are unchanged by scalar
extension of the matrix, so

$$\operatorname{Tr}_{L/k}(a)=\sum_i\sigma_i(a),\qquad
N_{L/k}(a)=\prod_i\sigma_i(a).$$

This is the same polynomial-splitting mechanism used for operators. The new
content is that the regular representation comes from a field multiplication.

The trace pairing $b(a,b)=\operatorname{Tr}_{L/k}(ab)$ is nondegenerate
for finite separable extensions. In the power basis its Gram matrix is
$V^{\mathsf T}V$, where $V_{ij}=\alpha_i^{j-1}$. The Vandermonde
determinant is nonzero because the roots are distinct; therefore its square,
the determinant of the trace Gram matrix, is nonzero. This proves
nondegeneracy even in positive characteristic when the extension is separable;
positivity has no role.

For a finite purely inseparable counterexample, take
$k=\mathbb F_p(s)$ and $L=k(\alpha)$ with $\alpha^p=s$.
In the basis $1,\alpha,\ldots,\alpha^{p-1}$, multiplication by
$\sum_{j=0}^{p-1}a_j\alpha^j$ has every diagonal entry $a_0$;
the other powers produce cyclic shifts. Thus its trace is $pa_0=0$.
The trace pairing is identically zero although $[L:k]=p$. A field extension
being finite does not suffice for trace duality.

Xi III §5.8 (printed pp. 272–278, PDF pp. 278–284) is the immediate
Galois-theoretic source. Lang III.1 (printed pp. 57–62, PDF pp. 71–76)
uses the separable trace pairing to define complementary integral modules.
The latter retains an integral lattice, which is extra information beyond the
$k$-vector space and its nondegenerate pairing.

## Why arithmetic needs more than field extensions

In a number field, the ring of integers is a $\mathbb Z$-module inside
a $\mathbb Q$-vector space. Tensoring with $\mathbb Q$ recovers the
ambient vector space but loses torsion and integral index. For example
$2\mathbb Z\subset\mathbb Z$ becomes an isomorphism after tensoring
with $\mathbb Q$, while its cokernel is $\mathbb Z/2$ before
tensoring. Integral bases and discriminants cannot be read from the rational
vector space alone.

Localizing a commutative ring $R$ at a multiplicative set $S$ produces
$S^{-1}R$ with a map from $R$ making all elements of $S$ invertible.
It is universal for that property. For modules,
$S^{-1}M\cong S^{-1}R\otimes_R M$ and localization is exact.
For instance if a localized element maps to zero, some denominator in $S$
annihilates its original image; multiplying the numerator by that denominator
reduces the kernel assertion to the original exact sequence. This proves the
middle exactness directly, with surjectivity obtained by lifting numerators.

A finitely generated torsion-free module over a Dedekind domain is projective
(Lang I.9, Proposition 26, printed p. 29, PDF p. 43). It need not be free:
a nonprincipal invertible ideal is a rank-one example. Its scalar extension to
the fraction field is one-dimensional, so vector-space dimension misses its
ideal class. Over a PID, this distinction vanishes for finitely generated
torsion-free modules. That is the arithmetic boundary of the elementary
structure theorem.

To read Lang efficiently, the missing bridges are integral dependence and
integral closure, prime ideal factorization in Dedekind domains, discrete
valuations, completions, and local ramification. Some algebraic ingredients
appear in Hungerford VIII and Grillet's commutative algebra chapters; their
existence in a table of contents does not establish complete preparation for
Lang's local and analytic arguments. Lang I.9 explicitly says it is not used
later in that book, so projectivity should be read for this conceptual bridge,
not falsely advertised as a prerequisite for all his subsequent chapters.

## Affine geometry: symmetric algebra, ideals, and tangent vectors

For a finite-dimensional vector space $V$, the affine coordinate algebra is
$\operatorname{Sym}(V^*)$. Imposing polynomial equations amounts to taking
a quotient by an ideal. Over an algebraically closed field, passage between
radical ideals and algebraic sets requires the Nullstellensatz; it is a
substantial theorem, not an immediate consequence of the quotient property.
Nonradical ideals retain nilpotent information invisible to a set of points.

For a finitely generated $k$-algebra $A$ and a $k$-rational point
$x:A\to k$, put $\mathfrak m=\ker x$. A tangent vector at $x$
can be defined as a $k$-linear derivation $D:A\to k$ satisfying

$$D(ab)=x(a)D(b)+x(b)D(a).$$

It vanishes on constants and on $\mathfrak m^2$. Conversely every
functional $\ell:\mathfrak m/\mathfrak m^2\to k$ defines
$D(a)=\ell((a-x(a))\bmod\mathfrak m^2)$. Expanding a product proves
the derivation law, and these assignments are inverse. Thus

$$T_x\operatorname{Spec}A\cong
\operatorname{Hom}_k(\mathfrak m/\mathfrak m^2,k).$$

This statement uses a rational point, so its residue field is $k$. At a
general scheme point the residue field and the relative differential module
must be tracked.

For $A=k[x_1,\ldots,x_n]/I$ at a rational point $a$, expand every
$f\in I$ modulo the square of the maximal ideal:

$$f(a+u)\equiv f(a)+\sum_i
\frac{\partial f}{\partial x_i}(a)u_i\pmod{(u)^2}.$$

The tangent space is the common kernel of these linear equations. For the cusp
$y^2=x^3$ at the origin, there is no nonzero linear equation from its defining
polynomial, so the tangent space is two-dimensional even though the curve has
dimension one. For $A=k[\varepsilon]/(\varepsilon^2)$, the point has a
one-dimensional tangent space despite its underlying point set having one
point. Nilpotents store infinitesimal directions.

Tensor products now do geometric work: affine fiber products are represented
by $A\otimes_R B$. Fibers of a module use $M\otimes_R\kappa(\mathfrak p)$.
Because this tensor operation may fail to preserve injections, flatness is
needed to control families. The finite-dimensional vector-space version of
exactness is insufficient once the coefficient ring varies.

## What the scheme and sheaf bridge adds

Hartshorne II.1–2 introduces sheaves and schemes; II.5 develops sheaves of
modules, and II.8 introduces differentials. These topics add local data and
gluing, not just new names for global vector spaces. A locally free sheaf is
locally a finite direct sum of the structure sheaf; a global free basis is an
extra condition. On an affine scheme, finite locally free sheaves correspond
to finitely generated projective modules, a theorem requiring the
module–sheaf correspondence and its local criteria.

Global sections form a left-exact functor; their higher derived functors are
sheaf cohomology. The obstruction here concerns sheaves and gluing even when
the ground field is a field. It is not contradicted by
$\operatorname{Ext}^j_k(V,W)=0$: these are different categories and different
functors. Hartshorne III.1–3 develops that transition. His introduction marks
externally cited commutative-algebra and homological results with an “A”
instead of proving them all in place (printed pp. xv–xvi, PDF pp. 14–15).
The collection provides many algebraic ingredients, but a reader still needs
localization, local rings, sheaves and stalks, and substantial commutative-algebra
fluency before this becomes a comfortable route.

## Differential topology: linear algebra varies smoothly

For a smooth map $F:M\to N$, differentiation gives maps
$dF_x:T_xM\to T_{F(x)}N$. The chain rule makes differentiation functorial.
At a regular point of a level set $F^{-1}(y)$, the implicit-function theorem
identifies

$$T_xF^{-1}(y)=\ker dF_x.$$

For a smooth embedded submanifold $M\subset N$, there is an exact sequence
of vector bundles over $M$,

$$0\to TM\to TN|_M\to\nu\to0,$$

where $\nu$ is the quotient normal bundle. A Riemannian metric on $N$
identifies it with the orthogonal normal bundle. On a paracompact smooth base,
a smooth positive bundle metric exists by partitions of unity, so every short
exact sequence of smooth vector bundles splits. The splitting need not be
natural without the chosen metric or other extra data.

This is stronger than choosing complements separately at each point: arbitrary
pointwise choices need not vary continuously. Conversely splitting does not
make either summand trivial. A nontrivial line bundle can be a direct summand
of a trivial higher-rank bundle. Smooth variation and a global frame are
different requirements.

Hirsch proves the bundle splitting theorem as IV.2.2 (printed p. 95,
PDF p. 105), using partitions of unity, and defines the orthogonal structure
immediately afterward. This is actual proof coverage, not an analogy inferred
from the chapter title. The necessary new bridges for his development are
multivariable calculus, the inverse/implicit-function theorems, general topology,
manifolds, partitions of unity, and then approximation and transversality.

The Hessian of a smooth real function at a critical point is a symmetric
bilinear form on the tangent space. Its inertia survives coordinate change,
which explains why Sylvester's law underlies the Morse index. The Morse lemma
and Morse theory additionally require analytic and topological arguments;
diagonalization alone does not prove their local normal form or global
conclusions. Hirsch VI is a destination for those arguments.

Exterior algebra can build differential forms once smooth bundles exist, but
Hirsch's preface expressly chooses a route without tensors or differential forms.
It would be misleading to force homological algebra, algebraic geometry, or
tensor calculus into his prerequisite chain. The common foundation is careful
linear geometry; the subsequent methods are genuinely additional.
