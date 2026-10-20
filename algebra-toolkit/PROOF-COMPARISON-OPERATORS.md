# Proof-level comparison: operators and multilinear constructions

This comparison supports a smaller route through the specified topics, not replacement of any whole book. It is based on newly read contiguous proof passages in the supplied editions: Xi Nanhua, *Basic Algebra*, volume II (Science Press, 2018); Thomas W. Hungerford, *Algebra* (the supplied Springer reprint of the 1974 text); and Pierre Antoine Grillet, *Abstract Algebra*, second edition (2007). Page references below give printed pages first and one-based physical PDF positions second. The offsets at these locations are respectively +6, +19, and +12.

**P** means the passage itself was read, including its argument; **V** means a rendered page was inspected; **T** means only a location or declared scope was checked. An image request returning a pointer or a warning does not earn V. The new proof readings below are P. The exact glyphs in Xi's quotient-chain correction and normalized-antisymmetrization displays remain **unverified visually** because the available reader returned extracted text and image pointers or explicit image-unavailable warnings; the prescribed download helper was unavailable. The reconstructed arguments are written independently in consistent notation and checked mathematically; they are not transcriptions.

## 1. Three existence proofs, one closely related uniqueness mechanism

| Source and inspected passage | Hypotheses and actual construction | What it supplies and what it costs |
|---|---|---|
| Xi II §2.4, Theorem 2.44, pp. 68–69; PDF 74–75, P | Finite-dimensional vector space over a field. Proves Cayley–Hamilton by dimension induction. A proper invariant subspace and its quotient give two annihilators whose product kills the whole space. If no proper nonzero invariant subspace exists, every nonzero vector is cyclic; its successive images form a basis, and the companion relation gives the characteristic polynomial. | A linear-algebra proof that precedes Jordan form. Requires quotient operators, the characteristic-polynomial product for a block triangular matrix, and polynomial division, without a PID module classification theorem. |
| Xi II §2.5, Theorems 2.51–2.53, pp. 72–74; PDF 78–80, P | A polynomial \(fg\) annihilates \(T\), with \(\gcd(f,g)=1\). Evaluating a Bézout identity splits the space as \(\ker f(T)\oplus\ker g(T)\). The proof also proves that the other factor acts invertibly on each kernel. Applying this to a split characteristic polynomial gives generalized eigenspaces and their dimensions. | The essential coprime-primary mechanism already appears in operator language. The two-factor lemma itself does not need eigenvalues or algebraic closure. The subsequent Jordan theorem needs splitting over the ground field. |
| Xi II §2.5, Theorems 2.56–2.57, pp. 75–77; PDF 81–83, P | Reduces to nilpotence on each generalized eigenspace. Quotients by a line in the kernel, uses induction to obtain chains downstairs, then changes their lifted generators so that at most one chain absorbs the kernel line. | A direct existence proof over any field for a nilpotent operator; split characteristic polynomial suffices for general Jordan form. It teaches the actual obstruction in lifting a quotient basis. |
| Hungerford IV.6, Lemma 6.8 and Theorem 6.9, pp. 222–223; PDF 241–242, P | For a module killed by \(p^n\), chooses an element of order \(p^n\). An elementary correction produces a nonzero cyclic submodule disjoint from it whenever the module is not cyclic. A maximal disjoint submodule, obtained using Zorn's lemma, is shown to be a complement by applying the same argument in the quotient. Finitely generated primary modules then decompose by induction on their number of generators. | A maximal-order cyclic splitting argument over every PID, not just \(K[t]\). The splitting lemma itself permits modules that are not finitely generated, provided their \(p\)-power exponent is bounded. That extra scope should not be erased by calling it merely another Jordan proof. |
| Grillet VIII.6, Theorems 6.1–6.3, pp. 336–339; PDF 348–351, P | First proves submodules of free PID modules free, with a Zorn argument in the arbitrary-rank statement. For finite free \(F\) and \(M\subseteq F\), maximizes an ideal \(\mu(M)\) among images under maps \(F\to R\). Bézout combinations force divisibility of all coordinates of a suitable \(m\in M\); writing \(m=ae\) gives \(\mu(e)=1\). This splits both \(F\) and \(M\), and rank induction yields a relative basis \(a_i e_i\), with \(a_i\mid a_{i+1}\). Taking a free presentation gives invariant factors. | The relative-basis theorem supplies integral presentations and arbitrary-field rational forms in one route. It needs free modules, quotients, principal ideals, the ascending chain condition for ideals of a PID, and rank. For the finite route, the arbitrary-rank Zorn theorem can be replaced by its finite-rank induction. |

The two PID treatments also use Bézout to obtain primary decomposition: Hungerford IV.6, Theorem 6.7, p. 222/PDF 241; Grillet VIII.6, Proposition 6.5, p. 340/PDF 352. Their statements concern arbitrary torsion modules over a PID. They factor an annihilator of each individual element; they do not assume one polynomial annihilates the entire module. Xi's finite-dimensional application has a common annihilator available from Cayley–Hamilton. These are the same coprime splitting mechanism at different scopes.

### The quotient-lifting step worth retaining

Here is a reconstruction of Xi's existence mechanism, with the delicate exponent made explicit. Let \(N\) be nilpotent and choose \(0\ne w\in\ker N\). In \(V/Kw\), take chains with lifted top vectors \(e_j\) and lengths \(m_j\). Their defects satisfy
\[
N^{m_j}e_j=\alpha_jw.
\]
If every \(\alpha_j=0\), the lifted chains together with \(w\) already give a chain basis. Otherwise choose \(r\) with \(\alpha_r\ne0\) and \(m_r\) maximal among indices having nonzero defect. Keep \(e_r\), extend its chain by one place, and, for \(j\ne r\) with \(\alpha_j\ne0\), replace
\[
e_j\quad\hbox{by}\quad
e'_j=e_j-\frac{\alpha_j}{\alpha_r}N^{m_r-m_j}e_r.
\]
The exponent is nonnegative because of the choice of \(r\), and \(N^{m_j}e'_j=0\). These are invertible elementary changes among the old chain vectors; \(w=\alpha_r^{-1}N^{m_r}e_r\) is now in the extended chain. This explains both why a quotient decomposition need not lift unchanged and how the correction repairs it. It is a useful finite-dimensional precursor to extension problems.

This construction and Hungerford's maximal-order splitting should not be conflated. Xi starts from an arbitrary one-dimensional submodule and repairs the lifted chains. Hungerford first chooses a cyclic submodule of maximal possible order and proves that this chosen submodule splits. The false assertion that **every** cyclic invariant subspace has an invariant complement is used by neither proof.

### A second Xi construction missed by a theorem-only comparison

Xi continues beyond the existence theorem. On pp. 79–81/PDF 85–87, P, he constructs chains from
\[
W_k=\operatorname{im}N^{k-1}\cap\ker N.
\]
One starts with a basis of the deepest nonzero \(W_k\), extends it through the descending filtration, and chooses preimages under the appropriate powers of \(N\). Applying high powers of \(N\) to a putative dependence eliminates successive coefficients. The number of vectors is justified by
\[
\dim W_k=\dim\ker N^k-\dim\ker N^{k-1},
\]
using the surjection \(N^{k-1}:\ker N^k\to W_k\), and then telescoping. This supplies a practical basis-finding procedure and an independence proof. The PID theorem's existence statement alone does not replace that skill.

### Exactly how uniqueness agrees

Xi pp. 77–78/PDF 83–84, P, counts blocks by differences of image dimensions. Grillet VIII.6, Lemma 6.7 and the completion of Theorem 6.3, pp. 340–342/PDF 352–354, P, first counts primary cyclic summands using \(M/pM\) over \(R/(p)\), then applies induction to \(pM\). Hungerford IV.6, Lemmas 6.10–6.11 and Theorem 6.12, pp. 224–225/PDF 243–244, P, explains how to adapt the earlier abelian-group uniqueness argument. That referenced argument was also read: II.2, Theorem 2.6, pp. 78–81/PDF 97–100, P. It detects the number of summands through \(p\)-torsion, then multiplies by a power of \(p\) to contradict the first discrepancy between exponent lists. Over a general PID, residue-field dimension replaces finite cardinality.

An economical common formulation, reconstructed from these arguments, is this. For a finite primary module \(M\simeq\bigoplus_jR/(p^{a_j})\), set
\[
d_k=\dim_{R/(p)}p^{k-1}M/p^kM.
\]
Each summand contributes one dimension precisely when \(a_j\ge k\). Thus \(d_k-d_{k+1}\) is the number of summands of exact exponent \(k\). For \(R=K[t]\) and \(p=t-\lambda\), this becomes Xi's rank formula
\[
b_k=\operatorname{rank}(T-\lambda I)^{k-1}
-2\operatorname{rank}(T-\lambda I)^k
+\operatorname{rank}(T-\lambda I)^{k+1}.
\]
Other primary components contribute equal ranks at all three stages and cancel. Therefore three full uniqueness proofs are unnecessary for theorem coverage; one proof of the residue-field layer count, followed by this translation, supplies the common invariant. For an irreducible polynomial of degree greater than one, \(K\)-dimensions of the layers must be divided by \(\deg p\); pretending that every irreducible is an eigenvalue loses the rational case.

## 2. The replacement map has a genuine boundary

Grillet VIII.7, pp. 342–346/PDF 354–358, P, constructs the \(K[X]\)-action, identifies invariant subspaces as submodules, obtains a nonzero annihilator from finite dimensionality of \(\operatorname{End}_K(V)\), and then applies the elementary-divisor theorem. Polynomial division proves the cyclic basis; replacing \(T\) by \(T-\lambda I\) converts it into a Jordan chain. His displayed main Jordan theorem assumes an algebraically closed field. Its proof also works when the relevant minimal polynomial splits, but that weaker hypothesis is a mathematical sharpening of the displayed statement.

Hungerford VII.4, pp. 355–365/PDF 374–384, P, carries this translation through both invariant factors and elementary divisors. It proves rational canonical form, primary rational form, and the split Jordan specialization. Proposition 4.9, pp. 363–364/PDF 382–383, is an additional computational bridge: it presents the operator module by \(tI-A\), proves exactness by reducing polynomial vectors to constant vectors, and identifies the nonunit Smith entries as the invariant factors. This is more than merely renaming Jordan blocks.

| Learning goal | Coverage that may be compressed after mastery | Material still needed |
|---|---|---|
| Primary decomposition when an annihilator is known | Xi 2.51 and the finite \(K[t]\)-specializations of the two PID primary-decomposition proofs | One explicit Bézout projector calculation; the distinction between coprime and noncoprime factors; the elementwise formulation for arbitrary torsion modules if that scope is wanted |
| Jordan existence over a splitting field | One of the two existence routes suffices for the theorem | Xi's lift-correction argument is a valuable alternate proof; his filtration method should remain a basis-construction exercise |
| Jordan uniqueness and block recovery | The three filtration proofs can be replaced by one common layer argument and translation | Actual rank/nullity calculations; constructing a conjugating basis; field and splitting hypotheses |
| Rational form over an arbitrary field | Xi's split Jordan proof is insufficient | A PID cyclic-decomposition theorem plus polynomial division; a nonsplit example; the \(tI-A\) presentation if effective invariant-factor computation is required |
| Finitely generated modules over a PID | Reading both complete existence proofs is unnecessary for the same classification theorem | Choose one proof; retain Hungerford's bounded-primary splitting lemma as an optional stronger result and Grillet's relative-basis theorem when integral presentations are needed |
| Cayley–Hamilton | Once independently proved, repeated derivations can be shortened | Preserve a coherent dependency order: Xi proves it **before** Jordan; Hungerford derives it from rational form in VII.5, p. 367/PDF 386; Grillet derives it after Jordan and passes to an algebraic closure, pp. 345–346/PDF 357–358 |

In particular, a route that uses Xi's characteristic-polynomial splitting argument to prove Jordan and then uses Jordan as its only proof of Cayley–Hamilton would be circular. One may instead follow Xi's preceding quotient proof, or follow the PID route and establish torsion through linear dependence among \(I,T,T^2,\ldots\).

The exercises are not interchangeable. Xi §2.5, pp. 83–84/PDF 89–90, P, includes explicit Jordan bases, powers, matrix-root equations, the polynomial semisimple/nilpotent decomposition, a commutator condition forcing nilpotence, and the finite exponential/logarithm correspondence. Hungerford VII.4 exercises, pp. 365–366/PDF 384–385, and VII.5 exercises, pp. 369–370/PDF 388–389, P, add invariance of invariant factors under field extension, descent of similarity, rational-form classification with nonsplit polynomials, a commutative-ring Cayley–Hamilton exercise, and norm/trace connections. These are separate destinations, even where some standard tasks overlap. This reading does not claim that every exercise in the chapters has been solved or that every application occurs in only one book.

## 3. Tensor products: the universal property is already proved in Xi

Xi II §6.2, Definition 6.11 and Theorem 6.15, pp. 273–275/PDF 279–281, P, defines a tensor product by a bilinear map whose pairs of basis vectors form a basis. He constructs such a space, proves uniqueness by the basis map, and proves the universal property by assigning the images of those basis tensors. This applies to arbitrary vector spaces with bases: the relevant expansions have finite support. The finite-dimensional qualifications on the adjacent \(\operatorname{Hom}\)-and-dual identifications should not be transferred to the universal property itself.

Hungerford IV.5, pp. 207–211/PDF 226–230, P, and Grillet XI.5, pp. 434–438/PDF 446–450, P, build the tensor product of a right and a left module over an arbitrary ring. Both start with the free abelian group on pairs and quotient by additivity and balancing relations. A balanced map extends to the free group, kills the relation subgroup, and therefore descends uniquely. Grillet motivates this with the same vector-space basis calculation that Xi uses.

The additional content is the applicability to modules without bases, noncommutative sidedness, and the subsequent exactness theory. It is inaccurate to say that one needs a graduate text merely to obtain tensor universality. Once the quotient construction and its factorization proof have been learned in either graduate source, the other construction proof is logically redundant. Xi's coordinate realization is still useful as the explicit free case.

Hungerford's right-exactness proof, p. 210/PDF 229, P, deserves separate retention. Given a surjection \(B\to C\), it constructs the inverse map from \(D\otimes C\) into the quotient of \(D\otimes B\) by the preceding image; independence of a chosen lift is exactly what the quotient enforces. This teaches a use of universality that is not supplied merely by the statement that basis tensors form a basis.

## 4. Exterior algebra: related bases, different constructions and scope

Xi II §6.4, pp. 292–299/PDF 298–305, P, assumes characteristic zero and finite dimension at the section opening. He realizes exterior powers inside tensor powers as alternating tensors and defines the product by normalized antisymmetrization. The associativity proof, pp. 293–295/PDF 299–301, proves that antisymmetrizing within a block and then globally agrees with global antisymmetrization. The ordered-wedge basis proof, pp. 296–297/PDF 302–303, first eliminates repetitions and sorts indices for spanning, then isolates the coefficient of each increasing tensor word for independence. This is a complete basis proof, not just a dimension assertion.

Grillet XIII.4, pp. 524–527/PDF 536–539, P, instead takes
\[
\Lambda(M)=T(M)/(v\otimes v:v\in M)
\]
over a commutative ring with identity. Universality follows by killing the defining ideal. He identifies the degree-\(n\) relation submodule with the span of tensors having repeated entries and proves the universal property for alternating \(n\)-linear maps. For free \(M\), pp. 525–526/PDF 537–538 prove the ordered-wedge basis by describing relations among tensor basis words, grouping the terms caused by repeated general vectors, and splitting off a free complement spanned by increasing words.

Thus both sources prove spanning **and** independence. Xi's independence comes from coefficients in an alternating subspace; Grillet's comes from an explicit quotient and a complement to its relation submodule. Grillet does not need division by \(n!\), characteristic zero, or finite rank for the ordered-basis statement.

A concise bridge between them is an original deduction: when \(n!\) is invertible, normalized antisymmetrization descends from the quotient exterior power to the alternating subspace. Ordered wedge classes map to normalized alternating basis tensors, so the map is an isomorphism in the free finite-dimensional case. Xi's product is normalized accordingly. This does not justify identifying the quotient with an alternating subspace in arbitrary characteristic. In characteristic two, the equation \(u\otimes v=-v\otimes u\) alone does not impose \(u\otimes u=0\); the quotient construction must retain the latter relation.

For a general algebra route, Grillet's quotient construction can be the single main proof. Retain Xi's alternating realization as a characteristic-zero model and as practice in coefficient calculations. Both sources connect the top exterior power with determinants; the proof of the ordered basis does not by itself replace exercises with minors, decomposability, or geometric interpretation. No absence claim about exterior algebra in Hungerford is made: a literal search found no match, which is not proof of noncoverage.

## 5. A smaller coherent route and stopping tests

For the intended bridge from undergraduate linear algebra to modules, use this order:

1. Learn invariant subspaces, quotients, polynomial evaluation, and Bézout. Prove the two-factor kernel decomposition and compute its projectors. If using Xi's route, include the pp. 68–69 Cayley–Hamilton proof before applying the characteristic polynomial.
2. Work through Xi's quotient-lifting Jordan construction once, then prove the common layer-count uniqueness formula. Construct at least one Jordan basis by the \(W_k\) filtration. Further repetitions of Jordan existence and uniqueness may then become short translations.
3. Learn the operator/\(K[t]\)-module dictionary. For broader classification, use **one** finite PID structure proof: Grillet's relative-basis proof is the natural choice when integer lattices, presentations, and rational form are downstream goals. Translate the result to operators with Hungerford VII.4, including the \(tI-A\) presentation. Hungerford's complete alternative IV.6 proof becomes optional proof comparison; its stronger bounded-primary lemma remains available when that generality is needed.
4. Use one balanced-tensor quotient construction and its universal property. Derive the free-basis model, induced maps, and a right-exactness example. Then use the exterior quotient and ordered-basis proof, followed by the characteristic-zero alternation comparison.

These are mastery gates, not estimated reading times:

- **Splitting gate:** for coprime \(f,g\), construct both projectors from a Bézout identity and check their images, kernels, sum, and idempotence. Explain why a vector-space complement need not be \(T\)-invariant.
- **Chain gate:** reconstruct the correction \(e'_j\) without assuming a quotient basis automatically lifts to chains. From nullities distinguish nilpotent block sizes \((4,2,2)\) and \((4,3,1)\), although dimension, characteristic polynomial, minimal polynomial, and eigenspace dimension agree. Their second nullities are respectively \(6\) and \(5\).
- **Rational gate:** treat \(K[t]/((t^2+1)^2)\) over \(K=\mathbb R\), then after extending to \(\mathbb C\). Explain which invariant factors remain the same and which elementary divisors split. Produce a companion matrix and a valid module presentation; merely writing a complex Jordan matrix does not pass.
- **Tensor gate:** define a map out of a tensor product by checking balancing and uniqueness; compute \((R/I)\otimes_R M\simeq M/IM\). Explain the failure of injectivity after tensoring \(2\mathbb Z\hookrightarrow\mathbb Z\) with \(\mathbb Z/2\mathbb Z\).
- **Exterior gate:** prove ordered wedges independent, not just spanning. Explain the role of \(n!\) in Xi's model, and construct \(\Lambda^2(K^2)\) in characteristic two using the repeated-vector relation.

A reader who passes these gates can compress repeated theorem coverage in the inspected portions. The route does not replace metric/spectral geometry, affine or projective geometry, tensor contraction practice, the remaining exercise collections, general ring and module theory, or homological algebra. Its economy comes from choosing one proof per common structural theorem and keeping the alternate constructions that teach a distinct method.

## Evidence boundary

The newly inspected operator passages are Xi II PDF 74–90, Grillet PDF 348–358, Hungerford PDF 237–245 and 374–390, with the referenced Hungerford uniqueness passage PDF 97–100. The new multilinear passages are Xi II PDF 279–281 and 298–305; Grillet PDF 446–450 and 536–539; Hungerford PDF 226–230. The comparison does not promote these ranges into an audit of the surrounding books. Source files and retrieval identifiers are private and are not included here.
