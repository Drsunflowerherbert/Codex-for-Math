# Mathematics evidence toolkit

A source-only Node/Python toolkit for mathematical statements, explicit assumptions,
declared dependencies, pinned sources, ordinary reviews, finite experiments and
separate live Lean evidence. Imported records and saved receipts grant no Lean pass.

Read [RUNBOOK.md](RUNBOOK.md) for reproduction, [SCHEMA.md](SCHEMA.md) for the
portable record format, [LEAN-RECEIPTS.md](LEAN-RECEIPTS.md) for the live gate, and
[VERIFICATION.md](VERIFICATION.md) for the evidence and trust limits.
No npm or Python package installation is required for the default suites.

```sh
node verify-public-sources.cjs
node run-tests.cjs
node cli.cjs accept-tangent samples/tangent.bundle.json
node cli.cjs validate samples/catalog.json samples/source-tree
```

The pinned sample is the original public tangent project at
[`d00a89dd9ce6c8ef782234d28c93e69cb712c947`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/d00a89dd9ce6c8ef782234d28c93e69cb712c947/tangent-limit).
Its 26 selected files are unchanged. The 37 declaration records comprise 33
theorems, three definitions and the assumption proposition `PiDiophantine`;
twelve theorem headers explicitly require that premise. Matching its definition
body does not prove the premise. The declared dependency graph omits mathlib
internals and does not establish completeness. Historical review metadata stays
`review_reported`, including the disclosed proof contribution by that reviewer.

The live runner compiles only inspected fixed plans. A fresh success requires
source/compiler/package identity, complete expected types, allowed axioms,
definition bodies where applicable, local kernel replay and unchanged evidence.
A stored receipt inspection checks integrity and internal consistency; it always
reports `leanPass: false` and `locallyObservedLeanPass: false`.

## Trust limits

Actual I/O/live testing is on Linux, Node 24 and Python 3.12, with Lean 4.24.0 and
mathlib `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The host runtime and clean pinned
dependency OLeans are trusted; dependencies are not rebuilt from source. Local
replay uses the same Lean kernel against an imported dependency baseline. The
full expected-type/body gate conservatively supports monomorphic declarations.
There is no independent verifier or OS sandbox for hostile Lean or concurrent
attackers. Native Mac and installed MRS integration are unvalidated. Hashes
establish byte consistency, not historical event authenticity or mathematical
novelty. No overall license is assigned to new toolkit code.

## Optional ordinary corpus intake

`archive-intake.py` safely verifies/extracts independently pinned user-supplied
archives without executing their contents. `corpus.cjs` losslessly wraps the
original supplement's seven studies and 81 core records, preserving all native
status fields. Five background nodes and two separately unreviewed optional
bounds remain separate. Schema/graph/hash consistency proves no mathematical
truth or Lean pass. Exact original fixture archives, compiled products and raw
historical receipt trees are excluded; public research directories contain
sanitized publication copies and cannot substitute for exact original archives.
See [MRS-ADAPTER.md](MRS-ADAPTER.md) for the unimplemented adapter contract.
