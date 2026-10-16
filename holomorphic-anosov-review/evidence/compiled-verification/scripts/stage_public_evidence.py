#!/usr/bin/env python3
"""Stage an explicit audit-evidence allowlist after the final replay status exists.

This script copies audit-owned harnesses/scripts, notes, metadata and text logs.
It does not copy or execute upstream proof sources, toolchains, dependencies,
caches, generated proof exports, source PDFs, repository setup code or keys.
Run only after the verification owner has finalized the replay record/report.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DESTINATION = (
    ROOT.parent / "extension" / "publication" / "holomorphic-anosov-review"
    / "evidence" / "compiled-verification"
)

# Exact files only: a newly created file is never included automatically.
ALLOWLIST = (
    "checks/README.md",
    "checks/VerifyStatements.lean",
    "checks/VerifyDefinitions.lean",
    "checks/initial/VerifyStatements.lean",
    "checks/initial/VerifyDefinitions.lean",
    "deliverables/verification-method.md",
    "deliverables/publication-plan.md",
    "provenance/README.md",
    "provenance/build-config-audit.md",
    "provenance/bundled-comparator-source-match.json",
    "provenance/dependency-installation.json",
    "provenance/installed-executables-and-sandbox.json",
    "provenance/kernel-replay-plan.md",
    "provenance/lean-official-release-v4.35.0-rc1.json",
    "provenance/lean-release-metadata.json",
    "provenance/toolchain-installation.json",
    "provenance/upstream-build-config-source-digests.json",
    "results/compiled-axiom-summary.json",
    "results/export-target-presence.json",
    "results/source-and-artifact-manifest.json",
    "results/verification-summary.json",
    "scripts/capture_artifacts.py",
    "scripts/check_export_targets.py",
    "scripts/export_selected_targets.py",
    "scripts/fetch_pinned_dependencies.py",
    "scripts/install_official_lean.py",
    "scripts/run_logged.py",
    "scripts/run_logged_build.py",
    "scripts/run_logged_build4.py",
    "scripts/summarize_axioms.py",
    "scripts/summarize_verification.py",
    "scripts/stage_public_evidence.py",
    "logs/axiom-summary.log",
    "logs/comparator-attempt.json",
    "logs/comparator-attempt.log",
    "logs/connectivity-check.json",
    "logs/controlled-restart.json",
    "logs/dependencies-fetch.log",
    "logs/exact-definitions-01.json",
    "logs/exact-definitions-01.log",
    "logs/exact-definitions-02.json",
    "logs/exact-definitions-02.log",
    "logs/exact-statements-01.json",
    "logs/exact-statements-01.log",
    "logs/exact-statements-02.json",
    "logs/exact-statements-02.log",
    "logs/harness-correction.json",
    "logs/mathlib-cache.json",
    "logs/mathlib-cache.log",
    "logs/premature-replay-discarded.json",
    "logs/selected-targets-export.json",
    "logs/selected-targets-export.stderr.log",
    "logs/selected-targets-replay.json",
    "logs/selected-targets-replay.log",
    "logs/selected-targets-replay-02.json",
    "logs/selected-targets-replay-02.log",
    "logs/solution-build.json",
    "logs/solution-build.log",
    "logs/solution-build-four-threads.json",
    "logs/solution-build-four-threads.log",
    "logs/toolchain-installation.log",
)

EXCLUDED = (
    "toolchains/", "build/", "cache/", "downloads/", "exports/",
    "upstream proof sources and dependency checkouts",
    "source PDFs/OCR/full third-party articles",
    "legacy standalone comparator/lean4export/Landrun metadata",
    "internal CONTINUE.md, report-update scripts, publication remote-head logs",
    "all files absent from the explicit allowlist",
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def no_symlinks(path: Path, base: Path) -> None:
    relative = path.relative_to(base)
    cursor = base
    if base.is_symlink():
        raise ValueError("symlinked bundle root")
    for part in relative.parts:
        cursor /= part
        if cursor.is_symlink():
            raise ValueError("symlink in allowlisted path: " + relative.as_posix())


def privacy_check(text: str, name: str) -> None:
    # Public release SHA, GitHub node/asset IDs and system paths are permissible.
    rules = (
        (r"libfile_[0-9a-f]{20,}", "private Library identifier"),
        (r"file_[0-9a-f]{24,}", "private attachment identifier"),
        (r"source_" + r"thread_id", "private conversation identifier key"),
        (r"/(?:workspace|home|root|tmp|mnt)/[^\s\"'<>`]+", "unmapped private path"),
        (r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----", "private key"),
        (r"(?:gh[pousr]_[A-Za-z0-9_]{30,}|github_pat_[A-Za-z0-9_]{30,})", "token"),
        (r"https?://[^/\s:@]+:[^/\s@]+@", "URL credentials"),
    )
    for pattern, reason in rules:
        if re.search(pattern, text):
            raise ValueError(f"{reason} in {name}; inspect privately before staging")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, default=DEFAULT_DESTINATION)
    parser.add_argument(
        "--private-root", action="append", default=[], metavar="PATH=TOKEN",
        help="additional explicit private prefix mapping; TOKEN must be $UPPER_CASE",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="validate and print a path-free summary without writing staged files",
    )
    args = parser.parse_args()

    final_path = ROOT / "logs/selected-targets-replay-02.json"
    if not final_path.is_file():
        raise ValueError("final selected-targets-replay-02 status is absent; staging forbidden")
    final = json.loads(final_path.read_text(encoding="utf-8"))
    if not isinstance(final.get("exit_code"), int) or "duration_seconds" not in final:
        raise ValueError("final replay record lacks a terminal exit status/duration")
    if final.get("step") != "selected-targets-replay-02":
        raise ValueError("wrong final replay step")
    method = (ROOT / "deliverables/verification-method.md").read_text(encoding="utf-8")
    if "proper selected-proof replay is still pending" in method:
        raise ValueError("method document still reports replay pending; finalize it before staging")

    # Longest prefix wins. No private absolute prefixes appear in public records.
    replacements = {
        str(ROOT): "$VERIFY_ROOT",
        str(ROOT.parent / "extension"): "$SOURCE_AUDIT",
        str(ROOT.parent): "$REVIEW_ROOT",
        str(ROOT.parent.parent): "$WORKSPACE_ROOT",
    }
    for item in args.private_root:
        path, separator, token = item.rpartition("=")
        if not separator or not Path(path).is_absolute() or not re.fullmatch(r"\$[A-Z_]+", token):
            raise ValueError("--private-root requires an absolute PATH=$UPPER_CASE")
        replacements[path.rstrip("/")] = token
    ordered = sorted(replacements.items(), key=lambda row: len(row[0]), reverse=True)

    original = {}
    normalized = {}
    rule_counts = {}
    for name in ALLOWLIST:
        path = ROOT / name
        no_symlinks(path, ROOT)
        if not path.is_file():
            raise ValueError("missing allowlisted file: " + name)
        data = path.read_bytes()
        original[name] = data
        value = data.decode("utf-8")
        counts = Counter()
        for prefix, token in ordered:
            count = value.count(prefix)
            if count:
                value = value.replace(prefix, token)
                counts[token] += count
        privacy_check(value, name)
        normalized[name] = value.encode("utf-8")
        rule_counts[name] = dict(counts)

    # Status records explicitly distinguish historical original log hashes from
    # hashes of the public normalized copies. Verify originals before relabelling.
    related_logs = {}
    for name in ALLOWLIST:
        if not name.endswith(".json") or not name.startswith("logs/"):
            continue
        value = json.loads(normalized[name])
        if not isinstance(value, dict):
            continue
        refs = []
        for path_key, hash_key, role in (
            ("log", "log_sha256", "combined_output"),
            ("stderr_log", "stderr_sha256", "stderr"),
        ):
            if hash_key not in value:
                continue
            relative = "logs/" + value[path_key]
            if relative not in normalized:
                raise ValueError("status references a log absent from allowlist: " + relative)
            raw_hash = digest(original[relative])
            if raw_hash != value[hash_key]:
                raise ValueError("original log hash mismatch: " + relative)
            value["original_" + hash_key] = value.pop(hash_key)
            published_hash = digest(normalized[relative])
            value["published_normalized_" + hash_key] = published_hash
            refs.append({
                "role": role, "path": relative,
                "original_sha256": raw_hash,
                "published_normalized_sha256": published_hash,
            })
        if refs:
            value["_publication"] = {
                "copy_kind": "normalized public copy; original record retained privately",
                "original_record_sha256": digest(original[name]),
                "normalization": "absolute private prefixes replaced by documented placeholders",
                "original_log_hash_fields_relabelled": True,
                "related_logs": refs,
            }
            normalized[name] = (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
            related_logs[name] = refs

    # The aggregate summary contains a nested copy of the replay log hash.
    name = "results/verification-summary.json"
    value = json.loads(normalized[name])
    replay = value["raw_kernel_replay"]
    relative = "logs/selected-targets-replay-02.log"
    raw_hash = digest(original[relative])
    if replay["log_sha256"] != raw_hash:
        raise ValueError("aggregate summary's original replay log hash mismatch")
    published_hash = digest(normalized[relative])
    replay["original_log_sha256"] = replay.pop("log_sha256")
    replay["published_normalized_log_sha256"] = published_hash
    refs = [{
        "role": "raw_kernel_replay.log", "path": relative,
        "original_sha256": raw_hash,
        "published_normalized_sha256": published_hash,
    }]
    value["_publication"] = {
        "copy_kind": "normalized public copy; original summary retained privately",
        "original_record_sha256": digest(original[name]),
        "normalization": "private prefixes replaced; nested raw_kernel_replay.log_sha256 explicitly relabelled",
        "related_logs": refs,
    }
    normalized[name] = (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    related_logs[name] = refs

    for name, data in normalized.items():
        privacy_check(data.decode("utf-8"), name)

    rows = [
        {
            "path": name,
            "original_bytes": len(original[name]),
            "original_sha256": digest(original[name]),
            "published_bytes": len(normalized[name]),
            "published_normalized_sha256": digest(normalized[name]),
            "changed_for_publication": original[name] != normalized[name],
            "prefix_replacement_counts": rule_counts[name],
            "status_log_hash_relabelling": name in related_logs,
        }
        for name in ALLOWLIST
    ]
    manifest = {
        "schema_version": 1,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "content": "audit-owned evidence only; normalized copies with explicit allowlist",
        "source_commit": "65f2b33a7309de661a8500e4642e5609a537a8ff",
        "final_replay": {
            "step": final["step"], "exit_code": final["exit_code"],
            "resource_stop": final.get("resource_stop"),
            "duration_seconds": final["duration_seconds"],
        },
        "normalization_record": {
            "encoding": "UTF-8; original newlines retained except JSON status reserialization",
            "placeholder_meanings": {
                "$VERIFY_ROOT": "private compiled-verification root",
                "$SOURCE_AUDIT": "private source-audit extension root",
                "$REVIEW_ROOT": "private review root",
                "$WORKSPACE_ROOT": "private enclosing workspace root",
            },
            "additional_placeholders": sorted(set(replacements.values()) - {
                "$VERIFY_ROOT", "$SOURCE_AUDIT", "$REVIEW_ROOT", "$WORKSPACE_ROOT"
            }),
            "absolute_private_prefixes_published": False,
            "hash_note": "original_* hashes identify retained raw bytes; published_normalized_* hashes identify these distributed copies",
            "status_note": "log_sha256 and stderr_sha256 become original_* plus published_normalized_* fields; no success/failure content removed",
        },
        "exclusions": list(EXCLUDED),
        "files": rows,
        "generated_file_hashes": "PUBLICATION.md is listed in SHA256SUMS; manifest and SHA256SUMS cannot hash themselves",
    }
    privacy_check(json.dumps(manifest), "publication-manifest.json")

    if args.dry_run:
        print(json.dumps({
            "dry_run": True, "allowlisted_files": len(rows),
            "published_bytes": sum(row["published_bytes"] for row in rows),
            "final_replay": manifest["final_replay"],
        }, indent=2))
        return 0

    destination = args.destination.resolve()
    if destination == ROOT or ROOT in destination.parents:
        raise ValueError("destination must be outside the private verification root")
    if destination.exists() and any(destination.iterdir()):
        raise ValueError("destination must be absent or empty; never silently retain stale files")
    destination.mkdir(parents=True, exist_ok=True)
    for name, data in normalized.items():
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    publication_note = """# Compiled verification evidence: distribution record

These are normalized public copies of audit-owned scripts/harnesses, notes,
execution metadata, artifact/source hash manifests, and complete text logs.
Original execution records remain private. `publication-manifest.json` records
each original-file SHA-256 and each published-copy SHA-256, prefix replacement
counts, and the terminal replay status. It makes no new mathematical claim.

`$VERIFY_ROOT`, `$SOURCE_AUDIT`, `$REVIEW_ROOT`, and `$WORKSPACE_ROOT` replace
private absolute paths. Status metadata labels raw log hashes `original_*` and
adds `published_normalized_*` hashes for the copies actually distributed here.
The original and normalized hashes can coincide if no log bytes changed.
System executable paths and public source URLs/commit hashes are retained.

No toolchain, build tree, dependency checkout, cache, downloaded archive,
generated proof export, source PDF/OCR/full article, private identifier or key
is included. The omitted 2,385,351,648-byte proof export is identified by SHA-256
`2864d2b33f4020c69b5093af94e365da0866c5add9a3d580ef16421a2ab17276`.
Artifact/source manifests contain hashes and relative names, not those sources.
The audit harnesses reproduce complete expected interfaces and selected
definition checks; they contain no upstream proof bodies. Their print logs
are diagnostic output, not copies of the upstream repository.

Historical provenance/harness-author statements that a particular inspection
subtask did not run Lean describe that subtask. Actual execution and its limits
are recorded in `deliverables/verification-method.md` and the status/log files.
`kernel-replay-plan.md` is a preparatory plan; actual commands/status take
precedence. Legacy standalone comparator/Landrun metadata mentioned by the
provenance research note is deliberately omitted from this distribution.

Failed, stopped and discarded attempts are retained with their explanations.
The configured comparator remains blocked by its required Bubblewrap UID-map
setup, independently of the direct replay outcome. A same-kernel raw replay
does not replace comparator comparison/allowlisting or discharge the explicit
`HomotopyTorusRigidity` premise of Theorems A, 1.1 and 1.3.

For reruns, use a fresh workspace containing only `scripts/` and `checks/`,
then follow `deliverables/verification-method.md`. The scripts derive their
verification root from `Path(__file__)`. Do not run over saved evidence or
reinterpret normalized status records as original raw logs.
"""
    (destination / "PUBLICATION.md").write_text(publication_note, encoding="utf-8")
    manifest_bytes = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    (destination / "publication-manifest.json").write_bytes(manifest_bytes)
    checksums = {
        name: digest(data) for name, data in normalized.items()
    }
    checksums["PUBLICATION.md"] = digest(publication_note.encode("utf-8"))
    checksums["publication-manifest.json"] = digest(manifest_bytes)
    (destination / "SHA256SUMS").write_text(
        "".join(f"{checksums[name]}  {name}\n" for name in sorted(checksums)), encoding="utf-8"
    )
    print(json.dumps({
        "staged": True, "allowlisted_files": len(rows),
        "generated_files": ["PUBLICATION.md", "publication-manifest.json", "SHA256SUMS"],
        "final_replay": manifest["final_replay"],
        "manifest_sha256": digest(manifest_bytes),
    }, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, UnicodeError, KeyError) as error:
        print("Staging refused: " + str(error), file=sys.stderr)
        raise SystemExit(2)
