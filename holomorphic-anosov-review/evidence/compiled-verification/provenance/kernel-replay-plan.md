# Standalone export/replay plan for the four target proofs

> Historical read-only plan. The main verification track subsequently executed export and the finalized-export replay; consult `../results/verification-summary.json` for terminal outcomes. Optional compression/streaming transport below was researched but not used for this run.

Read-only inspection of the official installed Lean **4.35.0-rc1** sources. No exporter, checker, repository code, build, installation, or test was run in this subtask. The source checkout under review remains commit **65f2b33a7309de661a8500e4642e5609a537a8ff**.

## Supported commands

Standalone export/replay is a separately authorized compiled check of the audited source. It is distinct from running the bundled comparator. The comparator's failed `bwrap` probe blocks that comparator workflow; it does not by itself withdraw authorization for this standalone check. Do not override the comparator's sandbox, imitate its success message, or describe the following operation as comparator-equivalent.

After the required project modules have built successfully, run this export payload from the verification build checkout. The directories and variable names below do not repurpose system variables. The commands are a plan; they have not been executed here.

```sh
review_base=$VERIFY_ROOT
review_toolchain=$VERIFY_ROOT/toolchains/lean-4.35.0-rc1-linux
review_build=$VERIFY_ROOT/build
mkdir -p "$review_base/exports"
cd "$review_build"
env PATH="$review_toolchain/bin:$PATH" LEAN_NUM_THREADS=2 LEAN_ABORT_ON_PANIC=1 \
  "$review_toolchain/bin/lake" env "$review_toolchain/bin/leanexport" \
  HolomorphicAnosov.Targets.TheoremA -- \
  HolomorphicAnosov.theorem_A \
  HolomorphicAnosov.theorem_1_1 \
  HolomorphicAnosov.theorem_1_2 \
  HolomorphicAnosov.theorem_1_3 \
  > "$review_base/exports/four-targets.ndjson.part" \
  2> "$review_base/exports/four-targets-export.stderr.log"
```

Record the exit status. **Only after export exits 0**, rename the `.part` file and replay it:

```sh
mv "$review_base/exports/four-targets.ndjson.part" "$review_base/exports/four-targets.ndjson"
"$review_toolchain/bin/leanchecker" --from-export \
  "$review_base/exports/four-targets.ndjson" \
  > "$review_base/exports/four-targets-replay.log" 2>&1
```

Record the replay exit status, complete log, export byte size and SHA-256. Do not replay a partial export after failure, kill, timeout, or disk exhaustion. A failed source build or missing `.olean` means the required export environment is incomplete; it does not establish a false mathematical theorem.

`TheoremA` already imports the other three target modules. The named declarations are the actual target proofs. This import avoids the additional umbrella `import Mathlib` in `Comparator.Solution`, though the actual proof dependency closure may still be large. `lake env` supplies the pinned workspace's complete search path; it evaluates the already audited project/dependency configuration and is an ordinary authorized tooling action. If the build owner already recorded the correct `LEAN_PATH` and `PATH`, the same official `leanexport` payload can instead be run directly with those exact paths; do not guess a partial search path.

To check the four **public wrappers** instead, substitute module `Comparator.Solution` and declarations:

```text
HolomorphicAnosov.zhang_theorem_A
HolomorphicAnosov.zhang_theorem_1_1
HolomorphicAnosov.zhang_theorem_1_2
HolomorphicAnosov.zhang_theorem_1_3
```

Use distinct output/log names. Their recursive proof closure includes the actual target proofs, since each wrapper applies its target. Importing the wrapper module loads its entire import environment, but only the selected declarations and recursive dependencies are serialized. Do **not** import `Comparator.Challenge` for a solution-proof replay.

## Why these are the exact CLI forms

Paths below are relative to the installed official `src/lean/` directory.

* `LeanExport.lean:11–19` implements `leanexport MODULE ... -- CONSTANT ...`. It writes NDJSON to stdout; there is no `-o` option in this entry point. A bare `--` separates module names from constant names. Avoid optional `--ignore-missing` and `--export-unsafe`; neither is needed.
* `LeanExport/Basic.lean:252–304` exports both theorem types and **proof values**, recursively visiting constants used in each. `:458–476` documents and implements this dependency-closed selected export. Inductive blocks, constructors and recursors are exported together where required. This is not merely an export of the four propositions as admitted axioms.
* `Lean/Environment.lean:2439–2450` shows that this import defaults to `loadExts=false` and no plugins. It reads compiled module data without initializing the project environment extensions. The exporter still imports/maps project `.olean` data in its own process; this raw operation does not have the comparator's additional isolation boundary.
* `LeanChecker.lean:60–90` implements `leanchecker --from-export FILE`: parse the data, create an empty environment, replay the constant map through the Lean kernel, then check the special quotient declarations against the kernel-generated ones. On success its normal output includes `Lean default kernel accepts the solution`, with exit 0 after the quotient post-check. Leave off `--silent` to retain explicit evidence.
* `Lean/Replay.lean:19–30,71–145` explains replay: definitions/theorems are sent to the kernel; inductives are recreated and their constructors/recursors checked against the generated versions. The checker does not re-run project tactics or import project `.olean` files when reading the NDJSON export.

Do not use `leanchecker` without `--from-export` for this purpose: its default mode enumerates matching `.olean` modules and replays their new declarations over imported environments. `--fresh MODULE` is a different whole-import-environment replay, larger than the selected proof closure (`LeanChecker.lean:92–144`). Also do not assume these small entry points implement a conventional `--help`: their source parses flags directly.

## What a successful replay would and would not establish

A successful run would establish that the **exported selected proof terms and their exported dependencies** are accepted by the default Lean kernel in a freshly reconstructed environment. This is additional protection against a corrupted or manipulated elaboration environment. It is **the same Lean kernel implementation**, not an independent kernel implementation. The installed `leanchecker-paranoid` filename alone does not establish algorithmic independence; this plan makes no such claim.

Raw replay does **not** enforce an axiom whitelist. `Lean/Replay.lean` replays axiom declarations as axioms; `LeanChecker.lean` has no permitted-axiom CLI parameter. In particular, successful replay alone would not reject a valid proof term that depends on `sorryAx` or another extra axiom. Keep the existing exact-type/definition harness and transitive `#print axioms` evidence as separate checks. The expected allowed names are `propext`, `Quot.sound`, and `Classical.choice`; the explicit `HomotopyTorusRigidity` parameter of A/1.1/1.3 remains a hypothesis even with a clean global axiom list.

Raw replay also does **not** compare the four theorem statements with the independently imported challenge, recursively compare their definitions, or validate the ordinary mathematical interpretation of the definitions. An axiom-name list does not by itself compare the types assigned to standard axiom names. Exact statement/definition checks and the mathematical semantic audit retain their separate roles.

The bundled comparator supplies these additional checks: `lake/Lake/CLI/Check.lean:476–507` calls `compareAt`, `checkAxioms`, and then kernel replay. It explicitly adds the permitted axioms, quotient primitives, and other kernel primitive definitions to the comparison/export target list. Its supported invocation is:

```sh
"$review_toolchain/bin/lake" comparator --config Comparator/config.json
```

That workflow remains blocked if its required `bwrap` isolation cannot start. Do not set `LAKE_CHECK_EXPORT` manually: it selects the implementation's inner export-only branch. Do not call raw export/replay a successful comparator run.

`lake check` is also broader than this selected proof test: its inner implementation exports everything in the default modules (`lake/Lake/CLI/Main.lean:1189–1203`). The repository's default Comparator library includes the Challenge placeholders, so a broad default-module axiom failure could be caused by those specification `sorry` declarations rather than the actual solution proofs. The selected export above avoids this ambiguity.

## Resource expectations and bounded execution

No runtime or peak-memory measurement is available from this read-only inspection. The source import closure is thousands of modules. Even selected export loads the import environment and scans its constants to construct the recursor map (`LeanExport/Basic.lean:79–92`); its state preallocates a large expression hash table (`:52–57`). The checker parses the whole export into memory before replay. Significant RAM, disk space, and execution time are therefore plausible; do not promise that four target names imply a small job.

Run one exporter/checker at a time under the existing 16 GiB cgroup ceiling, retain separate logs, and monitor memory and disk. The single combined export deduplicates shared proof dependencies. If it exceeds resources, separate per-target exports with the corresponding target module can reduce individual closures at the cost of repeating shared work. Apply an explicit bounded execution budget and report resource exhaustion/timeout as an incomplete check, not proof rejection. No hard runtime estimate is justified before measuring.

No action was denied or executed by this subtask. The known comparator isolation failure is a separate pending capability blocker; the source build and authorized standalone checks are owned by the parent task.

## Disk-bounded follow-up: compressed finalized export and streaming replay

The checker **can consume a FIFO or `/dev/stdin`** as its FILE argument on Linux. This is supported by the source, although it has not been operationally tested by this subtask:

* `LeanChecker.lean:60–64` opens the supplied pathname in read mode and calls `parseStream (.ofHandle handle)`. It does not request a regular file, file size, or seek.
* `LeanExport/Parse.lean:492–506` repeatedly calls `stream.getLine`, parses each NDJSON line, and stops at EOF. It does not call `readFile`, rewind, or seek. Lines `510–516` return the accumulated constant map only after parsing ends.
* `Init/System/IO.lean:721–726` specifies newline/EOF semantics for `getLine`; `:970–971` defines `withFile` simply by `Handle.mk` followed by the supplied action.

Consequently, **after** the exporter and compressor have both exited successfully, the immutable finalized compressed export may be replayed without expanding its text to disk. If `zstd` is available, the exact checker payload is:

```sh
set -o pipefail
zstd -dc -- "$review_base/exports/selected-targets.ndjson.zst" \
  2> "$review_base/exports/selected-targets-decompress.stderr.log" \
  | "$review_toolchain/bin/leanchecker" --from-export /dev/stdin \
      > "$review_base/exports/selected-targets-replay.log" 2>&1
```

Capture **both pipeline component statuses immediately** (in Bash, `${PIPESTATUS[@]}` before any subsequent command). Require decompressor exit 0 and checker exit 0. `gzip -dc -- finalized.ndjson.gz` can replace the decompressor for an archive actually produced with gzip. Do not send compressed bytes directly to the checker; it expects NDJSON.

To avoid the current raw-text disk growth on a new export attempt, stream the official exporter's stdout into a compressor such as `zstd -T1 -1 -c`, writing only `selected-targets.ndjson.zst.part`. Keep the exporter stderr separate, use `pipefail`, and record **both exporter and compressor exit statuses**. Finalize/rename/hash the archive only after both exit 0. A completed raw export can instead be compressed after its exporter exits successfully; any cleanup of redundant generated text should follow verified archival integrity, not race a growing output file. A resource-stopped export remains incomplete and must not be promoted to the final archive.

Record the finalized compressed file's SHA-256 and, through a separate successful decompression pass if desired, the decompressed stream's SHA-256 and byte count. Verify that all four selected theorem declarations are present in the completed exported constant map. This last check matters because the format has no mandatory end-of-export marker: a syntactically complete prefix can parse and replay successfully while omitting later selected targets. A producer failure must never be turned into apparent success merely because its downstream checker exits 0.

Using a pipe does **not** weaken checking when the decoded bytes are the same complete export. It changes only the transport into the same parser; the same freshly reconstructed map is replayed by the same kernel. A FIFO works for the same reason, but requires coordinated reader/writer startup and separate writer status collection; `/dev/stdin` with an ordinary pipeline is simpler.

This saves **disk**, not the principal checker memory requirement. `Parse.lean:36–46` retains name, level, expression, recursor-rule, and constant maps while reading, and the complete environment is parsed before replay starts. Decompression is streamed, but the proof graph remains in RAM. Continue monitoring the 16 GiB cgroup ceiling. Prefer finalized-export-then-checker execution over a simultaneous exporter-to-checker pipeline: the latter combines the two heavy processes, complicates producer-failure handling, and is unnecessary here.
