# Extended audit: regularity inputs and actual proofs

*Publication note: local source-copy filenames identify excluded reference material. Third-party PDFs, scans and OCR are not bundled; use the primary-source URLs.*


Scope: the regularity citations essential to Zhang, arXiv:2609.37695v3 (13 October 2026), Sections 2–4. Exact supplied PDF SHA-256: `3c8287bf41d153c7f0d0950b8a4b477546229333ee66ba7e9ae60e6a387920c6`. This note supplements the Section 4 audit in `../initial-limited-notes.md` and the independent `hps-foundations.md`. It is a bounded mathematical audit, not formal verification of the paper or cited books.

## Findings and certification limits

No additional mathematical error was demonstrated. The exact distributional regularity implication used in Sections 2 and 4 can be proved directly by mollification. The exact smooth orbit-map implication used in Section 3 can also be proved directly by averaging holomorphic coordinates. Consequently these two uses need not depend on unverified general formulations of Demailly's or Bochner–Montgomery's theorems.

The original BM46 full proof remains inaccessible in this audit. I have not certified the general locally compact-group formulation printed as Theorem 3.3. This is an explicit source/proof coverage limit, not a demonstrated counterexample to the theorem. The narrower application in this paper is independently reconstructed below.

The HPS foundational input has now been inspected in original material, including its plaque-family statement and the relevant proof paragraph. Its entire general differentiable-section/Lipschitz-jet machinery has not been re-proved; it remains an accepted external underpinning. See the separate HPS note for the precise distinctions.

## Evidence ledger

| Input | Statement checked | Proof-level work | Remaining limit |
|---|---|---|---|
| Demailly I.(3.29)(a), June 2012 | Exact original version and distribution/current statement, printed p.28 | Independently reconstructed the narrower continuous-coefficient implication needed here, below | General arbitrary-current version not independently re-proved in full |
| BM46 smooth action | Original bibliographic identity checked; accessible later research paper quotes a sufficient stronger formulation | Independently reconstructed the actual continuous Euclidean action by biholomorphisms, below | Original BM46 full text/proof and broad printed Theorem 3.3 formulation unverified |
| HPS stable/unstable plaque families | Original definition/theorem/proof, published pp.61–62, checked by delegated reviewer | Necessary local consequences reconstructed; exact leafwise C1 parameter continuity found explicitly in source | Full general HPS graph-transform/differentiable-section theorem not completely reproduced |
| J-invariance and complex individual leaves | Ghys original Lemma 2.1 checked; HPS note gives elementary derivation | Direct derivative estimate and graph Cauchy–Riemann argument | No extra external regularity theorem required beyond smooth immersed leaves |
| Intrinsic simple connectivity of stable leaves | HPS foundational description checked | Compact loops eventually contract inside one local plaque; Euclidean-leaf reconstruction in HPS note | Stronger ambient proper embedding is neither claimed nor used |

## Demailly: direct proof of precisely what the paper uses

Let `u` be a continuous complex-valued function on an open set `Omega` in `C^d`, and suppose each distributional antiholomorphic derivative vanishes. Choose a nonnegative smooth compactly supported mollifier `rho` on real `R^(2d)` of integral one and put `rho_epsilon(x)=epsilon^(-2d)rho(x/epsilon)`. On any relatively compact open subset at distance greater than `epsilon` from the boundary, convolution is well-defined and

`dbar_j (u * rho_epsilon) = (dbar_j u) * rho_epsilon = 0`.

The equality follows from distributional integration by parts, with derivatives transferred to the smooth compactly supported kernel. The convolution is smooth. The smooth Cauchy–Riemann equations make it holomorphic: for example, fix all but one complex coordinate and apply the one-variable Cauchy–Riemann theorem, then iterate the Cauchy integral formula on a polydisc. This gives joint holomorphicity without any regularity assumption on the original `u` beyond continuity.

Uniform continuity of `u` on a compact neighborhood gives `u*rho_epsilon -> u` uniformly on compact subsets. On a polydisc compactly contained in `Omega`, the Cauchy integral formula for the mollifications passes to the uniform limit, yielding the same formula for `u`. Differentiating its integral kernel, or applying the Cauchy formula again, shows that `u` is holomorphic.

This is sufficient for every use at issue. In Lemma 2.3 the limiting connection coefficient `a` is continuous and its distributional antiholomorphic derivatives vanish. In Lemma 4.1 the limiting section is continuous, and in a holomorphic frame its coefficients satisfy the same condition. Continuity of distributional differentiation supplies `dbar s=0` from the two convergences; all subsequent work is the local argument above. The approximating sections themselves do not have to be holomorphic.

For the Section 4 L2 input, on each compact coordinate neighborhood and for each compactly supported test function `varphi`, Cauchy–Schwarz gives

`|integral <dbar e_n,varphi> dnu| <= ||dbar e_n||_L2 ||varphi||_L2 -> 0`.

Uniform convergence of `e_n` gives its coefficientwise distributional convergence. Thus there is no unproved exchange of pointwise derivatives and uniform limits.

Original checked source: Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, title-page version 21 June 2012, Chapter I, Lemma (3.29)(a), printed p.28, [official PDF](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf). Local `source/demailly-agbook-2012.pdf`, SHA-256 `d7c7654a7417e8322e5dcf8fe8ec818b4c1a18cf280b41f2df5a871b776d89a1`. The published kernel proof also expressly extends its identity to currents by regularization; the argument above independently checks only the narrower implication actually used.

## Bochner–Montgomery: independent proof of the actual application

At this point of Zhang's Section 3 there is already a continuous action `Phi : R^m x Y -> Y`, where `Y` is a complex manifold of real dimension `m`; each `Phi_v` is biholomorphic. The orbit map `Theta(v)=Phi_v(x_0)` is already a homeomorphism from `R^m` onto `Y`, since it equals `H^{-1}`. These hypotheses are substantially more specific than the general theorem printed as Theorem 3.3.

Fix holomorphic coordinates `z:U -> C^(m/2)` about `x_0`. Joint continuity of the original action permits a relatively compact neighborhood `W` of `x_0` and a parameter ball `B_(2a)` such that `Phi_t(W)` stays in `U` for every `t` in that parameter ball. For a smooth nonnegative kernel `rho_epsilon` supported in `B_epsilon`, `epsilon<a`, of integral one, define

`psi_epsilon(x)=integral rho_epsilon(t) z(Phi_t(x)) dt`.

For fixed `t` the integrand is holomorphic in `x`; compact-parameter continuity and local uniform bounds permit Morera's theorem under the integral, proving that `psi_epsilon` is holomorphic. Joint continuity also gives local uniform convergence `psi_epsilon -> z` as `epsilon -> 0`. Cauchy estimates on smaller coordinate polydiscs give convergence of first derivatives. Therefore, for one sufficiently small fixed `epsilon`, `psi_epsilon` is a holomorphic coordinate map in a neighborhood `W_0` of `x_0`, by the holomorphic inverse function theorem.

For sufficiently small `v`, group additivity gives

`psi_epsilon(Theta(v)) = integral rho_epsilon(t) z(Theta(t+v)) dt`

`= integral rho_epsilon(s-v) z(Theta(s)) ds`.

To remove any domain ambiguity, choose a smooth cutoff in `s` that equals one on a ball containing all supports `supp(rho_epsilon)+v` for these small `v`, and is supported inside `B_(2a)`; extend the cutoff times the continuous function `z(Theta(s))` by zero. Then the right side is ordinary convolution with a compactly supported continuous function. Every derivative in `v` falls on the smooth kernel, so it is C-infinity. Composition with the smooth local inverse of `psi_epsilon` proves `Theta` is C-infinity near zero.

For any fixed `v_0`, the identity `Theta(v_0+w)=Phi_(v_0)(Theta(w))` extends smoothness to a neighborhood of `v_0`, since the fixed map `Phi_(v_0)` is biholomorphic. Differentiating this identity at `w=0` gives

`DTheta_(v_0)=D(Phi_(v_0))_(x_0) DTheta_0`.

The first factor is invertible. Hence `Theta` has constant rank. If its rank were smaller than `m`, the constant-rank theorem would force its image of some neighborhood of zero into a lower-dimensional local submanifold. But that image is open in `Y` because `Theta` is a homeomorphism. A lower-dimensional submanifold cannot contain such an open set. Thus the rank is `m`, and `Theta` is a local diffeomorphism everywhere. Bijectivity then makes it a global diffeomorphism.

Finally, joint smoothness of the action follows, if desired, from `Phi_v(x)=Theta(v+Theta^{-1}(x))`. No differentiability of `v -> Phi_v` was assumed at any step, so this proof does not assume its conclusion. It also avoids differentiating the original merely continuous conjugacy. It independently validates precisely the upgrade required on p.14.

### Exact citation status

BM46 is Salomon Bochner and Deane Montgomery, *Locally Compact Groups of Differentiable Transformations*, Annals of Mathematics 47 (1946), 639–653, [JSTOR record](https://www.jstor.org/stable/1969226), DOI `10.2307/1969226`. The original full text was not retrieved successfully: prior JSTOR PDF attempts returned an HTML challenge response, and the accessible record did not expose a readable full proof. I did not purchase access or attempt to bypass access controls.

The later primary research article Baouendi–Rothschild–Winkelmann–Zaitsev, *Lie group structures on groups of diffeomorphisms and applications to CR manifolds*, Theorem 3.5, quotes a BM formulation including the condition that only the identity fixes a nonempty open subset pointwise. Local file `references/baouendi-et-al.pdf`, [author/institutional PDF](https://www.maths.tcd.ie/report_series/tcdmath/tcdm0413.pdf). This condition holds for Zhang's free action. That corroboration is not being represented as reading the original BM46 proof, and the broader standalone formulation in Zhang's Theorem 3.3 remains unverified by this audit.

## HPS foundations

The complete delegated audit is [hps-foundations.md](hps-foundations.md), with [source and search log](../evidence/hps-searchlog.md). Its actual findings are:

- The HPS definition of a C^r pre-lamination is a continuous family with values in the C^r embedding space; Theorem 5.5 gives the stable pre-lamination. Published pp.61–62 and the relevant proof paragraph were inspected in original/author-provided material. This is the exact leafwise C1 parameter continuity used in Zhang's uniform inverse argument; it does not assert that the global stable distribution is C1 transversely.
- J-invariance follows because `Df^n Jv=J Df^n v` and `J` is bounded on a compact manifold. A stable vector remains stable after applying `J`; similarly backwards for unstable vectors.
- Once a smooth immersed leaf has J-invariant tangent space, write it locally as a smooth graph over a complex tangent plane. Tangent invariance is precisely the Cauchy–Riemann equation for the graph map, so the graph is holomorphic. This proves individual complex leaves and does not upgrade the entire foliation to a holomorphic foliation.
- Intrinsic leaf topology is essential: immersed leaves need not be properly embedded. Uniform local stable plaques and eventual contraction of a compact intrinsic loop place that loop inside a local disk, proving simple connectivity. The stronger Euclidean-leaf statement and its limits are treated in the HPS note.

The full general HPS proof is not completely independently reproduced. No claim of verifying all hypotheses or conclusions of normally hyperbolic theory is made.

## Bounded errata/counterexample searches and limitations

Searches sought BM corrections and exact smooth-action hypotheses and HPS corrections/counterexamples to the precise plaque-family implications. No relevant correction was found in the accessible primary materials. Search output included substantial irrelevant retrieval noise; therefore absence of a result is weak evidence and must not be read as proof that no erratum exists. The last combined web/Scholar metadata retrieval was aborted without a usable result and is not counted as checked evidence.

No further mathematical counterexample was found for these actual applications. The original BM46 proof is the principal unfinished citation audit. The HPS general foundational machinery remains accepted background. Neither limitation prevents the two direct regularity arguments above from establishing their narrow consequences.

