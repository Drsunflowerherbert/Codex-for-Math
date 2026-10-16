# Official toolchain and comparator provenance

> This is the read-only provenance subtask record. The main track subsequently installed and executed the official compiler and checked the selected source. Current terminal results are in `../results/verification-summary.json`; statements below about no execution describe this provenance subtask only. The official comparator was attempted but could not start its namespace sandbox.

Read-only provenance research, 16 October 2026. This track did not install or run Lean, Lake, comparator, exporters, sandbox executables, repository setup scripts, or repository proofs. The main verification track handles installation and execution separately.

## Lean release

- Official release: <https://github.com/leanprover/lean4/releases/tag/v4.35.0-rc1>.
- Official release API: <https://api.github.com/repos/leanprover/lean4/releases/tags/v4.35.0-rc1>.
- Release published: `2026-09-15T15:02:13Z`.
- Full release commit: `86c6347c75e39ec18c40e25ed2143b71a6e04a0a`.
- Official Linux archive: <https://github.com/leanprover/lean4/releases/download/v4.35.0-rc1/lean-4.35.0-rc1-linux.tar.zst>.
- Expected archive length: `594218389` bytes.
- GitHub release-asset SHA-256 digest: `a299763401c3b9b8e19bcca26f8443b40ae24962c3c3ddee73b5c72194877f65`.
- ZIP alternative: <https://github.com/leanprover/lean4/releases/download/v4.35.0-rc1/lean-4.35.0-rc1-linux.zip>; length `926104577`; SHA-256 `3a6e1e9ce0cc78a0d34b0e18b803e98e5bb8ad91c12323dfde4605f3091380f3`.

The release API lists ten platform archives, with digests, and no separate checksum/signature asset. The API reports the release commit as unsigned. This records GitHub's metadata, not independent cryptographic authentication of the publisher or an independently checked GPG signature. Downloaded archive checks belong in the execution record.

The complete official release metadata is in `lean-official-release-v4.35.0-rc1.json`. The full commit identity is also recorded in `comparator-pinned-source-metadata.json`.

## Selected path: comparator bundled in the official rc1 release

The installed official release contains `lake comparator` and `lake check`. The implementation is named `Lake/CLI/Check.lean`, rather than a file named Comparator. The initial filename-only API-tree search missed that implementation; the inference that rc1 lacked it was corrected before execution was proposed.

Five installed source files were compared byte for byte with their official raw files at the full release commit, and all matched:

| Source path under `src/` | SHA-256 |
| --- | --- |
| `lake/Lake/CLI/Help.lean` | `438d26afbdef9dfb234ddd3bda9d08f5694af982cd24c4b050750c07f6755301` |
| `lake/Lake/CLI/Main.lean` | `3e0dd82bf00d7958b11c432ac4d70a7951751276fe970c459a7d1c34ecd7868a` |
| `lake/Lake/CLI/Check.lean` | `0b27599383a5a49d461d946429a70e67431b9fc8fdbdd922a06b01eacc7a1d93` |
| `lake/Lake/Check/Axioms.lean` | `261fa54494a6a17c23b8588d788ab1080e5c39af2143948f8e140cfa295560d1` |
| `lake/Lake/Check/Compare.lean` | `0281630a33b8f08a9f3f40f229cd843c02441a0cd4d8a6d8548dc2bb8ded4c68` |

Exact URLs and match results are in `bundled-comparator-source-match.json`. For example, the official implementation is <https://github.com/leanprover/lean4/blob/86c6347c75e39ec18c40e25ed2143b71a6e04a0a/src/lake/Lake/CLI/Check.lean>.

This implementation uses the release's own `leanexport` and `leanchecker`; the exporter is deliberately not configurable. It requires `bwrap`, `git`, and `env`, and has no unsandboxed mode. Read-only command discovery found an existing `/usr/bin/bwrap`. No test of its namespace capability was performed by this track. The builtin comparator does not need Landrun, a separately installed comparator, or external `lean4export`.

From a pristine checkout of the already selected paper repository commit, with the pinned manifest retained, the supported command is:

```sh
cd /path/to/pristine/pinned-checkout
/path/to/lean-4.35.0-rc1-linux/bin/lake comparator --config Comparator/config.json
```

The `--config` option matters: the builtin default is `comparator.json`, whereas this project supplies `Comparator/config.json`. The config names the four intended solution targets and permits only `propext`, `Quot.sound`, and `Classical.choice`. It requests no external checker.

The builtin comparator resolves and builds within Bubblewrap, exports the challenge and selected solution declarations, checks their statement dependencies and permitted axioms, then invokes the bundled checker. Its exit statuses distinguish acceptance (`0`), rejection/build failure (`1`), and inability to start (`2`). Checking whether it actually starts and succeeds remains the main execution track's responsibility.

`lake check` is a different operation: it checks the project's default build targets. Those include the challenge specification with four intentional `sorry` proofs. A rejection caused by that specification is not, by itself, rejection of the selected solution proofs. The configured comparator is the appropriate challenge-versus-solution test. A successful result still checks the formal statements, including their explicit `HomotopyTorusRigidity` premises; it does not remove those premises or establish semantic correspondence with the manuscript.

## Legacy standalone comparator: researched alternative, not needed

The paper repository's README gives the older `lake env comparator Comparator/config.json` route. The official standalone source is <https://github.com/leanprover/comparator>. Its matching `v4.35.0-rc1` tag resolves to `909385295ed8a9248e87930a79513b5627b189df`. Its toolchain matches rc1, and its lockfile pins official <https://github.com/leanprover/lean4export> to `fd0d78eaa91750096cf519907b266efb1b26bf22`. GitHub reports both commits as signature-verified; this track did not independently verify their signatures. The standalone comparator has no release assets.

In that legacy version, calls to the sandbox runner are mandatory. `COMPARATOR_LANDRUN` changes the executable path; it does not turn sandboxing off or recognize the host execution environment's sandbox. The provided development shim runs commands without those protections and is not an equivalent supported verification setup. Its pinned README additionally specifies a systemd socket-family restriction for that route. These are reasons to prefer the already available official builtin comparator, not reasons to install another tool now.

The linked third-party runner's official upstream is <https://github.com/Zouuup/landrun>. At retrieval its `main` was `811cfff51ceaf3d9843708aa6d22e9b84ccac8b4`; its source requires Go 1.24.0 and pins `go-landlock` 0.9.0. It is outside the `leanprover` organization. If the legacy route were selected, installing or executing that new third-party tool would require confirmation that it falls within the user's executable authorization. No such action was taken here. That possible approval question is avoided by the selected builtin route, which uses existing Bubblewrap.

Metadata for the legacy comparator, exporter and runner was retained privately during research; the public evidence selects the builtin official route and excludes those unused metadata files. No recommendation is made to install optional Nanoda or any external checker.

## Evidence boundary

Included files are official public release/repository metadata, source hashes, and these audit-authored notes. They contain no credentials, private attachment/task identifiers, repository proof code, or full copied documentation. Public GitHub signature records are provenance metadata, not secret keys. No source fetched for this track was executed.
