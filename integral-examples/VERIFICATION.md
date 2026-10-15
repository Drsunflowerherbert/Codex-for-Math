# Verification ledger

The collection contains 16 original worked expositions. Every example received
an independent mathematical review by a model agent other than its author.
These are recorded mathematical audits, with source and computation checks;
**no human peer review or proof-assistant verification is claimed**.

## Independent review of each example

| Examples | Author role | Independent reviewer role | Evidence and disposition |
|---|---|---|---|
| E01–E04 | Lebesgue examples author | Geometry examples author | [Review](reviews/review-E01-E04.md): all pass; E04's symmetric truncation is explicitly a subset of its open domain. |
| E05, E06, E14–E16 | Parameters/convergence author | Area/coarea author | [Review](reviews/review-E05-E06-E14-E16.md): all pass; E14's real-measurable assumptions, diagonal subsequence, and source references clarified. |
| E07–E10 | Geometry examples author | Parameters/convergence author | [Review](reviews/review-E07-E10.md): all pass; no mathematical changes requested. |
| E11–E13 | Area/coarea author | Lebesgue examples author | [Review](reviews/review-E11-E13.md): all pass; E13's empty-interior argument and description of shrinking sets clarified. |

The reviewer checked analytic assumptions and derivations, not just final
answers. The author signed off the recorded changes. Each review contains
SHA256 hashes of the exact reviewed Markdown files; the
[review manifest](reviews/review-manifest.json) and collection checker detect
changes after review. No reviewer reviewed their own examples.

The [global review](reviews/global-review.md) separately audits the guide,
Hausdorff normalization, theorem dimensions and hypotheses, scalar versus
oriented integration, source locators, counterexample atlas, and retrieval
metadata. One repaired global statement now restricts sigma-finiteness to the
Lebesgue/counting product factors: ambient lower-dimensional Hausdorff measure
need not be sigma-finite. The source audit found dimensional misprints in older
notes and selected the corrected Simon 2018 area statement.

## Concrete computation checks

Run `python3 integral-examples/checks/check_examples.py` from the repository root.
The recorded run in [check-results.json](checks/check-results.json) performed
**92 concrete checks with zero failures**, using SymPy 1.14.0 and mpmath 1.3.0.
The JSON records every identity, method, expected value, result, input hash,
package version, and computational limitation.

| Example | Concrete checks | What those checks support |
|---|---:|---|
| E01 | 4 | Antiderivative, final value, series coefficient, quadrature in the original order |
| E02 | 4 | Finite-stage length recurrence/sums and weighted product computation |
| E03 | 0 | Proof-only: a nonmeasurable set and the null-envelope argument are not computationally verified |
| E04 | 8 | Primitive identities, iterated values, finite rectangle bound, section quadratures |
| E05 | 3 | Exact finite support sums and rectangular exhaustion identities |
| E06 | 6 | Parameter derivatives, exponential integral, positive/reversed/equal parameter quadratures |
| E07 | 5 | Speed, weighted length, unweighted length, quadratures |
| E08 | 5 | Speed/circulation density and once/twice trigonometric integrals |
| E09 | 5 | Gram determinant, height and area integrals, quadratures |
| E10 | 5 | Spherical Gram determinant, moment, area, cap formulas |
| E11 | 6 | Fold determinant, multiplicity-weighted and once-counted integrals |
| E12 | 11 | Radial Jacobian integrals, power thresholds/formulas, selected quadratures |
| E13 | 8 | Exact finite-stage Cantor lengths/slopes/masses; no infinite-stage theorem inferred |
| E14 | 4 | Exact mass and finite tail/convergence-set identities |
| E15 | 10 | Parameter derivative, antiderivative, symbolic endpoint expression, scaled quadratures |
| E16 | 8 | Kernel mass, first moment, exponential test-function values, quadratures |

The mpmath checks use 70 decimal digits and an absolute-or-relative comparison
tolerance of $10^{-50}$. This is a numerical consistency test, **not a certified
quadrature error bound**. Exact symbolic checks are recorded separately.

Neither symbolic integration nor finite numerical sampling proves
measurability, absolute integrability, a limit exchange, a general fiber count,
or an infinite-stage Cantor assertion. Those are justified by the written
arguments and theorem hypotheses. E03 is explicitly marked proof-only; E13's
checks concern finite stages only. No Lean files are supplied or Lean
verification asserted for this collection.

## Structural and document checks

- [check_collection.py](checks/check_collection.py) validates all 16 IDs,
  mandatory sections, source IDs, metadata arrays, local file links, exact
  review hashes, computation-result hashes, retrieval commands, required
  deliverables, and the restriction to `integral-examples/` changes.
- [metadata.schema.json](metadata.schema.json) documents the retrieval schema.
  The standard-library checker validates the required invariants directly;
  it does not claim to implement a complete JSON Schema engine.
- [build.py](build.py) generates the retained LaTeX from the Markdown and
  compiles that exact LaTeX with pdfLaTeX. The
  [build record](checks/pdf-build.json) identifies source/output hashes,
  tool versions, and any remaining layout warnings.
- [collection-check.json](checks/collection-check.json) records structural
  verification and final PDF/LaTeX hashes. PDF text and representative pages
  are also inspected during publication preparation.

## Publication scope and remaining limits

The base and fetched public branch heads are recorded in
[repository-base.json](checks/repository-base.json). The publication branch is
`codex/integral-examples-2026-10-15`, based on
`e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f`. All additions are under
`integral-examples/`. Publication uses an ordinary push to the new branch,
without a pull request, force push, merge, or modifications to other branches.
The final task response identifies the actual published commit and verification
of remote contents. This source document deliberately does not predict its own
future commit hash.

The earlier paper was not supplied or used. The collection is a checked first
batch, not an exhaustive atlas of all integration theorems. Its general
Lebesgue, area, and coarea theorems remain prerequisites, cited in
[SOURCES.md](SOURCES.md). Source PDFs are linked rather than redistributed;
online versions can change. Recorded review does not remove the value of
checking a theorem's precise hypotheses when adapting an example to a new map,
measure, signed weight, or unbounded domain.
