import TangentLimit
import EvidenceHarness
open Filter Topology
namespace TangentLimit
#evidence_definition TangentLimit.PiDiophantine =
  ∀ ν : ℝ, 2 < ν → ∃ Q : ℕ, ∀ q : ℕ, Q ≤ q → 0 < q →
    ∀ p : ℤ, (q : ℝ) ^ (-ν) ≤ |Real.pi - (p : ℝ) / (q : ℝ)|
#evidence_definition TangentLimit.poleIndex = fun n : ℕ => Nat.floor ((n : ℝ) / Real.pi)
#evidence_definition TangentLimit.poleDenom = fun n : ℕ => 2 * poleIndex n + 1
#evidence_definition TangentLimit.poleOffset = fun n : ℕ => (n : ℝ) - (poleDenom n : ℝ) * Real.pi / 2
end TangentLimit
