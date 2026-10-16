# Build configuration and cache provenance audit

Target commit: `65f2b33a7309de661a8500e4642e5609a537a8ff`.

Scope: read-only inspection of the submitted formalisation checkout, its pinned manifest, the exact upstream dependency configurations, and the pinned official Mathlib cache implementation. No Lean/Lake build, installation, repository executable, npm command, or setup script was run by this audit. Network actions were ordinary reads of pinned upstream source files. A companion [JSON digest list](upstream-build-config-source-digests.json) records the upstream URLs, byte sizes, and SHA-256 values read.

## Actionable findings

1. **Keep the checked-in lock manifest.** The root requires official Mathlib tag `v4.35.0-rc1`, resolved by the manifest to `c32e1ec0d1eb5237ba344eee50162f45d5b0fc76`. All eight transitive dependency revisions agree with that exact Mathlib commit's own manifest. Avoid `lake update` or rewriting the manifest during verification.
2. **Suppress the dependency auto-cache hook while preparing the workspace.** Pinned Mathlib has a `post_update` hook that runs its cache executable for downstream projects. `MATHLIB_NO_CACHE_ON_UPDATE=1` disables that hook, allowing a separate, logged cache-fetch step after the dependency revisions and source are checked. This is a concrete executable hook in the upstream dependency, not the paper repository.
3. **Use an isolated Mathlib cache and ordinary official cache reads.** Set a dedicated `MATHLIB_CACHE_DIR` under the verification workspace; remove inherited cache URL/container/scope overrides. Do not use cache `--unsafe`, alternate commit scopes, or a fork cache for this reproducibility run. The tool permits those choices, but they widen which compiled artifacts are trusted.
4. **ProofWidgets has npm build hooks.** Its pinned Lake configuration can run `npm install` when rebuilding its package lock, and `npm clean-install` plus `npm run build` for a JS rebuild. Pinned Mathlib supplies an `errorOnBuild` setting intended to reject an unexpected ProofWidgets JS rebuild. The package-lock target is fetched before that guard, so do not assume this guard makes every npm execution impossible. If cache reuse requests a JS/npm rebuild, record it and inspect that branch rather than disabling the guard silently.
5. **Respect the actual resource limit.** This environment has a 16 GiB cgroup memory ceiling and a CPU quota equivalent to four cores; a processor-count utility reports five available processors. The workspace had approximately 30 GiB free; the separate temporary filesystem had 8.8 GiB. Put toolchain, package checkout and expanded cache under the workspace, start conservatively, and monitor resident memory, concurrent compiler processes and disk growth. `LEAN_NUM_THREADS=2` is a reasonable starting setting; do not assume an undocumented `lake -j` option is available for this version.
6. **Separate source compilation from comparator verification.** The README's comparator step additionally requires `comparator`, `lean4export`, and `landrun`; these are not locked by the repository manifest. Record any separately obtained versions and provenance. A successful `lake build` alone does not establish that an external comparator run occurred.

## Repository configuration

`lakefile.toml:1–17` is declarative. It has two default library targets, `HolomorphicAnosov` and `Comparator`; the latter roots are `Comparator.Challenge` and `Comparator.Solution`. There is one direct dependency, the official Mathlib GitHub URL. There is no root `lakefile.lean`, custom executable target, post-update hook, shell script, workflow directory, git submodule, tracked symlink, native library or precompiled `.olean`/archive in the tracked tree inspected.

The root library glob includes all project submodules, so the default build is broad. There are 4,232 Lean source files including the root importer and the comparator files. Many local proof options increase computational budgets: 89 occurrences of `maxHeartbeats`, up to 4,000,000; 23 recursion-depth settings, up to 4,096. No zero/unlimited heartbeat setting was found by the targeted option scan. These finite budgets still allow individual compilation units to be expensive.

A targeted scan found no project `IO.Process`, filesystem/network operations, FFI declaration, custom tactic/elaborator registration, `#eval`, or initializer. One actual elaboration command occurs at `Comparator/Challenge.lean:134`: it clears Lean's auxiliary-lemma environment cache to align elaborated definitions with the library. It does not run an operating-system process. This scan is supporting evidence, not a proof that elaborating arbitrary Lean source is incapable of execution; ordinary imported tactics and the Lake configuration are executable trusted tooling.

The fixed toolchain file contains `leanprover/lean4:v4.35.0-rc1`. The root manifest's `fixedToolchain` field is false, while pinned Mathlib declares its toolchain fixed. Use the exact release named in the file and record the actual `lean`/`lake` version and binary digest; do not substitute a later stable release.

## Locked dependencies

| Package | Locked revision | Configuration inspected |
|---|---|---|
| Mathlib | `c32e1ec0d1eb5237ba344eee50162f45d5b0fc76` | `lakefile.lean` |
| plausible | `16fe28ca7c2e01b71856f7a0a801ea844580f2d5` | `lakefile.toml` |
| LeanSearchClient | `b43172c7f62b95ecd6daa0951602b83eb35182a1` | `lakefile.toml` |
| importGraph | `0b9118a4a6d4c752e51f4f731edc09f4cc135f4c` | `lakefile.toml` |
| ProofWidgets4 | `af0c1665a9cdb1c90409b52a183113efbb5a4480` | `lakefile.lean` |
| aesop | `7938bfd115516f80b260d43faf630c8520471a00` | `lakefile.toml` |
| Qq / quote4 | `21558817bf8b77bab8f4c3081e0062201fd974d2` | `lakefile.toml` |
| batteries | `2a71587431553220d08be069a144b8215350e1d6` | `lakefile.toml` |
| Cli | `3c7ccd7060887fa478a55e555fae61bbf466c3ba` | `lakefile.toml` |

All URLs are under `leanprover-community` or `leanprover`. Apart from Mathlib and ProofWidgets, these inspected package configurations declare Lean libraries and optional test/lint/graph executables, without custom setup hooks. Their source code and full runtime behavior were not exhaustively audited.

## Pinned official Mathlib cache

The repository documents `lake exe cache get` before `lake build`. The exact official Mathlib [Lake configuration](https://github.com/leanprover-community/mathlib4/blob/c32e1ec0d1eb5237ba344eee50162f45d5b0fc76/lakefile.lean) defines `cache` with root `Cache.Main`, describes its precompiled-artifact purpose, and contains the downstream update hook.

The pinned [cache command](https://github.com/leanprover-community/mathlib4/blob/c32e1ec0d1eb5237ba344eee50162f45d5b0fc76/Cache/Main.lean) implements `get` as download plus decompression of matching missing artifacts. Without module arguments it starts at `Mathlib`; this is appropriate here because the comparator challenge imports `Mathlib`. It also implements uploads, cleaning, alternate scopes and unsafe history fallback, but those are separate commands/options and are unnecessary for this run.

Pinned [cache IO](https://github.com/leanprover-community/mathlib4/blob/c32e1ec0d1eb5237ba344eee50162f45d5b0fc76/Cache/IO.lean) obtains `leantar` from the selected Lean toolchain's `bin` directory and runs it for extraction; it does not download a separate leantar executable. It normally uses system curl, with a static-curl download fallback for old versions. This environment's curl is 8.14.1, satisfying the tool's 7.81 threshold, so that fallback should not be needed. The dedicated cache directory also prevents reuse of any pre-existing cached curl or artifact files.

Pinned [cache infrastructure](https://github.com/leanprover-community/mathlib4/blob/c32e1ec0d1eb5237ba344eee50162f45d5b0fc76/Cache/Infra.lean) selects `https://cache.mathlib.org` as the public endpoint; the official Mathlib repository's normal container chain is `master`, then `legacy`. [Cache requests](https://github.com/leanprover-community/mathlib4/blob/c32e1ec0d1eb5237ba344eee50162f45d5b0fc76/Cache/Requests.lean) allows endpoint, container and scope overrides, and checks downstream toolchain/manifest agreement. Clear `MATHLIB_CACHE_GET_URL`, `MATHLIB_CACHE_BASE_URL`, `MATHLIB_CACHE_FROM`, `MATHLIB_CACHE_REPO_SCOPE`, and `MATHLIB_CACHE_DEBUG_USE_LEGACY` before the explicit fetch, or log any intentionally retained setting. Avoid `--unsafe` and `--scope` for the ordinary pinned upstream fetch.

The cache supplies **compiled upstream artifacts**. Their source-addressed selection and official provenance do not mean every imported Mathlib proof is being rebuilt in this verification attempt. Keep that distinction in the final evidence statement.

## Suggested execution sequence for the build owner

- Create a fresh checkout at the pinned project commit with no project build artifacts copied in.
- Install the exact official Lean release into a dedicated workspace directory and record the release URL, binary/archive hashes and reported versions.
- Preserve the lock manifest; set a dedicated cache directory and suppress the automatic update-cache hook while dependencies are prepared.
- Check the actual dependency checkout SHAs against the table, inspect/record any generated configuration changes, then invoke the ordinary official cache `get` explicitly and retain its complete output and exit code.
- Run the required library/comparator Lean targets with conservative initial resource settings. Keep complete logs and distinguish a source/type error from a process kill, timeout, disk exhaustion or cache miss.
- Run any intended independent export/comparator checks only with separately recorded tool versions. Report precisely which targets and checks finished.

This audit found no concrete malicious root setup customization. The identified execution surfaces are ordinary dependency hooks and cache/build tooling described above. No build success or proof correctness is claimed by this configuration inspection.
