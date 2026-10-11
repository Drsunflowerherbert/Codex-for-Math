"""Validate supplement links, record preservation and finite coarse bounds.

Uses only the standard library. Does not import or execute repository code.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
REVIEW = ROOT.parent
SOURCE = ROOT.parents[2] / "egyptian-fractions"

def require(value, detail):
    if not value:
        raise ValueError(detail)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read_json(path):
    return json.loads(path.read_text())

def existing(relative):
    require((ROOT / relative).is_file(), ("missing linked file", relative))
    return relative

def main():
    original_hashes = {}
    for line in (REVIEW / "original-sha256-before.txt").read_text().splitlines():
        expected, filename = line.split("  ", 1)
        p = Path(filename)
        require(digest(p) == expected, ("original changed", p.name))
        original_hashes[p.name] = expected
    old = read_json(SOURCE / "theorem-records.json")
    new = read_json(ROOT / "theorem-records.json")
    previous_review = read_json(REVIEW / "review-records.json")
    review_ids = {r["id"]: r for r in previous_review["records"]}
    require(len(old) == len(new) == 6, "six original records expected")
    unchanged_keys = ["schema", "native_mrs_imported", "source_revision", "lean_status",
                      "novelty_claim", "id", "title", "hypotheses", "conclusion", "dependencies"]
    record_links = set()
    for source, replacement in zip(old, new):
        for key in unchanged_keys:
            require(source[key] == replacement[key], ("changed theorem field", source["id"], key))
        require(replacement["ordinary_proof_status"] == "author_checked", "author status")
        require(replacement["ordinary_proof_review_status"] == "independently_reviewed_pass",
                "review status")
        provenance = replacement["original_record_provenance"]
        require(provenance["ordinary_proof_status"] == source["ordinary_proof_status"],
                "original author status provenance")
        require(provenance["file_sha256"] == original_hashes["theorem-records.json"],
                "original records hash provenance")
        require(provenance["record_id"] == replacement["id"], "original record ID")
        evidence = replacement["review_evidence"]
        require(evidence["record_id"] == replacement["id"]
                and review_ids[replacement["id"]]["ordinary_proof_review_status"]
                == replacement["ordinary_proof_review_status"], "linked status mismatch")
        for field in [replacement["proof_file"], provenance["file"], evidence["file"],
                      evidence["report"], evidence["audit_results"]] + replacement["verification_evidence"]:
            record_links.add(existing(field))
    original_text = (SOURCE / "study.md").read_text()
    corrected_text = (ROOT / "study.md").read_text()
    for heading, end_marker in [
        ("## 2 Removing repetitions with no length cost", "## 3 Padding while retaining a specified denominator"),
        ("## 3 Padding while retaining a specified denominator", "Iteration retains m")
    ]:
        old_proof = original_text.split(heading, 1)[1].split(end_marker, 1)[0]
        new_proof = corrected_text.split(heading, 1)[1].split(end_marker, 1)[0]
        require(old_proof == new_proof, ("original proof altered", heading))
    require(original_text.split("Proof. For k=1", 1)[1].split("The proof gives", 1)[0]
            == corrected_text.split("Proof. For k=1", 1)[1].split("For a positive rational x", 1)[0],
            "original finiteness proof altered")
    cert = read_json(SOURCE / "exact-examples.json")
    cases = cert["padding_cases"] + cert["exceptional_composite_cases"]
    equality_cases = 0
    for case in cases:
        M, next_M = max(case["input"]), max(case["output"])
        require(next_M <= M * (M + 1), ("coarse one-step bound", case))
        equality_cases += next_M == M * (M + 1)
    require(len(cases) == 14308, "finite coverage count")

    result = {
        "schema": "egyptian-corrected-supplement-validation-v1",
        "review_date_utc": "2026-10-11",
        "six_original_theorem_statements_and_dependencies_unchanged": True,
        "original_finiteness_cleanup_and_one_step_padding_proofs_unchanged": True,
        "original_author_statuses_preserved_in_provenance": True,
        "separate_independent_review_statuses_linked": True,
        "all_original_files_unchanged": True,
        "one_step_bound_cases_checked": len(cases),
        "one_step_bound_equality_cases": equality_cases,
        "arbitrary_iteration_computation_claimed": False,
        "optional_corollaries_have_separate_ordinary_proofs": True,
        "optional_corollaries_separately_independently_reviewed": False,
        "lean_verification_performed": False,
        "native_mrs_import_performed": False,
        "all_checks_passed": True,
    }
    result_path = ROOT / "validation-results.json"
    result_path.write_text(json.dumps(result, indent=2) + "\n")
    corollaries = read_json(ROOT / "coarse-padding-bound-records.json")
    require([r["id"] for r in corollaries] == ["EGY-COR-001", "EGY-COR-002"], "corollary IDs")
    for record in corollaries:
        require(record["ordinary_proof_status"] == "proved_in_review_supplement"
                and record["independent_review_status"] == "not_separately_reviewed"
                and record["lean_status"] == "not_run", "corollary evidence status")
        for field in [record["proof_file"], record["dependency_records_file"]] + record["verification_evidence"]:
            record_links.add(existing(field))
        dependency_ids = {r["id"] for r in read_json(ROOT / record["dependency_records_file"])}
        require(set(record["dependencies"]) <= dependency_ids, "unresolved corollary dependency")
    markdown_links = set()
    for p in ROOT.glob("*.md"):
        for link in re.findall(r"\]\(([^)]+)\)", p.read_text()):
            if link.startswith(("https://", "http://")):
                continue
            markdown_links.add(existing(link))
    result["local_record_file_links_verified"] = len(record_links)
    result["local_markdown_file_links_verified"] = len(markdown_links)
    result_path.write_text(json.dumps(result, indent=2) + "\n")

    files = ["README.md", "study.md", "theorem-records.json", "coarse-padding-bounds.md",
             "coarse-padding-bound-records.json", "validation-results.json", "validate_supplement.py"]
    linked_review_files = ["../review.md", "../review-records.json", "../independent-audit-results.json",
                           "../independent_audit.py", "../proposed-revisions.md"]
    manifest = {
        "schema": "egyptian-corrected-supplement-manifest-v1",
        "review_date_utc": "2026-10-11",
        "source_revision": cert["source_revision"],
        "hash_algorithm": "SHA-256",
        "path_base": "reviews/egyptian/corrected",
        "corrected_artifacts": {f: digest(ROOT / f) for f in files},
        "linked_review_evidence": {f: digest(ROOT / f) for f in linked_review_files},
        "preserved_original_files": {"../../../egyptian-fractions/" + f: h
                                     for f, h in original_hashes.items()},
        "self_hash_note": "This manifest omits its own hash; the exact manifest hash is supplied with delivery.",
    }
    manifest_path = ROOT / "supplement-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"validation": result, "corrected_artifact_hashes": manifest["corrected_artifacts"],
                      "supplement_manifest_sha256": digest(manifest_path)}, indent=2))

if __name__ == "__main__":
    main()
