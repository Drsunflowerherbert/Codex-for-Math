# Reproduction runbook

Read source before execution. Default suites use Node 24, Python 3.12 and a trusted
Linux filesystem; no npm or third-party Python dependency is required. Optional
`toolchain-audit.py` additionally requires `/usr/bin/zstd` and the exact existing
Lean release archive. Native Mac/MRS behavior is untested.

Run report-writing tests in a disposable copy. `package.py` includes all regular
files except its documented Python cache exclusions; `.gitignore` does not remove
raw test reports from an archive. Keep outputs outside a clean source package.

```sh
toolkit=/absolute/path/to/math-evidence
repository=/absolute/path/to/inspected/Codex-for-Math
runs=/absolute/existing/canonical/output-parent
cd "$toolkit"
node verify-public-sources.cjs
node run-tests.cjs
node cli.cjs validate samples/catalog.json samples/source-tree
node cli.cjs accept-tangent samples/tangent.bundle.json
node cli.cjs inventory samples/catalog.json samples/source-tree
node process-tests.cjs
node verification/adversarial-review/real-adversarial.cjs
node verification/adversarial-review/interruption.cjs
python3 verification/adversarial-review/archive-adversarial.py
python3 package-tests.py
```

Inherited 157 checks comprise 78 synthetic core, 60 acceptance, 11 mock CLI and
8 mock materializer checks. The 69 actual Node/filesystem cases and 29 synthetic
ZIP/filesystem cases are separate. Race tests use labeled syscall ordering hooks
with actual OS I/O. Temporary roots are selected through standard temp APIs.
Original archive tests are optional; `MATH_EVIDENCE_OPTIONAL_CORPORA=1` enables only
provided exact `corpora/original` fixtures and records the actual count.

## Live gate

Use the exact pinned original project, Lean 4.24.0 installation, nine clean pinned
package checkouts and their dependency caches. Existing installation locations
follow the original tangent environment layout. The runner performs no installer,
cache download or dependency update. Check project instructions before any work.
Each attempt requires a new output directory under an existing canonical parent.

```sh
node live.cjs run valid "$repository" "$runs/valid"
node live.cjs run general "$repository" "$runs/general"
node live.cjs run tangent "$repository" "$runs/tangent"
node live.cjs inspect-receipt "$runs/tangent"
```

The tangent plan checks 37 targets, four definition bodies and 59 local replay
entries. Inspection returns integrity-only and no Lean pass. The following fixed
negative fixtures should exit 2 in separate new directories: `sorry`,
`custom-axiom`, `wrong`, `wrong-compilation`, `specialized`, `skip-kernel`.
They test different gates; a compilation success alone cannot establish a pass.

```sh
node live-os-tests.cjs "$repository"
node verification/adversarial-review/live-adversarial.cjs "$repository"
```

The live adversarial suite copies selected project sources before intentional
mutation. `MATH_EVIDENCE_TEST_ROOT` may select an existing disposable parent; the
original project is never a mutation target. Preserve interrupted/failed attempt
receipts. SIGKILL cannot run a cleanup handler; the test harness handles its
observed child process group separately. Never replace missing evidence with an
older success.

## Deterministic source packaging and relocated consumer

Use a clean source directory with no imported `release-manifest.json` or raw
report outputs. This packer generates its own self-excluded release manifest.

```sh
python3 package.py pack "$toolkit" "$runs/public-a.zip"
python3 package.py pack "$toolkit" "$runs/public-b.zip"
cmp "$runs/public-a.zip" "$runs/public-b.zip"
python3 package.py inspect "$runs/public-a.zip" EXPECTED_SHA256
```

Verify the digest and inspect entries before extracting into a fresh directory.
Then use the inspected consumer script with the exact original project:

```sh
node consumer-smoke.cjs /absolute/extracted/math-evidence "$repository" "$runs/smoke"
```

The public smoke runs eight fixed commands: inherited tests, pinned bundle
acceptance, relocated source validation, two deterministic bundles, current
public-source hash verification, fresh valid live execution, and integrity-only
inspection of that fresh receipt. It executes no imported command or receipt
argv. Its current workflow differs from the historical archived smoke.
Expected tangent bundle SHA-256 is
`841e041ac0e31b9263b440a81cb5fd525c81ff001e61db7f05661fbde1cd1966`.

## Optional exact corpus fixtures

Original archives are not distributed here. If independently obtained, verify
names, sizes and hashes in `archive-intake.py`, inspect them and extract into new
destinations. An ordinary corpus remains ordinary throughout import.

```sh
python3 archive-intake.py supplement /absolute/original-supplement.zip "$runs/supplement"
node corpus.cjs import-supplement "$runs/supplement/openai-math-reviewed-supplement-2026-10-11" "$runs/collection.json"
node corpus-tests.cjs "$runs/supplement/openai-math-reviewed-supplement-2026-10-11"
```

The lossless importer can preserve legacy paths as reported text; it never follows
absolute evidence paths. Review contradictory native/index review statuses as
reported data. It does not translate them into a new verified status.
