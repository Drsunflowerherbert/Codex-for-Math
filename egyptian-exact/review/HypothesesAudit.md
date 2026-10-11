# Independent public statement and hypothesis audit

Reviewer task: `hypotheses_review`. Reviewed source on 2026-10-11:
`Egyptian/Basic.lean`, `Egyptian/Finite.lean`, `Egyptian/Cleanup.lean`, and
`Egyptian/Counterexample.lean`, `Egyptian/Termination.lean`, and
`Egyptian/Examples.lean`. The archive was unavailable; this audit uses the
delegation prompt and the actual local Lean source. The final independent
compiler audit now passed as recorded below.

## Mathematical verdict

The requested primary theorem is valid. The public statement
`exact_length_distinct` includes positive natural denominators, positive
reciprocal sum, and reciprocal sum strictly below one, and concludes positive
natural denominators, `Nodup`, unchanged length, and unchanged real reciprocal
sum. It does not claim marker preservation or a sharp denominator bound.

The final proof uses its positive-sum hypothesis to exclude the empty input.
No additional nonemptiness hypothesis appears in the actual public type.

## Replacement identities and edge cases

For odd `d = 2*k+1`, the pair `[d,d]` is replaced by
`[k+1,d*(k+1)]`. Reciprocal sum is preserved for every natural `k`, including
zero. Denominator-sum gain is `2*k^2`, strictly positive for `k >= 1`.

For even `d = 2*k`, the pair is replaced by `[k+1,k*(k+1)]`.
The identity requires `k > 0`, since Lean interprets inverse zero as zero.
Denominator-sum gain is `(k-1)^2`, strictly positive for `k >= 2`.

`duplicate_ge_three` supplies exactly these growth hypotheses: two copies of a
positive denominator one or two already have reciprocal sum at least one.
The total contribution of the remaining natural denominators is nonnegative.

The cleanup theorem correctly preserves positivity, length and value, and
strictly increases natural denominator sum. It permits collisions with existing
entries. Neither distinctness nor an arbitrary marker is asserted invariant.

The duplicate-count example has corrected denominator sums:
`[10,10,6,30] -> [6,30,6,30]`, reciprocal sum `2/5`, weight **56 -> 72**, and
duplicate excess **1 -> 2**. An earlier message mistakenly gave the old weight
as 46. No previous durable reviewer file contained that mistaken number.

Marker preservation fails for cleanup: `[4,4,6] -> [3,6,6] -> [3,4,12]`,
with reciprocal sum `2/3`, loses the specified denominator six.

## Finiteness and maximum argument

The canonical state set requires positive denominators, nondecreasing order,
fixed length and fixed real value, while retaining duplicates. Its finiteness
theorem correctly quantifies every real value without requiring rationality or
`x < 1`. For a nonempty sorted representation the first denominator `a`
satisfies `x <= length/a`; an Archimedean natural bound leaves finitely many
heads, and arbitrary-value induction gives finitely many tails for each head.

Sorting gives a nonempty canonical state set for the input. The proof chooses
a state maximizing denominator sum. A duplicate cleanup followed by sorting
preserves membership and strictly raises the weight, contradicting maximality.
This establishes the existential primary theorem without claiming an algorithm
with a universal iteration limit.

An explicit well-founded termination theorem must restrict states to the fixed
finite invariant family and use the relation
`R next current := current.sum < next.sum`. A maximum-weight-minus-current-weight
rank decreases. Increasing natural denominator sum on an unrestricted ambient
space would be insufficient.

## Boundary counterexample

The statement `two_positive_denominators_sum_one` proves that both denominators
must be two. The general theorem `no_distinct_two_term_one` therefore rules out
every positive distinct length-two expansion of one. `boundary_counterexample`
ties that impossibility to the exact input `[2,2]`, its positivity, its value,
and its length. These are the requested counterexample statements.

Positivity remains essential: `[0,1]` has distinct natural entries and reciprocal
sum one under Lean's inverse-zero convention, but is not a positive-denominator
representation.

## Compiled checks

`review/DuplicateExtraction.lean` independently compiled with Lean 4.24.0 and
imports only `Std`; its axiom output is
`[propext, Classical.choice, Quot.sound]`. Its source and build log are durable.

`review/PublicStatements.lean` is the independent final audit harness. It imports
the aggregate `Egyptian` module and prints the actual reciprocal-sum definition,
the sorted-state predicate, and the actual theorem types and axiom dependencies
of 19 public milestones, including `sorted_duplicate_cleanup`,
`exact_length_distinct`, `cleanup_wellFounded`, and `boundary_counterexample`.

Compilation command (working directory `<project>`):

```sh
ELAN_HOME=<project>/tooling/elan \
PATH=<project>/tooling/elan/bin:$PATH \
lake env lean -o review/PublicStatements.olean review/PublicStatements.lean \
  > evidence/reviewer-public-statements.log 2>&1
```

Exit status: **0**. The generated `.olean` and complete type/axiom log are
durable. The actual primary theorem type has exactly the requested positivity,
positive-value and value-below-one hypotheses, and exactly the positive,
distinct, equal-length and equal-value conclusion. The finite-state termination
type restricts its arguments to `sortedRepresentations n x`; it does not
accidentally assert well-foundedness on unrestricted natural-weight states.

All printed axiom lists are subsets of
`[propext, Classical.choice, Quot.sound]`. In particular, there is no `sorryAx`
and no additional axiom. `canonical_perm` and
`bounded_increasing_weight_wellFounded` use only `[propext, Quot.sound]`.

The exact boundary statements rule out every positive distinct two-term
representation of one and tie that impossibility to `[2,2]`. No missing or
strengthened hypothesis, logical proof defect, or compiled-proof blocker was
identified for the primary theorem and its supporting milestones.

Source hashes in `review/HypothesesAudit.source.sha256` identify this compiled
audit snapshot. Any subsequent mathematical source change should trigger a
fresh source review and type/axiom audit.
