> Historical source review: mathematical statements and verdicts are retained. Quoted hashes identify the original supplied files, which may differ from privacy-normalized public receipts. Original/public hashes are recorded in `publication/SOURCE-MAP.json`; fresh publication checks are separate.

# Independent final audit review

The frozen delivered project passes its default build, corrected public
declaration audit, and complete project-origin environment supplement.
This reviewer did not modify the mathematical proofs or the public checker.
The reviewer inspected the recovery boundary before execution, authored the
bounded supplemental inventory, and independently reconciled the completed
reports with the actual files and command receipts.

The mathematical statement and assumption review is separate in
[final-statement-review.md](final-statement-review.md). The acceptance here
concerns the declarations actually present in the delivered project; it does
not label all clauses of the 21 supplied records completed. In particular,
the exact tail range and all deferred source clauses remain as stated in
[final-proof-scope.md](final-proof-scope.md).

## Completed command evidence

| Check | Scope and result | Actual exits |
|---|---|---|
| Default build | `bash scripts/with-lean.sh lake build`; all 16 component modules and the umbrella target | 0; [receipt](../evidence/supplied/logs/final-default-build.json), [output](../evidence/supplied/logs/final-default-build.log) |
| Public audit | 17 module files, 513 named public declarations: 429 theorems, 82 definitions, one abbreviation, one structure | Build 0; axiom, type, and definition queries each 0; wrapper 0; [report](../evidence/supplied/logs/certificates-lean-final-audit.json), [receipt](../evidence/supplied/logs/final-public-audit.json) |
| Complete environment supplement | 835 constants selected by their originating imported project module; all exact kernel types and direct kernel dependencies recorded | Lean query 0; wrapper 0 at 2026-10-11 04:51:45 UTC, 136.11 seconds; [report](../evidence/supplied/logs/full-environment-audit.json), [receipt](../evidence/supplied/logs/final-environment-audit.json) |

The public audit records `#check @name` with full names and universe parameters
for every named public declaration, plus `#print` bodies for all 84 other
source declarations. Its 429 transitive theorem axiom results match the
expected names exactly. Independently recomputed totals agree with the report;
426 public theorems use all three standard logical axioms and three use only
`propext`.

The supplement uses `Environment.constants`, `getModuleIdxFor?`, and
`allImportedModuleNames`, selecting by originating module rather than a
declaration-name prefix. It includes private proofs, generated declarations,
instances, constructors, and recursors omitted by the source-syntax inventory.
All 513 public names occur in this inventory. Its 835 constants comprise
729 theorem constants, 103 definitions, one inductive, one constructor, and
one recursor. Every record has a nonempty readable full type and the complete
kernel `Expr` representation, with universe parameters.

Exactly 429 axiom results are reused from the **passed corrected public
audit**, after checking its exact theorem-name inventory and reconciling
source, configuration, and checker hashes. That report is itself frozen
through the supplemental run. The remaining 406 constants have fresh ordinary
`#print axioms` results. Every record identifies its evidence source. The
combined 835-name axiom inventory is exact and unique; no result from a failed
run is reused as a pass. This is not a claim that the supplement freshly
queried all 835 names.

All dependency sets are contained in `{propext, Classical.choice, Quot.sound}`.
Independently counted sets are: all three, 639 constants; `propext` only, 109;
`propext` and `Quot.sound`, 71; no axioms, 16. There is no project-origin axiom
declaration, additional mathematical axiom, or `sorryAx` dependency. The masked
proof-source scan has no `sorry`, `admit`, `axiom`, `unsafe`, `native_decide`,
or `implemented_by` tokens. The supplemental scan also has no source `partial`
or `partial_fixpoint` tokens.

## Compiler-generated runtime helpers

Five inventoried definitions have `partial=true` and `unsafe=false`:

| Name | Type | Safe source parent |
|---|---|---|
| `MixedMoments.central._unsafe_rec` | `Nat → Rat` | `MixedMoments.central` |
| `MixedMoments.hStar._unsafe_rec` | `Nat → Rat` | `MixedMoments.hStar` |
| `MixedMoments.kminus._unsafe_rec` | `Nat → Rat` | `MixedMoments.kminus` |
| `MixedMoments.kplus._unsafe_rec` | `Nat → Rat` | `MixedMoments.kplus` |
| `MixedMoments.moment._unsafe_rec` | `Nat → Rat` | `MixedMoments.moment` |

All originate in `MixedMoments.Rational`. Lean's pinned compiler source,
`Lean/Elab/PreDefinition/Basic.lean:292-308`, implements
`addAndCompilePartialRec` by generating `Compiler.mkUnsafeRecName` copies with
`DefinitionSafety.partial`. The report records that source's hash and excerpt.
Each exact helper name is recognized by this compiler function and paired
with its distinct safe, nonpartial source definition. Only these five names
are classified; the report does not claim that all constants are nonpartial.

The fresh query inspected type and value constant references for every
project declaration, including private/generated theorem proof terms and
opaque values; inductive constructor references are included as well.
Independent inspection confirms that **none of the other 830 constants
references any of these five runtime helpers**. Thus the helpers are recorded
compiler execution artifacts, absent from the certified project kernel
dependencies. They remain in the full type and transitive axiom inventory.
The axiom allowlist and prohibition on user source shortcuts were not relaxed.

## Stability, pins, and retained failures

Every current proof-source/configuration/public-checker hash matches the
successful public report and the canonical
[frozen inputs](../evidence/supplied/logs/final-frozen-inputs.json).
Every supplemental input hash matches the current file and its after-run
snapshot. All module inventories are stable and match the 16 components plus
the declaration-free umbrella. Helper revisions and their unchanged proof
hashes are recorded separately in
[supplemental-frozen-inputs.json](../evidence/supplied/logs/supplemental-frozen-inputs.json).

The reviewer independently reran the compiler version command, recomputed its
binary hash, and checked all nine dependency Git revisions and clean working
trees against the manifest. All commands exited zero and all recorded hashes
and revisions matched [final-environment.json](../evidence/supplied/logs/final-environment.json).
Lean is 4.24.0, commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`;
mathlib is `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.

The recovery's interrupted smoke audit remains failed, and its earlier
111-theorem Rational/Cancellation audit retains that subset scope. The first
final public audit also remains failed in
[certificates-lean-full-audit-first-failed.json](../evidence/supplied/logs/certificates-lean-full-audit-first-failed.json):
the obsolete `pp.width` option caused type/definition exits one, and the old
parser missed three wrapped axiom lists. The corrected public checker was
freshly executed successfully; the failed run was not reclassified.

The first supplement failed before inventory because its command monad and
JSON inference needed correction. The second Lean query exited zero with a
complete inventory, but its Python acceptance returned one because the
blanket nonpartial guard rejected the five compiler runtime helpers. Both
failed reports, command receipts, and outputs remain under distinct
`first-failed` and `second-failed` filenames. The final runtime classification
and dependency inspection come from a **fresh complete successful run**.

Finite rational checks, the 77 compiled rational examples, source provenance,
and the coverage table are separate supporting evidence. Compilation and axiom
inspection verify the stated Lean types; they do not infer arithmetic
independence, Catalan irrationality, or real nonmembership from a designated
formal zeta coefficient. No audit blocker remains for the frozen scoped
deliverable.

## Publication dependency-scan precision

The preserved complete-environment query scans all kernel types and all
definition/theorem/opaque values, plus constructor references. It does not
traverse recursor reduction-rule right-hand sides. The separate publication
query `scripts/inductive_kernel_metadata.lean` checks those rules and the
inductive/constructor metadata without changing the preserved proof or query
sources. Its actual exit is zero: exactly three project-origin records and
one recursor rule exclude all five disclosed runtime helpers. Current receipt
and exact query hashes are recorded separately under `evidence/publication/`.
Historical helper-dependency statements should be read with this original
scan boundary; the combined publication checks supply the additional coverage.
