# Architecture: structures, maps, and obstructions

## The organizing claim

Much ordinary linear algebra is the study of finite-dimensional vector spaces
with additional structure. The most reusable move is to identify that structure,
declare which maps preserve it, and then ask which familiar constructions remain
available. An abstract tool earns its place when it preserves information or
exposes an obstruction that a coordinate calculation conceals.

Four layers organize the collection:

1. **Linear structure.** Kernels, images, quotients, duals, direct sums, and
   tensor products describe how linear information is discarded, tested,
   assembled, and transported.
2. **An action or a multiplication.** An endomorphism makes a vector space a
   $k[t]$-module. A group action makes it a $k[G]$-module. A bilinear
   multiplication is a map $V\otimes V\to V$ satisfying specified identities.
3. **Decomposition and its obstructions.** Idempotents encode direct sums;
   coprime annihilators produce idempotents; semisimplicity guarantees invariant
   complements. Extensions measure ways in which complements fail to exist.
4. **Variation and locality.** Families of vector spaces introduce bundles and
   sheaves; changing coefficients introduces localization, integrality, and
   arithmetic. A theorem about each individual vector space need not control a
   family or an integral lattice.

These layers are connected, but none erases the others. A classification up to
arbitrary linear isomorphism does not solve a problem about lengths, positive
forms, an integral lattice, or smooth variation.

## The prerequisite map

The following arrows mean a useful prerequisite for the stated destination,
not a claim that every possible approach must take this route.

| Foundation | Construction or theorem it supports | Destination and extra bridge |
| --- | --- | --- |
| Equivalence relations, linear maps, subspaces | Quotients, kernels, first isomorphism theorem | Exact sequences; then modules and abelian categories if needed |
| Bases, linear functionals, quotients | Dual exact sequences, annihilators, evaluation | Adjoints after choosing a form; trace duality after separability |
| Direct sums, polynomial division, Bézout | Coprime primary decomposition | $k[t]$-modules, rational/Jordan forms, commuting operators |
| PID ideals and presentations | Smith normal form, cyclic module decomposition | Integral abelian groups and operator classification; higher-dimensional polynomial rings need different tools |
| Bilinear maps and quotients | Tensor products and Hom–tensor adjunction | Scalar extension, representations, multilinear algebra |
| Tensor algebra and relations | Symmetric and exterior algebras | Polynomial coordinate rings, determinants, differential forms after smoothness |
| Splitting and projective presentations | $\operatorname{Ext}^1$, $\operatorname{Tor}_1$ | Extension obstructions; derived functors after complexes and homotopies |
| Groups, invariant subspaces, duals, tensors | Group representations, Maschke, Schur | Matrix Lie groups after topology and the exponential map; Lie algebra representations after differentiation |
| Finite field extensions and multiplication maps | Norm, trace, separable trace pairing | Lang: integral closure, Dedekind ideals, valuations, completions, ramification |
| Commutative rings, modules, localization | Affine coordinate rings, local rings, tangent spaces | Hartshorne: sheaves, schemes, locally free sheaves, cohomology |
| Real linear maps, inner products, multivariable calculus | Tangent spaces, normal spaces, quadratic forms | Hirsch: manifolds, function-space topology, approximation, transversality, bundles |

An economical order for this study is

$$
\text{maps and quotients}\longrightarrow
\begin{cases}
\text{duality and splitting},\\
\text{polynomials and modules},\\
\text{bilinear maps and tensors}.
\end{cases}
$$

These three paths rejoin at invariant decompositions, determinant lines, forms,
and representations. Exactness becomes useful as soon as a construction stops
preserving injections or an invariant complement fails. There is no need to put
spectral sequences in front of that first obstruction.

## What the collection actually contributes

Xi's 基础代数 I develops the concrete languages of equations, matrix maps,
determinants, polynomial division, roots, symmetric polynomials, and resultants.
Volume II develops vector spaces and operators, but also the metric and geometric
meaning of those objects. Volume III adds transformation groups, representations,
modules, Lie algebra examples, and Galois theory. This is a connected course, not
merely three fragments awaiting replacement by a graduate book.

Grillet is particularly well aligned with the present structural route:
VIII.6–7 connects PID modules to Jordan form, X handles splitting and
projectivity, XI develops Hom and tensors, XII introduces Ext/Tor, and XIII builds
free algebras and their quotients. Hungerford independently recommends PID
torsion modules before his linear algebra chapter (printed p. xviii, PDF p. 15).
This is strong evidence that the module viewpoint is a sound organizational
choice, rather than a gratuitous modernization of the user's plan.

Mac Lane supplies a language for recognizing the same construction in different
categories. His universal arrows and representability are useful after several
concrete examples have been worked through. They do not by themselves provide
Jordan bases, a spectral theorem, or a treatment of Euclidean geometry.

Hilton–Stammbach supplies the next layer when exactness fails: projective
presentations, extension classes, complexes, and derived functors. Its route
through extensions before general derived functors is especially compatible with
a reader coming from linear algebra. Hall turns familiar matrix groups and the
exponential into systematic Lie theory and develops representation theory beyond
the initial $\mathfrak{sl}_2$ example.

Hartshorne and Lang are destinations requiring new bridges. Neither should be
mistaken for an interchangeable abstract-algebra text. Hirsch is a different
destination again: his preface (printed p. vii, PDF p. 8) deliberately avoids
tensors and differential forms, and largely avoids algebraic topology. The
relevant foundations for his approach are geometry, analysis, and topology as
well as linear algebra.

## The memory hierarchy

There are three different things to retain.

**Definitions that reconstruct maps.** Remember the quotient factorization
property, tensor universality, evaluation, and the equations defining a split
sequence or an idempotent. Each tells you how a new map must be defined and what
must be checked for it to exist.

**Theorems whose hypotheses control classification.** Remember finite generation
and the PID hypothesis in the module structure theorem; splitting of the minimal
polynomial for Jordan form; positivity and the base field in the spectral theorem;
invertibility of $|G|$ in Maschke's theorem; separability in trace duality. The
missing hypothesis often explains the entire difficulty.

**Geometric or computational interpretations.** A quotient is not a preferred
complement. A dual is not an inner-product identification. A tensor is not usually
a pure tensor. A canonical form is not a canonical basis. A fiber is not a smooth
bundle, and a finite-dimensional vector space over a number field is not its
integral lattice. These distinctions protect the structural tools from misuse.

## What this architecture does not promise

Two commuting operators give a module over $k[s,t]$, which is generally not a PID.
The one-operator classification therefore does not automatically extend to pairs.
Likewise, finite-dimensionality over $k$ does not make a $k[G]$-module
semisimple, and a bundle of rank $n$ does not automatically possess a global frame.
These are productive boundaries, not reasons to abandon abstraction.

The existing algebra direction has been confirmed as the Hadamard/Williamson
study. Its dedicated bridge locates its Gram matrices, integral cyclic group
algebras, finite-field characters, symmetry quotients, and Boolean constraints
within this map. The other subject bridges retain their independent value;
they are not presented as prerequisites for that particular problem.
