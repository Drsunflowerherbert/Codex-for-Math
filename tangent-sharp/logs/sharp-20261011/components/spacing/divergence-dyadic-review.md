# Independent review: divergence and dyadic summability

Reviewed 2026-10-11 at 03:07 UTC. No source files were changed.

## Conclusion

No mathematical or assumption-boundary issue found in `Divergence.lean` or
`DyadicSummability.lean`. Each source independently compiled with exit 0 and
empty output. An independent import/type/axiom audit also exited 0. The review
supports these components; it does not itself audit the final integrated sharp
theorem or its weighted block estimate.

## Unconditional divergence

`Divergence.lean` imports `NonPole.lean`, whose non-pole theorem explicitly uses
mathlib's proved `irrational_pi`. No project Diophantine hypothesis appears in
the source or theorem types. The final unconditional type is:

```lean
TangentLimit.not_summable_abs_tan_div_rpow_positive
  (s : ℝ) (hs : s ≤ 1) :
  ¬ Summable (fun n : ℕ =>
    |Real.tan ((n + 1 : ℕ) : ℝ)| /
      ((n + 1 : ℕ) : ℝ) ^ s)
```

The sine subtraction identity gives a lower bound `sin 1` on adjacent
absolute tangents. `sin 1 > 0` follows from `0 < 1 < π`. Both adjacent
cosines are nonzero by the unconditional integer non-pole theorem, so the
division-based tangent estimate has its required hypotheses.

The exponent-one contradiction adds the series to its one-step shift. Both
are summable if the original series is summable. For every `n`, the resulting
sum dominates `sin 1 / (n+2)`: divide the adjacent lower bound by the larger
denominator, then increase the first weighted tangent by decreasing its
denominator from `n+2` to `n+1`. This is sound without requiring disjoint
pairing; it uses exactly the sum of two summable series. Dividing by nonzero
`sin 1` yields the shifted harmonic series, and shifting back by two
contradicts `Real.not_summable_one_div_natCast`. Its natural zero term is
harmless because division at zero is the convention used by that library
theorem and a finite initial segment does not affect summability.

For arbitrary real `s ≤ 1`, including negative `s`, the base `n+1` is at
least one and strictly positive. Real-power monotonicity in the exponent
therefore gives `(n+1)^s ≤ n+1`; its power remains strictly positive.
Reciprocal comparison consequently shows the exponent-`s` terms dominate
the exponent-one terms. No positivity assumption on `s` is hidden.

## Dyadic infrastructure

`sum_range_two_pow_eq` keeps `f 0` separate and partitions the remaining
positive indices into the half-open blocks `[2^k, 2^(k+1))`. The base case
is `range 1 = {0}`, and the inductive finite-range identity has the correct
endpoint and orientation. No positive integer is omitted or duplicated.

`nat_le_two_pow` ensures every finite initial segment fits in a dyadic
initial segment. For nonnegative `f`, prefix sums increase under set
inclusion. The finite block bounds then majorize every prefix by
`f 0 + tsum g`; nonnegative summable `g` justifies its finite-sum bound.
The standard bounded-prefix criterion gives summability of `f`.

The positive-only variant replaces just `f 0` by zero, obtains global
nonnegativity, and transfers summability back through the shift-by-one
equivalence. Every block starts at a positive `2^j`, so its replacement
has identical block sums. Arbitrary zero terms are thus handled correctly.

The doubling harmonic block has exactly `N` terms in `range N`, each at
most `1/N` for positive `N`. The cardinality computation gives total at
most one. Splitting the harmonic sum of length `2^(j+1)` into two equal
parts proves `H_(2^j) ≤ j+1` with the reciprocal indices correctly starting
at one; the `j=0` case is `H_1 = 1`.

The linear geometric bound uses the standard summability of both `j*ρ^j`
and `ρ^j` for `0 ≤ ρ < 1`. The rpow identity converts positive dyadic bases
to `(2^β)^j` for every real `β`. A negative `β` gives `0 < 2^β < 1`, so the
rpow/harmonic bridge has no missing exponent restriction. All multiplying
constants are explicitly nonnegative where inequalities require it.

## Compiler and axiom evidence

From `<project>`, after sourcing
`scripts/environment.sh`, these independent commands exited 0:

```sh
lake env lean TangentLimit/Divergence.lean
lake env lean TangentLimit/DyadicSummability.lean
lake env lean <historical-workspace>/scratch/spacing/ReviewAudit.lean
```

Logs are `divergence-readonly-compile.log`, `dyadic-readonly-compile.log`, and
`divergence-dyadic-type-axiom-audit.log` in `<historical-workspace>/scratch/spacing`.
All audited declarations depend only on
`[propext, Classical.choice, Quot.sound]`, except `nat_le_two_pow`, which
needs only `[propext, Quot.sound]`. No `sorry`, `admit`, or new axiom occurs
in either source or `NonPole.lean`.

Source SHA256:

* Divergence: `6c3c2ca8bf67d07e29c1dbf4d845b214fac1cd905b81c00468065c32905e7158`
* DyadicSummability: `8407909d22436551d60b8e71e7e88e790c53019c8b1ae647962a9dc755a8132c`

Pins remain Lean `v4.24.0`, mathlib
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, and original project HEAD
`d00a89dd9ce6c8ef782234d28c93e69cb712c947`.
