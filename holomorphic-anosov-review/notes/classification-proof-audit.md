# Classification proof audit: Franks–Manning and homotopy-torus rigidity

*Publication note: any `extension/evidence/`, `working-reference/`, or source-copy filenames in these notes identify excluded working references. Third-party PDFs, scans, OCR and raw article-response logs are not bundled. Included search/access metadata is under `../evidence/`; use the primary-source URLs for original texts.*


Private extension to the review of Zhang's submitted arXiv:2609.37695v3. This note separates inspected original proofs, independent reconstructions, primary-source restatements, and unresolved source access. It supersedes the access-only limits in the earlier `notes/source-audit.md` where noted below.

## Result and limits

No new counterexample or fatal defect in Zhang's classification citations was found. Two original proofs are now inspectable: Franks 1969 and Hsiang–Wall 1969. The crucial hypotheses in Franks 1969 are stronger than the final Franks–Manning theorem: homological hyperbolicity and a full nonwandering set. I independently reconstructed the first implication for Zhang's exact holomorphic setting and verified that Franks's subsequent argument is insensitive to an exotic smooth structure. The second implication, the full-nonwandering-set step traditionally supplied by Manning, remains an original-proof access limit. This is **not** evidence that the theorem or citation is wrong, but it prevents claiming that this audit checked every critical proof in the classical classification.

The homotopy-torus implication is directly supported by Hsiang–Wall's original proof. Its application to a smooth manifold bypasses that note's triangulability-obstruction argument. The remaining essential input is the compatibility between the surgery classification of marked PL homotopy tori and the classification of PL structures on the fixed topological torus. That input is explicitly identified; the underlying surgery and Kirby–Siebenmann proofs have not been reverified from first principles.

## 1. What Zhang needs

At p. 12, Section 3, Zhang starts with a compact smooth manifold `X` homeomorphic to a real torus, equipped with a holomorphic Anosov diffeomorphism. He needs an actual homeomorphic conjugacy to a hyperbolic affine toral automorphism, without assuming transitivity or the standard smooth structure. At the preceding topological stage, the Ghys reduction needs a closed smooth manifold of torus homotopy type in real dimensions `2d >= 6` to be homeomorphic to the torus. Neither step requires a smooth classification of exotic tori.

| Dependency | Status in this extension |
| --- | --- |
| `f_*` has no root-of-unity eigenvalue | Original Franks 1969 proof inspected; independently checked by Lefschetz indices |
| `f_*` has no unit-modulus eigenvalue | Independently reconstructed below, conditional only on standard finite Markov coding for hyperbolic basic sets |
| Lifted semiconjugacy exists and is proper | Reconstructed by convergent series below; no standard smooth structure needed |
| Every lifted iterate has exactly one fixed point | Original Franks 1969 index argument inspected; reconstruction extends to exotic smooth tori |
| Full nonwandering set / regional recurrence | **Original Manning 1974 proof not obtained; not independently completed** |
| Unique stable–unstable intersection, global product, injective semiconjugacy, assuming the preceding hypotheses | Original Franks 1969 proof inspected and its essential mechanisms checked |
| Same conclusion for a homeomorphic exotic smooth torus | Scope explicitly stated by Fisher–Kalinin–Spatzier p. 169; conditional Franks argument reconstructed without a standard-smoothness requirement |
| Closed smooth homotopy torus in dimensions at least five is homeomorphic to the torus | Original Hsiang–Wall proof inspected; high-dimensional classification inputs mapped below |

## 2. Original Franks 1969: hypotheses and proof audit

Original scan: [Franks, *Anosov diffeomorphisms on tori*, Trans. AMS 145 (1969), 117–124](https://scispace.com/pdf/anosov-diffeomorphisms-on-tori-gkxjeli14m.pdf). The primary scan was read through web extraction, including all eight pages. Its text is preserved in `extension/evidence/classification-web-click-01.json`. A local PDF download from this mirror returned an empty HTTP 202 response; AMS endpoints returned 403.

Theorem 1, p. 117 requires both `Omega(f)=T^n` and hyperbolicity of the induced first-homology action. Theorem 2, p. 118 excludes roots of unity only. The proof proceeds through a semiconjugacy, the fixed-point index of each lift, uniqueness and existence of leaf intersections, then bounded intrinsic fiber diameters and hyperbolic expansion. In Lemma 1.6, p. 121, properness prevents the holonomy rectangle from escaping; uniqueness of intersections and local product identities control its limits. Bounded ambient image alone would not justify this continuation.

### Independently checked mechanisms and their exact category requirements

The following are reconstructions, not claims to have checked inaccessible portions of the 1970 survey.

**Semiconjugacy and properness.** Choose a deck-equivariant homeomorphism from the universal cover of an arbitrary smooth homotopy torus already known to be homeomorphic to `T^n` onto `R^n`. Its lifted map has the form

`F(x)=Ax+delta(x)`,

where `A` is the induced integral automorphism and `delta` is bounded and lattice-periodic. Once `A` is hyperbolic, write `A=A_s + A_u` on the stable/unstable direct sum. Set

`u_s(x) = -sum_{k>=0} A_s^k delta_s(F^(-k-1)(x))`,

`u_u(x) = sum_{k>=0} A_u^(-k-1) delta_u(F^k(x))`.

Both series converge uniformly. The lattice-periodic continuous correction `u=u_s+u_u` satisfies `u(Fx)-Au(x)=-delta(x)`, so `H(x)=x+u(x)` obeys `H F=A H`. Its bounded displacement makes it proper and, by degree, surjective. It descends to a degree-one map homotopic to the initial topological identification. Uniform continuity and the conjugacy equation send lifted stable/unstable leaves into the corresponding affine subspaces. No derivative of the initial identification has been used.

**Exactly one fixed point of a lifted iterate.** For any lift of `f^m`, the difference from its linear part `A^m` is bounded. If `A^m-I` is invertible, the fixed-point index in a sufficiently large ball is the degree of `I-A^m`, hence is `+1` or `-1`. Hyperbolicity of `f` makes fixed points isolated; the large-ball bound makes their number finite. The lifted unstable bundle is orientable because the universal cover is simply connected. The derivative of the lift has a constant orientation sign on that bundle, so all local fixed-point indices have the same sign. Their sum therefore has absolute value equal to the number of fixed points, which must be one. All index statements can be made on the actual smooth universal cover; conjugating coordinates topologically preserves the index. Standard smooth Euclidean coordinates are unnecessary.

**Why the full-nonwandering-set hypothesis matters.** Franks Lemma 1.5, pp. 119–120 turns two global intersections into a nearby periodic homoclinic configuration using density of periodic points in the whole torus. That density is obtained from `Omega(f)=T^n`; it cannot be silently supplied before recurrence has been proved. The unique-fixed-point argument above rules out the resulting configuration. Lemma 1.6 then uses the proper semiconjugacy and local product rectangles to obtain existence of every intersection. Finally, global product structure bounds intrinsic leafwise diameters of fibers over a compact fundamental domain. Expansion forces a nontrivial fiber to violate that bound. The stable-direction argument is also needed if the first stable–unstable corner happens to coincide with one endpoint; it is the symmetric version of the printed unstable argument.

These constructions use compactness, the topological torus cover, smooth Anosov foliations and a deck-invariant metric. None requires the cover identification to be a diffeomorphism. Thus a hypothetical objection based solely on an exotic torus smooth structure is not supported by the inspected proof.

## 3. Independent reconstruction of homological hyperbolicity

This calculation supplies the implication needed in Zhang's holomorphic setting, subject to the finite Markov-coding theorem for hyperbolic basic sets. It is not an attribution of a proof to Manning 1974, whose original article remains unavailable.

Let `A=f_*` on first homology and let `N_m=#Fix(f^m)`. In the holomorphic setting the real stable and unstable bundles carry their complex orientations, and `Df^m` preserves both. At a fixed point, complex eigenvalues occur in conjugate real pairs, so

`sign det_R(I-Df^m) = +1`.

The Lefschetz formula and the cohomology exterior algebra of a space homeomorphic to a torus give, for every positive `m`,

`N_m = L(f^m) = det(I-A^m) = |det(I-A^m)|`.

The absolute-value version also works for an orientable real Anosov unstable bundle. In the general real case one first passes to the characteristic mod-two cover to orient it. The smooth structure of that cover need not be standard.

**Periodic-count bounds needed here.** Spectral decomposition and finite Markov coding give constants `c,C>0`, a positive integer `q`, and a rate `rho>=1` such that

`c rho^(qn) <= N_(qn) <= C rho^(qn)` for all sufficiently large `n`.

Here is the part of this assertion that can be checked directly from the coding: each transitive basic set has an irreducible finite adjacency matrix `B`. Choose `q` divisible by all matrix periods. Perron–Frobenius bounds the number of admissible words above and `trace(B^(qn))` below by fixed multiples of `rho_B^(qn)`. Each fixed code maps to a fixed point and each point has at most the uniform finite coding multiplicity, giving the lower bound. For the upper bound, choose a code for every `f^(qn)`-fixed point. Two different such points cannot share its length-`qn` word: the rectangles are smaller than an expansivity constant, and periodicity makes the points close for every integer iterate, contradicting expansivity. Summing over finitely many basic sets gives the displayed bounds with `rho=max rho_B`.

If `A` had a root-of-unity eigenvalue, choose an iterate divisible by its order and by `q`. Its Lefschetz determinant vanishes, contradicting the positive lower periodic-count bound. Thus every unit-modulus eigenvalue, if present, is a non-root of unity.

Set `a=product_{|lambda|>1}|lambda|`, with eigenvalues counted with algebraic multiplicity. Factoring the determinant gives

`N_(qn) = a^(qn) C_n P_n`,

where `C_n -> 1` comes from the eigenvalues off the unit circle and

`P_n = product_{|lambda|=1}|1-lambda^(qn)|`.

The boundedness of `P_n` and the lower periodic-count bound imply `rho<=a`. If unit-modulus eigenvalues exist, take the compact subgroup generated by their `q`th powers in a product of circles. Every coordinate projection is the full circle because that eigenvalue is not a root of unity. Each coordinate-equals-one subgroup has Haar measure zero, so their finite union does not cover the group. Consequently some subsequence has `P_n` bounded away from zero. The upper periodic-count bound now gives `a<=rho`, hence `a=rho`.

On the other hand, simultaneous recurrence to the identity in that compact monothetic group gives an unbounded subsequence with every `lambda^(qn)` tending to 1, so `P_n->0`. This contradicts `N_(qn)/a^(qn)>=c`. Therefore no unit-modulus eigenvalue exists: `A` is hyperbolic.

**Boundary of the reconstruction.** Finite Markov coding, including uniform finite fiber multiplicity and a coding for each basic set, is an external hyperbolic-dynamics input. Its finite-fiber statement appears explicitly in Manning's checked 1972 thesis, Chapter 1, citing Bowen. I have checked the counting deduction above, not rederived the full Markov-partition existence theorem. This proof supplies homological hyperbolicity only; it does not by itself prove regional recurrence or injectivity of `H`.

## 4. What the accessible Manning sources do and do not establish

[Manning's 1972 thesis, *On zeta functions and Anosov diffeomorphisms*](https://wrap.warwick.ac.uk/id/eprint/71348/1/WRAP_Thesis_Manning_1972.pdf), Chapter 4, pp. 38–43, gives the Lefschetz/root-of-unity argument and the conditional nilmanifold classification. It explicitly leaves full recurrence and non-root unit-circle eigenvalues as open questions. It cannot substitute for the 1974 proof. His [1977 survey](https://www.numdam.org/item/AST_1977__50__273_0.pdf), p. 275, verifies that a surjective semiconjugacy onto a hyperbolic toral automorphism maps the nonwandering set onto the whole target: otherwise a periodic target orbit would have a nonempty closed invariant preimage disjoint from the nonwandering set. This is weaker than `Omega(f)=X` and does not justify replacing it by that conclusion.

The independent reconstruction in Section 3 addresses the unit-circle question. The remaining recurrence step is therefore stated as unchecked, not concealed behind the older thesis or the surjective-image proposition.

## 5. Hsiang–Wall 1969: actual implication used and dependencies

Original local scan: `extension/evidence/hsiang-wall1969.pdf`, SHA-256 `1974d9cda6de52a0bdb63127e4ceea4f78a50257a4705005cd9e917c1824a9a0`.

Source: [W.-C. Hsiang and C. T. C. Wall, *On homotopy tori II*, BLMS 1 (1969), 341–342](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hsiawall2.pdf). Both pages were read; p. 342 was also rendered and visually checked (`hsiang-wall1969-p342.png`).

The note's final paragraph concludes topological rigidity in dimensions at least five by identifying the invariants for marked PL homotopy tori with those for PL structures on a fixed topological torus. This compatibility matters: equality of numbers of structures would not suffice. For a closed smooth manifold, triangulability is already available, so the preceding obstruction-class argument is unnecessary. The note's deeper inputs remain the PL surgery classification of Hsiang–Shaneson/Wall and Kirby–Siebenmann's classification of PL structures. These were identified, not reproved here.

### Independent checks of possible category/hypothesis pitfalls

- **Dimension:** the rendered original says `n>=5`. Zhang's high-dimensional application has `n=2d>=6`, so the exceptional real-four-dimensional case is not imported.
- **Marked versus unmarked classification:** the PL structures on a fixed torus are parametrized by `H^3(T^n;Z/2)` before quotienting by changes of marking. In the earlier Hsiang–Shaneson PNAS note, the proof uses simple homotopy triangulations (pairs with a marking) before taking `GL(n,Z)` orbits. Comparing those marked structures, rather than merely the unmarked orbit sets, is the appropriate implication.
- **Smooth versus PL versus topological:** being smooth supplies a compatible PL structure. The classification does not assert that this PL structure is the standard one; the conclusion needed is only an underlying homeomorphism with `T^n`.
- **Simple homotopy:** the surgery formulation uses simple homotopy equivalences. For the torus group this follows from `Wh(Z^n)=0`. That algebraic K-theory theorem is a dependency, not newly verified in this bounded audit.
- **Homotopy type, not just fundamental group:** the conclusion applies once the manifold is shown to be aspherical with fundamental group `Z^n`, giving torus homotopy type. A bare abelian fundamental group would not be enough.

For completeness, I checked the elementary covering arithmetic in the longer topological argument. The cover corresponding to `2 Z^n` has degree `2^n`; its pullback is zero in positive-degree mod-two cohomology because multiplication by two is zero on `H^1(T^n;Z/2)`, whose exterior products generate the cohomology. On integral cohomology the same pullback is injective. Also the coefficient injection `Z/2 -> Z/24`, sending 1 to 12, is injective on `H^4(T^n;-)`, since the torus has free homology. Those are valid features of the proof. The homotopy invariance of the stable tangent sphere fibration and the calculation of `Top/PL` remain external inputs.

The earlier [Hsiang–Shaneson PNAS 62 (1969), 687–691](https://www.maths.gla.ac.uk/~mpowell/hsiang-shaneson-homotopy-tori-II.pdf) was checked for this distinction. Its Theorem B alone only produces a finite standard PL cover. That weaker statement must not be silently upgraded to topological rigidity; Hsiang–Wall supplies the upgrade. Their displayed surgery classification argument itself relies on Wall's obstruction-group decomposition and Rohlin's theorem, which are not recursively audited here.

## 6. Access, errata search, and proof-coverage record

Exact retrieval logs, query results and original response messages are under `extension/evidence/`. In particular:

- `classification-fetch-01.json`: successful local downloads of Hsiang–Wall, Manning's thesis and the 1977 survey; AMS 403 for Franks.
- `classification-web-click-01.json`: original Franks 1969 scan text obtained by following the page's actual PDF link.
- `classification-fetch-02.json`: SciSpace shell attempts returned empty 202 HTML responses, not PDFs.
- `classification-web-open-02.json`, `classification-web-open-03.json`, `classification-web-open-04.json`: inaccessible Franks 1970 URLs and Manning 1974 JSTOR/SciSpace attempts.
- `classification-web-open-07.json`: Manning's two-page 1975 seminar report is subscription content, not a successfully inspected proof.
- `classification-errata-search.json`, `classification-web-open-08.json`: targeted correction/counterexample searches. The issue-table-of-contents result mentioning a correction near Hsiang–Wall was checked: it belongs to Kingman's preceding article, not to *On homotopy tori II*. No relevant correction or counterexample was found in these searches. This is a bounded search result, not a proof that no erratum exists.

Original Franks 1970 and Manning 1974 remain inaccessible. AMS returns 403; JSTOR returns challenge/metadata HTML; the SciSpace Manning page has no accessible PDF link. The Internet Archive candidate was the wrong volume and access-restricted; no restricted full text was fetched. No access controls were bypassed, no purchase or installation was attempted, and no author was contacted.

### Separate confirmed cited-source error

The adversarial check requested during this track confirmed the false disk-containment conclusion in Ghys 1995, Lemma 4.3, Fact 1, p. 596. The no-triple-intersection consequence that Ghys actually needs is true and has a short intersection-graph repair. Counterexample and proof are in `extension/notes/ghys-fact1-adversarial-check.md`. It should be reported as a repairable source overstatement, not as a fatal classification counterexample.

### Exact confidence statement

High confidence in the identified theorem scopes, the independent covering/degree/counting calculations, and the exotic-smoothness category check. High confidence in the explicit Ghys Fact 1 counterexample and its weaker repair. Moderate confidence in claiming broad proof coverage of Franks's original argument: its key mechanisms were reconstructed, but foundational stable-manifold, spectral-decomposition and Markov-partition theorems remain inputs. No complete independent proof of regional recurrence, no full verification of Manning 1974, and no reconstruction of high-dimensional surgery theory is claimed.

Included publication-safe source-access records: [search log](../evidence/classification-search-log.md), [fetch metadata 1](../evidence/classification-fetch-01.json), and [fetch metadata 2](../evidence/classification-fetch-02.json). Raw response logs, source PDFs and OCR remain excluded.
