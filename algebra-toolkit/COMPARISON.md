# Selective comparison: what can be reorganized, what must be retained

The continuation adds two proof-level supplements:
[operators and multilinear constructions](PROOF-COMPARISON-OPERATORS.md)
and [arithmetic and representations](PROOF-COMPARISON-ARITHMETIC.md).
They broaden the actual proof reading behind this initial overview and
give precise substitution boundaries, dependency risks, and stopping tests.
In particular, Xi supplies two Jordan constructions and both Maschke proofs;
the supplements distinguish those methods from the graduate texts' routes.

## How to read the comparison

The criterion is the user's intended use: rebuilding algebra around reusable
principles, then returning to linear algebra and the Hadamard/Williamson study.
“Covered” has several meanings. A theorem may be stated, proved through a
different construction, left as an exercise, or illustrated geometrically.
These are distinct contributions. A chapter list can establish where to look;
it cannot establish that two books are interchangeable.

Evidence levels and edition/page conversions are in the source ledger. The
comparisons below are selective, and pedagogical judgments are identified as
judgments based on the inspected material. No global difficulty ranking or
exercise-by-exercise replacement audit is claimed.

## Xi I versus the graduate algebra books

Xi I starts with equations and low-order determinants, develops sets and maps,
then connects vector rows/columns, rank, and linear maps before abstract
group/ring/field language. Its Chapter 4 does more than provide a determinant
formula: oriented-volume motivation and multilinearity appear on printed
pp. 75–76 (PDF pp. 81–82), and §4.4 gives multiple characterizations
on p. 93 (PDF p. 99). The surrounding exercises include minor identities.
That material has structural value even when its elementary calculations are
already familiar.

Hungerford III and Grillet III give a broader ring-theoretic organization of
polynomial division and factorization; their later module chapters explain
why a PID is the right setting for one-operator structure. The present study
therefore reorganizes the **use** of Xi I's polynomial arithmetic into Bézout,
Chinese remainder, and annihilator arguments. It does not infer that Xi I's
derivations, examples, or root-location exercises are redundant.

Xi I §7.4 starts with symmetry in roots and elementary symmetric polynomials
(p. 177, PDF p. 183); §7.6 makes common-factor detection into a resultant
matrix (p. 190, PDF p. 196). These are useful links from coefficient
calculations to invariant expressions and elimination. Grillet IV.7's
resultant/discriminant location is verified from contents (p. 176,
PDF p. 188), but its entire proof and exercise treatment was not compared
against Xi's. No preference about replacement follows from that heading alone.

For a returning reader who can prove quotient factorization, rank–nullity,
determinant multilinearity, Euclidean division, and Bézout, much of Xi I can
be used as a reference rather than reread sequentially. That is a competence
criterion for selective study, not a judgment that introductory material lacks
content.

## Xi II and two routes to Jordan form

There is substantial, verified theorem overlap. Xi II Theorem 2.51
(printed pp. 72–73, PDF pp. 78–79) proves the coprime-annihilator split
using Bézout. Theorems 2.52–2.53 build the generalized eigenspaces.
Theorems 2.56–2.57 then establish Jordan form under the actual hypothesis that
the characteristic polynomial splits in the base field. Existence is proved
by quotient induction for nilpotent operators; uniqueness comes from dimensions
of images of powers (pp. 75–77, PDF pp. 81–83). These proof pages were read,
not inferred from the section title.

Grillet VIII.6 proves the PID structure theorem (pp. 336–342,
PDF pp. 348–354) and VIII.7 makes $V$ a $k[t]$-module, proves its
annihilator has a monic generator, and derives primary cyclic blocks and Jordan
bases (pp. 342–346, PDF pp. 354–358). Its sampled proof gives a real
alternative construction, with rational canonical forms and general
coefficient rings naturally close at hand. Hungerford's suggested linear-algebra
course explicitly takes torsion PID modules before VII.1–5 (printed
p. xviii, PDF p. 15); his IV.6 and VII.4–5 locations support the same broad
organization. A detailed proof-by-proof audit of Hungerford VII was not made.

For the user's purpose, the module route is an efficient **structural spine**:
one remembers a module and its annihilator, then recovers the canonical forms.
Xi's route retains pedagogical value: it shows what the projections do inside
the actual vector space and constructs chains through quotients. A reader who
knows only the abstract theorem should still reconstruct one chain and the
kernel-growth count. The two proofs illuminate different failure cases.

## Xi II tensor constructions versus Grillet and Mac Lane

Xi II Definition 6.11 constructs tensor products from a basis criterion,
proves uniqueness, and **proves the universal property** in Theorem 6.15
(pp. 273–275, PDF pp. 279–281). It is inaccurate to say that this book has
only coordinates or no universal-property treatment. Its Hom identification,
scalar extension, functorial maps, Kronecker products, contraction as trace,
and contraction as operator composition are explicit examples
(pp. 274–283, PDF pp. 280–289).

Grillet XI.5 constructs tensor products by generators and relations for a
right module and a left module, proving the balanced universal property
(pp. 434–437, PDF pp. 446–449). XI.6–8 adds right exactness, dual modules,
and flatness. This is a genuine extension of scope: vector-space bases do not
exist for arbitrary modules, and tensoring can destroy injections. The simplest
$\mathbb Z/2$ counterexample explains why that generality matters.

Mac Lane III.1–2 (pp. 55–62, PDF pp. 68–75) identifies universal arrows,
universal elements, and representability, and proves Yoneda. IV.1
(pp. 79–80, PDF pp. 92–93) formulates adjunction, including the Hom–tensor
example. Its contribution is a common recognition language, with careful
naturality. It does not replace tensor calculations or tell the reader which
finite-dimensionality hypotheses can be forgotten.

There is one confirmed scope error: the remark after Xi II Theorem 6.19
(p. 278, PDF p. 284) extends its identification of **all** mixed multilinear
forms to infinite-dimensional spaces. The identity-operator/finite-rank
counterexample in the Hom chapter disproves that extension for the preceding
definition (p. 263, PDF p. 269). This local correction does not invalidate
the finite-dimensional construction, its universality theorem, or the chapter's
examples. The definition and remark were checked as images.

## Exterior algebra: a real change in construction and scope

Xi II §6.4 begins by explicitly assuming characteristic zero and models exterior
powers inside antisymmetric tensors (p. 292, PDF p. 298). Its exterior
product uses the alternation operator. This model naturally continues the
chapter's tensor calculations and geometric language.

Grillet XIII.2–4 builds tensor, symmetric, and exterior algebras by universal
properties and quotient ideals over a commutative ring; the exterior relation
is $v\otimes v=0$ (pp. 518–527, PDF pp. 530–539). The basis and
alternating-map arguments were sampled in the actual proof pages. This quotient
construction is better suited to retaining characteristic $2$ and avoiding
factorial denominators. In characteristic zero, the models are connected by
normalized alternation; normalizations must be translated.

For determinants and minors, Xi I's characterizations and Xi II's geometric
motivation remain helpful. The notes choose the quotient exterior construction
so the rank and Cauchy–Binet arguments work in arbitrary field characteristic.
That is a decision about the desired scope, not an assertion that Xi's stated
characteristic-zero treatment is incomplete on its own terms.

## Metric and geometric material is not superseded by module theory

Xi II Chapter 3 develops real and Hermitian inner products, self-adjoint,
isometric and normal operators, complexification, orthogonal expansion,
projections, least squares, and orthogonal-polynomial examples. The normal
spectral theorem, Theorem 3.62 (pp. 126–128, PDF pp. 132–134), was read
with its proof. This supplies an orthonormal conclusion under a positive metric;
Jordan form supplies a different conclusion under arbitrary basis changes.

The inspected metric exercises include dual-basis transformations and norm
comparisons, providing practice that is not supplied by merely knowing the
module structure theorem. Xi's Chapters 4–5 add affine and Euclidean geometry,
transformation groups, indefinite spaces, quadrics, and projective geometry.
Only their contents and selected contextual passages were audited here, so no
claim that a graduate algebra book covers all their proofs or exercises is
warranted. Their relevance is already concrete in the Hadamard direction:
positive real Gram matrices and exact sign constraints are central, while
similarity alone discards the metric problem.

## Xi III, Grillet, and Hall: symmetry with a terminology trap

Xi III has an actual averaging proof for finite complex representations
(Theorem 3.20, pp. 109–111, PDF pp. 115–117), followed by examples and
remarks about compact groups. Its §3.7 gives dual and tensor representations
(pp. 152–162, PDF pp. 158–168). Its module definitions in §4.4
(pp. 186–188, PDF pp. 192–194) connect groups, algebras and actions.
The rendered pages show substantive construction coverage.

Grillet IX.7 proves the group-algebra correspondence and Maschke under the
field-characteristic condition (pp. 380–384, PDF pp. 392–396). It initially
calls a representation “irreducible” when it is **indecomposable**
(p. 381, PDF p. 393), explicitly making that correspondence on p. 383.
These notes, Xi and Hall use irreducible to mean a nonzero representation
with no proper nonzero invariant subspace. Outside a semisimple setting,
Grillet IX.7.1 must therefore not be read as an unconditional complete
reducibility theorem in the latter terminology. This is a convention
difference verified against a rendered page, not an OCR mistake or a false
theorem under his definition.

Hall §§4.3–4.7 proves unitary splitting, Schur's lemma, and the
$\mathfrak{sl}_2$ classification (pp. 90–101, PDF pp. 103–114).
Its unipotent representation of $\mathbb R$ demonstrates failure of complete
reducibility even over $\mathbb C$. Xi III's §4.6 starts from Lie module
conditions and explicitly points outside that section for enveloping algebra
and PBW theory (pp. 215–216, PDF pp. 221–222). Hall's later PBW,
root-system and highest-weight chapters are verified destinations from contents;
their full proofs were not compared against Xi's later examples or appendix.
Thus “Hall develops a systematic further theory” is supported, while “all
Xi representation examples are replaced” is not established.

For Hadamard/Williamson, the immediately useful representation theory is
finite cyclic characters and simultaneous splitting of the shift operator.
Full compact Lie theory and $\mathfrak{sl}_2$ are enriching branches that can
be deferred for that project.

## Homological and geometric graduate books: bridges, not substitutes

Hilton–Stammbach III.1–4 carefully distinguishes extension equivalence from
middle-module isomorphism and computes cyclic Ext groups
(pp. 84–99, PDF pp. 95–110). Its introduction explains why extensions
precede general derived functors. This is the right added construction when
invariant splitting fails. Over the field alone, positive Ext/Tor vanish;
complex homology remains meaningful. No need for advanced homological machinery
has been demonstrated in the sign-lifting constraints of the Hadamard study.

Hartshorne II.5 and II.8 develop local module data and differential universal
properties (pp. 108–111, 172–174; PDF pp. 123–126, 187–189).
They require sheaves, localization and local rings beyond one-vector-space
arguments. His “A” references make clear that some algebra is cited rather
than rederived. Lang I.9 and III.1 add projectivity over Dedekind rings and
integral trace duality (pp. 29, 57; PDF pp. 43, 71). They require integral
and local arithmetic information that scalar extension forgets.

Hirsch IV.2.2 proves splitting for vector bundles on a paracompact base using
partitions of unity (p. 95, PDF p. 105). This is an important extension of
the linear splitting discussion, while his preface deliberately chooses not
to use tensors or differential forms (printed p. vii, PDF p. 8). An algebraic
prerequisite ladder that makes him depend on those subjects would misrepresent
the actual book.

The practical decision is selective: use Xi for the concrete, metric, and
geometric language; choose Grillet or Hungerford for the module spine; use
Mac Lane to sharpen universal reasoning and Hilton–Stammbach when a real
exactness obstruction appears. Enter Hall, Lang, Hartshorne, and Hirsch along
their particular missing bridges. This is a branching reading plan, not eleven
sequential complete readings.
