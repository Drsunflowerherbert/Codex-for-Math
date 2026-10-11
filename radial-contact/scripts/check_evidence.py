#!/usr/bin/env python3
"""Check this library's recorded evidence without invoking Lean or changing files."""
import argparse
import hashlib
import json
import pathlib
import re
import sys
import tomllib

LEAN_TOOLCHAIN = "leanprover/lean4:v4.24.0"
MATHLIB_COMMIT = "f897ebcf72cd16f89ab4577d0c826cd14afaafc7"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
EVIDENCE_FILES = {
    "evidence/regression-tests.log", "evidence/toolchain-current.log",
    "evidence/resolved-dependencies.json", "evidence/final-build.log",
    "evidence/AxiomAudit.lean", "evidence/theorems-and-axioms.log",
    "evidence/assumptions.json",
}
COMMANDS = [
    ["python", "-m", "unittest", "discover", "-s", "tests", "-v"],
    ["lake", "env", "lean", "--version"], ["lake", "build"],
    ["lake", "env", "lean", "evidence/AxiomAudit.lean"],
]
COMMAND_LOGS = ["evidence/regression-tests.log", "evidence/toolchain-current.log",
                "evidence/final-build.log", "evidence/theorems-and-axioms.log"]


class EvidenceError(Exception):
    def __init__(self, code, detail):
        self.code, self.detail = code, detail
        super().__init__(f"{code}: {detail}")


def require(condition, code, detail):
    if not condition:
        raise EvidenceError(code, detail)


def sha256(path):
    require(path.is_file(), "missing_file", str(path))
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    require(path.is_file(), "missing_file", str(path))
    try:
        return json.loads(path.read_text())
    except (ValueError, UnicodeError) as exc:
        raise EvidenceError("malformed_json", str(path)) from exc


def inputs(root):
    required = ["RadialContact.lean", "lean-toolchain", "lakefile.toml",
                "lake-manifest.json", "README.md", "ASSUMPTIONS.md",
                "scripts/verify.py", "scripts/check_evidence.py", "tests/test_repro.py"]
    paths = {root / name for name in required}
    paths.update((root / "RadialContact").rglob("*.lean"))
    paths.update((root / "scripts").glob("*.py"))
    paths.update((root / "tests").glob("*.py"))
    require((root / "RadialContact/Basic.lean").is_file(), "missing_file", "RadialContact/Basic.lean")
    return {str(p.relative_to(root)): sha256(p) for p in sorted(paths)}


def lean_code(text):
    """Blank nested comments and strings while retaining line boundaries."""
    out, i, depth, quoted = [], 0, 0, False
    while i < len(text):
        pair, char = text[i:i + 2], text[i]
        if depth:
            if pair == "/-":
                depth += 1; out.extend("  "); i += 2; continue
            if pair == "-/":
                depth -= 1; out.extend("  "); i += 2; continue
            out.append("\n" if char == "\n" else " "); i += 1; continue
        if quoted:
            if char == "\\" and i + 1 < len(text):
                out.extend("  "); i += 2; continue
            if char == '"':
                quoted = False
            out.append("\n" if char == "\n" else " "); i += 1; continue
        if pair == "/-":
            depth = 1; out.extend("  "); i += 2; continue
        if pair == "--":
            end = text.find("\n", i)
            if end < 0:
                end = len(text)
            out.extend(" " * (end - i)); i = end; continue
        if char == '"':
            quoted = True; out.append(" "); i += 1; continue
        out.append(char); i += 1
    require(not depth and not quoted, "source_syntax", "Unclosed Lean comment or string")
    return "".join(out)


def declarations(root):
    found = {}
    for path in [root / "RadialContact.lean", *sorted((root / "RadialContact").rglob("*.lean"))]:
        code = lean_code(path.read_text())
        require(not re.search(r"\b(?:sorry|admit|axiom|unsafe)\b", code),
                "forbidden_source", str(path.relative_to(root)))
        unsupported = r"(?m)^\s*(?:@\[[^\]]+\]\s*)*(?:(?:noncomputable|private|protected)\s+)*(?:opaque|class|structure|inductive|instance|constant|alias|export)\b"
        require(not re.search(unsupported, code) and not re.search(r"(?m)^\s*(?:private|protected)\b", code),
                "unsupported_source", "Auditor supports this library's public theorem/def/abbrev syntax: " + str(path))
        namespaces = re.findall(r"(?m)^\s*namespace\s+(\S+)", code)
        require(all(n == "RadialContact" for n in namespaces), "unsupported_namespace", str(path))
        pattern = r"(?m)^[ \t]*(?:@\[[^\]]+\]\s*)*(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev)\s+(\w+)"
        for name in re.findall(pattern, code):
            name = "RadialContact." + name
            require(name not in found, "duplicate_declaration", name)
            found[name] = str(path.relative_to(root))
    require(bool(found), "empty_declarations", "No library declarations found")
    return found


def audit_source(names):
    lines = ["import RadialContact", "set_option pp.universes true"]
    for name in names:
        lines.extend(["#check @" + name, "#print axioms " + name])
    return "\n".join(lines) + "\n"


def parse_audit(text, expected):
    require(not re.search(r"(?m)^.*(?:error|warning):", text), "audit_diagnostic", "Audit has diagnostics")
    statements, axioms, current, body = {}, {}, None, []
    for line in text.splitlines():
        start = re.match(r"^@?(RadialContact\.\w+)(?:\.\{[^}]*\})?\s*:", line)
        dependency = re.match(r"^'(RadialContact\.\w+)' depends on axioms:\s*\[([^]]*)\]\s*$", line)
        no_axioms = re.match(r"^'(RadialContact\.\w+)' does not depend on any axioms\s*$", line)
        if start:
            require(current is None, "missing_axiom_record", current or "")
            current, body = start[1], [line]
            require(current not in statements, "duplicate_statement", current)
        elif dependency or no_axioms:
            match = dependency or no_axioms
            name = match[1]
            require(current == name, "unpaired_audit", name)
            require(name not in axioms, "duplicate_axiom_record", name)
            dependencies = sorted({x.strip() for x in dependency[2].split(",") if x.strip()}) if dependency else []
            require(not (set(dependencies) - ALLOWED_AXIOMS), "unexpected_axiom", name + ": " + str(dependencies))
            statements[name], axioms[name] = "\n".join(body), dependencies
            current, body = None, []
        elif current is not None:
            body.append(line)
        else:
            require(not line.strip(), "unexpected_audit_output", line)
    require(current is None, "missing_axiom_record", current or "")
    require(set(statements) == set(expected) and set(axioms) == set(expected),
            "audit_coverage", "Missing or extra statement/axiom records")
    return statements, axioms


def assumptions(found, statements, axioms):
    inventory = {}
    for name, source in found.items():
        statement = statements[name]
        extra = re.findall(r"\b(?:CompleteSpace|FiniteDimensional|StrictConvexSpace|Nonempty|Nontrivial)\b", statement)
        require(not extra, "unexpected_assumption", name + ": " + str(extra))
        classes = sorted(set(re.findall(r"\b(?:NormedAddCommGroup|NormedSpace|Subsingleton)\b", statement)))
        inventory[name] = {"source": source, "statement": statement,
                           "explicit_class_names": classes, "axioms": axioms[name]}
    return {"domains": {"InteriorCenter": "norm(c) < 1", "UnitSphere": "norm(v) = 1"},
            "interpretation": "The complete compiled type is authoritative; class names are a searchable summary.",
            "declarations": inventory}


def check_pins(root):
    require((root / "lean-toolchain").read_text().strip() == LEAN_TOOLCHAIN,
            "toolchain_pin", "Expected Lean 4.24.0")
    manifest = read_json(root / "lake-manifest.json")
    require(isinstance(manifest, dict), "dependency_pin", "Manifest must be an object")
    packages = manifest.get("packages", [])
    require(bool(packages), "dependency_pin", "Empty dependency manifest")
    names = [p.get("name") for p in packages]
    require(len(set(names)) == len(names), "dependency_pin", "Duplicate package names")
    for package in packages:
        require(package.get("type") == "git" and bool(re.fullmatch(r"[0-9a-f]{40}", package.get("rev", ""))),
                "dependency_pin", str(package.get("name")))
    mathlib = next((p for p in packages if p.get("name") == "mathlib"), {})
    require(mathlib.get("rev") == MATHLIB_COMMIT and
            mathlib.get("url") == "https://github.com/leanprover-community/mathlib4.git",
            "dependency_pin", "Unexpected mathlib revision or origin")
    try:
        configuration = tomllib.loads((root / "lakefile.toml").read_text())
    except tomllib.TOMLDecodeError as exc:
        raise EvidenceError("dependency_pin", "Invalid Lake TOML") from exc
    requirement = next((p for p in configuration.get("require", []) if p.get("name") == "mathlib"), {})
    require(requirement.get("rev") == MATHLIB_COMMIT and
            requirement.get("git") == mathlib.get("url"),
            "dependency_pin", "Lake configuration does not pin the official mathlib commit")
    return {p["name"]: p["rev"] for p in packages}


def check_evidence(root):
    record = read_json(root / "evidence/validation.json")
    require(isinstance(record, dict), "evidence_schema", "Validation must be an object")
    require(record.get("schema_version") == 2, "evidence_schema", "Expected v2 evidence")
    require(record.get("status") == "passed" and record.get("exit_code") == 0,
            "failed_verification", str(record.get("failure", "Verification did not pass")))
    require(record.get("source_sha256") == inputs(root), "source_drift", "Recorded inputs differ from current files")
    pins = check_pins(root)
    hashes = record.get("evidence_sha256", {})
    require(isinstance(hashes, dict), "evidence_coverage", "Evidence hashes must be an object")
    require(set(hashes) == EVIDENCE_FILES, "evidence_coverage", "Missing or extra evidence hash entries")
    for name, digest in hashes.items():
        require(sha256(root / name) == digest, "stale_evidence", name)
    commands = record.get("records", [])
    require(len(commands) == len(COMMANDS), "command_coverage", "Missing execution records")
    for observed, expected, logfile in zip(commands, COMMANDS, COMMAND_LOGS):
        command = observed.get("command", [])
        if expected[0] == "python":
            require(command[1:] == expected[1:], "command_coverage", str(command))
        else:
            require(command == expected, "command_coverage", str(command))
        require(observed.get("exit_code") == 0, "command_failed", str(command))
        require(observed.get("log") == logfile, "command_coverage", "Wrong log for " + str(command))
    tests = (root / "evidence/regression-tests.log").read_text()
    require(bool(re.search(r"Ran [1-9][0-9]* tests?", tests)) and bool(re.search(r"(?m)^OK$", tests)),
            "regression_coverage", "No successful test run recorded")
    require(read_json(root / "evidence/resolved-dependencies.json") == pins,
            "resolved_dependencies", "Recorded checkouts do not match the manifest")
    require("Lean (version 4.24.0," in (root / "evidence/toolchain-current.log").read_text(),
            "toolchain_execution", "Unexpected compiler version")
    found = declarations(root)
    require((root / "evidence/AxiomAudit.lean").read_text() == audit_source(found),
            "stale_audit_source", "Audit commands differ from current declarations")
    statements, axioms = parse_audit((root / "evidence/theorems-and-axioms.log").read_text(), found)
    require(read_json(root / "evidence/assumptions.json") == assumptions(found, statements, axioms),
            "stale_assumptions", "Assumptions inventory differs from compiled statements")
    require(record.get("declarations") == list(found) and record.get("axioms") == axioms,
            "stale_summary", "Summary differs from complete audit output")
    return {"status": "passed", "declarations": len(found),
            "axioms_found": sorted({a for group in axioms.values() for a in group})}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        result = check_evidence(args.root.resolve())
    except (EvidenceError, OSError, TypeError, KeyError) as exc:
        print(json.dumps({"status": "failed", "error": getattr(exc, "code", "invalid_evidence"),
                          "detail": str(exc)}, indent=2))
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
