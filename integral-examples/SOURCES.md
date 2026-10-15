# Sources and conventions audit

All links below were opened and checked on **2026-10-15**. These are author-hosted teaching texts, used for theorem statements and conventions. The worked examples in this directory are original expositions; the linked texts' proofs and problem collections are not reproduced. PDF page numbers below count the cover as page 1. A PDF viewer may display a different logical page label. Online files can change.

## `hunter-measure`

John K. Hunter, *Measure Theory*, University of California, Davis, 2011.
[Author's PDF](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf).

- Monotone convergence: Theorem 4.6, printed p.41, PDF p.45.
- Dominated convergence: Theorem 4.24, printed p.49, [PDF p.53](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf#page=53); a.e. versions are discussed in §4.6, printed p.50.
- Product-measurable sections: §5.1, Proposition 5.2, printed p.55, PDF p.59; function sections: Theorem 5.15, printed p.60.
- Fubini with absolute integrability: Theorem 5.18, printed p.61, [PDF p.65](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf#page=65).
- Completion and exceptional sections: Example 5.20 and Theorem 5.21, printed p.62, [PDF p.66](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf#page=66).

The completed Lebesgue product statement guarantees measurable and integrable sections almost everywhere. It does not guarantee measurability of every section. Theorem 5.15's sentence defining complex section integrals suppresses existence hypotheses; use the explicit integrability hypotheses of 5.18/5.21.

## `axler-mira`

Sheldon Axler, *Measure, Integration & Real Analysis*, Graduate Texts in Mathematics 282, Springer, 2020; author's online revision dated 12 June 2026.
[Author's PDF](https://measure.axler.net/MIRA.pdf).

- Tonelli: §5B, Theorem 5.28, printed p.129, [PDF p.144](https://measure.axler.net/MIRA.pdf#page=144).
- Nonnegative double sums: Corollary 5.31, printed p.131, PDF p.146.
- Fubini: Theorem 5.32, printed p.132, [PDF p.147](https://measure.axler.net/MIRA.pdf#page=147), with exceptional-parameter conventions immediately above and in the proof.

These product theorems assume sigma-finite factors. Tonelli accepts nonnegative product-measurable functions and permits the value infinity; Fubini requires a finite integral of the absolute value. This is an independent reference for the distinction used in the examples. For completed Lebesgue measurability rather than product measurability, also use `hunter-measure` §5.7.

## `simon-gmt`

Leon Simon, *Introduction to Geometric Measure Theory*, Stanford University, 2017/2018 NTU lecture draft; last-update line: 7 March 2018.
[Author's PDF](https://math.stanford.edu/~lms/ntu-gmt-text.pdf).

- Normalization: Chapter 1, definitions 2.1–2.2, printed p.11, [PDF p.9](https://math.stanford.edu/~lms/ntu-gmt-text.pdf#page=9); equality with Lebesgue outer measure: Theorem 2.6, printed p.12, PDF p.10.
- Area and multiplicity: Chapter 2, Theorem 3.3, printed p.57, [PDF p.32](https://math.stanford.edu/~lms/ntu-gmt-text.pdf#page=32); weighted fiber sum: Remark 3.4(2), printed p.58, PDF p.33; curves and submanifolds: Examples 3.5, printed pp.60–61, PDF pp.34–35.
- Coarea: Chapter 2, Theorem 7.3 and weighted Remark 7.4(1), printed p.76, [PDF p.42](https://math.stanford.edu/~lms/ntu-gmt-text.pdf#page=42).
- Critical parts of fibers: Theorem 7.5, printed p.80, PDF p.44; the stronger smooth Sard conclusion is distinguished in Remark 7.6.

The PDF has two printed pages per sheet. This version uses the factor `omega_k / 2^k` multiplying sums of diameter powers, where `omega_k` is unit-ball volume. Consequently normalized Hausdorff measure agrees with Lebesgue measure on k-planes. Counting measure is the k=0 convention.

## `hajlasz-geometry`

Piotr Hajłasz, *Geometric Analysis*, University of Pittsburgh, undated author-hosted lecture notes.
[Author's PDF](https://www.pitt.edu/~hajlasz/Notatki/Analysis_4.pdf).

- Normalization: §3.1, printed/PDF p.19; equality with Lebesgue measure: Theorem 3.2, p.20.
- Surface integration: Theorem 3.17 and following discussion, p.25.
- Area and multiplicity with the Lusin N condition: Theorem 3.18 and Remark 3.19, pp.26–27.
- Coarea: §3.4, Theorem 3.23, pp.28–29; radial slicing and projection/Fubini applications, p.29. Almost-everywhere rectifiability: Theorem 3.24, p.29.

Normalization agrees with `simon-gmt`. Two evident dimensional misprints occur in §3.4: the coarea Jacobian should vanish when the derivative has rank less than **m**, not n; the area half of Theorem 3.23 needs outer measure **H^n**, not H^m. The coarea half uses the correct fiber and target dimensions. Our area statements use Simon's 2018 Theorem 3.3 and Remark 3.4(2), whose dimensions are correct.

## `hajlasz-analysis`

Piotr Hajłasz, *Analysis I*, University of Pittsburgh, undated author-hosted lecture notes.
[Author's PDF](https://www.pitt.edu/~hajlasz/Notatki/Analysis%20I.pdf).

- Theorem 103 and the Cantor staircase discussion, printed/PDF p.76: a continuous increasing function can have derivative zero almost everywhere while its endpoint increment is positive.
- Absolute continuity and the fundamental theorem: §8.1, Theorem 106, printed/PDF pp.77–78.
- Convolution in L1: Theorem 87, pp.66–67; smooth approximate identities: Theorem 92, pp.70–71.

The Cantor paragraph prints `f'(0) = 0 a.e.`; the variable should be x. The example in this library proves its needed staircase properties directly. Derivative values on its exceptional null set may be assigned arbitrarily for Lebesgue integration, but those assignments do not make the staircase absolutely continuous or Lipschitz.

## `conrad-diff`

Keith Conrad, *Differentiating Under the Integral Sign*, University of Connecticut, undated author-hosted expository notes.
[Author's PDF](https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf).

- A sufficient differentiation theorem: §12, Theorem 12.3, printed/PDF p.16.
- Local parameter bounds illustrating the theorem: Table 2, p.16, and discussion on p.17.

Theorem 12.3 treats continuous integrands and parameter derivatives, dominated by parameter-independent integrable majorants near the parameter in question. Its infinite-interval integrals are stated as improper integrals. The library supplies Lebesgue proofs via dominated convergence of difference quotients; it does not silently equate conditional improper integration with Lebesgue integrability.

## Reading formulas across versions

Use the source IDs above, not a theorem number alone: Simon's 2014 and 2018 drafts number area and coarea differently. The older [2014 course draft](https://web.stanford.edu/class/math285/ts-gmt.pdf), printed p.54, formula 3.4, also has the incorrect target dimension H^m; the following weighted formula 3.5 has H^n. The library cites the corrected 2018 area statement.

The convention in this directory is scalar integration against positive measures. A parametrization's area Jacobian is nonnegative and counts repeated coverings. An oriented vector flux additionally needs a chosen normal and a signed dot product; it is not determined by the scalar Hausdorff measure alone.

No source access, symbolic calculation, numerical test, or review recorded here is a claim of proof-assistant verification.
