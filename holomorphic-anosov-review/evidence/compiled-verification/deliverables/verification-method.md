# Compiled verification method

This document describes the pinned inputs, commands, and evidence boundaries of the compiled verification. Paths such as `scripts/…`, `logs/…`, and `provenance/…` are relative to the verification bundle root. The proper finalized-export selected-proof replay completed successfully, using the same official Lean kernel implementation in a fresh environment; the configured comparator remains blocked.

## Recorded status

| Check | Recorded outcome |
|---|---|
| Official Lean release download and digest | Completed; digest matched the release API metadata |
| Nine locked dependency checkouts | Completed; all revision checks matched and the root manifest stayed unchanged |
| Official Mathlib cache retrieval | Completed, exit 0; see `logs/mathlib-cache.json` and `.log` |
| Configured bundled comparator | Blocked before comparison: Bubblewrap could not establish its UID map; exit 1 |
| `Comparator.Solution` source compilation | Completed, exit 0; 4,230 local solution-closure module artifacts; Lake reported 13,157 successful jobs |
| Exact-type and selected-definition harnesses | Both corrected `-02` runs completed, exit 0 |
| Transitive axiom inventory | All 16 requested lists contained exactly `propext`, `Quot.sound`, and `Classical.choice`, after removing printed universe suffixes |
| Selected proof export | Completed, exit 0; 2,385,351,648-byte export with recorded SHA-256 |
| Fresh-environment raw kernel replay | Proper run `selected-targets-replay-02` passed, exit 0 in 722.322 seconds; the earlier premature run was stopped and discarded |

The comparator failure message is `bwrap: setting up uid map: Read-only file system`. It is an environment isolation failure, not a recorded comparison result or mathematical rejection. No comparator sandbox bypass was attempted. Separately authorized direct use of the bundled exporter/checker is a different workflow and must not be reported as comparator acceptance.

## Pinned inputs

- Project: `https://github.com/frenzymath/HolomorphicAnosov`, commit `65f2b33a7309de661a8500e4642e5609a537a8ff`.
- Lean: `4.35.0-rc1`, release commit `86c6347c75e39ec18c40e25ed2143b71a6e04a0a`.
- Linux x86-64 release archive: `lean-4.35.0-rc1-linux.tar.zst`, 594,218,389 bytes, SHA-256 `a299763401c3b9b8e19bcca26f8443b40ae24962c3c3ddee73b5c72194877f65`.
- Mathlib: `c32e1ec0d1eb5237ba344eee50162f45d5b0fc76`.
- Root `lake-manifest.json` SHA-256: `de4af5f055b3b05d3a4a43c624db2a70381c762e18542f4e66bc3c71a02ebb1c`.

The archive was checked against GitHub's official release-asset digest and extracted with Python's tar data filter. This verifies agreement with the retrieved official metadata; it is not an independent publisher-signature verification. `provenance/toolchain-installation.json`, `provenance/installed-executables-and-sandbox.json`, and `provenance/dependency-installation.json` contain the recorded versions, binary hashes and exact dependency revisions. The reported compiler is Lean 4.35.0-rc1 and the reported Lake is 5.0.0-src+86c6347.

The audit-owned scripts fetched dependencies at their exact lockfile SHAs with detached Git checkouts and disabled Git hooks. They did not run a project setup script or `lake update`. Project proof sources were not edited to make the build pass. See `provenance/build-config-audit.md` for the dependency-hook inspection and `provenance/upstream-build-config-source-digests.json` for the sources read during it.

The post-build `results/source-and-artifact-manifest.json` records unchanged hashes for all 4,232 original Lean source files, unchanged tracked dependency sources at all nine pinned revisions, and the unchanged root lockfile. It identifies 4,230 local `.olean` artifacts: 4,229 `HolomorphicAnosov` modules plus `Comparator.Solution`. No challenge `.olean` existed in this checkout. Binary hashes identify this execution's artifacts; they do not by themselves authenticate their proof content.

## Fresh-workspace setup

These commands describe a fresh Linux x86-64 workspace containing only copies of this bundle's `scripts/` and `checks/`, without its saved logs or results. Do not run them over the saved evidence directory: use a fresh workspace or new run names. The installer requires Python with the `zstandard` module and a version of `tarfile` supporting the data extraction filter. Git, curl and the platform runtime dependencies must already be available. No unspecified package installation is implied by these commands.

```sh
mkdir -p build downloads toolchains cache/mathlib logs provenance exports results
curl --fail --location \
  https://api.github.com/repos/leanprover/lean4/releases/tags/v4.35.0-rc1 \
  --output provenance/lean-release-metadata.json
python3 scripts/install_official_lean.py

git -c core.hooksPath=/dev/null init build
git -C build remote add origin https://github.com/frenzymath/HolomorphicAnosov.git
git -C build -c core.hooksPath=/dev/null fetch --depth=1 origin \
  65f2b33a7309de661a8500e4642e5609a537a8ff
git -C build -c core.hooksPath=/dev/null checkout --detach FETCH_HEAD
git -C build rev-parse HEAD
python3 scripts/fetch_pinned_dependencies.py

review_root=$(pwd)
review_toolchain="$review_root/toolchains/lean-4.35.0-rc1-linux"
review_lake="$review_toolchain/bin/lake"
```

`scripts/install_official_lean.py` verifies the named release, archive length and SHA-256 before extraction. `scripts/fetch_pinned_dependencies.py` verifies every dependency HEAD and that the root manifest hash is unchanged. Preserve their logs and provenance records.

## Cache and source build

The recorded cache operation used two Lean runtime threads:

```sh
python3 scripts/run_logged.py mathlib-cache -- \
  "$review_lake" --no-cache exe cache get
```

The official Mathlib `cache get` explicitly downloads matching upstream build artifacts. The separate Lake `--no-cache` option disables Lake's automatic artifact service; it does not disable this explicitly invoked Mathlib command. The recorded attempt completed with exit 0 after approximately 90 seconds; see `logs/mathlib-cache.json` and `logs/mathlib-cache.log`.

The selected source-build command is:

```sh
python3 scripts/run_logged_build4.py solution-build-four-threads -- \
  "$review_lake" --no-ansi --no-cache --fail-fast \
  build +Comparator.Solution:olean
```

This compiles the solution wrapper module and its required project dependency closure, using official cached upstream artifacts where available. It completed with exit 0 in 3,713.487 seconds, approximately 62 minutes. The final output was `Build completed successfully (13157 jobs).` See `logs/solution-build-four-threads.json` and `.log`. It is not a complete from-source rebuild of Lean and Mathlib, and it is not necessarily a build of every unused project file. Selecting `Comparator.Solution` also avoids treating the challenge's intentional placeholder proofs as solution proofs.

The logged runners remove inherited Mathlib cache endpoint/scope settings and `LEAN_PATH`, `LEAN_SRC_PATH`, and `LEAN_SYSROOT`; prepend the exact release's `bin`; set a dedicated `MATHLIB_CACHE_DIR`; and set `MATHLIB_NO_CACHE_ON_UPDATE=1`. The four-thread runner sets `LEAN_NUM_THREADS=4`. It samples cgroup memory once per second and requests SIGTERM of its owned process group if anonymous memory exceeds 12 GiB. The two-thread `run_logged_build.py` used for the exact-type/definition checks has the same anonymous-memory guard. The earlier `run_logged.py`, used for cache retrieval and the comparator attempt, instead guarded total task memory at 14 GiB. The environment has a 16 GiB cgroup ceiling and a CPU quota equivalent to four cores. These are runtime resource settings, not changes to theorem statements or proof options.

The first source-build run used two threads and was deliberately stopped with SIGTERM after approximately 179 seconds, then resumed incrementally with four threads after measured anonymous memory remained below 1 GiB. That stop is recorded in `logs/solution-build.json` and `logs/controlled-restart.json`; its `-15` exit code is not a source compilation error. The restart record also preserves an earlier process-selection guard that found no match and sent no signal, and a nonexistent-runner invocation that exited 2 before the actual controlled stop. The completed four-thread run observed task anonymous memory of 6,947,663,872 bytes, about 6.47 GiB; the file-cache-inclusive task total is a different measurement.

The runners refuse to overwrite an existing status file. Use the displayed names only in a fresh workspace with no saved run records; choose distinct names for any additional attempts and adjust dependent helper inputs accordingly. A complete result should retain the command, exit code, full output, elapsed time, measured memory scope, and log hash. Total cgroup memory includes reclaimable file cache and other activity in the task environment; it must not be described as a compiler's exclusive resident-memory peak.

## Exact statements and axiom inventory: completed

The actual external harness is in `checks/VerifyStatements.lean` and `checks/VerifyDefinitions.lean`; its explanatory file is `checks/README.md`. It imports Solution alone, copies all four complete expected interface types into a separate namespace, and requires each actual target and each public wrapper to inhabit the corresponding type. The second file checks selected definition expansions by `rfl` or `Iff.rfl` and prints the actual structures. No challenge placeholders are imported.

The successful corrected runs used two runtime threads:

```sh
python3 scripts/run_logged_build.py exact-statements-02 -- \
  "$review_lake" --no-ansi --no-cache env "$review_toolchain/bin/lean" \
  "$review_root/checks/VerifyStatements.lean"
python3 scripts/run_logged_build.py exact-definitions-02 -- \
  "$review_lake" --no-ansi --no-cache env "$review_toolchain/bin/lean" \
  "$review_root/checks/VerifyDefinitions.lean"
python3 scripts/summarize_axioms.py \
  --statements-step exact-statements-02 --definitions-step exact-definitions-02
```

Both compiler invocations returned exit 0: the statement run took 7.007 seconds and the definition run 8.007 seconds. The statements file prints full signatures and transitive axiom lists for all four actual targets, all four wrappers and eight audit assignments. The summarizer requires successful compiler status, verifies log hashes, requires every expected report, and enforces the whitelist in the unchanged comparator config. All 16 observed lists contained exactly `propext`, `Classical.choice.{u}`, and `Quot.sound.{u}`. The summarizer strips only a trailing printed universe annotation before comparing the canonical names. No additional axiom or `sorryAx` appeared in these lists. See `logs/exact-statements-02.json`, `logs/exact-definitions-02.json`, their full logs, and `results/compiled-axiom-summary.json`.

The initial `exact-statements-01` and `exact-definitions-01` invocations both exited 1 because the audit-owned harness files requested the unsupported pretty-printing option `pp.width`. Only that option was removed; the complete expected types, definition equalities, and axiom queries were retained. Initial harness copies remain in `checks/initial/`, and both failed logs and `logs/harness-correction.json` are retained. This was an audit harness error; no imported project proof was changed. The final harness SHA-256 values are `15806db0fbf002baccc39470692053d99422ef0358bfc2d44baf628cc013276d` for `VerifyStatements.lean` and `5f9b307e3497fa7c345447202799f9e00a22091b41f2b5a0dc6e4f5c827531da` for `VerifyDefinitions.lean`.

A clean global axiom inventory does not remove the explicit `HomotopyTorusRigidity` argument of Theorem A, 1.1 and 1.3. These exact-type checks use the actual imported definitions and copied complete interface types. They are not the blocked solution/challenge comparator, and they do not establish the ordinary mathematical semantics of every definition.

## Selected proof export and raw replay: completed

The release includes `leanexport` and `leanchecker`. Their pinned implementation was inspected separately; see `provenance/kernel-replay-plan.md`. The following is a direct selected-proof check, separately authorized from the blocked comparator workflow. It uses neither the comparator's private export mode nor a disabled isolation boundary.

After the completed source build, the actual export was run through the audit-owned helper:

```sh
python3 scripts/export_selected_targets.py
```

That helper required the successful build status, used four runtime threads with the same clean environment settings, and invoked the following command from `build/`:

```sh
"$review_lake" env "$review_toolchain/bin/leanexport" \
  HolomorphicAnosov.Targets.TheoremA -- \
  HolomorphicAnosov.theorem_A \
  HolomorphicAnosov.theorem_1_1 \
  HolomorphicAnosov.theorem_1_2 \
  HolomorphicAnosov.theorem_1_3
```

Standard output went only to `exports/selected-targets.ndjson`; stderr went separately to `logs/selected-targets-export.stderr.log`. The helper sampled memory and available disk every second, stopping its process group if task anonymous memory exceeded 12 GiB or workspace free disk fell below 3 GiB. The export completed with exit 0 in 140.375 seconds, with empty stderr. It is 2,385,351,648 bytes and has SHA-256 `2864d2b33f4020c69b5093af94e365da0866c5add9a3d580ef16421a2ab17276`; see `logs/selected-targets-export.json`.

The helper writes directly to the final filename, so existence of that filename alone does not establish completion. The terminal exporter status and completed-file hash must be checked before replay. In this audit an initial checker was inadvertently started while the exporter was still running. That owned checker process group was stopped after approximately 36 seconds, returning `-15`; its empty log and result are explicitly discarded in `logs/premature-replay-discarded.json`. It supplies no verification result. The exporter was allowed to finish, and only its completed exit and hash were used for the proper second run:

```sh
python3 scripts/run_logged_build4.py selected-targets-replay-02 -- \
  "$review_toolchain/bin/leanchecker" --from-export \
  "$review_root/exports/selected-targets.ndjson"
```

The proper run completed with **exit 0** in 722.322 seconds and reported `Lean default kernel accepts the solution`. Its complete log is `logs/selected-targets-replay-02.log` and terminal metadata is `logs/selected-targets-replay-02.json`. The separate presence audit in `results/export-target-presence.json` verifies all four selected targets occur once as theorems in the completed export. Replay log SHA-256: `b4a5a2119e1d34b46527d63317f417c74261b65eeb93f14026389da2519c2ead`. This is the actual same-kernel replay verdict, not comparator acceptance. Do not replay a partial export after failure, timeout, termination or disk exhaustion. Exporting the wrapper declarations instead would require module `Comparator.Solution` and the four `HolomorphicAnosov.zhang_theorem_…` names, with distinct output names.

The successful selected export/replay establishes acceptance of the exported proof terms and their dependency closure by the **same default Lean kernel implementation** in a freshly reconstructed environment. It is not an independently implemented checker. Raw replay permits exported axiom declarations; it does not itself enforce an axiom whitelist, compare the solution with the challenge, recursively compare their statement definitions, or validate their mathematical interpretation. Keep those evidence categories separate.

## Configured comparator: blocked

The attempted supported command was:

```sh
"$review_lake" comparator --config Comparator/config.json
```

This is the comparator bundled with the official release. It does not require installing the legacy standalone comparator or Landrun. The attempt is recorded in `logs/comparator-attempt.json` and `logs/comparator-attempt.log`; its required Bubblewrap isolation failed before the comparison. The default success message must not be imitated, and raw export/replay must not be relabelled as a successful comparator run.

When its supported isolation works, the comparator adds checks absent from raw replay: solution/challenge statement-dependency comparison and an allowed-axiom check, followed by kernel replay. It still does not prove correspondence between the formal definitions and the prose theorem. Do not substitute a broad `lake check` result: the default project targets include the challenge specification's intentional placeholders, which can produce an unrelated axiom failure.

## Interpreting the evidence

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| Cache download exit 0 | Matching upstream artifacts were retrieved/decompressed | Project theorem compilation or upstream from-source rebuilding |
| Selected source build exit 0 | Selected modules and required source closure compiled with the recorded inputs | Challenge comparison, independent kernel implementation, or mathematical semantics |
| Exact-type/definition harness | Only the recorded comparisons that actually passed | Every definition's ordinary mathematical correctness |
| Transitive `#print axioms` | Reported global axiom dependencies of selected declarations | Removal of explicit hypotheses or axiom-type identity by names alone |
| Selected raw export/replay exit 0 | Exported proof closure accepted by the fresh same-kernel environment | Axiom allowlisting or comparator equivalence |
| Configured comparator exit 0 | Its documented comparison, axiom and replay checks completed | Unconditionality where `HS` is explicit, or correctness of prose-to-formal interpretation |

The source build, corrected exact-type/definition harnesses, axiom inventory, selected export and proper same-kernel raw replay have completed successfully. The configured comparator remains blocked. A missing capability, deliberate stop, resource limit or timeout is an incomplete check; it is not evidence that the theorem is false.

## Evidence distribution

A reviewable evidence bundle should retain the audit scripts, final and initial harnesses, pinned-input provenance, source/artifact manifest, all successful and failed status records, and complete text logs. The large generated export can be distributed separately with its size and hash; omitting it from a small evidence bundle must be stated. No compiler, downloaded cache, dependency checkout, or generated proof export needs to be committed to the review repository merely to document these results.

This document uses only public source identifiers and relative evidence paths. Raw local execution records contain absolute workspace paths. If copies are normalized for public distribution, label them as normalized copies, hash those copies separately, and retain the private originals with their original hashes. Do not present a sanitized file as byte-identical to a recorded raw log or silently remove the failed and discarded attempts. Before release, exclude private attachment identifiers, task or conversation identifiers, credentials, and unrelated workspace files. The verification evidence concerns the pinned formal repository and does not require distributing the user's uploaded PDF.

Reproduction helper inputs use original raw log hashes. Public normalized status copies explicitly label those as original and supply separate published-copy hashes; rerun the commands in a fresh workspace rather than feeding normalized archival logs into a raw-run summarizer. `results/verification-summary.json` is the concise terminal status record.
