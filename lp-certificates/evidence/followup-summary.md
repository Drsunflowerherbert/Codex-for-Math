# Reviewed follow-up result

The checked bridge and original-input soundness layer are complete for the
documented bounded certificate forms. The first commit `44329696` remains in
history. The exact parser/transcription boundary is independently tested and
reviewed, but is not a proved parser-refinement theorem.

## Fresh aggregate verification

Executed from `/workspace/lp-research/lp-certificates`:

```sh
python3 scripts/verify.py --output evidence/followup-run-20261013T025400Z \
  --lean-bin /workspace/Codex-for-Math/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin \
  --cached-repository /workspace/Codex-for-Math
```

Exit `0`, receipt `passed`. All ten recorded subprocesses exited `0`, including
the published compiler byte audit tied to the actual selected compiler, source
pin checks, fresh five-module library build, 78 named-declaration axiom audits,
and both independently authored expected-value harnesses. Fourteen definition
body gates and six complete soundness-type gates passed. The two same-kernel
local replay phases retained 216 and 176 declarations.

The Python suite ran 143 tests in `8.092s`, `OK (skipped=2)`: 141 ran
successfully. The optional live and observed-package tests were separately
executed against actual packages, rather than inferred from those skips.
The old 72,900-document bounded certificate experiment and the new
4,374-problem finder experiment continue to agree with independent raw-row
arithmetic. The reported oversized integer gain and arithmetic-formatting
regressions return structured failure without acceptance or traceback.

## Checked exports and actual recheck

These are byte-preserving copies of complete observed attempts. Copying and
integrity inspection did not perform a new Lean check or rewrite any original
hash binding:

| Package | Supplied inputs | Fresh commands, all exit zero |
| --- | ---: | ---: |
| [Author batch](checked-author-batch/receipt.json) | 10 | 72 |
| [Independent batch](checked-independent-batch/receipt.json) | 13 | 75 |
| [Relocated CLI recheck](checked-relocated-recheck/receipt.json) | 1 | 63 |

Every input in these completed packages has a kernel-generated acceptance proof,
an original-real soundness theorem, complete expected-type and axiom checks,
a numeric-problem definition-body check, and same-kernel replay. Each attempt
freshly rebuilds the task modules and pinned helper, verifies nine input-layer
bodies and three original-real types, and performs unchanged-byte postflight.
No stale task OLean or saved receipt substitutes for a phase.

The author batch includes a witness produced by the incomplete exact finder.
The independent batch covers all nine accepted fixtures and four additional
cases: interleaved row senses and weights under minimization, a negative-coordinate
maximizing ray, exact noncanonical fractions, and an empty zero-dimensional
problem. The recheck used a relocated package whose saved command metadata was
changed to a `touch` command. The marker was never created; the new actual first
command invoked pinned Lean `--version` and all fresh phases passed.

See [package hashes](followup-packages.json),
[formal review](followup-formal-review.md),
[computational review](followup-computational-review.md), and the
[checked-bridge contract](../notes/checked-bridge.md).

## Failures, bounds, and remaining obligations

Failed attempts remain identified in the independent reviews and retained in
the cloud workspace. They exposed an unused missing `Cli` cache, an insufficient
virtual-address cap, generated record indentation, and concurrent-process memory
pressure. Each failed attempt remained failed and exported no final checked
member. The final runner retains bounded time, logs, CPU and memory settings;
heavy Lean verification was serialized. No gate or mathematical hypothesis was
removed to obtain the successful results.

The new public reports omit agent-routing identifiers. The first checkpoint's
historical reports and exact raw paths are preserved with their original hashes;
any integration publication derivative must retain that distinction.

The source retains free real variables, original rows/objective, rational
witnesses, and no slack/artificial decision variables. No added mathematical
axiom, admitted proof, strong duality, parser refinement, or finder completeness
is asserted. Cached dependency OLeans and host runtime remain trusted; replay is
the same Lean kernel. Linux evidence gives no native Mac/installed MRS claim.
