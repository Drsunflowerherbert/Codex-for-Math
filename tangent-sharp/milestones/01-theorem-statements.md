# Requested statements and planned reusable lemmas

The hypothesis remains a named proposition and an explicit argument:

```lean
def PiDiophantine : Prop :=
  ∀ ν : ℝ, 2 < ν → ∃ Q : ℕ, ∀ q : ℕ, Q ≤ q → 0 < q →
    ∀ p : ℤ, (q : ℝ) ^ (-ν) ≤ |Real.pi - (p : ℝ) / (q : ℝ)|
```

Requested limit (natural indexing has a harmless zero term):

```lean
theorem tan_div_cube_tendsto_zero (h : PiDiophantine) :
  Filter.Tendsto (fun n : ℕ => Real.tan (n : ℝ) / (n : ℝ)^3)
    Filter.atTop (nhds 0)
```

Positive-integer indexing will also be supplied by `n + 1`.

Extension to be attempted after the main theorem compiles:

```lean
theorem summable_abs_tan_div_cube (h : PiDiophantine) :
  Summable (fun n : ℕ => |Real.tan (n : ℝ)| / (n : ℝ)^3)
```

Reusable lemmas cover the nearest positive odd denominator, its linear upper
bound and divergence, distance to a tangent pole, the sine chord estimate,
and conversion of the hypothesis to an eventual tangent bound.

These are target statements, not a claim that they already compile. The final
compiler-generated statement and axiom inventory will be saved separately.
