"""Create reviewed copies and independently check arithmetic using local stdlib only.

No source manuscript code or original record builder is executed.
Original artifacts are read but never modified.
"""

from copy import deepcopy
from fractions import Fraction
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORIGINAL = ROOT.parent.parent / "affine-avoidance"
CATALOG = ROOT.parent.parent / "catalog" / "sources"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


expected_hashes = {
    "02-periodic.tex": "495a0aad88677e2e61904cf5fe029b709033d0830f7c98d386661632abc8bdb8",
    "research-notes.txt": "2120829c854d12889b1c95b349e3b0d3fe91d7e10ec74529b35c7d4036d2c76a",
    "mrs-provisional-records.json": "8c20c775de9fc6b19392843ee4adaf74fb3e7bf06b6af0a9293a883a128582fe",
    "verification.json": "0fb3db92107b00e62aae7db194966272fc50d9963c821b268a8c728eecc4d175",
}
before_hashes = {name: sha(ORIGINAL / name) for name in expected_hashes}
assert before_hashes == expected_hashes, "Reviewed inputs changed; review must be reconciled."

notes = (ORIGINAL / "research-notes.txt").read_text()
edits = [
    (
        "Independent elementary proof and reusable records\nFamily 084 supporting lemma, reviewed 2026-10-11 UTC",
        "Independent elementary proof and reusable records\nFamily 084 supporting lemma, independently reviewed and corrected 2026-10-11 UTC",
    ),
    (
        "The repository’s family 084 Lean badge has dyadic-manuscript scope, rather than covering the newer all-ratios manuscript. The present proof has been self-checked; separate independent reviewer approval remains pending.",
        "The saved family 084 Lean scope document describes the dyadic manuscript, rather than claiming verification of the newer all-ratios manuscript. The present conditional proof has completed a separate ordinary mathematical review. One sentence about distinctness was corrected; the core theorem and its constants were accepted. This is not formal verification.",
    ),
    ("Local original: 02-periodic.tex", "Local original: ../../affine-avoidance/02-periodic.tex"),
    (
        "• Nullness, strict monotonicity, positivity, distinctness, and geometric form are not used by the reduction. The fixed sequence can be arbitrary if the stated normalized hitting condition holds. Distinctness becomes necessary indirectly for compatibility with arbitrarily small density, as the finite-range lemma shows.",
        "• Nullness, strict monotonicity, positivity, pairwise distinctness, and geometric form are not used by the reduction. The fixed sequence can be arbitrary if the stated normalized hitting condition holds. The finite-range lemma forces infinitely many distinct values, not pairwise distinct terms: repeating every term preserves all hitting and avoidance assertions. More strongly, for each fixed t∈[1,2), the set {t a_n modulo 1:n≥1} must be infinite, since finitely many residues would force a positive density lower bound by the same finite-union argument.",
    ),
    (
        "Independent reviewer status: pending.",
        "Independent reviewer status: completed ordinary mathematical review, core proof accepted, distinctness wording corrected. See independent-review.txt. No theorem prover was run.",
    ),
]
for old, new in edits:
    assert notes.count(old) == 1, f"Missing or ambiguous notes replacement: {old}"
    notes = notes.replace(old, new)
notes += """

9. INDEPENDENT REVIEW CLARIFICATIONS

This reviewed copy is accompanied by independent-review.txt and independent-verification.json. The originals remain unchanged. The source statement and all five reusable proofs were accepted as ordinary mathematics, conditional on the normalized hitting hypothesis. The record limitation about failed geometric budgets now explicitly applies to positive bases 0<r≤2; the lemma itself still assumes r>2.

The source bound 7η/16 bounds removed measure; it does not claim equality of that measure. The exact coefficient in the generalized construction is 7C/(24 max(1,C)); 7/24 is the uniform upper coefficient after using C/max(1,C)≤1. All uses of the normalized hypothesis have 0<p_k<1 for the stated 0<η<1 range. The saved source section references a main theorem whose statement is not included in that section; no broader parameter domain is inferred from that reference.

Concrete check on omitted assumptions. Let (b_n) enumerate the rationals in (0,1), and define a_(2n−1)=a_(2n)=b_n. For p∈(0,1), the open 1-periodic set H_p=⋃_{j∈ℤ}(j,j+p) has density p. For y∈ℝ and t≥1, the interval (y,y+t) meets H_p in a nonempty open set, and {y+t b_n:n≥1} is dense in that interval. Hence H_p hits the normalized copy. This bounded sequence has repetitions and does not tend to zero, yet satisfies the hypothesis with C=1. The example does not construct hitting sets for an arbitrary null sequence or for the geometric sequence in the source.

The catalog copy of 02-periodic.tex has one extra trailing blank line compared with the exact source reviewed here. No mathematical content differs. The recorded commit was not freshly authenticated over the network during this local review.
"""
(ROOT / "research-notes.reviewed.txt").write_text(notes)

original_records = json.loads((ORIGINAL / "mrs-provisional-records.json").read_text())
reviewed = deepcopy(original_records)
reviewed["reviewed_utc"] = "2026-10-11"
reviewed["review_status"] = "ordinary_proof_passed_with_clarifications"
reviewed["original_artifact"] = "../../affine-avoidance/mrs-provisional-records.json"
reviewed["independent_review_artifact"] = "independent-review.txt"
reviewed["source_metadata"]["local_file"] = "../../affine-avoidance/02-periodic.tex"
reviewed["source_metadata"]["source_authentication_scope"] = (
    "Saved bytes and recorded hash checked; no fresh network authentication of commit."
)

version_map = {r["record_id"]: r["record_id"].removesuffix(".v1") + ".v2"
               for r in reviewed["records"]}
for record in reviewed["records"]:
    old_id = record["record_id"]
    record["supersedes_record_id"] = old_id
    record["record_id"] = version_map[old_id]
    record["record_version"] = 2
    record["artifact"] = "research-notes.reviewed.txt"
    record["dependencies"] = [version_map[d] for d in record["dependencies"]]
    record["verification"] = {
        "proof_status": "ordinary_mathematical_proof_independently_reviewed",
        "independent_review_status": "completed",
        "independent_review_artifact": "independent-review.txt",
        "formal_verification_status": "not_performed",
        "lean_claim": (
            "No Lean execution or new formal verification. The saved scope document "
            "describes the dyadic manuscript, not verification of the newer all-ratios manuscript."
        ),
        "lean_scope_url": original_records["source_metadata"]["lean_scope_url"],
    }
    if old_id.endswith("dyadic_budget.v1"):
        old = "At r≤2 the positive-scale majorant diverges; this does not prove that the actual union has large measure."
        assert old in record["limitations"]
        record["limitations"][record["limitations"].index(old)] = (
            "For positive budget bases 0<r≤2, the positive-scale majorant diverges; "
            "this does not prove that the actual union has large measure."
        )
    if old_id.endswith("finite_range_obstruction.v1"):
        record["conclusion"].append(
            "The arbitrarily-small-density hypothesis forces infinitely many distinct values; "
            "it does not force pairwise distinct terms. Repetitions do not change the range."
        )
        record["proof"].append(
            "Repeating any sequence term leaves its range, all translated-dilated ranges, "
            "and every hitting assertion unchanged. Thus finite range and repeated terms are different issues."
        )
    if old_id.endswith("normalized_to_global.v1"):
        record["source_specialization"]["tolerance_range_checked"] = "η∈(0,1)"
        record["limitations"].append(
            "The saved source section does not include the statement of its referenced main theorem; "
            "this review checks the η∈(0,1) domain stated in the generalized theorem."
        )

reviewed["review_log"][-1] = {
    "reviewer": "independent_mathematical_reviewer",
    "reviewed_utc": "2026-10-11",
    "scope": (
        "Exact saved source statement, quantifiers, period/scaling estimate, budgets, signs, "
        "endpoints, compactness, finite-range obstruction, omitted assumptions, safe extensions, "
        "all five record statements and proofs."
    ),
    "status": "passed_ordinary_proof_review_with_notes_correction_and_domain_clarification",
    "report": "independent-review.txt",
    "formal_verification": False,
    "normalized_hitting_construction_verified": False,
}
record_file = ROOT / "mrs-provisional-records.reviewed.json"
record_file.write_text(json.dumps(reviewed, ensure_ascii=False, indent=2) + "\n")

# Independently recompute the exact constants. Infinite sums are justified by
# the proof, not by finite sampling; these checks evaluate their closed forms.
sum4 = Fraction(1, 4 - 1) + 1 + Fraction(2, 4 - 2)
source_coeff = 2 * 6 * Fraction(1, 64) * sum4
uniform_general_coeff = 2 * Fraction(1, 16) * sum4
assert sum4 == Fraction(7, 3)
assert source_coeff == Fraction(7, 16)
assert uniform_general_coeff == Fraction(7, 24)
assert uniform_general_coeff + Fraction(1, 2) == Fraction(19, 24) < 1

original_verification = json.loads((ORIGINAL / "verification.json").read_text())
assert Fraction(original_verification["sum4"]) == sum4
assert Fraction(original_verification["source_coefficient"]) == source_coeff
assert Fraction(original_verification["general_coefficient"]) == uniform_general_coeff

for sample in original_verification["normalization_samples"]:
    x, s = Fraction(sample["x"]), Fraction(sample["s"])
    k, t, y = sample["k"], Fraction(sample["t"]), Fraction(sample["y"])
    L = Fraction(2) ** k
    sigma = 1 if s > 0 else -1
    assert s != 0 and L <= abs(s) < 2 * L
    assert t == abs(s) / L and 1 <= t < 2
    assert y == sigma * x / L
    # Two coefficients suffice for equality of these affine polynomials in a.
    assert sigma * L * y == x
    assert sigma * L * t == s

general_parameter_checks = []
for C in (Fraction(1, 10), Fraction(1), Fraction(6), Fraction(100)):
    B = max(Fraction(1), C)
    exact_coefficient = Fraction(7) * C / (24 * B)
    assert exact_coefficient <= Fraction(7, 24)
    general_parameter_checks.append({"C": str(C), "B": str(B),
                                     "exact_removed_measure_coefficient": str(exact_coefficient)})
    for eta in (Fraction(1, 1000), Fraction(1, 2), Fraction(999, 1000)):
        for k in range(-12, 13):
            p = eta * Fraction(4) ** (-abs(k)) / (16 * B)
            assert 0 < p < 1

reloaded = json.loads(record_file.read_text())
ids = [r["record_id"] for r in reloaded["records"]]
assert len(ids) == len(set(ids)) == 5
assert all(d in ids for r in reloaded["records"] for d in r["dependencies"])
assert all(r["record_version"] == 2 for r in reloaded["records"])
assert all(r["verification"]["formal_verification_status"] == "not_performed"
           for r in reloaded["records"])
assert reloaded["native_mrs_imported"] is False
assert reloaded["native_mrs_compatible"] is None

catalog_source = CATALOG / (
    "preprints_The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026_"
    "build_sections_02-periodic.tex"
)
assert catalog_source.read_bytes() == (ORIGINAL / "02-periodic.tex").read_bytes() + b"\n"
after_hashes = {name: sha(ORIGINAL / name) for name in expected_hashes}
assert after_hashes == before_hashes

verification = {
    "review_date_utc": "2026-10-11",
    "ordinary_proof_review_status": "passed_with_notes_correction_and_domain_clarification",
    "computation_status": "passed_exact_arithmetic_and_structural_checks",
    "formal_verification": False,
    "lean_executed": False,
    "native_mrs_schema_validated": False,
    "native_mrs_imported": False,
    "normalized_hitting_construction_verified": False,
    "whole_geometric_manuscript_audited": False,
    "external_code_executed": False,
    "software_installed": False,
    "originals_preserved": before_hashes == after_hashes,
    "input_sha256": before_hashes,
    "reviewed_source_bytes": (ORIGINAL / "02-periodic.tex").stat().st_size,
    "catalog_source_difference": "One extra trailing newline only; exact byte relation verified.",
    "source_network_authentication_performed": False,
    "saved_lean_scope_sha256": sha(CATALOG / "lean_docs_084.md"),
    "corrections": [
        {"location": "research-notes.txt section 7 first bullet",
         "before": "Distinctness becomes necessary indirectly for compatibility with arbitrarily small density.",
         "after": "Infinitely many distinct values are necessary; pairwise distinct terms are not.",
         "effect": "Notes correction; the five original record theorem statements remain valid."},
        {"location": "dyadic_budget record limitation",
         "before": "At r≤2 the positive-scale majorant diverges.",
         "after": "For positive bases 0<r≤2 the positive-scale majorant diverges.",
         "effect": "Domain clarification for a limitation; the lemma already assumes r>2."},
        {"location": "verification.json general_coefficient",
         "before": "7/24",
         "after": "Exact coefficient is (7/24) C/max(1,C); 7/24 is the uniform upper coefficient.",
         "effect": "Metadata clarification; the original research proof already states the correct dependence."},
    ],
    "constants": {"dyadic_sum": str(sum4), "source_removed_measure_coefficient": str(source_coeff),
                  "general_exact_removed_measure_coefficient": "7*C/(24*max(1,C))",
                  "general_uniform_removed_measure_coefficient": str(uniform_general_coeff),
                  "measurable_extension_uniform_loss_coefficient": "19/24"},
    "original_normalization_samples_rechecked": len(original_verification["normalization_samples"]),
    "normalization_sample_method": "Exact rational coefficients of the affine identity, with dyadic range checks.",
    "general_parameter_checks": general_parameter_checks,
    "record_count": len(ids),
    "all_dependencies_resolve": True,
    "all_record_ids_unique": True,
    "report": "independent-review.txt",
    "reviewed_notes": "research-notes.reviewed.txt",
    "reviewed_records": "mrs-provisional-records.reviewed.json",
    "output_sha256": {name: sha(ROOT / name) for name in
                      ("independent-review.txt", "research-notes.reviewed.txt",
                       "mrs-provisional-records.reviewed.json", "audit_records.py")},
}
(ROOT / "independent-verification.json").write_text(
    json.dumps(verification, ensure_ascii=False, indent=2) + "\n"
)
print(json.dumps({"ordinary_proof_review": verification["ordinary_proof_review_status"],
                  "record_count": len(ids), "normalization_samples_rechecked": 21,
                  "originals_preserved": True, "formal_verification": False}))
