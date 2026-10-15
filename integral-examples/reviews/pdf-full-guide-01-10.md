# Full visual inspection of guide pages 1–10

Reviewer: primary collection agent, inspecting the rendered output of its own
document build. Date: 2026-10-15. This is model visual production QA, not human
peer review or a new mathematical verification claim.

Exact artifact: `pdf/guide.pdf`, 10 pages, SHA256
`f7a0010d91ac5a95cb7fc1df69109912296fb552f9bbcf6985cea91059d3e814`.

Every page below was individually opened with `view_image`, using its own
1391 by 1800 pixel PNG rendered by `pdftoppm -scale-to 1800 -png`. Images were
temporary inspection files in `/tmp/integral-full-page-qa/`, not published
deliverables. This records actual visual inspection, rather than inferring it
from text extraction or page-bound checks.

| Physical PDF page | Content inspected | Disposition |
|---|---|---|
| 1 | Title, date, full contents list, section numbers/page targets, introductory paragraph | Pass: legible and within margins; no collisions or missing entries observed. |
| 2 | Navigation list, search command examples/options, search-scope explanation, study guidance and reproduction commands | Pass: readable code and prose; the last paragraph continues normally onto page 3. |
| 3 | Review-scope continuation, branch/base identification, problem-index header and E01–E12 table rows | Pass: all four columns remain distinct; inline expressions and row wraps are legible. |
| 4 | Continued problem table E13–E16, suggested routes, functions versus values, measure conventions, signed-integrability formula | Pass: repeated header and continued rows are intact; mathematical superscripts, arrows, and integrals are readable. |
| 5 | Extended signed integral, Hausdorff normalization, Tonelli/Fubini/completion, area Jacobian and weighted fiber sum | Pass: covering sum/union, diameter factor, dimensions, matrix transpose, preimage condition, and integral measures are intact. |
| 6 | Area continuation, graph factor, coarea Jacobian and formula, orientation, convergence conditions, atlas introduction | Pass: square roots, transposes, fiber dimensions and nested integrals are readable; no clipping or overlap. |
| 7 | Atlas table: section measurability, signed exchanges, concentration, escape, parameter derivatives, derivative limits, multiplicity | Pass: columns and complete row text are distinct; expressions and sufficient conditions remain legible. |
| 8 | Atlas continuation for critical Jacobians and singular maps, concentration note, source-audit introduction and Hunter references | Pass: table continuation and reference bullets are intact. The E12 label was additionally inspected in a 200-dpi detail render and is complete. |
| 9 | Axler, Simon, and Hajłasz geometry references, page locators, normalization and dimensional-caveat text | Pass: links, names/diacritics, reference numbers and literal notation are readable, without overlap. |
| 10 | Hajłasz analysis and Conrad references, source-version caveats, scalar/orientation distinction and final verification-scope paragraph | Pass: all paragraphs and source-code notation are intact; final lines and page number are within margins. |

No clipping, illegible formula, missing glyph, or overlapping content was found
on any of the 10 pages. Natural paragraph and table continuations across pages
were checked as continuations, rather than mistaken for truncation. No PDF,
LaTeX, Markdown example, or mathematical review hash was changed by this QA.

This inspection covers these exact bytes using the stated renderer. It does
not certify accessibility tagging, screen-reader order, every PDF viewer, or
the absence of mathematical errors. The earlier independent mathematical
reviews and the earlier text/navigation checks retain their separate scopes.
