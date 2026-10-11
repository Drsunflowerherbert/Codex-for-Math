# Final independent audit of all public declarations

Reviewer task: `hypotheses_review`. Final aggregate, every local module under
`Egyptian/`, and `Evidence.lean` were independently inspected after the completed
aggregate build. The archived ordinary-proof source was unavailable; the audit
uses the user delegation prompt and local compiled source.

## Verdict

**PASS.** The complete public catalog contains **46 named declarations**:
**4 definitions and 42 theorems**. `Evidence.lean` checks every declaration's
actual type and prints every theorem's axiom dependencies, with no omissions or
extra catalog entries. Independent compilation of that harness exited zero:

```sh
ELAN_HOME=<project>/tooling/elan \
PATH=<project>/tooling/elan/bin:$PATH \
lake env lean -Dpp.funBinderTypes=true Evidence.lean \
  > evidence/reviewer-all-statements.log 2>&1
```

The explicit lambda-binder option makes the state subtype in the termination
contracts visible in the compiler output. The log has no errors or warnings.
All 42 theorem axiom lists are subsets of
`[propext, Classical.choice, Quot.sound]`. There is no `sorryAx`, source admission,
or local custom axiom/constant declaration.

## Contract checks

| Public contract | Final audit result |
| --- | --- |
| `exact_length_distinct` | Positive natural input denominators and `0 < reciprocalSum input < 1`; positive `Nodup` output with exactly the input length and value. No hidden extra input hypothesis. |
| `finite_sortedRepresentations` | Finite positive nondecreasing fixed-length representations for every real value. No unsupported executable-real enumeration claim. |
| Parity replacement identities and growth | Even identity requires positive half-denominator; strict-growth conditions are exactly the cases supplied by duplicated denominators at least three. |
| `duplicate_cleanup` and `sorted_duplicate_cleanup` | Positivity, length, value and finite-state membership are preserved; natural denominator sum strictly increases. No marker or duplicate-count invariant is claimed. |
| `cleanup_wellFounded` | Correct next/current orientation, with both arguments restricted to the same `sortedRepresentations n x` subtype. |
| `boundary_counterexample` | `[2,2]` is positive and has value one; every positive distinct representation with its length and value is impossible. |
| `pad_one_preserving_denominator` | Positive distinct expansion of one, length at least three, and a marker already present in the input; positive distinct output of length exactly one more, value one, and the same marker present. No extra prime or collision hypothesis survives in the public theorem. |
| `pad_one_preserving_denominator_bounded` | Adds an arbitrary caller-supplied upper bound `B` on input denominators and proves every output denominator is at most `B*(B+1)`. Taking `B` to be the input maximum yields the stated coarse maximum-denominator bound. |

The supplemental padding lemmas correctly isolate both possible ordinary-split
collisions, supply the nonprime obstruction from the sum-one invariant, and use
a factor split that avoids the specified retained maximum. Both new denominators
also avoid all smaller tail entries. The formal product-collision example is
present in the final public catalog and compiled.

## Executable companion

`scripts/exact.py` uses `fractions.Fraction` for exact arithmetic and has no
universal step guard. The enumerator requires exact rational inputs; the CLI
parses them as `Fraction`. The padding companion checks positivity, distinctness,
length, value, marker membership, and the coarse maximum-denominator bound.
Its tests report 278 cleanup states and 28 marker-padding checks, including the
product-collision case. This companion is expressly labeled validation support,
not a formal extraction/refinement theorem or universal runtime claim.

The denominator-sum example is correctly recorded as **56 -> 72**, not 46 -> 72.

## Durable evidence and scope

- `evidence/reviewer-all-statements.log`: actual complete type/axiom output from
  the independent successful compiler invocation.
- `review/AllStatementsAudit.json`: machine-readable declaration coverage,
  axiom/admission checks and formal-source SHA256 hashes; status `pass`.
- `review/AllStatementsAudit.source.sha256`: final formal source, harness and
  executable-companion hash snapshot.

No missing/strengthened hypothesis, unexpected axiom, admission, contract defect,
or remaining compiled-proof blocker was identified. No main source was edited
by this final audit. Subsequent mathematical source changes require a fresh
audit or explicit comparison against this hash snapshot.
