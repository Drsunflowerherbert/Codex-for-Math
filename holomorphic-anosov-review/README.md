# Zhang holomorphic Anosov paper: expanded correctness review

Review date: 16 October 2026. Exact manuscript: **arXiv:2609.37695v3, 13 October 2026**, 19 pages, 371,989 bytes. SHA-256: `3c8287bf41d153c7f0d0950b8a4b477546229333ee66ba7e9ae60e6a387920c6`.

**No counterexample to the main theorem or demonstrated fatal defect in the new arguments was found.** The review identifies a false auxiliary assertion in Ghys (with a repair of the needed consequence), an explicit unproved classical topological premise in three Lean targets, and two residual source-proof audit limits. It does not claim end-to-end mathematical or reproduced kernel verification.

- [Expanded report](updated-review.md) · [PDF](updated-review.pdf)
- [Manuscript-to-Lean correspondence](manuscript-to-lean-correspondence.md) · [theorem CSV](manuscript-to-lean-correspondence.csv) · [definition CSV](lean-definition-correspondence.csv)
- [Citation and dependency coverage ledger](citation-dependency-ledger.md) · [CSV](citation-dependency-ledger.csv)
- [Independent detailed notes](notes/)
- [Verification methods, results and limits](evidence/README.md)
- [Initial limited review, superseded](initial-limited-review.md) · [PDF](initial-limited-review.pdf) · [initial notes](initial-limited-notes.md)
- [SHA-256 file manifest](SHA256SUMS)

The formal source is pinned to [HolomorphicAnosov commit 65f2b33](https://github.com/frenzymath/HolomorphicAnosov/tree/65f2b33a7309de661a8500e4642e5609a537a8ff), requiring Lean 4.35.0-rc1 and Mathlib c32e1ec. No new compiler was installed and no Lean build, comparator run, or compiled axiom audit was reproduced. The source-level correspondence and lexical checks have the limitations stated in the report.

The supplied manuscript and copyrighted source PDFs/scans/OCR are excluded. The original private initial review and supplied PDF were preserved unchanged. This publication contains the reviewers' analysis, original illustration, audit scripts, hashes, dependency pins and metadata. Generic `working-reference/` names in archived notes refer to excluded reference copies, not downloadable repository files.
