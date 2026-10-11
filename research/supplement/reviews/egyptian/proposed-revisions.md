# Proposed clarifications for the Egyptian fraction study

These are proposed edits only. The original study, script, examples, author manifest, and theorem records are unchanged. No theorem statement needs repair.

## Correct the padding size disclaimer

Replace study.md line 74 with:

> Iteration retains m at every prescribed larger length. It does not preserve every original denominator. The construction gives the coarse one-step bound M′≤M(M+1), where M is the largest input denominator, and consequently M_t≤(M_0+1)^(2^t)−1 after t padding steps. No sharp or economical denominator-size estimate is claimed.

Reason: the explicit construction already supplies these elementary bounds, so the current phrase “nor does it imply any denominator-size bound” overstates the limitation.

## Specify the executable enumeration domain

Replace the first sentence of study.md line 18 with:

> For a positive rational x supplied exactly, the proof gives a complete finite enumeration algorithm. The finiteness theorem itself remains valid for every real x>0; a represented x is necessarily rational.

Keep the remaining interval bounds, branch rules, and exact-arithmetic instruction. The current bounds are valid, although they search some branches that cannot succeed.

## State the script contract

Add after the description of check_examples.py in Section 4:

> The functions assume finite lists of positive integer denominators, positive rational enumeration inputs, positive integer lengths and positive integer lower bounds. The script's default enumeration lower bound is two. Cleanup has a 10,000-step operational guard; the universal termination proof does not claim that every input finishes within this guard. Run the script without Python optimization so its assertions remain enabled.

For a later reusable library, replace assertion-only input checks with explicit domain validation and separate the top-level certificate-writing run under a main guard. This is hardening advice, not a prerequisite for the validity of the existing, independently checked run.

## Separate proof review from finite computational coverage

Do not silently overwrite the existing author-level statuses. Link a separate review record for each theorem with ordinary_proof_review_status set to independently_reviewed_pass and lean_status left as not_run.

- EGY-001: ordinary proof of finiteness; finite computational coverage consists of strict expansions of one at lengths three through six
- EGY-002: ordinary proof of universal cleanup; direct arithmetic coverage consists of 34 inputs and 80 replacements
- EGY-003: ordinary proof of exact marker padding; direct coverage consists of 14,307 enumerated marker cases and one separate composite exception
- EGY-004: ordinary induction proof; the original script does not directly exercise arbitrary target lengths
- EGY-005: ordinary impossibility proof; the original script does not directly encode it
- EGY-006: ordinary impossibility proof; the original script does not directly encode it

Keep native_mrs_imported as false unless an actual import is later performed. Retain the source revision, the existing attribution, and the absence of a novelty claim.
