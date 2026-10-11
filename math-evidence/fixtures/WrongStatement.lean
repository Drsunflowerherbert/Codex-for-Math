import Mathlib
namespace ReceiptFixture
theorem valid : (1 : Nat) + 1 = 2 := by decide
-- A future type-matching harness must reject this expected type.
example : (1 : Nat) + 1 = 3 := valid
end ReceiptFixture
