# Observed verification evidence

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](../PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

The final fresh attempt is
[`run-20261013T015800Z/receipt.json`](run-20261013T015800Z/receipt.json).
Its actual start was `2026-10-13T01:57:16.146283+00:00`; the directory name is
an attempt label, not a timestamp authority. The receipt gives exact argv, cwd,
start/end times, exit codes, separate stdout/stderr byte counts and SHA-256,
the actual compiler, package identities, source hashes, and trust limits.

Executed from `${PROJECT_REPOSITORY}/lp-certificates`:

```sh
python3 scripts/verify.py --output evidence/run-20261013T015800Z \
  --lean-bin ${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin \
  --cached-repository ${PINNED_REPOSITORY}
```

Exit `0`, result `passed`. All nine recorded subprocesses exited `0`:

1. Actual Lean version: `4.24.0`, official release compiler commit
   `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`.
2. Published evidence toolkit source pins: passed.
3. Published compiler byte audit: selected five compiler/runtime members match
   the independently pinned official archive bytes.
4. Compiler location: Lake selected the exact installation audited in step 3.
5. Python tests: 53 passed; the independent bounded raw-row oracle agrees on
   72,900 documents, with 2,072 accepted by both calculations.
6. Fresh project Lean build: successful, no diagnostics. Only the project's
   build cache was cleared; imported dependency caches remained trusted.
7. Declaration audit: all 64 named source definitions/lemmas/theorems covered;
   only `propext`, `Classical.choice`, and `Quot.sound` appear in axiom closures.
8. The published `EvidenceHarness.lean` was freshly compiled unchanged.
9. Independently authored `Expected.lean`: five arithmetic/cast definition-body
   gates, three full expected real statement gates, and replay of 111 local
   declarations against `[Mathlib, EvidenceHarness]`, all successful.

The nine clean package checkouts match the committed lockfile. The original
and final active input hashes are equal. A post-run integrity check reproduced
all 29 input hashes and the byte counts/hashes of all 18 command-output files.
This check validates stored consistency; it is not a new Lean execution.

The independent reports disclose their roles and methods:

- `math-review.md`: ordinary mathematical review and eight hand calculations.
- `computational-review.md`: separately authored raw-row arithmetic oracle,
  exhaustive bounded experiment, parser/CLI failures, and the corrected deeply
  nested JSON error-handling finding.
- `formal-review.md`: independently authored full expected types/body gates,
  proof/model assessment, transcription review, and an isolated fresh rerun.

Early development encountered Lean's removed `LinearOrderedField` instance
interface, an ambiguous rational-to-real cast annotation, and `decide` reduction
transparency on finite rational examples. These were corrected to modern ordered
field classes, explicit rational inner types, and `decide +kernel`. The final
proofs are checked; no failed development command is counted as acceptance.

The helper's fixed tangent protocol is not relabeled as LP acceptance. This
task directly reuses its suitable audited commands with a new scoped expected
harness. The generic core is universe-polymorphic; the three rational-to-real
targets are closed monomorphic types quantified over arbitrary natural
dimensions, supported by that helper. Replay uses the same Lean kernel.
An independent kernel implementation, a full dependency-source rebuild,
formal Python/JSON refinement, and native Mac/installed MRS integration were
not performed. Cached dependency oleans, the inspected helper, and the host
runtime are trusted. Reading a stored receipt does not grant a fresh pass.
