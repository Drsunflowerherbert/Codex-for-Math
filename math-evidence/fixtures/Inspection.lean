import Mathlib
namespace ReceiptFixture
theorem valid : (1 : Nat) + 1 = 2 := by decide
theorem incomplete : False := by sorry
#print valid
#print axioms valid
#print incomplete
#print axioms incomplete
end ReceiptFixture
