# Full-solutions PDF visual QA: pages 40–52

Reviewer: `author_parameters` agent. Date: 2026-10-15. Scope: **each of the 13 physical PDF pages 40 through 52, inclusive**, inspected individually as rendered page images using `view_image`. This audit covers rendering and readability, not an additional mathematical-proof review.

PDF: `pdf/integral-examples.pdf`

Exact SHA-256: `9d03d22882d87c4be3b40b2e7b21972bc159c5f15f3ed4522e4a0547a256f068`

The PDF byte hash was independently calculated and matched the locked hash supplied for this audit. Each supplied PNG is 1391 × 1800 pixels, with no contact-sheet reduction. The image paths were `/tmp/integral-full-page-qa/full-40.png` through `full-52.png`. Every listed image was actually opened and visually inspected; text extraction and symbolic checks were not used as substitutes.

## Per-page inspection

| Physical page | Status | Content inspected | Findings |
| --- | --- | --- | --- |
| 40 | Visually inspected — pass | E14 solution: concentration, escape, dilution; beginning of sufficient conditions | All display integrals, indicators, limits, bullet text and page boundaries are legible and complete. |
| 41 | Visually inspected — pass | E14 sufficient conditions, truncation/diagonal proof, pitfalls, tags and sources; E15 heading and piecewise problem | Dense inline formulas and subscripts remain legible. The piecewise definition is complete above the footer; the wrapped E15 heading is clear. |
| 42 | Visually inspected — pass | E15 hypotheses and full computation of the boundary layer and derivative-family obstruction | Fractions, one-sided derivatives, arrows, integration limits and shrinking-interval formulas are readable; no text or formula clips. |
| 43 | Visually inspected — pass | E15 differentiation theorem, pitfalls, tags and sources; E16 heading and problem limit | The derivative-of-integral display and its evaluation bar render clearly. Source links and the final approximate-identity display are complete. |
| 44 | Visually inspected — pass | E16 kernel data, rescaled DCT proof, epsilon/tail estimate and Lipschitz rate | All normalization, tail and rate displays are complete. The long aligned epsilon/tail estimate fits on the visible page and is readable. |
| 45 | Visually inspected — pass | E16 hypotheses, original-variable obstruction, pitfalls, tags and sources; counterexample atlas introduction | The kernel obstruction display, mathematical glyphs, links, heading and text all render clearly. |
| 46 | Visually inspected — pass | Counterexample atlas table, first seven rows | All three columns, header, row content, mathematical symbols and wrapping are readable without overlap or truncation. |
| 47 | Visually inspected — pass | Counterexample atlas table continuation and conclusion; sources audit introduction and Hunter source entry | The repeated table header and both remaining rows are present and clear. The lower source list, links and concluding paragraph fit safely above the footer. |
| 48 | Visually inspected — pass | Axler, Simon and Hajlasz geometry source entries, normalizations and source cautions | The dense source locators, superscripts, symbols, links and literal code identifiers are legible and stay on the page. |
| 49 | Visually inspected — pass | Hajlasz analysis and Conrad source entries; version conventions; verification ledger introduction | All source notes and inline formulas are readable. The bold review-limits statement at the bottom is complete. |
| 50 | Visually inspected — pass | Independent-review table; review explanation; computation-check introduction and table rows E01–E04 | Review table cells wrap clearly. The computation table begins with a readable header and all displayed E01–E04 cells are complete above the footer. |
| 51 | Visually inspected — pass | Computation table continuation E05–E16; computational limitations; structural checks; publication-scope beginning | Repeated computation-table header and every remaining row are readable. The long hash, code paths, tolerance exponent, links and bottom continuation render without clipping. |
| 52 | Visually inspected — pass | Final publication-scope continuation and remaining limits | Final two paragraphs and link are complete and legible. Remaining whitespace is expected on the last page; page number is clear. |

## Additional inspection of dense or potentially ambiguous areas

- Page 44: compared the long aligned epsilon/tail estimate with `pdf/integral-examples.tex` and the source display in E16. Its complete two-integral right-hand side and following bound are visible, with no clipped operator or differential. PDF word-position extraction supported the visual finding; it did not replace it.
- Page 47: visually checked the repeated three-column atlas header and the E12/E13 continuation rows again using a fresh single-page render of the locked PDF. The fresh PNG SHA-256 matched the supplied page image exactly (`b5ee96b351cd6cc2540d6d107479c4ffde1115077b21f7da0b234cd16c29c2b8`); the header is present and legible.
- Pages 50–51: inspected both sides of the computation-table page break. The header repeats, E04 ends completely on page 50, and E05 starts on page 51; no row content is missing.

## Rendered input hashes

These hashes identify the exact page images inspected, not mathematical certification.

| Physical page | PNG SHA-256 |
| --- | --- |
| 40 | `884367c9eb3ad3ab696c279765fa4215594e4158439eebadc217f84bb785ba82` |
| 41 | `ba5d1fa6e28d7d5a168742dca46bcaf824d68b2a88e178436a8e392bc5940e92` |
| 42 | `2c517ac1d3398d0c5f5729280cd4f5ae58996d431cf9ffc83ea4e266d34ac486` |
| 43 | `0de54ed2a49941063cb370c916a5aed5f36ec22ccdeea42e8036ec5f306c13bd` |
| 44 | `cd4535faafe90ff1e8ee6fca67ac58a6e65f4d8d783b98890a2bbdf52e652bc1` |
| 45 | `f8ee1bbd78a9b89b53de3ff5e8d71754570c5b84b0418f1d62343c2cd1119666` |
| 46 | `0a4610389f9aa04dc36abdc1a50c65cd3a5caa3a3442c451b576f6dc6605dc82` |
| 47 | `b5ee96b351cd6cc2540d6d107479c4ffde1115077b21f7da0b234cd16c29c2b8` |
| 48 | `471afea50cd9f638e7f99ab43a487609190ffd4e42c4595f970ecdc92319fbc4` |
| 49 | `a108c90536315fba212eb165e4a43961af27faeadf8a9d237bd1f97e71e6ee65` |
| 50 | `018a7715891edac0776a2086d84fdbdbc0216087b148165bc8d47c02ac14c13c` |
| 51 | `26ee0c7ee907d61e20dbb0f564266aea9cd9fef4a5821eb902979c2b46ebb379` |
| 52 | `4aeaa67a94b0ac2c401b68d10c5594a45292bf395fa183d9ee5610857c4324a9` |

## Disposition

**All 13 pages pass visual QA.** No clipping, illegible text, missing mathematical glyphs, overlapping content, truncated formulas or damaged table cells were found. No changes to the PDF, examples, existing reviews or git state were made for this audit. This report applies only to the exact PDF hash above and must be revisited if that PDF changes.
