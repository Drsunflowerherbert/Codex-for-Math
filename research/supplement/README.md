# Reviewed mathematics research-data supplement

Prepared 11 October 2026. This is the public edition of a separate supplement to the earlier starter bundle. It contains seven completed supporting-lemma studies, portable theorem data, mathematical reviews, provenance, and reproducible finite checks. It does not replace or modify the earlier bundle.

## Start here

Use the following final notes and evidence. `STUDY-INDEX.json` provides the same map in portable form.

1. **Affine avoidance:** `reviews/affine/research-notes.reviewed.txt` and `mrs-provisional-records.reviewed.json`; read `independent-review.txt` for the review. This is a conditional periodic-to-global reduction, assuming normalized hitting sets. The corrected limitation forces infinitely many distinct values, not pairwise distinct sequence terms. Five reviewed records.
2. **Egyptian fractions:** `reviews/egyptian/corrected/study.md` and `theorem-records.json`; the adjacent `../review.md` and `../review-records.json` review the six original statements. Fixed-length duplicate removal and marker-preserving padding remain ordinary mathematical results. The separate `coarse-padding-bounds.md` and `coarse-padding-bound-records.json` contain two optional, proved corollaries that have **not received an additional independent review**. Their finite one-step checks do not verify arbitrary iteration.
3. **Transport stability:** `transport-stability/proof.md` and `theorems.json`; `reviews/transport/audit-report.md` independently reviews the ten records. `optional-refinements.md` separately states two deductions checked during that review: fixed-priority induced-plan uniqueness and the fixed-mass one-half exponent obstruction. These do not prove a global upper stability theorem.
4. **Positive blocks:** `positive-blocks/study.md`, `theorem-records.json`, and `verification-status.json`; the directory's independent review and `reviews/positive-blocks/` record two ordinary proof audits. Ten theorem/identity records plus five background nodes, exact gaps, complete equality cases, and 16 named plus 180 seeded Gram fixtures.
5. **Mixed moments:** `mixed-moments/study.md`, `theorems.json`, `audit.md`, and `verification.json`. Twenty-one records cover mixed-moment identities and Taylor-contact cancellation, with 17,805 exact arithmetic checks. Catalan's constant remains symbolic; no irrationality or independence claim is proved here.
6. **Convex approximation:** `convex-approximation/study.md`, `theorem-records.json`, `audit.md`, and `verification.json`. Nineteen records cover finite-dimensional analytic convex outer approximation, quantitative bounds, and nesting. Exact rational checks and numerical illustrations are separately identified.
7. **Finite-field mixing:** `finite-field-mixing/study.md` and `theorems.json`; the final independent review is in `reviews/finite-field-mixing/`. Ten records cover Fourier mixing, four-product sufficient coverage, and positive-divisor lifting. The independent integer-polynomial check covers 141,477 nonempty sets, 17,148 ordered set pairs, and further heterogeneous cases. This is not a global Egyptian-fraction bound or an optimality claim.

There are 81 core theorem/identity records across these studies, plus separately labeled optional results and background/dependency nodes. Counts refer to portable research records, not accepted native database objects.

## What “reviewed” and “checked” mean

- **Ordinary mathematical review:** a separate mathematical reading of a stated proof and its hypotheses. It is not external peer-review certification or proof-assistant verification.
- **Exact finite checks:** integer or rational computations of stated examples and finite ranges. These support consistency and catch errors; they do not prove universally quantified or infinite analytic statements.
- **Numerical illustration:** floating-point sampling appears in the convex-approximation examples. It has a weaker evidential role than exact arithmetic and does not prove the analytic theorem.
- **Lean verification:** **none of these seven studies has been compiled or kernel-checked in Lean.** Formalization roadmaps are plans only. A saved source scope document and upstream formalization references do not verify these studies.
- **Portable JSON:** no native MRS schema validation or database import is claimed. Some preserved author records still contain historical pending-review fields; the separate hash-bound completed reviews and corrected copies give the current ordinary-review status.

All findings are scoped supporting results. No whole-manuscript validation, headline open-problem solution, or novelty claim is implied. Assumptions and limitations remain part of every result.

## Provenance and historical inputs

The recorded source revision is `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` of OpenAI/math. Revision-pinned URLs and SHA-256 values identify the supplied source bytes. Packaging did not freshly authenticate the remote commit. Seven small source/scope snapshots needed for provenance or the checks are included in `catalog/sources/`; the broad raw-source collection is omitted.

`affine-avoidance/` and `egyptian-fractions/` preserve original review inputs, including pre-correction prose, so the correction and audit programs can be reproduced. They are historical inputs, not the preferred final notes. Follow the corrected entry points above. The single Egyptian exact-example certificate is retained once; its duplicate rerun is recreated temporarily by the reproduction runner. The small transport rerun is retained because its review manifest explicitly fingerprints it. Initial review snapshots and redundant reruns are omitted.

The frozen finite-field review manifest SHA-256 is:

`ba21816100a93941c55a525939e73c8db24ddf0faf22e8bf9f9a2eb019239b72`

`PACKAGE-PROVENANCE.json` and `PACKAGING-VALIDATION.json` retain supplied historical packaging receipts. Public metadata and documentation were sanitized; the file-level original/public mapping is in `../../publication/SOURCE-MAP.json`. Proof statements and source snapshots are preserved. Use the portable runner below for the current public edition.

## Verify integrity and reproduce computations

Python 3.10 or newer, standard library only. No package installation or network access is required.

From the extracted supplement root:

    python3 verify_package.py
    python3 reproduce_checks.py --output /path/outside/supplement/reproduction-results.json

The default reproduction runs all seven study checkers, the affine/Egyptian review checks, and the independent positive-block checker. For finite-field mixing it uses the author's reduced `--quick` enumeration; the already saved certificates and independent review document the full completed ranges.

For both full finite-field enumerations as well:

    python3 reproduce_checks.py --full --output /path/outside/supplement/full-reproduction-results.json

The full option may take several minutes. The runner first verifies the package, creates an isolated temporary copy, runs only the included original standard-library study/checking programs, and deletes that temporary tree when finished. It does not edit the delivered files. The finite-field checker now uses a project-relative base path. In the temporary copy only, the runner rebases Egyptian preservation-list paths and hashes for privacy-normalized documentation after public integrity verification; it also recreates omitted duplicate rerun inputs. No mathematical algorithm or assertion is changed. A regenerated result may contain a new runtime, Python version, path, or temporary script hash; those differences do not change the saved review evidence.

`verify_package.py` routes to the public snapshot checker in `../../publication/verify.py`. It checks current file hashes/sizes, missing or extra files, JSON syntax, formal-source preservation, pins and explicit study status. Historical archive and nested review manifests describe the supplied original snapshots; they may fingerprint sanitized files. `MANIFEST-SHA256.supplied.json` retains the original root manifest. The current publication manifest excludes itself to avoid self-reference. Integrity checks establish byte consistency, not mathematical truth.
