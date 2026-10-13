# Independent review of mixed-row input normalization and bridge

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](../PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

Reviewer: independent formal reviewer, separate from the author of
`LPCertificates/Input.lean` and `bridge.py`. This follow-up preserves the first
published LP toolkit commit `44329696`; this review concerns its new input layer.

Review status: the generic input model and soundness gates passed an independent
fresh build. Three independently emitted original-JSON instances also passed
kernel acceptance and their soundness gates after the renderer correction.
The full nine-case portable driver batches are separate verification work;
this report does not substitute an unfinished reviewer batch for those receipts.

## Required mathematical semantics

The raw problem uses rational data, free real variables, three row senses
`≤`, `≥`, `=`, and a maximization or minimization objective. A `≥` row becomes
`−aᵢ x ≤ −bᵢ`; negating only the coefficient vector or only the right-hand side
would change the problem. A minimization objective `cᵀx` becomes maximization of
`−cᵀx`.

The implemented normalization retains the `n` original coordinates. Each original
row supplies one position in each of two masked row families. An equality row
is replaced by the zero tautology in the inequality family; a non-equality row
is replaced by the zero equality in the equality family. These are bookkeeping
rows, not added decision variables. Their zero multipliers preserve the intended
single raw-row multiplier vector: inequality weights must be nonnegative,
while equality weights can have either sign.

The original-objective conclusions proved from Boolean acceptance are:

- Optimal: the proposed point satisfies every original real row, and every
  original feasible real point has objective at most its value for maximization
  or at least its value for minimization.
- Infeasible: no real point satisfies every original row.
- Unbounded: for every real bound, an original feasible real point exceeds that
  bound for maximization or falls below it for minimization. A feasible supplied
  base and a strictly improving homogeneous direction are essential.

The independently written `scripts/ExpectedInput.lean` anchors complete closed
types and normalizer/checker bodies, and does not recover expected types from
theorem records. It checks nine definitions: `normalizeInput`, the two multiplier
masks, `InputFeasible`, `ObjectiveBound`, `ObjectiveBeyond`, and the three input
checker wrappers. Its three expected theorem types spell out the original real
row inequalities/equalities and objective sums, universally over dimensions and
all real comparison points or bounds.
The existing sufficient-certificate results require no row independence,
nondegeneracy, strict feasibility, or positive variable dimension. No converse,
certificate finder, strong duality or completeness claim follows.

`input_feasible_iff` proves feasibility equivalence in both directions.
`input_objective_bound_iff` proves the original-objective ordering for both
objective senses. The minimization unboundedness proof applies normalized
unboundedness to `−B`, obtaining `−cᵀy > −B`, hence `cᵀy < B`. No original
objective sign is silently changed in the conclusions. The five theorem axiom
prints (these two equivalences and three soundness theorems) contain exactly
`propext`, `Classical.choice`, and `Quot.sound`.

## Bridge boundary review

The inspected emitter interpolates canonical integer numerator/denominator data,
dimension counts derived from validated vector lengths, and fixed trusted
constructor/name strings. Row senses and objective senses select fixed enum
constructors. Input rational text is parsed to `Fraction` and printed as integer
literals; filenames do not become theorem names or executable code. Original
coefficients, right-hand sides, row senses, objective sense, point/direction and
one multiplier per original row are supplied to `InputProblem`; normalization is
computed in Lean. Negative equality multipliers survive the translation.

The runner compiles its own generated numeric-data instance using fixed argument
arrays with `shell=False` and a restricted environment. It checks pinned compiler
members, source/helper identity and dependency identities, and uses an initially
empty task-library cache. Its checked status requires a successful compiler exit,
no diagnostics, whole-type/body/axiom evidence and replay evidence. Time, output
and process limits are explicit. This review does not claim complete operating
system isolation or an independent compiler/kernel implementation.

Package recheck validates member paths, hashes, regular-file/symlink rules, the
original input bytes, regenerated semantic data and regenerated instance source,
and byte identity of the current trusted library/helper sources. It then feeds
only the saved original JSON bytes into a fresh run. Saved Lean source, logs,
receipt commands and status labels are not executed as instructions. Hashes
attest package consistency; they do not authenticate past execution.

An independent pure inspection exercised four original accepted fixtures:
the fraction/minimization optimum, equality-only contradiction, minimization
ray and zero-variable optimum. The semantic tables retained original minimizing
objectives and equality weights `−1/2`, `−1`, and `−7` as appropriate. A rational
input string containing a newline and `axiom injected : False` returned `invalid`
before rendering. This experiment was parsing/emission evidence, not itself
Lean acceptance.

Exact parsing and translation remain an external interface obligation; there is
no parser-refinement theorem. A successful instance proof applies to the exact
numeric `InputProblem` emitted and kernel checked. Agreement between that data
and the original JSON depends on the trusted strict parser and numeric emitter,
supported by separate tests and review.

Executing trusted committed Lean tactics on generated data is ordinary Lean
verification. It is not independent-kernel replay, native Mac MRS integration,
or a proof that every possible JSON document is correctly translated.

## Independent fresh Lean evidence

The reviewer copied project configuration, all five project modules and both
expected-value scripts into the initially empty directory
`${TEMP_ARTIFACT}`. The only cache shared with the original
workspace was the pinned dependency cache. No project OLeans were copied.

The following commands ran from that isolated directory:

```text
${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lake build
exit status: 0
Built Core, Rational, Examples, Input and LPCertificates
Build completed successfully (7356 jobs).
stderr bytes: 0

${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lake env lean --root=${PROJECT_REPOSITORY}/math-evidence/lean ${PROJECT_REPOSITORY}/math-evidence/lean/EvidenceHarness.lean -o .lake/build/lib/lean/EvidenceHarness.olean
exit status: 0
stdout/stderr: empty

${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lake env lean scripts/ExpectedInput.lean
exit status: 0
definition-body gates: 9 passed
whole-type gates: 3 passed
same-kernel local closure replay: 176 declarations retained
stderr bytes: 0

${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lake env lean scripts/Expected.lean
exit status: 0
definition-body gates: 5 passed
whole-type gates: 3 passed
same-kernel local closure replay: 216 declarations retained
stderr bytes: 0
```

Outputs were captured in distinct `build`, `helper`, `input-expected`, and
`baseline-expected` stdout/stderr logs in the isolated directory. The build job
count includes cached dependencies; it does not claim a fresh full mathlib
rebuild. Both replay phases use the unchanged published helper and the same
Lean kernel against imported `Mathlib`/`EvidenceHarness`.

Source hashes were compared between the isolated copy and current originals
after the successful fresh gates; all matched:

```text
4bfbbd5058b142ad21657462963ccf80a6bdd1dbdfc9fa36ae78253ee605eae7  LPCertificates/Input.lean
51592c9b71c70f87eff6f8f541c189a75370a06e6a617bb2c43ea479a1527ad7  scripts/ExpectedInput.lean
2f413af4039969062d39053edb85b06b03ee9c8a7776c5ef0b9c4d2276e4cf78  LPCertificates.lean
```

The preserved Core, Rational, Examples and original Expected script hashes also
matched their previously reviewed source snapshots.

## Draft harness and emitter failures

An initial inline expected-normalizer expression passed elaborator equality but
failed the stricter kernel body check. A draft with explicit case eliminators
also failed definition equality. The final harness declares its independently
written pure expected normalizer before invoking the evidence command, making
generated matcher declarations available to its captured checked environment.
The expected normalizer contains the explicit raw row/objective rules and does
not reference `normalizeInput`. All nine gates then passed, including a fresh
isolated run. Neither the implementation nor the published helper was altered
to make the gate pass. The replay count includes this pure expected definition.

The first original-JSON instance compilation exposed a renderer layout error:
the generated record began `({ a := ...` far to the right on a declaration line,
then placed following fields at column four without commas. Lean rejected the
source with `unexpected identifier; expected '}'`; the dependent acceptance
proof failed, and the expected-type gates rejected parser-recovery `sorryAx`.
The compiler exited `1`, so this was a failed attempt, not a checked certificate.
The failure was reported to the author with its exact generated source/logs,
and the failed snapshot was retained separately under
`failed-emitter-attempt-01` in the isolated directory. Adding commas alone still
failed the record layout and was retained as `corrected-emitter-attempt-02`.
A temporary single-line record passed with no logical-data change. The author
then placed the opening brace on a preceding line and consistently aligned all
fields; the actual corrected renderer is used by the successful checks below.

## Actual original-instance checks after correction

The reviewer copied the corrected trusted renderer and strict checker into a
separate `corrected-emitter-attempt-03`, parsed the nine original accepted JSON
fixtures and emitted nine numeric-only `InputProblem` sources. Normalization was
computed in Lean rather than exported as Python-normalized constraints.

The following three sources independently compiled successfully against the
fresh isolated task modules. Commands ran from
`${TEMP_ARTIFACT}`:

```text
${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lake env lean corrected-emitter-attempt-03/instance-infeasible_equalities.lean
${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lake env lean corrected-emitter-attempt-03/instance-infeasible_mixed.lean
${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lake env lean corrected-emitter-attempt-03/instance-infeasible_zero_variables.lean
```

Every command exited `0`; each generated acceptance theorem uses
`by decide +kernel`. Each run passed one problem-definition-body gate, two
complete type/axiom gates (`CheckedInput.accepted` and `CheckedInput.sound`),
and replay of 177 local declarations. All three had empty stderr and permitted
axiom closures only. The first two successes are recorded in attempt03
`instance-results.json`; the final sequential zero-variable retry is preserved
as `zero-variable-retry.stdout.log` and `.stderr.log`.

The first two commands ran in a two-worker reviewer batch. A subsequent leaf
returned nonzero with empty stdout/stderr, and the Python batch driver exited
`1`; its initial driver did not retain that leaf's exact subprocess return code,
so no exact leaf signal is asserted here. The parent identified cgroup OOM kills
during simultaneous verification jobs in the 16 GiB environment. The isolated
zero-variable retry then exited `0` with all gates. Further heavy reviewer jobs
were paused at the parent's instruction so complete driver batches could run
serially. This runtime-pressure interruption is separate from a mathematical
proof error, and the uncompleted parallel reviewer batch is not counted as a
nine-instance success.

The current corrected renderer was compared byte-for-byte with all nine emitted
source snapshots after these checks; all nine matched. The parser/emitter
snapshot identities are:

```text
c0fe2cbfc7511309f91524e86ed8e5342f0d891c090a343a0a1ee06736774dd2  bridge.py
bb55c5f57a91d9c8c225ab3dc219a718a383e13249314fff29b5a1ad33e290fb  verifier.py
```

No mathematical or generic formal-proof gap was found in the mixed-row or
original-objective layer. Parser refinement, certificate finding/completeness
and an independent kernel remain unproved. The reviewer made no commit or push,
changed no accounts/credentials and used no Library operation.
