import Dependency
namespace EvidenceFixture
def predicate : Prop := False
def answer : Nat := bound
theorem valid : (1 : Nat) + 1 = 2 := by decide
section
variable (hidden : False)
include hidden
theorem identity {n : Nat} (h : n = 2) : n = 2 := False.elim hidden
end
theorem conditional (h : predicate) : predicate := h
end EvidenceFixture
