> Historical source review: mathematical statements and verdicts are retained. Quoted hashes identify the original supplied files, which may differ from privacy-normalized public receipts. Original/public hashes are recorded in `publication/SOURCE-MAP.json`; fresh publication checks are separate.

# Rational recurrence core

`MixedMoments/Rational.lean` constructs rational arrays independently of their
analytic interpretation. Every statement in the file is a kernel-checked Lean
proof; the file contains no `sorry`, `admit`, custom axiom, or `native_decide`.

The central sequence starts at one and is defined by
`central (n + 1) = central n * (2*n + 1) / (2*n + 2)` over `ℚ`.
`central_eq_choose` identifies it with the normalized central binomial
coefficient `(Nat.choose (2*n) n : ℚ) / 4^n`; `central_pos` proves that all
terms, and therefore all central denominators used below, are nonzero.
`central_le_one` also establishes the coefficient bound used in geometric
majorants for the generating series.

`kernel : ℤ → ℚ` keeps index differences in the integers. It is zero for
negative and odd inputs, and `kernel (2*n) = central n` for natural `n`.
`kernel_step` and `kernel_shifted_step` prove the recurrences needed for the
Catalan and zeta coordinates of the boundary arrays. The shifted recurrence
includes natural index zero, where the right side explicitly uses the negative
input `kernel (-1)`.

`moment` starts at `2, 0` and obeys the rational two-step recurrence.
`moment_even`, `moment_odd`, and `moment_eq_if` prove the parity formulas from
the study. `momentExt` explicitly extends moments by zero to negative integers;
the only negative index used by `moment_recurrence_positive` is `-1`.
`moment_nonneg`, `moment_step_le`, and `moment_le_two` establish elementary
bounds, and `moment_sq_le` gives the stronger bound
`moment n ^ 2 ≤ 8 / ((n : ℚ) + 2)` that yields decay after a real cast.
`moment_telescope_step` and `moment_finite_telescope` prove finite
telescoping identities without any convergence or limit assumption.

`kminus` and `kplus` are the exact rational boundary parts from
`certificates.py`. Their starts are respectively `0, 2` and `0, 0`.
`kminus_recurrence` and `kplus_recurrence` quantify their defining recurrences
after clearing the nonzero rational denominator. The plus recurrence is
indexed by `n + 2`, so it includes the index-two start without dividing by zero.

`hStar` is the positive homogeneous normalization of the two-step boundary
recurrence. `hStar_even` and `hStar_odd` identify its two parity formulas.
`kminus_even_closed`, `kminus_odd_closed`, `kplus_even_closed`, and
`kplus_odd_closed` prove the study's finite boundary sums by parity induction.
The plus odd formula includes the empty sum at index one. The plus even formula
starts at index two; index zero retains its separate zero start.

`mRationalPart i j` is the finite diagonal reduction of these boundaries. Its
branch condition protects each natural subtraction: `i - j` occurs only when
`j ≤ i`, and `j - i` occurs only in the complementary branch. In the latter
branch, the study's sum from `j-i+1` through `j` is reindexed as a sum over
`Finset.range i`. The proved identities include both boundary restrictions,
`mRationalPart_diagonal`, and `mRationalPart_finite_diagonal`.
`mRationalPart_adjacent_diagonal` evaluates `mRationalPart (i+1) i` as
`momentExt (i-1) + moment i`, including natural index zero.

`harmonic` and `harmonicTwo` include empty sums and have proved successor
identities. `zRationalPart` uses the difference `(i : ℚ) - (j : ℚ)` in its
off-diagonal denominator; it does not use truncated natural subtraction.
`zRationalPart_symm`, `zRationalPart_diagonal_step`, and
`zRationalPart_finite_diagonal` prove its quantified symmetry and diagonal
identities.

`finite_diagonal_telescope` is a reusable theorem for any rational array
satisfying the stated one-step recurrence. It uses a finite induction and makes
no claim about infinite sums.

These definitions and proofs do not identify arrays with the original real
integrals, evaluate the boundary constants, prove analytic Taylor contact, or
claim independence of `1`, Catalan's constant, and zeta two. Those are separate
obligations in the analytic and cancellation modules.

Validation command from the project directory:

```bash
bash scripts/with-lean.sh lake build MixedMoments.Rational
```

Environment: Lean `4.24.0`, mathlib revision
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.
