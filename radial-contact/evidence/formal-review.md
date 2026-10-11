# Independent source and statement review

Reviewer: independent automated mathematical reviewer. Date: 2026-10-11 UTC.

## Scope and verification level

This is an independent, read-only review of the mathematical statements and proof structure in `RadialContact/Basic.lean`, `Lipschitz.lean`, `Inverse.lean`, and `Derived.lean`. The reviewer made no changes to those source files and did not start a Lake build. The review began before the implementation environment's source build completed and was finalized after independently inspecting the successful milestone logs, `final-build.log`, `validation.json`, and the complete `theorems-and-axioms.log`. Final compilation and transitive axiom verification are successful, as detailed below.

The identified Library archive could not be transferred after the two supported attempts recorded in `source-provenance.json`. This reviewer did not inspect or hash that archive. The review relies on the user's specification, locally available Lean source, pinned mathlib source, and `ordinary-review.md`; it makes no assertion about either requested record inside the unavailable ZIP.

The pinned versions read locally are Lean `leanprover/lean4:v4.24.0` and mathlib commit `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, the latter confirmed by `git -C .lake/packages/mathlib rev-parse HEAD`. The reviewed source snapshot has these SHA256 values:

| File | SHA256 |
| --- | --- |
| `RadialContact/Basic.lean` | `0a25656d386d2d73735b771f193e51a946dd6d596d37502619c7d6a0fd2f20bf` |
| `RadialContact/Lipschitz.lean` | `5961ea07e60e28e31615e2bca4c394b7d64debabeae072674ec66aa301101b00` |
| `RadialContact/Inverse.lean` | `f54a454b8fca904ad32fa48c49e8adea6ddc83e73e558e341592d1cdf43d7d6e` |
| `RadialContact/Derived.lean` | `2cb1d2f8c854b0ada4f32cb39776d22daef906c5e4a81a6e8011df5d80c80c2d` |

These are the final reviewed source hashes. The reviewer recomputed them and independently checked that all four match the corresponding entries in `validation.json`.

## Statements and domain assumptions

Every module uses an arbitrary type `E` with `[NormedAddCommGroup E] [NormedSpace ℝ E]`. Some norm-only declarations further omit the `NormedSpace` instance. No declaration adds completeness, finite dimension, smoothness, strict convexity, or a nontriviality/nonempty-sphere hypothesis. The unit sphere is the subtype `{v : E // ‖v‖ = 1}` and an interior center is `{c : E // ‖c‖ < 1}`. Inspection of all 47 compiled, fully explicit `#check @...` statements confirms these intended assumptions.

Writing `a = ‖c‖`, `m = 1 - a > 0`, and `M = 1 + a`, the principal exports have the following mathematical content:

| Export | Reviewed content |
| --- | --- |
| `parameter_comparison` | If `0 ≤ r ≤ s` and both `c + r • v`, `c + s • w` have norm 1, then `(s-r)(1-‖c‖) ≤ rs‖v-w‖`. This intentionally needs neither unit directions nor `‖c‖ < 1`. |
| `parameter_abs_comparison` | For nonnegative contact parameters, `|r-s|(1-‖c‖) ≤ rs‖v-w‖`. |
| `positive_contact_unique` | For an interior center, two positive contacts in the same direction have equal radii, without a unit-direction assumption. |
| `positive_contact_bounds` | For a unit direction and any nonnegative contact radius, `1-‖c‖ ≤ r ≤ 1+‖c‖`. This intentionally does not need an interior-center assumption. |
| `exists_positive_contact`, `existsUnique_positive_contact` | For `‖c‖ < 1` and `‖v‖ = 1`, exactly one positive contact radius exists. |
| `radius`, `radius_pos`, `norm_contact`, `radius_bounds`, `radius_eq_of_contact` | The chosen radius is positive, produces a sphere point, obeys the universal interval, and agrees with any positive contact radius. |
| `radius_dist_le`, `radius_lipschitz` | Radius has Lipschitz constant `M²/m` on the sphere. |
| `contact_dist_le`, `contact_lipschitz` | Contact `v ↦ c + radius(c,v) • v` has Lipschitz constant `2M/m`. |
| `direction`, `radius_direction`, `contact_direction`, `direction_contact` | The inverse is `x ↦ ‖x-c‖⁻¹ • (x-c)`; its contact radius is `‖x-c‖`, and it is inverse to contact on both sides. |
| `sphereHomeomorph` | Contact and direction form a homeomorphism of the unit-sphere subtype. |
| `reciprocal_radius_dist_le` | The reciprocal radius has bound `|1/r(v)-1/r(w)| ≤ ‖v-w‖/m`. |
| `direction_dist_le`, `direction_lipschitz` | The normalized inverse has Lipschitz constant `2/m`. |
| Zero-center exports | Radius is identically 1; contact and direction are identities. The radius is `0`-Lipschitz; contact and direction are isometries. |

Requested specification results appear in `Basic`, `Lipschitz`, and `Inverse`; additional refinements are grouped in `Derived`. The derived file explicitly avoids asserting sharpness, including on an empty sphere. The general constants are valid but loose at zero center; the separate zero-center results correctly improve them.

## Mathematical proof review

**Existence and bounds.** The real-valued function `t ↦ ‖c + t • v‖` is continuous. Its value at 0 is less than 1 and its value at `M` is at least 1 by the reverse triangle inequality. The imported intermediate value theorem is applied on the real interval `[0,M]`, so completeness of `E` is not used. The triangle inequalities give `m ≤ r ≤ M`, making the selected radius strictly positive.

**Comparison and uniqueness.** The module identity

`s • (c + r • v) = r • (c + s • w) + (s-r) • c + (r*s) • (v-w)`

is correct. With `0 ≤ r ≤ s`, taking norms produces the stated comparison. Swapping the ordered pair gives its absolute-value form. Setting `v=w` and using `m>0` forces equal radii. The argument therefore applies to norms with flat faces and needs no strict convexity.

**Quantitative contact estimates.** The comparison gives `|r-s|m ≤ rs‖v-w‖`. Since both radii are at most `M`, division by the positive `m` gives `M²/m`. The contact decomposition

`r • v - s • w = r • (v-w) + (r-s) • w`

is correct and yields `(M + M²/m)‖v-w‖`. The simplification to `2M/m` is valid because `m+M=2`.

**Inverse.** The reverse triangle inequality gives `m ≤ ‖x-c‖`, so every normalization denominator is strictly positive. Scalar cancellation proves `c + ‖x-c‖ • direction(c,x) = x`; radius uniqueness then proves one inverse identity. The other follows from `‖radius(c,v) • v‖ = radius(c,v)` and radius positivity. Continuity of reciprocal norms is invoked only at nonzero denominators.

**Derived estimates.** Dividing the comparison by `rs>0` proves the reciprocal-radius bound. For `nₓ=‖x-c‖` and `nᵧ=‖y-c‖`, the proof uses

`nₓ • (direction(c,x)-direction(c,y)) = (x-y) + (nᵧ-nₓ) • direction(c,y)`.

Together with `|nᵧ-nₓ| ≤ ‖x-y‖` and `m ≤ nₓ`, this gives the valid inverse bound `2/m` without compactness.

## Empty sphere and zero center

The definitions take an actual sphere element as an argument. `Classical.choose` selects a radius only from the existence proof attached to that input; it never selects a unit vector or requests a `Nonempty (UnitSphere E)` instance. In a subsingleton normed space, `unitSphere_isEmpty_of_subsingleton` rules out a sphere element by `‖0‖=0≠1`. The sphere homeomorphism remains well-defined on the empty type.

`zeroCenter` exists in every normed space. Contact radius 1 is valid for each unit direction, and uniqueness proves `radius_zero`. The identity and isometry assertions follow correctly. These assertions remain valid as vacuous function equalities or metric assertions on an empty sphere. No theorem incorrectly asserts that the smallest possible contact/isometry Lipschitz constant must be 1 on an empty domain.

## Lean API checks and axiom risks

A source scan found no `sorry`, `admit`, explicit `axiom`, `unsafe`, or trust-altering option in the library modules. The noncomputable use of `Classical.choose` is explicit and expected. Imported tactic implementations produce ordinary proof terms to be checked by Lean; none of the reviewed modules requests native evaluation or an extra axiom. The final compiled `#print axioms` audit was independently inspected: each of all 47 public declarations depends on exactly `[propext, Classical.choice, Quot.sound]`. There is no `sorryAx` or unexpected axiom dependency.

The reviewer checked the official local signature of `intermediate_value_Icc` in `Mathlib/Topology/Order/IntermediateValue.lean`, confirming it supplies membership in the image of the real interval as used by `exists_positive_contact`. The reviewer also ran the following tiny API check without starting a Lake build:

```sh
PATH="<project>/lean-4.24.0-linux/bin:$PATH" lake env lean <historical-review-check>.lean
```

The check imported `Mathlib.Algebra.Group.Basic`, printed the four generic additive cancellation signatures, and elaborated:

```lean
example {E : Type*} [AddCommGroup E] (c x : E) : c + (x - c) = x := by
  simp only [add_sub_cancel]
```

The final check completed with exit code 0. An earlier exploratory check also requested the nonexistent identifier `add_sub_cancel_comm`, and consequently exited 1; that speculative line was removed for the clean run. The checked signature is `add_sub_cancel (a b) : a + (b-a) = b`. Therefore the reviewer's initial suspicion about the original `radius_direction` cancellation was incorrect and was explicitly retracted during review. The executor's replacement by an `abel`-proved identity is mathematically equivalent.

## Final compilation and audit verification

The reviewer independently reread the source after the elaboration repairs. They preserve the mathematical statements: explicit norm simplification and the correct positive multiplication cancellation theorem in `Basic`; `NNReal` notation scope and noncomputable real-valued constants in `Lipschitz`; an explicit additive cancellation identity and weaker norm-only assumptions in `Inverse`; and an explicit type for the last divided inequality and removal of an unused `ring` tactic in `Derived`. No mathematical defect was introduced.

The observed successful milestone logs are:

| Module | Accepted build log |
| --- | --- |
| `Basic` | `milestone-1-attempt-2.log`, 1518 jobs, successful |
| `Lipschitz` | `milestone-2-attempt-2.log`, 1519 jobs, successful |
| `Inverse` | `milestone-3-attempt-3.log`, 1520 jobs, successful |
| `Derived` | `milestone-4-attempt-2.log`, 1521 jobs, successful, with unused-tactic warnings subsequently removed |

The subsequent full `lake build` compiled the cleaned-up `Derived` and root `RadialContact` modules successfully (1523 jobs), as recorded in `full-build-attempt-1.log`. The final repeated `lake build` completed successfully with cached dependencies and no warnings in `final-build.log`.

The final `validation.json` has overall exit code 0 and these command results:

| Command | UTC start | UTC finish | Exit |
| --- | --- | --- | --- |
| `lake build` | `2026-10-11T02:35:23.526329+00:00` | `2026-10-11T02:35:24.551882+00:00` | 0 |
| `lake env lean evidence/AxiomAudit.lean` | `2026-10-11T02:35:24.552902+00:00` | `2026-10-11T02:35:37.117585+00:00` | 0 |

The reviewer independently counted the source declarations and the printed audit entries: 47 in each, with no missing or extra declaration names. All 47 had the same three standard axiom dependencies listed above. The final audit contains no errors, warnings, or `sorryAx`. An independent scan of the fully explicit statements found no `CompleteSpace`, `FiniteDimensional`, `StrictConvexSpace`, `Nontrivial`, or `Nonempty` assumption. Recomputed hashes match validation for every reviewed source file.

An initial audit failed only because it requested the unsupported Lean option `pp.width`; the executor retained that audit and its validation record as `theorems-and-axioms-attempt-1.log` and `validation-attempt-1.json`, removed unsupported printing options, and reran successfully. Earlier failed elaboration logs can contain warnings about Lean-generated `sorry` placeholders for declarations whose elaboration failed. Such logs document rejected attempts, not accepted final declarations. The final clean build plus the complete compiled axiom audit establishes that no such placeholder is present in the accepted public library declarations.

## Final conclusion and limitation

The final reviewed library successfully compiles in pinned Lean/mathlib 4.24.0, and all 47 public declarations have only the standard Lean axioms `propext`, `Classical.choice`, and `Quot.sound`. The requested theorems and derived improvements retain the arbitrary real normed-space scope, correct empty-sphere behavior, and correct zero-center behavior. No formal proof or source-review blocker remains.

The blocked archive transfer remains an independent provenance limitation: equivalence to the requested unavailable study/review files is not certified. This does not affect the correctness of the compiled claims derived from the user-authorized specification.
