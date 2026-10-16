# Zhang holomorphic Anosov paper: expanded correctness review

Review date: 16 October 2026. Exact manuscript: **arXiv:2609.37695v3, 13 October 2026**, 19 pages, 371,989 bytes. SHA-256: `3c8287bf41d153c7f0d0950b8a4b477546229333ee66ba7e9ae60e6a387920c6`.

**No counterexample to the main theorem or demonstrated fatal defect in the new arguments was found.** The review identifies a false auxiliary assertion in Ghys (with a repair of the needed consequence), an explicit unproved classical topological premise in three Lean targets, and two residual source-proof audit limits. The pinned Lean solution now builds and passes the full-type, definition and axiom checks; the official comparator is blocked before comparison by user-namespace restrictions. This does not establish an unconditional formal proof of the manuscript.

- [Expanded report](updated-review.md) · [PDF](updated-review.pdf)
- [Manuscript-to-Lean correspondence](manuscript-to-lean-correspondence.md) · [theorem CSV](manuscript-to-lean-correspondence.csv) · [definition CSV](lean-definition-correspondence.csv)
- [Citation and dependency coverage ledger](citation-dependency-ledger.md) · [CSV](citation-dependency-ledger.csv)
- [Independent detailed notes](notes/)
- [Verification methods, results and limits](evidence/README.md)
- [Initial limited review, superseded](initial-limited-review.md) · [PDF](initial-limited-review.pdf) · [initial notes](initial-limited-notes.md)
- [SHA-256 file manifest](SHA256SUMS)

The formal source is pinned to [HolomorphicAnosov commit 65f2b33](https://github.com/frenzymath/HolomorphicAnosov/tree/65f2b33a7309de661a8500e4642e5609a537a8ff), requiring Lean 4.35.0-rc1 and Mathlib c32e1ec. The official compiler and all nine locked dependencies were installed in an isolated checkout. The 4,230-module solution closure built, the complete type and selected definition checks passed, and all eight target/wrapper axiom lists contain only the standard three. A separate finalized-export replay of all four target proofs also passed with the same official Lean kernel in a fresh environment. A, 1.1 and 1.3 retain the explicit homotopy-torus rigidity premise. See the [compiled verification record](evidence/compiled-verification/deliverables/verification-method.md), logs and hashes for the separate proof-replay result and the comparator startup blocker. The source-level correspondence and lexical checks retain the limitations stated in the report.

The supplied manuscript and copyrighted source PDFs/scans/OCR are excluded. The original private initial review and supplied PDF were preserved unchanged. This publication contains the reviewers' analysis, original illustration, audit scripts, hashes, dependency pins and metadata. Generic `working-reference/` names in archived notes refer to excluded reference copies, not downloadable repository files.
