#!/usr/bin/env python3
"""Bounded full environment inventory and axiom supplement to audit_lean.py.

Run only after a successful frozen project build. Lean module provenance
selects every constant originating in MixedMoments or its submodules,
including private declarations, instances, and generated helpers. The query
records complete kernel Expr representations as well as readable full types,
and invokes #print axioms on every remaining selected name after reusing the
passed public theorem audit at identical source/config/checker hashes. Each
record states its axiom evidence source. It does not rebuild mathlib.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess

PROJECT = Path(__file__).resolve().parents[1]
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
EXPECTED_RUNTIME_HELPERS = {
    "MixedMoments.central._unsafe_rec", "MixedMoments.hStar._unsafe_rec",
    "MixedMoments.kminus._unsafe_rec", "MixedMoments.kplus._unsafe_rec",
    "MixedMoments.moment._unsafe_rec"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inputs(project):
    files = sorted((project / "MixedMoments").rglob("*.lean"))
    files += [project / name for name in (
        "MixedMoments.lean", "lean-toolchain", "lakefile.toml", "lake-manifest.json",
        "scripts/with-lean.sh", "scripts/audit_lean.py",
        "scripts/full_environment_inventory.lean", "scripts/audit_environment.py")]
    if (project / "logs/certificates-lean-final-audit.json").exists():
        files.append(project / "logs/certificates-lean-final-audit.json")
    return {p.relative_to(project).as_posix(): digest(p) for p in files}


def run(project, timeout):
    before = inputs(project)
    public_audit_path = project / "logs/certificates-lean-final-audit.json"
    public_audit = json.loads(public_audit_path.read_text()) if public_audit_path.exists() else None
    public_hashes_match_before = (public_audit is not None
                                 and all(before.get(v["source_file"]) == v["source_sha256"]
                                         for v in public_audit["inputs"].values())
                                 and all(before.get(k) == v for k, v in public_audit["configuration_sha256"].items())
                                 and before["scripts/audit_lean.py"] == public_audit["checker_sha256"])
    public_theorem_names = [d["name"] for m in public_audit["inputs"].values()
                            for d in m["declarations"] if d["kind"] in ("theorem", "lemma")] if public_audit else []
    public_results = public_audit["axiom_results"] if public_audit else []
    reused_by_name = {r["declaration"]: sorted(r["axioms"]) for r in public_results}
    public_reuse_eligible = (public_audit is not None and public_audit["status"] == "passed"
                            and public_hashes_match_before and public_audit["build"]["returncode"] == 0
                            and all(q["returncode"] == 0 for q in public_audit["queries"].values())
                            and sorted(reused_by_name) == sorted(public_theorem_names)
                            and len(public_results) == len(reused_by_name)
                            and all(set(a) <= ALLOWED_AXIOMS for a in reused_by_name.values()))
    expected_modules = {str(Path(p).with_suffix("")).replace("/", ".")
                        for p in before if p.endswith(".lean") and not p.startswith("scripts/")}
    command = ["bash", "scripts/with-lean.sh", "lake", "env", "lean",
               "scripts/full_environment_inventory.lean"]
    try:
        if not public_reuse_eligible:
            raise ValueError("Passed public theorem audit at identical source/config/checker hashes is required")
        result = subprocess.run(command, cwd=project, text=True,
                                capture_output=True, timeout=timeout, check=False)
        command_result = {"command": command, "returncode": result.returncode,
                          "stdout": result.stdout, "stderr": result.stderr}
    except subprocess.TimeoutExpired as exc:
        decode = lambda x: x.decode(errors="replace") if isinstance(x, bytes) else (x or "")
        command_result = {"command": command, "returncode": 124, "timeout_seconds": timeout,
                          "stdout": decode(exc.stdout), "stderr": decode(exc.stderr)}
    records, imported_modules, completion_count = [], None, 0
    for line in command_result["stdout"].splitlines():
        if line.startswith("MM_DECL_JSON "):
            records.append(json.loads(line[len("MM_DECL_JSON "):]))
        elif line.startswith("MM_MODULES_JSON "):
            if imported_modules is not None:
                raise ValueError("Duplicate imported-module inventory")
            imported_modules = json.loads(line[len("MM_MODULES_JSON "):])
        elif line == "MM_ENVIRONMENT_INVENTORY_COMPLETE":
            completion_count += 1
    printed = []
    for match in re.finditer(r"^'([^\n]+)' depends on axioms:\s*\[([^\]]*)\]",
                             command_result["stdout"], re.MULTILINE):
        printed.append({"declaration": match.group(1),
                        "axioms": [a.strip() for a in match.group(2).split(",") if a.strip()]})
    for match in re.finditer(r"^'([^\n]+)' does not depend on any axioms$",
                             command_result["stdout"], re.MULTILINE):
        printed.append({"declaration": match.group(1), "axioms": []})
    after = inputs(project)
    names = [r["name"] for r in records]
    unique = len(names) == len(set(names))
    printed_by_name = {r["declaration"]: sorted(r["axioms"]) for r in printed}
    expected_fresh_names = set(names) - set(reused_by_name)
    print_match = (len(printed) == len(expected_fresh_names) and len(printed_by_name) == len(printed)
                   and set(printed_by_name) == expected_fresh_names)
    reused_names_match = (set(reused_by_name) <= set(names)
                          and all(r["axiom_query_reused"] == (r["name"] in reused_by_name) for r in records))
    combined = {**reused_by_name, **printed_by_name}
    combined_match = (set(combined) == set(names) and reused_names_match and print_match)
    # The ordinary #print axioms command performs Lean.collectAxioms once per
    # declaration. Associate its full-name output rather than traverse twice.
    for record in records:
        record["axiom_result_resolved"] = record["name"] in combined
        record["axioms"] = combined.get(record["name"], [])
        record["axiom_evidence_source"] = (
            "logs/certificates-lean-final-audit.json ordinary #print axioms" if record["axiom_query_reused"]
            else "Current supplemental query ordinary #print axioms")
    modules_match = imported_modules is not None and set(imported_modules) == expected_modules
    allowed = all(set(r["axioms"]) <= ALLOWED_AXIOMS for r in records)
    unsafe_or_axioms = [r["name"] for r in records if r["unsafe"] or r["kind"] == "axiom"]
    scanner_spec = importlib.util.spec_from_file_location("mixed_moments_audit", project / "scripts/audit_lean.py")
    scanner = importlib.util.module_from_spec(scanner_spec)
    scanner_spec.loader.exec_module(scanner)
    public_names, public_definitions, forbidden, partial_source_tokens = [], set(), [], []
    for relative in before:
        if relative.endswith(".lean") and not relative.startswith("scripts/"):
            decls, hits = scanner.declaration_inventory(project / relative, project)
            public_names.extend(d["name"] for d in decls)
            public_definitions.update(d["name"] for d in decls if d["kind"] == "def")
            forbidden.extend(hits)
            masked = scanner.mask_comments_and_strings((project / relative).read_text())
            partial_source_tokens.extend({"file": relative, "token": m.group(),
                                          "source_line": masked.count("\n", 0, m.start()) + 1}
                                         for m in re.finditer(r"\b(?:partial|partial_fixpoint)\b", masked))
    records_by_name = {r["name"]: r for r in records}
    partial_records = [r for r in records if r["partial"]]
    recognized_runtime = []
    for r in partial_records:
        parent = r["compiler_runtime_parent"]
        parent_record = records_by_name.get(parent)
        if (r["name"] in EXPECTED_RUNTIME_HELPERS and r["kind"] == "definition"
                and not r["unsafe"] and parent in public_definitions
                and parent_record is not None and parent_record["kind"] == "definition"
                and not parent_record["unsafe"] and not parent_record["partial"]
                and r["name"] == parent + "._unsafe_rec"):
            recognized_runtime.append(r["name"])
    runtime_names = EXPECTED_RUNTIME_HELPERS
    kernel_runtime_references = [
        {"declaration": r["name"], "runtime_dependencies": sorted(set(r["direct_kernel_dependencies"]) & runtime_names)}
        for r in records if r["name"] not in runtime_names
        and set(r["direct_kernel_dependencies"]) & runtime_names]
    runtime_classification = (set(recognized_runtime) == EXPECTED_RUNTIME_HELPERS
                              and len(recognized_runtime) == len(partial_records)
                              and not partial_source_tokens and not kernel_runtime_references)
    source_safety = not unsafe_or_axioms and runtime_classification
    compiler_prefix = subprocess.run(
        ["bash", "scripts/with-lean.sh", "lean", "--print-prefix"], cwd=project,
        text=True, capture_output=True, check=False)
    if compiler_prefix.returncode != 0:
        raise RuntimeError("Cannot resolve the active Lean compiler prefix")
    compiler_source = (Path(compiler_prefix.stdout.strip())
                       / "src/lean/Lean/Elab/PreDefinition/Basic.lean")
    compiler_source_lines = compiler_source.read_text().splitlines()
    compiler_runtime_justification = {
        "compiler_source_file": str(compiler_source), "source_sha256": digest(compiler_source),
        "source_lines": "292-308", "source_excerpt": "\n".join(compiler_source_lines[291:308]),
        "explanation": "Lean.addAndCompilePartialRec generates Compiler.mkUnsafeRecName copies of ordinary recursive definitions with DefinitionSafety.partial for compiled execution. The safe source definitions have distinct kernel terms. Every project's type/value/constructor constant dependency is inspected to exclude all five runtime helper names from all other declarations."}
    missing_public = sorted(set(public_names) - set(names))
    public_axioms_match = (public_audit is not None and public_audit["status"] == "passed"
                           and all(combined.get(r["declaration"]) == sorted(r["axioms"])
                                   for r in public_audit["axiom_results"]))
    public_hashes_match = (public_audit is not None
                          and all(before.get(v["source_file"]) == v["source_sha256"]
                                  for v in public_audit["inputs"].values())
                          and all(before.get(k) == v for k, v in public_audit["configuration_sha256"].items())
                          and before["scripts/audit_lean.py"] == public_audit["checker_sha256"])
    passed = (command_result["returncode"] == 0 and completion_count == 1 and bool(records)
              and unique and combined_match and modules_match and allowed and source_safety
              and before == after and not missing_public and not forbidden
              and public_axioms_match and public_hashes_match)
    return {
        "schema_version": 1, "status": "passed" if passed else "failed_or_incomplete",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Every Lean Environment.constants declaration with imported module provenance MixedMoments or a submodule",
        "selection": "Lean Environment.getModuleIdxFor? and allImportedModuleNames; no declaration-name prefix filtering",
        "command": command_result, "input_sha256": before,
        "input_sha256_after": after, "inputs_unchanged": before == after,
        "imported_project_modules": imported_modules, "expected_project_modules": sorted(expected_modules),
        "module_inventory_matches_sources": modules_match,
        "declaration_count": len(records), "kind_counts": dict(Counter(r["kind"] for r in records)),
        "proposition_valued_count": sum(r["proposition_valued"] for r in records),
        "origin_module_counts": dict(Counter(r["origin_module"] for r in records)),
        "unique_declaration_names": unique, "completion_marker_count": completion_count,
        "allowed_axioms": sorted(ALLOWED_AXIOMS), "all_axioms_allowed": allowed,
        "all_local_declarations_nonunsafe_nonaxiom": not unsafe_or_axioms,
        "unsafe_or_axiom_declarations": unsafe_or_axioms,
        "partial_declarations": [r["name"] for r in partial_records],
        "recognized_compiler_runtime_helpers": recognized_runtime,
        "expected_compiler_runtime_helpers": sorted(EXPECTED_RUNTIME_HELPERS),
        "compiler_runtime_justification": compiler_runtime_justification,
        "compiler_runtime_helper_classification_valid": runtime_classification,
        "nonruntime_kernel_references_to_runtime_helpers": kernel_runtime_references,
        "partial_source_tokens": partial_source_tokens,
        "print_axiom_result_count": len(printed), "reused_public_axiom_result_count": len(reused_by_name),
        "combined_axiom_result_count": len(combined),
        "fresh_print_axiom_declaration_inventory_match": print_match,
        "reused_public_names_present_and_marked_exactly": reused_names_match,
        "exact_combined_axiom_declaration_inventory_match": combined_match,
        "source_public_declaration_count": len(public_names), "missing_source_public_names": missing_public,
        "forbidden_source_tokens": forbidden,
        "public_final_audit_sha256": digest(public_audit_path) if public_audit_path.exists() else None,
        "public_final_audit_reuse_eligible_before_execution": public_reuse_eligible,
        "public_final_audit_axioms_match": public_axioms_match,
        "public_final_audit_source_and_checker_hashes_match": public_hashes_match,
        "declarations": records, "printed_axiom_results": printed,
        "limits": [
            "Standard Lean logical axioms are permitted. Axiom sets come from ordinary #print axioms, which invokes Lean.collectAxioms once per queried declaration.",
            "Passed public theorem results are reused only after source/config/checker hash reconciliation and exact full kernel inventory inclusion; each record names its evidence source.",
            "Compiler-generated _unsafe_rec runtime implementations may carry the partial flag: each must have a safe nonpartial source definition as parent, be recognized by Lean.Compiler.mkUnsafeRecName, and be absent from every other local declaration's direct kernel dependencies. They remain included in the type/axiom inventory; local unsafe/axiom and source partial declarations are rejected.",
            "The type_expression field is the complete kernel Expr representation; type is its readable full-name pretty-print.",
            "This query audits the already built project; the separate public final audit records rebuilding and source definition bodies.",
            "Dependency origin is established by the imported environment, while exact compiler/package pins are separately evidenced.",
            "Compilation verifies the stated types; mathematical statement correspondence is independently reviewed."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=PROJECT)
    parser.add_argument("--output", type=Path, default=Path("logs/full-environment-audit.json"))
    parser.add_argument("--timeout", type=int, default=900)
    args = parser.parse_args()
    project = args.project.resolve()
    report = run(project, args.timeout)
    output = args.output if args.output.is_absolute() else project / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in (
        "status", "declaration_count", "kind_counts", "all_axioms_allowed", "inputs_unchanged",
        "module_inventory_matches_sources", "exact_combined_axiom_declaration_inventory_match",
        "public_final_audit_axioms_match", "public_final_audit_source_and_checker_hashes_match")}, indent=2))
    raise SystemExit(0 if report["status"] == "passed" else 1)


if __name__ == "__main__":
    main()
