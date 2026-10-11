# Independent review: pole spacing and weighted blocks

Reviewed by the uniform-bound component implementation on 2026-10-11. This review is
read-only with respect to project sources. No mathematical or formalization
defects were found in the reviewed versions of `PoleSpacing.lean` and
`BlockEstimates.lean`.

## Uniform denominator and numerator coverage

Both spacing lemmas accept the full hypothesis

```lean
∀ q : ℕ, 0 < q → ∀ p : ℤ,
  c * (q : ℝ) ^ (1 - α) ≤ |(q : ℝ) * Real.pi - (p : ℝ)|
```

This is precisely what the compiled `piDiophantine_uniform` supplies. The
lemmas do not substitute an eventual-in-q bound. For the distance of one
argument, the denominator is `poleDenom n>0` and the integer numerator is
`2*n`. For differences between pole offsets, the numerator is `n-m` as an
integer, with both signs permitted. This all-integer numerator coverage is
essential and is correctly preserved.

The bound `poleIndex n<N` follows from `n<2N`, `poleIndex n*π≤n`, and `π>2`.
Thus `poleDenom n≤3N`. Because α>2 implies 1-α<0, decreasing the base from
3N to the positive denominator increases its real power. The direction of
`Real.rpow_le_rpow_of_nonpos` is correct. The identity
`|poleDenom n*π-2*n|=2*|poleOffset n|` produces exactly
`δ=(c/2)*(3N)^(1-α)`.

## Zero pole-index difference and orientation

The public pair-spacing theorem splits all three comparisons of the two pole
indices. Equal indices give
`poleOffset n-poleOffset m=n-m`. Since distinct natural arguments differ by
at least one and δ≤1/2, this case is valid without applying the approximation
estimate at denominator zero.

For unequal pole indices, the private lemma orients the difference so that
`q=poleIndex n-poleIndex m>0`. Natural subtraction is cast only after supplying
the appropriate order proof. The algebraic identity is

```text
q*π-(n-m)=-(poleOffset n-poleOffset m).
```

The other orientation uses `abs_sub_comm`. Thus no negative natural
denominator, truncated difference, or omitted r=0 case is present. The q≤3N
bound is conservative but sufficient.

## Weighted block and powers

`sum_abs_tan_div_rpow_le_reciprocal` requires positive N and nonnegative s.
For n≥N, `n^s≥N^s>0`, so replacing the denominator by N^s preserves the upper
bound. The positive pole-distance premise and the proved half-period bound
justify `|tan n|≤π/(2*|poleOffset n|)` at every term.

`weighted_block_coefficient` has positive c,N and is valid for arbitrary real
α,s,H. Its algebra gives

```text
π/(2*N^s) * (2/δ) * H
  = (2*π/c)*3^(α-1)*N^(α-1-s)*H.
```

The factor 2 is correct: δ contains c/2. The `Real.mul_rpow`, negation, and
subtraction identities use positive bases where needed. The dyadic identity
`(2^j)^a=(2^a)^j` is correctly oriented and valid for real a and natural j.

The reviewed integration in `SharpSummability.lean` supplies N≥1 and s>1,
therefore satisfying every positivity and nonnegative-s premise used above.
This observation does not substitute for the complete project integration
build and theorem audit.

## Fresh compiler evidence

Both reviewed source files compiled independently, with exit 0, to scratch
objects; their compiler logs are empty. The resulting object hashes exactly
match the objects imported by the type/axiom audit.

Commands, after sourcing `scripts/environment.sh` from the project root:

```bash
lake env lean -o <historical-workspace>/scratch/uniform/PoleSpacing-review.olean TangentLimit/PoleSpacing.lean
lake env lean -o <historical-workspace>/scratch/uniform/BlockEstimates-review.olean TangentLimit/BlockEstimates.lean
lake env lean <historical-workspace>/scratch/uniform/SpacingBlockAudit.lean
```

The audit records exact theorem types and `#print axioms` for the nine public
theorems in these files. Every result has only
`[propext, Classical.choice, Quot.sound]`. No placeholders or extra axioms
appear. These files make no unconditional assertion of `PiDiophantine` and
make no claim about conditional convergence of signed tangent series.

Source hashes were unchanged before and after review:

- `PoleSpacing.lean` SHA-256:
  `9faf23dbd9c48d93538e86746e13bfc20fe511aaa440bf8c01ca7f58acf35f48`.
- `BlockEstimates.lean` SHA-256:
  `52291955d48b84cddac050f5d1bbfbbc49379c98d77a8be3c4e55af0a034ec91`.

Object hashes:

- PoleSpacing:
  `0fd11d561c1b2487f140dbddbd15b18477c84a6fc9eb86d5f79cfc6ddde38fba`.
- BlockEstimates:
  `cb676968af927df6a6c7f8244b3ad0ce2241d4022ead2496d26aa901adc58d85`.

Supporting files are `pole-spacing-review-compile.log`,
`block-estimates-review-compile.log`, `SpacingBlockAudit.lean`, and
`spacing-block-audit.log` in `<historical-workspace>/scratch/uniform`.
