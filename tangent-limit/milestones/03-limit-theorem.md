# Milestone 3: requested limit compiled

`lake build TangentLimit.Limit` passed cleanly with Lean 4.24.0 and mathlib
commit `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.

The explicit hypothesis `PiDiophantine` remains an argument in both theorems:

```lean
theorem tan_div_cube_tendsto_zero (h : PiDiophantine) :
  Tendsto (fun n : ℕ => Real.tan (n : ℝ) / (n : ℝ)^3)
    atTop (nhds 0)

theorem tan_div_cube_positive_tendsto_zero (h : PiDiophantine) :
  Tendsto (fun n : ℕ => Real.tan ((n + 1 : ℕ) : ℝ) /
    ((n + 1 : ℕ) : ℝ)^3) atTop (nhds 0)
```

The main theorem uses only the exponent-three instance of the hypothesis.
Its eventual quadratic growth estimate is proved through the nearest odd
denominator and yields the bound `|tan(n)/n³| ≤ 4π/n`.

Build evidence: `logs/limit-01.log`.
Compiler statements and axiom inventory: `logs/milestone-03-theorem-inventory.log`.
No placeholder proofs or added axioms are used. The theorem inventory lists
only standard foundational Lean axioms.

The absolute-convergence extension starts after this passing milestone, as
requested. It will use the existing exponent-general estimate at exponent 5/2.
