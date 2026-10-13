# A checked bridge from original JSON to Lean instances

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](../PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

`bridge.py check` creates a fresh package only after compiling a generated
instance, proving its acceptance by `decide +kernel`, checking the complete
declaration types and allowed transitive axioms, and replaying the local
declaration closure with the same Lean kernel. Its final positive status is
`lean_checked`. Exact Python acceptance alone does not produce that status.

The bridge transcribes the original mixed rows and objective sense into
`InputProblem`. The `≥` sign flips, equality masks, and minimizing-objective
conversion are computed in Lean by `normalizeInput`; the original-real
soundness theorems relate those normalized checks to the original constraints
and objective. No theorem proves this Python parser/transcription faithful to
every JSON input. That interface remains trusted, separately inspected code.

## Use

Run from a trusted checkout of `lp-certificates/` with the existing pinned
Linux Lean installation and trusted pinned dependency caches:

```sh
python3 bridge.py check \
  examples/optimal_*.json examples/infeasible_*.json examples/unbounded_*.json \
  --output ${TEMP_ARTIFACT} \
  --lean-bin /absolute/official/lean-4.24.0-linux/bin

python3 bridge.py recheck ${TEMP_ARTIFACT} \
  --output ${TEMP_ARTIFACT} \
  --lean-bin /absolute/official/lean-4.24.0-linux/bin
```

Both output paths must be new leaves under existing directories. Existing
attempts, symlink paths, parent traversals, and nonregular input files are
rejected. There is no command that publishes an unchecked generated theorem.
The internal `_render_unchecked` helper exists for inspection and tests only.

The bridge installs nothing, performs no network operation, and does not modify
the repository's existing caches. It needs the repository's published
`math-evidence/lean/EvidenceHarness.lean` sibling and the current trusted LP
source modules. The nine dependency checkouts must match the pinned manifest
revision/origin and report empty tracked Git status. Index flags can hide changed
tracked bytes; this is not a strict dependency byte comparison. Eight existing dependency
library caches are used in the current environment. The locked `Cli` source is
also inspected; its absent, unused build cache is recorded as
`absent_not_imported`. Missing required caches fail the attempt.

## Bounded input and controlled source

The supported subset has:

- at most 64 KiB of UTF-8 original JSON per document;
- at most eight variables and sixteen original rows;
- at most 256 bits in each **raw** rational numerator and denominator;
- one through sixteen supplied documents per batch.

The existing verifier's strict v1 schema still applies: duplicate keys, floats,
booleans in rational slots, nonstandard constants, unknown fields, malformed
fractions, and inconsistent dimensions are invalid. A valid document outside
the bridge's narrower bounds is unsupported. A well-formed false certificate is
rejected. Those dispositions occur before a Lean process is launched. A batch
that fails preflight does not export checked members.

The source generator has fixed namespace, declaration names, imports, theorem
templates, and syntax. It emits only canonical integer/fraction literals,
controlled `RowSense`/`ObjectiveSense` constructor tokens, and a validated
SHA-256 hexadecimal comment. It never inserts a user identifier, expression,
path, field name, or arbitrary string into Lean code. Original row and coordinate
order are preserved. Inequality/equality multiplier arrays are interleaved into
one original-row-order vector; their signs are retained, and the Lean row masks
select the appropriate multipliers. This is not a new optimization algorithm.

## What a package preserves

Each completed attempt retains:

- `inputs/NNNN.json`: the exact original input bytes and their SHA-256;
- `semantic/NNNN.json`: canonical exact original coefficients, right-hand
  sides, dimensions, row order/senses, objective sense, and certificate values;
- `project/CheckedNNNN.lean`: the numeric instance, kernel acceptance proof,
  original-real conclusion, complete expected-type/axiom gates, and replay gate;
- copied trusted Lean sources, the unchanged pinned evidence helper, and pinned
  Lake configuration in `project/`;
- separate bounded stdout/stderr logs, exact process argv/cwd, exits,
  timestamps, byte counts, and hashes in `receipt.json`;
- source and package manifests covering the retained files.

The generated source and semantic/source manifest are deterministic for the
same input bytes, document order, and trusted source version. Runtime receipts
contain actual times and paths and are not expected to match across executions.
The complete package manifest deterministically hashes the particular files
in that attempt; it is not a signature or historical event attestation.

All task library modules and the helper are compiled into an empty, private
library directory once per batch. Every instance gets a fresh compilation.
Neither stale task OLeans nor a packaged compiled product can substitute for
these phases. Temporary dependency-cache links and compiled products are removed
after their hashes have been recorded and checked, so the portable package
contains sources and evidence rather than `.lake` caches or binary products.

## Fresh acceptance gates

The runner checks the published Linux Lean 4.24.0 loader and four runtime
library byte pins, then checks the actual reported compiler version/commit.
The independently written `ExpectedInput.lean` harness checks nine definition
bodies, all three original-real soundness theorem types, allowed transitive
axioms, and same-kernel local replay.

For each generated instance, the runner requires:

1. a fresh successful compilation of `accepted` using `decide +kernel`;
2. an instantiated original-real `sound` theorem;
3. closed whole-type kernel equality and allowed axiom checks for both theorems;
4. a numeric `InputProblem` definition-body match;
5. replay of both targets in the local declaration closure against
   `[Mathlib, EvidenceHarness]`.

Postflight compares the original and copied source bytes, generator and verifier
hashes, compiler/runtime hashes, dependency identities, every recorded log,
and every compiled product against the preflight or freshly recorded identities.
A changed artifact, missing marker, malformed marker, warning/error, or failed
phase prevents the final positive status. If a later phase fails, completed
instance phases remain evidence in the failed receipt, but no instance retains
a final `lean_checked` disposition in that failed attempt.

## Recheck does not execute a supplied package

`recheck` validates regular-file layout, complete manifest coverage and hashes,
input snapshots, canonical semantic tables, the current numeric renderer's
source, current trusted library/helper bytes, required phase inventory, and
recorded log/gate consistency. Process fields do not receive a complete strict
type/consistency gate: boolean exit codes, noncanonical timestamps, negative
PIDs and malformed recorded working directories can survive coherently rehashed
saved metadata. It rejects unexpected members or runtime caches.
It then reads the saved **original** strict JSON and calls the fresh `check`
pipeline using current trusted code and a new output directory.

Supplied Lean files, saved argv, receipts, statuses, and binary products are
never executed or treated as fresh proof evidence. A stored report, even one
that is internally consistent, establishes no historical execution authenticity.
Only the newly observed compilation and gates can produce the new positive
status. The current generator/verifier and source version must match the saved
package for this v1 recheck; migration across versions is not implemented.

## Resource failures and trust limits

Each process has a 240-second wall limit, a bounded CPU limit, a sixteen-GiB
virtual-address limit, bounded file descriptors and file sizes, and separate
two-MiB log caps. Lean compilation uses one worker and a four-GiB Lean memory
setting. Timeouts, output overflow, SIGINT, and SIGTERM cancel the process group,
including descendants, and fail the attempt. A hard SIGKILL can leave an
`in_progress` attempt and temporary files; that is not acceptance and cannot be
resumed as a completed package.

The host runtime and trusted dependency OLeans are assumed; dependencies are not
rebuilt from source. Replay uses the same Lean kernel implementation, rather
than an independent implementation. This is not an OS sandbox against a hostile
host or concurrent attacker. Linux evidence does not establish native Mac or
installed MRS integration. None of these phases proves certificate finding,
algorithm termination/completeness, strong duality, or a proved JSON parser.

Exit codes are `0` for `lean_checked`, `1` for `rejected`, `2` for `invalid`,
`3` for `unsupported`, `4` for `failed`, and `5` for `in_progress`. An interruption
observed by the runner returns failure. Hard-killed processes cannot emit a
normal final exit report.

## Observed development checks

The bridge boundary suite is reproduced with:

```sh
python3 -m unittest discover -s tests -p test_bridge.py -v
```

Initial observed result: 33 tests passed, exit `0`. This suite checks the input
and numeric-rendering boundaries, raw mixed directions/objective/order,
symlinks/FIFOs/existing outputs, timeout descendant cancellation, bounded output,
and forged/malformed package rejection. These are implementation tests, not
Lean acceptance.

Early live attempts were preserved as failures: a missing unused `Cli` cache
was first treated as required, then two compilations aborted at `Examples.lean`
under an eight-GiB virtual-address cap. Controlled diagnosis with the pinned
compiler, one worker, and a four-GiB Lean memory setting gave exit `-6` at the
eight-GiB address cap and exit `0` at sixteen GiB, both with physical peak usage
below three GiB. The bound was adjusted to sixteen GiB without changing a
mathematical check or kernel gate. Successful final live results are separate
from those failed attempts. Later simultaneous large replay runs exceeded this
host's sixteen-GiB memory limit, so final author and independent runs were
sequenced. The Lean memory setting does not cap all imported/runtime memory.

The author generated one additional exact certificate with the current finder:

```sh
python3 - <<'PY'
import finder,json,pathlib
problem={"version":1,"problem":{"objective":{"sense":"max","coefficients":[3,2]},"constraints":[{"coefficients":[1,1],"sense":"<=","rhs":4},{"coefficients":[1,0],"sense":">=","rhs":0},{"coefficients":[0,1],"sense":">=","rhs":0},{"coefficients":[1,-1],"sense":"=","rhs":0}]}}
result=finder.find(problem)
print(json.dumps({'status':result['status'],'kind':result.get('kind'),'certificate':result.get('certificate_document',{}).get('certificate')},sort_keys=True))
if result.get('status')=='found':
 path=pathlib.Path('${TEMP_ARTIFACT}')
 with path.open('x') as out: json.dump(result['certificate_document'],out,indent=2,sort_keys=True); out.write('\n')
 print(str(path))
PY
```

Observed exit `0`, finder status `found`; candidate `(2,2)`, inequality
multipliers `(5/2,0,0)`, equality multiplier `1/2`. That certificate is a supplied
witness for the next step; its production does not certify the finder complete.
Finder source SHA-256 was
`bc91178bb5dd8b779ca6f565fa5cbea38c4feb2f0bbee7b9e07a795c43758876`;
generated input SHA-256 was
`5a5de45c186cae9a39039218046ce832493fec15f444e91a5be82069a8b7f75d`.

The actual author batch command was:

```sh
python3 bridge.py check examples/optimal_*.json examples/infeasible_*.json \
  examples/unbounded_*.json ${TEMP_ARTIFACT} \
  --output ${TEMP_ARTIFACT} \
  --lean-bin ${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin
```

Observed exit `0`, final `lean_checked` at `2026-10-13T02:42:05.136908+00:00`.
All ten input instances passed; 72 recorded commands completed; sixteen fresh
compiled products were hashed before removal. The library gate checked nine
definition bodies and three theorem types. The instance gates checked twenty
complete theorem types, ten numeric problem bodies, and ten local replays.
The tenth instance is the finder-produced certificate and certifies original
objective value `10`. All postflight identities were unchanged.

The receipt binds bridge source SHA-256
`c0fe2cbfc7511309f91524e86ed8e5342f0d891c090a343a0a1ee06736774dd2`
and verifier source SHA-256
`bb55c5f57a91d9c8c225ab3dc219a718a383e13249314fff29b5a1ad33e290fb`.
Author package hashes:

```
877d9f1d3fd1e694df1e36cdc2337649a9bc39d535c412623c743521a87f388f  receipt.json
e55a49e3792736c710e39e0f5023fa566d7d0cc23e75c0ef9704df77ec1b3606  source-manifest.json
14ab5b288299e90dac3978335884cdaa5587c438087937d9b61b80921e7d564c  package-manifest.json
```

Subsequent integrity inspection with `validate_package` returned all ten input
snapshots. That inspection grants no new fresh execution claim. Independent
raw-source review and a newly executed recheck are recorded separately by the
independent verifier reviewer.
