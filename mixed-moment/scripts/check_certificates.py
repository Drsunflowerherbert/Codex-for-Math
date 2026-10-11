#!/usr/bin/env python3
"""Authenticate local supplied bytes, rerun exact checks in scratch, independently check.

No network, third-party packages, or original-source mutations.  The fixed outer
ZIP hash is the hash independently identified for the actual Library archive.
Revision strings in its inner metadata are recorded provenance, not a fresh
authentication of a remote Git revision.  Run from any working directory.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import tempfile
import zipfile

import independent_checks

PROJECT = Path(__file__).resolve().parents[1]
ARCHIVE_NAME = "openai-math-reviewed-supplement-2026-10-11"
ARCHIVE_BYTES = 523782
ARCHIVE_SHA256 = "9e03b1ce33dc5d5fa62ab9478b06998bcb0eb32635fc11bccac065223e892a74"
SOURCE_SHA256 = "3929650dfb36859d8f88281795d348043f903c41a70b0bf3598c21586a633852"
SOURCE_REVISION = "fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb"
SNAPSHOT = "catalog/sources/preprints_Catalans-constant-is-irrational-September-24-2026_build_sections_foundations.tex"
EXPECTED_COUNTS = {
    "fixed_low_index_M": 12, "fixed_low_index_Z": 6,
    "moment_recurrence": 100, "central_binomial_ratio": 100, "H_star_ratio": 100,
    "minus_closed_form": 101, "plus_closed_form": 101,
    "full_minus_boundary_recurrence": 99, "full_plus_boundary_recurrence": 99,
    "M_diagonal_recurrence": 625, "Z_diagonal_recurrence": 625, "Z_symmetry": 625,
    "M_finite_series_telescope": 2500, "Z_finite_series_telescope": 2500,
    "rational_adjacent_diagonal": 100, "polynomial_defect_identity": 40,
    "Taylor_contact_cancellation": 28, "bounded_polynomial_defect_identity": 6480,
    "bounded_polynomial_contact_cancellation": 2916, "contact_perturbation_detected": 648,
}


def digest_bytes(data):
    return hashlib.sha256(data).hexdigest()


def digest(path):
    return digest_bytes(path.read_bytes())


def read_json(path):
    return json.loads(path.read_text())


def safe_relative(name):
    path = PurePosixPath(name)
    if path.is_absolute() or not path.parts or ".." in path.parts or "\\" in name:
        raise AssertionError(f"unsafe archive/manifest path: {name!r}")
    return path


def inventory(directory):
    return {p.relative_to(directory).as_posix(): digest(p)
            for p in sorted(directory.rglob("*")) if p.is_file()}


def run(archive, source):
    audit = independent_checks.Audit()
    before = inventory(source)
    actual_archive_hash = digest(archive)
    audit.equal("archive_size", archive.stat().st_size, ARCHIVE_BYTES)
    audit.equal("archive_hash", actual_archive_hash, ARCHIVE_SHA256)
    archive_entries = {}
    with zipfile.ZipFile(archive) as bundle:
        audit.equal("archive_crc", bundle.testzip(), None)
        for member in bundle.infolist():
            if member.is_dir():
                continue
            path = safe_relative(member.filename)
            audit.equal("archive_root", path.parts[0], ARCHIVE_NAME)
            relative = PurePosixPath(*path.parts[1:]).as_posix()
            audit.check("archive_no_duplicate_path", relative not in archive_entries, relative)
            data = bundle.read(member)
            archive_entries[relative] = digest_bytes(data)
            audit.equal("extracted_file_matches_archive", (source/relative).read_bytes(), data, relative)
    audit.equal("extracted_inventory_matches_archive", before, archive_entries)

    manifest = read_json(source/"MANIFEST-SHA256.json")
    audit.equal("manifest_algorithm", manifest["hash_algorithm"], "SHA-256")
    audit.equal("manifest_self_excluded", manifest["self_excluded"], True)
    manifest_paths = set()
    for item in manifest["files"]:
        relative = str(safe_relative(item["file"]))
        audit.check("manifest_no_duplicate_path", relative not in manifest_paths, relative)
        manifest_paths.add(relative)
        file = source/relative
        audit.equal("manifest_size", file.stat().st_size, item["bytes"], relative)
        audit.equal("manifest_hash", digest(file), item["sha256"], relative)
    audit.equal("manifest_inventory", manifest_paths, set(before)-{"MANIFEST-SHA256.json"})

    verification = read_json(source/"mixed-moments/verification.json")
    saved = read_json(source/"mixed-moments/certificates.json")
    records = read_json(source/"mixed-moments/theorems.json")
    catalog = read_json(source/"catalog/source_manifest.json")
    provenance = read_json(source/"PACKAGE-PROVENANCE.json")
    audit.equal("source_snapshot_hash", digest(source/SNAPSHOT), SOURCE_SHA256)
    for label, value in (("certificate", saved["source_sha256"]),
                         ("verification", verification["source_sha256"]),
                         ("theorem_source", records["source"]["sha256"])):
        audit.equal("metadata_source_hash", value, SOURCE_SHA256, label)
    for label, value in (("certificate", saved["revision"]),
                         ("verification", verification["source_revision"]),
                         ("theorem_source", records["source"]["revision"]),
                         ("catalog", catalog["revision"]),
                         ("package", provenance["upstream_revision"])):
        audit.equal("metadata_revision", value, SOURCE_REVISION, label)
    snapshot_catalog = [x for x in catalog["files"] if x["file"] == Path(SNAPSHOT).name]
    audit.equal("snapshot_catalog_count", len(snapshot_catalog), 1)
    audit.equal("snapshot_catalog_hash", snapshot_catalog[0]["sha256"], SOURCE_SHA256)
    audit.equal("snapshot_catalog_size", snapshot_catalog[0]["bytes"], (source/SNAPSHOT).stat().st_size)
    for item in verification["files"]:
        relative = safe_relative(item["file"])
        file = source/"mixed-moments"/relative
        audit.equal("study_verification_hash", digest(file), item["sha256"], str(relative))
        audit.equal("study_verification_size", file.stat().st_size, item["bytes"], str(relative))
    for item in provenance["original_artifacts_copied"]:
        file = source/safe_relative(item["file"])
        audit.equal("copied_artifact_hash", digest(file), item["sha256"], item["file"])
        audit.equal("copied_artifact_size", file.stat().st_size, item["bytes"], item["file"])

    audit.equal("certificate_schema", saved["schema_version"], 1)
    audit.equal("record_schema", records["schema_version"], 1)
    audit.equal("saved_check_categories", saved["check_counts"], EXPECTED_COUNTS)
    audit.equal("saved_check_total", saved["total_checks"], 17805)
    audit.equal("saved_check_total_sum", sum(saved["check_counts"].values()), 17805)
    audit.equal("verification_check_total", verification["exact_arithmetic_checks_passed"], 17805)
    theorems = records["theorems"]
    audit.equal("theorem_ids", [t["id"] for t in theorems], [f"MM{n:03d}" for n in range(1, 22)])
    audit.equal("theorem_record_count", len(theorems), verification["theorem_records"])
    ids = {t["id"] for t in theorems}
    topological_order = records["topological_order"]
    audit.equal("topological_order_ids", set(topological_order), ids)
    audit.equal("topological_order_count", len(topological_order), len(ids))
    rank = {name: n for n, name in enumerate(topological_order)}
    edges = sum(len(t["dependencies"]) for t in theorems)
    audit.equal("dependency_edge_count", edges, 39)
    audit.equal("verification_dependency_edges", verification["dependency_edges"], edges)
    for theorem in theorems:
        audit.equal("dependency_uniqueness", len(set(theorem["dependencies"])), len(theorem["dependencies"]), theorem["id"])
        for dependency in theorem["dependencies"]:
            audit.check("dependency_resolves", dependency in ids, dependency)
            audit.check("dependency_precedes_theorem", rank[dependency] < rank[theorem["id"]], theorem["id"])

    # Execute the exact supplied program only in a newly created scratch tree.
    # -I isolates Python from PYTHONPATH/user site; -B prevents bytecode writes.
    with tempfile.TemporaryDirectory(prefix="mixed-moments-certificates-") as scratch_name:
        scratch = Path(scratch_name)
        target = scratch/"mixed-moments"
        target.mkdir()
        (scratch/Path(SNAPSHOT).parent).mkdir(parents=True)
        shutil.copyfile(source/"mixed-moments/certificates.py", target/"certificates.py")
        shutil.copyfile(source/SNAPSHOT, scratch/SNAPSHOT)
        completed = subprocess.run([sys.executable, "-I", "-B", str(target/"certificates.py")],
                                   cwd=scratch, text=True, capture_output=True, timeout=180, check=False)
        audit.equal("supplied_script_exit_code", completed.returncode, 0, completed.stderr)
        audit.equal("supplied_script_stderr_empty", completed.stderr, "")
        generated_path = target/"certificates.json"
        generated_bytes = generated_path.read_bytes()
        audit.equal("regenerated_certificate_byte_identical", generated_bytes,
                    (source/"mixed-moments/certificates.json").read_bytes())
        generated = json.loads(generated_bytes)
        audit.equal("regenerated_certificate_json_equal", generated, saved)
        supplied_summary = json.loads(completed.stdout)
        audit.equal("rerun_check_counts", supplied_summary["check_counts"], EXPECTED_COUNTS)
        audit.equal("rerun_check_total", supplied_summary["total_checks"], 17805)
        # Temporary output paths are deliberately normalized in the durable log.
        supplied_summary["output"] = "<temporary scratch>/mixed-moments/certificates.json"
        regenerated_hash = digest_bytes(generated_bytes)

    independent = independent_checks.run(source)
    after = inventory(source)
    audit.equal("original_source_tree_unchanged", after, before)
    audit.equal("original_archive_unchanged", digest(archive), actual_archive_hash)
    return {
        "schema_version": 1, "status": "passed", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "checker_sha256": {"scripts/check_certificates.py": digest(Path(__file__).resolve()),
                           "scripts/independent_checks.py": digest(Path(independent_checks.__file__).resolve())},
        "archive": {"file": archive.name, "bytes": archive.stat().st_size,
            "sha256": actual_archive_hash, "fixed_expected_sha256": ARCHIVE_SHA256,
            "archive_files": len(archive_entries), "all_extracted_files_match_archive": True},
        "inner_manifest": {"file": "MANIFEST-SHA256.json", "sha256": digest(source/"MANIFEST-SHA256.json"),
                           "files_verified": len(manifest_paths), "complete_except_explicit_self_exclusion": True},
        "source": {"snapshot": SNAPSHOT, "sha256": SOURCE_SHA256,
                   "recorded_revision": SOURCE_REVISION, "remote_revision_freshly_authenticated": False,
                   "all_original_files_unchanged": True, "files_hashed_before_and_after": len(before)},
        "records": {"theorems": len(theorems), "dependency_edges": edges, "acyclic_topological_order_valid": True},
        "supplied_rerun": {"scratch_execution": True, "byte_identical_to_saved": True,
                           "certificate_sha256": regenerated_hash, **supplied_summary},
        "independent": independent,
        "provenance_and_rerun_check_counts": dict(sorted(audit.counts.items())),
        "provenance_and_rerun_total_checks": sum(audit.counts.values()),
        "limits": ["Pinned archive and local snapshot bytes are authenticated; remote repository history is not reauthenticated.",
                   "Arithmetic triples are formal coordinates of 1, G, zeta(2); no independence is assumed.",
                   "Neither the supplied nor independent Python checks prove analytic integrals, infinite sums, irrationality, or Lean theorems."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, default=PROJECT/"source"/(ARCHIVE_NAME+".zip"))
    parser.add_argument("--source", type=Path, default=PROJECT/"source/reviewed"/ARCHIVE_NAME)
    parser.add_argument("--output", type=Path, default=PROJECT/"logs/certificates-verification.json")
    args = parser.parse_args()
    report = run(args.archive.resolve(), args.source.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    independent_output = args.output.with_name("certificates-independent.json")
    independent_output.write_text(json.dumps(report["independent"], indent=2)+"\n")
    print(json.dumps({"status": report["status"], "supplied_checks": report["supplied_rerun"]["total_checks"],
                      "independent_checks": report["independent"]["total_checks"],
                      "provenance_and_rerun_checks": report["provenance_and_rerun_total_checks"],
                      "original_source_unchanged": True, "output": str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
