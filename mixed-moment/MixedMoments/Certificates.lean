import MixedMoments.Cancellation

/-! Exact rational regression certificates checked by the Lean kernel.
Generated from the independent certificate implementation. No floating point
or substitutions for the real constants occur. These are finite formal-array
equalities, not statements about unevaluated integrals. -/

namespace MixedMoments.Certificates

open MixedMoments

theorem m_0_0 : formalM 0 0 = Coordinates.mk (0) (4) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_0_1 : formalM 0 1 = Coordinates.mk (0) (0) (3/2) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_0_2 : formalM 0 2 = Coordinates.mk (2) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_0_3 : formalM 0 3 = Coordinates.mk (1/2) (0) (3/4) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_0_4 : formalM 0 4 = Coordinates.mk (14/9) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_0_5 : formalM 0 5 = Coordinates.mk (1/2) (0) (9/16) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_1_0 : formalM 1 0 = Coordinates.mk (2) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_1_1 : formalM 1 1 = Coordinates.mk (-2) (4) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_1_2 : formalM 1 2 = Coordinates.mk (-1) (0) (3/2) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_1_3 : formalM 1 3 = Coordinates.mk (4/3) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_1_4 : formalM 1 4 = Coordinates.mk (0) (0) (3/4) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_1_5 : formalM 1 5 = Coordinates.mk (52/45) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_2_0 : formalM 2 0 = Coordinates.mk (1) (2) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_2_1 : formalM 2 1 = Coordinates.mk (2) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_2_2 : formalM 2 2 = Coordinates.mk (-2) (4) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_2_3 : formalM 2 3 = Coordinates.mk (-1) (0) (3/2) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_2_4 : formalM 2 4 = Coordinates.mk (4/3) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_2_5 : formalM 2 5 = Coordinates.mk (0) (0) (3/4) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_3_0 : formalM 3 0 = Coordinates.mk (16/9) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_3_1 : formalM 3 1 = Coordinates.mk (-1/3) (2) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_3_2 : formalM 3 2 = Coordinates.mk (4/3) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_3_3 : formalM 3 3 = Coordinates.mk (-22/9) (4) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_3_4 : formalM 3 4 = Coordinates.mk (-4/3) (0) (3/2) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_3_5 : formalM 3 5 = Coordinates.mk (16/15) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_4_0 : formalM 4 0 = Coordinates.mk (13/12) (3/2) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_4_1 : formalM 4 1 = Coordinates.mk (16/9) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_4_2 : formalM 4 2 = Coordinates.mk (-1/3) (2) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_4_3 : formalM 4 3 = Coordinates.mk (4/3) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_4_4 : formalM 4 4 = Coordinates.mk (-22/9) (4) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_4_5 : formalM 4 5 = Coordinates.mk (-4/3) (0) (3/2) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_5_0 : formalM 5 0 = Coordinates.mk (368/225) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_5_1 : formalM 5 1 = Coordinates.mk (1/60) (3/2) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_5_2 : formalM 5 2 = Coordinates.mk (56/45) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_5_3 : formalM 5 3 = Coordinates.mk (-31/45) (2) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_5_4 : formalM 5 4 = Coordinates.mk (16/15) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem m_5_5 : formalM 5 5 = Coordinates.mk (-598/225) (4) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_0_0 : formalZ 0 0 = Coordinates.mk (0) (0) (1) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_0_1 : formalZ 0 1 = Coordinates.mk (1) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_0_2 : formalZ 0 2 = Coordinates.mk (3/4) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_0_3 : formalZ 0 3 = Coordinates.mk (11/18) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_0_4 : formalZ 0 4 = Coordinates.mk (25/48) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_0_5 : formalZ 0 5 = Coordinates.mk (137/300) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_1_0 : formalZ 1 0 = Coordinates.mk (1) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_1_1 : formalZ 1 1 = Coordinates.mk (-1) (0) (1) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_1_2 : formalZ 1 2 = Coordinates.mk (1/2) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_1_3 : formalZ 1 3 = Coordinates.mk (5/12) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_1_4 : formalZ 1 4 = Coordinates.mk (13/36) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_1_5 : formalZ 1 5 = Coordinates.mk (77/240) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_2_0 : formalZ 2 0 = Coordinates.mk (3/4) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_2_1 : formalZ 2 1 = Coordinates.mk (1/2) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_2_2 : formalZ 2 2 = Coordinates.mk (-5/4) (0) (1) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_2_3 : formalZ 2 3 = Coordinates.mk (1/3) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_2_4 : formalZ 2 4 = Coordinates.mk (7/24) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_2_5 : formalZ 2 5 = Coordinates.mk (47/180) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_3_0 : formalZ 3 0 = Coordinates.mk (11/18) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_3_1 : formalZ 3 1 = Coordinates.mk (5/12) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_3_2 : formalZ 3 2 = Coordinates.mk (1/3) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_3_3 : formalZ 3 3 = Coordinates.mk (-49/36) (0) (1) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_3_4 : formalZ 3 4 = Coordinates.mk (1/4) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_3_5 : formalZ 3 5 = Coordinates.mk (9/40) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_4_0 : formalZ 4 0 = Coordinates.mk (25/48) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_4_1 : formalZ 4 1 = Coordinates.mk (13/36) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_4_2 : formalZ 4 2 = Coordinates.mk (7/24) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_4_3 : formalZ 4 3 = Coordinates.mk (1/4) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_4_4 : formalZ 4 4 = Coordinates.mk (-205/144) (0) (1) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_4_5 : formalZ 4 5 = Coordinates.mk (1/5) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_5_0 : formalZ 5 0 = Coordinates.mk (137/300) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_5_1 : formalZ 5 1 = Coordinates.mk (77/240) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_5_2 : formalZ 5 2 = Coordinates.mk (47/180) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_5_3 : formalZ 5 3 = Coordinates.mk (9/40) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_5_4 : formalZ 5 4 = Coordinates.mk (1/5) (0) (0) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem z_5_5 : formalZ 5 5 = Coordinates.mk (-5269/3600) (0) (1) := by
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem one_x_0 : formalEntry 1 Polynomial.X 0 = Coordinates.mk (-3/2) (4) (0) := by
  rw [formalEntry_one_X]
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem one_x_1 : formalEntry 1 Polynomial.X 1 = Coordinates.mk (3/2) (0) (0) := by
  rw [formalEntry_one_X]
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem one_x_2 : formalEntry 1 Polynomial.X 2 = Coordinates.mk (5/4) (0) (0) := by
  rw [formalEntry_one_X]
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem one_x_3 : formalEntry 1 Polynomial.X 3 = Coordinates.mk (-1/8) (0) (3/4) := by
  rw [formalEntry_one_X]
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

theorem one_x_4 : formalEntry 1 Polynomial.X 4 = Coordinates.mk (73/72) (0) (0) := by
  rw [formalEntry_one_X]
  ext k
  fin_cases k <;> norm_num [formalM, formalZ, Coordinates.mk, mRationalPart,
    zRationalPart, kminus, kplus, moment, central, kernel, Int.toNat, harmonic, harmonicTwo,
    Finset.sum_range_succ]

end MixedMoments.Certificates
