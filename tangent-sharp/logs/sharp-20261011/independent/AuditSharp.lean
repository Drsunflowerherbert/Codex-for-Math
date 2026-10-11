import TangentLimit

-- Independent consumer check of the exact final public statements.
#print TangentLimit.PiDiophantine
#check TangentLimit.summable_abs_tan_div_rpow
#check TangentLimit.summable_abs_tan_div_rpow_positive
#check TangentLimit.summable_abs_tan_div_rpow_positive_iff
#check TangentLimit.not_summable_abs_tan_div_positive
#check TangentLimit.not_summable_abs_tan_div_rpow_positive
#print axioms TangentLimit.PiDiophantine
#print axioms TangentLimit.summable_abs_tan_div_rpow
#print axioms TangentLimit.summable_abs_tan_div_rpow_positive
#print axioms TangentLimit.summable_abs_tan_div_rpow_positive_iff
#print axioms TangentLimit.not_summable_abs_tan_div_positive
#print axioms TangentLimit.not_summable_abs_tan_div_rpow_positive

-- These elaborated consumer statements also exclude hidden mathematical inputs.
example (h : TangentLimit.PiDiophantine) (s : ℝ) (hs : 1 < s) :
    Summable (fun n : ℕ => |Real.tan ((n + 1 : ℕ) : ℝ)| /
      (((n + 1 : ℕ) : ℝ) ^ s)) :=
  TangentLimit.summable_abs_tan_div_rpow_positive h s hs

example (h : TangentLimit.PiDiophantine) (s : ℝ) :
    Summable (fun n : ℕ => |Real.tan ((n + 1 : ℕ) : ℝ)| /
      (((n + 1 : ℕ) : ℝ) ^ s)) ↔ 1 < s :=
  TangentLimit.summable_abs_tan_div_rpow_positive_iff h s

example (s : ℝ) (hs : s ≤ 1) :
    ¬ Summable (fun n : ℕ => |Real.tan ((n + 1 : ℕ) : ℝ)| /
      (((n + 1 : ℕ) : ℝ) ^ s)) :=
  TangentLimit.not_summable_abs_tan_div_rpow_positive s hs
