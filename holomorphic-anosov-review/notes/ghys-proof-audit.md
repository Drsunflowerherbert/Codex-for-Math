# Ghys proof audit for Zhang's cited dependencies

*Publication note: any `extension/evidence/`, `working-reference/`, or source-copy filenames in these notes identify excluded working references. Third-party PDFs, scans, OCR and raw article-response logs are not bundled. Included search/access metadata is under `../evidence/`; use the primary-source URLs for original texts.*


Audit date: 16 October 2026. This is a private mathematical audit of the original proofs, supplementing the whole-paper review. It does not certify a formalization.

**Target paper:** Zhang, arXiv:2609.37695v3, 13 October 2026, exact attachment SHA-256 `3c8287bf41d153c7f0d0950b8a4b477546229333ee66ba7e9ae60e6a387920c6`.

**Primary source:** Étienne Ghys, *Holomorphic Anosov systems*, Inventiones mathematicae **119** (1995), 585–614, [DOI](https://doi.org/10.1007/BF01245193), [author's PDF](https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf). Private reference SHA-256 `b30c190cc95c94c8fb2a32d4c97fddb44df822cb8ca86b7a662b644c152709e6`. Printed pages 589–598 were read, with rendered pages 592, 593, and 596 checked to resolve OCR ambiguity.

## Outcome and relevance

The mathematical content of Ghys Proposition 2.2 that Zhang needs can be reconstructed without a transitivity hypothesis, including the passage from conformal transverse holonomy to an ambient holomorphic subbundle. Ghys Proposition 3.1's contraction, holomorphicity, and completeness arguments also reconstruct correctly. The post-Lemma-5.1 reduction on p. 598 does not use transitivity once complete global holonomy is available; an explicit product and deck-group argument is given below.

A **false auxiliary strengthening** occurs in Ghys Lemma 4.3, Fact 1, p. 596: its containing-disks assertion fails for an explicit elementary example. The no-triple-intersection consequence actually needed there remains correct, with a short replacement proof. This is an error in a cited source's unnecessarily strong combinatorial assertion, **not a flaw in Zhang's theorem**. Evidence is in `../evidence/ghys-fact1-counterexample-and-repair.md`.

One additional source inference remains **unresolved by this bounded audit**: at the start of Ghys Lemma 4.3, the existence of an absolutely continuous invariant measure for the expanding Markov quotient is asserted to force transitivity. That is not a valid implication for arbitrary disconnected expanding Markov systems; extra structure of this specific construction must be used. I did not establish the full specific implication or find a published correction. I do not infer that Ghys's proposition is false. Zhang's own flat affine connection and developing map bypass Ghys Proposition 4.1 in complex dimension at least three; the essential post-completeness reduction can be reconstructed from Zhang's already-proved lemmas. **The surface base case is different:** Zhang invokes Ghys Theorem A, whose original proof invokes Proposition 4.1 for both foliations. The unresolved source-proof audit step therefore remains on the surface-case dependency path. It is not a demonstrated gap in Zhang's theorem, but the full theorem cannot be advertised as independently reverified through this source audit. The separate formalization reviewer reports an alternative finite-integral-budget/path-packing route for the projective-holonomy result, rather than this printed Markov argument; this source audit does not assess that alternative proof or its formal bridge.

No published erratum or primary-source counterexample to the cited Ghys theorems was located. The search was bounded; see the exact queries and limits in `../evidence/ghys-search-log.md`.

## What was checked and what was accepted

| Item | Audit level | Remaining accepted inputs |
|---|---|---|
| Ghys Proposition 2.2, pp. 589–590 | Original argument read; asymptotically conformal approximation reconstructed; ambient bundle conclusion supplied explicitly | Stable manifold/graph-transform regularity and uniform near-identity projection construction; compactness of quasiconformal maps; Hartogs theorem |
| Ghys Proposition 3.1 and Lemmas 3.2–3.3, pp. 590–593 | Jet interpretation, contraction direction, leafwise holomorphicity and completeness reconstructed | Existence and uniform leafwise smoothness of stable/unstable plaques; local holomorphic ODE theorem; Banach fixed-point theorem |
| Ghys Proposition 4.1, pp. 593–597 | Schwarzian cocycle, diameter measure, subinvariance-to-invariance calculation, combinatorial consequence and final vanishing implication checked | Markov partition existence and boundary measure control; full specific acim-to-transitivity step remains unresolved |
| Ghys Lemma 5.1, pp. 597–598 | Read to identify exactly where transitivity enters | Transverse full-support measure and resulting disk compactness accepted, not independently audited; Zhang replaces this lemma's argument |
| Ghys proof of Theorem B after Lemma 5.1, p. 598 | Developing/product/deck-group reduction reconstructed below; no hidden transitivity found | High-dimensional homotopy-torus topological rigidity and final Franks–Manning theorem delegated to the classification source reviewers |

These are ordinary mathematical proof checks, not machine verification. Foundational books were not all reopened, and the entire Ghys paper was not audited.

## 1. Proposition 2.2: the holomorphic-bundle implication

Use Ghys's convention for this discussion: the unstable distribution has complex dimension one. Applying the conclusion to the inverse diffeomorphism gives Zhang's holomorphic unstable distribution when the stable distribution has complex dimension one.

### Conformality of the holonomy

Let `h` be stable holonomy between compact neighborhoods in two unstable holomorphic curves. Forward iteration contracts the stable separation between paired points. Uniform continuity of the unstable tangent distribution and uniform leafwise smoothness permit a near-identity `C^1` projection `pi_n` between the paired iterated unstable plaques. Its singular values have ratio tending to one. The maps

`h_n = f^(-n) o pi_n o f^n`

therefore have quasiconformal distortion tending to one: both outer maps are conformal on their one-dimensional complex leaves. Backward contraction along unstable leaves makes `h_n -> h` uniformly. Since `h` is a homeomorphism, quasiconformal compactness gives conformality of `h`; orientations are the complex orientations and the near-identity approximants preserve them.

The printed distortion bound using `1 + epsilon_n` rather than `(1 + epsilon_n)/(1 - epsilon_n)` is an innocuous reparameterization of a sequence tending to one. No transitivity, invariant measure, or density of leaves appears in this proof.

### Why the conclusion is an ambient holomorphic foliation

The terminology in the source could leave a reader wondering whether the result supplies only an abstract transverse complex structure. There is a direct reconstruction of the needed stronger conclusion.

First, the same approximation applies to **arbitrary holomorphic curve transversals**, not just unstable curves. For a tangent vector `v = v_s + v_u` to a compact transverse curve, transversality gives a uniform positive lower bound on the unstable component. Then

`||Df^n v_s|| / ||Df^n v_u|| <= C (tau/lambda)^n ||v_s|| / ||v_u|| -> 0`.

Consequently the tangent lines of each iterated transverse curve approach the one-dimensional unstable directions. Paired transverse curves become close along stable leaves, and the same uniform local graph-projection construction yields `pi_n` asymptotically conformal. The restrictions of `f^n` to these holomorphic curves are conformal, so their stable holonomy is holomorphic as well. The technical uniform graph/projection input is the standard stable-manifold/inclination machinery used in the source; this audit has checked its role and estimate, not reproved that machinery from scratch.

Now choose a small ambient holomorphic chart `(z,w)` in `C^(d-1) x C` so that stable plaques are graphs

`w = g(z,t)`, with `g(0,t)=t`.

Continuity and transversality give a common graph box. For fixed `t`, the graph is a complex leaf, so `g(.,t)` is holomorphic. For fixed `z`, the map `t -> g(z,t)` is precisely stable holonomy between two vertical holomorphic transversals, so it too is holomorphic. Hartogs's theorem makes `g` jointly holomorphic. The graph map `(z,t) -> (z,g(z,t))` is locally biholomorphic because each one-variable transverse holonomy is univalent and has nonzero derivative. Stable plaques thus become the level sets of the holomorphic coordinate `t`, and their tangent distribution is a holomorphic subbundle.

This supplies the regularity passage rather than merely citing a later restatement. As corroboration, Cantat's [official 2004 paper](https://ems.press/content/serial-article-files/43027), Proposition 1.2, pp. 780–781, and §5.1, p. 793, explicitly uses this ambient holomorphic-foliation conclusion in arbitrary complex dimension.

## 2. Proposition 3.1: invariant complete affine structures

Ghys encodes an affine structure by a homogeneous splitting from nonzero one-jets of leaf charts to two-jets. In local leaf coordinates this is equivalent to specifying a holomorphic second-order ODE for affine charts. The ODE is invariant under affine reparameterization precisely because of homogeneity; its local solutions provide an affine atlas. This is the usual one-dimensional affine-connection description in jet language.

The difference of two homogeneous splittings has a weighted supremum norm, dividing its scalar difference at a nonzero tangent vector by that vector's norm. Homogeneity makes the norm descend to the compact base. The space of such continuous splittings is a complete affine space and is nonempty because the fibers are affine and contractible.

The source's forward pullback operator is expanding in this distance: the lower bound is `C^(-1) lambda^n`. Its inverse, obtained from backward iteration, is contracting for some iterate. Banach's theorem yields one fixed splitting. Uniqueness for that iterate also makes it fixed for the original operator. Thus the source has the correct contraction direction; the word 'dilatation' is not a mistaken application of a contraction theorem.

One does not need a globally chosen initial splitting holomorphic on every leaf. For a small fixed leaf disk, backward iteration eventually puts the whole disk in one member of a finite family of local holomorphic leaf charts. Transport that chart's holomorphic splitting forward. Uniform contraction gives convergence to the invariant splitting, locally uniformly on the fixed leaf disk. The limit is holomorphic. Uniform bounds require choosing relatively compact chart subboxes, as usual in this finite-atlas argument.

Completeness can be checked directly. Every unstable leaf is simply connected, so its affine structure has a developing map to `C`. Compactness gives a uniform local injectivity radius for normalized developing coordinates and a uniform target disk contained in their images. If two points have the same developed coordinate, backward iteration brings them into a single such injectivity plaque; affine equivariance preserves equality, so the points coincide. For surjectivity, transport the uniform target disk at a backward iterate forward by the leafwise affine map. Its scale grows at least as `C^(-1) lambda^n`, so the image at the original point contains arbitrarily large disks. The developing map is therefore a biholomorphism to `C`.

This confirms the content quoted near Zhang Lemma 2.7. Zhang's own connection-based construction independently proves the particular complete affine coordinates it needs, so the original jet construction is corroborative rather than an indispensable extra assumption.

## 3. Proposition 4.1: Schwarzian/Markov argument and limits

### Calculations that reconstruct

For stable holonomy between affine unstable leaf coordinates, the Schwarzian is a holomorphic quadratic differential. Changing the base point along the same stable leaf changes its evaluated values by a constant after transporting the tangent vector. Their diameter is therefore independent of that choice. Complex scalar multiplication of the tangent vector scales the diameter by the squared absolute value, so the diameter defines a nonnegative transverse area density.

For a Markov rectangle, the inverse image of a stable plaque is a connected union of the inverse-branch stable plaques. The diameter of the image of a connected finite union is at most the sum of the component image diameters. Affine dynamics preserves the Schwarzian cocycle. These observations give the source's subinvariance inequality for the diameter measure. The inverse branches partition up to measure-zero boundaries, so the total mass of the pullback is the original finite total mass. Integrating the nonnegative defect forces equality; continuity supplies equality away from the partition boundary and then by limits where needed.

Once this density vanishes, every stable-holonomy Schwarzian vanishes: the image diameter is zero and includes the identity holonomy, whose Schwarzian is zero. Solving the equation `S h = 0` gives a Möbius germ. Equivalently, `u=h''/h'` obeys `u'=u^2/2`, whose solutions integrate to affine or fractional-linear functions. This part has no problematic implication.

### False auxiliary assertion and repair

Fact 1 on p. 596 claims more geometric structure of the compact image sets than its diameter hypothesis guarantees. The three-set equilateral-triangle example in the separate evidence file disproves the disk-containment strengthening. The needed no-triple-intersection conclusion is nevertheless valid: the intersection graph is connected, a shortest chain between diameter-realizing points must use every positive-diameter set, and any extra edge would shorten that chain. The graph is a path and cannot contain a triple-intersection triangle.

Fact 2 is the usual covering-dimension obstruction: a compact set with nonempty interior in real dimension at least two cannot admit arbitrarily fine finite covers of multiplicity at most two. One can thicken a finite closed cover preserving the multiplicity bound, because its triple intersections are empty compact intersections, and contradict the covering dimension of an interior ball. This is a standard foundational topology result, not reproved here from first principles.

The source's iterated stable covers can be pulled forward to a fixed stable rectangle, where contraction makes them arbitrarily fine. Thus the direction of iteration does not spoil this final topological argument.

### Unresolved inference, precisely bounded

The beginning of Lemma 4.3 infers transitivity of the expanding Markov quotient from its nonzero absolutely continuous invariant measure, and then uses transitivity to assert that the diameter density is nowhere zero. The finite Markov quotient is a disjoint union of transversals. A generic expanding map on a disjoint union can preserve an absolutely continuous measure without being transitive—for example, two disjoint copies of an expanding toral endomorphism. Thus 'has an acim' alone is insufficient. The foliation construction, analyticity, connectedness of the original manifold, or another specific dynamical property may justify Ghys's inference; I did not complete that justification in this bounded audit.

This is recorded as an unresolved step in the original source proof, not a demonstrated failure of Proposition 4.1. The later [Zhang 2025 paper, §4](https://arxiv.org/html/2311.00251v2) uses the corrected weaker combinatorial Fact 1 but assumes transitivity throughout; it does not settle this question. No published erratum was located. Ghys Theorem A, pp. 598–600, explicitly invokes Proposition 4.1 twice to obtain a two-sided projective developing map on a complex surface. Consequently Zhang's cited surface base case retains this source dependency; the `d>=3` bypass below does not remove it from the whole-paper dependency map.

## 4. Theorem B after Lemma 5.1: an explicit transitivity-free reduction

Ghys uses transitivity in Lemma 5.1 to obtain a full-support transverse measure and bounded transported disks. After that lemma supplies entire holonomy, the subsequent p. 598 argument only needs completeness and the foliation/developing structures.

In Ghys's formulation, a projective developing map to `CP^1` restricts on each one-dimensional unstable leaf to the complement of one point. Entire stable holonomy identifies these images for leaves related by stable transport; chains of stable and unstable plaque paths connect any two points of the connected manifold. All omitted points are consequently the same. Taking that point as infinity makes the developing map affine and `C`-valued.

For Zhang, there is a more direct reconstruction which **does not require Ghys Proposition 4.1**. Zhang Lemma 2.3 already gives a flat holomorphic normal line connection with `d^nabla pi=0`. On the simply connected universal cover, choose a global parallel nonzero normal frame. The quotient one-form becomes an ordinary closed holomorphic form `omega`; integrate it to obtain

`D : X_tilde -> C`, with `ker dD = E_tilde^u`.

Zhang's complete stable affine coordinates give, on every stable leaf,

`D(p) = D(x) + a_x phi_x(p)`, where `a_x != 0`.

Thus each stable leaf maps bijectively to `C`.

Set `Y=D^(-1)(0)`. Every point `x` is on a unique stable leaf meeting `Y`, with intersection point

`r(x)=phi_x^(-1)(-a_x^(-1) D(x))`.

The inverse-coordinate continuity proved in Zhang Lemma 2.7 makes `r` continuous. Conversely, `(y,z) -> phi_y^(-1)(a_y^(-1) z)` continuously identifies `Y x C` with the universal cover, and `D` is the second-coordinate projection. Since the universal cover is connected, `Y` is connected. Its components are precisely unstable leaves, because locally it is the fiber of the submersion with kernel `E_tilde^u`. Hence it is a single unstable leaf, homeomorphic to `R^(2d-2)`. The universal cover is therefore homeomorphic to `R^(2d)` and contractible.

Deck transformations act on `D` by affine maps of `C`. If a nontrivial deck transformation fixed a point of `C`, it would preserve the corresponding connected unstable fiber. A path within that fiber from a point to its deck translate would project to a loop in an unstable leaf downstairs. Such a leaf is simply connected, so that loop is null-homotopic in `X`, contrary to its nontrivial deck element. The affine action is consequently faithful and every nonidentity element has no fixed point. Such affine maps are exactly nonzero translations. The deck group embeds in `(C,+)` and is a finitely generated torsion-free abelian group `Z^r`.

Since `X` is aspherical, it is a `K(Z^r,1)` and has the homotopy type of `T^r`. Comparing top cohomology of this closed orientable real `2d`-manifold with that of `T^r` gives `r=2d`. Thus `X` is a homotopy `2d`-torus. For `d>=3`, the final passage to a homeomorphic torus is the high-dimensional homotopy-torus rigidity theorem; the classification topology audit handles that source. The final conjugacy is the Franks–Manning theorem, handled separately. This reconstruction has no transitivity assumption.

The construction also explains why simply connected Anosov leaves are needed in the deck-group argument. Ambient density of a leaf does not invalidate it: the null-homotopy is taken in the intrinsic simply connected leaf and then composed with its immersion into `X`.

## Bounded conclusion

The critical Ghys uses in Zhang's `d>=3` proof survive this deeper audit, with ordinary stable-manifold, quasiconformal, complex-analytic, and topological foundations explicitly retained as dependencies. A false but unnecessary strengthening in Ghys's Fact 1 has a precise counterexample and repair. The original Schwarzian/Markov argument contains one source inference this audit has not independently closed; Zhang's own affine connection bypasses it for `d>=3`, while the cited surface base case still depends on Ghys Theorem A and its Proposition 4.1 input. The entire Ghys theorem package should therefore not be described as fully reverified from foundational sources.
