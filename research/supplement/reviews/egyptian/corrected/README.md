# Corrected Egyptian fraction review supplement

The six original theorem statements are unchanged. This supplement applies the scope, runtime, evidence and denominator-size wording corrections identified by the independent review, and adds a separately proved optional corollary about coarse denominator size.

- study.md is the corrected replacement prose
- theorem-records.json preserves the original six IDs, hypotheses, conclusions and dependencies, adds linked independent review statuses, and retains the original author status as provenance
- coarse-padding-bounds.md proves the optional one-step and iterated bounds
- coarse-padding-bound-records.json records those two corollaries separately from the six original statements
- validation-results.json records the completed file, link, preservation and finite one-step-bound checks
- validate_supplement.py reproduces those checks using only the Python standard library
- supplement-manifest.json records exact SHA-256 hashes for these files, their linked review evidence and the preserved originals

The corrected theorem records distinguish ordinary_proof_status, now author_checked, from ordinary_proof_review_status, independently_reviewed_pass. Their original_record_provenance retains the exact original author_checked_pending_independent_review value and the original file hash. Review evidence remains a separate artifact rather than replacing the original author record. These JSON files are portable supplement records, not validated native MRS imports.

The optional corollaries are proved in this supplement. They have not received an additional separate independent review. No Lean verification, software installation, remote publication or source-file modification is part of this supplement.

Relative links assume this corrected directory remains at reviews/egyptian/corrected within the research tree. Keep the adjacent review evidence and original egyptian-fractions directory when copying the supplement, or adjust links explicitly. The original arithmetic script and its 5.3 MB certificate are referenced in place rather than duplicated again here.
