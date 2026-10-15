# Independent PDF and text review

Reviewer: geometry author, independently checking the root author's PDF build. Date: 2026-10-15. Disposition: **pass; no blocking rendering or navigation defect found in the reviewed candidates**.

## Exact reviewed artifacts

| Artifact | Pages | SHA-256 |
| --- | ---: | --- |
| `pdf/integral-examples.pdf` | 52 | `9d03d22882d87c4be3b40b2e7b21972bc159c5f15f3ed4522e4a0547a256f068` |
| `pdf/guide.pdf` | 10 | `f7a0010d91ac5a95cb7fc1df69109912296fb552f9bbcf6985cea91059d3e814` |

These are the final candidate hashes supplied by the builder and independently recomputed from the files inspected. A later PDF rebuild changes the reviewed artifacts and requires checking the new hashes and affected layouts again.

## Scope and procedure

- Inspected both retained LaTeX sources and extracted PDF text using `pdftotext -layout`.
- Checked every page's extracted word bounding boxes with PyMuPDF: no word extends outside its physical page. This is a physical-page clipping check, not proof that every mathematical glyph is correct.
- Checked PDF outlines, named destinations, and problem-index link targets programmatically. Named internal destinations are reported as link kind 4 by this PyMuPDF installation and were checked by their resolved page fields, rather than incorrectly requiring link kind 1.
- Rendered sample pages at 105 dpi with `pdftoppm` and inspected the resulting images using `view_image`. Full collection pages: **8, 23, 25, 27, 28, 29, 30, 34, 37, 46**. Guide pages: **3, 5**. The temporary renders were kept outside the repository in `/tmp/integral-pdf-qa/` during review.

The inspection samples the rendered pages; it does not claim that every page received a visual inspection. All 62 pages received the text, bounds, and destination checks described above. The mathematical example reviews remain separate from this production review.

## Findings

**Normalization and mathematical notation.** The normalized Hausdorff definition is readable in both PDFs, including the unit-ball factor, diameter exponent, sum, covering union, and limiting scale. The agreement with Lebesgue measure on planes and the counting interpretation of zero-dimensional measure appear in the text. Greek letters, superscripts, square roots, integrals, fiber sums, matrix entries, and boxed results display clearly on the inspected pages. No missing mathematical expression or clipped formula was found in those samples. Text extraction found no replacement-character glyphs and no unresolved `??` label markers in either PDF.

**Geometry pages.** The parabola speed and weighted integral, circle multiplicity count and fiber sum, paraboloid Gram matrix and area factor, and sphere angular chart, Jacobian, moment, and cap area all render legibly. Multi-line derivations remain in their proper order. The sphere's omitted-meridian explanation continues normally across pages 29–30. The coarea formula and critical-point treatment on page 34 and Cantor-map counting formula on page 37 are also readable. The scalar-versus-orientation discussion is retained in extracted text.

**Problem index and atlas.** The guide's problem table has separated columns and readable wrapped rows, with no computed answers inserted into the problem-index table. The atlas's failure and sufficient-condition columns remain distinguishable and readable on full-collection page 46. Text continuing on subsequent pages is present in extraction; no row omission was detected.

**Navigation.** The full PDF has 156 outline entries, including all 16 example headings. Its 184 resolved destination links have valid target pages. The 16 problem-index entries resolve, in example order, to pages **9, 12, 14, 16, 19, 21, 23, 25, 27, 29, 31, 34, 36, 39, 41, 43**, matching the example headings. The guide has 23 outline entries and 33 valid resolved internal destinations. Its 16 solution links point to the corresponding example paths on the publication branch; these are external GitHub links because the guide omits the worked solutions. This checks URL routing and path identity, not the availability of an unpublished remote branch at review time.

**Build diagnostics.** The builder reports no overfull boxes or undefined labels and records one underfull paragraph as a spacing-only warning. The inspected layouts show no resulting legibility problem. This reviewer did not modify the examples, their locked mathematical review hashes, or either PDF.

## Limits and remaining gaps

No PDF-production blocker remains for these exact hashes. Rendered visual inspection was sampled as specified above. Accessibility tagging, screen-reader reading order for formulas, every possible PDF viewer's behavior, live remote-link availability, and human peer review were not certified. The review makes no claim of Lean or other formal verification.
