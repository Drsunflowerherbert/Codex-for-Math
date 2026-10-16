# HPS foundations audit for Zhang, arXiv:2609.37695v3

*Publication note: any `extension/evidence/`, `working-reference/`, or source-copy filenames in these notes identify excluded working references. Third-party PDFs, scans, OCR and raw article-response logs are not bundled. Included search/access metadata is under `../evidence/`; use the primary-source URLs for original texts.*


Audit date: 16 October 2026. Scope: the ordinary stable-manifold inputs to Sections 2 and 4, and their use in the accompanying formalisation interfaces. This is a mathematical source/proof audit, not a formal verification.

## Conclusion

I found no error in the HPS inputs needed here. In particular, the assertion in Zhang's Lemma 2.5 (p. 9) that stable plaques vary continuously in the leafwise \(C^1\) topology is explicitly supplied by the original HPS theorem and its proof. It does not assert a \(C^1\) dependence on the transverse/base variable.

The global leaves have their intrinsic smooth leaf topology, are diffeomorphic to the appropriate Euclidean spaces, and hence are simply connected. For the particular uses in Zhang, simple connectivity can also be reconstructed directly from the nested local-disc construction. Holomorphicity of the ambient diffeomorphism makes both invariant distributions \(J\)-invariant and each individual stable/unstable leaf a complex submanifold. None of those facts alone implies that either distribution is a holomorphic subbundle.

These foundations do not settle the separate global unstable-holonomy continuation argument of Section 2.

## Sources actually inspected

1. **Hirsch–Pugh–Shub, _Invariant Manifolds_, LNM 583 (1977)**, publisher record: [DOI 10.1007/BFb0092042](https://link.springer.com/book/10.1007/BFb0092042). Complete scan obtained from [UC eScholarship](https://escholarship.org/content/qt6m58s433/qt6m58s433_noSplash_8a35f009e454419ac236b82dfae5a96c.pdf). Excluded working-reference file: `extension/evidence/HirschPughShub1977.pdf`, 154 PDF pages, 3,613,746 bytes, SHA-256:
   `7a192838a2c5b84c34ac7ec200c242fed5728c3573dde2cdde75ce96c5d0dfc9`.
2. **Published Section 5**, “Pseudo hyperbolicity and plaque families,” pp. 53–64, [DOI 10.1007/BFb0092047](https://link.springer.com/chapter/10.1007/BFb0092047). Read the [original chapter PDF uploaded by Morris Hirsch](https://www.researchgate.net/profile/Morris-Hirsch/publication/317569958_Pseudo_hyperbolicity_and_plaque_families/links/594031150f7e9ba171b23704/Pseudo-hyperbolicity-and-plaque-families.pdf), with [author-upload provenance](https://www.researchgate.net/publication/317569958_Pseudo_hyperbolicity_and_plaque_families). This independently confirms the published printed pagination and the wording at pp. 60–63. The web tool could read it; a separate local HTTP download received 403.
3. **Published Section 3**, pp. 25–38, [DOI 10.1007/BFb0092045](https://doi.org/10.1007/BFb0092045), read in the [author-uploaded PDF](https://www.researchgate.net/profile/Morris-Hirsch/publication/317568690_The_Cr_section_theorem_and_lipschitz_jets/links/59401769aca272371224cfad/The-Cr-section-theorem-and-lipschitz-jets.pdf), especially (3.1), (3.2), and the statement and opening proof of (3.5).
4. **HPS §6B and §7**, especially (6B.4), (7.5), (7.6), and §7A: inspected in the complete scan, PDF pp. 115–120 and 131–140. Excluded working-reference OCR and rendered page images were retained under `extension/evidence/hps-pages/`.
5. **Pugh–Shub–Wilkinson, “Hölder foliations, revisited,” arXiv:1112.2646v2**, [original paper](https://arxiv.org/pdf/1112.2646), particularly Introduction, §3, and §11. Excluded working-reference file `extension/evidence/PughShubWilkinson2012-holder.pdf`; SHA-256 `794ae975ba281376c57c92dfe49e05ef067654355d75d18e4c918759eb8fa79c`. The downloaded PDF is identified by its arXiv header as v2, 8 April 2012; its internal date says June 4, 2018. This metadata inconsistency does not affect the cited mathematical discussion.

**Pagination caution.** The full UC scan has a contents table whose page labels differ from the publisher's chapter ranges. I therefore identify its evidence by PDF page as well as theorem number. In the passages actually cross-checked against the published Section 5, published pp. 60, 61, 62, 63 correspond to UC PDF pp. 65, 66, 67, 68. Do not infer other printed page numbers solely from the UC contents table.

## Dependency map

| Needed input | Use in Zhang | Verification status |
|---|---|---|
| Embedded local stable/unstable discs, tangent to the invariant bundles | Lemmas 2.5–2.7, pp. 9–10 | Explicit HPS (5.4)–(5.5); original proof checked as below |
| Continuous plaque parametrisations and leaf derivatives, uniformly on compact parameter domains | Uniform \(r,\varepsilon\) in Lemma 2.5; continuity of the family in Lemma 2.7 | Explicit definition on HPS p. 61 and proof on p. 62; sufficient without transverse differentiability |
| Local product structure and continuous local holonomy | Local holonomy in Lemma 2.8; continuation setup after it | Reconstructed by transverse graph contraction; compatible with HPS §7A |
| Intrinsic global leaves and simple connectivity | Global-leaf linearisation, homotopy/holonomy uses; Section 4 | Reconstructed from local-disc exhaustion; Euclidean parametrisation also reconstructed using global graph transform |
| \(J E^{s/u}=E^{s/u}\) | Complex dimensions, holomorphic leaf maps throughout | Direct proof below |
| Individual leaves are holomorphic immersed submanifolds | Biholomorphic meaning in Lemmas 2.5–2.7 and 4.2 | Direct local CR proof below |
| Distribution is a holomorphic subbundle | Ghys input for \(E^u\); Zhang's Theorem 1.3 for \(E^s\) | **Not** supplied by the preceding foundations; checked separately by the coordinating reviewer |

## 1. Exact HPS local input and hypotheses

Write \(g=f^N\), where \(N\) is sufficiently large that, in a fixed continuous adapted norm,
\[
 \|Dg|E^s\|\le a<1,\qquad \|(Dg|E^u)^{-1}\|\le b<1 .
\]
One can alternatively arrange these one-step inequalities with an adapted metric. Passing to an iterate is harmless: stable and unstable sets for \(f\) and \(g\) coincide, since there are only finitely many intervening iterates and those maps are uniformly continuous on the compact manifold.

Choose \(a<\rho<1\). Then \(M\) is a \(\rho\)-pseudo-hyperbolic set for \(g\), with \(E_2=E^s\) and \(E_1=E^u\), in the exact sense used at the beginning of HPS §5. Thus the stable case of (5.5) applies. The unstable case follows by applying the same statement to \(g^{-1}\). Compactness gives the uniform coordinate size and estimates needed by the construction; transitivity is unnecessary.

On HPS published p. 61 the topology of a \(C^r\) pre-lamination is defined using local continuous sections into the space of \(C^r\) embeddings of a disc. The stronger notion in which the evaluation map is differentiable in the base variable is defined separately. Theorem (5.5) gives self-coherent \(C^r\) stable pre-laminations. In its proof, published p. 62, both the plaques and their derivatives along the plaque parameter are explicitly continuous, and the family is \(C^1\)-precompact.

The proof's construction is legitimate for ordinary Anosov maps:

- Lift \(g\) near each orbit point into its tangent fibre by exponential coordinates.
- Use a cutoff to extend these fibre maps, preserving uniform \(C^1\) proximity to the invariant linear maps.
- Apply the graph transform simultaneously over the continuous invariant splitting.
- The transform preserves the closed subspace of continuous families. Its fixed family is continuous.
- Apply the derivative/jet argument in the leaf variables. The stable-versus-unstable contraction factors are strictly below one. For each finite leaf-derivative order \(j\), the highest-order factor is of the form \(b a^j\), up to an arbitrarily small error. Thus no additional bunching is required for the strong stable leaves.

The smoothness step uses HPS's differentiable section/jet theorem, rather than pretending that the ordinary graph transform is a contraction for the full \(C^1\) norm. HPS explicitly warns against that shortcut in §3. I checked the graph-transform estimates and the way (5.4) and (5.5) use the section theorem. I have not independently re-proved every Lipschitz-jet argument in §3. That general theorem remains an accepted external underpinning.

For \(f\) smooth, use each finite \(r\). Local uniqueness of the stable discs identifies the resulting families, giving smooth individual plaques and continuous dependence in every finite leafwise \(C^r\) topology.

## 2. Why Zhang's uniform inverse argument is valid

Work in finitely many common ambient charts and use continuous frames of \(E^s\). Let
\[
 \psi_x:B_R(0)\longrightarrow W^s_{\mathrm{loc}}(x)
\]
be the plaque parametrisations. After shrinking the centre domains and \(R\), their values and leaf derivatives are jointly continuous, with uniform derivative bounds and lower bounds on the derivative near \(0\).

In these coordinates put \(K_x=k_x\circ\psi_x\), identifying the target \(E^s_x\) with a fixed parameter space through the frame. The construction of \(k_x\) uses smooth holomorphic \(t\) and the continuous invertible maps \(B_x=dt_x|E^s_x\). Hence \(K_x\) has jointly continuous leaf derivative and its derivative at \(0\) is a uniformly invertible map (the identity if the plaque is parametrised with its prescribed tangent frame).

By compactness one can choose a common small parameter ball on which
\[
 \|D K_x(\xi)-D K_x(0)\|
\]
is uniformly small compared with the inverse bound for \(D K_x(0)\). The quantitative inverse-function argument then gives both injectivity and a common target ball. Uniform comparison of plaque-coordinate distance with intrinsic leaf distance gives common positive \(r,\varepsilon\) in Zhang's statement.

This uses differentiation only along the plaques. It does not require that \(x\mapsto\psi_x\) be differentiable. Each \(k_x\) is holomorphic by the complex-leaf argument in §5 below, so its nonzero complex derivative makes the local inverse holomorphic.

## 3. Global leaves, Euclidean structure, and simple connectivity

The global stable set is obtained by pulling local stable discs backwards:
\[
 W^s(x)=\bigcup_{n\ge0}g^{-n}D^s_{g^n x}.
\]
Choose the uniform local discs so that \(g(D^s_x)\subset D^s_{gx}\). The sets in this union are nested, open in the intrinsic leaf, and are smooth discs. Local stable-set uniqueness identifies overlaps; the ambient inclusion is an injective immersion. The intrinsic manifold topology is the one obtained by these charts.

A compact subset of this increasing open union lies in one of its discs: take a finite subcover and the largest index. In particular every continuous loop has its image in a single disc and contracts there. This proves simple connectivity with no transitivity assumption and no global-product assumption.

For completeness, the stronger assertion “diffeomorphic to Euclidean space” can be obtained without an appeal to a general monotone-union theorem. Use the globally extended tangent-fibre system from HPS (5.1). Its global stable graph \(\widehat W^s_x\) is a smooth graph over the entire vector space \(E^s_x\), hence is diffeomorphic to \(\mathbb R^{\dim_{\mathbb R}E^s}\). The extended maps can be chosen to be diffeomorphisms: their uniform Lipschitz error from their invertible linear parts is smaller than the minimum norm of those parts. On the stable graphs they contract toward the zero section.

For \(v\in\widehat W^s_x\), let \(\widehat g^n_x(v)\) denote its forward image in the tangent fibre over \(g^n x\), and set, for sufficiently large \(n\),
\[
 I_x(v)=g^{-n}\!\left(\exp_{g^n x}(\widehat g^n_x(v))\right).
\]
For all large \(n\), the fibre orbit is inside the region where the extension agrees with the genuine coordinate expression for \(g\). Consequently the expression is independent of \(n\). Near any fixed \(v\), one common \(n\) works, so \(I_x\) is smooth and immersive. If two images coincide, apply a common sufficiently large iterate and use injectivity of the exponential chart and the extended fibre map to deduce that the two graph points coincide. Conversely every point in \(W^s(x)\) eventually belongs to the local stable disc, whose tangent lift is in the global stable graph; invert the fibre iterates to obtain a preimage. Thus \(I_x\) is a diffeomorphism onto the intrinsic stable leaf. Apply the same construction to \(g^{-1}\) for unstable leaves.

This does **not** make the global leaf inclusion a topological embedding into \(M\). For example, the integer matrix
\[
 A=\begin{pmatrix}2&1\\1&1\end{pmatrix}
\]
acts holomorphically and hyperbolically on \(\mathbb C^2/(\mathbb Z^2+i\mathbb Z^2)\). Its stable complex line has irrational real slope; its image is injectively immersed and dense. A returning sequence on that leaf can converge in the ambient torus without converging intrinsically.

## 4. Local product structure and tangent-path uniqueness

In a common small chart, stable plaques and unstable plaques are graphs over transverse coordinate subspaces, with uniformly small slopes. Their intersection is the fixed point of the composition of the two graph maps. The product of the slope bounds is less than one. If the centres are close enough, the maps preserve the chosen small domains, giving existence, uniqueness, and continuous dependence by the contraction principle. This proves the local product structure and continuous local holonomy needed to start Section 2.

For ordinary stable/unstable distributions, the “a tangent path stays in its leaf” assertion also has an elementary direct proof. If a piecewise \(C^1\) path \(\gamma\) is everywhere tangent to \(E^s\), then
\[
 \operatorname{length}(f^n\gamma)
 \le C\tau^n\operatorname{length}(\gamma).
\]
Hence its endpoints are forward asymptotic, and belong to the same stable leaf; apply the same argument to every subpath. Use \(f^{-1}\) for \(E^u\). This checks the relevant specialization of the HPS unique-path-lifting discussion (7.5)–(7.6). It does not establish completeness of arbitrary transverse holonomy continuations.

## 5. Direct complex-geometric reconstruction

Let \(J\) be the complex structure. Holomorphicity gives
\[
 Df_xJ_x=J_{fx}Df_x.
\]
Using a Hermitian metric, \(J\) is an isometry. If \(v\in E^s_x\), then
\[
 \|Df_x^n(J_xv)\|=\|J_{f^nx}Df_x^nv\|
 \le C\tau^n\|v\|.
\]
A vector whose forward derivatives tend to zero lies in \(E^s_x\): a nonzero unstable component would grow exponentially, and the uniformly bounded splitting projections prevent it being cancelled by the stable component. Thus \(J E^s=E^s\). Apply the backward version to get \(J E^u=E^u\).

Now take a smooth local stable plaque \(N\) and a point \(p\in N\). In a holomorphic ambient chart choose complex coordinates \((z,w)\) whose horizontal space is \(T_pN\). The real implicit-function theorem writes \(N\) near \(p\) as a smooth real graph \(w=h(z)\). Since its tangent space at every point is \(J\)-invariant,
\[
 Dh(z)(i\xi)=i\,Dh(z)(\xi).
\]
These are the Cauchy–Riemann equations, so \(h\) is holomorphic. Thus the plaque is a complex submanifold, and the intrinsic global leaf has the induced complex structure. Its inclusion is a holomorphic injective immersion. The same argument works for unstable leaves.

This proof neither differentiates the distribution in the base variable nor assumes that it is a holomorphic subbundle. Zhang's use of Ghys to establish the latter for \(E^u\) is therefore a genuinely additional input.

## 6. Errata and overstatement check

A bounded web search for HPS errata, gaps, and counterexamples did not find an original correction invalidating (5.4)–(5.5) for ordinary smooth Anosov maps. Search results were often poor or unrelated; this is explicitly **not** evidence that no such correction exists.

The primary follow-up by Pugh–Shub–Wilkinson discusses a real distinction that matters here: transverse Hölder regularity of some leaf conjugacies/holonomies does not follow just from Hölder tangent fields. Its results and cautions concern stronger transverse assertions, and do not contradict continuous leafwise \(C^1\) plaque dependence. HPS itself distinguishes a smooth lamination from a smooth foliation and discusses branching/unique-path questions in much more general normally hyperbolic settings.

No such stronger transverse assertion is necessary to justify Zhang's Lemma 2.5. Once the integrated review supplies the holomorphicity of \(E^u\), local unstable holonomy between complex stable transversals is holomorphic by holomorphic foliation coordinates; that further conclusion is not being extracted from HPS regularity alone.

## Coverage and limits

**Checked:** exact HPS statement and definition for the local plaque topology; its graph-transform construction and derivative-continuity mechanism; the specialization of its hypotheses to an iterate of a compact smooth Anosov diffeomorphism; the uniform inverse-function use in Zhang Lemma 2.5; intrinsic-leaf exhaustion and simple connectivity; Euclidean parametrisation from the global graph construction; local product structure; tangent-path uniqueness; \(J\)-invariance and holomorphic individual leaves.

**Accepted underpinning:** the full general differentiable-section/Lipschitz-jet theorem (HPS §3), and the familiar contraction/implicit-function principles it invokes. I read the relevant statements and their use, not every line of all proofs in the monograph.

**Not certified here:** Ghys's quasiconformal rigidity argument; Zhang's invariant connection and \(L^2\) estimates; the continuation of unstable holonomy to every point of a whole stable leaf; all general HPS lamination-stability statements; formal Lean correctness or axiom adequacy beyond the ordinary mathematical interfaces discussed above.

No source-access blocker remains for the HPS inputs. The separate 1970 AMS announcement was not obtained (HTTP 403), but it is unnecessary after access to the 1977 original chapter and complete scan.

