#!/usr/bin/env python3
"""Run the radial library's regression tests, pinned build, and complete axiom audit."""
import datetime
import json
import pathlib
import subprocess
import sys

from check_evidence import (EvidenceError, EVIDENCE_FILES, assumptions, audit_source,
                            check_evidence, check_pins, declarations, inputs,
                            parse_audit, require, sha256)


def verify(root):
    evidence = root / "evidence"
    evidence.mkdir(exist_ok=True)
    record = {"schema_version": 2, "status": "failed", "exit_code": 1,
              "failure": "Verification has not completed", "records": []}

    def save():
        temporary = evidence / "validation.json.tmp"
        temporary.write_text(json.dumps(record, indent=2) + "\n")
        temporary.replace(evidence / "validation.json")

    def run(command, filename):
        started = datetime.datetime.now(datetime.timezone.utc).isoformat()
        with (evidence / filename).open("w") as stream:
            try:
                result = subprocess.run(command, cwd=root, stdout=stream, stderr=subprocess.STDOUT)
                code = result.returncode
            except OSError as exc:
                stream.write(str(exc) + "\n")
                code = 127
        record["records"].append({"command": command, "exit_code": code,
                                  "started_utc": started,
                                  "finished_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                                  "log": "evidence/" + filename})
        save()
        require(code == 0, "command_failed", str(command) + "; see evidence/" + filename)

    save()  # A failed new attempt must never leave an older success marker.
    try:
        before = inputs(root)
        pins = check_pins(root)
        found = declarations(root)
        run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"], "regression-tests.log")
        run(["lake", "env", "lean", "--version"], "toolchain-current.log")
        resolved = {}
        for name, expected in pins.items():
            checkout = root / ".lake/packages" / name
            result = subprocess.run(["git", "-C", str(checkout), "rev-parse", "HEAD"],
                                    text=True, capture_output=True)
            require(result.returncode == 0 and result.stdout.strip() == expected,
                    "checkout_pin", name)
            dirty = subprocess.run(["git", "-C", str(checkout), "diff", "--quiet", "HEAD"],
                                   text=True, capture_output=True)
            require(dirty.returncode == 0, "dirty_dependency", name)
            resolved[name] = result.stdout.strip()
        (evidence / "resolved-dependencies.json").write_text(json.dumps(resolved, indent=2) + "\n")
        run(["lake", "build"], "final-build.log")
        (evidence / "AxiomAudit.lean").write_text(audit_source(found))
        run(["lake", "env", "lean", "evidence/AxiomAudit.lean"], "theorems-and-axioms.log")
        statements, axioms = parse_audit((evidence / "theorems-and-axioms.log").read_text(), found)
        (evidence / "assumptions.json").write_text(
            json.dumps(assumptions(found, statements, axioms), indent=2, ensure_ascii=False) + "\n")
        require(before == inputs(root), "source_drift_during_run", "Inputs changed during verification")
        record.update(status="passed", exit_code=0, source_sha256=before,
                      evidence_sha256={name: sha256(root / name) for name in sorted(EVIDENCE_FILES)},
                      declarations=list(found), axioms=axioms)
        record.pop("failure", None)
        save()
        check_evidence(root)
    except (EvidenceError, OSError, TypeError, KeyError) as exc:
        record.update(status="failed", exit_code=1,
                      failure={"error": getattr(exc, "code", "invalid_evidence"), "detail": str(exc)})
        save()
    return record["exit_code"]


if __name__ == "__main__":
    root = pathlib.Path(__file__).resolve().parents[1]
    status = verify(root)
    print(json.dumps({"exit_code": status, "validation": str(root / "evidence/validation.json")}, indent=2))
    sys.exit(status)
