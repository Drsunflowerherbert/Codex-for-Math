#!/usr/bin/env python3
"""Independently rebuild local Lean modules and record exact declaration evidence.

The source inventory, exact `#check @name` types, definition/structure bodies,
`#print axioms` results, and complete subprocess output are saved as JSON.
Only Python's standard library is used; Lean is invoked through with-lean.sh.
This checker is independent of the authors of the project's Lean proofs.

The axiom allowlist consists of Lean's standard propext, Classical.choice,
and Quot.sound. No custom axiom, sorry/admit, unsafe, native_decide, or
implemented_by token is accepted in local source code. Comments and strings
are masked before the source scan. Mathematical statement review remains a
separate task: successful compilation cannot identify a wrongly stated goal.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
FORBIDDEN = re.compile(r"\b(?:sorry|admit|axiom|unsafe|native_decide|implemented_by)\b")
DECLARATION = re.compile(
    r"(?:(?:@\[[^\n]*\]|noncomputable|protected)\s+)*"
    r"(theorem|lemma|def|abbrev|structure|inductive|opaque)\s+([^\s:(]+)"
)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mask_comments_and_strings(text):
    """Preserve newlines/columns while masking nested Lean comments and strings."""
    chars = list(text)
    i, depth, quoted = 0, 0, False
    while i < len(text):
        pair = text[i:i+2]
        if depth:
            if pair == "/-":
                chars[i:i+2] = "  "
                depth += 1
                i += 2
            elif pair == "-/":
                chars[i:i+2] = "  "
                depth -= 1
                i += 2
            else:
                if text[i] != "\n":
                    chars[i] = " "
                i += 1
        elif quoted:
            if text[i] == "\\":
                chars[i] = " "
                if i+1 < len(text) and text[i+1] != "\n":
                    chars[i+1] = " "
                i += 2
            elif text[i] == '"':
                chars[i] = " "
                quoted = False
                i += 1
            else:
                if text[i] != "\n":
                    chars[i] = " "
                i += 1
        elif pair == "/-":
            chars[i:i+2] = "  "
            depth = 1
            i += 2
        elif pair == "--":
            end = text.find("\n", i)
            end = len(text) if end < 0 else end
            chars[i:end] = " "*(end-i)
            i = end
        elif text[i] == '"':
            chars[i] = " "
            quoted = True
            i += 1
        else:
            i += 1
    return "".join(chars)


def declaration_inventory(path, project):
    """Inventory explicitly named public declarations in ordinary module syntax.

    Anonymous instances and compiler-generated helper names are not counted.
    Private theorem dependencies are still followed by Lean's axiom collector.
    The complete queried declaration list is exposed in the report.
    """
    code = mask_comments_and_strings(path.read_text())
    namespace, declarations = [], []
    for line_number, line in enumerate(code.splitlines(), 1):
        stripped = line.strip()
        match = re.fullmatch(r"namespace\s+(\S+)", stripped)
        if match:
            namespace.append(match.group(1))
        match = re.fullmatch(r"end\s+(\S+)", stripped)
        if match and namespace and namespace[-1] == match.group(1):
            namespace.pop()
        match = DECLARATION.match(stripped)
        if match:
            kind, name = match.groups()
            name = name.split(".{", 1)[0]
            declarations.append({"name": ".".join(namespace+[name]), "kind": kind,
                                 "source_line": line_number})
    forbidden = [{"file": path.relative_to(project).as_posix(), "token": match.group(),
                  "source_line": code.count("\n", 0, match.start())+1}
                 for match in FORBIDDEN.finditer(code)]
    return declarations, forbidden


def completed_command(command, project, timeout):
    try:
        completed = subprocess.run(command, cwd=project, text=True,
                                   capture_output=True, timeout=timeout, check=False)
        return {"command": command, "returncode": completed.returncode,
                "stdout": completed.stdout, "stderr": completed.stderr}
    except subprocess.TimeoutExpired as exc:
        decode = lambda value: value.decode(errors="replace") if isinstance(value, bytes) else (value or "")
        return {"command": command, "returncode": 124, "timeout_seconds": timeout,
                "stdout": decode(exc.stdout), "stderr": decode(exc.stderr)}


def source_files(project, requested_modules=None):
    if requested_modules:
        return [project/(name.replace(".", "/")+".lean") for name in requested_modules]
    paths = sorted((project/"MixedMoments").rglob("*.lean"))
    if (project/"MixedMoments.lean").exists():
        paths.insert(0, project/"MixedMoments.lean")
    return paths


def run(project, requested_modules=None, timeout=1800):
    files = source_files(project, requested_modules)
    if not files:
        raise ValueError("No Lean modules found")
    modules = [path.relative_to(project).with_suffix("").as_posix().replace("/", ".") for path in files]
    inputs, forbidden = {}, []
    for path, module in zip(files, modules):
        declarations, hits = declaration_inventory(path, project)
        inputs[module] = {"source_file": path.relative_to(project).as_posix(),
                          "source_sha256": sha256(path), "declarations": declarations}
        forbidden.extend(hits)
    configuration = {name: sha256(project/name) for name in
                     ("lean-toolchain", "lakefile.toml", "lake-manifest.json", "scripts/with-lean.sh")
                     if (project/name).exists()}
    declarations = [decl for item in inputs.values() for decl in item["declarations"]]
    names = [decl["name"] for decl in declarations]
    if len(set(names)) != len(names):
        raise AssertionError("Duplicate declaration names in source inventory")
    theorem_names = [decl["name"] for decl in declarations if decl["kind"] in ("theorem", "lemma")]
    definition_names = [decl["name"] for decl in declarations if decl["kind"] not in ("theorem", "lemma")]
    imports = [f"import {module}" for module in modules]
    axiom_query = "\n".join(imports+[f"#print axioms {name}" for name in theorem_names])+"\n"
    # @ exposes all implicit binders. Full names disambiguate rational moments,
    # analytic moments, series, and distinct kernels in different namespaces.
    type_query = "\n".join(imports+[
        "set_option pp.universes true", "set_option pp.fullNames true", "set_option format.width 120",
    ]+[f"#check @{name}" for name in names])+"\n"
    definition_query = "\n".join(imports+[
        "set_option pp.universes true", "set_option pp.fullNames true", "set_option format.width 120",
    ]+[f"#print {name}" for name in definition_names])+"\n"
    build = completed_command(["bash", "scripts/with-lean.sh", "lake", "build", *modules], project, timeout)
    skipped = {"command": [], "returncode": 99, "stdout": "", "stderr": "Skipped because the build failed"}
    queries = {}
    with tempfile.TemporaryDirectory(prefix="mm-independent-lean-audit-") as scratch:
        for label, source in (("axioms", axiom_query), ("types", type_query), ("definitions", definition_query)):
            query = Path(scratch)/(label+".lean")
            query.write_text(source)
            result = completed_command(["bash", "scripts/with-lean.sh", "lake", "env", "lean", str(query)],
                                       project, timeout) if build["returncode"] == 0 else skipped.copy()
            if result["command"]:
                result["command"][-1] = "<scratch>/"+query.name
            result["query_source"] = source
            queries[label] = result

    axiom_results = []
    axiom_output = queries["axioms"]["stdout"]
    for match in re.finditer(r"(?m)^'([^']+)' depends on axioms:\s*\[([^\]]*)\]", axiom_output):
        axiom_results.append({"declaration": match.group(1),
                              "axioms": [item.strip() for item in match.group(2).split(",") if item.strip()]})
    for match in re.finditer(r"(?m)^'([^']+)' does not depend on any axioms$", axiom_output):
        axiom_results.append({"declaration": match.group(1), "axioms": []})
    source_unchanged = {module: sha256(path) == inputs[module]["source_sha256"]
                        for module, path in zip(modules, files)}
    configuration_unchanged = {name: sha256(project/name) == before for name, before in configuration.items()}
    module_inventory_unchanged = source_files(project, requested_modules) == files
    exact_inventory = sorted(item["declaration"] for item in axiom_results) == sorted(theorem_names)
    allowed = all(set(item["axioms"]) <= ALLOWED_AXIOMS for item in axiom_results)
    passed = (build["returncode"] == 0 and all(query["returncode"] == 0 for query in queries.values())
              and exact_inventory and allowed and not forbidden and all(source_unchanged.values())
              and all(configuration_unchanged.values()) and module_inventory_unchanged)
    return {
        "schema_version": 2, "status": "passed" if passed else "failed_or_changed_during_audit",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "checker_sha256": sha256(Path(__file__).resolve()),
        "scope": "Independent rebuild, exact public declaration types and interface definitions, public theorem axiom inspection, and preservation checks",
        "inventory_scope": "Explicitly named public theorem/lemma/def/abbrev/structure/inductive/opaque declarations; anonymous instances and generated helper names are not separately counted",
        "build": build, "queries": queries, "inputs": inputs,
        "module_count": len(modules), "public_declaration_count": len(declarations),
        "public_theorem_count": len(theorem_names), "public_definition_count": len(definition_names),
        "axiom_result_count": len(axiom_results), "exact_axiom_declaration_inventory_match": exact_inventory,
        "all_axioms_allowed": allowed, "allowed_axioms": sorted(ALLOWED_AXIOMS),
        "forbidden_source_tokens": forbidden, "axiom_results": axiom_results,
        "source_unchanged_during_audit": source_unchanged,
        "configuration_sha256": configuration, "configuration_unchanged_during_audit": configuration_unchanged,
        "module_inventory_unchanged_during_audit": module_inventory_unchanged,
        "limits": ["The standard Lean axioms are permitted; no additional local axioms or placeholder proofs are permitted.",
                   "Compilation and axiom checking verify the stated types, not their correspondence with an informal problem.",
                   "Independent mathematical scope review is documented separately in docs/lean-independent-review.md."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=PROJECT)
    parser.add_argument("--module", action="append", help="Limit the audit to this module; may be repeated")
    parser.add_argument("--output", type=Path, default=Path("logs/certificates-lean-final-audit.json"))
    parser.add_argument("--timeout", type=int, default=1800, help="Timeout in seconds for each Lean process")
    args = parser.parse_args()
    project = args.project.resolve()
    report = run(project, args.module, args.timeout)
    output = args.output if args.output.is_absolute() else project/args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": report["status"], "module_count": report["module_count"],
                      "public_declaration_count": report["public_declaration_count"],
                      "public_theorem_count": report["public_theorem_count"],
                      "public_definition_count": report["public_definition_count"],
                      "all_axioms_allowed": report["all_axioms_allowed"],
                      "source_unchanged": all(report["source_unchanged_during_audit"].values()),
                      "output": str(output)}, indent=2))
    raise SystemExit(0 if report["status"] == "passed" else 1)


if __name__ == "__main__":
    main()
