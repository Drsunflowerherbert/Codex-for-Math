#!/usr/bin/env python3
"""Reviewer-owned independent compilation and declaration audit.

Run only after the authors freeze the production import closure. This writes
review artifacts and a separate OLean cache, never author proof source.
"""
from __future__ import annotations

import hashlib
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import shutil
import sys
from datetime import datetime, timezone

PROJECT = Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,default=PROJECT/'reviews/current')
parser.add_argument('--audit-only',action='store_true')
ARGS=parser.parse_args()
REVIEW = ARGS.output
CACHE = REVIEW / "lean-cache"
LAKE=shutil.which('lake')
if not LAKE:raise SystemExit('Install the pinned Lean toolchain and put lake on PATH.')
BIN = Path(subprocess.check_output([LAKE,'env','lean','--print-prefix'],cwd=PROJECT,text=True).strip())/'bin'


def fingerprint(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def run(args: list[str], env: dict[str, str], log: Path) -> dict[str, object]:
    process = subprocess.run(args, cwd=PROJECT, env=env, text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log.write_text(process.stdout)
    return {"command": args, "exit_code": process.returncode,
            "log": log.name, **fingerprint(log)}


def own_import_closure() -> tuple[list[Path], dict[str, list[str]]]:
    ordered: list[Path] = []
    imports: dict[str, list[str]] = {}
    visiting: set[Path] = set()
    visited: set[Path] = set()

    def visit(path: Path) -> None:
        if path in visited:
            return
        if path in visiting:
            raise RuntimeError(f"Cyclic imports at {path}")
        visiting.add(path)
        listed = re.findall(r"(?m)^import\s+([\w.]+)\s*$", path.read_text())
        imports[str(path.relative_to(PROJECT))] = listed
        for module in listed:
            child = PROJECT / (module.replace(".", "/") + ".lean")
            if child.is_file() and not child.is_relative_to(PROJECT / ".lake"):
                visit(child)
        visiting.remove(path)
        visited.add(path)
        ordered.append(path)

    visit(PROJECT / "PositiveBlocks.lean")
    return ordered, imports


def public_declarations(path: Path) -> list[dict[str, str]]:
    declarations = []
    scopes: list[tuple[str, str]] = []
    for number, line in enumerate(path.read_text().splitlines(), 1):
        match = re.match(r"^namespace\s+([\w.]+)", line)
        if match:
            scopes.append(("namespace", match[1]))
        elif re.match(r"^(?:noncomputable\s+)?section(?:\s|$)", line):
            scopes.append(("section", ""))
        elif re.match(r"^end(?:\s|$)", line) and scopes:
            scopes.pop()
        match = re.match(r"^(?:@\[[^\]]+\]\s*)?(?:noncomputable\s+)?(?:protected\s+)?(theorem|def)\s+([\w.]+)", line)
        if match:
            namespace = [name for kind, name in scopes if kind == "namespace"]
            declarations.append({"name": ".".join(namespace + [match[2]]),
                                 "kind": match[1],
                                 "source": str(path.relative_to(PROJECT)),
                                 "line": number})
    return declarations


def main() -> int:
    REVIEW.mkdir(parents=True,exist_ok=True)
    CACHE.mkdir(exist_ok=True)
    env = dict(os.environ)
    env["PATH"] = str(BIN) + os.pathsep + env.get("PATH", "")
    paths, imports = own_import_closure()
    before = {str(p.relative_to(PROJECT)): fingerprint(p) for p in paths}
    baseline = subprocess.check_output([str(BIN / "lake"), "env", "printenv", "LEAN_PATH"],
                                       cwd=PROJECT, env=env, text=True).strip()
    env["LEAN_PATH"] = str(CACHE) + os.pathsep + baseline
    compilation = []
    if "--audit-only" in sys.argv[1:]:
        prior = json.loads((REVIEW / "final-source-audit.json").read_text())
        if prior["source_fingerprints"] != before:
            raise RuntimeError("Source changed since independent compilation")
        compilation = prior["compilation"]
    else:
        for path in paths:
            relative = path.relative_to(PROJECT)
            output = CACHE / relative.with_suffix(".olean")
            output.parent.mkdir(parents=True, exist_ok=True)
            log = REVIEW / ("compile-" + str(relative).replace("/", "-") + ".log")
            result = run([str(BIN / "lean"), "-o", str(output), str(relative)], env, log)
            compilation.append(result)
            print(f"compile {relative}: {result['exit_code']}", flush=True)
            if result["exit_code"]:
                break
    declarations = [declaration for path in paths for declaration in public_declarations(path)]
    audit_path = REVIEW / "DeclarationAudit.lean"
    audit_text = ["import PositiveBlocks", "set_option pp.universes true"]
    for declaration in declarations:
        audit_text += [f"#check @{declaration['name']}", f"#print axioms {declaration['name']}"]
    audit_path.write_text("\n".join(audit_text) + "\n")
    audit = None
    if all(result["exit_code"] == 0 for result in compilation):
        audit = run([str(BIN / "lean"), str(audit_path)], env, REVIEW / "declaration-audit.log")
        print(f"declaration audit: {audit['exit_code']}", flush=True)
    after = {str(p.relative_to(PROJECT)): fingerprint(p) for p in paths}
    metadata = {
        "reviewed_utc": datetime.now(timezone.utc).isoformat(),
        "source_unchanged_during_audit": before == after,
        "source_fingerprints": after,
        "imports": imports,
        "declarations": declarations,
        "compilation": compilation,
        "declaration_audit": audit,
        "fresh_review_cache": "lean-cache",
        "method": "Each production module compiled directly from source in dependency order; own imports resolved first against independently compiled review OLeans. Mathlib uses the supplied pinned build cache.",
    }
    (REVIEW / "final-source-audit.json").write_text(json.dumps(metadata, indent=2) + "\n")
    success = before == after and all(result["exit_code"] == 0 for result in compilation) and audit and audit["exit_code"] == 0
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
