# Migration from the published v1 toolkit

Keep `math-evidence/` and shared publication manifests intact. Use this directory
as an additional reviewed companion on the assigned branch. The original schema,
fixture plans, historical reports and acceptance statuses retain their meanings.

## Receipt acceptance

Use `node inspect-v1.cjs RUN` when a caller requires a complete reported v1
closure. Exit 0 means stricter reported integrity; exit 2 means missing,
incomplete, malformed, changed or unsupported evidence. Preserve rejected
attempts and their logs. This inspector intentionally rejects failed/incomplete
receipts as *complete* evidence; it does not rewrite or erase them.

Additional requirements include canonical UUID/timestamps, phase chronology,
termination/error/PID/exit consistency, exact environment fields, bounded output
counts, exact artifact descriptors, attempt-marker binding, compiler/runtime
pins, package metadata and stdout bindings, fixed command argv/cwd, every compile
JSON severity/data envelope, empty compiler stderr, full target/body/replay
marker coverage, and unchanged source/work bindings. Artifact metadata is checked
before reading the bounded closure (64 MiB maximum). FIFOs, symlinks and shared
hard links cannot act as evidence files.

The original runner supports origins differing only by a `.git` suffix. This
companion's complete-v1 profile deliberately requires the exact origin string in
the published lock and capture. An otherwise legitimate differently spelled
origin is unsupported here and must receive review rather than automatic repair.
Likewise, unexpected stderr and noncanonical timestamps can cause conservative
rejection. The actual baseline valid/general/tangent receipts pass this profile.

The full expected Lean terms and body harnesses are bound to the original source
pins. The inspector checks marker structure and agreement with captured JSON;
it does not elaborate `observedType` report text or independently verify imported
OLean proof bodies. A completely coherent fabricated historical closure can
still pass reported integrity, with all pass/freshness/authenticity fields false.
No imported command is executed. A fresh runtime call is required for a fresh
observation.

## Source identity

`git diff --exit-code` alone can overlook changed tracked files when the index
marks them `assume-unchanged` or `skip-worktree`. Run `git-source.cjs` using the
independently reviewed exact package commit, before and after the relevant
execution, and compare `sourceClosureSHA256`. The checker disables replacement
objects; a `git replace` ref cannot substitute another tree for the pinned commit.
It does not change index flags or repository configuration.

This check compares tracked byte identity and rejects untracked Lean overlays
outside `.git`, `.lake`, `.cache`, `.elan`. Cache directories are deliberately
excluded and remain trusted. It does not discover arbitrary executable Lean
imports, authenticate a remote origin, pin cache artifacts or rebuild packages.
Do not upgrade a source-check result to formal proof acceptance. A caller needing
those broader guarantees must implement separately reviewed closure discovery,
cache pinning/source rebuild and environment isolation.

## Fixture protocol

`fixed-fixture-receipt/v1` is a companion-owned fixed-test schema, not a replacement
for `math-live-receipt/v1`, `math-exchange/v1` or a native MRS format. Only reviewed
labels execute. Expected types and definition bodies come from fixed files;
receipt fields cannot supply a plan, command or Lean expression.

The standalone core corpus is useful for migration regression. Its positive
receipt does not certify the tangent project or any other research project.
General polymorphic targets, arbitrary imported code, independent kernel
checking, authenticated receipts and native Mac/MRS adaptation remain deferred.
