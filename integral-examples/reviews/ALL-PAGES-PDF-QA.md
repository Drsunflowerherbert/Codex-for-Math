# Final visual QA of all 62 PDF pages

Date: 2026-10-15. Disposition: **pass for both exact published PDFs**.

Every physical page of the 52-page worked collection and the 10-page guide was
individually rendered and opened with `view_image` at 1391 by 1800 pixels.
Reviewers examined text, equations, tables, page transitions, margins, and
glyphs. They used higher-resolution detail rendering or the retained source
when a detail needed clarification. Text extraction and bounds checks were
supporting evidence; they were not substituted for actual visual inspection.

| PDF | Pages individually inspected | SHA256 |
|---|---:|---|
| `pdf/integral-examples.pdf` | All 52, pages 1–52 | `9d03d22882d87c4be3b40b2e7b21972bc159c5f15f3ed4522e4a0547a256f068` |
| `pdf/guide.pdf` | All 10, pages 1–10 | `f7a0010d91ac5a95cb7fc1df69109912296fb552f9bbcf6985cea91059d3e814` |

Detailed records assign each page exactly once in this final coverage pass:

- [Worked collection pages 1–13](pdf-full-pages-01-13.md): geometry author.
- [Worked collection pages 14–26](pdf-full-pages-14-26.md): source auditor.
- [Worked collection pages 27–39](pdf-full-pages-27-39.md): Lebesgue author.
- [Worked collection pages 40–52](pdf-full-pages-40-52.md): parameters author.
- [Guide pages 1–10](pdf-full-guide-01-10.md): primary collection agent.

No clipping, illegible formulas, missing glyphs, overlapping content, or broken
equation layout was observed on any page. The recorded single underfull
paragraph warning remains a spacing-only observation; its rendered text is
legible. Natural page continuations were checked, including repeated table
headers and multi-page solutions. No repair or rebuild was needed: both PDFs
remain byte-identical to the edition at commit
`f64a1b0133ee8fdf3843469e703f09b9cae494c4`.

The earlier [PDF review](pdf-review.md) accurately records its original sampled
visual scope. This later pass closes that coverage gap; it does not rewrite the
historical review or claim that the earlier sample was exhaustive. The new
machine-readable [coverage record](../checks/pdf-all-pages-qa.json) lists every
inspected page and review file. Run
`python3 integral-examples/checks/check_all_pages_qa.py` from the repository root
to check its coverage, report presence, and exact PDF identities. That script
checks the recorded evidence; it cannot itself perform visual review.

These are model production reviews. They do not claim human inspection,
accessibility certification, behavior in every PDF viewer, or additional
mathematical/formal verification. No mathematical source, solution, theorem
hypothesis, computation result, or locked mathematical review hash was changed.
