# Archive status: initial limited independent notes

**Historical notes from the initial limited review. Read `updated-review.md` for the current integrated assessment.** Later source and Lean audits supersede the original source-coverage limits and the statement that the only defect found was the open/closed-disk wording. Private local paths have been made generic; cited-source copies are not distributed.

# Detailed independent review notes

Private review of the exact 19-page attachment `2609.37695.pdf`, arXiv:2609.37695v3, 13 October 2026. Prepared 16 October 2026.

Source SHA-256: `3c8287bf41d153c7f0d0950b8a4b477546229333ee66ba7e9ae60e6a387920c6`.

These section reviews and the adversarial challenge support the companion correctness report. They preserve conditional section-level conclusions and explicit source-access limits; the main report supplies the integrated verdict. No formal verification was performed. The proposed substantive objections to global holonomy were tested and not sustained. The only literal defect found is the open/closed disk compactness wording, with the ball-convention qualification given in the main report.

## Contents

1. Section 2: connection, affine coordinates, holonomy
2. Independent adversarial global-holonomy check
3. Section 3: holomorphic torus conjugacy
4. Section 4: eigenform and regularity bootstrap
5. Introduction and final example
6. Bounded primary-source audit

Generic working-reference paths identify audit reference copies excluded from this publication; use the primary-source URLs for the cited material. Original-source access failures are distinguished from checked research restatements.


---

# Independent review: Section 2, invariant connection and global holonomy

**Paper reviewed:** Jiesong Zhang, *Codimension-One Holomorphic Anosov Diffeomorphisms*, arXiv:2609.37695v3, 13 October 2026, exact supplied file `source/2609.37695.pdf`, SHA-256 `3c8287bf41d153c7f0d0950b8a4b477546229333ee66ba7e9ae60e6a387920c6`.

**Coverage:** Section 2, printed pp. 5–12; especially Lemmas 2.2–2.8 and 2.10. The parent reviewer separately checks the full reduction in Proposition 2.9. No document-embedded code or formalization was executed.

## Finding and confidence

I found **no demonstrated substantive error in the connection, affine linearization, or global-holonomy arguments**. The new continuation argument is more than an unsupported extension of a local affine formula: the continuous family of entire leaf coordinates in Lemma 2.7 supplies a continuous candidate continuation on every bounded stable disk. This prevents escape of its lifted holonomy path at a finite base-path time. The familiar objection that “a linear germ need not be genuine global holonomy” does not invalidate the argument once this continuation step is included.

There is one small, repairable compactness wording problem: Lemma 2.10, p. 11, defines `D_R = phi_x^{-1}(B(0,R))` and then calls `D_R` compact. In the usual convention `B(0,R)` is an open ball, so this assertion is literally false. Replace it by the closed disk `K_R = phi_x^{-1}({v : ||v|| <= R})`, with holonomy defined on an open neighborhood of that disk, or perform the argument on the closure inside `D_(R+1)`. This does not threaten the theorem. The same correction makes the claimed uniform convergence and finite-subcover continuation precise.

Confidence is high in the local calculations and curvature estimate, and moderately high in the global continuation after the explicit closed-disk clarification below. This is a mathematical review, not formal verification.

## Dependency map

1. Ghys Proposition 2.2 applied to `f^{-1}` makes the unstable foliation/bundle holomorphic because `dim_C E^s = 1`.
2. The quotient `L = T^(1,0)X / E^u` is therefore a holomorphic line bundle carrying its Bott partial connection.
3. Lemma 2.2 uses contraction of covectors annihilating `E^u` to obtain a unique compatible invariant continuous connection.
4. Lemma 2.3 uses rank one, `dim_C E^u = d-1 >= 2`, a singular-value estimate, and change of variables to force its curvature to vanish. Distributional Cauchy–Riemann regularity makes the limiting connection holomorphic.
5. Lemma 2.4 produces local affine first integrals of the unstable foliation.
6. Lemmas 2.5–2.7 turn these first integrals into a continuous family of complete affine coordinates on stable leaves, conjugating `f` to `D f | E^s`.
7. Lemma 2.8 identifies unstable holonomy germs as complex-linear in those particular affine coordinates.
8. Lemma 2.10 combines that identity with continuous dependence of the entire inverse coordinates to prove genuine global holonomy, without a transitivity or density hypothesis.
9. Proposition 2.9 invokes the post-completeness portion of Ghys's p. 598 argument to obtain topological torus conjugacy.

## Reconstruction of the connection argument

### Lemma 2.2, pp. 6–7

In a holomorphic unstable-foliation box `(z,w)` with `E^u = ker dz` and quotient frame `e = pi(partial_z)`, compatibility is exactly `A = a dz`. The overlap conditions are affine conditions on the space of connections, so a smooth partition of unity supplies an initial compatible connection.

The difference `alpha = f^* nabla_0 - nabla_0` is a scalar `(1,0)`-form annihilating `E^u`. Rank one is essential to the scalar identification, but it is satisfied. Invariance of `E^u` and the bounded projections of the Anosov splitting give

`||(f^n)^* alpha|| <= C tau^n ||alpha||`.

The resulting telescoping series converges uniformly. Its limit is compatible and invariant. The identical contraction applied to the difference of two invariant compatible connections proves uniqueness. No assumed invariant volume or transitivity enters.

### Lemma 2.3, pp. 7–8

The local curvature is `R_n = d a_n wedge dz`. On a finite collection of relatively compact foliation boxes, the fixed initial one-forms `d a_0` and normal covectors `dz` have uniformly bounded norms. Pullback yields

`|R_n|^2 <= C ||Q_n||^2 ||U_n||^2`.

This is legitimate despite possible nonorthogonality of `E^s` and `E^u`: `dz` factors through the quotient metric, and the full derivative is bounded by a constant times `||U_n||` using bounded splitting projections.

Using the orthogonal splitting `E^u + (E^u)^perp` gives an upper-triangular derivative matrix. Its complex determinant has absolute value `||Q_n|| |det_C U_n|`, so its real Jacobian is exactly

`J(f^n) = ||Q_n||^2 |det_C U_n|^2`.

If the `d-1` singular values of `U_n` are `sigma_1 >= ... >= sigma_(d-1)`, then

`|det_C U_n| >= ||U_n|| m(U_n)^(d-2)`.

Consequently

`|R_n|^2 <= C lambda^(-2(d-2)n) J(f^n)`.

Integrating is valid for an arbitrary smooth Hermitian volume: `integral J(f^n) dnu = nu(X)` by the change-of-variables theorem. Thus `R_n -> 0` in `L^2` for `d >= 3`. The proof does not accidentally assume volume preservation.

Since the connection forms converge uniformly, distributional differentiation gives `dA = 0` for `A = a dz`. Its `(1,1)` component is `(bar partial a) wedge dz`, whose coefficients vanish independently. Hence `bar partial a = 0` as a distribution; the continuous coefficient is holomorphic. The `(2,0)` component then also vanishes, proving flatness. There is no missing product of distributions, since differentiation is applied to uniformly convergent continuous forms and wedge multiplication is by smooth coordinate forms.

The exponent is zero for `d=2`; the paper explicitly excludes that case here and invokes Ghys's surface theorem. This dimension restriction is handled correctly.

## Reconstruction of the affine-leaf argument

### Lemma 2.4, pp. 8–9

Compatibility implies `d^nabla pi = 0` locally because both `pi` and the connection form are multiples of `dz`. A local nonzero flat section `sigma` is holomorphic because the `(0,1)` connection is the bundle's Dolbeault operator. Writing `pi = omega tensor sigma` gives a closed holomorphic ordinary one-form `omega`; shrinking the box produces a holomorphic first integral `t` with `dt = omega`. Its differential is nowhere zero, because the quotient map is surjective. This is sound.

### Lemmas 2.5–2.6, pp. 9–10

Two flat frames differ by a nonzero constant on each connected overlap component. Thus their first integrals differ affinely, and the normalizing derivative `B_x = dt_x | E_x^s` cancels the scalar change. The local coordinate `k_x` is well defined as a germ. A finite atlas and compactness provide a uniform radius, after shrinking charts and stable plaques as usual.

Connection invariance makes `f` affine in these first integrals, giving `k_(f x) o f = S_1(x) o k_x`. All functions involved along a fixed stable leaf are holomorphic even though the entire stable distribution has not yet been proved holomorphic. Holomorphicity of the individual stable leaves is sufficient.

### Lemma 2.7, p. 10

For `p in W^s(x)`, forward iteration brings `p` into the uniform plaque about `f^n x`. The local equivariance makes

`phi_x(p) = S_n(x)^(-1) k_(f^n x)(f^n p)`

independent of all sufficiently large `n`. Injectivity follows by iterating two points into a common injective local plaque. Surjectivity follows from the uniform target disk and `S_n(x) v -> 0`. These are full injectivity and surjectivity proofs, not an unjustified extension of a germ.

For later use, the important continuity is the global map `(x,v) -> phi_x^(-1)(v)` into `X`, with `v` in the stable tangent bundle. The same inverse formula works with one sufficiently large `n` on a neighborhood of each fixed `(x,v)`. Thus this continuity is actually established and does not rely on an implicit ambient topology on all pairs of points on the same stable leaf.

### Lemma 2.8, pp. 10–11

In a single unstable-foliation box, the first integral `t` is constant on the unstable plaques. Therefore

`phi_y o h_xy^u o phi_x^(-1) = B_y^(-1) B_x`.

Differentiation at zero identifies the constant linear factor with `D_x h_xy^u`. The holonomy is holomorphic because it is holonomy of a holomorphic foliation between holomorphic transverse stable plaques. No regularity of the full stable foliation is used. This proves precisely a local germ identity at this stage; the paper correctly leaves global holonomy to Lemma 2.10.

## Detailed continuation check for Lemma 2.10, pp. 11–12

Choose the base path `gamma` inside a sufficiently small unstable plaque. The germ derivative

`L_t = D_x h_(x,gamma(t))^u`

exists for every `t` even before global continuation of holonomy on large disks is established. In the original transverse-coordinate box it is `B_(gamma(t))^(-1) B_x`, so it depends continuously on `t` and remains invertible. Define an entire stable-leaf map

`H_t = phi_(gamma(t))^(-1) o L_t o phi_x`.

Lemma 2.7 makes `(t,p) -> H_t(p)` continuous, and each `H_t` is biholomorphic between the two entire stable leaves. This alone does not declare it to be holonomy.

Now use a closed stable disk `K_R` and let `t_0` be the maximal common continuation time for genuine holonomy on an open neighborhood of `K_R`. There is a positive initial time by a finite cover of `K_R` and local product structure. For every `t < t_0`, the genuine holomorphic holonomy and `H_t` agree near `x` by Lemma 2.8; the identity theorem makes them agree on the connected disk wherever the holonomy has been continued. The continuous family on the compact parameter set gives uniform convergence to `H_(t_0)` on `K_R`.

For a fixed `p`, choose a foliation chart about `H_(t_0)(p)`. The path `H_t(p)`, for `t < t_0`, is genuine lifted holonomy and lies in this chart for all sufficiently late times by continuity. Its transverse chart coordinate is locally constant there, so it is constant throughout the connected final time interval. The limit belongs to that same unstable plaque. This justifies the paper's short assertion that the path lies in one plaque near `t_0`; it is not claiming that unstable leaves are closed in the ambient manifold.

The preceding reasoning is uniform on finitely many neighborhoods covering `K_R`: continuity of `H` puts their tails into the chosen charts, and the stable plaques about these points vary continuously with the leaf parameter. Standard local product continuation therefore supplies holonomy to `t_0` and beyond if `t_0 < 1`. The local continuations glue by uniqueness of continuation; equivalently the identity theorem identifies them with `H_t` on connected overlaps. This contradicts maximality unless `t_0 = 1`.

Taking all radii yields genuine entire holonomy equal to `H_1`. Invertibility is explicit from its formula. General endpoints on the same unstable leaf are reached by a finite chain of local unstable plaques along a compact path. Path independence of the germ follows from simple connectedness of Anosov unstable leaves (each is a Euclidean space); the global maps then agree by the identity theorem.

This argument uses compact disks in complete affine stable leaves, compactness of `X` for their initial uniform local structures, and continuity of the global inverse-coordinate family. It does not use topological transitivity, density of leaves, or a transverse invariant measure.

## Source checks and their limits

**Ghys 1995:** The original author's PDF is [Holomorphic Anosov systems](https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf), obtained via [Ghys's publications page](https://perso.ens-lyon.fr/ghys/papers/). Local copies are `references/Ghys1995.pdf` and `.txt`. I inspected Proposition 2.2, pp. 589–590; Proposition 3.1, pp. 590–593; and Lemma 5.1 and the following proof of Theorem B, pp. 597–598.

Ghys Proposition 2.2 has no transitivity hypothesis. Its literal wording is '(transversely) holomorphic foliation'; this terminology is not evidence that Zhang incorrectly assumes an ambient holomorphic foliation. Cantat's original paper explicitly restates the relevant conclusion as a holomorphic foliation and uses it that way in arbitrary dimension (see next paragraph). Ghys Lemma 5.1 uses transitivity to control transported disks via a full-support transverse measure. Zhang replaces that disk control with the continuous explicit entire maps `H_t`; the replacement addresses the particular role of transitivity in that lemma.

**Cantat 2004:** The official EMS PDF is [Difféomorphismes holomorphes Anosov](https://ems.press/content/serial-article-files/43027), local copies `references/Cantat2004.pdf` and `.txt`. Proposition 1.2, pp. 780–781, explicitly states the holomorphicity of the complementary foliation when the other foliation has complex dimension one. Section 5.1, p. 793, uses this as a smooth holomorphic foliation of codimension one, with no transitivity assumption. This independently corroborates the interpretation at the beginning of Zhang Section 2.

I did not independently reprove the stable manifold theorem/HPS regularity, the distributional Cauchy–Riemann theorem, or the topological surgery theorem used at the end of Ghys's proof. The parent review separately checks Proposition 2.9 and the final Franks–Manning implication. Nothing in these notes certifies the Lean formalization.


---

# Independent adversarial check of Section 2 global holonomy

Source reviewed: Jiesong Zhang, *Codimension-One Holomorphic Anosov Diffeomorphisms*, the supplied 19-page `source/2609.37695.pdf`, arXiv:2609.37695v3, dated 13 October 2026. Page numbers below are printed paper pages. This note independently checks the local-to-global mechanism after Lemma 2.7, concentrating on Lemma 2.10 (pp. 11–12). I also checked the corresponding Ghys argument in the original 1995 paper, pp. 597–598, available locally as `references/Ghys1995.pdf` and `Ghys1995-layout.txt`.

## Verdict

I find no mathematical counterexample or unrepaired obstruction to the global-holonomy conclusion. The delicate point is valid: continuous convergence of the actual holonomy **path**, rather than an arbitrary sequence of points in a possibly nonclosed leaf, gives the final single-plaque property. The initial simultaneous continuation across a large compact stable disk uses an elementary foliation-tube construction, not global product structure. The proof should spell these facts out. There is one literal compactness mistake: the displayed disk is the inverse image of an open ball and need not be compact. Replacing it with a closed disk repairs this throughout.

There is also a clean independent reconstruction from Lemmas 2.3, 2.4, and 2.7: a developing map on the universal cover, together with completeness of every stable affine line, directly produces global product structure. This entirely bypasses the potentially terse continuation paragraph and confirms that no global-product hypothesis has been smuggled in.

## Dependency reconstruction

1. Lemma 2.3 (pp. 7–8) supplies a flat holomorphic connection on the normal line bundle `L = T^(1,0)X / E^u`.
2. The local calculation in Lemma 2.4 (pp. 8–9) supplies `d_nabla pi = 0` and hence holomorphic transverse affine coordinates, with unstable plaques given by constant transverse coordinate.
3. Lemmas 2.5–2.7 (pp. 9–10) provide a continuous family of biholomorphic affine parametrizations `phi_x : W^s(x) -> E^s_x`, normalized at the base point. This is completeness of the transverse affine lines; it is stronger than merely knowing that individual stable leaves are biholomorphic to C.
4. Lemma 2.8 (pp. 10–11) makes each local unstable holonomy complex-linear in these normalized parametrizations. Thus its germ has a unique entire extension `H_t` and the extension varies continuously in both the base-path parameter and the stable point.
5. Compact-disk continuation identifies that entire extension with genuine unstable holonomy. Alternatively, the developing-map argument below directly supplies this identification.

None of steps 1–4 uses transitivity or a preexisting global product structure. In particular, the fact that the local affine coordinate has been defined geometrically, and that the same affine coordinate extends completely on every stable leaf, is the key additional input absent from an arbitrary foliation with biholomorphic C transversals.

## Challenge 1: ambient convergence and unstable plaques

The manuscript says that, for fixed `p`, the path `t -> h_t(p)` lies in one unstable plaque for `t < t_0` sufficiently close to `t_0`, and its limit belongs to that plaque. Merely saying that points on a nonclosed leaf converge in the ambient manifold would be insufficient: a sequence can visit different plaques of that leaf and approach a different leaf.

Here the stronger information actually present is enough. The prescribed `H_t(p)` exists continuously on the closed interval. Choose a foliation box about `H_(t_0)(p)`, and a smaller box whose closure lies in the first. For all `t` in a final interval `(t_0-delta,t_0)`, the path lies in this smaller box. Before `t_0` it is the genuine leafwise-continuous unstable lift of the base path. The transverse-coordinate function of an unstable foliation box is therefore locally constant along this path, hence constant on the connected final interval. Its limit has the same transverse coordinate and lies inside the larger box. Thus it belongs to exactly that plaque. No closedness of the global unstable leaf is used.

This is a routine missing explanation, not a valid objection to the theorem. The argument uses the continuity of the **whole final path**; it would not follow solely from convergence along selected times.

## Challenge 2: positive initial time for a large stable disk

One must use the closed stable affine disk

`K_R = phi_x^(-1)({v in E^s_x : ||v|| <= R})`,

and work initially in a slightly larger disk `K_(R+eta)` so that boundary points have surrounding plaques. It is a compact embedded disk in the intrinsic stable leaf, and also an embedded compact disk in the ambient manifold: the leaf inclusion is injective, and a continuous injection from a compact space to a Hausdorff space is an embedding.

A compact disk in a leaf admits a small foliated tube over that disk. In this setting the complementary unstable foliation supplies the transverse plaques. One way to see the construction is to cover the larger stable disk by finitely many simultaneous stable/unstable product boxes, transport a sufficiently small unstable transversal at `x` along paths within the disk, and shrink the transversal finitely many times so that all required transitions are defined. Independence of the chosen stable paths follows from their homotopies within the simply connected disk and the usual homotopy invariance of local foliation holonomy. The resulting neighboring stable disks are connected by unstable plaques over the entire smaller disk `K_R`.

Consequently, every sufficiently short initial segment of `gamma` has unstable holonomy defined simultaneously on `K_R`. This proves `t_0 > 0` without asserting product structure over a whole stable leaf. The same finite-tube argument around `H_(t_0)(K_R)`, which is a compact embedded disk in the target stable leaf, supplies a uniform further continuation after the endpoint has been reached. The local map obtained in the tube agrees with `H_t` near the base point by Lemma 2.8, and hence everywhere on its connected domain by the holomorphic identity theorem.

The argument is local around a compact disk of one leaf. A claim of a tube around an arbitrary noncompact entire leaf would be substantially stronger and is unnecessary.

## Challenge 3: leaf topology and monodromy

The equality `h_t = H_t` is an identity of maps into the intrinsic target stable leaf. This is justified because actual foliation holonomy takes a connected stable disk to a connected local continuation of that leaf and is holomorphic there; its germ agrees with `H_t` by Lemma 2.8. The identity theorem applies in this intrinsic complex curve. The ambient continuity of the family `H_t` is the continuity asserted for the inverses in Lemma 2.7.

For arbitrary `y in W^u(x)`, the chosen unstable path is compact and can be subdivided into finitely many segments lying in local unstable plaques. Compose the resulting entire biholomorphic holonomies. This is exactly the reduction in the first sentence of Lemma 2.10. There is no demand for a uniformly finite subdivision across all pairs `x,y`.

Global Anosov stable and unstable leaves are injectively immersed copies of real Euclidean spaces by the stable-manifold theorem. In particular, unstable leaves are simply connected; their holonomy germs have no path monodromy. Even if path independence were not stated, the assertion needed for Proposition 2.9 is obtained along each chosen unstable path, and the entire extension is uniquely determined by its germ. A null-homotopic loop has identity germ and hence identity entire extension.

## Independent proof using the developing map

This proof verifies the global conclusion without using Lemma 2.10 or assuming global product structure.

Let `Y` be the universal cover of `X`, with all bundles, forms and foliations lifted. Since the lifted connection is flat and `Y` is simply connected, it has a global nowhere-zero parallel section `sigma`. It is holomorphic because the connection has `(0,1)`-part `dbar`. Write

`pi = omega tensor sigma`.

The globally defined scalar holomorphic 1-form `omega` is closed: the local calculation `d_nabla pi = 0` in Lemma 2.4 gives `d omega = 0`. Therefore there is a global holomorphic function

`q : Y -> C`, with `dq = omega`.

It is a submersion and `ker dq = E^u`. Put `ell_x = dq_x|E^s_x`, a nonzero complex-linear map `E^s_x -> C`. On the stable leaf through `x`, the local definitions give

`q(p) = q(x) + ell_x(phi_x(p))`

near `x`. Both sides are holomorphic on that connected stable leaf, so the identity theorem extends the equality everywhere. Lemma 2.7 now says that `q` maps every stable leaf bijectively onto C.

Define `F = q^(-1)(0)` and

`r(x) = phi_x^(-1)(ell_x^(-1)(-q(x)))`.

This is the unique point where the stable leaf through `x` meets `F`. The map

`Psi : Y -> F x C`, `Psi(x) = (r(x), q(x))`

has inverse

`Psi^(-1)(r,z) = phi_r^(-1)(ell_r^(-1)(z))`.

Both maps are continuous, by the joint continuity in Lemma 2.7 and continuity of `ell_x`. The family of stable parametrizations lifts continuously to `Y`: this follows either from the same local-iteration formula or the covering homotopy property applied to the continuous family `(x,tv) -> phi_x^(-1)(tv)`, starting at `x`. Thus there is no covering-space continuity assumption hidden here.

Since `Y` is connected, the product representation implies that `F` is connected. Every fiber `q^(-1)(z)` is homeomorphic to `F`, so is connected. A connected fiber of a submersion whose kernel is the unstable tangent distribution is one unstable leaf: its connected components are precisely the maximal connected integral manifolds. We have therefore proved global product structure on the universal cover.

For lifted points `x,y` on the same unstable leaf, hence with `q(x)=q(y)`, the map

`p -> (q|W^s(y))^(-1)(q(p))`

is an entire biholomorphism `W^s(x) -> W^s(y)`. Each image point lies on the same unstable leaf as `p`, because those leaves are exactly the connected `q` fibers. Locally this map is the unstable holonomy, and along an unstable base path it gives its continuation. Projection to `X` supplies exactly Lemma 2.10. The stable leaves project bijectively to their original stable leaves, which are simply connected, so no quotient ambiguity arises.

This reconstruction also explains the endpoint continuation intuitively: the transverse affine developing coordinate is complete on every stable leaf, and its fibers cannot split into multiple unstable leaves because the stable lines provide a global product decomposition.

## Findings suitable for the referee report

* **Confirmed minor error, p. 11, Lemma 2.10:** `D_R` is defined using an open ball and is then repeatedly called compact. Use a closed ball, with a slightly larger disk during local continuation. This changes no mathematical conclusion.
* **Exposition needing expansion, pp. 11–12, Lemma 2.10:** state the finite foliated-tube argument for `t_0 > 0` and endpoint continuation; explain that the final holonomy path stays in one foliation box, so its transverse coordinate is constant. These are repairable local details, not an identified genuine proof gap.
* **No confirmed major error:** the entire analytic extensions remain genuine unstable holonomy. The developing-map construction provides an independent derivation from already established inputs and rules out the proposed circularity.

## Original-source cross-check and limits

Ghys's Lemma 5.1 (1995, pp. 597–598) also works with **closed** affine disks, and its continuation argument bounds the disk family using the invariant transverse measure available from transitivity. In the proof of Theorem B on p. 598, once global holonomy is established, Ghys derives a trivial developing fibration and an injective translation holonomy group. No new use of transitivity appears in that paragraph. The new manuscript replaces the compactness input with its globally defined, continuous affine extensions, which is a coherent replacement.

This note does not certify Proposition 2.9's final torus-topology argument, the upstream curvature estimate in Lemma 2.3, Sections 3–5, or any claimed Lean formalization. Its conclusion is conditional on the stated flat connection, the locally closed transverse form, and the continuous complete stable affine parametrizations, for which the independent reviewers are conducting the upstream checks. No public files were written and no author was contacted.


---

# Independent correctness review of Section 3 (Theorem 1.2)

Source: exact supplied `2609.37695.pdf`, 19 pages, arXiv:2609.37695v3, 13 October 2026. SHA-256: `3c8287bf41d153c7f0d0950b8a4b477546229333ee66ba7e9ae60e6a387920c6`.

## Outcome

I found no substantive mathematical error in the internal argument on pp. 12–14. Assuming the quoted Franks–Manning input, the proof of Theorem 1.2 is sound. Neither irreducibility of the toral automorphism nor a separate transitivity assumption is needed. The global holomorphic product step and convergence of the translated maps can both be reconstructed rigorously. The use of Bochner–Montgomery in this application can also be replaced by a short direct smoothing argument, given below.

This is an independent mathematical reading, not a formal verification. The original full texts of Franks [Fra69], Manning [Man74] and Bochner–Montgomery [BM46] were not successfully obtained in this section review. Their publisher/JSTOR bibliographic records were checked. A separate review of Ghys [Ghy95], p. 598, confirms that Ghys uses Franks–Manning after proving only that the manifold is homeomorphic to a torus. Do not report the original source audit as complete.

## Claim/dependency map

1. Theorem 1.2 hypotheses: compact connected complex X, f holomorphic Anosov, X homeomorphic to a real torus, both E^s and E^u holomorphic.
2. Franks–Manning supplies a conjugacy h to a hyperbolic affine toral automorphism. A translation removes its affine constant since I−A is invertible.
3. The lifted conjugacy H identifies the lifted stable and unstable foliations with affine subspaces parallel to V^s and V^u. This supplies global product structure on the universal cover.
4. Lemma 3.1: the projections of the lattice are dense in the respective subspaces. (The printed formula contains closure bars; PDF extraction drops them.)
5. Lemma 3.2: holomorphic transverse foliations + global product imply a global holomorphic product S×U. A deck transformation acts as a pair of biholomorphisms, so each stable/unstable component acts biholomorphically. Lattice-projection density extends this to every translated vector by locally uniform convergence.
6. Bochner–Montgomery, or the direct smoothing proof below, gives a smooth orbit map Θ=H^{-1}. Freeness/transitivity then make Θ a diffeomorphism.
7. All translations preserve the transported complex structure J_0 on V. Hence J_0 is constant, A commutes with J_0, and h descends to the required biholomorphic torus conjugacy.

## Detailed checks

### Franks–Manning input (p. 12)

The distinction between “homeomorphic to a torus” and “diffeomorphic to the standard smooth torus” deserves checking because exotic smooth tori exist. No unjustified smooth identification is subsequently made in Section 3: H initially remains a homeomorphism, and its smoothness is proved at the end. The proof therefore avoids assuming its intended regularity conclusion. Ghys’s original argument makes the same use of Franks–Manning on a merely homeomorphic torus; see the source-audit limitation above. In the actual dependency of Theorem A, Theorem 1.1 already provides topological toral conjugacy, so the application does not require a stronger topological classification assertion than that step has established.

An affine automorphism α(v)=Av+b has a fixed point: choose a representative b∈V and solve (I−A)v=b. Hyperbolicity excludes eigenvalue 1. Lifts F,H can be chosen compatibly so H F=A H. Identifying the deck lattice with Γ through h_* then gives H γ H^{-1}=L_γ. These are standard choices, not additional assumptions.

### Density of lattice projections (Lemma 3.1, pp. 12–13)

A direct proof eliminates reliance on an unstated minimality citation. If π(V^u) were not dense in V/Γ, its closed connected subgroup closure would have a nonzero annihilating character. Thus there would be 0≠ℓ∈Γ^* with ℓ|_{V^u}=0. The covectors ℓ∘A^n are nonzero lattice covectors and tend to zero: they vanish on V^u and A^n contracts V^s. This contradicts discreteness of Γ^*. Hence V^u+Γ is dense in V. Passing to the quotient by V^u proves density of p_sΓ in V^s. Apply the same argument to A^{-1} for p_uΓ.

This argument works for reducible hyperbolic toral automorphisms too. No rational irreducibility condition is missing.

### Global holomorphic product (Lemma 3.2, p. 13)

Let S=W^s(o), U=W^u(o), H(o)=0. The conjugacy gives continuous maps r_s=H^{-1}p_sH and r_u=H^{-1}p_uH, with image S and U, and unique intersections of all complementary leaves.

To see r_s is holomorphic near an arbitrary x, choose a finite leafwise path from x to r_s(x) in W^u(x). A finite chain of holomorphic foliation charts defines a holomorphic holonomy germ from a local stable transversal at x to S near r_s(x). Because r_s is continuous and the global intersection is unique, this germ agrees with r_s near x. Similarly r_u is holomorphic. Their differentials have complementary kernels E^u and E^s, so (r_s,r_u) is a holomorphic local biholomorphism. It is globally bijective by global product structure, hence a biholomorphism. This supplies the omitted local-to-global explanation of the product map B.

Since deck transformations preserve both lifted foliations and are biholomorphic, they act in these product coordinates as (ρ^s_γ,ρ^u_γ), where each factor is a biholomorphism. Their stable and unstable components are therefore biholomorphic. The displayed coordinate identities on p. 13 are type-correct, using H^{-1}|_{V^s} and H^{-1}|_{V^u} for the two factors.

### Locally uniform convergence (pp. 13–14)

If v_j→v, then H^{-1}L_{v_j}H→H^{-1}L_vH uniformly on every compact subset of the universal cover: H(K) plus the compact set {v_j}∪{v} lies in a compact subset of V, on which H^{-1} is uniformly continuous. Uniform convergence in coordinate charts implies the limit is holomorphic. Applying this also to −v_j ensures the inverse limit is holomorphic. This avoids the false general inference that a locally uniform limit of biholomorphisms must automatically be biholomorphic.

### Bochner–Montgomery formulation (Theorem 3.3, p. 14)

The broad statement printed in the paper is stronger in appearance than one frequently quoted form of [BM46], which explicitly assumes that no nonidentity element fixes a nonempty open set pointwise. The current application is safe under that stronger condition: the action is free. Moreover, the group here is already the Lie group (V,+), and all maps are biholomorphic. Thus there is no need to prove the general locally compact-group assertion in order to complete Section 3.

I have not confirmed from the original [BM46] full text whether its exact stated hypotheses equal those of Theorem 3.3. This is a citation/formulation check left open, not a demonstrated false theorem or a proof gap in the present application. A transparent editorial repair would state the stronger, sufficient version and note explicitly that freeness implies its hypothesis, or use the direct proof below.

Research-source corroboration: Baouendi–Rothschild–Winkelmann–Zaitsev, *Lie group structures on groups of diffeomorphisms and applications to CR manifolds*, Theorem 3.5, quotes the stronger version and attributes it to BM46. Accessible author-hosted PDF: https://www.maths.tcd.ie/report_series/tcdmath/tcdm0413.pdf. Downloaded as `references/baouendi-et-al.pdf`; see pp. 8–9 of that PDF. This is not a substitute for claiming the original BM46 text was checked.

### Independent proof of the regularity upgrade, avoiding BM46

Let Φ_v be the continuous V≅R^m action already proved biholomorphic, and let Θ(v)=Φ_v(x_0)=H^{-1}(v). Fix a holomorphic coordinate map z on a neighborhood of x_0. By continuity choose a smaller neighborhood W of x_0 and a small parameter ball B_{2ε} such that Φ_t(W) stays in the coordinate domain whenever t∈B_{2ε}. Choose a smooth compactly supported mollifier ρ_ε in B_ε with integral 1, and set

    z_ε(x) = ∫ ρ_ε(t) z(Φ_t(x)) dt.

This is holomorphic in x. As ε→0, z_ε→z locally uniformly; Cauchy estimates give C^1 convergence on smaller coordinate neighborhoods. Hence, for sufficiently small ε, z_ε is a holomorphic coordinate map near x_0. For sufficiently small v,

    z_ε(Θ(v)) = ∫ ρ_ε(t) z(Φ_{t+v}(x_0)) dt
              = ∫ ρ_ε(s−v) z(Φ_s(x_0)) ds.

All v derivatives fall on the smooth compactly supported kernel; the other factor is continuous. The expression is C^∞ in v. Applying the holomorphic inverse coordinate map proves Θ is C^∞ near 0, and Θ(v+w)=Φ_v(Θ(w)) proves smoothness near every v.

Also DΘ_v=DΦ_v|_{x_0} DΘ_0, so DΘ has constant rank. Since Θ is already a homeomorphism onto the entire universal cover, the constant-rank theorem excludes rank<m: the local image would otherwise lie in a lower-dimensional submanifold and could not be open. Thus Θ is a local diffeomorphism everywhere and, being bijective, a global diffeomorphism. This fully reconstructs the regularity step using only local complex analysis and elementary real differential topology.

### Final transported complex structure (p. 14)

Once H is smooth, J_0=H_*J is a smooth complex structure on V. Holomorphicity of every Φ_v is exactly invariance of J_0 under all translations, which makes J_0 constant. Holomorphicity of F and H F H^{-1}=A give A J_0=J_0 A. The Γ-equivariant H therefore descends to a biholomorphism X→(V,J_0)/Γ and conjugates f to a holomorphic torus automorphism. No unjustified conclusion from topological to complex torus occurs.

## Source access and coverage

Internal Section 3 proof: fully read and reconstructed, conditional only on its standard topological classification input. No confirmed mathematical errors found there.

Original source bibliographic links: Franks [Fra69], https://doi.org/10.1090/S0002-9947-1969-0253352-7 and https://www.jstor.org/stable/1995062; Manning [Man74], https://www.jstor.org/stable/2373551; Bochner–Montgomery [BM46], https://www.jstor.org/stable/1969226. Direct AMS PDF returned HTTP 403. JSTOR PDF requests returned 3,038-byte HTML challenge pages, not usable PDF text. The unusable responses were removed so they cannot be mistaken for checked reference PDFs.

The mathematical correctness of the narrower BM application has been independently established above even though its original citation audit remains incomplete. No claims about the correctness of Sections 2, 4, 5 or any Lean formalization are made by these section-specific notes.


---

# Independent correctness review of Section 4

Reviewer scope: Theorem 1.3 and Lemmas 4.1–4.3, printed pp.14–17; the use of Lemma 2.7 on p.10; the Ghys and Demailly inputs needed here. Reviewed attachment: Jiesong Zhang, *Codimension-One Holomorphic Anosov Diffeomorphisms*, arXiv:2609.37695v3, 13 October 2026, 19 pages, SHA-256 `3c8287bf41d153c7f0d0950b8a4b477546229333ee66ba7e9ae60e6a387920c6`.

## Verdict for this section

I found no confirmed mathematical error in the Section 4 arguments. Conditional on Theorem 1.1 (including its global product structure consequence), the holomorphicity of the codimension-one unstable foliation, and Lemma 2.7, Lemmas 4.2 and 4.3 give the claimed holomorphic stable line bundle. In particular, the Jacobian and singular-value estimate on p.17 is valid: it does not assume that the selected volume is invariant, and it does not require a bunching inequality between the largest and smallest unstable exponents.

Confidence is high for the algebraic and analytic estimates in Lemma 4.3, and high for the deck transformation descent in Lemma 4.2 under its stated inputs. This is a mathematical reading and reconstruction, not formal verification. The central global holonomy argument of Section 2 is outside this reviewer's assigned section and was not independently certified here.

## Claim and dependency map

1. Ghys Proposition 2.2, applied to the inverse map, supplies the holomorphic codimension-one foliation tangent to `E^u` when `dim_C E^s = 1`.
2. Theorem 1.1 supplies a toral conjugacy and hence a universal-cover global product decomposition; no regularity of the conjugacy is differentiated.
3. Lemma 2.7 supplies a biholomorphic coordinate on each stable leaf, equivariant under the stable derivative cocycle.
4. At the fixed lift of the origin, this coordinate conjugates the stable restriction to multiplication by a scalar `mu`, `0 < |mu| < 1`.
5. Projection along lifted unstable leaves to this stable leaf gives the holomorphic submersion `q : X_tilde -> C`.
6. A nontrivial deck translation cannot preserve an unstable leaf; consequently its induced automorphism of `C` is a translation. Thus `dq` descends to a nowhere-zero closed holomorphic one-form `theta` with `ker(theta)=E^u` and `f^*theta=mu theta` (Lemma 4.2).
7. Normalize the continuous stable vector field by `theta(e)=1`. Pulling back a smooth normalized field `e_0` produces smooth `e_n` tending uniformly to `e`.
8. The antiholomorphic derivatives of `e_n` lie in the expanding bundle. The complex Jacobian supplies exactly enough volume weight to show `||dbar e_n||_L2 -> 0` (Lemma 4.3).
9. Distributional closedness and the distributional Cauchy–Riemann theorem make `e` holomorphic (Lemma 4.1), so its span is a holomorphic line bundle.

There is no circular dependence on holomorphicity of `E^s` in this chain. Prior to its proof, the stable leaves are individually complex submanifolds; a foliation with holomorphic tangent bundle is not needed to restrict holomorphic maps to an individual leaf.

## Lemma 4.1 (p.15): distributional criterion

This is correct. In a holomorphic frame the Dolbeault operator is coefficientwise distributional differentiation, which is continuous. Thus the two assumed limits give `dbar s=0`. The continuous coefficients coincide with the holomorphic distributions given by the distributional Cauchy–Riemann theorem, yielding actual holomorphic functions. The fact that the approximating sections in the lemma are only continuous causes no difficulty: their Dolbeault derivatives are well defined as distributions. In the application they are smooth.

The cited original source was checked: Demailly, *Complex Analytic and Differential Geometry*, version 21 June 2012, Chapter I, Lemma (3.29)(a), printed p.28, explicitly treats the current/distribution case and concludes that a `dbar`-closed `(p,0)` current is a holomorphic form. Taking `p=q=0` is appropriate. The nearby Corollary (3.30), printed p.29, gives an alternative regularity formulation.

## Lemma 4.2 (pp.15–16): independent reconstruction

Let `p=H^{-1}(0)`. The compatibility `H F=A H` and invertibility of `H` imply `F(p)=p`; therefore `F` preserves the stable leaf `S` through `p`. Lemma 2.7 gives a biholomorphism `phi:S -> E_p^s ~= C`. Its equivariance gives `phi F phi^{-1}(z)=mu z`, where `mu` is the stable derivative at `p`. Hyperbolicity and invertibility give `0<|mu|<1`.

Global product structure makes every lifted unstable leaf meet `S` in exactly one point. Define `q` by applying `phi` to that point. Locally the projection is a composition of finitely many holonomy germs along a path in an unstable leaf. Because this foliation is holomorphic and the stable leaf is a complex transversal, each such germ is holomorphic. In a foliation box this is a holomorphic submersion; its kernel is the unstable tangent bundle. Thus both identities in (23) follow, including the scalar equivariance.

For a deck transformation `Phi_gamma`, the induced map can be written explicitly as

`g_gamma = q o Phi_gamma o phi^{-1}: C -> C`.

It is holomorphic; the corresponding expression with `-gamma` is its inverse. Hence it is a biholomorphism of `C`, and therefore affine. A fixed point of `g_gamma` would mean `Phi_gamma` preserves the entire fiber of `q`, an unstable leaf. On the toral universal cover that would imply `gamma in V^u`. But `A^{-n} gamma` is then a sequence of nonzero lattice points tending to zero, contrary to lattice discreteness. This uses that `A` is an invertible lattice automorphism, not merely a lattice endomorphism. Therefore for `gamma != 0` the affine map has no fixed point, forcing its linear coefficient to equal one. For `gamma=0` it is the identity. Consequently every deck transformation preserves `dq`.

The descended form is holomorphic, nowhere zero and closed, since these properties are local and hold for `dq`. Its kernel and eigenvalue identity follow by pullback to the universal cover. There is no implicit need for the deck translations to act properly discontinuously on `C`; the induced translation subgroup can be dense, and the argument does not form a quotient of `C` by it.

## Lemma 4.3 (pp.16–17): independent reconstruction

### Existence and convergence of approximations

Since `theta` is a nonzero covector everywhere and the invariant splitting is complementary, it restricts to an isomorphism on the stable complex line. Thus the field `e` is globally defined and continuous, and is nowhere zero. A smooth normalized field `e_0` exists, for example by taking the metric dual of `theta` divided by its squared norm.

The equivariance of `theta`, preservation of the stable line and its normalization give

`D f^n e = mu^n (e o f^n)`.

Since `theta(e_0-e)=0`, the difference belongs to `E^u`. Therefore (24) gives exactly

`e_n-e = mu^n U_n^{-1} ((e_0-e) o f^n)`.

Uniform boundedness of the continuous difference on compact `X`, together with uniform unstable expansion, gives uniform convergence. Although `e` is only continuous at this stage, every `e_n` is smooth because `f` and `e_0` are smooth.

### Antiholomorphic derivative and type

The inverse derivative of a holomorphic diffeomorphism is holomorphic in local holomorphic frames. Differentiating the pullback vector field therefore produces no derivative of that factor in the antiholomorphic directions. Formula (25) is the standard chain rule. Strictly as a map of complex bundles, its final `D f^n` acts on the antiholomorphic tangent factor, i.e. by the conjugate of the complex `(1,0)` derivative; the displayed notation can equally be read as the real differential restricted to `(0,1)` vectors. Its operator norm is identical, so this is harmless notation, not a mathematical error.

Holomorphicity of `theta` and `theta(e_0)=1` imply `theta(dbar e_0)=0`, so `dbar e_0` takes values in `E^u`. This justifies replacing the full inverse derivative by `U_n^{-1}` in (26). The selected Hermitian metric is smooth because `E^u` is holomorphic, `e_0` is smooth and never zero, and the specified direct sum is smooth.

### Full derivative bound in (28)

The bound `||D f^n|| <= C ||U_n||` is valid despite the noninvariance of the complement `C e_0`. To see this independently, decompose a vector in the continuous invariant splitting `E^s + E^u`. Compactness bounds both projections. Its unstable component grows by at most `||U_n||`; its stable component grows by `|mu|^n` times a bounded ratio of the norms of `e` at its endpoints. Uniform expansion makes `||U_n||` dominate this latter bound uniformly for all `n>=1`, after enlarging a fixed constant. Thus the off-diagonal block cannot cause an additional exponential factor.

### Determinant, singular values and integration

In unitary frames for the smooth orthogonal splitting `E^u + C e_0`, the quotient derivative is exactly multiplication by `mu^n`, because `theta(e_0)=1` at both source and target. The triangular block form therefore gives the exact real-volume Jacobian

`J_n = |mu|^(2n) |det_C U_n|^2`.

No metric determinant has been omitted. The real determinant of a complex-linear map is the square of the modulus of its complex determinant, with the same source and target Hermitian unitary-frame conventions used here.

Write the singular values of `U_n` as `sigma_1 >= ... >= sigma_(d-1) > 0`. For sufficiently large `n`, uniform hyperbolicity makes every singular value at least one. Consequently

`|det_C U_n| = product sigma_j >= sigma_1 = ||U_n||`.

If `m_n=sigma_(d-1)`, (26) and the boundedness of `dbar e_0` give

`|dbar e_n|^2 <= C |mu|^(2n) m_n^(-2) ||U_n||^2 <= C m_n^(-2) J_n <= C lambda^(-2n) J_n`.

All constants are independent of the base point and `n`. Integrating is legitimate with respect to the selected smooth Hermitian volume. The change-of-variables identity for the diffeomorphism `f^n` gives `integral_X J_n dnu = nu(X)`; invariance of `nu` is unnecessary. Thus the `L^2` norm tends to zero exponentially.

Finally, `L^2` convergence to zero implies distributional convergence locally by Cauchy–Schwarz. Uniform convergence of `e_n` implies its distributional convergence to `e`. Lemma 4.1 applies to the holomorphic tangent bundle, giving the result. No pointwise derivative convergence is asserted or required.

## Lemma 2.7 dependency (p.10)

I checked the use of this lemma in Section 4 and its displayed dynamical extension argument. Conditional on Lemmas 2.5 and 2.6, formula (18) is independent of sufficiently large `n` by local equivariance. Stable contraction brings any two chosen points into the uniform injectivity domain and proves injectivity. It also shrinks any fixed vector into the uniform target ball, proving surjectivity. The resulting inverse is holomorphic because the map is a locally biholomorphic injective holomorphic map of Riemann surfaces. Continuity of the family follows locally using one common sufficiently large iterate. This is a standard, valid local-to-global iteration. I did not re-review the construction of the connection in Lemmas 2.2–2.3 as part of this assignment.

## Primary citations checked and terminology resolved

- Ghys, *Holomorphic Anosov systems*, Invent. Math. 119 (1995), 585–614, [author-hosted original](https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf), Proposition 2.2, pp.589–590. Its unstable complex line hypothesis is correctly converted to the submitted paper's stable complex line hypothesis by applying it to the inverse. No transitivity hypothesis occurs in this proposition.
- Ghys uses the parenthetical terminology “(transversely) holomorphic” in the proposition, and his following surface remark distinguishes transverse from full holomorphicity. I flagged this for cross-check rather than treating it as a counterexample. The independent primary paper by Cantat, *Diffeomorphismes holomorphes Anosov*, CMH 79 (2004), Proposition 1.2, pp.780–781, restates precisely the full holomorphic-foliation conclusion used by Zhang; section 5.1, p.793, explicitly uses it in arbitrary dimension before introducing any projectivity assumption for that local statement. This supports the usage in the submission. It is not counted here as a confirmed citation error or a gap.
- Demailly, [*Complex Analytic and Differential Geometry*, exact 21 June 2012 version](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), Chapter I, Lemma (3.29)(a), printed p.28. The title page confirms the version. Local PDF: `source/demailly-agbook-2012.pdf`, SHA-256 `d7c7654a7417e8322e5dcf8fe8ec818b4c1a18cf280b41f2df5a871b776d89a1`.

No claim about Theorem 1.1's global holonomy step is based on the citation cross-check above; that step still needs its separate review.

## Classification and coverage

- **Confirmed errors:** none in assigned Section 4.
- **Substantive proof gaps established:** none in assigned Section 4, conditional on the earlier theorem and lemmas identified above.
- **Resolved concern:** Ghys's transverse-holomorphic wording, checked against Cantat's precise use of the same input.
- **Harmless exposition:** conjugate tangent factor in (25)–(26) is implicit; (28)'s second inequality could include the one-sentence invariant-splitting justification supplied above.
- **Not checked here:** Section 2's construction and global holonomy continuation in full; Section 3; Section 5 and its lattice example; other bibliography entries; independent proofs of the general stable manifold and holomorphic-foliation facts used in the cited established results.

No public posting, author contact, or modification of the supplied attachment was performed.


---

# Independent review: introduction and final example

Reviewer scope: submitted PDF `2609.37695.pdf`, arXiv:2609.37695v3, 13 October 2026, 19 pages. Source SHA-256 supplied by lead reviewer: `3c8287bf41d153c7f0d0950b8a4b477546229333ee66ba7e9ae60e6a387920c6`.

This note independently checks Section 5 (printed pp. 17–18) and the mathematical scope/dependency claims in Section 1 (pp. 1–5). It does not certify Sections 2–4 or the manuscript's stated Lean formalisation.

## Result

**No mathematical error found in Section 5.** Its group, lattice, complex structure, quotient automorphism, hyperbolicity, and non-holomorphic invariant distributions all survive direct verification. In particular, a tempting objection that the multiplication uses complex conjugation is unfounded: the manuscript correctly calls this a **real** nilpotent Lie group, and the multiplication is holomorphic in the right variable when the left factor is fixed. That is exactly what is needed for the left lattice quotient to inherit the standard complex structure.

The introductory uses of Ghys's Theorems A/B and Proposition 2.2 and Cantat's Theorem 1.4/Example 1.5 agree with the checked originals, allowing reversal of the diffeomorphism for stable/unstable conventions.

## Section 5: explicit reconstruction

Write one factor as

\[
(x,y,z)*(x',y',z')=(x+x',y+y',z+z'+\bar x y').
\]

The full group is the product of two such real groups, with coordinates `(a,b,c)` in the second factor.

1. **Associativity and inverses (p. 18, first display).** The central coordinate in either bracketing of three factors is
   \[
   z+z'+z''+\bar x y'+\bar x y''+\bar x' y''.
   \]
   The identity is zero and
   \[
   (x,y,z)^{-1}=(-x,-y,-z+\bar x y).
   \]
   All operations are smooth real polynomial maps. The underlying space is `C^6`, hence simply connected. The commutator in one factor is `(0,0,bar(x)y'−bar(x')y)`, central, so the group is two-step nilpotent and nonabelian.

2. **Complex structure (p. 18, sentence following the group law).** For fixed `(x,y,z)`, left multiplication sends `(x',y',z')` to affine holomorphic functions of these primed variables. Thus the standard integrable complex structure on `C^6` is left invariant, and left multiplication by the lattice acts biholomorphically. Joint holomorphicity of multiplication is neither claimed nor needed. Right multiplication generally is not holomorphic; this is not a complex Lie group with this `J`.

3. **The arithmetic embedding is a lattice (p. 18, definition of `R` and `Gamma`).** Every element of `R=Z[i,sqrt(3)]` has a unique expression
   \[
   m+ni+p\sqrt3+qi\sqrt3,\qquad m,n,p,q\in\mathbb Z.
   \]
   The embedding `alpha ↦ (alpha,sigma alpha)` has real-linearly independent basis vectors `(1,1)`, `(i,i)`, `(sqrt(3),−sqrt(3))`, `(i sqrt(3),−i sqrt(3))`. It is therefore a full lattice `L` in `C^2` (covolume 12 in standard real coordinates). The coordinate set `Gamma` is the product of three copies of this lattice, after grouping `(x,a)`, `(y,b)`, `(z,c)`.

   It is a subgroup: the first three new coordinates of a product are
   \[
   \alpha+\alpha',\quad\beta+\beta',\quad
   \gamma+\gamma'+\bar\alpha\beta'\in R,
   \]
   and their last-three counterparts are their `sigma` images because `sigma` commutes with ordinary complex conjugation. The inverse formula preserves `R` for the same reason. Discreteness follows from the displayed full lattice embedding. Cocompactness can be checked directly: multiply on the left by elements with `beta=gamma=0` to reduce `(x,a)` to a fixed compact fundamental parallelepiped for `L`; multiply by elements with `alpha=gamma=0` to reduce `(y,b)`; finally use central elements `alpha=beta=0` to reduce `(z,c)`. All coordinates then lie in fixed compact parallelepipeds. This gives a compact set meeting every left coset.

4. **Non-torus assertion on p. 4.** Since `G` is contractible, `pi_1(Gamma\G)=Gamma`. The elements
   \[
   g=(1,0,0,1,0,0),\quad h=(0,1,0,0,1,0)
   \]
   have commutator `(0,0,1,0,0,1)`, so this fundamental group is nonabelian. Consequently the example is not homeomorphic to a torus. This strengthens the terse claim on p. 4 with a direct invariant.

5. **Automorphism (p. 18, definition of `F`).** With `lambda=2+sqrt(3)>1`, `lambda^{-1}=2−sqrt(3)` and `sigma(lambda)=lambda^{-1}`. For the first central cross term,
   \[
   \overline{\lambda^2x}\,\lambda^{-1}y'=\lambda\bar x y',
   \]
   matching the weight of `z`; for the second,
   \[
   \overline{\lambda^{-2}a}\,\lambda b'=\lambda^{-1}\bar a b',
   \]
   matching `c`. Thus `F` is a group automorphism; its inverse has the reciprocal weights. It is complex linear in the standard coordinates and hence holomorphic. On `Gamma`, its first three coordinates are obtained by multiplying `(alpha,beta,gamma)` by `(lambda^2,lambda^{-1},lambda)`, and the remaining coordinates are their `sigma` images. These multipliers and their inverses belong to `R`, so `F(Gamma)=Gamma`, rather than merely inclusion. Therefore the descended map is a biholomorphism.

6. **Invariant frame and Anosov estimates (p. 18, frame and multiplier displays).** Differentiating left multiplication at the identity gives precisely the six smooth vector fields in the manuscript. They are left invariant and descend to a global smooth complex frame on the quotient. For example,
   \[
   DF(Y_p)=\lambda^{-1}\partial_y+\lambda\bar x\partial_z
            =\lambda^{-1}Y_{F(p)}.
   \]
   The six multipliers are exactly `(lambda^2,lambda^{-1},lambda,lambda^{-2},lambda,lambda^{-1})`. Declare the descended frame unitary for a smooth Hermitian metric. Then on `E^s=span_C{Y,A,C}`, `||Df^n||≤lambda^{-n}` and on `E^u=span_C{X,Z,B}`, `||Df^{-n}||≤lambda^{-n}` for all `n≥0`. This proves uniform hyperbolicity directly. Both complex ranks are 3, so the example does not satisfy the codimension-one assumption in Theorem A or Theorem 1.3.

7. **Non-holomorphic bundles (p. 18, final displays).** In standard holomorphic coordinates,
   \[
   \bar\partial Y=d\bar x\otimes Z,\qquad
   \bar\partial B=d\bar a\otimes C.
   \]
   The smooth sections `Y` and `B` belong respectively to `E^s` and `E^u`, but their antiholomorphic derivatives have respectively a nonzero `Z` component modulo `E^s` and a nonzero `C` component modulo `E^u`. A holomorphic subbundle has its smooth sections preserved by the ambient Dolbeault operator. Thus both bundles are indeed non-holomorphic. The use of coordinate test vectors is local, so they need not descend globally.

The claim that this example is consistent with an algebraic classification is correct in the explicit sense established in the text: it is induced by a real nilpotent group automorphism preserving a left invariant integrable complex structure. The original Ghys conjectural sentence does not supply a more detailed definition of “complex infra-nilmanifold”; the report should not silently replace the explicit model here by a quotient of a complex Lie group.

## Introduction and primary-source checks

### Ghys 1995

Primary source: Étienne Ghys, *Holomorphic Anosov systems*, Invent. Math. 119 (1995), 585–614, author-hosted PDF: <https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf>. Inspected local text `working-reference/references/Ghys1995-layout.txt`.

- **Original p. 585, Theorem A:** compact complex surfaces supporting holomorphic Anosov maps are complex tori and the maps are holomorphically conjugate to linear automorphisms. This matches the manuscript's dimension-two base case.
- **Original pp. 585–586, Theorem B:** transitive holomorphic Anosov maps with complex one-dimensional unstable foliation have torus topology and linear topological models. Applying this to `f^{-1}` switches to the manuscript's rank-one stable convention. The explicit transitivity hypothesis is correctly identified in submitted p. 2.
- **Original p. 589, Proposition 2.2:** a rank-one unstable foliation implies that the stable foliation is transversely holomorphic; no transitivity hypothesis is present. Reversing `f` gives the manuscript's holomorphic `E^u` when `dim_C E^s=1`.
- **Original p. 586, conjectural sentence:** holomorphic conjugacy to an automorphism of a complex infra-nilmanifold is indeed proposed. The submitted paper's use of “affine” is compatible with the ordinary algebraic model convention; the original sentence itself does not spell out a definition.
- **Original pp. 597–598, Lemma 5.1 and proof of Theorem B:** transitivity supplies a full-support transverse invariant measure, which gives a compactness argument for global holonomy. After that lemma, the torus conclusion is obtained from the common developing image, free translation holonomy, and Franks–Manning. This supports the submitted p. 2 description that the assumed transitivity is used at the global-holonomy step. Ghys earlier derives transitivity conditionally in Lemma 4.3 from a hypothetical nonzero measure; that is not an added standing transitivity hypothesis.

### Cantat 2004

Primary source: Serge Cantat, *Difféomorphismes holomorphes Anosov*, Comment. Math. Helv. 79 (2004), 779–797. Publisher PDF: <https://ems.press/content/serial-article-files/43027>. A copy was saved at `working-reference/references/Cantat2004.pdf` (224773 bytes).

- **Original p. 781, Theorem 1.4(a):** projective plus both invariant foliations holomorphic gives a finite torus cover and a linear model. **Part (b):** projective plus complex codimension one gives a torus and linear model. This is consistent with submitted p. 2, provided “corresponding classification” in the general-holomorphic-foliation case is understood to permit the finite quotient, as the context of Ghys's conjecture does.
- **Original p. 781, Example 1.5:** the construction is a free involution quotient of `A×A`, where `A=C^2/Lambda^2`, with involution `(a,b)↦(a+tau,−b)` and hyperbolic linear map `[[3,2],[2,1]]` on each factor. Its eigenvalues are `2±sqrt(5)`, one inside and one outside the unit circle, giving complex stable and unstable ranks 2. The half-period `tau=(1/2,1/2)` is fixed modulo the lattice because the matrix sends it to `(5/2,3/2)`. Hence the involution commutes with the map and is free. The quotient is not homeomorphic to a torus: on its universal-cover deck group the involution lift conjugates translations in the second `A` factor to their inverses, producing a nonabelian fundamental group. This verifies the stronger topology wording in submitted p. 4, rather than relying only on Cantat's phrase that it is not a torus.

### Scope/quantifiers

- The complex-dimension-three consequence on p. 2 is valid: invariant bundles are complex by holomorphicity of `f`, are nonzero for an Anosov diffeomorphism of a positive-dimensional compact manifold, and their ranks sum to 3.
- The displayed Theorems A and 1.1–1.3 say “compact complex manifold” without repeating “connected.” The abstract and initial definition on p. 1 specify connectedness, so this is at most a scope clarification under that standing convention. If theorem statements are meant to stand independently, insert “connected”: a disjoint union of two copies of a complex torus with the same Anosov automorphism is an immediate counterexample to the literal connected-torus conclusion. This is **not a substantive objection to the intended connected-manifold theorem**.
- The final example gives exactly the advertised higher-codimension obstruction to the regularity conclusion; it supplies no counterexample to the claimed codimension-one classification.

## Claim/dependency map for reviewed material

| Submitted location | Claim | Dependencies checked | Outcome |
|---|---|---|---|
| p. 2, known surface case | Rank-one argument can use Ghys Theorem A in dimension 2 | Ghys original p. 585 | Citation matches |
| p. 2, known transitive case | Ghys Theorem B needs transitivity | Ghys original pp. 585–586, 597–598 | Citation and use match |
| pp. 3, 5 | Rank-one stable implies holomorphic unstable bundle | Ghys original Prop. 2.2, `f↦f^{-1}` | Citation matches |
| p. 4, higher-codimension topology | Cantat has non-torus complex fourfold, ranks `(2,2)` | Original Ex. 1.5; explicit eigenvalues and π1 action | Verified |
| p. 18, compact quotient | Real group + arithmetic lattice + left holomorphic action | Direct group/lattice computations | Verified |
| p. 18, holomorphic Anosov automorphism | Group weights, preserved lattice, smooth diagonal frame | Direct formulas and uniform estimates | Verified |
| p. 18, non-holomorphic invariant bundles | Dolbeault derivatives leave the bundles | Direct local calculation | Verified |

## Coverage and limits

Read all of submitted Section 1 and Section 5; independently reconstructed all substantive calculations in Section 5; checked the specified Ghys and Cantat primary-source statements. Did not independently audit the historical Borel–Smale attribution in [Sma67], the Catanese/Catanese–Oguiso–Peternell background examples, Xu–Zhang's partially hyperbolic constructions, Zhang's separate preprint, all original Franks/Manning statements, or the formalisation repository. Those contextual claims are not premises in the direct verification of Section 5. No document-embedded code was run and no public write or author contact occurred.


---

# Bounded primary-source audit: classification and transformation-group citations

Private review of Zhang, *Codimension-One Holomorphic Anosov Diffeomorphisms*, arXiv:2609.37695v3, submitted PDF `working-reference/source/2609.37695.pdf`. This note supplements the section reviewers; it does not reprove the classification theorems.

## Conclusions

1. **No demonstrated hypothesis defect in the use of Franks–Manning on p. 12.** The distinction between a manifold homeomorphic to a torus and a manifold with the standard torus smooth structure is real, but the needed topological-conjugacy conclusion is explicitly supported by a later primary research paper. Ghys also uses precisely this implication in the proof of Theorem B, p. 598. The original Franks and Manning articles were not successfully obtained, so their exact original formulations and proofs remain unchecked.
2. **The smoothness upgrade on p. 14 is supported for the action actually constructed.** A checked modern statement of Bochner–Montgomery has a stronger hypothesis than global effectiveness: an element fixing every point of a nonempty open set must be the identity. The paper's action is free, hence satisfies this condition automatically. No gap in this application follows from the difference in theorem wording. The original 1946 article remains inaccessible in this audit.
3. **The high-dimensional homotopy-torus rigidity needed in the Ghys reduction is verified at the level of an original theorem statement.** Hsiang–Wall's 1969 primary note explicitly treats closed topological manifolds homotopy equivalent to a torus in dimensions at least five. This includes the real dimensions at least six arising here. This is a stronger and more directly usable source for this implication than the earlier Hsiang–Shaneson PNAS note alone.

## 1. Franks–Manning: torus topology versus torus smooth structure

**Paper use.** Section 3, p. 12 assumes `X` is a compact complex manifold homeomorphic to a real torus (Theorem 1.2) and obtains a homeomorphism conjugating `f` to a hyperbolic affine toral automorphism.

**Checked primary research source.** David Fisher, Boris Kalinin, Ralf Spatzier, with an appendix by James F. Davis, *Global rigidity of higher rank Anosov actions on tori and nilmanifolds*, Journal of the American Mathematical Society **26** (2013), 167–198, p. 169, introductory paragraph immediately before Theorem 1.3. The authors explicitly state that an Anosov diffeomorphism on a smooth manifold homeomorphic to an infra-nilmanifold has an affine model with a homeomorphic conjugacy. The torus case is included. This statement requires no transitivity or standard-smooth-structure hypothesis. This is corroboration by a primary research paper, not an examination of the original proof.

Source: <https://jfdavis.pages.iu.edu/papers/fksd.pdf>.

Local files: `references/fisher-kalinin-spatzier.pdf` and `references/fisher-kalinin-spatzier.txt`.

PDF SHA-256: `bb29f8fca13fc39f4f550a076a290a3c0f99a44d1f7e51132a4d8c74f0c3f246`.

**Checked earlier primary source.** Étienne Ghys, *Holomorphic Anosov systems*, Inventiones mathematicae **119** (1995), 585–614, p. 598, proof of Theorem B. Ghys first obtains the homotopy type of a torus, promotes this to homeomorphism with a torus, then invokes Franks–Manning to conclude topological conjugacy to an automorphism. This is exactly the category transition at issue in Zhang's p. 12.

Local source: `references/Ghys1995.pdf`; inspectable extraction: `references/Ghys1995-layout.txt`, around lines 659–671.

**Original-source access limits.**

- Franks, *Anosov diffeomorphisms on tori*, Trans. AMS **145** (1969), 117–124, DOI <https://doi.org/10.1090/S0002-9947-1969-0253352-7>. The publisher PDF returned HTTP 403 at both the `/journals/tran/` and `/tran/` canonical paths, in both shell and web fetches. Search-index text of the introduction mentions the older nonwandering-set hypothesis; it was not used as proof of the final Franks–Manning theorem.
- Manning, *There are No New Anosov Diffeomorphisms on Tori*, Amer. J. Math. **96** (1974), 422–429, DOI <https://doi.org/10.2307/2373551>. JSTOR's nominal PDF URL redirected to an HTML client challenge; no article pages were obtained. The unusable HTML response originally named `references/manning1974.pdf` was removed; it was not treated as a checked PDF.
- Franks's 1970 survey was not obtained in this bounded audit. No separate verification of its internal hypotheses or the original Franks–Manning proofs is claimed.

**Review disposition.** Do not list the homeomorphic/standard-smooth torus distinction as a proof gap. If the final report discusses citation coverage, distinguish the checked primary research restatements from the inaccessible original articles.

## 2. Bochner–Montgomery smoothness of the translation action

**Paper use.** Theorem 3.3, p. 14 asserts that a locally compact group acting effectively and continuously by smooth diffeomorphisms has a Lie structure and smooth action. Its application uses the already-known Lie group `(V,+)`, acting freely and transitively by biholomorphisms.

**Checked modern primary statement.** M. S. Baouendi, L. P. Rothschild, J. Winkelmann, D. Zaitsev, *Lie group structures on groups of diffeomorphisms and applications to CR manifolds*, Annales de l'Institut Fourier **54** (2004), 1279–1303, Theorem 3.5 (near the end of Section 3). In this formulation the locally compact group acts continuously by smooth diffeomorphisms, and the only element fixing an entire nonempty open subset is the identity. The conclusion includes smoothness of the joint action.

Source: <https://numdam.org/articles/10.5802/aif.2050/>.

Local files: `references/baouendi-et-al.pdf`, `references/baouendi-et-al.txt`, extraction lines 348–353.

**Hypothesis check for the actual application.** A nonidentity element of a free action fixes no point, so cannot fix an entire nonempty open subset. The stronger hypothesis is therefore available. The action is already continuous by its construction through a homeomorphism, and each action map is biholomorphic, hence smooth. This supports the application even if the paper's general wording of Theorem 3.3 is broader than the particular source statement checked here. An independent elementary proof for the free vector-group case is supplied in the Section 3 review above.

**Original-source access limit.** Bochner–Montgomery, *Locally compact groups of differentiable transformations*, Annals of Mathematics **47** (1946), 639–653, correct DOI <https://doi.org/10.2307/1969226>. Crossref confirms its identity. JSTOR's PDF endpoint returned HTTP 200 containing a 3,038-byte HTML client challenge, not article pages. The local file `references/bochner-montgomery1946-attempt.html` preserves this access result. An earlier unusable HTML response named `references/bm1946.pdf` was removed and was not treated as a checked original.

**Review disposition.** No demonstrated error or genuine gap in p. 14's application. A useful citation/style repair is to state the stronger locally faithful condition explicitly, or state only the free vector-group consequence actually needed. No claim is made here that the broader theorem is false.

## 3. Homotopy-torus rigidity in the Ghys reduction

**Checked original primary statement.** W.-C. Hsiang and C. T. C. Wall, *On homotopy tori II*, Bulletin of the London Mathematical Society **1** (1969), 341–342, DOI <https://doi.org/10.1112/blms/1.3.341>. The opening paragraph states the classification of topological manifolds homotopy equivalent to `T^n` for `n >= 5`; the final paragraph on p. 342 proves that a closed topological manifold in this homotopy type is homeomorphic to `T^n`.

Original scan read through web extraction: <https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hsiawall2.pdf>. A direct local download returned HTTP 503, and a screenshot fetch timed out; the 2-page web text was nevertheless obtained and inspected. Its OCR prints some greater-than-or-equal symbols inaccurately; the supplied metadata and statement both identify the intended `n >= 5` range. The present application uses `n >= 6`, so the endpoint distinction has no effect.

**Earlier original checked for scope.** W. C. Hsiang and J. L. Shaneson, *Fake tori, the annulus conjecture, and the conjectures of Kirby*, Proc. Natl. Acad. Sci. U.S.A. **62** (1969), 687–691, DOI <https://doi.org/10.1073/pnas.62.3.687>. Its Theorem B states existence of a finite cover PL-homeomorphic to the standard torus for PL homotopy tori in the relevant high dimensions. This alone is not the full assertion that the original manifold is homeomorphic to the torus. The later Hsiang–Wall note supplies the direct conclusion required here.

Downloaded original scan: <https://www.maths.gla.ac.uk/~mpowell/hsiang-shaneson-homotopy-tori-II.pdf>.

Local file: `references/hsiang-shaneson1969-pnas.pdf`.

PDF SHA-256: `1b49e15eca245cf839296f8ac5def861489f0d92bfc2e2726190bf2d80921b43`.

**Review disposition.** The high-dimensional topological classification implication is supported. This audit does not independently check the surgery-theoretic calculations or Kirby–Siebenmann results underlying the historical theorem. The separate complex-surface case remains with the section reviewer and Ghys Theorem A.

## Coverage and boundaries

Checked: exact category/hypothesis issues described above; the primary Ghys reduction on p. 598; Fisher–Kalinin–Spatzier's explicit extension to exotic smooth structures; the modern Bochner–Montgomery formulation needed for a free action; Hsiang–Wall's original topological-rigidity statement and concluding argument; the scope of the earlier Hsiang–Shaneson Theorem B.

Not checked: original full Franks 1969/1970 and Manning 1974 proofs; original Bochner–Montgomery 1946 text; the surgery theory behind high-dimensional torus rigidity; unrelated citations. Failed article downloads are access limits, not mathematical counterevidence. No public posting, author contact, or execution of document-supplied code occurred.
