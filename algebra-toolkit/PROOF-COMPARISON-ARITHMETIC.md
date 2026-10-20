# A selective reconstruction of Xi I and III: proof routes, prerequisites, and stopping tests

This comparison asks a local question: which already familiar parts of Xi can a returning undergraduate reconstruct from a smaller collection of proofs, and what would that reconstruction omit? The answer is conditional on competence. It is not a replacement claim about any complete book.

The broadened source reading changes two tempting conclusions. Xi III does **not** stop at the complex inner-product proof of complete reducibility: it also gives the general averaged-projection proof of Maschke. Xi III does **not** introduce modules only as terminology: its module section proves the submodule theorem over a PID and uses a determinant argument to characterize integral elements. A graduate text is useful where it supplies a missing proof or a reusable generalization; its higher placement in a curriculum does not make every local proof shorter.

Evidence follows the existing ledger: **P** = actual statement/proof text read; **V/P** = rendered source page and proof inspected; **T** = contents/location only. Physical PDF pages are one-based. The checked body offsets remain Xi I/III +6, Grillet +12, Hungerford +19, and Lang +14. The supplied Xi III scan has 361 physical pages, although the Library text reader reports only 150. Local rendering recovered the relevant pages; source bytes and rendered evidence remain private.

## 1. The resultant: Xi's matrix construction already supplies an organizing principle

**Xi I §7.6, printed 190–193 / PDF 196–199, V/P.** Definition 7.76 starts with the Sylvester determinant and permits zero leading coefficients in the displayed, fixed-degree coefficient lists. Proposition 7.77 does not merely assert that a resultant detects a common factor. Its proof first converts the question into a bounded-degree relation

\[
f u+g v=0,\qquad \deg u<m,\quad \deg v<n,
\]

where the displayed bounds for \(f,g\) are \(n,m\). Equating coefficients gives a square linear system whose determinant is the resultant, up to the transpose convention visible in the proof. Euclid's lemma supplies the reverse implication when \(f,g\) are coprime. Thus the proof already connects polynomial divisibility, a kernel, and determinant singularity.

There is a real hypothesis issue here, rather than a cosmetic convention. With the nominal coefficient lengths fixed, Xi's criterion includes the alternative that **both displayed leading coefficients vanish**. For instance, if \(f=x+1\) and \(g=x+2\) are both padded to nominal degree two over \(\mathbb Q\), the resulting determinant is zero even though they are coprime. A reconstruction that silently replaces nominal degrees by actual degrees changes the statement.

Proposition 7.78, printed 191–192 / PDF 197–198, then obtains the root-product formula by replacing the roots of \(f\) by independent indeterminates and studying the polynomial \(\operatorname{Res}(F,g-y)\) in \(y\). Its roots are the values \(g(x_i)\); specialization gives the desired identity. The proof uses polynomial arithmetic in a rational-function field, not a prior theory of norms or resultants. Proposition 7.79 derives the discriminant identity. The exercises at printed 193 / PDF 199 include multiplicativity, the discriminant of a product, cyclotomic-looking examples, and elimination in two variables. Reading only the opening matrix definition misses these connections.

**Grillet IV.7, printed 176–179 / PDF 188–191, P.** The direction is reversed. Grillet defines the resultant by the product of differences between roots in an algebraic closure. Proposition 7.2 then proves that it equals the Sylvester determinant, assuming the leading coefficients are nonzero. The proof introduces universal coefficient and root variables over \(\mathbb Z\), shows that each root difference divides the specialized determinant, controls the total degree, and determines the remaining integer constant. The root-product definition makes the vanishing criterion immediate; the longer work is proving that the invariant is a coefficient polynomial.

These are overlapping theorems with different constructions. Xi offers the more immediate route from a concrete linear system to elimination. Grillet offers a universal polynomial identity that survives specialization. Neither route supplies the other perspective merely by stating the same resultant formula. Hungerford was searched for this topic but no exact counterpart was established; that is an access/coverage limit, not evidence that the book contains no relevant material.

**A compact reconstruction.** Define

\[
S_{f,g}:k[x]_{<m}\oplus k[x]_{<n}\longrightarrow k[x]_{<m+n},
\qquad (u,v)\longmapsto fu+gv
\]

for nonzero polynomials of actual degrees \(n,m\). Identify its matrix with the Sylvester matrix, with a recorded ordering/sign convention. Prove \(\ker S_{f,g}\neq0\) exactly when \(\gcd(f,g)\neq1\). Then derive the product formula using either Xi's generic-root argument or Grillet's universal identity. This is a reorganization of inspected proofs, not a newly discovered structure absent from Xi.

The following are useful stopping tests before skipping these pages:

1. Derive the matrix from the map rather than memorizing its rows, and explain why the domain and codomain have the same dimension.
2. Produce the padded-degree counterexample above and state the corrected criterion.
3. Explain why \(x-1\) and \(x+1\) are comaximal in \(\mathbb Q[x]\) but not in \(\mathbb Z[x]\). Their resultant is a nonzero nonunit over \(\mathbb Z\); evaluation at \(1\) and \(-1\) sends \(\mathbb Z[x]/(x^2-1)\) to the pairs of integers with equal parity, not to all of \(\mathbb Z^2\).
4. Recover the discriminant identity, including its sign, and compute one cubic directly.

**Narrow, visually verified erratum.** Xi I Example 7.80, printed 193 / PDF 199, displays \(-2p^3-27q^2\) for the discriminant of \(x^3+px+q\). The correct expression is \(-4p^3-27q^2\). The special case \(x^3+x\), with roots \(0,i,-i\), gives discriminant \(-4\), whereas the displayed expression gives \(-2\). The general cubic exercise on printed 190 / PDF 196 has the correct coefficient \(-4a_0a_2^3\). This is a local example error; it does not invalidate the inspected determinant criterion or product-formula argument.

## 2. Finite fields: the short route must include construction and subfields

### What the inspected books actually prove

**Xi III §1.4 Theorem 1.21, printed 34 / PDF 40, V/P.** The finite multiplicative subgroup theorem uses the maximum order of an element and the polynomial root bound. The step asserting that every element is a root of \(X^r-1\), with \(r\) the maximum order, uses the preceding finite-abelian-group structure, or can be supplied independently by the elementary least-common-multiple lemma below. It is not valid for arbitrary finite groups merely because \(r\) is a maximum.

**Xi III §5.6, printed 260–266 / PDF 266–272, V/P.** Theorem 5.40 recalls multiplicative cyclicity. Theorems 5.41–5.43 establish the prime-power order, uniqueness, and existence. Existence takes a splitting field of \(X^{p^n}-X\), uses derivative \(-1\) for distinct roots, and verifies that the roots form a subfield. Proposition 5.44 at printed 261 / PDF 267 proves the subfield criterion directly: necessity uses the tower dimension; sufficiency uses divisibility of \(X^{p^r}-X\) into \(X^{p^n}-X\) when \(r\mid n\). Theorem 5.45 gives extensions of any finite degree.

At printed 262 / PDF 268, Xi identifies the automorphism group using Frobenius and the already established Galois theorem. It then obtains irreducible polynomials in every degree. Printed 262–266 / PDF 268–272 develops Möbius inversion, cyclotomic polynomials, and the count of monic irreducible polynomials over \(\mathbb F_q\). Thus “replace §5.6 by a finite-field existence theorem” would omit much of the section. The exercises beginning on printed 266 / PDF 272 require minimal polynomials and explicit factorizations, not just theorem recall. The remaining exercise pages 267–269 were not audited.

**Grillet IV.1.6, printed 157 / PDF 169, P.** Cyclicity is proved by decomposing a finite abelian group into its prime-primary subgroups. In each subgroup, a maximal-order element and the root bound force the whole subgroup to be cyclic; the relatively prime orders then combine. This avoids needing the full invariant-factor classification at that point, but it still relies on the earlier primary decomposition.

**Grillet V.1.3, printed 192–193 / PDF 204–205, P.** Existence and uniqueness again use \(X^{p^n}-X\), derivative \(-1\), root-set closure, and uniqueness of splitting fields. Subfield existence/uniqueness, the divisibility criterion, and the intersection formula are **exercises** on printed 193, not locally supplied proofs. A “Grillet replaces Xi §5.6” claim must either solve these exercises or admit that it has traded Xi's written proof for work assigned to the reader.

**Hungerford V.5, printed 279–282 / PDF 298–301, P.** Theorem 5.3 proves cyclicity using the invariant-factor theorem for finite abelian groups: all elements satisfy the polynomial determined by the largest invariant factor, and the root bound rules out more than one nontrivial factor. Proposition 5.6 and Corollary 5.7 provide the same splitting-field construction and uniqueness. Frobenius is introduced in Lemma 5.5; Proposition 5.10 identifies the cyclic Galois group using the fundamental theorem of Galois theory. The construction of fields of orders 9 and 25 is assigned as Exercise 5. Irreducible-polynomial existence is also assigned as a short proof. A local shortcut is possible, but reading these paragraphs as written imports both finite-abelian classification and general Galois theory.

### A smaller undergraduate sequence, with its imports made explicit

For applications needing only finite fields, their cyclic multiplicative groups, Frobenius, and subfields, the following sequence is sufficient:

1. **Polynomial arithmetic and one-root adjunction.** Prove the field property of \(k[x]/(h)\) for irreducible \(h\), the degree/root bound, and the derivative criterion. Construct a splitting field of a fixed polynomial by finitely many successive adjunctions. Prove uniqueness of this finite splitting field by extending an isomorphism one root at a time. An algebraic closure, Zorn's lemma, and the full Galois correspondence are unnecessary for this finite task.
2. **Root-set field construction.** Carry out the proof for \(X^{p^n}-X\) completely. Do not start by choosing an irreducible polynomial of degree \(n\) unless its existence has already been proved; that would conceal the main existence problem.
3. **Cyclicity from element orders.** In a finite abelian group, elements of orders \(a,b\) yield an element of order \(\operatorname{lcm}(a,b)\): for each prime, retain from one of them a power with the largest required prime-power order, then multiply these commuting components of pairwise coprime orders. Iteration shows that the exponent is attained by an element. Applied to a finite multiplicative subgroup of a field, the root bound for \(X^e-1\) gives \(|G|\le e\), while the element of order \(e\) gives \(e\le |G|\). No classification theorem is needed.
4. **Subfields by polynomial divisibility.** Use Xi's direct proof of Proposition 5.44. Uniqueness follows because a subfield of order \(p^r\) must be exactly the roots of \(X^{p^r}-X\) inside the larger field. Intersections follow by the same root-set description or the Euclidean algorithm for these polynomials.
5. **Frobenius without full Galois theory.** In \(\mathbb F_{p^n}\), Frobenius has order \(n\): its \(n\)-th power is the identity and a smaller positive power cannot fix all \(p^n\) elements by the root bound. Choose a generator \(\alpha\) of the multiplicative group, so the field is \(\mathbb F_p(\alpha)\). Its minimal polynomial has degree \(n\); an automorphism is determined by its image of \(\alpha\), with at most \(n\) choices. The \(n\) Frobenius powers therefore exhaust the automorphisms.

This sequence is genuinely smaller in prerequisites than importing a full abstract-algebra chapter. It is not much smaller than the relevant core pages of Xi once those earlier facts are available. It also does not replace the Möbius-counting and cyclotomic portions.

**Stopping tests.** Construct \(\mathbb F_9=\mathbb F_3[u]/(u^2+1)\); prove the defining polynomial irreducible; show \(1+u\) has order eight; compute Frobenius on \(a+bu\). Explain why \(\mathbb F_{p^6}\) has a unique subfield of order \(p^2\) and none of order \(p^4\). For the counting portion, independently derive

\[
q^m=\sum_{d\mid m}dN_d,\qquad
N_m=\frac1m\sum_{d\mid m}\mu(m/d)q^d,
\]

where \(N_d\) counts monic irreducible degree-\(d\) polynomials. A reader who can only quote cyclicity and field uniqueness has not yet passed these construction tests.

## 3. Representations and modules: Xi already contains both averaging proofs

**Xi III §3.2, printed 109–115 / PDF 115–121, V/P.** Theorem 3.20 averages a positive Hermitian form to make a finite-dimensional complex representation unitary. The accompanying remarks distinguish real orthogonal representations, compact-group integration, and the practical problem of finding a useful matrix change of basis. Example 3.22, printed 111–113 / PDF 117–119, explicitly splits the permutation representation of \(S_3\), writes the two-dimensional matrices, and changes bases to geometric and eigenvector coordinates.

The crucial additional pages are printed 113–115 / PDF 119–121. Theorem 3.24 states complete reducibility in characteristic zero or characteristic not dividing \(|G|\), and gives **two proofs**:

- Over \(\mathbb C\), the averaged Hermitian form makes the orthogonal complement of an invariant subspace invariant.
- Over any allowed field, start with an arbitrary vector-space projection \(\theta\) onto the invariant subspace \(U\), and average its conjugates:

  \[
  P(v)=|G|^{-1}\sum_{g\in G}g\,\theta(g^{-1}v).
  \]

  Xi proves \(P|_U=1\), constructs \(V=U\oplus\ker P\), and checks invariance of the kernel by reindexing. The text then distinguishes the nonuniqueness of individual summands from the later uniqueness of isotypic data.

Therefore a comparison based only on printed 109–111 would understate Xi's algebraic proof content.

**Grillet IX.7, printed 381–386 / PDF 393–398, P.** The group algebra is constructed from the group basis and its universal extension property. Propositions 7.2–7.3 prove the correspondence between representations and modules, including equivalence/isomorphism and invariant-subspace/submodule compatibility. Theorem 7.4, printed 383–384 / PDF 395–396, averages a projection just as Xi does, with an equivalent placement of inverses. Its additional organization is to conclude semisimplicity of \(k[G]\), and then use the preceding theory of semisimple rings for classification consequences.

There are two different reading tasks here. The local representation/module dictionary and projection proof require only basic linear algebra, finite sums, module definitions, and invertibility of \(|G|\). The subsequent matrix-algebra decomposition, counts of irreducibles, and center arguments invoke the developed semisimple-ring theory. They do not arrive for free from the one-page averaging proof.

Terminology must also be translated: Grillet's definition on printed 381 uses “irreducible” for what standard module language calls **indecomposable**. The text explicitly identifies this with indecomposability on printed 383. This does not contradict its results, but it can produce false comparisons with Xi's absence-of-proper-invariant-subspaces definition unless the semisimplicity hypothesis has already been imposed.

**Hungerford IX.5, Proposition 5.8, printed 454–455 / PDF 473–474, P.** This is a materially different proof, labeled a sketch. The regular representation realizes elements of the group algebra as matrices. An element of the Jacobson radical can be normalized to have identity coefficient one. The radical is nilpotent because the algebra is Artinian, so its matrix has trace zero; the regular-representation calculation instead makes that trace \(|G|\), giving a contradiction when \(|G|\neq0\) in the field. For the converse, the sum of all group elements generates a nonzero square-zero ideal when the characteristic divides the group order.

This is an efficient synthesis **after** radicals and Artinian ring theory. It is not the shorter elementary proof for a reader who has not learned those theories. The following matrix-algebra decomposition also invokes preceding structure theorems.

### What the module chapter adds—and where a gap remains

**Xi III §4.4, printed 186–196 / PDF 192–202, V/P.** Besides module definitions, quotients, kernels, annihilators and Schur's lemma, the section develops finite free modules and their mapping property. Proposition 4.46 discusses uniqueness of rank, including the distinction between domains, commutative rings, and general noncommutative rings. Theorem 4.47, printed 193 / PDF 199, proves that a submodule of a finite-rank free module over a PID is free, by projecting onto a rank-one quotient and lifting a basis. This is a genuine construction.

At printed 194 / PDF 200, the general cyclic decomposition with nested annihilators is stated, with references to the previously developed abelian-group and \(k[x]\)-operator cases. A complete local proof of the general invariant-factor theorem is not supplied there. The exercises at printed 196 / PDF 202 then explicitly ask the reader to recover Jordan form from the \(\mathbb C[x]\)-module theorem and to generalize earlier abelian-group results to arbitrary PIDs.

This is a defensible location for a focused supplement from Grillet VIII.6, whose fuller proof is documented in the existing source ledger, or from another fully proved PID treatment. It does **not** justify saying that the module viewpoint itself is missing from Xi. Nor should one advertise Xi III's brief statement plus exercise as an already completed proof of the general classification.

### A compact representation sequence and its limits

For cyclic Fourier methods and finite-group invariant complements, a small sequence suffices:

1. Define representations, intertwiners, invariant subspaces, and the group algebra; prove the representation/module dictionary by extending the action linearly.
2. Prove the averaged-projection lemma directly—Xi printed 114–115 or Grillet printed 383–384 both work.
3. Prove Schur's lemma from kernels and images, adding the algebraically closed scalar conclusion only when required.
4. For a cyclic group, identify \(k[C_n]\cong k[x]/(x^n-1)\). Over a splitting field with characteristic not dividing \(n\), derive the eigenspace projectors by polynomial CRT or the finite geometric-series identity. Over \(\mathbb Q\), retain irreducible cyclotomic blocks rather than claiming all constituents are one-dimensional.
5. Work one nonabelian example, such as Xi's \(S_3\) permutation-module split, to test what cyclic intuition fails to capture.

The first four steps need neither Jacobson radicals nor Wedderburn–Artin theory, compact integration, Lie algebras, or a full character table theory. They also do not replace those topics, Xi's rotation-group and \(SU(2)\) examples, or the representation appendix. Hall's previously sampled unitary and Lie-theoretic pages remain a separate extension; no new Hall proof audit was made for this comparison.

**Stopping tests.** Prove that the averaged map is a projection and commutes with the action; identify exactly where \(|G|^{-1}\) is used. In characteristic \(p\), use \(C_p\) acting by \(I+N\) on a two-dimensional space, with \(N\neq0\) and \(N^2=0\), to show an invariant line need not have an invariant complement. Over \(\mathbb C\), distinguish the existence of a common invariant Hermitian form from separate diagonalizability of each group element. Finally split the \(S_3\) permutation representation and exhibit an actual intertwining matrix. These test construction and failure cases, not just theorem names.

## 4. Integrality and cyclotomic fields: retain the elementary bridge before Lang

**Xi III §4.4, Lemma 4.49 and Theorem 4.50, printed 194–195 / PDF 200–201, V/P.** The text proves that an element \(t\) of a domain is integral over \(\mathbb Z\) exactly when \(\mathbb Z[t]\) is finitely generated as a \(\mathbb Z\)-module. The reverse direction writes multiplication by \(t\) on a finite generating family and uses the vanishing of the determinant of \(tI-A\), whose polynomial is monic. It then deduces closure of integral elements under addition and multiplication using finite generation and the PID submodule result. Character values, being sums of roots of unity, are connected back to algebraic integers.

This already gives a concrete bridge from matrix algebra and modules to integrality. A reconstructed version can phrase the determinant step as the adjugate identity; no Dedekind domain or valuation is needed. It is especially useful before passing from rational spectral data back to integer coefficients.

**Xi III §§5.6–5.7, printed 264–265 and 270–272 / PDF 270–271 and 276–278, V/P.** Example 5.47 constructs cyclotomic polynomials through the factorization of \(x^n-1\), proves integral coefficients by monic division and induction, and postpones general irreducibility. Theorem 5.50 later proves irreducibility over \(\mathbb Q\) by Gauss's lemma and reduction modulo a prime \(p\nmid n\): if a primitive root's \(p\)-th power belonged to a different factor, the reductions of the factors would share a factor, contradicting squarefreeness of \(x^n-1\) modulo \(p\). Iterating over prime factors of an exponent reaches all primitive roots. This is an undergraduate polynomial argument with explicit prerequisites.

**Lang, Algebraic Number Theory IV.1, printed 71–75 / PDF 85–89, P.** The inspected route is different. It first studies prime-power roots of unity through \(\pi=1-\zeta\), units of the form \((1-\zeta^i)/(1-\zeta)\), and the product expressing \(p\). Valuations and ramification-index bounds then establish the degree and total ramification. The proof that \(\mathbb Z[\zeta]\) is the full ring of integers uses localization and discriminant comparisons from earlier chapters; the general case uses composita and a discriminant criterion.

Lang therefore supplies arithmetic structure that the elementary cyclotomic irreducibility theorem does not establish. But sending an undergraduate to these pages merely to obtain \([\mathbb Q(\zeta_n):\mathbb Q]=\varphi(n)\) imports unnecessary valuation, ramification, and discriminant theory. Xi's inspected proof is the smaller route for that purpose.

Neither inspected passage was verified as a ready-made proof of the full integral CRT image for a chosen factorization of \(x^n-1\). Such gluing conditions require their own argument over \(\mathbb Z\). Rational factorization and the fact that each component is an algebraic integer do not prove that an arbitrary tuple of component values comes from one integer polynomial.

**Stopping tests.** Reconstruct the determinant proof of the integrality criterion; derive the elementary cyclotomic irreducibility argument and pinpoint why \(p\nmid n\) matters; then give the parity obstruction for \(x^2-1\) over \(\mathbb Z\). Enter Lang when the actual next question asks about the ring of integers, prime decomposition, ramification, or discriminants—not just because cyclotomic notation has appeared.

## 5. The local substitution decision

| Selected goal | Smaller sequence justified by the inspected evidence | What it does not replace |
| --- | --- | --- |
| Common-factor detection and elimination | Xi's bounded-degree kernel argument, followed by one product-formula proof | Degree-degeneration care, computational elimination practice, root-location material |
| Finite-field existence, cyclicity, subfields, Frobenius | Finite splitting-field construction; root-set field; lcm/root-bound cyclicity; direct subfields; automorphism counting | Möbius inversion, irreducible counts, explicit arithmetic, full Galois correspondence |
| Finite-group invariant complements | Basic representation/module dictionary plus Xi's or Grillet's averaged projection | Character theory, matrix-algebra classification, compact/Lie theory, explicit examples not worked |
| General PID module structure | Xi's definitions and submodule theorem plus a complete invariant-factor proof from the chosen graduate source | A proof cannot be replaced by Xi's later exercise requesting it |
| Elementary integrality and cyclotomic degree | Xi's finite-module determinant criterion plus Gauss/reduction-mod-\(p\) irreducibility | Integral CRT gluing, ring-of-integers theorems, ramification, valuations and discriminants |

The practical conclusion is to keep one proof of each reusable mechanism, solve at least one construction and one failure-case test, and use Xi's omitted computations as a diagnostic bank. Grillet or Hungerford can organize the next layer, but only after their local prerequisites are distinguished from the much larger theories surrounding the desired result.

## Inspected-page ledger for this supplement

| Source | New/current inspection | Scope and limitation |
| --- | --- | --- |
| Xi I | printed 190–193 / PDF 196–199, V/P | Entire resultant proof sequence 7.76–7.80 and visible exercises; narrow cubic-example error confirmed on image |
| Xi III | printed 34–35 / PDF 40–41, V/P | Cyclicity theorem and surrounding finite-abelian context; earlier classification proof not re-audited here |
| Xi III | printed 109–115 / PDF 115–121, V/P | Hermitian averaging, explicit \(S_3\) example, both Maschke proofs, following remarks |
| Xi III | printed 186–196 / PDF 192–202, V/P | Module definitions through PID submodules, structure statement, integrality proofs, exercises |
| Xi III | printed 260–266 / PDF 266–272, V/P | Finite fields, subfields, Frobenius, Möbius inversion, cyclotomic construction and irreducible counts; later §5.6 exercise pages not audited |
| Xi III | printed 270–272 / PDF 276–278, V/P | Roots-of-unity theorem, cyclotomic irreducibility proof including its final lines, exercises |
| Grillet | printed 157 / PDF 169, P | Cyclic finite multiplicative subgroup proof |
| Grillet | printed 176–179 / PDF 188–191, P | Resultant definition, universal determinant proof, discriminant identity |
| Grillet | printed 192–193 / PDF 204–205, P | Finite-field proof and exact exercise status of subfield results |
| Grillet | printed 197–200 / PDF 209–212, P | General Galois framework sampled to identify prerequisites; not used as a shorter proof recommendation |
| Grillet | printed 381–386 / PDF 393–398, P | Group algebra, representation/module dictionary, Maschke, adjacent classification and cyclic-group exercises |
| Hungerford | printed 279–282 / PDF 298–301, P | Finite-field proofs, explicit imports and exercises |
| Hungerford | printed 453–456 / PDF 472–475, P | Maschke radical/trace proof and surrounding algebra-structure context |
| Lang | printed 71–75 / PDF 85–89, P | Cyclotomic degree, ramification and integer-ring proof dependencies; formulas whose extraction was uncertain were not transcribed |

Public prose contains original paraphrases and small mathematical reconstructions only. Source scans, raw excerpts, private Library identifiers and access metadata are outside the repository. No commit or push was performed.
