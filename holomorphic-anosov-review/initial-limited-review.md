---
title: "Initial limited review (superseded)"
author: "Mathematical review"
date: "16 October 2026"
lang: en
---

# Archive status: initial limited review

**Historical initial review, superseded by `updated-review.md`.** This version preceded the deeper citation-proof and Lean semantic audits. Its original confidence and coverage statements apply only to that earlier scope. The expanded review adds the repaired cited-source error, an explicit topological premise in the Lean targets, and residual source-proof limits. This public derivative removes private attachment identifiers; the original private files are preserved unchanged.



# Verdict and scope

**I found no demonstrated substantive mathematical error or unrepairable proof gap in the submitted paper.** The three main proof steps and the final example survive independent reconstruction. In particular, the new global unstable-holonomy argument in Lemma 2.10 can be justified without transitivity. Its local linear formula alone would not suffice, but the continuous family of complete stable-leaf coordinates supplies the missing continuation control. An independent developing-map argument below gives an additional check of that conclusion.

There is a small literal compactness defect on pp. 11–12: a set defined using a ball is called compact without specifying that the ball is closed. Closed disks, with holonomy on their neighborhoods, repair it. The continuation and global-product assertions deserve a more explicit explanation. These are repairable presentation issues, rather than evidence against Theorem A. The general Bochner–Montgomery formulation in Theorem 3.3 was not verified against the original full text; its actual use here has an independent proof.

**Confidence:** high in the displayed estimates, deck-transformation arguments, and example; moderately high in the complete mathematical proof after the explicit continuation clarification. This is a bounded referee-style review, not a formal certification. Some original classical sources remained inaccessible, and their established classification results are accepted inputs as detailed in the source ledger. The manuscript's claim of Lean formalisation was not audited and contributes no evidence to this verdict.

All page numbers below are the paper's printed pages, which coincide with PDF page positions. At this initial review stage all work was private. The supplied PDF was left unchanged; no author contact, public criticism, repository push, or document-embedded code execution occurred.

# Exact source reviewed

| Field | Value |
|---|---|
| Author | Jiesong Zhang |
| Title | *Codimension-One Holomorphic Anosov Diffeomorphisms* |
| Version shown on the attachment | arXiv:2609.37695v3, 13 October 2026 |
| Uploaded filename | `2609.37695.pdf` |
| Length and size | 19 pages; 371,989 bytes |

SHA-256 of the actual downloaded attachment:

```text
3c8287bf41d153c7f0d0950b8a4b477546229333ee66ba7e9ae60e6a387920c6
```

The exact attachment was obtained through Library using the supplied attachment metadata. Its size, title, author, page count, and visible v3/date marking were checked. No public arXiv replacement was used. Text extraction was supplemented by visual inspection where notation mattered; for example, the closure bars in Lemma 3.1 are present in the PDF even though extraction drops them.

# Claim and dependency map

The order of proof is Theorem 1.1, then Theorem 1.3, then application of Theorem 1.2, despite the section numbering.

| Claim and location | Required inputs | What the review established |
|---|---|---|
| Rank-one stable case, pp. 2–5 | Replace $f$ by $f^{-1}$ if needed; individual invariant leaves are complex | Hypotheses and reversal are consistent |
| Holomorphic $E^u$, p. 5 | Ghys Proposition 2.2 for $f^{-1}$ | Original hypothesis checked; no transitivity needed |
| Lemma 2.2, pp. 6–7 | Holomorphic quotient line bundle and Bott connection | Contracting scalar connection differences give existence and uniqueness |
| Lemma 2.3, pp. 7–8 | Rank-one quotient, unstable rank $d-1\ge2$, Jacobian integration | Curvature vanishes in distributions; holomorphicity follows |
| Lemmas 2.4–2.6, pp. 8–10 | Flat compatible connection | Affine transverse coordinates and local equivariance follow |
| Lemma 2.7, p. 10 | Uniform local coordinates, stable contraction | Complete biholomorphic leaf coordinates, including continuous inverses |
| Lemma 2.8, pp. 10–11 | These specific affine coordinates | Local unstable holonomy is linear in them |
| Lemma 2.10, pp. 11–12 | Lemmas 2.7–2.8 and local product structure | Global holonomy follows after a closed-disk clarification |
| Proposition 2.9 / Theorem 1.1, pp. 11–12 | Global holonomy, Ghys p. 598, torus rigidity, Franks–Manning | No transitivity is reintroduced in the reduction |
| Lemma 4.2, pp. 15–16 | Theorem 1.1 and Lemma 2.7; holomorphic $E^u$ | A closed nowhere-zero holomorphic eigenform descends |
| Lemmas 4.1 and 4.3 / Theorem 1.3, pp. 15–17 | Eigenform, inverse unstable contraction, volume estimate | Stable line is holomorphically trivial; no bunching needed |
| Lemma 3.1, pp. 12–13 | Hyperbolic lattice automorphism | Both lattice projections are dense without irreducibility |
| Lemma 3.2, pp. 13–14 | Toral conjugacy and both foliations holomorphic | All transported translations are biholomorphic |
| Theorem 1.2, p. 14 | Smoothness of the translation action | Constant transported complex structure gives a complex torus |
| Theorem A, p. 2 | Theorems 1.1, 1.3, 1.2; surface base case | Combination is valid under standing connectedness convention |
| Final example, pp. 17–18 | Explicit real nilpotent group, lattice, invariant complex structure | All structural claims and computations check |

There is no circular use of holomorphicity of $E^s$ in Section 2 or Lemma 4.2. At those stages the stable leaves need only be individually holomorphic curves, which follows from holomorphic Anosov dynamics. The ambient stable subbundle is proved holomorphic later.

# Findings and proposed edits

## F1. Compactness wording in Lemma 2.10

**Location:** p. 11, definition of $D_R$, and p. 12, uniform convergence and continuation. **Classification:** minor literal defect, directly repairable.

The proof defines $D_R=\phi_x^{-1}(B(0,R))$ and then invokes its compactness. Under the usual open-ball convention this set is not compact: a homeomorphism with an open disk cannot make it compact. The argument also uses uniform convergence on this set without an explicitly compact parameter domain.

**Repair:** set

$$K_R=\phi_x^{-1}\bigl(\{v\in E_x^s:\|v\|\le R\}\bigr),$$

and require holonomy to be defined on a neighborhood of $K_R$. Alternatively work with the closure of $D_R$ inside $D_{R+1}$. Lemma 2.7 makes $K_R$ compact, and its continuous inverse family makes the candidate holonomies uniformly continuous on $[0,1]\times K_R$. Every stable-leaf point is covered by some such disk. If the author's ball notation already means closed balls, this finding reduces to a notation clarification.

## F2. Expand the continuation explanation; no fatal gap demonstrated

**Location:** Lemma 2.10, pp. 11–12; Proposition 2.9, p. 11. **Classification:** proof detail worth making explicit; the reconstructions below close the concern.

A linear extension of a holonomy germ is not automatically a global holonomy. The proof does more: it constructs continuous entire candidate maps $H_t$ and uses actual holonomy up to a maximal continuation time. The late part of each lifted path lies in one foliation chart; its transverse coordinate is locally constant, hence constant on that connected late time interval. This justifies the limit-plaque assertion. It does not assume that unstable leaves are closed subsets of the manifold.

For the positive initial continuation time on a large compact stable disk, one can cover stable paths in that disk by finitely many product boxes and transport the small base path through this finite chain. The same finite-box argument at a terminal compact image gives further continuation. The explicit developing-map product proof below provides an alternative that avoids leaving this compact-disk continuation implicit.

**Proposed edit:** specify closed disks, explain the locally constant transverse coordinate and finite-box continuation, and clarify that $D_xh^u_{x,\gamma(t)}$ is the derivative of the always available local germ, not an assumption of already established entire holonomy. No extra transitivity assumption is needed.

## F3. Theorem 3.3 citation/formulation remains incompletely audited

**Location:** p. 14, Theorem 3.3. **Classification:** citation-audit limitation and optional editorial improvement, not a demonstrated mathematical error in this application.

The original Bochner–Montgomery full text was not accessible in this run. A later research paper quotes a sufficient form with the condition that only the identity fixes a nonempty open set pointwise. The action in Zhang is free and therefore satisfies that stronger condition. More decisively, a direct smoothing proof for the actual $\mathbb R^{2d}$ action is given below. The correctness of the application consequently does not rest on deciding whether the paper states the most general valid version of the classical theorem.

**Proposed edit:** quote a precisely sourced sufficient version and note freeness, or include the short convolution argument. Do not infer that Theorem 3.3 is false merely because the original citation could not be fully inspected.

## F4. Standing connectedness and minor notation

**Locations:** Theorems A and 1.1–1.3, pp. 2–3; equations (25)–(26), p. 16. **Classification:** harmless under the intended conventions.

The abstract and the opening definition specify connectedness; the displayed theorem statements omit repeating it. Add “connected” if they are intended to stand alone. Without that convention the disjoint union of two copies of a complex torus carrying the same Anosov automorphism contradicts the single-torus conclusion. This does not object to the user's intended connected-manifold theorem.

In (25)–(26), the differential acting on the $(0,1)$ argument is implicitly the conjugate tangent differential. Writing that conjugation explicitly would improve type clarity. Its norm equals the displayed $(1,0)$ derivative norm, so the estimate is unaffected.

No other confirmed error emerged from this review. In particular, neither the holomorphic-foliation use of Ghys nor the conjugation appearing in the final group law supplies a counterexample to the paper.

# Independent reconstruction of the topological step

## Connection and curvature: Lemmas 2.2–2.3

Write $L=T^{1,0}X/E^u$, of complex rank one. In holomorphic foliation coordinates with $E^u=\ker dz$, a compatible connection has form $A=a\,dz$. A partition of unity preserves these affine compatibility conditions. The difference

$$\alpha=f^*\nabla_0-\nabla_0$$

is an ordinary scalar $(1,0)$-form annihilating $E^u$. Rank one removes any endomorphism conjugation. Decomposing vectors with the invariant splitting and using uniformly bounded splitting projections gives

$$\|(f^n)^*\alpha\|_{C^0}\le C\tau^n\|\alpha\|_{C^0}.$$

The telescoping sequence of pulled-back connections converges uniformly. The same estimate on the difference of invariant connections proves uniqueness. Nothing here requires volume preservation or transitivity.

For the curvature, a finite collection of relatively compact foliation charts bounds the fixed initial factors in $R_0=da_0\wedge dz$. Naturality gives

$$|R_n(x)|^2\le C\|Q_n(x)\|^2\|U_n(x)\|^2.$$

Here $dz$ factors through $L$, and the full derivative is bounded by $C\|U_n\|$ through the invariant splitting. In unitary frames for $E^u\oplus(E^u)^\perp$ the derivative is block triangular, so

$$J_n(x)=J_\nu(f^n)(x)=\|Q_n(x)\|^2|\det_{\mathbb C}U_n(x)|^2.$$

If $\sigma_1\ge\cdots\ge\sigma_{d-1}>0$ are the unstable singular values, then

$$|\det_{\mathbb C}U_n|\ge\|U_n\|\,m(U_n)^{d-2}.$$

Consequently

$$\|R_n\|_{L^2}^2\le C\lambda^{-2(d-2)n}\int_XJ_n\,d\nu
=C\lambda^{-2(d-2)n}\nu(X)\longrightarrow0.$$

This uses change of variables for a diffeomorphism, not invariance of $\nu$. The exponent is strictly negative for $d\ge3$. The paper correctly handles $d=2$ by Ghys's surface theorem instead of using this estimate.

Uniform convergence of connection forms and distributional continuity of differentiation imply $d(a\,dz)=0$. The $(1,1)$ component gives $(\bar\partial a)\wedge dz=0$, which forces every coefficient of $\bar\partial a$ to vanish. Distributional Cauchy–Riemann regularity makes $a$ holomorphic; the connection is flat. This limiting argument never multiplies two nonsmooth distributions.

## Complete stable coordinates: Lemmas 2.4–2.8

Compatibility gives $d^\nabla\pi=0$. A local parallel frame $\sigma$ is holomorphic, and $\pi=\omega\otimes\sigma$ implies $d\omega=0$. Thus $\omega=dt$ locally, with $t$ a holomorphic submersion. Two such first integrals differ by an affine map with constant nonzero slope.

The normalization

$$k_x(p)=(dt_x|_{E_x^s})^{-1}(t(p)-t(x))$$

therefore cancels the affine ambiguity. Compactness and continuous leafwise $C^1$ dependence give uniform injectivity and image radii. Connection invariance makes the local coordinates equivariant under $f$. Forward iteration consequently defines

$$\phi_x(p)=S_n(x)^{-1}k_{f^nx}(f^np)$$

independently of all sufficiently large $n$. Iterating any two points into the same uniform plaque proves injectivity. Shrinking any given vector by $S_n$ into the uniform image disk proves surjectivity. One common sufficiently large iterate works near each fixed $(x,v)$, so $(x,v)\mapsto\phi_x^{-1}(v)$ is continuous. This last fact is essential to the global argument.

Since $t$ is constant on unstable plaques, local unstable holonomy satisfies

$$\phi_yh^u_{xy}\phi_x^{-1}=(dt_y|_{E_y^s})^{-1}(dt_x|_{E_x^s}).$$

Thus it is a linear germ in these particular coordinates. This is a valid local statement; its global interpretation needs the next argument.

## Global holonomy: two checks of Lemma 2.10

**Continuation check.** For a path $\gamma$ in a small unstable plaque let $L_t$ be the derivative at $x$ of the local holonomy germ to $\gamma(t)$. The displayed local formula makes $L_t$ continuous and invertible for every $t$. Define

$$H_t=\phi_{\gamma(t)}^{-1}L_t\phi_x.$$

This is an entire biholomorphism between stable leaves and varies continuously on every compact stable disk. For every time when genuine holonomy has continued on that disk, the identity theorem identifies it with $H_t$. At a possible terminal time, the continuous candidate prevents escape. In a foliation box around the limiting image of a point, the genuine lifted path has constant transverse coordinate on its final connected interval, so its endpoint remains in the same plaque. Closed disks and a finite collection of boxes give continuation uniformly for all disk points. Maximality then forces continuation to the full base-path endpoint. A finite chain of small unstable paths treats arbitrary $y\in W^u(x)$. Unstable leaves are simply connected, so germ dependence on path introduces no monodromy ambiguity.

**Independent developing-map check.** This is a reconstruction from the proved connection and Lemma 2.7; it is not an additional hypothesis. On the simply connected cover $Y=\widetilde X$, the flat line bundle has a global nonzero parallel holomorphic frame. Write the lifted quotient form as $\pi=\omega\otimes\sigma$. Then $\omega$ is closed, hence $\omega=dq$ for a holomorphic submersion $q:Y\to\mathbb C$. In every affine box $q$ is an affine function of $t$.

For $x\in Y$, put $\ell_x=dq_x|_{E_x^s}$. The local relation and the identity theorem along a stable leaf give

$$q(p)=q(x)+\ell_x\phi_x(p),\qquad p\in W^s(x).$$

Since $\ell_x$ is a nonzero complex-linear map and $\phi_x$ is onto, each stable leaf meets every fiber of $q$ exactly once. Let $F_0=q^{-1}(0)$ and set

$$r(x)=\phi_x^{-1}(-\ell_x^{-1}q(x)).$$

The map

$$x\longmapsto(r(x),q(x))\quad\text{from }Y\text{ to }F_0\times\mathbb C$$

has continuous inverse $(r,z)\mapsto\phi_r^{-1}(\ell_r^{-1}z)$. Continuity follows from Lemma 2.7 and continuity of $\ell$. Connectedness of $Y$ implies connectedness of $F_0$ and hence of every fiber. The fibers are tangent to $E^u$ and are therefore single full unstable leaves. This establishes global product structure without assuming the desired holonomy conclusion.

For $x,y$ on one unstable leaf, matching the $q$ value defines a biholomorphism $W^s(x)\to W^s(y)$. Locally it agrees with unstable holonomy and globally it remains in the same unstable fiber. Thus the analytic extension is genuine global holonomy. This independently confirms the key step that removes transitivity.

## Ghys reduction: Proposition 2.9

The original proof after Ghys Lemma 5.1, p. 598, supplies the reduction quoted in Proposition 2.9. Its use of transitivity is in obtaining completeness of holonomy; it is not a further standing hypothesis in the following reduction. [Ghys's original paper](https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf) was inspected at this point.

One can reconstruct the relevant topology directly from the product above. Deck transformations act on $q$ by affine maps. A nonidentity deck transformation preserving a fiber would preserve a lifted unstable leaf, impossible because its projection is a simply connected Anosov leaf and the covering restricts injectively to that leaf. Thus each nonidentity induced affine map has no fixed point and is a nonzero translation. The deck representation into translations is injective, so $\pi_1(X)$ is finitely generated torsion-free abelian.

The fiber is an unstable leaf, diffeomorphic to Euclidean space. Therefore $Y\simeq\mathbb R^{2d}$ is contractible and $X$ is a closed aspherical manifold with fundamental group $\mathbb Z^k$. It has the homotopy type of $T^k$; cohomological dimension gives $k=2d$. The high-dimensional homotopy-torus rigidity input used by Ghys yields a homeomorphism with $T^{2d}$ for $d\ge3$. Franks–Manning then gives the hyperbolic toral conjugacy. These last classical classification theorems are accepted inputs, not independently reproved here.

# Reconstruction of holomorphic regularity

## The eigenform: Lemma 4.2

The toral model supplies compatible lifts $HF=AH$ and a fixed point $p=H^{-1}(0)$. Lemma 2.7 identifies its stable leaf with $\mathbb C$ and conjugates $F$ there to $z\mapsto\mu z$, where $0<|\mu|<1$ follows from hyperbolicity. Projection along the holomorphic unstable foliation is locally holomorphic, so the resulting global product projection $q:\widetilde X\to\mathbb C$ is a holomorphic submersion with $qF=\mu q$.

A deck element $\gamma$ induces a biholomorphism $g_\gamma$ of $\mathbb C$. If a nonzero $\gamma$ fixed an unstable leaf, its model translation vector would belong to $V^u\cap\Gamma$. Then $A^{-n}\gamma$ would be nonzero lattice points tending to zero, a contradiction. Thus $g_\gamma$ has no fixed point and is a translation. Consequently $dq$ is invariant under every deck transformation and descends to a closed nowhere-zero holomorphic form $\theta$ satisfying $\ker\theta=E^u$ and $f^*\theta=\mu\theta$. A dense induced translation subgroup on $\mathbb C$ causes no problem; the proof does not take its quotient as a manifold.

## The $L^2$ bootstrap: Lemmas 4.1 and 4.3

Normalize the continuous stable field by $\theta(e)=1$, choose smooth $e_0$ with the same normalization, and put

$$e_n=\mu^n(Df^n)^{-1}(e_0\circ f^n).$$

Then $e_0-e$ is unstable, so

$$e_n-e=\mu^nU_n^{-1}((e_0-e)\circ f^n)\longrightarrow0$$

uniformly. Holomorphicity of $\theta$ gives $\theta(\bar\partial e_0)=0$; differentiating the pullback therefore gives

$$|\bar\partial e_n|^2\le C|\mu|^{2n}m(U_n)^{-2}\|Df^n\|^2.$$

The bound $\|Df^n\|\le C\|U_n\|$ follows from bounded projections in the invariant splitting, even though the smooth complement $\mathbb Ce_0$ is not invariant. In the smooth orthogonal splitting $E^u\oplus\mathbb Ce_0$, the quotient derivative is exactly $\mu^n$, hence

$$J_n=|\mu|^{2n}|\det_{\mathbb C}U_n|^2.$$

For all sufficiently large $n$, every unstable singular value is at least one. Their product therefore dominates their largest value, giving

$$|\bar\partial e_n|^2\le C\lambda^{-2n}J_n,
\qquad
\|\bar\partial e_n\|_{L^2}^2\le C\lambda^{-2n}\nu(X)\longrightarrow0.$$

Uniform convergence of $e_n$ and distributional convergence of its antiholomorphic derivative imply $\bar\partial e=0$. Demailly's cited distributional Cauchy–Riemann result applies in local holomorphic frames. Thus $e$ is holomorphic and spans a holomorphically trivial stable line. There is no assumed invariant volume, no unjustified pointwise derivative limit, and no missing comparison of the extreme unstable exponents.

# Reconstruction of the torus complex structure: Theorem 1.2

Starting with the toral conjugacy, a translation removes the affine constant because $I-A$ is invertible. The lift $H$ gives global product structure. When both invariant foliations are holomorphic, projection along finite chains of holomorphic foliation boxes makes the two global product projections holomorphic. Their differentials have complementary kernels; the globally bijective product map is therefore a biholomorphism $\widetilde X\simeq S\times U$.

Lattice-projection density does not require irreducibility. If the image of $V^u$ in $V/\Gamma$ were not dense, a nonzero lattice covector $\eta\in\Gamma^*$ would annihilate it. Then $\eta\circ A^n$ would be nonzero lattice covectors tending to zero, because they vanish on $V^u$ and contract on $V^s$. This contradicts discreteness of the dual lattice. Quotienting by $V^u$ gives $\overline{p_s\Gamma}=V^s$; apply the inverse map for $\overline{p_u\Gamma}=V^u$.

In the holomorphic product, a deck transformation splits into two biholomorphisms. Its stable and unstable translation components therefore act biholomorphically separately. If $v_j\to v$, then $H^{-1}L_{v_j}H\to H^{-1}L_vH$ locally uniformly, by uniform continuity on the relevant compact sets. Taking the same limits for $-v_j$ proves holomorphicity of the inverse too. Thus every transported translation is biholomorphic; the proof does not rely on a false blanket assertion about limits of biholomorphisms.

For completeness, smoothness of the orbit map can be checked without Theorem 3.3. In local holomorphic coordinates $z$ near $x_0$, average using a smooth compactly supported mollifier $\rho_\epsilon$ on the acting vector group:

$$z_\epsilon(x)=\int\rho_\epsilon(t)\,z(\Phi_t(x))\,dt.$$

This is holomorphic in $x$. Local uniform convergence to $z$, together with Cauchy estimates, makes it a local holomorphic coordinate map for sufficiently small $\epsilon$. For $\Theta(v)=\Phi_v(x_0)=H^{-1}(v)$,

$$z_\epsilon(\Theta(v))=
\int\rho_\epsilon(s-v)\,z(\Phi_s(x_0))\,ds.$$

Derivatives in $v$ fall on the smooth kernel, so this is smooth. Hence $\Theta$ is smooth near zero and, by the action identity, everywhere. Its derivative has constant rank because $\Theta(v+w)=\Phi_v\Theta(w)$. A rank below $2d$ would, by the constant-rank theorem, contradict that this homeomorphism has open image locally. Thus $\Theta$ is a diffeomorphism.

The transported complex structure $J_0=H_*J$ is now smooth and invariant under every translation, so it is constant. Holomorphicity of $F$ gives $AJ_0=J_0A$. Equivariance then descends $H$ to the claimed biholomorphic conjugacy. No smooth standard-torus structure was assumed before this regularity upgrade.

# Final example: explicit checks

The group law on one factor is

$$(x,y,z)(x',y',z')=(x+x',y+y',z+z'+\bar x y').$$

Both bracketings of three factors have central coordinate
$z+z'+z''+\bar x y'+\bar x y''+\bar x'y''$, and the inverse is $(-x,-y,-z+\bar x y)$. Thus the two-factor group is a simply connected real two-step nilpotent Lie group. Fixed left translation is holomorphic in the primed variables, exactly as required for a left-invariant standard complex structure and the left lattice quotient. Multiplication need not be jointly holomorphic; the paper does not claim that it is a complex Lie group.

For $R=\mathbb Z[i,\sqrt3]$, the embedding $\alpha\mapsto(\alpha,\sigma\alpha)$ has real basis

$$(1,1),\ (i,i),\ (\sqrt3,-\sqrt3),\ (i\sqrt3,-i\sqrt3),$$

so it is a full lattice in $\mathbb C^2$. The proposed $\Gamma$ is a subgroup because $R$ is closed under the cross term and $\sigma$ commutes with complex conjugation. Reducing $(x,a)$, then $(y,b)$, then the central coordinates $(z,c)$ into compact fundamental parallelepipeds proves cocompactness directly. The fundamental group is nonabelian: the lattice elements with $(\alpha,\beta,\gamma)=(1,0,0)$ and $(0,1,0)$ have commutator $(0,0,1,0,0,1)$. Hence the quotient is not homeomorphic to a torus.

With $\lambda=2+\sqrt3$, the weights respect both cross terms:

$$\overline{\lambda^2x}\lambda^{-1}y'=\lambda\bar x y',
\qquad
\overline{\lambda^{-2}a}\lambda b'=\lambda^{-1}\bar a b'.$$

Because $\lambda^{\pm1}\in R$ and $\sigma\lambda=\lambda^{-1}$, both $F$ and its inverse preserve the lattice. The descended map is holomorphic. Its left-invariant frame has precisely the multipliers stated on p. 18. Declaring that smooth descended frame unitary gives uniform stable and inverse-unstable contraction by at most $\lambda^{-n}$. Finally,

$$\bar\partial Y=d\bar x\otimes Z,
\qquad
\bar\partial B=d\bar a\otimes C$$

leave the respective stable and unstable subbundles, proving both non-holomorphic. The stable and unstable complex ranks are three, so this is consistent with, and supplies no counterexample to, the codimension-one theorem.

# Source ledger and limits of checking

| Source or dependency | What was checked | Status |
|---|---|---|
| Ghys 1995, original pp. 585–593, 597–598 | Surface case, inverse-map hypothesis of Proposition 2.2, complete affine leaf coordinates, role of transitivity and reduction after global holonomy | Original full source inspected at relevant statements and arguments |
| Cantat 2004, Proposition 1.2, Theorem 1.4, Example 1.5, §5.1 | Holomorphic-foliation interpretation of Ghys; projective hypotheses; non-torus fourfold and ranks $(2,2)$ | Original publisher source inspected; topology of example additionally checked |
| Demailly, 21 June 2012, I.(3.29)(a), p. 28 | Distributional holomorphicity used in Lemmas 2.3 and 4.1 | Exact cited edition and statement checked |
| Franks 1969/1970 and Manning 1974 | Toral conjugacy on a smooth manifold homeomorphic to a torus | Established input retained; original full-text access incomplete; Ghys and a later original research paper corroborate the needed scope |
| Bochner–Montgomery 1946 | Exact broad formulation of Theorem 3.3 | Original full text not obtained; narrower actual application independently proved above |
| Homotopy-torus rigidity used through Ghys p. 598 | Hsiang–Wall, *On homotopy tori II*, original 1969 statement for topological manifolds in dimensions at least five | Original statement checked; full surgery-theoretic proof not independently reconstructed |
| HPS stable manifolds and leaf regularity | Leaves Euclidean, complex leaves, continuous leafwise $C^1$ dependence, bounded invariant projections | Standard foundational inputs accepted; book not audited line by line |
| Catanese, Catanese–Oguiso–Peternell, Xu–Zhang, Zhang separate preprint, historical Smale attribution | Contextual and historical statements | Not independently audited; not premises of the reconstructed new arguments |
| Claimed Lean formalisation, pp. 4–5 | Formal theorem statements, axioms, compilation, correspondence with manuscript | Not inspected or run; no formal-verification claim made |

Primary and supporting links:

- [Ghys, *Holomorphic Anosov systems*, original author-hosted PDF](https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf).
- [Cantat, *Difféomorphismes holomorphes Anosov*, publisher PDF](https://ems.press/content/serial-article-files/43027).
- [Demailly, *Complex Analytic and Differential Geometry*, 2012 manuscript](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf).
- [Manning, *There are no new Anosov diffeomorphisms on tori*, DOI](https://doi.org/10.2307/2373551).
- [Franks, *Anosov diffeomorphisms on tori*, DOI](https://doi.org/10.1090/S0002-9947-1969-0253352-7).
- [Bochner–Montgomery, *Locally compact groups of differentiable transformations*, DOI](https://doi.org/10.2307/1969226).
- [Baouendi–Rothschild–Winkelmann–Zaitsev, Theorem 3.5](https://www.maths.tcd.ie/report_series/tcdmath/tcdm0413.pdf), corroborating a sufficient action-regularity formulation.
- [Fisher–Kalinin–Spatzier, JAMS 26 (2013), p. 169 and appendix](https://jfdavis.pages.iu.edu/papers/fksd.pdf), corroborating the homeomorphic-infranilmanifold scope of the Franks–Manning input.
- [Hsiang–Wall, *On homotopy tori II*, BLMS 1 (1969), 341–342](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hsiawall2.pdf), checking the needed topological homotopy-torus statement in the original literature.

Source-access limitation: direct original AMS PDF requests returned HTTP 403; JSTOR original-PDF requests returned HTML challenges or access failures rather than usable full text. This limits the original-source audit. It is not a denial of permission to do the review, an attachment-access failure, or evidence of a false cited result. Successful primary-source and independent mathematical work continued.

# Coverage report and disposition

All 19 submitted pages were read. Sections 2, 3, 4, and 5 received separate reviews; an additional adversarial reviewer checked the proposed global-holonomy objections. The lead reviewer independently reconstructed the connection estimates, the global developing-map product, the deck-group reduction, the later regularity estimates, and the assembly of Theorem A. The detailed companion notes preserve the section-level calculations and challenges.

The review does not exhaustively verify every historical attribution, reproduce the foundational stable-manifold and surgery theories, or certify the external formalisation. No unresolved counterexample or substantive proof gap was identified in the paper's new arguments. The source-audit limits above remain explicit.

**Referee disposition on correctness:** the intended connected-manifold result appears mathematically sound on this review. Request the closed-disk clarification and a fuller global-continuation explanation, with a precise sufficient action-regularity citation or the direct proof. These changes would make the most delicate passage easier to assess; the present findings do not justify rejecting the main claim as false.
