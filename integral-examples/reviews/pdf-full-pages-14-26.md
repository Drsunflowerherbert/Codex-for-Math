# Full PDF visual inspection: pages 14–26

Review date: 2026-10-15. Reviewer: source/conventions auditor agent, assigned
only physical PDF pages 14 through 26 inclusive for this visual pass.

PDF: `pdf/integral-examples.pdf`.

Exact PDF SHA256:
`9d03d22882d87c4be3b40b2e7b21972bc159c5f15f3ed4522e4a0547a256f068`.

Each of the **13 pages was actually opened and visually inspected individually**
with `view_image`, using its separate `full-14.png` through `full-26.png` render
at an 1800-pixel long side. Images were supplied with original detail. The PDF
hash was checked before and after the visual pass; image dimensions were also
confirmed. These programmatic checks support the visual review and do not
replace it. No montage, OCR-only check, or text extraction was used as a
substitute for opening any page.

The inspection covered every visible heading, paragraph, bullet, reference,
displayed and inline formula, code-style tag, and page number in the assigned
range. There are no tables in this range. The criteria were clipping,
overlapping content, illegibility, omitted or substituted mathematical glyphs,
and pagination/rendering defects. This is a visual document audit; the separate
mathematical reviews retain their stated scope.

| PDF page | Content visually inspected | Status and findings |
|---:|---|---|
| 14 | E02 reusable technique and sources; E03 problem, hypotheses, Vitali-set explanation, null-envelope calculation, and first solution step. | **Pass.** All text, superscripts, set operations, indicator symbols, and displayed bounds are readable. No clipping, collision, or missing glyph observed. |
| 15 | E03 exceptional section, interpretation of the outer integral, general section proof, completed-product applicability discussion. | **Pass.** Section subscripts, symmetric differences, null-set formulas, and the sigma-algebra tensor notation render clearly. Paragraph and formula spacing is intact. |
| 16 | E03 pitfalls, tags and sources; E04 title, problem, kernel definition, hypotheses and signed-integral convention. | **Pass.** The long E04 title wraps cleanly onto its second line. The fraction, powers, sign parts and infinity symbol are legible, without overlap or cropping. |
| 17 | E04 two iterated-integral computations; boxed positive/negative values; start of the explicit rectangle argument. | **Pass.** Derivative operators, evaluation brackets, nested integral limits, inequalities and rectangle exponents are complete and readable. Both answer boxes fit. |
| 18 | E04 disjoint-rectangle divergence, positive/negative parts, symmetric truncation, applicability and pitfalls. | **Pass.** The aligned finite sums, infinity statements and truncated-square integral render completely. Text and formulas remain separated and within the page. |
| 19 | E04 reusable technique and sources; E05 problem, piecewise signed matrix, counting-measure hypotheses and row-first sums. | **Pass.** The piecewise brace, all three cases, countable-measure symbols and nested sums are readable. The long E05 title remains fully visible. |
| 20 | E05 column-first sums, absolute divergence, finite rectangles, applicability, pitfalls and reusable technique. | **Pass.** Dense sums and their index limits, the finite-rectangle identity, tensor products and wrapped tags are complete. No collision with the footer. |
| 21 | E05 sources; E06 problem, parameter/measure hypotheses, positive kernel representation, Tonelli computation and endpoint estimate. | **Pass.** Exponential superscripts, double-integral limits, boxed logarithm and absolute-value estimate are legible and fit on the page. |
| 22 | E06 tail estimate, local derivative bound, dominated-convergence exchange, applicability, pitfalls and tags. | **Pass.** The derivative subscripts, parameter-neighborhood endpoints, common majorant and improper limits render correctly. Wrapped prose and tags are readable. |
| 23 | E06 sources; E07 problem, explicit normalized Hausdorff definition, parametrization, speed and weighted-length computation. | **Pass.** The cover infimum, summation/union limits, measure restriction, prime marks, radicals and boxed value are all visible with no missing glyph. |
| 24 | E07 arc-length calculation, inverse-hyperbolic-sine identity, applicability, pitfalls, tags and Simon reference. | **Pass.** The length box, logarithm and radical notation are complete; source link text and section/theorem references remain readable. |
| 25 | E08 problem, normalized length/multiplicity hypotheses, double-circle parameter computation, fiber count and weighted area identity. | **Pass.** The long heading, trigonometric powers, fiber-count expression, weighted sum with its subscript and final boxed scalar integral fit and are legible. |
| 26 | E08 single traversal, circulation and flux/orientation comparisons, applicability, pitfalls and reusable technique. | **Pass.** Vector dot products, signs, normal notation and boxed circulation are readable. Bullets, tags and the page number do not overlap. |

**Disposition:** all 13 assigned pages pass this visual inspection. No defect
requiring repair was found. No PDF, LaTeX source, example, existing review, or
Git state was modified during this pass. Any later rebuild producing a different
PDF hash requires checking which visual-review conclusions still apply.
