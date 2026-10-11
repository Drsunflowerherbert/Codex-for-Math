# Mathematical exchange schema v1

This is a companion-owned exchange schema. It is not a native MRS schema.
The executable validator in core.cjs is normative. Strict JSON parsing must occur
before validation; plain JSON.parse alone loses duplicate-key information.

Every object below has exactly the listed fields. Unknown, missing and mistyped
fields fail. Arrays preserve identifiers and order. No imported field can supply
an executable command.

## Catalog

    {
      "schema": "math-exchange/v1",
      "project": {
        "repository": "https://host/owner/repository",
        "revision": "<full lowercase 40-character Git revision>",
        "branch": "<conservative branch label>",
        "lean_toolchain": "leanprover/lean4:v<major>.<minor>.<patch>",
        "mathlib_revision": "<full lowercase 40-character Git revision>"
      },
      "files": [{"path": "relative/file", "sha256": "<64 lowercase hex>", "role": "source"}],
      "records": [<record>]
    }

A branch is a label, never the revision authority. Generic validation does not
contact the repository to attest a revision. Tangent acceptance uses separate
fixed hashes and metadata derived from the exact published revision.

File roles: source, toolchain, lockfile, review, experiment, legacy_log,
statement_inventory. Exactly one toolchain and one Lake lockfile are required.
Their hash-checked contents must agree with project pins. The mathlib lock entry
must be a Git package at the official leanprover-community/mathlib4 HTTPS origin.

## Record

Required fields:

- id: an ASCII identifier, retaining original case, up to 128 characters.
- kind: definition, theorem or assumption.
- name: an ASCII Lean declaration name, possibly qualified.
- statement: text, source_path, source_excerpt, sha256.
- assumptions: distinct existing record IDs of kind assumption.
- dependencies: distinct existing record IDs.
- sources: nonempty list of objects with url, revision, locator.
- review: status and evidence.
- experiments: list of objects with claim, scope, evidence.
- lean: status, evidence, reason.

For each statement, text equals source_excerpt; sha256 hashes its exact UTF-8 bytes.
source_path must name a manifest file with role source. The excerpt must occur
exactly once in that hash-checked file and begin with def, theorem or lemma and the
short declaration name. The heuristic is deliberately not semantic Lean parsing.

Each source has an HTTPS URL without credentials, query or fragment, an exact
Git revision and a nonempty locator. This release does not define DOI, arXiv or
non-Git revision schemes; preserve those in original files until a reviewed
schema extension exists.

Declared graph references must resolve and the graph must be acyclic. A direct
dependency on an assumption must also be explicit in a theorem's assumptions.
The validator does not prove complete transitive assumptions or infer how a proof
discharges a premise. Empty assumptions mean none declared, not unconditionally true.

Review status:
- not_reviewed: evidence must be empty.
- review_reported: one or more role=review evidence paths are required.

Experiments report a claim, an explicit scope string and one or more role=experiment
evidence paths. The validator checks attached bytes, not execution or finite-domain
completeness. It reports experimentScopeValidation=not_established.

Lean status:
- not_run: evidence must be empty; reason remains required.
- historical_report: nonempty role=legacy_log evidence and reason are required.

passed, checked, complete, kernel_verified and all other Lean statuses fail.
There is no live receipt or positive pass status in v1.

## Portable paths and limits

Paths use ASCII letters, numbers, underscore, hyphen, dot and slash. Absolute
paths, backslashes, dot/dot-dot/empty segments, trailing dots, Windows device
names, case-fold collisions and file/directory prefix conflicts fail.

Limits: 2,048 records, 1,000 files, 16 MiB combined file bytes, 2 MiB individual
metadata strings, JSON depth 64. The strict parser additionally bounds input
and array lengths. CLI JSON input is at most 32 MiB.

Local readers reject source symlinks and require realpath containment, regular
files and size limits. The reader assumes a trusted workspace without concurrent
hostile filesystem mutation; it is not an OS sandbox.

## Byte bundle

    {
      "schema": "math-bundle/v1",
      "catalog": <catalog>,
      "files": [{"path": "relative/file", "sha256": "<64 lowercase hex>", "hex": "<exact lowercase byte hex>"}]
    }

Bundle files must match the catalog file set and hashes exactly. Extra, missing,
duplicate or changed files fail. Validation returns an in-memory byte map, not an
automatic filesystem extraction. Generic hashes are integrity commitments, not
signatures, authenticated authorship, trusted timestamps or kernel receipts.

## Machine-readable verification boundaries

Every successful summary includes:

    leanCompilation: not_performed
    leanTypeMatching: not_performed
    leanAxiomAudit: not_performed
    independentKernelReplay: not_performed
    assumptionCompleteness: not_established
    dependencyCompleteness: not_established
    experimentScopeValidation: not_established
    sourceRevisionAttestation: not_performed
    counts.leanPasses: 0

The tangent-specific acceptance adds exact published byte/declaration pins and
historical log-name coverage. It still reports leanPass=false and
liveAxiomInspection=not_performed.
