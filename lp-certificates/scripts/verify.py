#!/usr/bin/env python3
"""Record a fresh LP verification attempt. Never overwrite an existing attempt."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
LEAN_VERSION = "leanprover/lean4:v4.24.0"
MATHLIB_REV = "f897ebcf72cd16f89ab4577d0c826cd14afaafc7"
LEAN_COMMIT = "797c613eb9b6d4ec95db23e3e00af9ac6657f24b"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def utc():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inputs():
    paths = [ROOT / "lean-toolchain", ROOT / "lakefile.toml", ROOT / "lake-manifest.json",
             ROOT / "verifier.py", ROOT / "LPCertificates.lean"]
    paths.extend(ROOT.glob("*.py"))
    for folder, suffix in (("LPCertificates", ".lean"), ("scripts", ".py"),
                           ("scripts", ".lean"), ("tests", ".py"), ("examples", ".json")):
        paths.extend(sorted((ROOT / folder).glob("*" + suffix)))
    return {str(p.relative_to(ROOT)): digest(p) for p in sorted(set(paths))}


def code_only(text):
    """Remove nested block comments, line comments, and strings for a source scan."""
    out, i, depth, quoted = [], 0, 0, False
    while i < len(text):
        pair, char = text[i:i+2], text[i]
        if depth:
            if pair == "/-": depth += 1; i += 2
            elif pair == "-/": depth -= 1; i += 2
            else: out.append("\n" if char == "\n" else " "); i += 1
        elif quoted:
            if char == "\\": i += 2
            else:
                if char == '"': quoted = False
                out.append("\n" if char == "\n" else " "); i += 1
        elif pair == "/-": depth = 1; i += 2
        elif pair == "--":
            end = text.find("\n", i)
            i = len(text) if end < 0 else end
        elif char == '"': quoted = True; i += 1
        else: out.append(char); i += 1
    if depth or quoted:
        raise ValueError("Unclosed Lean comment or string")
    return "".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--lean-bin", type=Path)
    parser.add_argument("--cached-repository", type=Path,
                        help="Optional repository containing the original pinned release archive")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    record = {"schema": "lp-certificates-local-verification/v1", "started_utc": utc(),
              "status": "in_progress", "commands": [], "source_sha256": inputs(),
              "trust_limits": ["cached dependency oleans and host runtime trusted",
                  "same Lean kernel replay, not an independent kernel implementation",
                  "JSON/Python refinement to Lean not proved", "no native Mac/MRS integration"]}
    environment = os.environ.copy()
    if args.lean_bin:
        environment["PATH"] = str(args.lean_bin.resolve()) + os.pathsep + environment.get("PATH", "")
    lake = shutil.which("lake", path=environment.get("PATH"))

    def write_record():
        (output / "receipt.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")

    def run(label, argv, cwd=ROOT):
        entry = {"label": label, "argv": [str(x) for x in argv], "cwd": str(cwd),
                 "started_utc": utc()}
        process = subprocess.run(entry["argv"], cwd=cwd, env=environment, capture_output=True,
                                 timeout=300, shell=False)
        for stream in ("stdout", "stderr"):
            path = output / (label + "." + stream + ".log")
            path.write_bytes(getattr(process, stream))
            entry[stream] = {"file": path.name, "bytes": path.stat().st_size,
                             "sha256": digest(path)}
        entry.update({"exit_code": process.returncode, "ended_utc": utc()})
        record["commands"].append(entry)
        write_record()
        if process.returncode:
            raise ValueError(f"{label} exited {process.returncode}; inspect captured logs")
        return process.stdout.decode("utf-8") + process.stderr.decode("utf-8")

    try:
        write_record()
        if lake is None:
            raise ValueError("Pinned Lake binary unavailable; supply --lean-bin")
        record["lake_binary"] = str(Path(lake).resolve())
        if (ROOT / "lean-toolchain").read_text().strip() != LEAN_VERSION:
            raise ValueError("Unexpected Lean toolchain pin")
        manifest = json.loads((ROOT / "lake-manifest.json").read_text())
        mathlib = next(p for p in manifest["packages"] if p["name"] == "mathlib")
        if mathlib["rev"] != MATHLIB_REV or mathlib["url"] != "https://github.com/leanprover-community/mathlib4.git":
            raise ValueError("Unexpected mathlib pin")
        packages = []
        for p in manifest["packages"]:
            folder = ROOT / ".lake/packages" / p["name"]
            def git(*argv):
                return subprocess.check_output(["git", "-C", str(folder), *argv], text=True).strip()
            observed = {"name": p["name"], "revision": git("rev-parse", "HEAD"),
                        "origin": git("remote", "get-url", "origin"),
                        "tracked_status": git("status", "--porcelain", "--untracked-files=no")}
            if observed["revision"] != p["rev"] or observed["origin"].removesuffix(".git") != p["url"].removesuffix(".git") or observed["tracked_status"]:
                raise ValueError("Dependency identity/cleanliness mismatch: " + p["name"])
            packages.append(observed)
        record["resolved_dependencies"] = packages
        version = run("compiler-version", [lake, "env", "lean", "--version"])
        if "version 4.24.0," not in version or LEAN_COMMIT not in version:
            raise ValueError("Wrong actual compiler")
        toolkit = ROOT.parent / "math-evidence"
        record["evidence_helper_sha256"] = digest(toolkit / "lean/EvidenceHarness.lean")
        run("toolkit-source-pins", ["node", toolkit / "verify-public-sources.cjs"], cwd=toolkit)
        if args.cached_repository:
            byte_audit = json.loads(run("compiler-byte-audit", [sys.executable,
                toolkit / "toolchain-audit.py", args.cached_repository.resolve()]))
            actual_prefix = Path(run("compiler-location", [lake, "env", "lean", "--print-prefix"]).strip()).resolve()
            audited_lean = Path(byte_audit["compilerAndRuntime"]["bin/lean"]["installed"]).resolve()
            if (actual_prefix / "bin/lean").resolve() != audited_lean:
                raise ValueError("Byte-audited compiler is not the compiler selected by Lake")
            record["compiler_byte_audit"] = "actual_selected_compiler_matches_pinned_release_members"
        else:
            record["compiler_byte_audit"] = "not_performed_no_archive_supplied"
        run("python-tests", [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"])
        # Force all project modules to be recompiled while retaining pinned dependency caches.
        project_cache = ROOT / ".lake/build"
        if project_cache.is_symlink():
            raise ValueError("Refusing to clear a symlinked project build directory")
        if project_cache.exists(): shutil.rmtree(project_cache)
        build = run("lean-build", [lake, "build"])
        if re.search(r"(?mi)\b(?:error|warning):", build):
            raise ValueError("Lean build had diagnostics")
        names = []
        for path in [ROOT / "LPCertificates.lean", *sorted((ROOT / "LPCertificates").glob("*.lean"))]:
            code = code_only(path.read_text())
            if re.search(r"\b(?:sorry|admit|axiom|unsafe|native_decide)\b", code):
                raise ValueError("Forbidden proof/source construct: " + str(path))
            names.extend("LPCertificates." + n for n in re.findall(
                r"(?m)^\s*(?:def|theorem|lemma)\s+(\w+)", code))
        audit = output / "AxiomAudit.lean"
        audit.write_text("import LPCertificates\nset_option pp.universes true\n" +
                         "".join("#check @"+n+"\n#print axioms "+n+"\n" for n in names))
        inventory = run("declaration-audit", [lake, "env", "lean", "--root=" + str(output), audit])
        if re.search(r"(?mi)\b(?:error|warning):", inventory):
            raise ValueError("Declaration audit had diagnostics")
        axioms = {}
        for name, group in re.findall(r"'([^']+)' depends on axioms:\s*\[([^]]*)\]", inventory):
            axioms[name] = sorted(x.strip() for x in group.split(",") if x.strip())
        for name in re.findall(r"'([^']+)' does not depend on any axioms", inventory): axioms[name] = []
        if set(axioms) != set(names) or any(set(a)-ALLOWED_AXIOMS for a in axioms.values()):
            raise ValueError("Incomplete audit or unexpected axiom closure")
        record["named_declarations"] = names
        record["transitive_axioms"] = axioms
        lib = ROOT / ".lake/build/lib/lean"
        run("evidence-helper-build", [lake, "env", "lean", "--root=" + str(toolkit / "lean"),
             toolkit / "lean/EvidenceHarness.lean", "-o", lib / "EvidenceHarness.olean"])
        expected = run("independent-expected-and-replay", [lake, "env", "lean", "scripts/Expected.lean"])
        if (re.search(r"(?mi)\b(?:error|warning):", expected) or
            expected.count("MATH_EVIDENCE_TARGET ") != 3 or
            expected.count("MATH_EVIDENCE_DEFINITION ") != 5 or
            expected.count("MATH_EVIDENCE_REPLAY ") != 1):
            raise ValueError("Incomplete expected-type/body/replay gate")
        input_expected = run("independent-input-expected-and-replay",
                             [lake, "env", "lean", "scripts/ExpectedInput.lean"])
        if (re.search(r"(?mi)\b(?:error|warning):", input_expected) or
            input_expected.count("MATH_EVIDENCE_TARGET ") != 3 or
            input_expected.count("MATH_EVIDENCE_DEFINITION ") != 9 or
            input_expected.count("MATH_EVIDENCE_REPLAY ") != 1):
            raise ValueError("Incomplete original-input expected-type/body/replay gate")
        if inputs() != record["source_sha256"]:
            raise ValueError("Sources changed during verification")
        record["status"] = "passed"
        record["results"] = {"fresh_project_compilation": "passed", "named_axiom_audit": "passed",
                             "independent_expected_type_and_body_gate": "passed",
                             "independent_original_input_type_and_body_gate": "passed",
                             "same_kernel_local_replay": "passed", "python_tests": "passed"}
    except Exception as error:
        record.update({"status": "failed", "failure": str(error)})
    finally:
        record["ended_utc"] = utc()
        write_record()
    print(json.dumps({"status": record["status"], "receipt": str(output / "receipt.json"),
                      "failure": record.get("failure")}, indent=2))
    return 0 if record["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
