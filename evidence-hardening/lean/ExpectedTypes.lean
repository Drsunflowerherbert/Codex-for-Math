import Fixture
import EvidenceHarness
#evidence_check EvidenceFixture.valid : (1 : Nat) + 1 = 2
#evidence_check EvidenceFixture.identity : ∀ {n : Nat}, n = 2 → n = 2
-- Named predicate equality alone is intentionally insufficient: body gate follows.
#evidence_check EvidenceFixture.conditional : EvidenceFixture.predicate → EvidenceFixture.predicate
#evidence_check EvidenceFixture.predicate : Prop
#evidence_check EvidenceFixture.answer : Nat
