# Finite-field product mixing

A standalone Lean library pinned to Lean 4.24.0 and mathlib revision
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.

## Completed formal scope

The supplied completed snapshot contains 85 audited declarations, including
definitions and helper lemmas, across eight library modules and their umbrella.
Its principal results are:

- `uniform_product_fourier_bound`: the rectangular normalized nonzero-frequency
  coefficient bound `sqrt(p / (|A| * |B|))`.
- `productSumProbability_lower_bound`: the diagonal `k`-product probability
  lower bound `[1-(p-1)*(sqrt(p)/|H|)^k]/p` for nonempty `H`.
- `four_product_probability_lower_bound` and `four_products_cover`: under
  `|H|^4 >= p^3`, every residue has probability at least `1/p^2` and is a sum
  of four products of `H` elements.
- `divisor_four_product_rational_lift`: a local positive-divisor lift giving
  a positive integral multiplier and a rational four-summand identity.

Primality, nonempty sampling sets where stated, and independent uniform
sampling are essential. Counts use ordered Cartesian tuples with their actual
multiplicities. Zero elements and repeated samples are allowed. The density
hypothesis in the four-product theorems itself implies nonemptiness.

See [proof notes](notes/proof-notes.md), the
[exact declaration inventory](evidence/final-theorem-inventory.log), and the
[formal scope map](evidence/formal-scope.json). The general heterogeneous
set/coefficient/shift theorem, radical-free criterion equivalences, the separate
squared count bound, and arbitrary-`k` divisor lifting are ordinary results
outside the completed exported formal scope. No global Egyptian-fraction
constant, novelty, optimal product count, or distinctness result is claimed.

## Sources

The ordinary input study and its prior review are already published:

- [Finite-field mixing study](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/finite-field-mixing/study.md)
- [Ordinary mathematical review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/e8b12891144385544976c0db277a64144837383d/research/supplement/reviews/finite-field-mixing/independent-review.md)
- [Motivating source passage](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/build/prescribed.tex#L326-L366)

Those ten ordinary records were not pre-existing Lean certificates. The new
formal results have the narrower scope listed above. The motivating source
attributes its bilinear estimate to Glibichuk and Konyagin. Retain the
repository's [third-party attribution](../THIRD-PARTY.md); no overall license
is assigned to this independently written project by this publication.

## Historical evidence and publication boundary

The [supplied final audit](evidence/final-independent-audit.json), dated
11 October 2026, records a successful fresh project-source build, all-declaration
axiom checks, and Lean smoke checks. It records Lean 4.24.0, the pinned mathlib
revision, and only the standard dependencies `propext`, `Classical.choice`, and
`Quot.sound`. The reported 7,360 jobs include provisioned dependencies; this
is not a claim that all of mathlib was rebuilt from scratch.

Publication review checked archive, source, and supporting-artifact hash
consistency and matched all 85 declaration names against the saved inventory.
It did not rerun Lean or the finite computations. All nine library source
files, both Lean check files, and the dependency pins are byte-identical to
the supplied completed snapshot.

Historical receipts retain their original contents and hashes. Some reference
excluded logs, reference archives, or environment-specific scripts; those
references describe the original verification run, not files shipped here.
In particular, the historical `scripts/verify.sh` command is not included.
The original finite-test checker and its input archive are also omitted, so
this public subset does not provide a standalone rerun of that exact suite.
Finite regression checks supplement the universal Lean statements; they do
not prove them. Four line pointers in `evidence/declarations.json` point to
the blank line immediately before an attributed declaration; names and saved
printed types remain authoritative.

The [batch source map](../publication/FINITE-FIELD-GUIDE-SOURCE-MAP.json)
records every supplied entry's disposition and original/public hashes. The
[batch file manifest](../publication/FINITE-FIELD-GUIDE-FILES.json) identifies
the current public bytes. No historical verdict is upgraded by a new hash.

## Reproduction inputs

Dependencies and compiled objects are not distributed. Install the pinned
Lean toolchain and obtain the exact dependencies in `lake-manifest.json`
(including the matching mathlib cache). From this project directory, the
standard source/check commands are:

```sh
lake build
lake env lean scripts/TheoremInventory.lean
lake env lean scripts/SmokeTests.lean
```

These commands describe how to check the published sources; they were not
executed during this publication-only review.

Publication note: this README was edited to remove private source metadata,
replace omitted-input references with public links, and clarify evidence and
reproduction scope. Mathematical implementation files were not changed.
