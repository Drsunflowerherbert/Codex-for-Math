# Independent audit of finiteness and termination

Reviewer task: `finite_state_review`. Main source reviewed initially:
`Egyptian/Finite.lean`, theorem `finite_sortedRepresentations`.

## Finiteness

The theorem is mathematically valid for every real `x`, with no assumption of
rationality, positivity, or `x < 1`. It asserts propositional finiteness, not
effective exact enumeration for a black-box real input.

For length zero the state set is contained in the singleton empty list. For
successor length, positivity of all denominators forces a positive reciprocal
sum. Thus, if `x ≤ 0`, the set is empty. If `x > 0`, a sorted list with first
denominator `a` satisfies `x ≤ (n+1)/a`. An Archimedean integer bound
`B > (n+1)/x` forces `a < B`. For each of the finitely many candidate first
denominators, its tail has length `n`, is positive and sorted, and has sum
`x−1/a`, so induction applies. Induction at arbitrary real values is essential:
the theorem does not assume that arbitrary candidate residuals are positive.

The definition uses nondecreasing sorted lists and retains duplicates. This is
the correct canonical state space for duplicate cleanup. It does not prematurely
assume pairwise distinctness.

## Completeness and invariant obligations

Any list with positive denominators can be sent to this state space by sorting;
the sorting permutation must preserve length, reciprocal sum, natural
denominator sum, positivity, and the `Nodup` property. Sorting alone does not
establish termination: each duplicate-replacement successor must be sorted and
proved to remain in the same fixed-length, fixed-value state set.

## Termination orientation

For well-founded recursion the relation must be
`R next current := weight current < weight next`. The cleanup step increases
denominator sum in forward time. Reversing these arguments would fail to prove
termination in the intended direction.

`review/FiniteTermination.lean` provides an independent generic proof on the
subtype of a finite state set. If `B` is the maximum of all weights, the natural
rank `B−weight state` strictly decreases along `R`. Both weights are bounded by
`B`, so natural subtraction cannot truncate in a way that spoils strictness.
The subtype membership obligations prevent accidental use of an ambient
unbounded state space.

Collisions with other retained denominators do not invalidate this termination
method. A step need not reduce the number of duplicates: strict growth of the
natural denominator sum within the same finite set is sufficient. In particular,
the progress proof must not add an unjustified claim that each new pair is
disjoint from the remainder.

This argument certifies logical termination. It supplies neither a universal
numeric step bound such as 10000 nor a sharp maximum-denominator bound. The
finite-set maximum may be chosen classically; executable enumeration for an
arbitrary real input is a separate issue.

## Independent compiled orientation check

`review/BoundedTermination.lean` compiled successfully with Lean 4.24.0 before
mathlib source setup completed. It imports only `Lean.Elab.Tactic.Omega` and
contains both the bounded-weight well-foundedness theorem and
`terminal_exists_of_bounded_progress`. The latter converts a progress rule for
every bad state into existence of a good state by well-founded induction.

Command (working directory `<project>`):

```sh
ELAN_HOME=<project>/tooling/elan \
PATH=<project>/tooling/elan/bin:$PATH \
lake env lean review/BoundedTermination.lean \
  > evidence/reviewer-bounded-termination.log 2>&1
```

Exit status: 0. The log prints actual theorem types and axiom outputs:

- `bounded_increasing_weight_wellFounded`: `[propext, Quot.sound]`.
- `terminal_exists_of_bounded_progress`:
  `[propext, Classical.choice, Quot.sound]`.

## Independent compiled finite-set wrapper

`review/FiniteTermination.lean` also compiled successfully after the implementation
source build produced `Mathlib.Data.Set.Finite.Lemmas.olean`. Its only imports
are this finite-set module and `Lean.Elab.Tactic.Omega`. It obtains an upper
bound from the finite image of natural weights; for a nonempty image, the
mathlib lemma chooses a member with maximal weight.

Command (same working directory):

```sh
ELAN_HOME=<project>/tooling/elan \
PATH=<project>/tooling/elan/bin:$PATH \
lake env lean review/FiniteTermination.lean \
  > evidence/reviewer-finite-termination.log 2>&1
```

Exit status: 0. The log prints actual theorem types and axiom outputs. Both
`finite_increasing_weight_wellFounded` and
`finite_increasing_weight_induction` have only
`[propext, Classical.choice, Quot.sound]`. Neither has `sorryAx`.

## Main finiteness theorem: imported and checked

The implementation build then completed `Egyptian.Finite` successfully. The reviewer
independently compiled `review/FiniteStatements.lean`, importing that module
and checking the theorem at arbitrary real `x` with no additional premise.
`evidence/reviewer-finite-statements.log` prints the complete sorted-state
definition and the actual theorem type:

```lean
Egyptian.finite_sortedRepresentations :
  ∀ (n : ℕ) (x : ℝ), (Egyptian.sortedRepresentations n x).Finite
```

Its only axioms are `[propext, Classical.choice, Quot.sound]`.

The check command was the same environment invocation as above, with
`lake env lean review/FiniteStatements.lean` and output redirected to
`evidence/reviewer-finite-statements.log`; exit status was 0.

## Main termination and public theorem

The main `Egyptian/Termination.lean` uses the same bounded rank and obtains
its bound from `(hs.image weight).bddAbove`. Its relation is correctly oriented
on the subtype. `cleanup_wellFounded` is valid at every real `x`: it concerns
strict weight growth inside the fixed finite state set, independently of whether
duplicate replacement is available at that value.

The main `exact_length_distinct` obtains a representation of maximal
denominator sum within the sorted invariant set. A duplicate would supply a
strictly larger member of the same set, contradicting maximality. Every sorting
invariant needed by that argument is supplied by `canonical_mem` and the
sorting permutation's `sum_eq`. The theorem's stated `0 < reciprocalSum input`
premise is redundant for nonempty positive lists but correctly matches the
requested theorem; its presence is harmless.

The implementation completed the core build successfully (965 jobs). The reviewer
independently imported `Egyptian.Termination` and compiled
`review/FinitePublicStatements.lean`, exit status 0. The actual theorem types and
axiom outputs are in `evidence/reviewer-finite-public-statements.log`. This
checks `canonical_mem`, `sorted_duplicate_cleanup`, `exact_length_distinct`,
`finite_increasing_weight_wellFounded`, and `cleanup_wellFounded`; every one
uses only `[propext, Classical.choice, Quot.sound]`.

Command (same environment and working directory):

```sh
ELAN_HOME=<project>/tooling/elan \
PATH=<project>/tooling/elan/bin:$PATH \
lake env lean review/FinitePublicStatements.lean \
  > evidence/reviewer-finite-public-statements.log 2>&1
```

Verdict: accepted for the fixed-length finite state argument and the primary
cleanup theorem. No unresolved mathematical or compilation blocker remains
within this reviewer scope. Exact reviewed source hashes are recorded in
`review/FiniteStateAudit.source.sha256`.
