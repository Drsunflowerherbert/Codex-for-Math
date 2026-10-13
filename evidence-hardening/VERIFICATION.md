# Verification of the frozen companion

Final fixture source digest:
`738cae9009e2dc05dab9ff2081372326e87402bd4ea24e3845acf115d68b0500`.
Production code and fixture policy were frozen by 02:03 UTC on 2026-10-13,
well before the 04:05 development cutoff. Independent final tests used a
disposable source snapshot and record matching before/after source hashes.

## Final acceptance results

| Suite | Result | Actual scope |
| --- | --- | --- |
| [Node/filesystem/Git regressions](evidence/node-regression.json) | 49/49, exit 0 | Process metadata, strict JSON/logs, regular-file/FIFO guards, real capture failures/timeouts, index flags and replacement refs |
| [Pinned Lean corpus](evidence/lean-corpus.json) | 10/10, exit 0 | One positive and nine intended-gate negatives; all targets compile, only the positive passes formal gates |
| [Independent v1 receipts](evidence/independent-v1-receipts.json) | 57/57, exit 0 | Actual baseline success import, 55 contradictory/changed negatives, aged integrity-only receipt |
| [Independent fixture receipts](evidence/independent-fixture-receipts.json) | 45/45, exit 0 | Actual fresh fixture import, 43 changed/contradictory negatives, aged integrity-only receipt |
| [Independent runtime/source/policy](evidence/independent-runtime.json) | 5/5, exit 0 | Actual pinned Lean timeout and observed-process abort; preabort; unpinned source; stale policy rejection |
| [Pinned package byte checks](evidence/pinned-package-sources.json) | 9/9, exit 0 | Exact tracked source bytes for all baseline packages, including 7,575 mathlib files |

These are distinct suites and observations, not a combined number of formal
proofs. Both inspectors grant zero imported Lean passes. The adversarial reviewer
also independently reran the 49-case Node suite and directly tested FIFO,
replacement-ref, coherent-synthetic and stale-old-receipt cases.

The independent test author contributed the three disclosed test harnesses under
`tests/`; that subagent did not edit production code. A separate adversarial
reviewer inspected implementation and formal scope without production edits.
See [adversarial review](reviews/final-adversarial-review.md) and
[verification review](reviews/final-verification.md).

## Exact commands and captures

[commands.json](evidence/commands.json) records actual argv, cwd, times, exits,
stdout/stderr sizes, SHA-256 and text for baseline and final companion wrappers.
Paths identify the disposable execution locations; they are not portable default
paths or commands imported by an acceptance gate. Self-contained reproduction
commands are in the [README](README.md).

[lean-corpus-captures.json](evidence/lean-corpus-captures.json) preserves original
process descriptions and stdout/stderr bytes for every final corpus phase,
including actual type/axiom, definition-body and replay messages and negative
Lean diagnostics. Capture descriptors were checked against their actual bytes
before publication. Compiled products and duplicate input trees are omitted;
this is explicitly a reported-evidence wrapper, not a complete inspectable
receipt directory. It cannot grant a fresh Lean pass.

The positive fixture has five checked targets, two independent definition-body
checks and a local same-kernel replay. `identity` retains the premise `n = 2`;
`conditional` is `False → False`. Negative `definition-substitution` and
`transitive-drift` pass the type gate before body rejection. `skip-kernel` passes
compilation/type/axiom phases before replay rejects the invalid proof body.
`sorry` and the custom axiom are explicitly labeled regression inputs.

## Baseline validation and pinned environment

[baseline-verification.json](evidence/baseline-verification.json) records ten
default commands and three live workflows, all exit 0 in disposable copies.
Default counts are 157 inherited checks (including labeled mocks), 8 process,
69 actual Node/filesystem, 4 interruption, 29 ZIP and 16 packaging tests. Source
manifest validation checked 89 public files. Generic source/schema acceptance
still reports zero Lean passes.

Actual pinned baseline Lean testing separately passed 31 live adversarial cases,
three actual Lean OS interruptions, and the full tangent plan: 70 phases,
37 targets, four definition bodies and 59 local replay declarations. The
`PiDiophantine` hypothesis remains unproved. Clean dependency sources and the
official external precompiled cache were used; no full dependency rebuild was
performed. General and tangent saved receipts pass the stricter inspector as
integrity only (172 and 208 artifacts respectively).

The official compiler archive and selected release members were independently
verified. The initial cache setup failed because a shallow ProofWidgets checkout
lacked its release tag; the exact official tag was fetched and checked against
the already pinned commit, then cache retrieval succeeded. Pins were preserved.
Earlier intentional corpus-construction/path-support failures remain under
`evidence/iterations/` as superseded observations, not final acceptance.

## Hypotheses and deferred obligations

No numerical check or source inspection substitutes for Lean acceptance. These
results do not prove a new research theorem or novelty. Same-kernel replay is
not an independent kernel. Fixture core OLeans and baseline dependency OLeans
remain trusted. Full cache-byte closure, dependency rebuild, arbitrary import
closure discovery, polymorphic target support, hostile-workspace isolation,
authenticated historical receipts and native Mac/MRS validation are deferred.

No publication blocker remains for this scoped companion under those limits.
Main research integration and shared publication manifests are deliberately left
to the user's final integration task.
