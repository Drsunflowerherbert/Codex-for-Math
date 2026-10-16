# Exact theorem and definition verification harness

Prepared against `frenzymath/HolomorphicAnosov` commit **65f2b33a7309de661a8500e4642e5609a537a8ff**, with its locked Lean **4.35.0-rc1** and Mathlib commit **c32e1ec0d1eb5237ba344eee50162f45d5b0fc76**. These files live outside the upstream checkout and do not modify its source. These harnesses were subsequently executed by the main verification track. Both corrected runs labelled `02` exited 0; the first runs failed on an unsupported `pp.width` printing option in the audit files. See the complete run logs and `../results/compiled-axiom-summary.json`. The independent harness author initially prepared them without executing Lean.

Files:

- `VerifyStatements.lean`: imports the actual solution, defines the four complete expected statement types copied from the challenge/solution interfaces, and requires both each actual target and each public comparator wrapper to inhabit the corresponding type. It prints all eight signatures, all four expected proposition bodies, all four wrapper declarations, and the transitive axiom lists of all eight public declarations and eight audit bindings.
- `VerifyDefinitions.lean`: checks selected imported definitions against explicit expanded mathematical expressions using definitional equality (`rfl`/`Iff.rfl`); checks the actual fixed-iterate Anosov fields; prints the manifold, bundle, lattice, hyperbolicity, conjugacy, and HS interfaces and relevant Mathlib structures.

Run these only after the pinned project and `Comparator.Solution` have been built in the isolated build checkout. From that checkout, with `VERIFY_ROOT` set to the isolated audit directory and the pinned toolchain first in `PATH`, the corresponding payloads are:

```sh
"$VERIFY_ROOT/toolchains/lean-4.35.0-rc1-linux/bin/lake" env lean "$VERIFY_ROOT/checks/VerifyStatements.lean"
"$VERIFY_ROOT/toolchains/lean-4.35.0-rc1-linux/bin/lake" env lean "$VERIFY_ROOT/checks/VerifyDefinitions.lean"
```

Save complete stdout/stderr and exit status for each invocation. These are verification commands, not a request to replace existing logs or source files. A missing imported `.olean` reports an incomplete build environment; it does not establish a mathematical or formalization error. A syntax/type error in an audit file must first be distinguished from a failure of the imported upstream theorem.

## What the expected types say

`StatementA` has the full compact connected complex manifold, biholomorphism, actual Anosov datum, and stable-or-unstable **complex** rank-one hypotheses. It concludes actual biholomorphic conjugacy to a **hyperbolic**, lattice-preserving complex-linear torus automorphism.

`Statement11` requires complex dimension d≥2 and stable complex rank one; it concludes a homeomorphism to the real torus of dimension **2d** intertwining f with an invertible integral matrix having no eigenvalue on the unit circle. Its type has no transitivity or holomorphic-splitting input.

`Statement12` requires the two actual invariant distributions to be realifications of holomorphic subbundles and X to be **homeomorphic**, not necessarily diffeomorphic, to some real torus. Its conclusion uses a genuine biholomorphism and lattice-preserving complex-linear torus automorphism. It does **not** assert hyperbolicity explicitly, matching the printed Theorem 1.2; the actual Theorem A target supplies that separately.

`Statement13` concludes holomorphic subbundles of ranks 1 and d−1 whose realifications **equal the original stable and unstable distributions pointwise**. It cannot be satisfied by unrelated convenient subbundles.

**A, 1.1, and 1.3 explicitly quantify over `HS : HomotopyTorusRigidity`; 1.2 does not.** The harness preserves this premise. It does not claim an unconditional proof of HS. The expanded definition in the second file is the schema that every closed smooth real n-manifold homotopy equivalent to T^n is homeomorphic to it, for n≥5.

`Function.Semiconj h f A` is a full conjugacy here because h has the type `Biholomorph`, which includes a bijective map and a holomorphic inverse. The definition harness unfolds it to the pointwise equation `h (f x) = A (h x)` and prints `Diffeomorph` as additional evidence.

## Which declarations are checked

| Role | Declaration |
|---|---|
| Actual A target | `HolomorphicAnosov.theorem_A` |
| Actual 1.1 target | `HolomorphicAnosov.theorem_1_1` |
| Actual 1.2 target | `HolomorphicAnosov.theorem_1_2` |
| Actual 1.3 target | `HolomorphicAnosov.theorem_1_3` |
| Public A wrapper | `HolomorphicAnosov.zhang_theorem_A` |
| Public 1.1 wrapper | `HolomorphicAnosov.zhang_theorem_1_1` |
| Public 1.2 wrapper | `HolomorphicAnosov.zhang_theorem_1_2` |
| Public 1.3 wrapper | `HolomorphicAnosov.zhang_theorem_1_3` |

The public wrapper names match `Comparator/config.json`, which gives `Comparator.Challenge` as specification module and `Comparator.Solution` as solution module. The config permits exactly these axiom names:

```text
propext
Quot.sound
Classical.choice
```

For each `#print axioms` output, check that the listed transitive axiom closure is a **subset** of that list. In particular, flag `sorryAx` or any additional custom/trust axiom. Do not infer success merely because the command itself exits successfully: `#print axioms` displays the axiom list; it does not enforce this whitelist. Conversely, not all three permitted axioms must appear in each theorem.

The HS premise will **not appear** as a global axiom in this output: it is a universally quantified parameter of the theorem. This is why the exact-type checks and printed signatures are needed in addition to axiom checks. An axiom list alone cannot show whether a theorem has an extra hypothesis.

## Why Challenge is not imported

`Comparator/Challenge.lean` contains its own copied definitions and four statement placeholders with `sorry`, under the same public theorem names as `Comparator/Solution.lean`. Importing it together with Solution would cause duplicate declarations and/or contaminate the wrong specification environment. Its placeholders specify the task; they are not the solution proof bodies.

The expected types are instead copied into a fresh namespace (`HolomorphicAnosovAudit`) in the harness. The eight assignments then ask Lean to type-check the **actual imported targets and actual solution wrappers** against those complete types. The `#print axioms` queries refer specifically to those actual declarations, not the challenge placeholders.

This harness tests correspondence to the repository's intended interface, not the truth of the entire mathematical interpretation by itself. The accompanying source audit is the published `notes/lean-semantic-correspondence.md`. The successful execution and clean axiom output provide compiled evidence for these exact conditional statements and expanded definitions at the pinned source/dependency versions; it would not discharge HS or replace the mathematical review of the PDF.
