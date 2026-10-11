# Milestone 1: complete mathematical proof

The complete mathematical proof was written and independently checked before
Lean theorem formalization began. See `docs/mathematical-proof.md`.

The approximation hypothesis is explicit and is not proved. The nearest odd
denominator is `2 * floor(n / π) + 1`. The proof gives the eventual bound
`|tan(n)| ≤ π q^(ν-1) ≤ π (2n)^(ν-1)`.

At exponent 3 this proves the limit by comparison with `4π/n`. At exponent
5/2 it proves summability by comparison with `π 2^(3/2) n^(-3/2)`.

Lean 4.19.0 and mathlib v4.19.0 have been selected. Compiler installation has
succeeded; mathlib dependency setup is in progress. Source formalization is
starting. No compiled theorem is claimed at this milestone.

Files preserved: mathematical proof, intended theorem statements, explicit
hypothesis source, setup logs, pinned toolchain and Lake configuration.
