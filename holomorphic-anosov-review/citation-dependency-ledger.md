# Citation and dependency audit ledger

Review date: 16 October 2026. Original-statement inspection, proof inspection/reconstruction, and bounded errata searching are separate evidence categories. “Unverified” describes the audit boundary, not a disproof. CL-02 is a hypothetical attribution clarification; Zhang cites Franks **and** Manning, so that row is not an error alleged against the paper.

See `notes/ghys-proof-audit.md`, `notes/classification-proof-audit.md`, `notes/regularity-proof-audit.md`, and `notes/hps-foundations.md` for proofs, exact locations and access limits. The separate machine-readable CSV/JSON has the same rows.

## Ghy95-P2.2

Zhang p5; p15; Ghys pp589-590

**Claim:** holomorphic complementary bundle for one-dimensional complex opposite direction

**Status:** proof-read-and-reconstructed

**Original statement:** Checked in original

**Proof coverage:** Asymptotically conformal holonomy; arbitrary holomorphic transversals; Hartogs graph argument

**Errata search:** Bounded queries recorded; no relevant correction located

**Unverified inputs:** Stable manifold and inclination/projection machinery; quasiconformal compactness; Hartogs

**Finding and limit:** No hidden transitivity; no demonstrated defect. Foundational dependency proofs not all reopened

[Primary source or scope evidence](https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf)

## Ghy95-P3.1

Zhang p10; Ghys pp590-593

**Claim:** invariant complete affine structures on one-dimensional leaves

**Status:** proof-read-and-reconstructed

**Original statement:** Checked in original

**Proof coverage:** Homogeneous jet splittings; inverse contraction; local holomorphic limits; injectivity and surjectivity by iteration

**Errata search:** Bounded queries recorded; no relevant correction located

**Unverified inputs:** Stable-manifold regularity; local holomorphic ODE; Banach fixed point

**Finding and limit:** No demonstrated defect; Zhang independently constructs needed coordinates. Full foundational jet/ODE theory accepted

[Primary source or scope evidence](https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf)

## Ghy95-P4.1

Zhang Prop2.9 background and cited surface basecase; Ghys pp593-597,598-600

**Claim:** projective holonomy and developing structure

**Status:** proof-partly-reconstructed-specific-step-unresolved

**Original statement:** Checked in original

**Proof coverage:** Schwarzian cocycle; diameter density; invariant-measure calculation; repaired no-triple consequence

**Errata search:** Bounded queries recorded; no relevant correction located

**Unverified inputs:** Markov partitions and boundaries; covering dimension; specific acim-to-transitivity inference unresolved

**Finding and limit:** False unnecessary disk-containment strengthening in Fact1; needed weaker consequence repaired. Zhang d>=3 affine proof bypasses this proposition; d=2 basecase via Ghys TheoremA retains this unresolved source-proof audit step

[Primary source or scope evidence](https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf)

## Ghy95-Fact1

Ghys p596

**Claim:** diameter equality implies no triple overlap

**Status:** counterexample-to-strengthening-and-repair

**Original statement:** Checked in original

**Proof coverage:** Three compact sets with middle equilateral triangle; intersection-graph proof of needed consequence

**Errata search:** Bounded queries recorded; no relevant correction located

**Unverified inputs:** Elementary metric geometry only

**Finding and limit:** Containing collinear disjoint disks claim false; no-triple consequence true. No counterexample to theorem; no formal prover used

[Primary source or scope evidence](https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf)

## Ghy95-L5.1

Zhang pp11-12; Ghys pp597-598

**Claim:** complete global holonomy under transitivity

**Status:** proof-read-role-checked-replaced-in-Zhang

**Original statement:** Checked in original

**Proof coverage:** Identified full-support transverse measure and disk-compactness role

**Errata search:** Bounded queries recorded; no relevant correction located

**Unverified inputs:** Plante transverse-measure input and disk compactness not independently audited

**Finding and limit:** Transitivity used here; Zhang supplies separate continuous-linearization continuation. Do not label original lemma proof foundationally verified

[Primary source or scope evidence](https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf)

## Ghy95-TheoremB-post-L5.1

Zhang Prop2.9 p11; Ghys p598

**Claim:** topological torus and toral conjugacy after complete holonomy

**Status:** essential-reduction-reconstructed

**Original statement:** Checked in original

**Proof coverage:** Global developing coordinate; Y x C product; no fixed-point deck holonomy; Z^(2d) aspherical fundamental group

**Errata search:** Bounded queries recorded; no relevant correction located

**Unverified inputs:** Anosov leaves intrinsically Euclidean; homotopy-torus rigidity; Franks-Manning

**Finding and limit:** No extra transitivity after completeness; direct affine reconstruction bypasses P4.1. Final topological rigidity and conjugacy sources handled by other source audits

[Primary source or scope evidence](https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf)

## Ghy95-TheoremA

Zhang Theorems1.1/1.3 d=2 basecases; Ghys pp598-600

**Claim:** surface holomorphic torus classification

**Status:** dependency-path-inspected-not-complete-proof-audit

**Original statement:** Checked in original

**Proof coverage:** Original proof invokes P4.1 for both stable and unstable foliations and uses two-sided projective developing map

**Errata search:** Bounded queries recorded; no relevant correction located

**Unverified inputs:** P4.1 original acim-to-transitivity inference unresolved in this audit; stable leaves simply connected

**Finding and limit:** No demonstrated theorem error; source-proof coverage remains limited. Do not apply d>=3 affine bypass to claim surface source proof fully checked

[Primary source or scope evidence](https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf)

## CL-01

Zhang p.12, Section3 (Theorem1.2)

**Claim:** Anosov diffeomorphism on a smooth manifold homeomorphic to a torus is topologically conjugate to a hyperbolic affine toral automorphism

**Status:** PARTIALLY_VERIFIED

**Original statement:** Franks1969 conditional proof

**Proof coverage:** Homological hyperbolicity under finite Markov coding; Proper semiconjugacy by convergent series; Unique fixed points of lifts by degree and index; Conditional argument tolerates exotic smooth structure

**Errata search:** Bounded queries recorded; no invalidating correction located

**Unverified inputs:** Manning1974 regional recurrence/full nonwandering set; Franks1970 original proof; Foundational finite Markov coding theorem not reproved

**Finding and limit:** No demonstrated defect; do not count classical proof as fully checked. See unverified inputs and detailed note

[Primary source or scope evidence](https://jfdavis.pages.iu.edu/papers/fksd.pdf)

## CL-02

Zhang p.12 Franks–Manning invocation

**Claim:** Franks1969 alone removes all nonwandering-set and homological hypotheses

**Status:** FALSE_IF_ATTRIBUTED_TO_FRANKS1969_ALONE

**Original statement:** Franks1969 pp.117–124

**Proof coverage:** See disposition and detailed source note

**Errata search:** Bounded queries recorded; no invalidating correction located

**Unverified inputs:** None beyond the elementary argument stated

**Finding and limit:** Zhang cites Franks together with Manning, so this is a dependency clarification, not an error in Zhang. See unverified inputs and detailed note

[Primary source or scope evidence](https://scispace.com/pdf/anosov-diffeomorphisms-on-tori-gkxjeli14m.pdf)

## CL-03

Zhang p.12 hyperbolic linear model

**Claim:** The homology action has no eigenvalue on the unit circle

**Status:** INDEPENDENTLY_RECONSTRUCTED_CONDITIONAL_ON_MARKOV_CODING

**Original statement:** Franks1969 excludes roots of unity

**Proof coverage:** Periodic-count exponential comparability; Lefschetz determinant identity; Compact-group simultaneous recurrence contradiction

**Errata search:** Bounded queries recorded; no invalidating correction located

**Unverified inputs:** Finite Markov coding existence and uniform fiber multiplicity accepted as standard input; Original Manning1974 proof unavailable

**Finding and limit:** Supports this particular implication; does not prove full classification. See unverified inputs and detailed note

[Primary source or scope evidence](https://wrap.warwick.ac.uk/id/eprint/71348/1/WRAP_Thesis_Manning_1972.pdf)

## CL-04

Zhang p.12; topological stage invoking Ghys

**Claim:** The required full-nonwandering-set/regional-recurrence step is valid by original Manning1974 proof

**Status:** UNVERIFIED

**Original statement:** Original unavailable; scope corroborated in later primary research

**Proof coverage:** See disposition and detailed source note

**Errata search:** Bounded queries recorded; no invalidating correction located

**Unverified inputs:** Manning1974 original unavailable; Independent recurrence proof not completed

**Finding and limit:** Original-proof access limit; no counterexample or error inferred. HTML/client challenge, not article pages; SciSpace has no accessible PDF link

[Primary source or scope evidence](https://www.jstor.org/stable/pdf/2373551.pdf)

## CL-05

Ghys reduction used for Zhang Theorem1.1, realdimension>=6

**Claim:** Closed smooth manifold homotopy equivalent to T^n, n>=5, is homeomorphic to T^n

**Status:** ORIGINAL_PROOF_SOURCE_CHECKED_WITH_DEEP_INPUTS_UNVERIFIED

**Original statement:** Hsiang–Wall1969 both pages; Hsiang–Shaneson1969 PNAS proof outline

**Proof coverage:** Smooth implies available PL structure; Marked/unmarked distinction; Dimension threshold; Mod2 cover pullback zero and integral pullback injective; Coefficient injection H4(Z2)->H4(Z24) for torus homology

**Errata search:** Bounded queries recorded; no invalidating correction located

**Unverified inputs:** Kirby–Siebenmann Top/PL and PL-structure classification; PL surgery classification and compatibility of invariants; Whiteheadgroup Wh(Z^n)=0; Wall surgery-obstruction calculations and Rohlin input not reproved

**Finding and limit:** Correct scope; do not claim surgery theory independently verified. See unverified inputs and detailed note

[Primary source or scope evidence](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hsiawall2.pdf)

## CL-06

Ghys1995 p.596 Lemma4.3 Fact1

**Claim:** Diameter equality gives containing disks with disjoint interiors and collinear centers

**Status:** CONFIRMED_FALSE_REPAIRABLE_SOURCE_OVERSTATEMENT

**Original statement:** Original unavailable; scope corroborated in later primary research

**Proof coverage:** Filled equilateral triangle between [0,1] and [2,3] satisfies hypotheses but refutes disks; Needed no-triple consequence proved via intersection graph

**Errata search:** Bounded queries recorded; no invalidating correction located

**Unverified inputs:** None beyond the elementary argument stated

**Finding and limit:** Do not propagate as fatal: weaker needed consequence holds. See unverified inputs and detailed note

[Primary source or scope evidence](https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf)

## REG-HPS

Zhang Lemmas 2.5–2.8, pp.9–11; Section4

**Claim:** Stable manifolds, continuous leafwise C1 plaques, intrinsic Euclidean leaves

**Status:** Original statements checked, specialized proof mechanisms reconstructed

**Original statement:** HPS §§3,5,7; published §5 pp.60–63 and scan cross-checked

**Proof coverage:** Graph transform and differentiated contraction; local product contraction; direct nested-disc and J-invariance arguments

**Errata search:** Bounded primary-source searches recorded; no invalidating erratum located

**Unverified inputs:** Full general section/Lipschitz-jet theorem and smooth manifold foundations

**Finding and limit:** No required transverse C1 hypothesis; no demonstrated defect. No recursive proof audit of general HPS theorem

[Primary source or scope evidence](https://doi.org/10.1007/BFb0092042)

## REG-DM

Zhang Lemma2.3 pp.7–8; Lemma4.3 pp.16–17

**Claim:** Distributional Cauchy–Riemann regularity

**Status:** Exact original statement checked; narrow implication reconstructed

**Original statement:** Demailly 2012 I.(3.29)(a)

**Proof coverage:** Continuous coefficients are mollified; smooth convolutions satisfy CR; compact uniform convergence and the Cauchy formula give holomorphicity

**Errata search:** Bounded primary-source searches recorded; no invalidating erratum located

**Unverified inputs:** Standard distribution convolution and complex-analytic limit foundations

**Finding and limit:** No demonstrated defect in required implication. General arbitrary-current version not independently re-proved; continuous-coefficient consequence sufficient here

[Primary source or scope evidence](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf)

## REG-BM

Zhang Theorem3.3 and Lemma3.4 pp.13–14

**Claim:** Smoothness of the free vector translation action

**Status:** Original proof inaccessible; sufficient application independently reconstructed

**Original statement:** Broad original theorem wording not checked

**Proof coverage:** Average local holomorphic coordinates over the parameter; Cauchy estimates retain coordinate invertibility; convolution makes orbit chart smooth; constant rank and injectivity give smooth action

**Errata search:** Bounded primary-source searches recorded; no invalidating erratum located

**Unverified inputs:** Convolution, holomorphic estimates, constant-rank theorem

**Finding and limit:** No error shown in actual application; broad citation remains unchecked. Do not count inaccessible original theorem as proof-read

[Primary source or scope evidence](https://doi.org/10.2307/1969226)

## CTX-Cantat

**Location:** Zhang introduction; initial source audit

**Claim:** Prior holomorphic Anosov classification and holomorphic-foliation interpretation

**Status:** ORIGINAL_STATEMENT_AND_SELECTED_SECTIONS_CHECKED_NOT_FULL_PROOF_AUDIT

**Original statement:** Cantat2004 Proposition1.2, Theorem1.4 and relevant sections inspected

**Proof coverage:** Used as primary-source corroboration of Ghys scope; no independent audit of the complete Cantat proof

**Errata search:** Not separately exhaustively searched

**Unverified inputs:** Full proof and projective classification foundations

**Finding:** Context and corroboration, not a substitute for the Ghys proof audit

**Limits:** Not a premise needed beyond the critical dependencies already mapped

[Primary source](https://ems.press/content/serial-article-files/43027)

## CTX-history

**Location:** Zhang introduction and bibliography pp.18–19

**Claim:** Historical/contextual statements of Smale, Newhouse, Catanese, Catanese–Oguiso–Peternell, Xu–Zhang, and Zhang separate preprint

**Status:** CONTEXT_READ_ORIGINAL_PROOFS_NOT_AUDITED

**Original statement:** No complete original-source statement/proof audit in this bounded review

**Proof coverage:** None claimed; these contextual results are not premises of the reconstructed new argument

**Errata search:** Not separately searched

**Unverified inputs:** Their original proofs and full hypotheses remain unchecked

**Finding:** Coverage limit explicitly retained

**Limits:** Do not read the whole-paper audit as verifying every historical citation

Source: the exact supplied manuscript bibliography, pp.18–19.
