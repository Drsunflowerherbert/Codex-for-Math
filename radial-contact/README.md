# RadialContact

Reproducibility edition **v2**. The Lean theorem files, toolchain, Lake
configuration, and dependency manifest are unchanged from the delivered original.
The original archive fingerprint is retained; this edition adds evidence
integrity checks and regression tests. Private Library identifiers are omitted.

## Reproduce or inspect

Use Python 3.11 or later and the pinned Lean 4.24.0 toolchain. With `lake` on
`PATH`, run this one command from the project root:

```sh
python3 scripts/verify.py
```

It runs the failure-oriented regression suite, verifies the compiler and clean
dependency checkouts against the pinned manifest, builds the library, and audits
every public declaration's complete type and transitive axioms. A successful
result has exit code zero and `status: passed` in `evidence/validation.json`.
Each execution records its actual command, exit code, timestamps, and full log.
Every new attempt writes a failure marker first, so an interrupted or failed run
cannot leave an older success marker standing.

To inspect saved evidence without Lean, network access, or file changes:

```sh
python3 scripts/check_evidence.py
```

This requires complete statement/axiom coverage and matching hashes for the
current Lean files, verifier, tests, documentation, pinned configuration, and
required evidence files. Changed inputs produce `source_drift`; missing files,
altered logs, omitted audit records, and stale assumptions have explicit failure
codes. Staleness means a content mismatch or incomplete evidence, not elapsed
time. Hashes establish consistency, not an independent rerun of Lean; use the
first command for fresh kernel verification.

`ASSUMPTIONS.md` inventories the parameter requirements and geometric scope;
`evidence/assumptions.json` records the exact compiled types and axioms for all
declarations. The source scanner intentionally supports this library's public
theorem/def/abbrev syntax and rejects unsupported declaration forms rather than
silently skipping them. Extending its syntax requires review and new tests.

A standalone Lean 4 library for radial contact with the unit sphere in arbitrary
real normed spaces. The only ambient assumptions are `NormedAddCommGroup E` and
`NormedSpace ℝ E`. Completeness, finite dimension, smoothness, strict convexity,
and an inhabited unit sphere are not assumed.

## Version pin

- Lean: `leanprover/lean4:v4.24.0`, release compiler commit
  `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`.
- mathlib: official `v4.24.0`, pinned by full commit
  `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.
- Transitive dependencies: pinned in `lake-manifest.json`.

With that Lean toolchain available, run `lake update`, then `lake build`.
The upstream cache hook is optional: if its host is inaccessible, use
`MATHLIB_NO_CACHE_ON_UPDATE=1 lake update` and build the required imports from
source. This project's full local commands and outcomes are in `evidence/`.

## API

Import `RadialContact`. Within namespace `RadialContact`:

- `UnitSphere E` is `{v : E // ‖v‖ = 1}`.
- `InteriorCenter E` is `{c : E // ‖c‖ < 1}`.
- `existsUnique_positive_contact` establishes exactly one positive real radius
  with `‖c + r • v‖ = 1` for each unit vector.
- `positive_contact_bounds` and `radius_bounds` establish
  `1 - ‖c‖ ≤ r ≤ 1 + ‖c‖`.
- `radius c v` is the unique positive radius; `contact c v` is the resulting
  sphere point.
- `radius_dist_le` / `radius_lipschitz` give the constant
  `(1 + ‖c‖)^2 / (1 - ‖c‖)`.
- `contact_dist_le` / `contact_lipschitz` give the constant
  `2 * (1 + ‖c‖) / (1 - ‖c‖)`.
- `direction c x` is `‖x - c‖⁻¹ • (x - c)` on the sphere.
- `contact_direction` and `direction_contact` prove both inverse identities;
  `sphereHomeomorph c` packages the continuous maps as a homeomorphism.
- `unitSphere_isEmpty_of_subsingleton` covers the zero space. All constructions
  accept an empty domain without manufacturing an arbitrary sphere point.
- `radius_zero`, `contact_zero`, and `direction_zero` give the exact behavior at
  `zeroCenter`: radius one and both maps the identity.

## Required results versus derived refinements

`Basic.lean`, `Lipschitz.lean`, and `Inverse.lean` implement the mathematical
specification. The key reusable triangle inequality is `parameter_comparison`,
valid for nonnegative parameters and arbitrary directions. Its absolute form
implies uniqueness without any strict-convexity assumption.

`Derived.lean` separately contains reciprocal-radius control, an inverse
Lipschitz bound `2 / (1 - ‖c‖)`, the exact zero radius Lipschitz constant zero,
and zero-center isometries. Sharpness examples are ordinary mathematical review
evidence only; they are not claimed as Lean theorems.

## Provenance and validation

At formalization time, the specified starter archive was unavailable after two
supported transfer attempts. The formalizers therefore did not inspect its study
records or verify its hash. They independently implemented the supplied mathematical
specification. This publication session subsequently retrieved the starter archive
and verified its supplied SHA256; that does not retroactively establish original
source access or equivalence of the specifications. The sanitized historical record
is in `evidence/source-provenance.json`.

This implementation therefore follows the user-authorized mathematical
specification and an independent ordinary proof review. Validation status,
complete build logs, axiom dependencies, and independent source review are
recorded in `evidence/`. The complete library build passed without warnings, and
the completed audit checked all 47 public declarations. Its only dependencies
are Lean's standard logical axioms `propext`, `Classical.choice`, and `Quot.sound`;
there is no `sorryAx` or newly declared axiom. Both final verification commands
returned exit code zero on 2026-10-11, with the audit completed at 02:35:37 UTC.

The original build and audit are preserved under `evidence/original/`. The v2
runner records fresh evidence in `evidence/validation.json`; current proof
files can be compared with the original source hashes there or in the original
Library ZIP. `evidence/original-deliverable.json` preserves the earlier archive fingerprint.

Historical failed elaboration logs are retained separately. Their automatically
generated placeholder warnings are compiler diagnostics from failed attempts,
not admitted proofs in the accepted library. `evidence/validation.json` and
`evidence/theorems-and-axioms.log` describe the final accepted declarations.

The `evidence/original/` and `evidence/supplied-v2/` receipts are historical.
The current `evidence/validation.json` records the publication build. Historical
manifests retain their supplied hashes and may reference sanitized or omitted files;
use the repository publication manifest for the current tree.
