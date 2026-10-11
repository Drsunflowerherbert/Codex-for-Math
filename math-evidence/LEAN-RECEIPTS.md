# Live Lean evidence protocol

math-live-receipt/v1 is this companion's protocol, not a native MRS receipt.
math-exchange/v1 continues to accept only not_run and historical_report. The only
positive local result comes directly from a new execution of live.cjs with a fixed,
reviewed plan and all required phases complete. inspect-receipt never grants one.

## Phases and their meanings

1. Source preflight: acceptTangent checks 26 published files against independent
   fixed pins; selected fixtures, helper, expected harnesses and runner code are
   copied and hashed. Changed source plus coordinated catalog edits still fail.
2. Compiler preflight: the selected Linux loader and four Lean runtime libraries
   match fixed release-member bytes before any Lean invocation. Version and commit
   must match 4.24.0 / 797c613eb9b6d4ec95db23e3e00af9ac6657f24b. The member pins
   were independently compared with the existing archive whose SHA is fixed by
   the published tangent installer. Host runtime and dependency oleans remain
   explicit trusted inputs; this is not a full toolchain rebuild/signature audit.
3. Dependency preflight: actual Git HEAD/origin and clean tracked source of all
   nine packages match the fixed Lake manifest. Trusted existing cache paths are
   captured. No setup/update command or archive-embedded command runs.
4. Fresh compilation: fixed copied modules compile to a new private cache. Stale
   project oleans are excluded. stdout and stderr are separate bounded artifacts.
5. Expected type and axiom audit: the separately reviewed harness compares the
   entire closed declaration type, including implicit forall binders, with its
   expected type using elaborator and kernel definitional equality. No target
   specialization is allowed. All actual transitive axioms must be among propext,
   Classical.choice and Quot.sound; sorryAx and custom axioms fail. The helper
   forces completion of checked kernel work. Polymorphic targets are unsupported.
6. Definition-body matching: the tangent's four definitions match trusted closed
   expected bodies using kernel definitional equality. Matching PiDiophantine's
   predicate definition is not proving that predicate.
7. Local kernel replay: Lean.Replay rechecks new local declaration bodies and
   auxiliaries against the imported [Mathlib,EvidenceHarness] baseline. This uses
   the same compiler/kernel, not an independent checker. It excludes dependency
   proof bodies already in the baseline. The actual tangent closure has59 entries.
8. Postflight: original, copied and working source, runner code, compiler/runtime,
   package identity, products and captured evidence must remain unchanged. Every
   required phase and marker must be present; aborted attempts cannot pass.

## Process and receipt rules

Each execution owns a new directory; no old attempt is resumed or overwritten.
The initial attempt marker records in_progress and locallyObservedLeanPass:false.
Process receipts record exact argv/cwd, relevant environment, timestamps, PID/group,
termination kind, exit code/signal, and separate output byte counts/SHA-256.
Commands use shell:false and fixed trusted arguments. Abort, timeout and output
limit cancel the Unix process group with TERM followed by KILL, including surviving
descendants. Captured output is capped at4MiB per phase. SIGTERM/SIGINT leave failed
receipts; a hard-killed CLI leaves an incomplete marker with no final receipt.
SIGKILL cannot run cleanup code; the OS test harness separately cleaned its observed
remaining child group. None of these interrupted cases is a pass.

The stored reportedOutcome is a report of what that execution observed. Hashes do
not authenticate historical process events. Inspection checks structure, statuses,
artifact coverage/hashes, preserved fixed sources, fixed build-input mappings,
compiler member pins and the recorded Lean message markers. Even a wholly coherent
fabrication would establish only reported internal consistency, never a new live
pass. Missing, tampered or unsupported evidence/statuses are rejected.

A live local pass remains conditional on the inspected trusted workspace, fixed
runner/helper and pinned cached dependency environment. No general sandbox for
arbitrary imported Lean elaborator code is supplied. A malicious host or altered
trusted dependency cache is outside the asserted guarantee. Full dependency source
rebuild, independent kernel implementation/replay and native Mac/MRS tests remain
not_performed or unavailable_unvalidated.

## Historical and current evidence

The archived full tangent run is summarized under a distinct derivative schema in
`verification/HISTORICAL-EVIDENCE.json`. Its raw closure is not distributed here,
so this summary cannot be consumed as a complete live receipt. The independent
review inspected the original 208-artifact closure privately. Fresh public-package
checks are separate in `verification/PUBLIC-VERIFICATION.json`; only actual fresh
executions can provide newly observed local results. Historical sample logs remain
unchanged and grant no new pass.
