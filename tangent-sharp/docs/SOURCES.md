> Historical baseline record for the original cubic project. Current sharp-series results are described in the tangent-sharp project README and sharp evidence. Use scripts/verify-sharp.sh for the current 78-declaration audit; legacy scripts/verify.sh only audits exported declarations and writes historical logs.

# Source attribution and verification boundaries

The Lean bridge lemmas and mathematical proof in this project were constructed
for the user's conditional tangent-limit task. The supplied
`OpenAI-math-research-starter-2026-10-11.zip` provided supporting ordinary proof
notes and an ordinary proof review. Its packaged SHA-256 manifest had 38 entries;
all matched on local inspection. Relevant reference files are preserved without
changes here:

- `starter-reference/pi-bridge/study.md`: rational approximation to tangent growth.
- `starter-reference/reviews/pi-review.md`: ordinary proof and source-record review.
- `starter-reference/reviews/pi-review-validation.json`: the supplied review record.

The archive fingerprint and publication subset are recorded in
`starter-reference/inspection.json`. The starter did not supply Lean source for
these bridge lemmas or compiled Lean evidence. Its source-inspection claims and
ordinary review are distinct from this project's executed compiler checks.

The reference notes attribute the statement of the approximation hypothesis to:

- [OpenAI/math scope note 017](https://github.com/openai/math/blob/main/lean/docs/017.md).
- [PiExponent comparator statement](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PiExponent.lean).
- [PiExponent Main.lean statement](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/PiExponent/Main.lean).

These are retained public source locators from the starter's research record.
The scope/comparator locators are branch-based as supplied; the Main locator is
pinned to the supplied revision. They are not proof dependencies. This project does not import
that research repository, independently verify those upstream claims, or prove
the π-approximation hypothesis. `TangentLimit.PiDiophantine` remains an explicit
argument to every conditional conclusion.

Standard trigonometric, real-power, limit, summability, and π-irrationality
results are imported from [mathlib v4.24.0](https://github.com/leanprover-community/mathlib4/tree/f897ebcf72cd16f89ab4577d0c826cd14afaafc7).
The project uses Lean 4.24.0; dependency commits are recorded in
`lake-manifest.json`. The compiled axiom inventory uses only the standard
foundational axioms `propext`, `Classical.choice`, and `Quot.sound`.

The stronger general-weight series discussion in the supplied reference review
is not a claimed compiled theorem here. The compiled cubic-series extension
uses the simpler pointwise comparison at exponent 5/2.
