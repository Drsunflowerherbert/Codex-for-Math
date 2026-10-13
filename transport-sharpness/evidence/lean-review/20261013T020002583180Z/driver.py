#!/usr/bin/env python3
"""Independent, fresh finite/scalar Lean review; no update/download operation.

This is a custom scoped audit using the published helper, not a live.cjs receipt
or an independent kernel implementation. Local project oleans are excluded.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

PIN_COMMIT = "797c613eb9b6d4ec95db23e3e00af9ac6657f24b"
MEMBERS = {
    "bin/lean": (9024, "8fadc3ed92cc9decb94c96ee9c0876e91e03a3a5e69138f32114f02789e2766c"),
    "lib/lean/libleanshared.so": (193479936, "8cc9858cc57c52015ba6dd948bdbf7f05926b9b5fcead69a964f0ad61ddd79dd"),
    "lib/lean/libleanshared_1.so": (6232, "6ce912e300ad305bb38a362404544602e2229d072b78d75b1dd71c637e453c2c"),
    "lib/lean/libleanshared_2.so": (6232, "6ce912e300ad305bb38a362404544602e2229d072b78d75b1dd71c637e453c2c"),
    "lib/lean/libInit_shared.so": (6232, "6ce912e300ad305bb38a362404544602e2229d072b78d75b1dd71c637e453c2c"),
}
HELPER_SHA = "bb71282fcb088498a9c40b0460694f1663e8f3a145fc15469050b8ade2f390dc"


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def digest(path):
    data = path.read_bytes()
    return {"bytes": len(data), "sha256": sha(data)}


def require(condition, explanation):
    if not condition:
        raise ValueError(explanation)


def lean_code(text):
    """Remove line/nested block comments and string literals for lexical audit."""
    pieces = []
    i = 0
    while i < len(text):
        if text.startswith("--", i):
            pieces.append(" ")
            end = text.find("\n", i)
            i = len(text) if end == -1 else end
        elif text.startswith("/-", i):
            pieces.append(" ")
            depth = 1
            i += 2
            while depth and i < len(text):
                if text.startswith("/-", i):
                    depth += 1
                    i += 2
                elif text.startswith("-/", i):
                    depth -= 1
                    i += 2
                else:
                    i += 1
            require(depth == 0, "unterminated Lean block comment")
        elif text[i] == '"':
            pieces.append(" ")
            i += 1
            while i < len(text) and text[i] != '"':
                i += 2 if text[i] == "\\" else 1
            require(i < len(text), "unterminated Lean string")
            i += 1
        else:
            pieces.append(text[i])
            i += 1
    return "".join(pieces)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", required=True)
    parser.add_argument("--lake", required=True)
    parser.add_argument("--elan-home", required=True)
    parser.add_argument("--toolkit", required=True)
    args = parser.parse_args()
    project = Path(__file__).resolve().parents[2]
    toolkit = Path(args.toolkit).resolve()
    lean = Path(args.lean).resolve()
    attempt = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    logs = project / "evidence" / "lean-review" / attempt
    logs.mkdir()
    private = project / ".cache" / "lean-review" / attempt
    work = private / "inputs"
    cache = private / "cache"
    work.mkdir(parents=True)
    cache.mkdir()
    env = dict(os.environ, ELAN_HOME=str(Path(args.elan_home).resolve()))
    report = {"schema": "scoped-independent-lean-review/v1", "attempt": attempt,
              "started": now(), "status": "in_progress", "phases": [],
              "invocation": {"pythonExecutable": sys.executable, "argv": sys.argv,
                             "optimizationLevel": sys.flags.optimize, "guards": "explicit_require_not_assert"},
              "boundaries": {"nativeMacMRS": "not_performed", "independentKernel": "not_performed",
                             "dependencySourceRebuild": "not_performed", "hostRuntime": "trusted",
                             "dependencyOleans": "trusted_pinned_cache", "measureTheoryBridge": "not_formalized"}}
    report_path = logs / "report.json"

    def save():
        report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")

    def step(name, argv, cwd=project, run_env=env):
        started = now()
        process = subprocess.run([str(a) for a in argv], cwd=cwd, env=run_env,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=600)
        paths = {}
        for stream, data in (("stdout", process.stdout), ("stderr", process.stderr)):
            path = logs / (name + "." + stream)
            path.write_bytes(data)
            paths[stream] = {"path": str(path.relative_to(project)), "bytes": len(data), "sha256": sha(data)}
        report["phases"].append({"name": name, "argv": [str(a) for a in argv], "cwd": str(cwd),
                                 "started": started, "finished": now(), "exitCode": process.returncode,
                                 "environment": {"ELAN_HOME": run_env.get("ELAN_HOME"), "LEAN_PATH": run_env.get("LEAN_PATH")},
                                 "outputs": paths})
        save()
        require(process.returncode == 0, name + " failed; see " + str(logs))
        return process.stdout

    save()
    try:
        report["runner"] = digest(Path(__file__))
        (logs / "driver.py").write_bytes(Path(__file__).read_bytes())
        configuration = [project / "lean-toolchain", project / "lakefile.toml", project / "lake-manifest.json"]
        report["configuration"] = [{"path": str(p.relative_to(project)), **digest(p)} for p in configuration]
        release = lean.parent.parent
        report["compilerMembers"] = {}
        for member, (size, expected) in MEMBERS.items():
            actual = digest(release / member)
            require(actual == {"bytes": size, "sha256": expected}, "compiler member differs: " + member)
            report["compilerMembers"][member] = actual
        version = step("compiler-version", [lean, "--version"]).decode().strip()
        commit = step("compiler-commit", [lean, "--githash"]).decode().strip()
        require("version 4.24.0," in version and commit == PIN_COMMIT, "compiler version or commit differs from pin")
        report["compilerVersion"] = version
        report["compilerCommit"] = commit
        lock = json.loads((project / "lake-manifest.json").read_text())
        report["packages"] = []
        for package in lock["packages"]:
            path = project / lock["packagesDir"] / package["name"]
            head = step("package-" + package["name"] + "-head", ["git", "rev-parse", "HEAD"], path).decode().strip()
            origin = step("package-" + package["name"] + "-origin", ["git", "config", "--get", "remote.origin.url"], path).decode().strip()
            clean = step("package-" + package["name"] + "-clean", ["git", "status", "--porcelain", "--untracked-files=no"], path)
            require(head == package["rev"], "package HEAD differs: " + package["name"])
            require(origin.rstrip("/").removesuffix(".git") == package["url"].rstrip("/").removesuffix(".git"), "package origin differs: " + package["name"])
            require(not clean, "tracked package source is dirty: " + package["name"])
            report["packages"].append({"name": package["name"], "head": head, "origin": origin, "trackedSourceClean": True})
        pathtext = step("dependency-search-path", [args.lake, "env", "/usr/bin/printenv", "LEAN_PATH"]).decode().strip()
        dependencies = [str(Path(p).resolve()) for p in pathtext.split(os.pathsep)
                        if Path(p).resolve() != (project / ".lake/build/lib/lean").resolve()]
        expected_paths = [str((project / lock["packagesDir"] / p["name"] / ".lake/build/lib/lean").resolve()) for p in lock["packages"]]
        expected_paths.append(str((release / "lib/lean").resolve()))
        require(sorted(dependencies) == sorted(expected_paths), "dependency search path differs from pinned package paths")
        run_env = dict(env, LEAN_PATH=os.pathsep.join([str(cache)] + dependencies))
        mappings = [
            (toolkit / "lean/EvidenceHarness.lean", "EvidenceHarness.lean", "EvidenceHarness"),
            (project / "TransportSharpness/Finite.lean", "TransportSharpness/Finite.lean", "TransportSharpness.Finite"),
            (project / "TransportSharpness/Obstruction.lean", "TransportSharpness/Obstruction.lean", "TransportSharpness.Obstruction"),
            (project / "TransportSharpness.lean", "TransportSharpness.lean", "TransportSharpness"),
            (project / "scripts/ReviewHarness.lean", "ReviewHarness.lean", "ReviewHarness"),
            (project / "scripts/Replay.lean", "Replay.lean", "Replay"),
        ]
        require(digest(mappings[0][0])["sha256"] == HELPER_SHA, "published helper source differs from pin")
        report["lexicalSourceAudit"] = []
        for original, _, _ in mappings[1:4]:
            bad = re.findall(r"\b(sorry|admit|axiom|unsafe|partial|native_decide|skipKernelTC)\b", lean_code(original.read_text()))
            require(not bad, "forbidden Lean source tokens in " + str(original) + ": " + str(bad))
            report["lexicalSourceAudit"].append({"path": str(original.relative_to(project)), "status": "no_forbidden_code_tokens"})
        report["sources"] = []
        for original, destination, module in mappings:
            copied = work / destination
            copied.parent.mkdir(parents=True, exist_ok=True)
            copied.write_bytes(original.read_bytes())
            report["sources"].append({"original": str(original), "module": module, **digest(original)})
        report["products"] = []
        for original, destination, module in mappings:
            out = cache / (module.replace(".", "/") + ".olean")
            out.parent.mkdir(parents=True, exist_ok=True)
            step("compile-" + module, [lean, "--json", "--root=" + str(work), "-o", out, work / destination], work, run_env)
            report["products"].append({"module": module, **digest(out), "archived": False})
        targets, definitions, replays = [], [], []
        for line in (logs / "compile-ReviewHarness.stdout").read_text().splitlines():
            message = json.loads(line)
            for prefix, output in (("MATH_EVIDENCE_TARGET ", targets), ("MATH_EVIDENCE_DEFINITION ", definitions)):
                if message.get("data", "").startswith(prefix):
                    require(message["severity"] == "information", "non-information target or definition marker")
                    output.append(json.loads(message["data"][len(prefix):]))
        for line in (logs / "compile-Replay.stdout").read_text().splitlines():
            message = json.loads(line)
            if message.get("data", "").startswith("MATH_EVIDENCE_REPLAY "):
                require(message["severity"] == "information", "non-information replay marker")
                replays.append(json.loads(message["data"][len("MATH_EVIDENCE_REPLAY "):]))
        names = []
        defs = []
        kinds = {}
        for original, _, _ in mappings[1:3]:
            for kind, name in re.findall(r"^(abbrev|def|theorem) (\w+)", original.read_text(), re.M):
                names.append("TransportSharpness." + name)
                kinds["TransportSharpness." + name] = "theorem" if kind == "theorem" else "definition"
                if kind != "theorem":
                    defs.append("TransportSharpness." + name)
        require(len(targets) == len(names) and sorted(t["target"] for t in targets) == sorted(names), "target name coverage differs")
        require(all(t["declarationKind"] == kinds[t["target"]] for t in targets), "target declaration kind differs")
        require(len(definitions) == len(defs) and sorted(d["target"] for d in definitions) == sorted(defs), "definition name coverage differs")
        require(len(replays) == 1 and sorted(replays[0]["targets"]) == sorted(names), "replay target coverage differs")
        require(replays[0]["baseModules"] == ["Mathlib", "EvidenceHarness"] and replays[0]["independentKernelReplay"] == "not_performed", "unexpected replay baseline or scope")
        require(all(t["typeMatching"] == "closed_whole_type_kernel_definitional_equality" for t in targets), "unexpected type-matching contract")
        require(all(d["definitionBodyMatching"] == "kernel_definitional_equality" for d in definitions), "unexpected body-matching contract")
        require(all(set(t["axioms"]) <= {"propext", "Classical.choice", "Quot.sound"} for t in targets + definitions), "unapproved axiom closure")
        for (original, destination, _), source in zip(mappings, report["sources"]):
            require(digest(original) == digest(work / destination) == {"bytes": source["bytes"], "sha256": source["sha256"]}, "source or copied source changed: " + str(original))
        require(digest(Path(__file__)) == digest(logs / "driver.py") == report["runner"], "runner or runner snapshot changed")
        for path, captured in zip(configuration, report["configuration"]):
            require(digest(path) == {"bytes": captured["bytes"], "sha256": captured["sha256"]}, "configuration changed: " + str(path))
        for product in report["products"]:
            out = cache / (product["module"].replace(".", "/") + ".olean")
            require(digest(out) == {"bytes": product["bytes"], "sha256": product["sha256"]}, "compiled product changed: " + product["module"])
        for member, actual in report["compilerMembers"].items():
            require(digest(release / member) == actual, "compiler/runtime changed: " + member)
        for package in lock["packages"]:
            path = project / lock["packagesDir"] / package["name"]
            require(step("post-package-" + package["name"] + "-head", ["git", "rev-parse", "HEAD"], path).decode().strip() == package["rev"], "postflight package HEAD differs")
            origin = step("post-package-" + package["name"] + "-origin", ["git", "config", "--get", "remote.origin.url"], path).decode().strip()
            require(origin.rstrip("/").removesuffix(".git") == package["url"].rstrip("/").removesuffix(".git"), "postflight package origin differs")
            require(not step("post-package-" + package["name"] + "-clean", ["git", "status", "--porcelain", "--untracked-files=no"], path), "postflight tracked package source is dirty")
        for phase in report["phases"]:
            for artifact in phase["outputs"].values():
                require(digest(project / artifact["path"]) == {"bytes": artifact["bytes"], "sha256": artifact["sha256"]}, "captured phase output changed")
        report.update(status="passed", targets=targets, definitions=definitions, replay=replays[0],
                      sourcePostflight="original_and_copies_unchanged", postflight="sources_config_helper_runner_compiler_products_outputs_packages_unchanged", finished=now())
        save()
        print(json.dumps({"status": "passed", "report": str(report_path.relative_to(project)),
                          "wholeTypes": len(targets), "definitionBodies": len(definitions),
                          "replayedDeclarations": replays[0]["replayedDeclarations"]}))
    except BaseException as exc:
        report.update(status="failed", failure=str(exc), finished=now())
        save()
        raise


if __name__ == "__main__":
    main()
