#!/usr/bin/env python3
"""Read-only, streaming presence audit of selected Lean NDJSON declarations.

This is not a parser/kernel proof check. Expression records are never decoded.
Only name prefixes needed by the requested targets are retained in memory.
The input export is opened read-only; the only write is the JSON result.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys


DEFAULT_TARGETS = (
    "HolomorphicAnosov.theorem_A",
    "HolomorphicAnosov.theorem_1_1",
    "HolomorphicAnosov.theorem_1_2",
    "HolomorphicAnosov.theorem_1_3",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("export", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--expect-sha256", required=True)
    parser.add_argument("--expect-bytes", type=int, required=True)
    parser.add_argument("--target", action="append", dest="targets")
    args = parser.parse_args()
    source = args.export.resolve(strict=True)
    destination = args.output.resolve()
    if source == destination:
        parser.error("the result must not overwrite the export")

    targets = tuple(args.targets or DEFAULT_TARGETS)
    parts = {name: tuple(name.split(".")) for name in targets}
    allowed_prefixes = {
        path[:length]
        for path in parts.values()
        for length in range(len(path) + 1)
    }
    # Name 0 is the export format's anonymous root. Unrelated names are discarded.
    selected_names: dict[int, tuple[str, ...]] = {0: ()}
    target_by_parts = {path: name for name, path in parts.items()}
    target_by_id: dict[int, str] = {}
    found: dict[str, list[dict[str, int | str]]] = {name: [] for name in targets}
    mismatches: list[dict[str, int | str]] = []
    relevant_errors: list[dict[str, int | str]] = []
    metadata = None
    digest = hashlib.sha256()
    byte_count = 0
    line_count = 0
    name_records = 0
    theorem_records = 0
    stat_before = source.stat()
    declaration_prefixes = {
        b'{"thm":': "thm",
        b'{"axiom":': "axiom",
        b'{"def":': "def",
        b'{"opaque":': "opaque",
    }
    with source.open("rb", buffering=1024 * 1024) as handle:
        for line_count, line in enumerate(handle, 1):
            digest.update(line)
            byte_count += len(line)
            if line_count == 1:
                metadata = json.loads(line).get("meta")
                continue
            if line.startswith(b'{"in":'):
                name_records += 1
                record = json.loads(line)
                component = record.get("str")
                # The selected names have string components, not numbered names.
                if component is None:
                    continue
                parent = selected_names.get(component["pre"])
                if parent is None:
                    continue
                path = parent + (component["str"],)
                if path in allowed_prefixes:
                    identifier = record["in"]
                    if identifier in selected_names and selected_names[identifier] != path:
                        relevant_errors.append({"line": line_count, "reason": "name ID reused"})
                    selected_names[identifier] = path
                    if path in target_by_parts:
                        target_by_id[identifier] = target_by_parts[path]
                continue
            kind = next(
                (kind for prefix, kind in declaration_prefixes.items() if line.startswith(prefix)),
                None,
            )
            if kind is None:
                # All expression/universe/recursor/inductive records are skipped.
                continue
            if kind == "thm":
                theorem_records += 1
            body = json.loads(line)[kind]
            target = target_by_id.get(body["name"])
            if target is None:
                continue
            evidence = {
                "name": target,
                "kind": kind,
                "declaration_line": line_count,
                "name_id": body["name"],
                "type_expression_id": body["type"],
            }
            if kind == "thm":
                evidence["proof_expression_id"] = body["value"]
                found[target].append(evidence)
            else:
                mismatches.append(evidence)

    stat_after = source.stat()
    unchanged = (
        stat_before.st_dev,
        stat_before.st_ino,
        stat_before.st_size,
        stat_before.st_mtime_ns,
    ) == (
        stat_after.st_dev,
        stat_after.st_ino,
        stat_after.st_size,
        stat_after.st_mtime_ns,
    )
    actual_hash = digest.hexdigest()
    presence_ok = all(len(found[name]) == 1 for name in targets)
    hash_ok = actual_hash == args.expect_sha256.lower()
    size_ok = byte_count == args.expect_bytes
    accepted = presence_ok and hash_ok and size_ok and unchanged and not mismatches and not relevant_errors
    result = {
        "schema_version": 1,
        "audit": "selected-theorem-presence-only; not kernel or axiom verification",
        "export": {
            "path": str(source),
            "bytes": byte_count,
            "sha256": actual_hash,
            "expected_bytes": args.expect_bytes,
            "expected_sha256": args.expect_sha256.lower(),
            "size_matches": size_ok,
            "sha256_matches": hash_ok,
            "stat_unchanged_during_scan": unchanged,
            "lines": line_count,
            "metadata": metadata,
        },
        "targets": [
            {"name": name, "theorem_declarations": found[name], "exactly_one_present": len(found[name]) == 1}
            for name in targets
        ],
        "all_targets_present_as_theorems": presence_ok,
        "non_theorem_target_declarations": mismatches,
        "relevant_name_errors": relevant_errors,
        "scan_counts": {
            "name_records": name_records,
            "theorem_records": theorem_records,
            "retained_name_prefixes_including_anonymous": len(selected_names),
        },
        "accepted": accepted,
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(destination.name + ".part")
    temporary.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    temporary.replace(destination)
    print(json.dumps({"accepted": accepted, "bytes": byte_count, "sha256": actual_hash, "result": str(destination)}))
    return 0 if accepted else 1


if __name__ == "__main__":
    sys.exit(main())
