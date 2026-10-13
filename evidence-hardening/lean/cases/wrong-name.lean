import Dependency
namespace Hidden
def predicate : Prop := False
def answer : Nat := EvidenceFixture.bound
theorem valid : (1 : Nat) + 1 = 2 := by decide
theorem identity {n : Nat} (h : n = 2) : n = 2 := h
theorem conditional (h : predicate) : predicate := h
end Hidden
