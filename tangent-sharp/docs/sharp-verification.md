# Sharp tangent series verification

The full sharp absolute-summability theorem and the separate unconditional
divergence theorem compiled successfully during this run on 2026-10-11 UTC.
The full project build passed, the complete type and axiom inventories passed,
and an independent fresh source check and consumer audit passed.

## Execution and pins

The supplied extension was developed from exact base commit
`d00a89dd9ce6c8ef782234d28c93e69cb712c947`. Its build, audit and baseline
receipts below describe the supplied run; publication-session checks are separate.

| Component | Verified value |
| --- | --- |
| Lean | 4.24.0 |
| Lean compiler commit | `797c613eb9b6d4ec95db23e3e00af9ac6657f24b` |
| mathlib commit | `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` |
| `lean-toolchain` SHA-256 | `42779d67b81608af8a12aa4328d2ab47ca201925b3b2bd68369587b5340bb434` |
| `lakefile.toml` SHA-256 | `dbb3f4f563156a8062f93ceb0aa660a12b60650d2f47fb0de4f32308fb25e451` |
| `lake-manifest.json` SHA-256 | `8f871ddcf1917c176ac801f24bc66c975e4562d4d7aab8193c45ef7f31d5ad03` |
| Hypothesis source SHA-256 | `6f9fb3e7a25e2ba27fba29faf93e88add77a8c0aa3a8de59be72ae7b9ea2562a` |

The toolchain file, lakefile, dependency manifest, and hypothesis source were
also compared byte for byte with the pinned original commit and are unchanged.

## Fresh baseline

Before extending the proof, the task ran its own verification of the original
project, rather than relying on the environment repair report or historical
publication logs. The baseline build completed successfully with 2547 jobs.
Its compiler inventory checked all 37 original declarations and printed their
axiom dependencies; only the standard foundational axioms occurred.

Each of the eight original source modules was then independently elaborated
from source using the pinned compiler, with separate output objects and
diagnostic logs under the scoped baseline directory. All eight succeeded
without diagnostics. This is a fresh project-source check against the pinned,
already provisioned mathlib dependencies; it is not a clean rebuild of all
mathlib sources.

The commands were run from the `tangent-limit` directory:

```bash
TANGENT_VERIFY_LOG_DIR=<historical-workspace>/scratch/tangent-baseline \
  bash <historical-workspace>/tangent-limit-environment/verify.sh
source scripts/environment.sh
for f in Hypothesis Trigonometry NearestPole Diophantine \
         LimitComparison Limit NonPole Summability; do
  lake env lean "TangentLimit/$f.lean" \
    -o "<historical-workspace>/scratch/tangent-baseline/$f.olean" \
    > "<historical-workspace>/scratch/tangent-baseline/fresh-$f.log" 2>&1
done
```

The environment verification helper is external to the distributable project.
For reproduction, the original `scripts/verify.sh` covers the original audit;
the self-contained extension verifier described below covers the completed
development without requiring that environment helper.

Saved baseline evidence is in `logs/sharp-20261011/baseline`. Empty fresh-module
logs mean successful Lean elaboration with no diagnostics, not omitted runs.

## Completed theorem and declaration audit

The final compiler-generated types include:

```lean
TangentLimit.summable_abs_tan_div_rpow_positive_iff
    (h : TangentLimit.PiDiophantine) (s : ℝ) :
  (Summable fun n => |Real.tan ↑(n + 1)| / ↑(n + 1) ^ s) ↔ 1 < s

TangentLimit.not_summable_abs_tan_div_rpow_positive
    (s : ℝ) (hs : s ≤ 1) :
  ¬ Summable (fun n => |Real.tan ↑(n + 1)| / ↑(n + 1) ^ s)
```

The complete exported type inventory is `logs/sharp-20261011/public-inventory.log`.
It contains all 76 exported declarations: 37 originals and 39 additions.
`scripts/PrivateInventory.lean` separately checks and prints the dependencies
of the two private spacing lemmas. Together the inventories cover all 78
source declarations, with no duplicate or missing source names.

Every dependency list is a subset of
`[propext, Classical.choice, Quot.sound]`. There is no `sorryAx`. A source scan
found no `sorry`, `admit`, or added axiom declaration. The final equivalence
retains the original hypothesis as an explicit argument; the unconditional
divergence statement has no such argument and its project imports use only
`NonPole`, whose π irrationality theorem is proved in mathlib.

The extension verification command started at **03:12:00 UTC** and completed
successfully:

```bash
bash scripts/verify-sharp.sh <historical-workspace>/scratch/tangent-release
```

Its saved full-library build completed successfully with 3138 jobs. The script
prints all types and axioms, verifies exact compiler and mathlib pins, guards
the dependency manifest against changes, and checks source/inventory name
coverage. Fresh logs are copied to `logs/sharp-20261011`. The declaration-name
completeness check added after that run was executed against the same completed
inventories and passed; no theorem source changed.

To reproduce the final evidence with the packaged project:

```bash
bash scripts/setup.sh
bash scripts/verify-sharp.sh
```

This writes logs under `.cache/research/verify-sharp`. An optional first argument
selects another untracked directory. The verifier refuses to overwrite tracked
logs and does not alter the supplied pins or hypothesis.

## Independent review

Independent component implementations and reviews checked the uniform approximation,
spacing, packing, dyadic infrastructure, and divergence components. Separate
review checked the ordinary argument, all seven new source modules, and the
integration's actual assumption boundaries and dyadic summability connection.

The final reviewer freshly elaborated `SharpSummability.lean` at
**03:10:38–03:10:50 UTC**, exiting 0 with no diagnostics. An independently
written consumer audit imported `TangentLimit`, checked the sufficient and
equivalence theorems and unconditional divergence, printed the hypothesis and
their axiom dependencies, and elaborated explicit consumer examples. It ran
at **03:10:38–03:10:48 UTC**, exiting 0.

The full review is `docs/sharp-independent-review.md`; its successful commands,
metadata, and audit source/log are in `logs/sharp-20261011/independent`.
Selected successful component evidence is in `logs/sharp-20261011/components`.
Earlier component hashes in their historical notes describe that component
stage; the top-level final manifest identifies the delivered source bytes.

## Delivery and limitations

The source-and-evidence archive includes the pinned project sources, all seven
new modules, readable proof notes, exact inventories, current build logs,
independent review, and SHA-256 manifests. Dependency caches, compiler binaries,
Git metadata, and credentials are excluded. This publication contains a separate full `tangent-sharp/` project copy; the
redundant archive patch is omitted.

The requested conditional sharp theorem is complete. `PiDiophantine` remains an
assumption; this work does not establish it from ordinary π irrationality.
There is no claim about conditional convergence of the signed tangent series.
