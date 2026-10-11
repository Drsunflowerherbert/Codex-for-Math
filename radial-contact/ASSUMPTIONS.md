# Assumptions inventory

The mathematical source is byte-for-byte identical to the delivered original.
`evidence/assumptions.json` pairs every declaration's complete compiled type
with its source module, explicit class names, and actual axiom dependencies.
The complete type is authoritative; the class-name list is a search aid.

| Result family | Ambient assumptions | Parameter assumptions |
| --- | --- | --- |
| `UnitSphere`, `InteriorCenter`, zero center, elementary distance bounds | `NormedAddCommGroup E` | Subtypes respectively require norm one and norm strictly below one |
| `parameter_comparison` | `NormedAddCommGroup E`, `NormedSpace ℝ E` | Nonnegative `r`, `r ≤ s`, both contact norms one; directions need not be unit |
| `parameter_abs_comparison` | Same real normed-space assumptions | Both parameters nonnegative, both contact norms one |
| `positive_contact_unique` | Same | Center norm strictly below one, positive parameters, both contact norms one; unit direction not required |
| `positive_contact_bounds` | Same | Unit direction, nonnegative parameter, contact norm one; interior center not required |
| Positive-radius existence, radius/contact maps and their Lipschitz estimates | Same | Interior center and unit direction(s) |
| Normalized inverse and sphere homeomorphism | Same | Interior center and unit-sphere point(s) |
| Reciprocal-radius and inverse Lipschitz refinements | Same | Interior center and unit direction(s)/sphere point(s) |
| `unitSphere_isEmpty_of_subsingleton` | `NormedAddCommGroup E`, `Subsingleton E` | None; it proves that no unit direction exists |
| Zero-center radius, identities and isometries | Real normed-space assumptions | Unit direction or sphere point; assertions remain valid on empty domains |

No declaration assumes completeness of E, finite dimension, smoothness, strict
convexity, a nontrivial E, or an inhabited sphere. Real scalar analysis uses the
usual properties of ℝ. The empty-sphere lemma's `Subsingleton E` assumption is
local to that lemma; it is not imposed on the contact construction.

The allowed transitive logical axioms are `propext`, `Classical.choice`, and
`Quot.sound`. Noncomputable radius selection uses classical choice. The audit
rejects any additional dependency, including `sorryAx`. Requested mathematical
results remain in Basic/Lipschitz/Inverse; derived refinements remain in Derived.
