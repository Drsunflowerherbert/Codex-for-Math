# OpenAI mathematics release: revision-pinned inventory

Checked 2026-10-11 UTC. Revision: [fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/commit/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb).

## What this inventory establishes

- 719 active manuscripts in 372 result families across 17 discipline groups, parsed from the current manuscript map.
- The initial release had 722 manuscripts. Three family032 papers are now withdrawn; all 372 families remain.
- 27 active manuscript directory links changed: 13 citation-only revisions and 14 corrections/repairs/hypothesis clarifications, confirmed against their individual README version notes.
- Family IDs run through 377 with gaps; they are grouping labels, not ranks, and do not count distinct questions or independently solved problems.
- A family can contain a principal argument, companion results, alternatives, consequences, or conditional work. Do not interpret a family badge as certifying all its manuscripts.

## Source and review policy

The [official October6 announcement](https://openai.com/index/sharing-ai-progress-in-mathematics/) introduces model-produced mathematical results. The [repository README](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/README.md) warns that verification is at different stages. The [history](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/history.md) records corrections. All descriptions in the detailed index below are author claims; this inventory does not endorse their proofs, novelty, or priority.

The [Lean manifest](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/formalization.yaml) reports review.status = unchecked and scope = Partial progress. Its 173 paper-source entries, 200 main-result declarations and 189 comparator configurations are distinct units. The README/history claim 300/719 top-line results formalized; that total has not been independently reconstructed or verified here. There are 242 family scope notes. One manifest source still points to the pre-revision September23 Taming paper, while the active catalogue points to October6. Of its 173 source paths, 172 match active manuscript PDFs exactly.

No repository code was compiled or executed. LaTeX sources, metadata and Lean scope/configuration text were inspected as data. A Comparator challenge can contain a placeholder proof because the configuration points to a separate solution module; a placeholder in the challenge alone is not evidence that the configured proof is missing. Actual machine verification requires the configured toolchain and axiom/scope checks.

External peer review has not been established from the inspected official materials. A listed formalization, a human-reviewed mathematical proof, and a reproduced machine check are separate statuses.

## Changes and withdrawals

Individual withdrawal notices date the withdrawals October6; history groups them under October7; the public merge timestamp is October8 at05:20UTC. These are preserved separately rather than silently choosing one.

- Family032: [The rational Hodge conjecture for products of K3 surfaces](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-rational-Hodge-conjecture-for-products-of-K3-surfaces-October-4-2026/README.md). The stabilization-trace sign error leaves the proof unsupported; withdrawal does not say the statement is false.
- Family032: [Algebraicity of Kuga–Satake Correspondences for K3 Surfaces](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Algebraicity-of-Kuga-Satake-Correspondences-for-K3-Surfaces-October-3-2026/README.md). The stabilization-trace sign error leaves the proof unsupported; withdrawal does not say the statement is false.
- Family032: [Algebraicity of Weil classes on split abelian eightfolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Algebraicity-of-Weil-classes-on-split-abelian-eightfolds-September-18-2026/README.md). The stabilization-trace sign error leaves the proof unsupported; withdrawal does not say the statement is false.

The family032 heading changed from ‘Hodge and Kuga–Satake results for all projective K3 surfaces’ to ‘The rational Hodge conjecture for CM abelian varieties’. The latter and other surviving results must still be evaluated on their own dependencies.

### Family017 π audit

From initial adc7f124… to current fd4aeeb…, the manuscript PDF, complete manuscript source tree, README, catalogue block, Lean scope, comparator statement and entire Lean PiExponent implementation tree are unchanged. Hashes are in pi_revision_check.json. This is a revision comparison, not a correctness certification. The Lean scope explicitly excludes the paper’s Flint–Hills convergence consequence.

## Discipline counts

| Discipline | Families | Active manuscripts | Family Lean scope links |
|---|---:|---:|---:|
| Number theory | 31 | 58 | 17 |
| Algebraic and complex geometry | 36 | 86 | 8 |
| Real and complex analysis | 16 | 26 | 10 |
| Convex and metric geometry | 15 | 30 | 13 |
| Theoretical computer science | 40 | 73 | 34 |
| Dynamical systems and ergodic theory | 12 | 19 | 9 |
| Combinatorics | 37 | 50 | 33 |
| Algebra | 18 | 29 | 10 |
| Probability and statistical mechanics | 29 | 105 | 19 |
| Mathematical logic | 6 | 8 | 6 |
| Group theory | 14 | 22 | 12 |
| Mathematical physics | 25 | 59 | 17 |
| Operator algebras | 19 | 31 | 15 |
| Topology | 18 | 26 | 3 |
| Functional analysis | 11 | 19 | 10 |
| Differential geometry | 29 | 49 | 15 |
| Partial differential equations | 16 | 29 | 11 |

## Six first study targets

See [shortlist.md](shortlist.md) for exact statements, prerequisites, source links and proof boundaries. All six are supporting-lemma or explicit-example studies rather than attempts to certify headline open-problem solutions.

- Family025: [Exact-length Egyptian fractions and marker-preserving padding](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/build/elementary.tex).
- Family084: [Normalized periodic hitting implies global affine avoidance](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/build/sections/02-periodic.tex).
- Family322: [Radial contact in normed balls](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/build/main.tex).
- Family374: [Three-atom transport obstruction with exact distances](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/build/source/sections/sharpness.tex).
- Family005: [Mixed moments and Taylor-contact cancellation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/foundations.tex).
- Family325: [Positive-block energy and convex outer approximation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/build/main.tex).

## Files

- inventory.json: all719 active manuscript records, abstracts, family membership, pinned links, current and initial directory paths, and status distinctions.
- inventory.md: this report plus the complete source-linked index.
- shortlist.json / shortlist.md: six scoped study briefs.
- revision_changes.json / revision_readmes.json: all27 version changes and the three withdrawals.
- formalization_index.json: the manifest's sources and exact declarations/configurations, not a proof certificate.
- pi_revision_check.json: initial/current hash audit for family017.
- sources/: inspected public source snapshots. source_manifest.json records SHA-256 fingerprints.

## Complete active index


### Number theory

#### 001. Milne’s rationality conjecture and algebraic specialization.

- [Milne's rationality conjecture for abelian varieties](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/README.md) · citation-only; not independently verified here

#### 002. The full BSD formula from low Selmer corank.

- [Exact Birch–Swinnerton-Dyer Formula from Low Selmer Corank](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/exact-bsd-low-selmer-corank.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/README.md) · proof_statement_hypothesis_or_citation_correction; not independently verified here
- [The Selmer converse for elliptic curves at every prime](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/README.md) · citation-only; not independently verified here
- [The two-primary Birch–Swinnerton-Dyer formula in Selmer corank at most one](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/README.md) · citation-only; not independently verified here

#### 003. The quasi-Riemann hypothesis.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/003.md)
- [The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\Re s\gt 7/8$](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/README.md) · manifest paper-source listed; not independently verified here
- [The Quasi-Riemann Hypothesis (alternate 11/12 proof)](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/README.md) · not independently verified here
- [Uniform exclusion of Landau–Siegel zeros](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/README.md) · manifest paper-source listed; not independently verified here

#### 004. Hilbert’s tenth problem over ℚ.

- [Hilbert’s tenth problem over the rational numbers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026/README.md) · citation-only; not independently verified here
- [A pointwise 2-converse for elliptic curves with rational two-torsion](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/README.md) · citation-only; not independently verified here

#### 005. Irrationality of Catalan’s constant.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/005.md)
- [Catalan's constant is irrational](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Catalans-constant-is-irrational-September-24-2026/README.md) · not independently verified here

#### 006. Goldfeld’s conjecture: densities and mean analytic rank.

- [Goldfeld's analytic density conjecture and the 2-converse for elliptic curves](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-October-7-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-October-7-2026/README.md) · citation-only; not independently verified here
- [The mean analytic rank of quadratic twists of elliptic curves](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-mean-analytic-rank-of-quadratic-twists-of-elliptic-curves-October-6-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-mean-analytic-rank-of-quadratic-twists-of-elliptic-curves-October-6-2026/README.md) · citation-only; not independently verified here

#### 007. Ordinary two-point correlations and the corrected Elliott conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/007.md)
- [Ordinary two-point correlations of multiplicative functions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/README.md) · not independently verified here

#### 008. The Deligne–Drinfeld conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/008.md)
- [The Deligne-Drinfeld conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Deligne-Drinfeld-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Deligne-Drinfeld-conjecture-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 009. Function-field reconstruction from Milnor K-theory and Galois data.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/009.md)
- [Reconstruction of Function Fields from Mod-ℓ Milnor K-Theory](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/mod-ell-bogomolov-pop.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/README.md) · not independently verified here
- [Reconstruction from Milnor K-theory modulo the characteristic](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/README.md) · not independently verified here
- [The Bogomolov-Pop reconstruction theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/README.md) · not independently verified here

#### 010. Unrestricted pro-modularity at the prime two.

- [Unrestricted pro-modularity at the prime two](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/two-adic-promodularity.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Unrestricted-pro-modularity-at-the-prime-two-October-6-2026/README.md) · citation-only; not independently verified here
- [The Dimension of the Two-Adic Hecke Algebra at Odd Level](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/two-adic-hecke.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/README.md) · not independently verified here
- [Fontaine–Mazur modularity at the prime 2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/README.md) · citation-only; not independently verified here

#### 011. Prime-factor statistics of $p-1$.

- [Weighted dilation graphs, smooth shifted primes and totient fibers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/README.md) · not independently verified here
- [The Poisson-Dirichlet law for prime predecessors](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/README.md) · not independently verified here
- [Prime Predecessors with an Even Number of Prime Factors](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/README.md) · not independently verified here

#### 012. Independent largest prime factors of consecutive integers.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/012.md)
- [The joint Dickman law for consecutive integers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/README.md) · not independently verified here

#### 013. Ostmann’s inverse Goldbach conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/013.md)
- [The additive indecomposability of the primes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/the-additive-indecomposability-of-the-primes-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/the-additive-indecomposability-of-the-primes-September-24-2026/README.md) · not independently verified here

#### 014. Restricted geometric Langlands, global Arthur enhancements, and generic Ramanujan.

- [Global Arthur Enhancements of Cuspidal Excursion Parameters](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/README.md) · not independently verified here
- [Rationality of the Canonical Unramified Arthur Filtration](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Rationality-of-the-Canonical-Unramified-Arthur-Filtration-September-24-2026/README.md) · not independently verified here
- [Ramanujan-Arthur Decompositions of Cuspidal Functions at Full Finite Level](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/README.md) · not independently verified here
- [Temperedness at ramified places for globally generic exceptional groups](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/ramified-ramanujan.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/README.md) · not independently verified here
- [The Restricted Geometric Langlands Equivalence in Positive Characteristic](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Restricted-Geometric-Langlands-Equivalence-in-Positive-Characteristic-September-24-2026/README.md) · not independently verified here
- [Constructible tame Hecke eigensheaves in positive characteristic](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/constructible-tame-hecke-eigensheaves-positive-characteristic.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Constructible-tame-Hecke-eigensheaves-in-positive-characteristic-October-5-2026/README.md) · not independently verified here
- [Tame Hecke Eigensheaves with Several Marked Points](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/Tame-Hecke-Eigensheaves-with-Several-Marked-Points.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Tame-Hecke-Eigensheaves-with-Several-Marked-Points-October-5-2026/README.md) · not independently verified here
- [Frobenius Structures on Tame Hecke Eigensheaves](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/tame-hecke-frobenius.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Frobenius-Structures-on-Tame-Hecke-Eigensheaves-October-5-2026/README.md) · not independently verified here

#### 015. Torus-packet equidistribution in prime, quartic, and sextic degrees.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/015.md)
- [Equidistribution of Prime-Degree Torus Packets with Arbitrary Local Type](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026/README.md) · not independently verified here
- [Equidistribution of primitive quartic torus packets for arbitrary orders](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/quartic-torus-packets.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/README.md) · not independently verified here
- [Equidistribution of Primitive Sextic Torus Packets](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026/primitive-sextic-torus-packets.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026/README.md) · not independently verified here

#### 016. Zilber–Pink in abelian varieties and the Siegel threefold.

- [The abelian Zilber–Pink conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/README.md) · not independently verified here
- [The E×CM component of Zilber–Pink for curves in A2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/README.md) · not independently verified here
- [Quaternionic division points on curves in the Siegel threefold](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/README.md) · not independently verified here
- [Elliptic squares and Zilber–Pink for curves in A2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/README.md) · not independently verified here

#### 017. The irrationality exponent of π is 2.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/017.md)
- [The irrationality exponent of pi is 2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/README.md) · not independently verified here

#### 018. The Margulis–Platonov conjecture over global fields.

- [The Margulis–Platonov conjecture over global function fields](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026/margulis-platonov-global-function-fields.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026/README.md) · not independently verified here
- [The Margulis–Platonov conjecture over number fields](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026/README.md) · not independently verified here

#### 019. The local p-adic section conjecture and global consequences.

- [Étale covers with a prescribed exterior sheet](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Etale-covers-with-a-prescribed-exterior-sheet-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Etale-covers-with-a-prescribed-exterior-sheet-September-24-2026/README.md) · not independently verified here
- [The p-adic section conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-p-adic-section-conjecture-October-6-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-p-adic-section-conjecture-October-6-2026/README.md) · citation-only; not independently verified here

#### 020. Squarefree quartics and power-free polynomial values.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/020.md)
- [Squarefree values of quartics and power-free values of polynomials](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 021. A quadratic bound for Jacobsthal’s function.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/021.md)
- [A quadratic bound for Jacobsthal's function](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 022. The weak inhomogeneous Duffin–Schaeffer conjecture.

- [The Weak Inhomogeneous Duffin–Schaeffer Conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/README.md) · not independently verified here

#### 023. Patterson's first moment for cubic Gauss sums.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/023.md)
- [An unconditional first moment for cubic Gauss sums](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/README.md) · not independently verified here

#### 024. An asymptotic formula for the number of totients.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/024.md)
- [An asymptotic formula for the number of totients](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/An-asymptotic-formula-for-the-number-of-totients-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/README.md) · not independently verified here

#### 025. Short Egyptian fractions.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/025.md)
- [Short Egyptian fractions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/Short-Egyptian-fractions-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 026. Positive lower density of large prime gaps.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/026.md)
- [Positive lower density of large prime gaps](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/README.md) · not independently verified here

#### 027. Potential integral density on curve character varieties.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/027.md)
- [Integral points on character varieties of curves](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 028. Uniformly bounded components of Gaussian-prime graphs.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/028.md)
- [Bounded-Step Walks on Gaussian Primes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/README.md) · manifest paper-source listed; not independently verified here

#### 029. Primitive roots for every admissible integer base.

- [Primitive roots for every admissible integer base](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/primitive-roots-all-integer-bases.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/README.md) · not independently verified here
- [Simultaneous primitive roots: a conditional lower bound for prime bases](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/simultaneous-primitive-roots-conditional-lower-bound-prime-bases.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/README.md) · not independently verified here

#### 030. Modularity of elliptic curves over imaginary quadratic fields.

- [Modularity of elliptic curves over imaginary quadratic fields](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/README.md) · not independently verified here

#### 031. Uchida’s conjecture for open homomorphisms of Galois groups.

- [Open Homomorphisms of Global Solvably Closed Galois Groups](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/open-homomorphisms-solvably-closed-galois-groups.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/README.md) · not independently verified here


### Algebraic and complex geometry

#### 032. The rational Hodge conjecture for CM abelian varieties.

- [The rational Hodge conjecture for CM abelian varieties](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/README.md) · citation-only; not independently verified here
- [Algebraic Kuga–Satake correspondences and Hodge conjectures on a K3 quadratic locus](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/README.md) · not independently verified here
- [Weil classes and Hodge classes on abelian powers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/README.md) · citation-only; not independently verified here
- [Abelian covers, Gale correspondences, and the Hodge conjecture for powers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/README.md) · citation-only; not independently verified here
- [A Conditional Reduction for Algebraic Kuga–Satake Correspondences](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/README.md) · not independently verified here

#### 033. Iitaka subadditivity, variation, and logarithmic additivity.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/033.md)
- [Orbifold and logarithmic Iitaka subadditivity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026/README.md) · not independently verified here
- [Logarithmic Kodaira dimension and whole-fiber variation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/README.md) · not independently verified here
- [The reverse logarithmic Kodaira inequality and additivity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/README.md) · not independently verified here
- [Projective Hodge lines and ordinary Iitaka subadditivity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026/README.md) · not independently verified here
- [B-semiampleness for compact log-smooth Kähler fibrations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026/README.md) · not independently verified here

#### 034. Log abundance for compact Kähler spaces under logarithmic Iitaka subadditivity.

- [Log abundance for compact Kähler spaces under logarithmic Iitaka subadditivity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Log-abundance-for-compact-Kahler-spaces-under-logarithmic-Iitaka-subadditivity-October-6-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Log-abundance-for-compact-Kahler-spaces-under-logarithmic-Iitaka-subadditivity-October-6-2026/README.md) · proof_statement_hypothesis_or_citation_correction; not independently verified here
- [Uniform indices for semi-log-canonical log Calabi–Yau pairs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-indices-for-semi-log-canonical-log-Calabi-Yau-pairs-October-5-2026/uniform-slc-index.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-indices-for-semi-log-canonical-log-Calabi-Yau-pairs-October-5-2026/README.md) · not independently verified here
- [Conditional good minimal models for compact Kähler fourfolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Conditional-good-minimal-models-for-compact-Kahler-fourfolds-October-6-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Conditional-good-minimal-models-for-compact-Kahler-fourfolds-October-6-2026/README.md) · proof_statement_hypothesis_or_citation_correction; not independently verified here
- [Log abundance in characteristic zero](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Log-abundance-in-characteristic-zero-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Log-abundance-in-characteristic-zero-September-24-2026/README.md) · not independently verified here
- [Minimal metrics and interior injectivity for nef adjoints](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Minimal-metrics-and-interior-injectivity-for-nef-adjoints-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Minimal-metrics-and-interior-injectivity-for-nef-adjoints-September-27-2026/README.md) · not independently verified here
- [Fourfold nonvanishing by minimal metrics and moving jets](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Fourfold-nonvanishing-by-minimal-metrics-and-moving-jets-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Fourfold-nonvanishing-by-minimal-metrics-and-moving-jets-September-27-2026/README.md) · not independently verified here
- [Lifting sections from the reduced support of an adjoint](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Lifting-sections-from-the-reduced-support-of-an-adjoint-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Lifting-sections-from-the-reduced-support-of-an-adjoint-September-27-2026/README.md) · not independently verified here
- [Schnell fiber spaces and good canonical models](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Schnell-fiber-spaces-and-good-canonical-models-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Schnell-fiber-spaces-and-good-canonical-models-September-24-2026/README.md) · not independently verified here
- [Uniform log Iitaka fibrations and bounded moduli denominators](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-log-Iitaka-fibrations-and-bounded-moduli-denominators-October-4-2026/uniform-log-iitaka.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-log-Iitaka-fibrations-and-bounded-moduli-denominators-October-4-2026/README.md) · not independently verified here
- [Uniform Pluricanonical Iitaka Fibrations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Pluricanonical-Iitaka-Fibrations-October-3-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Pluricanonical-Iitaka-Fibrations-October-3-2026/README.md) · not independently verified here
- [Relative denominators and effective systems for log Calabi-Yau fibrations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Relative-denominators-and-effective-systems-for-log-Calabi-Yau-fibrations-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Relative-denominators-and-effective-systems-for-log-Calabi-Yau-fibrations-September-27-2026/README.md) · not independently verified here
- [Arithmetic Stein-degree bounds for log Calabi–Yau pairs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Arithmetic-Stein-degree-bounds-for-log-Calabi-Yau-pairs-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Arithmetic-Stein-degree-bounds-for-log-Calabi-Yau-pairs-September-25-2026/README.md) · not independently verified here
- [Uniform effective log Iitaka fibrations for fourfolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-effective-log-Iitaka-fibrations-for-fourfolds-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-effective-log-Iitaka-fibrations-for-fourfolds-September-26-2026/README.md) · not independently verified here
- [Abundance after nonvanishing for compact Kähler fourfolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Abundance-after-nonvanishing-for-compact-Kahler-fourfolds-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Abundance-after-nonvanishing-for-compact-Kahler-fourfolds-September-27-2026/README.md) · not independently verified here

#### 035. Log-canonical threefold abundance in numerical dimension one.

- [Log abundance in numerical dimension one for threefolds in positive characteristic](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Log-abundance-in-numerical-dimension-one-for-threefolds-in-positive-characteristic-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Log-abundance-in-numerical-dimension-one-for-threefolds-in-positive-characteristic-October-5-2026/README.md) · not independently verified here
- [Abundance in numerical dimension one for terminal threefolds in positive characteristic](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Abundance-in-numerical-dimension-one-for-terminal-threefolds-in-positive-characteristic-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Abundance-in-numerical-dimension-one-for-terminal-threefolds-in-positive-characteristic-September-24-2026/README.md) · not independently verified here

#### 036. Numerical semiampleness and generalized minimal models.

- [Numerical semiampleness of nef adjoint classes on compact Kähler manifolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Numerical-semiampleness-of-nef-adjoint-classes-on-compact-Kahler-manifolds-October-6-2026/numerical-generalized-abundance.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Numerical-semiampleness-of-nef-adjoint-classes-on-compact-Kahler-manifolds-October-6-2026/README.md) · proof_statement_hypothesis_or_citation_correction; not independently verified here
- [Numerical Semiampleness of Nef Adjoint Divisors](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Numerical-Semiampleness-of-Nef-Adjoint-Divisors-October-3-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Numerical-Semiampleness-of-Nef-Adjoint-Divisors-October-3-2026/README.md) · not independently verified here
- [Minimal models and Mori fibre spaces for generalized log canonical Q-pairs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Minimal-models-and-Mori-fibre-spaces-for-generalized-log-canonical-Q-pairs-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Minimal-models-and-Mori-fibre-spaces-for-generalized-log-canonical-Q-pairs-September-24-2026/README.md) · not independently verified here
- [Minimal models in numerical dimension one](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Minimal-models-in-numerical-dimension-one-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Minimal-models-in-numerical-dimension-one-September-24-2026/README.md) · not independently verified here

#### 037. The ordinary-double-point volume gap.

- [The ordinary-double-point gap in every dimension](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/README.md) · not independently verified here
- [The normalized-volume gap in dimension four](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-normalized-volume-gap-in-dimension-four-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-normalized-volume-gap-in-dimension-four-September-24-2026/README.md) · not independently verified here

#### 038. Fujita’s freeness conjecture.

- [Fujita's freeness conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Fujitas-freeness-conjecture-September-23-2026/Fujitas-freeness-conjecture-September-23-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Fujitas-freeness-conjecture-September-23-2026/README.md) · not independently verified here

#### 039. Nagata’s conjecture and maximal Seshadri constants.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/039.md)
- [Nagata's conjecture for plane curves](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [Maximal Seshadri constants on arbitrary polarized surfaces](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [Maximal Multipoint Seshadri Constants in Higher Dimensions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/README.md) · not independently verified here
- [Maximal multipoint Seshadri constants in positive characteristic](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/seshadri-positive-characteristic.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/README.md) · not independently verified here

#### 040. Bloch’s conjecture for complex surfaces.

- [Bloch’s conjecture for surfaces with p_g=0](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Blochs-Conjecture-for-Surfaces-with-pg-equals-q-equals-0-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Blochs-Conjecture-for-Surfaces-with-pg-equals-q-equals-0-September-24-2026/README.md) · not independently verified here

#### 041. Hyperkähler SYZ and projective-space bases.

- [Projective-space bases of Lagrangian fibrations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/README.md) · not independently verified here
- [The strong hyperkähler SYZ conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/README.md) · not independently verified here

#### 042. Oka classification for minimal compact complex surfaces: Kodaira dimension zero and class VII.

- [Every complex K3 surface is Oka](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Every-complex-K3-surface-is-Oka-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Every-complex-K3-surface-is-Oka-September-23-2026/README.md) · not independently verified here

#### 043. P = W for fixed-determinant SLn moduli spaces.

- [P=W in composite rank for fixed determinant](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/P-equals-W-in-composite-rank-for-fixed-determinant-September-24-2026/README.md) · not independently verified here

#### 044. The equivariant cohomological Hikita conjecture.

- [The equivariant cohomological Hikita conjecture for arbitrary quivers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/README.md) · not independently verified here

#### 046. Shafarevich counterexamples in dimension two and with large fundamental group.

- [A projective fourfold with large fundamental group and non-Stein universal cover](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-projective-fourfold-with-large-fundamental-group-and-non-Stein-universal-cover-October-5-2026/large-fundamental-group-non-stein.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-projective-fourfold-with-large-fundamental-group-and-non-Stein-universal-cover-October-5-2026/README.md) · not independently verified here
- [A surface counterexample to Shafarevich holomorphic convexity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-surface-counterexample-to-Shafarevich-holomorphic-convexity-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-surface-counterexample-to-Shafarevich-holomorphic-convexity-September-23-2026/README.md) · not independently verified here

#### 047. Zariski cancellation and affine fibrations over the complex numbers.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/047.md)
- [An explicit failure of complex affine-space cancellation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 048. A characteristic-zero counterexample to Lipman–Zariski.

- [A singular normal affine surface with free tangent sheaf](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-singular-normal-affine-surface-with-free-tangent-sheaf-September-23-2026/README.md) · not independently verified here

#### 049. A stable-coordinate counterexample in four variables.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/049.md)
- [A stable coordinate that is not a coordinate in four variables](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026/stable-coordinate-four-variables.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026/README.md) · manifest paper-source listed; not independently verified here
- [An explicit noncoordinate polynomial with affine three-space zero fibre](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 050. A counterexample to Griffiths’ positivity conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/050.md)
- [Ample rank-two bundles on the quadric surface without Griffiths-positive metrics](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 051. Kobayashi’s canonical-ampleness conjecture.

- [Canonical ampleness of compact hyperbolic Kähler manifolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/canonical-ampleness.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Canonical-ampleness-of-compact-hyperbolic-Kahler-manifolds-September-23-2026/README.md) · not independently verified here

#### 052. Tangent splittings and product decompositions.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/052.md)
- [Universal-cover splitting for compact Kähler manifolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [Integrability of split tangent bundles on rationally connected manifolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/README.md) · not independently verified here

#### 053. A counterexample to Pixton completeness in Chow.

- [A high-arity counterexample to Pixton completeness in Chow](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-high-arity-counterexample-to-Pixton-completeness-in-Chow-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-high-arity-counterexample-to-Pixton-completeness-in-Chow-September-24-2026/README.md) · not independently verified here

#### 054. Irrational cubic fourfolds with Hodge-theoretic and categorical K3 associations.

- [Irrational cubic fourfolds with geometric K3 categories](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Irrational-cubic-fourfolds-with-geometric-K3-categories-September-24-2026/README.md) · not independently verified here

#### 055. Gepner symmetry and large-volume stability on threefolds.

- [A Gepner stability condition on every smooth quintic threefold](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/README.md) · not independently verified here
- [Prescribed large-volume charges on threefolds with trivial canonical bundle](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/README.md) · not independently verified here

#### 056. Termination of projective and Kähler fourfold minimal model programs.

- [Termination of generalized log canonical flips on compact Kähler fourfolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Termination-of-generalized-log-canonical-flips-on-compact-Kahler-fourfolds-October-7-2026/termination-generalized-lc-kahler-fourfolds.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Termination-of-generalized-log-canonical-flips-on-compact-Kahler-fourfolds-October-7-2026/README.md) · proof_statement_hypothesis_or_citation_correction; not independently verified here
- [Termination of generalized-canonical flips on compact Kähler fourfolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Termination-of-generalized-canonical-flips-on-compact-Kahler-fourfolds-October-6-2026/termination-generalized-terminal-flips-compact-kahler-fourfolds.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Termination-of-generalized-canonical-flips-on-compact-Kahler-fourfolds-October-6-2026/README.md) · proof_statement_hypothesis_or_citation_correction; not independently verified here
- [Termination for projective log canonical fourfolds with rational boundary](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Termination-for-projective-log-canonical-fourfolds-with-rational-boundary-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Termination-for-projective-log-canonical-fourfolds-with-rational-boundary-September-24-2026/README.md) · not independently verified here
- [Finite ordinary minimal model programs on compact Kähler fourfolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-October-6-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-October-6-2026/README.md) · proof_statement_hypothesis_or_citation_correction; not independently verified here
- [Finite ordinary minimal model programs on compact Kähler fourfolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-September-24-2026/README.md) · not independently verified here

#### 057. Fundamental groups of special complex varieties and root orbifolds.

- [The abelianity conjecture for special compact Kähler manifolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-abelianity-conjecture-for-special-compact-Kahler-manifolds-September-23-2026/README.md) · not independently verified here
- [Two-step monodromy of special quasi-projective varieties](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Two-step-monodromy-of-special-quasi-projective-varieties-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Two-step-monodromy-of-special-quasi-projective-varieties-September-24-2026/README.md) · not independently verified here
- [A conditional abelianity theorem for special fourfold pairs with a half-weight divisor](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-with-a-half-weight-divisor-October-5-2026/README.md) · not independently verified here

#### 058. Semialgebraic universal covers and bounded domains.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/058.md)
- [Semialgebraic universal covers of normal projective varieties](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/README.md) · not independently verified here
- [Symmetry of semialgebraic bounded domains with compact quotient](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 059. Counterexamples to Zariski’s multiplicity conjecture.

- [Ambiently homeomorphic isolated hypersurfaces of multiplicities two and three](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/README.md) · not independently verified here
- [Ambiently homeomorphic isolated hypersurface germs in ℂ⁴ with multiplicities four and five](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/README.md) · not independently verified here

#### 060. The Global Spherical Shell conjecture.

- [Global Spherical Shells on Minimal Surfaces of Class VII](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/README.md) · not independently verified here

#### 062. Projective contact classification and the LeBrun–Salamon conjecture.

- [Contact Fano manifolds and the LeBrun–Salamon conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/README.md) · not independently verified here

#### 063. The generalized Mukai conjecture.

- [The generalized Mukai conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Generalized-Mukai-Conjecture-September-24-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Generalized-Mukai-Conjecture-September-24-2026/README.md) · not independently verified here

#### 064. Topological triviality of μ-constant surface singularities.

- [Topological triviality of mu-constant families of surface singularities](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Topological-triviality-of-mu-constant-families-of-surface-singularities-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Topological-triviality-of-mu-constant-families-of-surface-singularities-September-24-2026/README.md) · not independently verified here

#### 065. Virasoro constraints for complete intersections and projective-bundle towers.

- [Virasoro Constraints under Projectivization](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Virasoro-Constraints-under-Projectivization-October-5-2026/virasoro-constraints-under-projectivization.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Virasoro-Constraints-under-Projectivization-October-5-2026/README.md) · not independently verified here
- [Virasoro Constraints for Projective Complete Intersections](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/README.md) · not independently verified here

#### 066. Bounded klt complements for Fano contractions.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/066.md)
- [Bounded klt complements for Fano contractions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/Bounded-klt-complements-for-Fano-contractions-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/README.md) · not independently verified here
- [Uniform Cartier sections for Fano type contractions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 067. The Campana–Peternell conjecture in dimension six.

- [The Campana–Peternell conjecture in dimension six](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/README.md) · not independently verified here

#### 068. Anticanonical nonvanishing in every dimension.

- [Anticanonical nonvanishing from smooth semipositivity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Anticanonical-nonvanishing-from-smooth-semipositivity-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Anticanonical-nonvanishing-from-smooth-semipositivity-September-26-2026/README.md) · not independently verified here
- [Invariant anticanonical indices and conversion of twisted differentials](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Invariant-anticanonical-indices-and-conversion-of-twisted-differentials-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Invariant-anticanonical-indices-and-conversion-of-twisted-differentials-September-26-2026/README.md) · not independently verified here
- [Bounded anticanonical metrics on klt pairs and torus quotients](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-anticanonical-metrics-on-klt-pairs-and-torus-quotients-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-anticanonical-metrics-on-klt-pairs-and-torus-quotients-September-26-2026/README.md) · not independently verified here
- [Cohomological transfer and equivariant anticanonical sections](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cohomological-transfer-and-equivariant-anticanonical-sections-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cohomological-transfer-and-equivariant-anticanonical-sections-September-26-2026/README.md) · not independently verified here
- [Metric descent and rank-preserving contractions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Metric-descent-and-rank-preserving-contractions-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Metric-descent-and-rank-preserving-contractions-September-26-2026/README.md) · not independently verified here
- [Integrable metrics and effectivity with controlled boundary](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integrable-metrics-and-effectivity-with-controlled-boundary-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integrable-metrics-and-effectivity-with-controlled-boundary-September-26-2026/README.md) · not independently verified here
- [Exact orders and invariant anticanonical linear systems](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-orders-and-invariant-anticanonical-linear-systems-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-orders-and-invariant-anticanonical-linear-systems-September-26-2026/README.md) · not independently verified here

#### 069. Global quantum geometric Langlands at irrational level.

- [Global quantum geometric Langlands at irrational level](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/quantum-langlands.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/README.md) · not independently verified here


### Real and complex analysis

#### 071. Koebe’s circle-domain conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/071.md)
- [Removable Boundaries and Rigidity of Circle Domains](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Removable-Boundaries-and-Rigidity-of-Circle-Domains-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Removable-Boundaries-and-Rigidity-of-Circle-Domains-September-23-2026/README.md) · not independently verified here
- [Koebe's Circle-Domain Conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Koebes-Circle-Domain-Conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Koebes-Circle-Domain-Conjecture-September-23-2026/README.md) · not independently verified here

#### 072. Brennan's conjecture and the integral-means spectrum.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/072.md)
- [Brennan's conjecture and sharp inverse-square integral means](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/README.md) · manifest paper-source listed; not independently verified here
- [A strict inverse-first-power bound for univalent functions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 073. The Falconer distance conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/073.md)
- [The Falconer distance conjecture in all dimensions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 074. Kakeya in three and four dimensions.

- [The Kakeya maximal conjecture in three dimensions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/README.md) · not independently verified here
- [Every four-dimensional Kakeya set has full Hausdorff dimension](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/README.md) · not independently verified here

#### 075. The $L\log L$ Fourier-convergence conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/075.md)
- [Almost-everywhere Fourier convergence in L log L](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 076. Real ultraflat Littlewood polynomials and unbounded binary merit factors.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/076.md)
- [Ultraflat real Littlewood polynomials](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ultraflat-real-Littlewood-polynomials-October-5-2026/ultraflat-real-littlewood-polynomials.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ultraflat-real-Littlewood-polynomials-October-5-2026/README.md) · not independently verified here
- [Nearly minimal maxima and positive minima of Littlewood polynomials](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026/littlewood-lower-envelope.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nearly-minimal-maxima-and-positive-minima-of-Littlewood-polynomials-October-5-2026/README.md) · not independently verified here
- [Asymptotically minimal maxima of real Littlewood polynomials](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 077. Fourier restriction for positively curved surfaces.

- [Elliptic capacity propagation and Fourier restriction to the sphere](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/README.md) · not independently verified here
- [Diagonal Fourier extension for positively curved surfaces in three dimensions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026/README.md) · not independently verified here

#### 078. The three-dimensional Bochner–Riesz conjecture.

- [Bochner–Riesz multipliers in three dimensions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/README.md) · not independently verified here

#### 079. Local smoothing in three dimensions.

- [Critical local smoothing for the three-dimensional wave equation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/README.md) · not independently verified here

#### 080. The exact Sobolev endpoint for Schrödinger convergence.

- [Endpoint convergence for the planar Schrodinger equation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026/README.md) · not independently verified here
- [Endpoint pointwise convergence for the Schrodinger equation in higher dimensions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Endpoint-pointwise-convergence-for-the-Schrodinger-equation-in-higher-dimensions-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Endpoint-pointwise-convergence-for-the-Schrodinger-equation-in-higher-dimensions-September-24-2026/README.md) · not independently verified here

#### 081. Riesz transforms and rectifiability in higher codimension.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/081.md)
- [Riesz transforms and uniform rectifiability in higher codimension](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 082. Annular variation and dyadic absolute bounds for the triangular Hilbert transform.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/082.md)
- [Annular variation of the triangular Hilbert transform at the symmetric point](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/annular-variation.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026/README.md) · not independently verified here
- [An L³ bound for the dyadic triangular Hilbert form](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026/dyadic-triangular-hilbert.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026/README.md) · not independently verified here
- [The maximal triangular Hilbert transform at the symmetric point](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 083. Hilbert transforms along Lipschitz directions.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/083.md)
- [A uniform Hilbert transform estimate for Lipschitz directions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/README.md) · not independently verified here

#### 084. The geometric case of the Erdős similarity conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/084.md)
- [The geometric case of the Erdős similarity conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/geometric-erdos-similarity.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/README.md) · not independently verified here
- [The dyadic case of the Erdős similarity conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026/README.md) · not independently verified here

#### 085. Endpoint Sobolev regularity of centered disk averages.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/085.md)
- [An Endpoint Gradient Bound for the Centered Disk Maximal Operator](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026/README.md) · manifest paper-source listed; not independently verified here

#### 086. An L3 bound for the trilinear Hilbert transform.

- [An L3 bound for the trilinear Hilbert transform](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/README.md) · not independently verified here


### Convex and metric geometry

#### 087. The Mahler conjectures, functional inequalities and polar-product symplectic width.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/087.md)
- [The symmetric Mahler conjecture and its equality cases](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/README.md) · manifest paper-source listed; not independently verified here
- [The Mahler Conjecture for General Convex Bodies](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/README.md) · not independently verified here
- [Symplectic Balls in Symmetric Polar Products](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026/README.md) · manifest paper-source listed; not independently verified here

#### 088. Sharp projection-body inequalities and a counterexample to simplex maximization.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/088.md)
- [Petty’s projection-volume conjecture in dimensions at least four](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/README.md) · manifest paper-source listed; not independently verified here
- [A product counterexample to the simplex maximum for projection-body volume](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 089. Bounded-distortion L1 embeddings of planar and bounded-treewidth graphs.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/089.md)
- [Planar Graph Metrics Embed into L1 with Constant Distortion](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [L1 Embeddings of Graphs of Bounded Treewidth](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 090. Triangular-lattice optimality, long-range Riesz and Coulomb energies, and spherical logarithmic energy.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/090.md)
- [An atomic certificate for triangular-lattice universal optimality](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/README.md) · not independently verified here
- [Universal optimality of the triangular lattice](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026/README.md) · not independently verified here
- [A sharp Fourier certificate for planar circle packing](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-sharp-Fourier-certificate-for-planar-circle-packing-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-sharp-Fourier-certificate-for-planar-circle-packing-September-23-2026/README.md) · not independently verified here
- [Triangular minimality for planar Coulomb renormalized energy](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/README.md) · not independently verified here

#### 091. Logarithmic and Lp Brunn–Minkowski inequalities and the B-conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/091.md)
- [The logarithmic Brunn–Minkowski conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 092. The optimal order of convex-body covering density.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/092.md)
- [A single-lattice covering bound of order n log n](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [Translative covering densities of order n log n](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/README.md) · not independently verified here

#### 093. Dimension-free logarithmic Sobolev inequality for subgaussian log-concave measures.

- [A dimension-free logarithmic Sobolev inequality for subgaussian log-concave measures](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/README.md) · not independently verified here

#### 094. Subpolynomial dimension reduction in Lp.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/094.md)
- [Subpolynomial dimension reduction in Lp](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 095. Hyperbolicity cones without semidefinite lifts.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/095.md)
- [Hyperbolicity Cones Without Semidefinite Lifts](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026/nonliftable-hyperbolicity.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026/README.md) · not independently verified here
- [A nonspectrahedral hyperbolicity cone](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026/nonspectrahedral-hyperbolicity-cone.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026/README.md) · manifest paper-source listed; not independently verified here
- [An Exact Semidefinite Lift of a Nonspectrahedral Hyperbolicity Cone](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone-October-5-2026/Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone-October-5-2026/README.md) · not independently verified here

#### 096. The Gaussian propeller conjecture in every dimension.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/096.md)
- [The Gaussian propeller bound in every dimension](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 097. The Euclidean Steinitz–Bergström bound.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/097.md)
- [The Euclidean Steinitz–Bergström theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 098. Compact counterexamples to bi-Lipschitz dimension reduction.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/098.md)
- [A doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 099. The sharp exponential scale of edit-distance distortion.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/099.md)
- [Edit Distance in l1: Matching Bounds up to Constants in the Exponent](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/README.md) · not independently verified here
- [Finite-Circle Obstructions, Binary Codes, and Histogram Embeddings for Edit Distance](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/README.md) · not independently verified here
- [Tree Constructions for the l1 Distortion of Binary Edit Distance](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026/README.md) · not independently verified here

#### 100. Cylinder coverings below the half-area bound.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/100.md)
- [Finite angular cylinder covers below the half-area bound](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-angular-cylinder-covers-below-the-half-area-bound-September-27-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-angular-cylinder-covers-below-the-half-area-bound-September-27-2026/README.md) · not independently verified here
- [Finite cylinder approximation of ruled sets](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-cylinder-approximation-of-ruled-sets-September-27-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-cylinder-approximation-of-ruled-sets-September-27-2026/README.md) · not independently verified here
- [Slope-field perturbations of the two-cylinder covering](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Slope-field-perturbations-of-the-two-cylinder-covering-September-27-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Slope-field-perturbations-of-the-two-cylinder-covering-September-27-2026/README.md) · not independently verified here
- [Finite triangular approximation of radial sweeps](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-triangular-approximation-of-radial-sweeps-September-27-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-triangular-approximation-of-radial-sweeps-September-27-2026/README.md) · not independently verified here

#### 101. The sharp simplex conjecture for isotropic constants.

- [A sharp entropy bound and the simplex inequality for isotropic constants](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/isotropic-simplex.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/README.md) · not independently verified here


### Theoretical computer science

#### 102. The Unique Games Conjecture and optimal approximation thresholds.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/102.md)
- [The Unique Games Theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Unique-Games-Theorem-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [A Direct Proof of Optimal Max-Cut Hardness](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [The Factor-Two Hardness Threshold for Vertex Cover](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [Constant-factor hardness of Min-UnCut](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Constant-factor-hardness-of-Min-UnCut-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Constant-factor-hardness-of-Min-UnCut-September-23-2026/README.md) · not independently verified here
- [Constant-factor hardness of directed feedback vertex set](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/README.md) · not independently verified here

#### 103. Exact derandomization of logarithmic space: $\mathsf L=\mathsf{RL}=\mathsf{BPL}$.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/103.md)
- [Exact derandomization of logarithmic space: L = RL = BPL](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 104. Quasipolynomial algorithms for mean-payoff, stochastic and parity games.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/104.md)
- [Turn-Based Stochastic Mean-Payoff Games in Deterministic Quasipolynomial Time](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/stochastic-mean-payoff-games.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/README.md) · not independently verified here
- [Mean-payoff parity games in quasipolynomial time](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/mean-payoff-parity.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Mean-payoff-parity-games-in-quasipolynomial-time-October-5-2026/README.md) · not independently verified here
- [Deterministic quasipolynomial-time mean-payoff games](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Deterministic-quasipolynomial-time-mean-payoff-games-September-25-2026/README.md) · not independently verified here
- [Randomized quasipolynomial-time mean-payoff games](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 105. Perfect completeness for 2-to-1 games.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/105.md)
- [Perfect completeness for 2-to-1 games](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 106. Hardness of coloring three-colorable graphs.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/106.md)
- [Hardness of finding large independent sets in three-colorable graphs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 107. Matrix multiplication with exponent at most 9/4.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/107.md)
- [An Upper Bound of 9/4 for the Matrix Multiplication Exponent](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/README.md) · manifest paper-source listed; not independently verified here
- [Complex Matrix Multiplication Below 2.258 and Rectangular Bounds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/README.md) · manifest paper-source listed; not independently verified here
- [Staggered extraction for exact matrix multiplication over every field](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 108. A cubic permanent–determinant lower bound.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/108.md)
- [A cubic lower bound for border determinantal complexity of the permanent](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/README.md) · not independently verified here

#### 109. Integer multiplication below $n\log n$.

- [Integer multiplication below n log n](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integer-multiplication-below-n-log-n-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integer-multiplication-below-n-log-n-September-23-2026/README.md) · not independently verified here

#### 110. Optimal-order randomized k-server on arbitrary metrics.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/110.md)
- [Squared-logarithmic randomized k-server on arbitrary metrics](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026/README.md) · not independently verified here
- [Uniform computation of the squared-logarithmic k-server bound](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026/README.md) · not independently verified here

#### 111. One-sample matroid prophet inequalities against an almighty adversary.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/111.md)
- [One Sample Suffices for Matroid Prophet Inequalities against an Almighty Adversary](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/final.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/README.md) · not independently verified here

#### 112. Beyond the square-root exponent for depth-three circuits.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/112.md)
- [Beyond the Square-Root Exponent for Depth-Three Boolean Circuits](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 113. Approximate counting and entropy of perfect matchings.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/113.md)
- [A Fully Polynomial Randomized Approximation Scheme for Perfect Matchings in General Graphs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/README.md) · not independently verified here
- [Entropy and Face Dimension of the Perfect-Matching Polytope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 114. Approximate counting of common integer polymatroid bases.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/114.md)
- [An FPRAS for Common Integer Polymatroid Bases with Binary Capacities](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/polymatroid-fpras.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/README.md) · not independently verified here
- [Approximate counting of common bases of two matroids](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Approximate-counting-of-common-bases-of-two-matroids-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 115. Sampling and counting contingency tables with arbitrary margins.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/115.md)
- [Exact Uniform Sampling of Contingency Tables with Arbitrary Margins](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/README.md) · not independently verified here
- [An FPRAS for Cell-Bounded Contingency Tables](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/README.md) · not independently verified here

#### 116. Uniform black-box noncommutative identity testing across characteristics.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/116.md)
- [Uniform Matrix Hitting Points in Every Positive Characteristic](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/uniform-matrix-hitting-points-positive-characteristic.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/README.md) · not independently verified here
- [One Rational Matrix Hitting Point for Noncommutative Formulas](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/README.md) · not independently verified here
- [Polynomial Hitting Lists for Noncommutative Rational Formulas](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 117. Uniform sparsest cut: hardness and semidefinite gaps.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/117.md)
- [Constant-factor hardness of uniform sparsest cut](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/README.md) · not independently verified here
- [Near-square-root logarithmic integrality gaps for uniform sparsest cut](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 118. Bin packing and unbounded configuration-LP gaps.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/118.md)
- [Additive hardness and unbounded configuration gaps in bin packing](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 119. The Courtade–Kumar and Hellinger conjectures.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/119.md)
- [Sharp binary-information contraction on the discrete cube](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/README.md) · manifest paper-source listed; not independently verified here
- [Hellinger contraction with arbitrary Boolean output bias](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/README.md) · not independently verified here

#### 120. Almost-linear-time exact matching and prescribed-degree factors in general graphs.

- [Almost-Linear-Time Maximum-Cardinality Matching in General Graphs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/README.md) · not independently verified here

#### 121. Almost-linear approximation of edit distance.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/121.md)
- [An Almost-Linear Approximation Scheme for Edit Distance](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/README.md) · not independently verified here

#### 122. Quantitative trace-reconstruction bounds with a uniform decoder.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/122.md)
- [Uniform quasipolynomial-time trace reconstruction](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/uniform-trace-reconstruction.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/README.md) · not independently verified here
- [A latest-anchor induction with spectrally compact masks for worst-case trace reconstruction](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026/README.md) · not independently verified here
- [Quantitative lower bounds for trace reconstruction](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/README.md) · not independently verified here

#### 124. Polynomial-time scheduling on three identical machines.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/124.md)
- [A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/README.md) · not independently verified here

#### 125. The metric k-median approximation threshold and recovery.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/125.md)
- [Single-exponential recovery and bounded-price strictness for metric k-median](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/README.md) · manifest paper-source listed; not independently verified here
- [The approximation threshold for metric k-median](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/README.md) · not independently verified here

#### 126. Exponential semidefinite complexity of perfect matching.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/126.md)
- [Exponential PSD rank of positively shifted matching matrices](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/shifted-matching-psd.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/README.md) · not independently verified here

#### 127. Average sensitivity of polynomial threshold functions.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/127.md)
- [Average sensitivity of polynomial threshold functions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 128. A factor-two approximation for shortest common superstring.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/128.md)
- [A Polynomial-Time 2-Approximation for Shortest Common Superstring](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 129. Exponential state costs for two-way automata.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/129.md)
- [An exponential state lower bound for two-way nondeterministic complementation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/README.md) · manifest paper-source listed; not independently verified here
- [An exponential two-way deterministic state lower bound for one-way liveness](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 130. Exact Fourier transforms below $n\log n$.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/130.md)
- [An explicit power saving for the exact discrete Fourier transform](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/README.md) · manifest paper-source listed; not independently verified here
- [Finite tensor savings and exact Fourier circuits](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 131. Rapid mixing of graph switches for every degree sequence.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/131.md)
- [Polynomial mixing of the switch chain for every graphical degree sequence](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Polynomial-Mixing-of-the-Switch-Chain-for-Every-Graphical-Degree-Sequence-September-25-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Polynomial-Mixing-of-the-Switch-Chain-for-Every-Graphical-Degree-Sequence-September-25-2026/README.md) · not independently verified here

#### 132. A superquadratic separation of sensitivity and block sensitivity.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/132.md)
- [A superquadratic separation between sensitivity and block sensitivity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 133. The computational complexity of Weisfeiler–Leman refinement.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/133.md)
- [Parity lifts and bounded-treewidth witnesses for Weisfeiler–Leman equivalence](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/README.md) · not independently verified here
- [The complexity of identifying a graph by Weisfeiler–Leman refinement](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/README.md) · not independently verified here
- [Unconditional time lower bounds for Weisfeiler–Leman equivalence](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/README.md) · not independently verified here
- [Variable-dimension Weisfeiler–Leman equivalence on general and subcubic graphs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/README.md) · not independently verified here

#### 134. Generalized star height at most three.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/134.md)
- [Finite Monoid Computations and a Uniform Generalized Star-Height Bound](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/README.md) · not independently verified here
- [Generalized Star Height at Most Four](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/Generalized-Star-Height-at-Most-Four-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/README.md) · not independently verified here
- [Generalized Star Height at Most Three](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/README.md) · not independently verified here

#### 135. Homogeneous depth-five lower bounds for iterated matrix multiplication.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/135.md)
- [Homogeneous depth-five lower bounds for iterated matrix multiplication](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/README.md) · not independently verified here

#### 136. A quasilinear PCP theorem for PPAD.

- [The PCP-for-PPAD conjecture: a quasilinear reduction](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/README.md) · not independently verified here

#### 137. One-tape time simulation in two-fifths-power space.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/137.md)
- [Simulating One-Tape Time in Two-Fifths-Power Space](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 138. Subset Sum in $O(2^{0.49n})$ time.

- [Subset Sum in Time $O(2^{0.49n})$](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/subset-sum.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/README.md) · not independently verified here
- [A Low-Space Algorithm for Worst-Case Subset Sum](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/README.md) · not independently verified here

#### 139. Subpolynomial query complexity for log-concave sampling.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/139.md)
- [Subpolynomial query complexity for well-conditioned log-concave sampling](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/README.md) · manifest paper-source listed; not independently verified here

#### 140. Memory–sample lower bounds for noiseless Gaussian regression.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/140.md)
- [Memory and precision in noiseless Gaussian regression](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/README.md) · manifest paper-source listed; not independently verified here
- [Posterior replicas and conditional information in Gaussian regression](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Posterior-replicas-and-conditional-information-in-Gaussian-regression-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Posterior-replicas-and-conditional-information-in-Gaussian-regression-September-27-2026/README.md) · manifest paper-source listed; not independently verified here
- [Localization costs and information growth for exact Gaussian observations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Localization-costs-and-information-growth-for-exact-Gaussian-observations-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Localization-costs-and-information-growth-for-exact-Gaussian-observations-September-27-2026/README.md) · not independently verified here
- [Projection moments, positive cap domination, and Riesz estimates on the sphere](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Projection-moments-positive-cap-domination-and-Riesz-estimates-on-the-sphere-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Projection-moments-positive-cap-domination-and-Riesz-estimates-on-the-sphere-September-27-2026/README.md) · manifest paper-source listed; not independently verified here
- [Replacing Gaussian observations in memory-constrained inference](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Replacing-Gaussian-observations-in-memory-constrained-inference-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Replacing-Gaussian-observations-in-memory-constrained-inference-September-27-2026/README.md) · manifest paper-source listed; not independently verified here
- [Subsphere methods for memory-sample lower bounds in noiseless Gaussian regression](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Subsphere-methods-for-memory-sample-lower-bounds-in-noiseless-Gaussian-regression-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Subsphere-methods-for-memory-sample-lower-bounds-in-noiseless-Gaussian-regression-September-27-2026/README.md) · manifest paper-source listed; not independently verified here

#### 141. Existential–universal real sentences in the counting hierarchy.

- [Existential–universal real sentences in the counting hierarchy](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Existential-universal-real-sentences-in-the-counting-hierarchy-October-4-2026/etr-counting-hierarchy.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Existential-universal-real-sentences-in-the-counting-hierarchy-October-4-2026/README.md) · not independently verified here

#### 142. Deterministic polynomial factorization over prime fields.

- [Deterministic Polynomial Factorization over Prime Fields](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/Deterministic-Polynomial-Factorization-over-Prime-Fields.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/README.md) · not independently verified here


### Dynamical systems and ergodic theory

#### 143. Hilbert's sixteenth problem: uniform bounds for limit cycles.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/143.md)
- [Uniform bounds for planar polynomial limit cycles](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/README.md) · not independently verified here
- [Two limit cycles for quintic Liénard systems](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/two-limit-cycles-for-quintic-lienard-systems-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 144. Banach’s simple Lebesgue-spectrum problem.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/144.md)
- [A smooth three-torus diffeomorphism with simple Lebesgue spectrum](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/README.md) · not independently verified here

#### 145. Rokhlin’s multiple-mixing problem.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/145.md)
- [Rokhlin's multiple-mixing problem for one transformation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/README.md) · not independently verified here

#### 146. Positive metric entropy for the standard map.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/146.md)
- [Positive Metric Entropy for the Standard Map at Large Parameters](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/README.md) · not independently verified here

#### 147. The near-boundary Birkhoff conjecture.

- [Continuous Phase Foliations Create Analytic Caustic Collars](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/README.md) · not independently verified here
- [Rigidity of Smooth Billiards with a Continuous Caustic Collar](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/README.md) · not independently verified here

#### 148. The entropy-rate dimension formula for self-similar measures.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/148.md)
- [The entropy-rate dimension formula for self-similar measures on the line](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 149. Classwise permanence for weakly reversible mass-action systems.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/149.md)
- [Uniform Permanence in Weakly Reversible Mass-Action Systems](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/permanence.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/README.md) · not independently verified here
- [Boundedness and persistence of weakly reversible mass-action systems](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026/README.md) · not independently verified here

#### 150. Weak mixing of triangular billiards with an irrational angle.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/150.md)
- [Weak mixing of triangular billiards with an irrational angle](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Weak-mixing-of-triangular-billiards-with-an-irrational-angle-October-5-2026/weak-mixing-triangular-billiards.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Weak-mixing-of-triangular-billiards-with-an-irrational-angle-October-5-2026/README.md) · not independently verified here
- [Ergodicity of triangular billiards with an irrational angle](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ergodicity-of-triangular-billiards-with-an-irrational-angle-September-25-2026/Ergodicity-of-triangular-billiards-with-an-irrational-angle-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ergodicity-of-triangular-billiards-with-an-irrational-angle-September-25-2026/README.md) · not independently verified here

#### 151. A C1 counterexample to the entropy conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/151.md)
- [A C^1 Counterexample to the Entropy Conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026/README.md) · not independently verified here

#### 152. Zero entropy does not guarantee a smooth positive-volume model.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/152.md)
- [A zero-entropy system without a smooth positive-volume model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026/README.md) · not independently verified here

#### 153. Arithmetic classification and non-Pisot singularity for Bernoulli convolutions.

- [Arithmetic classification and non-Pisot singularity for Bernoulli convolutions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Arithmetic-classification-and-non-Pisot-singularity-for-Bernoulli-convolutions-October-3-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Arithmetic-classification-and-non-Pisot-singularity-for-Bernoulli-convolutions-October-3-2026/README.md) · not independently verified here

#### 154. Pointwise multiple ergodic averages for mixing transformations.

- [Pointwise Multiple Ergodic Averages for Mixing Transformations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/multiple-ergodic-averages.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/README.md) · not independently verified here
- [Pointwise convergence of fourfold ergodic averages for mixing transformations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Pointwise-convergence-of-fourfold-ergodic-averages-for-mixing-transformations-October-4-2026/fourfold-ergodic-averages.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Pointwise-convergence-of-fourfold-ergodic-averages-for-mixing-transformations-October-4-2026/README.md) · not independently verified here
- [Triple ergodic averages with distinct integer slopes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026/triple-ergodic-distinct-slopes.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026/README.md) · not independently verified here
- [Pointwise convergence of triple ergodic averages for mixing transformations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026/pointwise-triple-ergodic-averages-mixing-transformations.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Pointwise-convergence-of-triple-ergodic-averages-for-mixing-transformations-October-4-2026/README.md) · not independently verified here


### Combinatorics

#### 155. A counterexample to periodic tiling in dimension three.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/155.md)
- [A translational tile with no fully periodic tiling in dimension three](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 156. Borsuk's conjecture fails in dimension nine.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/156.md)
- [A nine-dimensional counterexample to Borsuk's covering assertion](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 157. Graph coloring, clique minors, and Colin de Verdière invariants.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/157.md)
- [A counterexample to Hadwiger's conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [A counterexample to the Colin de Verdière chromatic conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/README.md) · not independently verified here
- [A linear list-coloring bound in terms of the Hadwiger number](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/README.md) · not independently verified here

#### 158. The Euclidean plane cannot be colored with five colors.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/158.md)
- [The Euclidean plane is not five-colorable](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 159. Erdős’s reciprocal-sum conjecture and quasipolynomial Szemerédi bounds.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/159.md)
- [Quasipolynomial Bounds for Arithmetic Progressions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/README.md) · not independently verified here

#### 160. Superexponential van der Waerden numbers.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/160.md)
- [Quantitative Superexponential Bounds for van der Waerden Numbers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 161. Counterexamples to Sidorenko’s conjecture and the forcing conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/161.md)
- [A counterexample to Sidorenko's conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/README.md) · not independently verified here

#### 162. Counterexamples to Ryser’s covering conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/162.md)
- [Balanced counterexamples to Ryser's conjecture at prime orders](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/README.md) · not independently verified here
- [A counterexample to Ryser's covering conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 164. Hindman’s finite sums and products conjecture.

- [Monochromatic finite sums and products in the positive integers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/README.md) · not independently verified here

#### 165. The Harary–Hill and Zarankiewicz crossing-number formulas.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/165.md)
- [The crossing number of complete graphs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-crossing-number-of-complete-graphs-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-crossing-number-of-complete-graphs-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [The crossing number of complete bipartite graphs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 166. The higher-dimensional Erdős distinct-distances conjecture.

- [The higher-dimensional Erdős distinct-distances conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/README.md) · not independently verified here

#### 167. Planar distinct distances and unit-distance bounds.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/167.md)
- [The weak pinned planar distance theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [A power saving for planar unit distances](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-power-saving-for-planar-unit-distances-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-power-saving-for-planar-unit-distances-September-23-2026/README.md) · not independently verified here

#### 168. Combinatorial invariance of Kazhdan–Lusztig polynomials.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/168.md)
- [Combinatorial invariance of Kazhdan–Lusztig polynomials](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/README.md) · not independently verified here

#### 169. Shareshian–Wachs elementary positivity.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/169.md)
- [Elementary positivity of chromatic quasisymmetric functions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/README.md) · not independently verified here

#### 170. Sharp logarithmic exponents for off-diagonal Ramsey numbers.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/170.md)
- [The sharp logarithmic exponent of r(5,t)](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Sharp-Logarithmic-Exponent-of-r-5-t-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Sharp-Logarithmic-Exponent-of-r-5-t-September-24-2026/README.md) · not independently verified here
- [Sharp logarithmic exponents for fixed off-diagonal Ramsey numbers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-Logarithmic-Exponents-for-Fixed-Off-Diagonal-Ramsey-Numbers-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-Logarithmic-Exponents-for-Fixed-Off-Diagonal-Ramsey-Numbers-September-24-2026/README.md) · not independently verified here

#### 171. The hypercube Ramsey conjecture.

- [The hypercube Ramsey number has linear order](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/README.md) · not independently verified here

#### 172. Classification of finite Euclidean Ramsey configurations.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/172.md)
- [A classification of finite Euclidean Ramsey configurations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 173. Seymour’s second-neighborhood conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/173.md)
- [A proof of Seymour’s second-neighborhood conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 174. Deterministic construction of strong thin spanning trees.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/174.md)
- [The strong thin tree conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-strong-thin-tree-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-strong-thin-tree-conjecture-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [A polynomial-time construction of strong thin trees](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-polynomial-time-construction-of-strong-thin-trees-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-polynomial-time-construction-of-strong-thin-trees-September-23-2026/README.md) · not independently verified here

#### 175. Talagrand’s expectation thresholds, discrete convexity, and graph decompositions.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/175.md)
- [Graph Decompositions at the Integral Expectation Threshold](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026/graph-threshold-decompositions.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026/README.md) · not independently verified here
- [Integral and fractional expectation thresholds are equivalent](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [Talagrand’s discrete-convexity conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 176. The second Kahn–Kalai conjecture with an edge-count bound.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/176.md)
- [The second Kahn–Kalai conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 177. Bounded-degree coboundary expanders.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/177.md)
- [Bounded-degree coboundary expanders in every dimension](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-degree-coboundary-expanders-in-every-dimension-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-degree-coboundary-expanders-in-every-dimension-September-24-2026/README.md) · not independently verified here

#### 178. Deterministic nonbipartite Ramanujan graphs in every fixed degree.

- [Deterministic nonbipartite Ramanujan graphs in every fixed degree](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Deterministic-nonbipartite-Ramanujan-graphs-in-every-fixed-degree-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Deterministic-nonbipartite-Ramanujan-graphs-in-every-fixed-degree-September-23-2026/README.md) · not independently verified here

#### 179. The circulant Hadamard and Barker-sequence conjectures.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/179.md)
- [The circulant Hadamard conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-circulant-Hadamard-conjecture-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 180. Barnette’s Hamiltonian-cycle conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/180.md)
- [Paired states and Hamiltonian cycles in cubic bipartite planar graphs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Paired-states-and-Hamiltonian-cycles-in-cubic-bipartite-planar-graphs-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Paired-states-and-Hamiltonian-cycles-in-cubic-bipartite-planar-graphs-September-24-2026/README.md) · not independently verified here

#### 181. The Erdős–Gallai cycle-decomposition conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/181.md)
- [A linear cycle-and-edge decomposition of every graph](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 182. Power savings for intersective polynomial differences and prime arguments.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/182.md)
- [A power saving for intersective polynomial differences with an exponent depending only on the degree](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/power-saving-intersective-polynomial-differences.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/README.md) · not independently verified here
- [A Power Saving for Polynomial Differences at Prime Arguments](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/prime-argument-polynomial-differences.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/README.md) · not independently verified here
- [A power saving for square-difference-free sets](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/README.md) · not independently verified here

#### 183. Power savings for planar halving lines and k-sets.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/183.md)
- [A power saving for planar halving lines](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-power-saving-for-planar-halving-lines-September-25-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-power-saving-for-planar-halving-lines-September-25-2026/README.md) · not independently verified here

#### 184. Correspondence coloring with a fixed forbidden subgraph.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/184.md)
- [Correspondence coloring graphs with a forbidden clique](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/correspondence-coloring-forbidden-clique.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/README.md) · not independently verified here
- [A logarithmic independence bound for clique-free graphs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 185. Counterexamples to infinite matroid intersection and packing/covering.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/185.md)
- [A Counterexample to the Infinite Matroid Packing/Covering Conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 186. Uniform influence and sharp thresholds for graph and hypergraph properties.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/186.md)
- [A uniform influence bound for hypergraph properties](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/hypergraph-influences.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/README.md) · not independently verified here
- [A Sharp Threshold Bound for Monotone Graph Properties](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/README.md) · not independently verified here

#### 187. Snaky in 21 Maker moves.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/187.md)
- [Snaky in 21 Maker moves](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Snaky-in-21-Maker-moves-September-25-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Snaky-in-21-Maker-moves-September-25-2026/README.md) · not independently verified here

#### 188. The sharp terminal leave in random triangle removal.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/188.md)
- [The sharp terminal leave in random triangle removal](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026/README.md) · not independently verified here

#### 189. Cycle–clique Ramsey numbers.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/189.md)
- [Cycle--clique Ramsey numbers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cycle-clique-Ramsey-numbers-September-25-2026/Cycle-clique-Ramsey-numbers-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cycle-clique-Ramsey-numbers-September-25-2026/README.md) · not independently verified here

#### 190. Polynomial removal fails for ordered binary matrices.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/190.md)
- [Polynomial removal fails for ordered binary matrices](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 191. A power improvement in the Heilbronn triangle lower bound.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/191.md)
- [A power improvement in the Heilbronn triangle lower bound](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026/README.md) · not independently verified here

#### 192. Boolean functions violate the square-root degree bound by arbitrary factors.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/192.md)
- [Unbounded Violations of the Square-Root Degree Bound](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/README.md) · not independently verified here


### Algebra

#### 193. Serre’s intersection-multiplicity conjecture.

- [Positivity of Serre's Intersection Multiplicity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positivity-of-Serres-Intersection-Multiplicity-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positivity-of-Serres-Intersection-Multiplicity-September-23-2026/README.md) · not independently verified here

#### 194. Lech’s multiplicity conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/194.md)
- [Lech's multiplicity conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Lechs-multiplicity-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Lechs-multiplicity-conjecture-September-23-2026/README.md) · not independently verified here

#### 195. A counterexample to the small Cohen–Macaulay module conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/195.md)
- [A Complete Local Domain without a Small Cohen–Macaulay Module](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 196. A counterexample to Kaplansky’s zero-divisor conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/196.md)
- [A Torsion-Free Group Algebra with Zero Divisors](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 197. A torsion-free group algebra that is not directly finite.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/197.md)
- [A Torsion-Free Group Algebra That Is Not Directly Finite](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Torsion-Free-Group-Algebra-That-Is-Not-Directly-Finite-October-4-2026/direct-finiteness.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Torsion-Free-Group-Algebra-That-Is-Not-Directly-Finite-October-4-2026/README.md) · not independently verified here
- [A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [A Counterexample to the Group-Ring Determinant Conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Odd Characteristic](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/README.md) · manifest paper-source listed; not independently verified here

#### 198. A counterexample to finitistic-dimension finiteness.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/198.md)
- [An algebra of infinite little finitistic dimension](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 199. Counterexamples to Auslander–Reiten, Tachikawa and related homological conjectures.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/199.md)
- [An explicit counterexample to the Auslander-Reiten conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [A counterexample to Tachikawa's second conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 200. Eisenbud–Green–Harris and lex-plus-powers.

- [The Artinian Lex-Plus-Powers Betti Theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Artinian-Lex-Plus-Powers-Betti-Theorem-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Artinian-Lex-Plus-Powers-Betti-Theorem-September-23-2026/README.md) · not independently verified here
- [Commuting Division-Coefficient Forms and the Artinian Eisenbud--Green--Harris Conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Commuting-Division-Coefficient-Forms-and-the-Artinian-Eisenbud-Green-Harris-Conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Commuting-Division-Coefficient-Forms-and-the-Artinian-Eisenbud-Green-Harris-Conjecture-September-23-2026/README.md) · not independently verified here

#### 201. A counterexample to Kurosh’s division-ring problem.

- [A Counterexample to Kurosh’s Division-Ring Problem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-Kuroshs-Division-Ring-Problem-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-Kuroshs-Division-Ring-Problem-September-23-2026/README.md) · not independently verified here

#### 202. The blockwise Alperin weight conjecture.

- [The Blockwise Alperin Weight Conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/README.md) · not independently verified here

#### 203. Donovan's conjecture over fields and complete mixed-characteristic DVRs.

- [Donovan's Conjecture over Algebraically Closed Fields](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/README.md) · not independently verified here
- [Integral Donovan Finiteness over Witt Vectors](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/README.md) · not independently verified here

#### 204. Tensor saturation for even spin groups.

- [Tensor saturation for even spin groups](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Tensor-Saturation-for-Even-Spin-Groups-September-24-2026/README.md) · not independently verified here

#### 205. Saxl’s conjecture and universal tensor squares.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/205.md)
- [Universal Tensor Squares for Symmetric Groups](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/README.md) · not independently verified here
- [A Cyclic Polytabloid Proof of Saxl's Conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 206. Finite lattice representation and undecidability.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/206.md)
- [Finite congruence lattices: characterization and undecidability](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026/README.md) · not independently verified here
- [A negative solution to the finite lattice representation problem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Negative-Solution-to-the-Finite-Lattice-Representation-Problem-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Negative-Solution-to-the-Finite-Lattice-Representation-Problem-September-24-2026/README.md) · not independently verified here

#### 207. The ℓ¹-Bass conjecture for all discrete groups.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/207.md)
- [The ℓ¹-Bass Conjecture for Discrete Groups](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-l1-Bass-Conjecture-for-Discrete-Groups-October-5-2026/l1-bass-conjecture.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-l1-Bass-Conjecture-for-Discrete-Groups-October-5-2026/README.md) · not independently verified here
- [The Bass trace conjecture and the characteristic-zero Kaplansky idempotent conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 208. Finite symmetric tensor categories and the Verlinde tower.

- [Fiber functors for finite symmetric tensor categories in positive characteristic](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026/README.md) · not independently verified here

#### 209. Integral counterexamples to Gersten’s conjecture.

- [An integral counterexample to Gersten's conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026/README.md) · not independently verified here
- [An integral degree-three Gersten counterexample](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/README.md) · not independently verified here

#### 210. Foulkes' conjecture for sixth powers and quadratic stabilization.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/210.md)
- [Foulkes' conjecture for the sixth symmetric power](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/README.md) · not independently verified here
- [Quadratic stabilization of the canonical Foulkes--Howe map](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/README.md) · manifest paper-source listed; not independently verified here


### Probability and statistical mechanics

#### 211. The geometric phase diagram, diffusion, and spectra of random planar maps.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/211.md)
- [Random Walks on Critical FK–Ising Maps and Liouville Brownian Motion](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Random-Walks-on-Critical-FK-Ising-Maps-and-Liouville-Brownian-Motion-October-5-2026/fk-ising-walk-limit.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Random-Walks-on-Critical-FK-Ising-Maps-and-Liouville-Brownian-Motion-October-5-2026/README.md) · not independently verified here
- [Spectral convergence for critical FK–Ising planar maps](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Spectral-convergence-for-critical-FK-Ising-planar-maps-October-5-2026/spectral-convergence-critical-fk-ising-planar-maps.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Spectral-convergence-for-critical-FK-Ising-planar-maps-October-5-2026/README.md) · not independently verified here
- [A Linear Clock for Random Walk on Tree-Weighted Planar Maps](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Linear-Clock-for-Random-Walk-on-Tree-Weighted-Planar-Maps-October-5-2026/linear-clock-random-walk-tree-weighted-planar-maps.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Linear-Clock-for-Random-Walk-on-Tree-Weighted-Planar-Maps-October-5-2026/README.md) · not independently verified here
- [Canonical conformal limits of subcritical FK planar maps](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Canonical-conformal-limits-of-subcritical-FK-planar-maps-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Canonical-conformal-limits-of-subcritical-FK-planar-maps-September-24-2026/README.md) · not independently verified here
- [The critical Liouville quantum sphere and geometric limits of FK maps at q=4](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-critical-Liouville-quantum-sphere-and-geometric-limits-of-FK-maps-at-q-equals-4-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-critical-Liouville-quantum-sphere-and-geometric-limits-of-FK-maps-at-q-equals-4-September-24-2026/README.md) · not independently verified here
- [Metric-measure limits of subcritical FK and spanning-tree planar maps](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/README.md) · not independently verified here
- [Brownian continuum random tree limits of finite Fortuin–Kasteleyn maps above four](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Brownian-continuum-random-tree-limits-of-finite-Fortuin-Kasteleyn-maps-above-four-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Brownian-continuum-random-tree-limits-of-finite-Fortuin-Kasteleyn-maps-above-four-September-24-2026/README.md) · not independently verified here

#### 212. Planar first-passage geometry and the absence of bigeodesics.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/212.md)
- [No bigeodesics in planar first-passage percolation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/README.md) · not independently verified here
- [Strict convexity and differentiability of the planar exponential first-passage limit shape](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 213. Critical percolation on every quasi-transitive graph.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/213.md)
- [Critical bond and site percolation on the cubic lattice](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/README.md) · manifest paper-source listed; not independently verified here
- [No percolation at criticality on quasi-transitive graphs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/README.md) · not independently verified here

#### 214. The Benjamini–Schramm nonuniqueness conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/214.md)
- [Nonuniqueness of percolation on nonamenable quasi-transitive graphs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/README.md) · not independently verified here

#### 215. Canonical $O(3)$ continuum limit and exact $O(4)$ mass asymptotics.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/215.md)
- [The canonical massive continuum limit of the two-dimensional O(3) model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-canonical-massive-continuum-limit-of-the-two-dimensional-O3-model-October-4-2026/massive-continuum-o3.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-canonical-massive-continuum-limit-of-the-two-dimensional-O3-model-October-4-2026/README.md) · not independently verified here
- [An Isolated Particle Pole for the Two-Dimensional O(3) Spin Field](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Isolated-Particle-Pole-for-the-Two-Dimensional-O3-Spin-Field-October-4-2026/o3-particle-pole.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Isolated-Particle-Pole-for-the-Two-Dimensional-O3-Spin-Field-October-4-2026/README.md) · not independently verified here
- [Exact mass asymptotics for the two-dimensional O(4) lattice model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-mass-asymptotics-for-the-two-dimensional-O4-lattice-model-October-5-2026/exact-mass-o4.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-mass-asymptotics-for-the-two-dimensional-O4-lattice-model-October-5-2026/README.md) · not independently verified here
- [Sharp mass bounds for the two-dimensional O(4) model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/README.md) · not independently verified here
- [Exponential decay in two-dimensional classical O(n) models](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 216. Critical and near-critical XY scaling and BKT universality.

- [The critical logarithmic correction for the planar XY model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-critical-logarithmic-correction-for-the-planar-XY-model-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-critical-logarithmic-correction-for-the-planar-XY-model-October-5-2026/README.md) · not independently verified here
- [Critical Center Magnetization in the Planar XY Model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Critical-Center-Magnetization-in-the-Planar-XY-Model-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Critical-Center-Magnetization-in-the-Planar-XY-Model-October-5-2026/README.md) · not independently verified here
- [The Critical Spin Field of the Planar XY Model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Critical-Spin-Field-of-the-Planar-XY-Model-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Critical-Spin-Field-of-the-Planar-XY-Model-October-5-2026/README.md) · not independently verified here
- [Essential Singularity of the Correlation Length in the Planar XY Model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Essential-Singularity-of-the-Correlation-Length-in-the-Planar-XY-Model-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Essential-Singularity-of-the-Correlation-Length-in-the-Planar-XY-Model-October-5-2026/README.md) · not independently verified here
- [The critical correlation exponent of the planar XY model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-critical-correlation-exponent-of-the-planar-XY-model-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-critical-correlation-exponent-of-the-planar-XY-model-September-24-2026/README.md) · not independently verified here
- [BKT universality for height and planar spin fields](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/BKT-universality-for-height-and-planar-spin-fields-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/BKT-universality-for-height-and-planar-spin-fields-September-24-2026/README.md) · not independently verified here

#### 217. The low-temperature Sherrington–Kirkpatrick fluctuation law.

- [The low-temperature Sherrington–Kirkpatrick free-energy limiting law](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/README.md) · not independently verified here
- [The low-temperature Sherrington–Kirkpatrick fluctuation scale](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026/README.md) · not independently verified here

#### 218. Conformal universality for weakly interacting and random-bond Ising models.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/218.md)
- [Quenched SLE₃ limits for general weak random-bond Ising models](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quenched-SLE3-limits-for-general-weak-random-bond-Ising-models-October-5-2026/general-weak-random-bond-ising.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quenched-SLE3-limits-for-general-weak-random-bond-Ising-models-October-5-2026/README.md) · not independently verified here
- [Quenched SLE₃ Universality for the Weak Random-Bond Ising Model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quenched-SLE3-Universality-for-the-Weak-Random-Bond-Ising-Model-October-5-2026/quenched-sle3-weak-random-bond-ising.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quenched-SLE3-Universality-for-the-Weak-Random-Bond-Ising-Model-October-5-2026/README.md) · not independently verified here
- [Logarithmic Relative Fluctuations in the Weakly Disordered Planar Ising Model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Logarithmic-Relative-Fluctuations-in-the-Weakly-Disordered-Planar-Ising-Model-October-5-2026/critical-relative-second-moment-weak-random-bond-ising.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Logarithmic-Relative-Fluctuations-in-the-Weakly-Disordered-Planar-Ising-Model-October-5-2026/README.md) · not independently verified here
- [Conformal universality of bulk Ising correlations under weak interactions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/README.md) · not independently verified here
- [SLE3 universality for weak finite-range Ising interactions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/SLE3-universality-for-weak-finite-range-Ising-interactions-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/SLE3-universality-for-weak-finite-range-Ising-interactions-September-23-2026/README.md) · not independently verified here
- [Buffered comparison and stopping-band resolution in critical Ising](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Buffered-comparison-and-stopping-band-resolution-in-critical-Ising-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Buffered-comparison-and-stopping-band-resolution-in-critical-Ising-September-23-2026/README.md) · not independently verified here

#### 219. GOE bulk universality for regular graphs with weak Anderson disorder.

- [Fixed-energy universality for weak Anderson disorder on random regular graphs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/fixed-energy-universality-weak-anderson-disorder-random-regular-graphs.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/README.md) · not independently verified here
- [GOE bulk universality for fixed-degree random regular graphs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/README.md) · not independently verified here

#### 220. Directional zero–one laws beyond iid environments and iid ballisticity.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/220.md)
- [A directional zero–one law for finite-range-dependent random environments](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/directional-zero-one-finite-range.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/README.md) · not independently verified here
- [A directional zero–one law under strict ellipticity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/README.md) · not independently verified here
- [Directional transience implies ballisticity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Directional-transience-implies-ballisticity-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 221. The Mézard–Parisi formula for diluted spin glasses.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/221.md)
- [The Mézard–Parisi formula for diluted spin glasses](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/README.md) · not independently verified here

#### 222. Perceptron free energies and microscopic jamming exponents.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/222.md)
- [The free energy of the Ising random perceptron](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-free-energy-of-the-Ising-random-perceptron-September-24-2026/The-free-energy-of-the-Ising-random-perceptron-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-free-energy-of-the-Ising-random-perceptron-September-24-2026/README.md) · not independently verified here
- [Microscopic jamming in the negative spherical perceptron](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026/README.md) · not independently verified here
- [The spherical perceptron with bi-orthogonally invariant disorder](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026/README.md) · not independently verified here
- [The free energy of the spherical random perceptron](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-free-energy-of-the-spherical-random-perceptron-September-24-2026/The-free-energy-of-the-spherical-random-perceptron-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-free-energy-of-the-spherical-random-perceptron-September-24-2026/README.md) · not independently verified here

#### 223. Random-cluster interfaces: critical, disordered, thermal, and natural-time scaling.

- [Square-lattice FK interfaces and nested loops for 1 <= q < 4](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Square-lattice-FK-interfaces-and-nested-loops-for-1-leq-q-lt-4-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Square-lattice-FK-interfaces-and-nested-loops-for-1-leq-q-lt-4-September-23-2026/README.md) · not independently verified here
- [Self-dual random-cluster interfaces below one](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Self-dual-random-cluster-interfaces-below-one-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Self-dual-random-cluster-interfaces-below-one-September-23-2026/README.md) · not independently verified here
- [Quenched SLE Universality for Weakly Disordered FK–Ising Interfaces](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quenched-SLE-Universality-for-Weakly-Disordered-FK-Ising-Interfaces-October-5-2026/quenched-fk-ising.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quenched-SLE-Universality-for-Weakly-Disordered-FK-Ising-Interfaces-October-5-2026/README.md) · not independently verified here
- [Thermal FK–Ising interfaces and massive SLE](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Thermal-FK-Ising-interfaces-and-massive-SLE-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Thermal-FK-Ising-interfaces-and-massive-SLE-October-5-2026/README.md) · not independently verified here
- [Natural Occupation Measures for Critical Square-Lattice FK Interfaces](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Natural-Occupation-Measures-for-Critical-Square-Lattice-FK-Interfaces-October-5-2026/natural-occupation-measures-critical-square-lattice-fk-interfaces.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Natural-Occupation-Measures-for-Critical-Square-Lattice-FK-Interfaces-October-5-2026/README.md) · not independently verified here
- [Conformal Limits of Critical Square-Lattice Random-Cluster Interfaces](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Conformal-Limits-of-Critical-Square-Lattice-Random-Cluster-Interfaces-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Conformal-Limits-of-Critical-Square-Lattice-Random-Cluster-Interfaces-October-5-2026/README.md) · not independently verified here

#### 224. Critical and quenched near-critical universality for Poisson–Voronoi percolation.

- [From critical crossings to quenched near-critical universality in Voronoi percolation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/From-critical-crossings-to-quenched-near-critical-universality-in-Voronoi-percolation-October-5-2026/critical-crossings-quenched-near-critical-universality-voronoi-percolation.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/From-critical-crossings-to-quenched-near-critical-universality-in-Voronoi-percolation-October-5-2026/README.md) · not independently verified here
- [A Pivotal Amplitude for Voronoi Percolation from Cardy's Formula](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Pivotal-Amplitude-for-Voronoi-Percolation-from-Cardys-Formula-October-5-2026/voronoi-pivotal-amplitude.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Pivotal-Amplitude-for-Voronoi-Percolation-from-Cardys-Formula-October-5-2026/README.md) · not independently verified here
- [Cardy’s formula for critical Poisson–Voronoi percolation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cardys-formula-for-critical-Poisson-Voronoi-percolation-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cardys-formula-for-critical-Poisson-Voronoi-percolation-September-23-2026/README.md) · not independently verified here

#### 225. Gaussian free field limits throughout the balanced six-vertex regime.

- [The Gaussian free field limit of the balanced six-vertex model with variance multiplier 1/arcsin(c/2)](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026/README.md) · not independently verified here

#### 226. The double-dimer loop ensemble converges to CLE4.

- [The curve scaling limit of half-plane double dimers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/README.md) · not independently verified here

#### 227. Critical SK autocorrelation processes and dynamics across the temperature transition.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/227.md)
- [Universality of critical quench autocorrelations in the Sherrington–Kirkpatrick model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Universality-of-critical-quench-autocorrelations-in-the-Sherrington-Kirkpatrick-model-October-5-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Universality-of-critical-quench-autocorrelations-in-the-Sherrington-Kirkpatrick-model-October-5-2026/README.md) · not independently verified here
- [Functional universality of critical SK autocorrelations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Functional-universality-of-critical-SK-autocorrelations-October-5-2026/critical-sk-autocorrelations.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Functional-universality-of-critical-SK-autocorrelations-October-5-2026/README.md) · not independently verified here
- [A spectral gap throughout the high-temperature Sherrington–Kirkpatrick phase](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-spectral-gap-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-spectral-gap-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/README.md) · not independently verified here
- [Cutoff throughout the high-temperature Sherrington–Kirkpatrick phase](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cutoff-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cutoff-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/README.md) · not independently verified here
- [Critical slowing down in the Sherrington–Kirkpatrick model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Critical-slowing-down-in-the-Sherrington-Kirkpatrick-model-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Critical-slowing-down-in-the-Sherrington-Kirkpatrick-model-September-24-2026/README.md) · manifest paper-source listed; not independently verified here
- [Stretched-exponential barriers for typical SK initial states](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Stretched-exponential-barriers-for-typical-SK-initial-states-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Stretched-exponential-barriers-for-typical-SK-initial-states-September-24-2026/README.md) · not independently verified here
- [A typical-start upper bound for low-temperature SK Glauber dynamics](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026/README.md) · not independently verified here
- [Critical mixing in the Sherrington–Kirkpatrick model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Critical-mixing-in-the-Sherrington-Kirkpatrick-model-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Critical-mixing-in-the-Sherrington-Kirkpatrick-model-September-25-2026/README.md) · not independently verified here

#### 228. Continuum phase transitions for radial pair potentials.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/228.md)
- [A continuum temperature singularity for a radial pair potential](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-continuum-temperature-singularity-for-a-radial-pair-potential-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-continuum-temperature-singularity-for-a-radial-pair-potential-September-24-2026/README.md) · manifest paper-source listed; not independently verified here
- [A radial continuum phase transition with algebraic decay](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-radial-continuum-phase-transition-with-algebraic-decay-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-radial-continuum-phase-transition-with-algebraic-decay-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 229. Exact three- and four-state reconstruction thresholds and four-state tree capacity.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/229.md)
- [The Reconstruction Threshold for the Ferromagnetic Four-State Potts Model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/four-state-potts.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/README.md) · not independently verified here
- [A Capacity Criterion for Four-State Potts Reconstruction on Trees](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/four-state-capacity.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/README.md) · not independently verified here
- [The exact reconstruction threshold for the three-state symmetric channel](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/README.md) · not independently verified here

#### 230. Exact Hausdorff gauges for SLE.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/230.md)
- [An exact Hausdorff gauge for SLE](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-exact-Hausdorff-gauge-for-SLE-September-25-2026/An-exact-Hausdorff-gauge-for-SLE-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-exact-Hausdorff-gauge-for-SLE-September-25-2026/README.md) · not independently verified here
- [An explicit exact Hausdorff gauge for SLE](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026/An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026/README.md) · not independently verified here

#### 231. The free uniform spanning forest is a factor of IID.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/231.md)
- [The free uniform spanning forest is a factor of IID](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026/README.md) · not independently verified here

#### 232. Gaussian fields and interfaces for triangular-lattice Lipschitz heights.

- [Gaussian free-field limits of weighted integer Lipschitz heights](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Gaussian-free-field-limits-of-weighted-integer-Lipschitz-heights-October-6-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Gaussian-free-field-limits-of-weighted-integer-Lipschitz-heights-October-6-2026/README.md) · proof_statement_hypothesis_or_citation_correction; not independently verified here
- [The Gaussian free field limit of integer Lipschitz heights with two-arc boundary data](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-October-6-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-October-6-2026/README.md) · proof_statement_hypothesis_or_citation_correction; not independently verified here
- [Uniform real Lipschitz surfaces on the triangular lattice](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-October-6-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-October-6-2026/README.md) · proof_statement_hypothesis_or_citation_correction; not independently verified here

#### 233. The joint critical Ashkin–Teller current limit.

- [The joint scaling limit of critical Ashkin-Teller currents](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-joint-scaling-limit-of-critical-Ashkin-Teller-currents-October-6-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-joint-scaling-limit-of-critical-Ashkin-Teller-currents-October-6-2026/README.md) · proof_statement_hypothesis_or_citation_correction; not independently verified here

#### 234. All-temperature pressure of orthogonally invariant Ising spin glasses.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/234.md)
- [All-temperature pressure for orthogonally invariant Ising spin glasses](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/README.md) · not independently verified here

#### 235. Limiting random SAT thresholds, sharp variance and computability.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/235.md)
- [A Limiting Satisfiability Threshold for Every Fixed Clause Size](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/README.md) · not independently verified here
- [Linear Variance of the Random 3-SAT Hitting Time](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/linear-variance-of-the-random-3-sat-hitting-time.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/README.md) · not independently verified here
- [Variance of the Random k-SAT Hitting Time](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026/README.md) · not independently verified here
- [Computing the Random 3-SAT Threshold](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/README.md) · not independently verified here

#### 236. The exact factor-of-IID threshold for free Ising spins on trees.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/236.md)
- [The sharp factor-of-IID threshold for the free Ising model on regular trees](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/README.md) · manifest paper-source listed; not independently verified here

#### 237. The three-quarter exponent for honeycomb self-avoiding walk.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/237.md)
- [Radial transfer estimates and polygon length laws for honeycomb walks](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Radial-transfer-estimates-and-polygon-length-laws-for-honeycomb-walks-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Radial-transfer-estimates-and-polygon-length-laws-for-honeycomb-walks-September-26-2026/README.md) · not independently verified here
- [Critical honeycomb chords with prescribed boundary endpoints](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Critical-honeycomb-chords-with-prescribed-boundary-endpoints-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Critical-honeycomb-chords-with-prescribed-boundary-endpoints-September-26-2026/README.md) · manifest paper-source listed; not independently verified here
- [Cylinder loop weights and planar nesting](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cylinder-loop-weights-and-planar-nesting-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cylinder-loop-weights-and-planar-nesting-September-26-2026/README.md) · not independently verified here
- [Mass and covering exponents for fixed-length honeycomb walks](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Mass-and-covering-exponents-for-fixed-length-honeycomb-walks-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Mass-and-covering-exponents-for-fixed-length-honeycomb-walks-September-26-2026/README.md) · not independently verified here
- [Signed cylinder propagation and marked polygons on the honeycomb lattice](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Signed-cylinder-propagation-and-marked-polygons-on-the-honeycomb-lattice-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Signed-cylinder-propagation-and-marked-polygons-on-the-honeycomb-lattice-September-26-2026/README.md) · not independently verified here
- [Cylinder amplitudes and logarithmic bridge-length windows on the honeycomb lattice](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cylinder-amplitudes-and-logarithmic-bridge-length-windows-on-the-honeycomb-lattice-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cylinder-amplitudes-and-logarithmic-bridge-length-windows-on-the-honeycomb-lattice-September-26-2026/README.md) · not independently verified here
- [Marked polygon correlations and one-arc bounds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Marked-polygon-correlations-and-one-arc-bounds-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Marked-polygon-correlations-and-one-arc-bounds-September-26-2026/README.md) · not independently verified here
- [Disk transfer representations and confined bridge mass](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Disk-transfer-representations-and-confined-bridge-mass-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Disk-transfer-representations-and-confined-bridge-mass-September-26-2026/README.md) · not independently verified here
- [Polynomial vacuum representations and bridge mass for honeycomb walks](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Polynomial-vacuum-representations-and-bridge-mass-for-honeycomb-walks-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Polynomial-vacuum-representations-and-bridge-mass-for-honeycomb-walks-September-26-2026/README.md) · not independently verified here
- [Renewal and changes of law for critical honeycomb walks](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Renewal-and-changes-of-law-for-critical-honeycomb-walks-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Renewal-and-changes-of-law-for-critical-honeycomb-walks-September-26-2026/README.md) · not independently verified here
- [Critical strip-crossing mass on the honeycomb lattice](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Critical-strip-crossing-mass-on-the-honeycomb-lattice-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Critical-strip-crossing-mass-on-the-honeycomb-lattice-September-26-2026/README.md) · not independently verified here
- [Uniform marked-polygon estimates and sharp finite bridge moments](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-marked-polygon-estimates-and-sharp-finite-bridge-moments-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-marked-polygon-estimates-and-sharp-finite-bridge-moments-September-26-2026/README.md) · not independently verified here
- [Cap-selected amplitudes and triangle chords for honeycomb walks](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cap-selected-amplitudes-and-triangle-chords-for-honeycomb-walks-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cap-selected-amplitudes-and-triangle-chords-for-honeycomb-walks-September-26-2026/README.md) · not independently verified here

#### 238. Optimal logarithmic mixing of the Thorp shuffle.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/238.md)
- [Optimal-order mixing of the Thorp shuffle](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/README.md) · not independently verified here
- [Random coordinate frames and partial permutation laws](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Random-coordinate-frames-and-partial-permutation-laws-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Random-coordinate-frames-and-partial-permutation-laws-September-26-2026/README.md) · not independently verified here
- [From partial permutation information to Fourier bounds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/From-partial-permutation-information-to-Fourier-bounds-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/From-partial-permutation-information-to-Fourier-bounds-September-26-2026/README.md) · not independently verified here
- [Conditional information under deterministic coordinate sweeps](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Conditional-information-under-deterministic-coordinate-sweeps-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Conditional-information-under-deterministic-coordinate-sweeps-September-26-2026/README.md) · not independently verified here
- [Conditional permutations in a revealed switching environment](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Conditional-permutations-in-a-revealed-switching-environment-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Conditional-permutations-in-a-revealed-switching-environment-September-26-2026/README.md) · not independently verified here
- [Routing densities and representation contraction for Thorp sweeps](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/README.md) · manifest paper-source listed; not independently verified here
- [Row–column symmetry and contraction of coordinate sweeps](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Row-column-symmetry-and-contraction-of-coordinate-sweeps-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Row-column-symmetry-and-contraction-of-coordinate-sweeps-September-26-2026/README.md) · not independently verified here
- [Random-subspace tests and trace smoothing for coordinate sweeps](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Random-subspace-tests-and-trace-smoothing-for-coordinate-sweeps-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Random-subspace-tests-and-trace-smoothing-for-coordinate-sweeps-September-26-2026/README.md) · not independently verified here
- [Compatibility entropy and the spectrum of a Thorp sweep](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/README.md) · manifest paper-source listed; not independently verified here
- [Signed tensor densities and diagram budgets for the Thorp shuffle](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Signed-tensor-densities-and-diagram-budgets-for-coordinate-sweeps-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Signed-tensor-densities-and-diagram-budgets-for-coordinate-sweeps-September-26-2026/README.md) · not independently verified here
- [Conditional coordinate sweeps and analytic transfer](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Conditional-coordinate-sweeps-and-analytic-transfer-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Conditional-coordinate-sweeps-and-analytic-transfer-September-26-2026/README.md) · manifest paper-source listed; not independently verified here
- [A strict four-row permanent inequality and permutation moments](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-strict-four-row-permanent-inequality-and-permutation-moments-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-strict-four-row-permanent-inequality-and-permutation-moments-September-26-2026/README.md) · not independently verified here

#### 239. Sharp singularity rates for symmetric random sign matrices.

- [The sharp exponential rate of singularity for symmetric Bernoulli matrices](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-sharp-exponential-rate-of-singularity-for-symmetric-Bernoulli-matrices-October-3-2026/symmetric-bernoulli-singularity.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-sharp-exponential-rate-of-singularity-for-symmetric-Bernoulli-matrices-October-3-2026/README.md) · not independently verified here
- [The sharp singularity rate for biased symmetric sign matrices](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/biased-symmetric-sign-singularity.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/README.md) · not independently verified here


### Mathematical logic

#### 240. Shelah's eventual categoricity and the prescribed-threshold obstruction.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/240.md)
- [A CH obstruction to a prescribed categoricity threshold](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/README.md) · manifest paper-source listed; not independently verified here
- [Eventual categoricity for abstract elementary classes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026/README.md) · not independently verified here

#### 241. Rigidity of the Turing degrees.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/241.md)
- [Rigidity of the Turing degrees](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Rigidity-of-the-Turing-degrees-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Rigidity-of-the-Turing-degrees-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 242. Single-fold Diophantine representations and undecidability under an at-most-one-solution promise.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/242.md)
- [Single-fold Diophantine representations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Single-fold-Diophantine-representations-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Single-fold-Diophantine-representations-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 243. Separating choiceless counting from polynomial time and witnessed choice.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/243.md)
- [Choiceless polynomial time with counting does not capture polynomial time](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [Witnessed symmetric choice is strictly stronger than choiceless polynomial time with counting](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/README.md) · not independently verified here

#### 244. The Partition Principle does not imply Choice.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/244.md)
- [The Partition Principle does not imply Choice](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/partition-principle-without-choice.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 245. Weak normalization implies strong normalization in pure type systems.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/245.md)
- [Weak and strong normalization in pure type systems](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Weak-and-strong-normalization-in-pure-type-systems-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Weak-and-strong-normalization-in-pure-type-systems-September-25-2026/README.md) · not independently verified here


### Group theory

#### 246. Cannon's conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/246.md)
- [A Modulus Proof of Cannon’s Conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Modulus-Proof-of-Cannons-Conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Modulus-Proof-of-Cannons-Conjecture-September-23-2026/README.md) · not independently verified here

#### 247. An infinite finitely presented residually finite 2-group and a finitely presented nil algebra.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/247.md)
- [An infinite finitely presented residually finite 2-group](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-infinite-finitely-presented-residually-finite-2-group-October-5-2026/residually-finite-torsion.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-infinite-finitely-presented-residually-finite-2-group-October-5-2026/README.md) · not independently verified here
- [An infinite finitely presented periodic group](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-infinite-finitely-presented-periodic-group-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-infinite-finitely-presented-periodic-group-September-23-2026/README.md) · not independently verified here

#### 248. Thompson's group F is nonamenable.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/248.md)
- [Thompson's group F is nonamenable](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Thompsons-group-F-is-nonamenable-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Thompsons-group-F-is-nonamenable-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 249. A finitely generated Eilenberg–Ganea counterexample.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/249.md)
- [A finitely generated counterexample to the Eilenberg–Ganea conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-finitely-generated-counterexample-to-the-Eilenberg-Ganea-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-finitely-generated-counterexample-to-the-Eilenberg-Ganea-conjecture-September-23-2026/README.md) · not independently verified here

#### 250. Boone–Higman embeddings with higher finiteness.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/250.md)
- [Finite algebraic envelopes and the Boone–Higman conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/README.md) · not independently verified here
- [Simple F∞ overgroups of groups with decidable word problem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/README.md) · not independently verified here
- [A universal group of type F∞](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-universal-group-of-type-F-infinity-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-universal-group-of-type-F-infinity-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 251. Amenability, unitarizability, and strong Ulam stability.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/251.md)
- [Unitarizability implies amenability for discrete groups](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [Strong Ulam Stability Characterizes Amenability](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/strong-ulam-stability.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/README.md) · not independently verified here

#### 252. A torsion-free hyperbolic group that is neither residually finite nor linear over any field.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/252.md)
- [A torsion-free hyperbolic group that is not residually finite](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 253. An infinite finitely presented simple amenable group.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/253.md)
- [An infinite finitely presented simple amenable group](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 254. Classifying spaces and geometric obstructions for Artin groups.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/254.md)
- [Harmonic heights and the Artin K(pi,1) conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Harmonic-heights-and-the-Artin-K-pi-1-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Harmonic-heights-and-the-Artin-K-pi-1-conjecture-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [An Artin group with no geometric CAT(0) action](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [Parabolic intersections in Artin groups](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Parabolic-intersections-in-Artin-groups-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Parabolic-intersections-in-Artin-groups-September-23-2026/README.md) · not independently verified here

#### 255. Quasi-isometric recognition of virtually polycyclic groups.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/255.md)
- [Quasi-isometric recognition of virtually polycyclic groups](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/quasi-isometric-recognition-of-virtually-polycyclic-groups-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/quasi-isometric-recognition-of-virtually-polycyclic-groups-September-24-2026/README.md) · not independently verified here

#### 256. Nonsingular systems of equations over arbitrary groups.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/256.md)
- [Nonsingular systems of equations over arbitrary groups](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026/nonsingular-systems-over-arbitrary-groups.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026/README.md) · not independently verified here
- [The Kervaire theorem for groups](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Kervaire-Theorem-for-Groups-September-24-2026/The-Kervaire-Theorem-for-Groups-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Kervaire-Theorem-for-Groups-September-24-2026/README.md) · not independently verified here

#### 257. A hyperbolic group without a geometric CAT(0) action.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/257.md)
- [A hyperbolic group with no geometric CAT(0) action](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 258. Gersten’s conjecture and virtual compact specialness of one-relator groups.

- [Baumslag-Solitar-free one-relator groups are hyperbolic](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Baumslag-Solitar-free-one-relator-groups-are-hyperbolic-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Baumslag-Solitar-free-one-relator-groups-are-hyperbolic-September-25-2026/README.md) · not independently verified here
- [Virtual compact specialness of hyperbolic one-relator groups](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Virtual-compact-specialness-of-hyperbolic-one-relator-groups-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Virtual-compact-specialness-of-hyperbolic-one-relator-groups-September-25-2026/README.md) · not independently verified here

#### 259. A group without fixed price.

- [A group without fixed price](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-group-without-fixed-price-October-5-2026/unequal-costs-rank-100-amalgam.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-group-without-fixed-price-October-5-2026/README.md) · not independently verified here


### Mathematical physics

#### 260. Spacetime Penrose inequalities: enclosing area, charge, rotation, and anti-de Sitter extensions.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/260.md)
- [The spacetime Penrose inequality with charge and original-data rigidity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-spacetime-Penrose-inequality-with-charge-and-original-data-rigidity-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-spacetime-Penrose-inequality-with-charge-and-original-data-rigidity-October-5-2026/README.md) · not independently verified here
- [A Charged Reduction of the Spacetime Penrose Inequality in Spatial Dimensions at Least Four](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026/README.md) · not independently verified here
- [Spacetime Penrose inequalities: enclosing area, charge, and rigidity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Spacetime-Penrose-inequalities-enclosing-area-charge-and-rigidity-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Spacetime-Penrose-inequalities-enclosing-area-charge-and-rigidity-October-5-2026/README.md) · not independently verified here
- [The Kerr–Newman Penrose Inequality for Axisymmetric Electrovacuum Exteriors](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Kerr-Newman-Penrose-Inequality-for-Axisymmetric-Electrovacuum-Exteriors-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Kerr-Newman-Penrose-Inequality-for-Axisymmetric-Electrovacuum-Exteriors-October-5-2026/README.md) · not independently verified here
- [Electromagnetic tails and the Kerr–Newman Penrose inequality](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Electromagnetic-tails-and-the-Kerr-Newman-Penrose-inequality-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Electromagnetic-tails-and-the-Kerr-Newman-Penrose-inequality-October-5-2026/README.md) · not independently verified here
- [The nonmaximal anti-de Sitter Penrose Inequality and original-data rigidity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-nonmaximal-anti-de-Sitter-Penrose-Inequality-and-original-data-rigidity-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-nonmaximal-anti-de-Sitter-Penrose-Inequality-and-original-data-rigidity-October-5-2026/README.md) · not independently verified here
- [The Penrose inequality for maximal asymptotically hyperbolic initial data](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Penrose-inequality-for-maximal-asymptotically-hyperbolic-initial-data-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Penrose-inequality-for-maximal-asymptotically-hyperbolic-initial-data-October-5-2026/README.md) · not independently verified here
- [A local Penrose inequality for conformal perturbations of Schwarzschild–anti-de Sitter data](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-local-Penrose-inequality-for-conformal-perturbations-of-Schwarzschild-anti-de-Sitter-data-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-local-Penrose-inequality-for-conformal-perturbations-of-Schwarzschild-anti-de-Sitter-data-October-5-2026/README.md) · not independently verified here
- [The spacetime Penrose inequality and enclosing area](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-spacetime-Penrose-inequality-and-enclosing-area-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-spacetime-Penrose-inequality-and-enclosing-area-September-27-2026/README.md) · not independently verified here
- [Conformal flow and the Riemannian Penrose inequality with minimizing frontiers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Conformal-flow-and-the-Riemannian-Penrose-inequality-with-minimizing-frontiers-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Conformal-flow-and-the-Riemannian-Penrose-inequality-with-minimizing-frontiers-September-27-2026/README.md) · not independently verified here
- [Equality and rigidity in the spacetime Penrose inequality](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Equality-and-rigidity-in-the-spacetime-Penrose-inequality-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Equality-and-rigidity-in-the-spacetime-Penrose-inequality-September-27-2026/README.md) · not independently verified here
- [Boundary graph deformations for the spacetime Penrose inequality](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Boundary-graph-deformations-for-the-spacetime-Penrose-inequality-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Boundary-graph-deformations-for-the-spacetime-Penrose-inequality-September-27-2026/README.md) · not independently verified here
- [Area-controlled end replacement and the Bondi Penrose inequality in the CKS class](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Area-controlled-end-replacement-and-the-Bondi-Penrose-inequality-in-the-CKS-class-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Area-controlled-end-replacement-and-the-Bondi-Penrose-inequality-in-the-CKS-class-September-27-2026/README.md) · not independently verified here

#### 261. Localization and delocalization in the Anderson model.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/261.md)
- [Absolutely Continuous Spectrum for Weak-Disorder Anderson Models in Dimensions at Least Three](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/README.md) · not independently verified here
- [Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/README.md) · not independently verified here

#### 262. Sharp finite-matrix Lieb–Thirring inequalities and all equality cases.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/262.md)
- [Equality cases in the sharp one-dimensional matrix Lieb–Thirring inequality](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/sharp-one-dimensional-lieb-thirring-inequalities-matrix-potentials.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/README.md) · not independently verified here
- [Sharp one-dimensional Lieb–Thirring inequalities for matrix potentials](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/sharp-matrix-lieb-thirring.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/README.md) · not independently verified here
- [Sharp one-dimensional Lieb–Thirring constants](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 263. The ionization and generalized ionization conjectures.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/263.md)
- [Uniform excess charge for Coulomb molecules and the outer radius of neutral atoms](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/README.md) · not independently verified here
- [Generalized ionization energies for full Coulomb atoms](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026/README.md) · manifest paper-source listed; not independently verified here
- [Generalized outer-electron radii of neutral Coulomb atoms](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Generalized-outer-electron-radii-of-neutral-Coulomb-atoms-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Generalized-outer-electron-radii-of-neutral-Coulomb-atoms-September-24-2026/README.md) · not independently verified here

#### 264. Strong cosmic censorship near two-ended Kerr data.

- [Generic Future Inextendibility with Square-Integrable Connection Near a Fixed Kerr Spacetime](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Generic-Future-Inextendibility-with-Square-Integrable-Connection-Near-a-Fixed-Kerr-Spacetime-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Generic-Future-Inextendibility-with-Square-Integrable-Connection-Near-a-Fixed-Kerr-Spacetime-September-23-2026/README.md) · not independently verified here
- [Generic C1 Future Inextendibility Near Rotating Subextremal Kerr Spacetimes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Generic-C1-Future-Inextendibility-Near-Rotating-Subextremal-Kerr-Spacetimes-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Generic-C1-Future-Inextendibility-Near-Rotating-Subextremal-Kerr-Spacetimes-September-23-2026/README.md) · not independently verified here
- [Quantitative Near-Kerr Evolution and Generic C2 Future Inextendibility](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quantitative-Near-Kerr-Evolution-and-Generic-C2-Future-Inextendibility-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quantitative-Near-Kerr-Evolution-and-Generic-C2-Future-Inextendibility-September-23-2026/README.md) · not independently verified here

#### 265. Area laws and tensor networks for two-dimensional gapped systems.

- [A two-dimensional area law from a global spectral gap](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-two-dimensional-area-law-from-a-global-spectral-gap-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-two-dimensional-area-law-from-a-global-spectral-gap-September-24-2026/README.md) · not independently verified here
- [Polynomial PEPS approximation of gapped square-grid ground states](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Polynomial-PEPS-approximation-of-gapped-square-grid-ground-states-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Polynomial-PEPS-approximation-of-gapped-square-grid-ground-states-September-24-2026/README.md) · not independently verified here

#### 266. Exactly three mutually unbiased bases in dimension six.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/266.md)
- [The maximum number of mutually unbiased bases in dimension six](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/README.md) · not independently verified here
- [Exact Fourier certificates for complex Hadamard matrices of order six](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/README.md) · not independently verified here

#### 267. Positive-temperature Bose–Einstein condensation and exact quantum depletion.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/267.md)
- [Bose–Einstein condensation at positive temperature in the dilute hard-sphere gas](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/positive-temperature-hard-spheres.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/README.md) · not independently verified here
- [Quantum Depletion and Momentum Distribution in the Dilute Hard-Sphere Bose Gas](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026/Quantum-Depletion-in-the-Dilute-Hard-Sphere-Bose-Gas.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026/README.md) · not independently verified here
- [Quantum Depletion for Fixed Bounded Repulsive Potentials](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quantum-Depletion-for-Fixed-Bounded-Repulsive-Potentials-October-5-2026/fixed-repulsion-quantum-depletion.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quantum-Depletion-for-Fixed-Bounded-Repulsive-Potentials-October-5-2026/README.md) · not independently verified here
- [A density-uniform condensate bound for dilute Bose gases](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026/README.md) · not independently verified here
- [Ground-state condensation in the dilute hard-sphere gas](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026/README.md) · not independently verified here

#### 268. The spin-one Haldane gap.

- [The periodic spin-one Haldane gap](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/README.md) · not independently verified here
- [A boundary-field gap for the spin-one Heisenberg chain](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026/README.md) · not independently verified here

#### 269. Uniform Laughlin gap and stability under bounded scalar disorder.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/269.md)
- [Uniform Stability of the Spherical Laughlin Gap](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/uniform-stability-spherical-laughlin-gap.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/README.md) · not independently verified here
- [A Fock-space inequality and the Laughlin spectral gap](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 270. Threshold and positive-energy bound states of the BFSS matrix model.

- [The unique threshold bound state of the SU(N) BFSS model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-unique-threshold-bound-state-of-the-SU-N-BFSS-model-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-unique-threshold-bound-state-of-the-SU-N-BFSS-model-September-24-2026/README.md) · not independently verified here
- [Positive eigenvalues of the relative SU(2) BFSS Hamiltonian](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positive-eigenvalues-of-the-relative-SU-2-BFSS-Hamiltonian-October-5-2026/positive-eigenvalues-relative-su2-bfss.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positive-eigenvalues-of-the-relative-SU-2-BFSS-Hamiltonian-October-5-2026/README.md) · not independently verified here

#### 271. Bloch's law, its lattice correction, and the spherical magnetization law.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/271.md)
- [Bloch's Law for Finite-Range Heisenberg Ferromagnets in Three Dimensions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/bloch-law-heisenberg.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Blochs-Law-for-Finite-Range-Heisenberg-Ferromagnets-in-Three-Dimensions-October-5-2026/README.md) · not independently verified here
- [The first lattice correction to Bloch's law](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/first-lattice-correction-bloch-law.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-first-lattice-correction-to-Blochs-law-October-5-2026/README.md) · not independently verified here
- [The spherical magnetization law for the three-dimensional quantum Heisenberg ferromagnet](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/spherical-magnetization.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/README.md) · not independently verified here
- [Spontaneous magnetization in the quantum Heisenberg ferromagnet](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/README.md) · not independently verified here

#### 272. Entanglement without distillable secret key.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/272.md)
- [Entanglement with zero distillable secret key in local dimension ten](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/README.md) · not independently verified here

#### 273. The entropy photon-number inequality.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/273.md)
- [The entropy photon-number inequality](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-entropy-photon-number-inequality-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-entropy-photon-number-inequality-September-24-2026/README.md) · not independently verified here

#### 274. Parity is not in QAC0.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/274.md)
- [Product-projection localization and the QAC0 parity lower bound](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Product-projection-localization-and-the-QAC0-parity-lower-bound-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Product-projection-localization-and-the-QAC0-parity-lower-bound-September-24-2026/README.md) · manifest paper-source listed; not independently verified here
- [Regular trajectories, pruning and quantum parity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Regular-trajectories-pruning-and-quantum-parity-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Regular-trajectories-pruning-and-quantum-parity-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 275. QMA-hardness of continuum Coulomb energy.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/275.md)
- [Continuum Coulomb hardness with binary nuclear charges](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026/README.md) · not independently verified here
- [QMA-hardness of continuum Coulomb energy with unit nuclear charges](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/QMA-hardness-of-continuum-Coulomb-energy-with-unit-nuclear-charges-September-24-2026/QMA-hardness-of-continuum-Coulomb-energy-with-unit-nuclear-charges-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/QMA-hardness-of-continuum-Coulomb-energy-with-unit-nuclear-charges-September-24-2026/README.md) · not independently verified here

#### 276. Classical capacity of generalized amplitude damping.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/276.md)
- [Classical capacity and entropy inequalities for generalized amplitude damping](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 277. Threshold repetition for entangled games.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/277.md)
- [Threshold parallel repetition for finite-dimensional entangled games](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 278. Failure of Kohn–Sham ensemble representation.

- [A Coulomb ground-state density without Kohn-Sham ensemble representation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Coulomb-Ground-State-Density-without-Kohn-Sham-Ensemble-Representation-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Coulomb-Ground-State-Density-without-Kohn-Sham-Ensemble-Representation-September-25-2026/README.md) · not independently verified here

#### 279. Exact quantum factoring over a fixed finite gate set.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/279.md)
- [Exact quantum factoring over a fixed finite gate set](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-quantum-factoring-over-a-fixed-finite-gate-set-September-25-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-quantum-factoring-over-a-fixed-finite-gate-set-September-25-2026/README.md) · not independently verified here

#### 280. Unitary vertex operator algebras and conformal nets.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/280.md)
- [Strongly rational unitary vertex operator algebras and conformal nets](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Strongly-rational-unitary-vertex-operator-algebras-and-conformal-nets-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Strongly-rational-unitary-vertex-operator-algebras-and-conformal-nets-September-25-2026/README.md) · not independently verified here

#### 281. QAOA attains the SK optimum in the thermodynamic-first limit.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/281.md)
- [QAOA attains the SK ground-state energy in the thermodynamic-first limit](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/README.md) · not independently verified here
- [Full support of the zero-temperature Sherrington-Kirkpatrick order parameter](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/README.md) · not independently verified here

#### 282. From scale symmetry to local conformal symmetry in four-dimensional QFT.

- [Scale and conformal symmetry in four-dimensional operational quantum field theory](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Scale-and-conformal-symmetry-in-four-dimensional-operational-quantum-field-theory-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Scale-and-conformal-symmetry-in-four-dimensional-operational-quantum-field-theory-September-26-2026/README.md) · not independently verified here

#### 283. Polynomial-time unitary synthesis from a Boolean oracle.

- [Polynomial-Time Unitary Synthesis from a Boolean Oracle](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026/README.md) · not independently verified here

#### 284. The optimal quartic separation between randomized and quantum queries.

- [A Nearly Quartic Separation Between Randomized and Quantum Query Complexity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/quartic-query-separation.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/README.md) · not independently verified here


### Operator algebras

#### 285. Counterexamples to Baum–Connes and Kadison–Kaplansky.

- [A torsion-free counterexample to reduced Baum–Connes injectivity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026/README.md) · not independently verified here
- [A torsion-free counterexample to the Kadison–Kaplansky projection conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/README.md) · not independently verified here
- [An irrational-trace counterexample to reduced Baum–Connes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026/README.md) · not independently verified here

#### 286. Rigidity and arithmetic of lattice von Neumann algebras.

- [Arithmeticity of twisted finite correspondences for lattices over local fields](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Arithmeticity-of-twisted-finite-correspondences-for-lattices-over-local-fields-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Arithmeticity-of-twisted-finite-correspondences-for-lattices-over-local-fields-September-23-2026/README.md) · not independently verified here
- [The arithmetic category and stable recovery of lattice factors](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-arithmetic-category-and-stable-recovery-of-lattice-factors-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-arithmetic-category-and-stable-recovery-of-lattice-factors-September-23-2026/README.md) · not independently verified here

#### 287. Isomorphism of the free group factors.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/287.md)
- [An isomorphism of the free group factors](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-isomorphism-of-the-free-group-factors-September-23-2026/An-isomorphism-of-the-free-group-factors-September-23-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-isomorphism-of-the-free-group-factors-September-23-2026/README.md) · not independently verified here

#### 288. Kadison's similarity conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/288.md)
- [Kadison's similarity theorem through uniform derivation estimates](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026/README.md) · not independently verified here

#### 289. Strong Kadison–Kastler stability and its spatial boundaries.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/289.md)
- [Universal strong Kadison–Kastler stability](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026/README.md) · not independently verified here
- [Near Inclusions of von Neumann Algebras Without Small Spatial Embeddings](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Near-Inclusions-of-von-Neumann-Algebras-Without-Small-Spatial-Embeddings-October-5-2026/near-inclusions.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Near-Inclusions-of-von-Neumann-Algebras-Without-Small-Spatial-Embeddings-October-5-2026/README.md) · not independently verified here
- [Close Separable C*-Algebras Without Spatial Conjugacy](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Close-Separable-Cstar-Algebras-Without-Spatial-Conjugacy-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Close-Separable-Cstar-Algebras-Without-Spatial-Conjugacy-October-5-2026/README.md) · not independently verified here

#### 290. Relative bicentralizers and modular spectral recovery.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/290.md)
- [Expected amenable subalgebras preserving core commutants](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/README.md) · not independently verified here
- [Bounded recovery for modular spectral averages](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026/Bounded-recovery-for-modular-spectral-averages-September-23-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 291. Cuntz comparison, nuclear dimension, and equivariant Jiang–Su stability.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/291.md)
- [Equivariant Jiang–Su Stability for Amenable Actions in the Unital Stably Finite Case](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026/README.md) · not independently verified here
- [Cuntz comparison and Jiang–Su absorption](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/README.md) · not independently verified here
- [Nuclear dimension and Jiang–Su stability without elementary subquotients](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/README.md) · not independently verified here
- [Tracial projection methods and uniform property Gamma](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 292. Kirchberg's $\mathcal O_2$ norm-ultrapower embedding problem.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/292.md)
- [An explicit obstruction to nuclear norm-ultrapower embeddings](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-explicit-obstruction-to-nuclear-norm-ultrapower-embeddings-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-explicit-obstruction-to-nuclear-norm-ultrapower-embeddings-September-23-2026/README.md) · not independently verified here

#### 293. Invariant projections, hyperinvariant subspaces, and transitive algebras.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/293.md)
- [Invariant-projection counterexamples for every irrational rotation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026/README.md) · not independently verified here
- [Backward intertwiners and a transitive commutant](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/README.md) · manifest paper-source listed; not independently verified here

#### 294. Kaplansky's quasitrace conjecture and failure of tensor-product stable finiteness.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/294.md)
- [A counterexample to Kaplansky's quasitrace conjecture and failure of tensor-product stable finiteness](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 295. The Kadison–Ringrose cohomology conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/295.md)
- [Vanishing of higher bounded Hochschild cohomology](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026/README.md) · not independently verified here

#### 296. The generator problem for finite factors.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/296.md)
- [Relative generation and the generator problem for finite factors](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Relative-generation-and-the-generator-problem-for-finite-factors-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Relative-generation-and-the-generator-problem-for-finite-factors-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 297. A ZFC counterexample to Naimark's problem.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/297.md)
- [A counterexample to Naimark's problem in ZFC](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026/naimark-counterexample-zfc.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026/README.md) · not independently verified here

#### 298. Two notions of free entropy differ even when both are finite.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/298.md)
- [A finite-entropy separation of microstates and nonmicrostates free entropy](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-finite-entropy-separation-of-microstates-and-nonmicrostates-free-entropy-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-finite-entropy-separation-of-microstates-and-nonmicrostates-free-entropy-September-25-2026/README.md) · not independently verified here

#### 299. The Kirchberg–Rørdam character criterion and infinite tensor-power Jiang–Su stability.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/299.md)
- [The Kirchberg–Rørdam character criterion](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 300. Approximation and quadratic strong-operator paving.

- [Approximation Paving over Arbitrary Maximal Abelian Subalgebras](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/README.md) · not independently verified here
- [Quadratic Strong-Operator Paving over Arbitrary Maximal Abelian Subalgebras](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/README.md) · not independently verified here

#### 301. Trace cones and Razak–Jacelon stabilization.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/301.md)
- [The trace cone classifies Razak–Jacelon stabilizations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 302. Radius of comparison equals half the mean dimension.

- [Filtered products and boundary-preserving compression in complex cobordism](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Filtered-products-and-boundary-preserving-compression-in-complex-cobordism-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Filtered-products-and-boundary-preserving-compression-in-complex-cobordism-September-25-2026/README.md) · not independently verified here
- [Radius of comparison equals half the mean dimension](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Radius-of-comparison-equals-half-the-mean-dimension-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Radius-of-comparison-equals-half-the-mean-dimension-September-25-2026/README.md) · not independently verified here

#### 303. Weak pure infiniteness and Cuntz-algebra absorption.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/303.md)
- [Weak pure infiniteness and O-infinity absorption](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Weak-pure-infiniteness-and-O-infinity-absorption-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Weak-pure-infiniteness-and-O-infinity-absorption-September-25-2026/README.md) · not independently verified here


### Topology

#### 304. The Hilbert–Smith conjecture in every dimension.

- [The Hilbert–Smith conjecture in every finite dimension](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026/README.md) · not independently verified here

#### 305. Four-dimensional disk embedding and Wall's conjecture.

- [A boundary-only obstruction to four-dimensional disk embedding](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-boundary-only-obstruction-to-four-dimensional-disk-embedding-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-boundary-only-obstruction-to-four-dimensional-disk-embedding-September-24-2026/README.md) · not independently verified here
- [A marked tensor obstruction to four-dimensional disk embedding](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-marked-tensor-obstruction-to-four-dimensional-disk-embedding-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-marked-tensor-obstruction-to-four-dimensional-disk-embedding-September-24-2026/README.md) · not independently verified here
- [A PD4 group without an aspherical manifold model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-PD4-group-without-an-aspherical-manifold-model-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-PD4-group-without-an-aspherical-manifold-model-September-24-2026/README.md) · not independently verified here

#### 306. The purely cosmetic surgery conjecture.

- [Purely cosmetic surgery on knots in the three-sphere](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/README.md) · not independently verified here

#### 307. Failure of rational injectivity for maximal coarse assembly.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/307.md)
- [Failure of rational injectivity for maximal coarse assembly](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026/README.md) · not independently verified here
- [A counterexample to the coarse Novikov conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026/README.md) · not independently verified here

#### 308. Finite Smith–Toda complexes at every height.

- [Finite Smith–Toda Complexes at Varying Primes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-Smith-Toda-Complexes-at-Varying-Primes-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-Smith-Toda-Complexes-at-Varying-Primes-September-23-2026/README.md) · not independently verified here
- [A finite Smith–Toda complex V(4) at the prime 1009](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-finite-Smith-Toda-complex-V4-at-the-prime-1009-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-finite-Smith-Toda-complex-V4-at-the-prime-1009-September-23-2026/README.md) · not independently verified here

#### 309. The Kervaire invariant problem at the prime three.

- [The Kervaire invariant problem at the prime three](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026/README.md) · not independently verified here

#### 310. Quillen's conjecture in rational homology.

- [Rational homology and Quillen's conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Rational-homology-and-Quillens-conjecture-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Rational-homology-and-Quillens-conjecture-September-24-2026/README.md) · not independently verified here

#### 311. The Hovey–Strickland and Chai conjectures.

- [Stabilizer orbits and thick tensor ideals of dualizable K(n)-local spectra](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-Dualizable-Kn-Local-Spectra-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-Dualizable-Kn-Local-Spectra-September-24-2026/README.md) · not independently verified here

#### 312. The Grothendieck homotopy hypothesis.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/312.md)
- [The Grothendieck homotopy hypothesis via elementary expansions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 313. Finite generation for the $K(n)$-local sphere.

- [Finite generation for the K(n)-local sphere](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-generation-for-the-Kn-local-sphere-September-24-2026/Finite-generation-for-the-Kn-local-sphere-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-generation-for-the-Kn-local-sphere-September-24-2026/README.md) · not independently verified here

#### 314. Cyclic length and chromatic fixed-point loss.

- [Cyclic length and chromatic fixed-point loss](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cyclic-Length-and-Chromatic-Fixed-Point-Loss-September-24-2026/Cyclic-Length-and-Chromatic-Fixed-Point-Loss-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Cyclic-Length-and-Chromatic-Fixed-Point-Loss-September-24-2026/README.md) · not independently verified here

#### 315. The four-dimensional Singer conjecture.

- [The Singer conjecture in dimension four](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026/README.md) · not independently verified here

#### 316. Curtis’s conjecture.

- [The Stable Hurewicz Image of the Sphere at Two](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Stable-Hurewicz-Image-of-the-Sphere-at-Two-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Stable-Hurewicz-Image-of-the-Sphere-at-Two-September-25-2026/README.md) · not independently verified here

#### 317. Thomason model structures in all strict higher dimensions.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/317.md)
- [Thomason Model Structures in Every Strict Higher Dimension](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Thomason-Model-Structures-in-Every-Strict-Higher-Dimension-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Thomason-Model-Structures-in-Every-Strict-Higher-Dimension-September-25-2026/README.md) · not independently verified here

#### 318. Chromatic splitting: filtrations and counterexamples.

- [Filtered chromatic splitting at generic primes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Filtered-chromatic-splitting-at-generic-primes-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Filtered-chromatic-splitting-at-generic-primes-September-25-2026/README.md) · not independently verified here
- [The height-three chromatic overlap: an explicit filtration and its attachments](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-height-three-chromatic-overlap-an-explicit-filtration-and-its-attachments-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-height-three-chromatic-overlap-an-explicit-filtration-and-its-attachments-September-27-2026/README.md) · not independently verified here
- [A rational obstruction to strong chromatic splitting at height three](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-rational-obstruction-to-strong-chromatic-splitting-at-height-three-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-rational-obstruction-to-strong-chromatic-splitting-at-height-three-September-25-2026/README.md) · not independently verified here
- [Failure of finite assembly for a chromatic overlap at the prime three](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Failure-of-finite-assembly-for-a-chromatic-overlap-at-the-prime-three-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Failure-of-finite-assembly-for-a-chromatic-overlap-at-the-prime-three-September-25-2026/README.md) · not independently verified here
- [Counterexamples to weak chromatic splitting: sphere kernels and descent exponents](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Counterexamples-to-weak-chromatic-splitting-sphere-kernels-and-descent-exponents-September-27-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Counterexamples-to-weak-chromatic-splitting-sphere-kernels-and-descent-exponents-September-27-2026/README.md) · not independently verified here

#### 319. Counterexamples to finite generation at chromatic height two.

- [Counterexamples to the Hahn-Wilson conjecture at height two](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Counterexamples-to-the-Hahn-Wilson-conjecture-at-height-two-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Counterexamples-to-the-Hahn-Wilson-conjecture-at-height-two-September-26-2026/README.md) · not independently verified here

#### 320. Nonhomeomorphic closed aspherical four-manifolds.

- [Nonhomeomorphic closed aspherical four-manifolds with the same homotopy type](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/README.md) · not independently verified here

#### 321. A counterexample to Wall's finite D(2) problem.

- [A Counterexample to Wall's D(2) Problem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-Walls-D2-Problem-October-6-2026/wall-d2-counterexample.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-Walls-D2-Problem-October-6-2026/README.md) · not independently verified here


### Functional analysis

#### 322. Tingley’s sphere-isometry problem.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/322.md)
- [A positive solution to Tingley’s problem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 323. Independence of the separable quotient problem.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/323.md)
- [Relative independence of the separable quotient problem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Relative-independence-of-the-separable-quotient-problem-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Relative-independence-of-the-separable-quotient-problem-September-23-2026/README.md) · not independently verified here

#### 324. Lipschitz equivalent Banach spaces need not be linearly isomorphic.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/324.md)
- [Lipschitz Equivalent Separable Banach Spaces Need Not Be Linearly Isomorphic](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/README.md) · manifest paper-source listed; not independently verified here
- [Bi-Lipschitz Absorption of c0 Without a Linear Copy of c0](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/README.md) · manifest paper-source listed; not independently verified here

#### 325. The complete Crouzeix conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/325.md)
- [A direct proof of the complete Crouzeix inequality](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/README.md) · manifest paper-source listed; not independently verified here
- [The complete Crouzeix theorem: optimal similarity and a common positive boundary representation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-complete-Crouzeix-theorem-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-complete-Crouzeix-theorem-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 326. The cotype–cotype conjecture under the approximation property.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/326.md)
- [The cotype–cotype conjecture under the approximation property](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-cotype-cotype-conjecture-under-the-approximation-property-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 327. Markov type characterizes superreflexivity.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/327.md)
- [Nontrivial Markov Type Forces Superreflexivity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 328. Nonexpansive fixed points in reflexive Banach spaces.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/328.md)
- [Fixed Points of Nonexpansive Maps in Reflexive Banach Spaces](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 329. A counterexample to metric-entropy duality.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/329.md)
- [Counterexamples to the duality conjecture for metric entropy](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 330. A uniformly discrete counterexample to bounded approximation in Lipschitz-free spaces.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/330.md)
- [A uniformly discrete counterexample to bounded approximation in Lipschitz-free spaces](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Failure-of-Bounded-Approximation-in-a-Lipschitz-Free-Space-over-a-Uniformly-Discrete-Metric-Space-September-26-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Failure-of-Bounded-Approximation-in-a-Lipschitz-Free-Space-over-a-Uniformly-Discrete-Metric-Space-September-26-2026/README.md) · not independently verified here

#### 331. Reflexive midpoint convexity and diamond distortion.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/331.md)
- [Asymptotic midpoint uniform convexity and unbounded diamond distortion in a reflexive tree space](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/README.md) · manifest paper-source listed; not independently verified here
- [Midpoint lenses in segment spaces](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Midpoint-lenses-in-segment-spaces-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Midpoint-lenses-in-segment-spaces-September-27-2026/README.md) · manifest paper-source listed; not independently verified here
- [Distortion of countably branching diamonds from midpoint and tree energies](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Diamond-distortion-from-midpoint-and-tree-energies-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Diamond-distortion-from-midpoint-and-tree-energies-September-27-2026/README.md) · manifest paper-source listed; not independently verified here
- [Exact asymptotic moduli in a Daugavet subspace of L1](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-asymptotic-moduli-in-a-Daugavet-subspace-of-L1-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Exact-asymptotic-moduli-in-a-Daugavet-subspace-of-L1-September-27-2026/README.md) · manifest paper-source listed; not independently verified here
- [Midpoint convexity from bounded tree potentials and path costs](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Midpoint-convexity-from-bounded-tree-potentials-and-path-costs-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Midpoint-convexity-from-bounded-tree-potentials-and-path-costs-September-27-2026/README.md) · manifest paper-source listed; not independently verified here
- [Independent products in real L1: asymptotic midpoint convexity without AUC renormings](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Independent-products-in-real-L1-asymptotic-midpoint-convexity-without-AUC-renormings-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Independent-products-in-real-L1-asymptotic-midpoint-convexity-without-AUC-renormings-September-27-2026/README.md) · manifest paper-source listed; not independently verified here
- [Midpoint convexity from two recursive potentials](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Midpoint-convexity-from-two-recursive-potentials-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Midpoint-convexity-from-two-recursive-potentials-September-27-2026/README.md) · manifest paper-source listed; not independently verified here

#### 332. Metric Markov cotype of ℓ1 and Hilbert-space Lipschitz extension.

- [Metric Markov Cotype Two of ℓ1](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/l1-markov-cotype.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/README.md) · not independently verified here


### Differential geometry

#### 333. Smooth isometric immersions of surfaces into ℝ4.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/333.md)
- [Smooth isometric immersions of closed surfaces into Euclidean four-space](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Smooth-isometric-immersions-of-closed-surfaces-into-Euclidean-four-space-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Smooth-isometric-immersions-of-closed-surfaces-into-Euclidean-four-space-September-23-2026/README.md) · not independently verified here

#### 334. A smooth surface metric with no local isometric immersion in ℝ3.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/334.md)
- [A Smooth Metric with No Local Isometric Immersion into Three-Space](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 335. Gromov’s integral scalar-curvature bound for simplicial volume.

- [An integral scalar curvature bound for real simplicial volume](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/v126-proof.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/README.md) · not independently verified here
- [Positive scalar curvature forces rational inessentiality](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026/README.md) · not independently verified here

#### 336. Spectral scalar curvature, Urysohn width, and macroscopic dimension.

- [Spectral scalar curvature and uniform Urysohn width](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Spectral-scalar-curvature-and-uniform-Urysohn-width-October-5-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Spectral-scalar-curvature-and-uniform-Urysohn-width-October-5-2026/README.md) · not independently verified here
- [Spectral scalar curvature and Urysohn width in dimension three](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Spectral-scalar-curvature-and-Urysohn-width-in-dimension-three-October-5-2026/spectral-urysohn-three-manifolds.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Spectral-scalar-curvature-and-Urysohn-width-in-dimension-three-October-5-2026/README.md) · not independently verified here
- [Positive scalar curvature and uniform codimension-two width](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positive-scalar-curvature-and-uniform-codimension-two-width-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positive-scalar-curvature-and-uniform-codimension-two-width-September-23-2026/README.md) · not independently verified here

#### 337. Sharp Cartan–Hadamard isoperimetry and rigidity.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/337.md)
- [Generalized Cartan–Hadamard isoperimetry and Euclidean equality rigidity](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026/README.md) · not independently verified here
- [Sharp integral fillings in CAT(0) spaces](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/README.md) · not independently verified here

#### 338. Yau's uniformization conjecture.

- [Uniformization of complete Kähler manifolds with positive bisectional curvature](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/README.md) · not independently verified here

#### 339. Katok's entropy rigidity conjecture.

- [Entropy equality and local symmetry in negative curvature](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Entropy-equality-and-local-symmetry-in-negative-curvature-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Entropy-equality-and-local-symmetry-in-negative-curvature-September-23-2026/README.md) · not independently verified here

#### 340. A counterexample to the nearby Lagrangian conjecture.

- [A counterexample to the nearby Lagrangian conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-the-nearby-Lagrangian-conjecture-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-the-nearby-Lagrangian-conjecture-September-23-2026/README.md) · not independently verified here

#### 341. Donaldson's hypersymplectic deformation conjecture.

- [Deforming hypersymplectic four-manifolds to hyperkähler triples](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-October-7-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-October-7-2026/README.md) · proof_statement_hypothesis_or_citation_correction; not independently verified here

#### 342. Donaldson's tamed-to-compatible conjecture.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/342.md)
- [Taming implies compatibility on four-manifolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/README.md) · proof_statement_hypothesis_or_citation_correction; not independently verified here

#### 343. Symplectic ball packing in higher dimensions.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/343.md)
- [Symplectic Ball Packings in Higher Dimensions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026/README.md) · not independently verified here

#### 344. The metric Blaschke conjecture.

- [The metric Blaschke theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-metric-Blaschke-theorem-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-metric-Blaschke-theorem-September-23-2026/README.md) · not independently verified here

#### 345. Infinitely many closed geodesics on Riemannian spheres and closed three-manifolds.

- [Infinitely many closed geodesic images on every Riemannian sphere](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/README.md) · not independently verified here

#### 346. Sharp singular-set bounds for stationary integral varifolds.

- [A Codimension-One Bound for the Singular Set of a Stationary Integral Varifold](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/varifold-singular-dimension.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/README.md) · not independently verified here
- [Almost-everywhere regularity of stationary integral varifolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/README.md) · not independently verified here

#### 347. Counterexamples to stable-Morse and strong Arnold fixed-point bounds.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/347.md)
- [Hamiltonian Fixed Points Below the Stable Morse Number in Dimension Twenty-Two](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/hamiltonian-fixed-points-below-stable-morse-number.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/README.md) · not independently verified here
- [Sharpness of the Cyclic Integral Floer Bound Below the Stable Morse Number](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/sharp-cyclic-integral-floer-bound-below-stable-morse-number.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/README.md) · not independently verified here
- [Hamiltonian Fixed Points Below the Stable Morse Number](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/README.md) · not independently verified here
- [A nondegenerate counterexample to the Morse-number Arnold bound](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/README.md) · not independently verified here
- [Three fixed points on the symplectic quadric threefold](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 348. Nonnegative-curvature Einstein classification and an L2 topological gap.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/348.md)
- [Zero-Plane Rigidity for Einstein Four-Manifolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/einstein-boundary.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/README.md) · not independently verified here
- [An L² Einstein Gap for Nonnegatively Curved Four-Manifolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/einstein-gap.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/README.md) · not independently verified here
- [Positively curved Einstein four-manifolds](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/README.md) · not independently verified here

#### 349. The Solomon–Yau least-volume conjecture.

- [The Solomon–Yau least-volume theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/README.md) · not independently verified here

#### 350. Yau’s nodal bounds: surfaces and higher dimensions.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/350.md)
- [Sharp nodal length on smooth surfaces](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-nodal-length-on-smooth-surfaces-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-nodal-length-on-smooth-surfaces-September-23-2026/README.md) · not independently verified here
- [Smooth counterexamples to Yau's nodal upper bound in dimensions three and four](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/README.md) · manifest paper-source listed; not independently verified here
- [Power-law violations of Yau's nodal upper bound](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 351. Scalar curvature and finite-time Ricci-flow singularities.

- [A closed Ricci flow with bounded scalar curvature and finite-time curvature blowup](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/README.md) · not independently verified here
- [Bounded scalar curvature and smooth extension of four-dimensional Ricci flow](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/README.md) · not independently verified here
- [Path selection and an elliptic inequality on degenerating Ricci-flat trees](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/README.md) · not independently verified here

#### 352. A finite-time singularity of Calabi flow.

- [A finite-time singularity of Calabi flow on projective space](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/README.md) · not independently verified here

#### 353. Affine Bernstein rigidity through dimension nine and a smooth dimension-ten counterexample.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/353.md)
- [A Smooth Nonquadratic Entire Affine Maximal Graph in Dimension Ten](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Smooth-Nonquadratic-Affine-Maximal-Graph-in-Dimension-Ten-October-5-2026/affine-maximal-dimension-ten.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Smooth-Nonquadratic-Affine-Maximal-Graph-in-Dimension-Ten-October-5-2026/README.md) · not independently verified here
- [The affine Bernstein theorem in dimensions three through nine](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-affine-Bernstein-theorem-in-dimensions-three-through-nine-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-affine-Bernstein-theorem-in-dimensions-three-through-nine-September-24-2026/README.md) · not independently verified here

#### 354. The isoperimetric profile of the cubic three-torus.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/354.md)
- [The Isoperimetric Conjecture for the Cubic Flat Three-Torus](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Isoperimetric-Conjecture-for-the-Cubic-Flat-Three-Torus-September-24-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Isoperimetric-Conjecture-for-the-Cubic-Flat-Three-Torus-September-24-2026/README.md) · not independently verified here

#### 355. Unique tangent flows at the first surface singularity.

- [Uniqueness of tangent flows at the first singular time of embedded surface mean-curvature flow](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Tangent-flow-uniqueness-2026-09-24/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Tangent-flow-uniqueness-2026-09-24/README.md) · not independently verified here

#### 356. Gigli’s characterization of Alexandrov curvature.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/356.md)
- [Gigli’s distributional curvature characterization of Alexandrov spaces](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/README.md) · not independently verified here
- [Weak Hessian bounds along every geodesic in RCD spaces](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/weak-hessian-geodesics.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 357. Bi-Lipschitz coordinates at every regular RCD point.

- [Bi-Lipschitz Coordinates at Regular Points of Noncollapsed RCD Spaces](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bi-Lipschitz-Coordinates-at-Regular-Points-of-Noncollapsed-RCD-Spaces-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bi-Lipschitz-Coordinates-at-Regular-Points-of-Noncollapsed-RCD-Spaces-September-25-2026/README.md) · not independently verified here

#### 358. A three-manifold without conjugate points or nonpositive curvature.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/358.md)
- [A Three-Manifold Without Conjugate Points and Without a Nonpositively Curved Metric](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 359. Negative Kähler curvature without bounded holomorphic coordinates.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/359.md)
- [A negatively pinched Kähler threefold without bounded holomorphic coordinates](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/README.md) · manifest paper-source listed; not independently verified here
- [One-sided negative sectional curvature and the holomorphic Liouville property](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/README.md) · not independently verified here

#### 360. Weak MTW curvature gives convexity and regular optimal transport.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/360.md)
- [Global Support and Convex Injectivity Domains under Weak MTW](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/README.md) · manifest paper-source listed; not independently verified here
- [Uniform Bi-Holder Transport from Weak MTW](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026/README.md) · manifest paper-source listed; not independently verified here

#### 361. Failure of integer-degree harmonic dimension comparison.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/361.md)
- [A counterexample to integer-degree harmonic dimension comparison](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/README.md) · manifest paper-source listed; not independently verified here
- [A Three-Dimensional Counterexample to Integer-Degree Harmonic Dimension Comparison](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026/README.md) · not independently verified here


### Partial differential equations

#### 362. Global smoothness for relativistic Vlasov–Maxwell.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/362.md)
- [Global classical solutions of the three-dimensional relativistic Vlasov–Maxwell system](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 363. Nonuniqueness with local conservation for the hard-sphere Boltzmann equation.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/363.md)
- [Nonuniqueness with local conservation for the hard-sphere Boltzmann equation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nonuniqueness-with-local-conservation-for-the-hard-sphere-Boltzmann-equation-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nonuniqueness-with-local-conservation-for-the-hard-sphere-Boltzmann-equation-October-5-2026/README.md) · not independently verified here
- [Nonuniqueness for the periodic hard-sphere Boltzmann equation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nonuniqueness-for-the-periodic-hard-sphere-Boltzmann-equation-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nonuniqueness-for-the-periodic-hard-sphere-Boltzmann-equation-September-23-2026/README.md) · not independently verified here

#### 364. Kinetic limits and fluctuations over the Boltzmann lifespan.

- [The Boltzmann–Grad limit for stable radial potentials on regular kinetic intervals](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Boltzmann-Grad-limit-for-stable-radial-potentials-on-regular-kinetic-intervals-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Boltzmann-Grad-limit-for-stable-radial-potentials-on-regular-kinetic-intervals-September-23-2026/README.md) · not independently verified here
- [Hard-sphere fluctuations on the regular Boltzmann lifespan](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Hard-sphere-fluctuations-on-the-regular-Boltzmann-lifespan-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Hard-sphere-fluctuations-on-the-regular-Boltzmann-lifespan-September-23-2026/README.md) · not independently verified here

#### 365. Joint metric and connection recovery from one boundary patch.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/365.md)
- [Determination of a metric and a unitary connection from one boundary patch](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Determination-of-a-metric-and-a-unitary-connection-from-one-boundary-patch-October-5-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Determination-of-a-metric-and-a-unitary-connection-from-one-boundary-patch-October-5-2026/README.md) · not independently verified here
- [Smooth anisotropic uniqueness in the Calderón problem from one boundary patch](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/README.md) · not independently verified here
- [Nonuniqueness for bounded measurable scalar conductivities in three dimensions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026/README.md) · manifest paper-source listed; not independently verified here

#### 366. The planar Mumford–Shah regularity conjecture and local weak-L4 gradient bounds.

- [Interior regularity of planar Mumford–Shah minimizers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Interior-regularity-of-planar-Mumford-Shah-minimizers-September-24-2026/Interior-regularity-of-planar-Mumford-Shah-minimizers-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Interior-regularity-of-planar-Mumford-Shah-minimizers-September-24-2026/README.md) · not independently verified here

#### 367. The critical dimension for the one-phase Bernoulli problem.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/367.md)
- [The critical dimension for one-phase Bernoulli minimizers](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/README.md) · not independently verified here

#### 368. The three-dimensional Ball–Evans approximation problem.

- [Strong diffeomorphic approximation in three dimensions for 1≤p≤2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/README.md) · not independently verified here
- [Strong diffeomorphic approximation in three dimensions for p>2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/README.md) · not independently verified here

#### 369. The hot spots conjecture for simply connected planar domains.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/369.md)
- [Strict hot spots and absence of interior critical points on smooth simply connected planar domains](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/main.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/README.md) · not independently verified here

#### 370. The Lane–Emden and Hénon–Lane–Emden conjectures.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/370.md)
- [The Subcritical Hénon–Lane–Emden Conjecture](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/README.md) · manifest paper-source listed; not independently verified here

#### 371. Stable blowup for the defocusing Schrödinger equation.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/371.md)
- [Stable self-similar blowup for a supercritical defocusing Schrödinger equation on the torus](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Stable-Self-Similar-Blowup-for-a-Supercritical-Defocusing-Schrodinger-Equation-on-the-Torus-September-24-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Stable-Self-Similar-Blowup-for-a-Supercritical-Defocusing-Schrodinger-Equation-on-the-Torus-September-24-2026/README.md) · not independently verified here

#### 372. Global uniqueness in smooth isotropic elasticity.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/372.md)
- [Global Uniqueness for the Smooth Isotropic Elasticity Inverse Problem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026/README.md) · not independently verified here

#### 373. Nonattainment of the three-marginal Coulomb Monge problem.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/373.md)
- [A counterexample to the Monge ansatz for the three-marginal Coulomb cost](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-the-Monge-ansatz-for-the-three-marginal-Coulomb-cost-September-25-2026/paper.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-counterexample-to-the-Monge-ansatz-for-the-three-marginal-Coulomb-cost-September-25-2026/README.md) · not independently verified here

#### 374. Sharp one-third stability of Brenier maps.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/374.md)
- [Sharp One-Third Stability of Brenier Maps](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/README.md) · not independently verified here

#### 375. De Giorgi's conjecture in dimension eight.

- [A positive resolution of De Giorgi's conjecture in dimension eight](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/article.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/README.md) · not independently verified here

#### 376. Universal computation in forced Navier–Stokes flows.

[Family formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/376.md)
- [Finite Instructions and Solenoidal Shear Flows](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-Instructions-and-Solenoidal-Shear-Flows-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-Instructions-and-Solenoidal-Shear-Flows-September-27-2026/README.md) · not independently verified here
- [A Fixed Particle Test for Computation in a Forced Viscous Flow](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Fixed-Particle-Test-for-Computation-in-a-Forced-Viscous-Flow-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Fixed-Particle-Test-for-Computation-in-a-Forced-Viscous-Flow-September-27-2026/README.md) · not independently verified here
- [Universal Computation with Eventually Stationary Navier–Stokes Forcing](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/README.md) · not independently verified here
- [Geometric Programs for Solenoidal Forcing](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Geometric-Programs-for-Solenoidal-Forcing-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Geometric-Programs-for-Solenoidal-Forcing-September-27-2026/README.md) · not independently verified here
- [Prefix Instructions and Incompressible Flows](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Prefix-Instructions-and-Incompressible-Flows-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Prefix-Instructions-and-Incompressible-Flows-September-27-2026/README.md) · not independently verified here
- [Computation under Rapidly Vanishing Navier–Stokes Forcing](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/README.md) · not independently verified here
- [Velocity-Field Detection of Computation in Forced Navier–Stokes Flows](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026/README.md) · not independently verified here
- [Scalar Potentials and Slow Clocks for Forced Fluid Computation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Scalar-Potentials-and-Slow-Clocks-for-Forced-Fluid-Computation-September-27-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Scalar-Potentials-and-Slow-Clocks-for-Forced-Fluid-Computation-September-27-2026/README.md) · not independently verified here
- [Incompressible Box Transport and Finite Computation](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Incompressible-Box-Transport-and-Finite-Computation-October-6-2026/manuscript.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Incompressible-Box-Transport-and-Finite-Computation-October-6-2026/README.md) · proof_statement_hypothesis_or_citation_correction; not independently verified here

#### 377. Interior $C^{1,\alpha}$ regularity for infinity-harmonic functions.

- [Uniform Interior $C^{1,\alpha}$ Estimates for Infinity-Harmonic Functions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Interior-C1alpha-Estimates-for-Infinity-Harmonic-Functions-October-4-2026/interior-c1-infinity-harmonic.pdf) · [citation/version notes](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Uniform-Interior-C1alpha-Estimates-for-Infinity-Harmonic-Functions-October-4-2026/README.md) · not independently verified here

