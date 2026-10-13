# Independent formal-model and proof review

> Publication copy: this dated text describes the original source snapshot and observed runs. Environment locators and workflow wording are normalized; original capture descriptors retain their historical byte bindings. See the [publication notice](../PUBLICATION-NOTICE.md) for original/current hashes and trust scope.

Reviewer: delegated agent `independent-automated-reviewer`, separate from the agent authoring
`LPCertificates/Core.lean`, `Rational.lean` and `Examples.lean`.
Review date: 2026-10-13 UTC. This is independent human-readable reasoning and a
separately authored expected-value harness, not an independent kernel checker.

## Model and hypotheses

The model is maximization with free variables. An input bound such as `x ≥ 0`
must be supplied as a row; there is no implicit variable sign constraint. Every
inequality is represented as `Aᵢ x ≤ bᵢ`; equalities remain `Eⱼ x = fⱼ`.
There are no slack or artificial variables, affine objective constants, strict
inequality rows, or optimization algorithms in this formal model.

`Problem α n m k` has exactly `n` coordinates, `m` inequality rows and `k`
equality rows. The soundness theorems do not assume full rank, independence,
strict feasibility, a vertex optimum, nondegeneracy, or nonempty index sets.
Core results use an ordered field; the executable acceptance tests use `ℚ`,
and the three bridge theorems conclude facts about `ℝ`.

The complete hypotheses of the accepted forms are:

- Optimal: a feasible rational point `x`, nonnegative inequality multipliers
  `w`, unrestricted equality multipliers `v`, coordinatewise identity
  `wᵀA + vᵀE = c`, and exact equality `wᵀb + vᵀf = cᵀx`.
- Infeasible: `w ≥ 0`, `wᵀA + vᵀE = 0`, and the strict contradiction
  `wᵀb + vᵀf < 0`. There is no primal-point hypothesis.
- Unbounded: a feasible rational base point `x`, a rational direction `d`
  satisfying `Ad ≤ 0`, `Ed = 0`, and the strict gain `cᵀd > 0`.

Each Boolean is `decide` of exactly its stated finite rational predicate.
`scripts/Expected.lean` compares all three bodies to separately written explicit
finite arithmetic formulas, and also checks the bodies of `realVector` and
`realProblem`. This anchors the semantics rather than merely checking the names
of predicates used by the soundness theorems.

## Proof assessment

The central bound is obtained by multiplying each inequality by `wᵢ ≥ 0`,
adding them, and substituting each equality after multiplying it by arbitrary
`vⱼ`. Nonnegativity is required only for inequality multipliers. This proves
weak duality for supplied multipliers; no converse or existence theorem is used.

For optimality, the exact bound attained at `x` bounds every feasible point.
For infeasibility, the zero coordinate combination would give `0 ≤ wᵀb +
vᵀf`, contradicting its strict negativity. For unboundedness, `x + t d`
is feasible for every `t ≥ 0`, and has objective `cᵀx + t cᵀd`. The proof
constructs a suitable real `t` for every real bound `B`; it does not merely
show a numerical trend or a sequence of rational sample points.

The casts preserve all finite sums, products, equalities and order relations.
Crucially, the three bridge conclusions quantify over *all real points*:
accepted optimality bounds every real feasible point; accepted infeasibility
rules out every real feasible point; accepted unboundedness exceeds every real
bound at some real feasible point. None is limited to rational candidate points.

The expected whole-type gates explicitly spell out those real inequalities,
equalities and objectives as finite sums, rather than deriving the expected
types from the declarations under test. Dimensions are universally quantified;
there is no hidden specialization to a checked example.

`duality_gap` and `complementary_slackness` assume a feasible primal point and
an already valid dual certificate. The gap is the sum of nonnegative terms
`wᵢ(bᵢ − Aᵢx)`, so zero gap is equivalent to each product being zero. This is
a conditional characterization, not a proof that optimal multipliers exist.
Inactive rows have zero multipliers; a zero multiplier need not imply an
inactive row. Equality multipliers need no complementary-slackness product.

Empty finite sums make the same proofs valid when any of `n`, `m`, or `k`
is zero. In particular, a zero-variable unbounded certificate cannot pass:
its objective-direction sum is zero and cannot have strictly positive gain.
Lower-dimensional affine feasible sets are handled directly through equalities.
Redundant rows do not affect the derivation and can yield distinct valid
multiplier vectors. No uniqueness, duality completeness, certificate finder,
or algorithmic completeness is asserted.

## Signs, scaling and normalization

For a mixed-direction input, a `≥` row must be negated together with its
right-hand side before applying the formal model. Its multiplier is nonnegative
in that normalized representation. A minimization objective must be negated;
optimality then supplies a lower bound for the original objective, and the
unbounded form means unbounded below. Equality multipliers can have either sign.

Positive rescaling of an inequality row preserves its feasible set and requires
inverse rescaling of the corresponding multiplier to preserve the same linear
combination. Equality rows permit nonzero rescaling, including a negative one,
with the same inverse-multiplier rule. Negative rescaling of an inequality
requires reversing its sense before returning to normalized `≤` form.

Positive rescaling of an infeasibility witness preserves its zero combination
and strict negative bound. Positive rescaling of an unbounded direction preserves
the certificate. Scaling all optimal multipliers while holding the objective
fixed generally breaks the identity `wᵀA + vᵀE = c`. These algebraic observations
are explanatory notes, not additional claimed Lean scaling theorems. They imply
no canonical, uniquely optimal, or algorithmically preferred normalization.

## Executed evidence

The published helper is `../math-evidence/lean/EvidenceHarness.lean`, used
unchanged. SHA-256:
`bb71282fcb088498a9c40b0460694f1663e8f3a145fc15469050b8ade2f390dc`.

Pinned executable:
`${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lake`.
Toolchain declaration is `leanprover/lean4:v4.24.0`; mathlib revision is
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.

Reviewed source snapshot hashes, obtained by
`sha256sum LPCertificates/Core.lean LPCertificates/Rational.lean LPCertificates/Examples.lean scripts/Expected.lean`:

```text
5c9755bfdc0b11dcd680a2bfd42da61c5a73f2107cb8bb564be83821af2fb59a  LPCertificates/Core.lean
be5b7bf5c286303fef192404ddb6d2e07f8c3c7a5b794548740382b0722f5f94  LPCertificates/Rational.lean
159433f1444e5fcf641028091bb926cb3282b0bc275cca09069ea5231f499f94  LPCertificates/Examples.lean
f1c56809c8836b57546e5b958467aa75fb02c93cb4a2a6c3c26b67118fe913db  scripts/Expected.lean
```

The hash command exited `0`. These identify reviewed source files; the earlier
compiled umbrella snapshot described below preceded the two example changes.

A preliminary harness run, while the umbrella module was still building, used
a temporary copy of `scripts/Expected.lean` with its sole umbrella import changed
to `import LPCertificates.Rational`:

```text
lake env lean ${TEMP_ARTIFACT}
exit status: 0
definition-body gates: 5 passed
closed whole-type gates: 3 passed
same-kernel local closure replay: 67 declarations retained
```

The full umbrella harness also ran successfully:

```text
lake env lean scripts/Expected.lean
exit status: 0
definition-body gates: 5 passed
closed whole-type gates: 3 passed
same-kernel local closure replay: 108 declarations retained
```

This run used the then-existing compiled library, before the final example
alignment/rebuild. It establishes the unchanged core/rational gates but is not
the final fresh-source verification receipt. The verification runner
rebuilds the project and repeats this harness for the final sources.

The reviewer then copied the final project configuration, all four project Lean
modules, and `scripts/Expected.lean` into the initially empty directory
`${TEMP_ARTIFACT}`. Its `.lake/packages` symlink pointed to
the existing pinned dependency cache at
`${PINNED_REPOSITORY}/tangent-limit/.lake/packages`; no project build
artifacts were copied. From that isolated directory the reviewer executed:

```text
${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lake build
exit status: 0
Built LPCertificates.Core, LPCertificates.Rational, LPCertificates.Examples and LPCertificates
Build completed successfully (7355 jobs).

${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lake env lean --root=${PROJECT_REPOSITORY}/math-evidence/lean ${PROJECT_REPOSITORY}/math-evidence/lean/EvidenceHarness.lean -o .lake/build/lib/lean/EvidenceHarness.olean
exit status: 0
stdout/stderr: empty

${PINNED_REPOSITORY}/tangent-limit/.cache/onboarding/lean-dist/lean-4.24.0-linux/bin/lake env lean scripts/Expected.lean > ${TEMP_ARTIFACT}/expected.stdout.log 2> ${TEMP_ARTIFACT}/expected.stderr.log
exit status: 0
definition-body gates: 5 passed
closed whole-type gates: 3 passed
same-kernel local closure replay: 111 declarations retained
stderr bytes: 0
```

The first command rebuilt the four local modules while trusting the shared
pinned dependency cache; the job count does not claim that all mathlib modules
were freshly compiled. This isolated run verifies the final example changes as
well as the core/rational modules, and uses the unchanged published helper.
Inspection of the pinned Lean source `Lean/Elab/Tactic/ElabTerm.lean`,
`evalDecideCore`/`doKernel`, confirms that `decide +kernel` constructs
`mkDecideProof` and submits it through the synchronous kernel-checked
`mkAuxLemma` path. The example acceptance/rejection facts use this kernel
reduction mode.

The parent final run also has a `passed` receipt at
[`run-20261013T015800Z/receipt.json`](run-20261013T015800Z/receipt.json), with
start `2026-10-13T01:57:16.146283+00:00` and end
`2026-10-13T01:58:56.865558+00:00`. The reviewer read that receipt: all 9 recorded
commands exited `0`, with fresh local compilation, 53 Python tests, 64 named
declaration axiom audits, the same 5 body/3 type gates, and 111 replayed
declarations. A separate reviewer command compared the four isolated Lean/harness
file hashes with both the current originals and receipt `source_sha256` entries;
all four matched the reviewed hashes above. The unchanged helper hash matched
the receipt too. This receipt supplies the larger toolchain/provenance audit;
the isolated reviewer run does not claim to repeat that entire audit.

The four requested axiom prints (three soundness bridges and complementary
slackness) reported exactly `[propext, Classical.choice, Quot.sound]`. The helper
also rejects any other axiom in the checked target closure. No unapproved target
axiom or failed proof gate was found.

## Independent fixture transcription review

After the initial `freeRay` mismatch was reported and corrected by the author,
the following accepted fixture data match their named Lean models and supplied
witnesses, after normalizing `≥` rows and minimization objectives:

| JSON fixture | Lean model | Independently computed decisive quantity |
| --- | --- | --- |
| `optimal_mixed_redundant.json` | `mixedRedundant` | Combined objective `(3,2)`, bound and attained maximum `10` |
| `optimal_min_fraction_equality.json` | `singletonMin` | Normalized objective `−3/2`, equality multiplier `−1/2`, normalized value `−1/2` |
| `infeasible_mixed.json` | `contradiction` | Zero coordinate combination, bound `−1` |
| `infeasible_equalities.json` | `equalityContradiction` | `2(1,1) − (2,2) = 0`, bound `−1` |
| `unbounded_min_lower_dimensional.json` | `lineRayMin` | `Ad = (−1,−2)`, `Ed = 0`, normalized objective gain `1` |
| `optimal_zero_variables.json` | `zeroVariableFeasible` | Empty objective and bound both `0`; negative equality multiplier permitted |
| `infeasible_zero_variables.json` | `zeroVariableInfeasible` | Empty coordinate combination, bound `−1` |
| `unbounded_max_no_rows.json` | `freeRay` | Empty row tests, objective gain `(1/2)·2 = 1` |
| `optimal_constant_no_rows.json` | `constantNoRows` | No rows and zero objective; candidate `(7,−2/3)` and bound both have value `0` |

For `mixedRedundant`, a second Lean certificate has weights `(5/2,0,0,0)`
instead of `(1,3/4,0,0)`, with the same equality multiplier `1/2`. Both combine
to `(3,2)` and attain bound `10`. This explicitly demonstrates nonunique
certificate multipliers in the presence of a redundant row.

Lean rejection examples independently cover negative inequality weights,
an infeasible proposed optimum, a zero contradiction bound, a zero-gain ray,
a bad ray base point and a direction violating an equality. Their instance data
are not generally identical to the separate JSON rejection fixtures; no claim
of automatic fixture extraction or one-to-one failure-test transcription is
made. Parser failure fixtures have no corresponding Lean input because the
formal model begins after parsing.

## Trust limits and deferred obligations

The expected-value gates use completed kernel declarations, kernel definitional
equality, and an axiom-closure check. Replay imports `Mathlib` and
`EvidenceHarness`, then checks the entire local declaration closure with the
same Lean kernel. It is stronger than source inspection, but remains dependent
on the pinned Lean kernel, imported library and published helper. It is not
independent-kernel replay, native Mac MRS integration, or a claim that every
phase of a larger evidence-toolkit integration plan was executed.

The Python/JSON interface is outside this formalization. Its exact arithmetic,
schema validation, mixed-direction normalization and mapping into `Problem`
require separate tests and review. Hand-transcribed examples can be checked
against input fixtures, but no parser refinement or extraction theorem connects
the Python implementation to these Lean declarations. Acceptance by the Python
program alone is not Lean acceptance of the corresponding JSON instance.

No proof or review establishes that all optimal, infeasible or unbounded rational
LPs have a certificate in the accepted forms. Proving strong duality, Farkas
converses, rational-witness existence, search termination and completeness is
deferred. A rejected certificate does not determine the LP's true status.

No mathematical or formal-proof blocker was found within the sufficient-certificate
scope. No external service, Library operation, account change, commit, or push
was performed by this reviewer.
