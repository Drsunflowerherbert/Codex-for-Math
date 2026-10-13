#!/usr/bin/env python3
"""Fresh Lean-checked packages for supplied exact LP certificates.

The JSON-to-Lean transcription is trusted code, not a proved parser refinement.
No saved Lean source, command, receipt, or status is executed on recheck.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import shutil
import signal
import stat
import subprocess
import sys
import time
from typing import Any

import verifier


ROOT = Path(__file__).resolve().parent
MAX_INPUT_BYTES = 65536
MAX_DIMENSION = 8
MAX_ROWS = 16
MAX_BITS = 256
MAX_BATCH = 16
MAX_LOG_BYTES = 2 * 1024 * 1024
TIMEOUT_SECONDS = 240
ADDRESS_SPACE_BYTES = 16 * 1024**3
HELPER_SHA256 = "bb71282fcb088498a9c40b0460694f1663e8f3a145fc15469050b8ade2f390dc"
LEAN_COMMIT = "797c613eb9b6d4ec95db23e3e00af9ac6657f24b"
MATHLIB_REV = "f897ebcf72cd16f89ab4577d0c826cd14afaafc7"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
# Published math-evidence Linux 4.24.0 release-member pins. Host runtime and
# cached dependency OLeans remain trusted; no installer or full rebuild runs.
RELEASE_MEMBERS = {
    "bin/lean": (9024, "8fadc3ed92cc9decb94c96ee9c0876e91e03a3a5e69138f32114f02789e2766c"),
    "lib/lean/libleanshared.so": (193479936, "8cc9858cc57c52015ba6dd948bdbf7f05926b9b5fcead69a964f0ad61ddd79dd"),
    "lib/lean/libleanshared_1.so": (6232, "6ce912e300ad305bb38a362404544602e2229d072b78d75b1dd71c637e453c2c"),
    "lib/lean/libleanshared_2.so": (6232, "6ce912e300ad305bb38a362404544602e2229d072b78d75b1dd71c637e453c2c"),
    "lib/lean/libInit_shared.so": (6232, "6ce912e300ad305bb38a362404544602e2229d072b78d75b1dd71c637e453c2c"),
}
SCHEMA = "lp-certificates-checked-bridge/v1"
HISTORICAL_BRIDGE_SHA256 = "c0fe2cbfc7511309f91524e86ed8e5342f0d891c090a343a0a1ee06736774dd2"
TRUST_LIMITS = [
    "JSON-to-Lean transcription is trusted, not a proved parser refinement",
    "host runtime and clean pinned dependency caches are trusted",
    "same Lean kernel replay, not an independent kernel implementation",
    "package hashes attest consistency, not historical execution authenticity",
    "no finding/completeness, native Mac, or installed MRS claim",
]


class BridgeError(ValueError):
    def __init__(self, status: str, message: str):
        self.status = status
        super().__init__(message)


def utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True,
                       allow_nan=False) + "\n").encode("utf-8")


def strict_json(data: bytes) -> Any:
    return json.loads(data.decode("utf-8"), object_pairs_hook=verifier._unique_object,
                      parse_constant=verifier._forbid_constant)


def no_symlink_path(path: Path, *, allow_missing_leaf: bool = False) -> Path:
    if ".." in path.parts:
        raise BridgeError("invalid", "Parent traversal is not a supported path")
    absolute = Path(os.path.abspath(path))
    for index in range(1, len(absolute.parts) + 1):
        part = Path(*absolute.parts[:index])
        try:
            mode = part.lstat().st_mode
        except FileNotFoundError:
            if allow_missing_leaf and index == len(absolute.parts):
                continue
            raise BridgeError("invalid", "Path component does not exist: " + str(part))
        if stat.S_ISLNK(mode):
            raise BridgeError("invalid", "Symlink paths are not supported: " + str(part))
        if index < len(absolute.parts) and not stat.S_ISDIR(mode):
            raise BridgeError("invalid", "Parent path component is not a directory")
    return absolute


def read_regular(path: Path, limit: int) -> bytes:
    path = no_symlink_path(path)
    descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
                         | getattr(os, "O_NONBLOCK", 0))
    try:
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode):
            raise BridgeError("invalid", "Expected a regular file: " + str(path))
        if info.st_size > limit:
            raise BridgeError("unsupported", "File exceeds the supported byte bound")
        with os.fdopen(descriptor, "rb", closefd=False) as stream:
            data = stream.read(limit + 1)
        if len(data) > limit:
            raise BridgeError("unsupported", "File exceeds the supported byte bound")
        return data
    finally:
        os.close(descriptor)


def new_output(path: Path) -> Path:
    path = no_symlink_path(path, allow_missing_leaf=True)
    # mkdir without exist_ok is the ownership boundary; never resolve a symlink
    # into an existing destination, resume an attempt, or overwrite an old one.
    try:
        path.mkdir(mode=0o700)
    except FileExistsError as error:
        raise BridgeError("invalid", "Output already exists; select a fresh directory") from error
    return path


def canonical_fraction(value: Any) -> str:
    return verifier.fraction_string(verifier.rational(value, "$"))


def _bounded_rationals(document: Any) -> None:
    # The strict verifier has already established the shallow v1 schema.
    vectors = [document["problem"]["objective"]["coefficients"]]
    for row in document["problem"]["constraints"]:
        vectors.extend([row["coefficients"], [row["rhs"]]])
    for key, value in document["certificate"].items():
        if key != "kind":
            vectors.append(value)
    for values in vectors:
        for value in values:
            if type(value) is int:
                numbers = [value]
            else:
                # Bound the raw numerator/denominator, not only a reduced result.
                try:
                    numbers = [int(part) for part in value.split("/")]
                except ValueError as error:
                    raise BridgeError("unsupported", "Integer exceeds supported parse size") from error
            if any(abs(number).bit_length() > MAX_BITS for number in numbers):
                raise BridgeError("unsupported", "Rational numerator/denominator exceeds 256 bits")


def inspect_input(data: bytes) -> dict[str, Any]:
    if len(data) > MAX_INPUT_BYTES:
        raise BridgeError("unsupported", "Input exceeds 64 KiB")
    try:
        text = data.decode("utf-8")
    except UnicodeError as error:
        raise BridgeError("invalid", "Input is not UTF-8") from error
    try:
        document = strict_json(data)
        verifier.parse_document(document)
    except (ValueError, UnicodeError, RecursionError):
        result = verifier.verify_json(text)
        return {"status": "invalid", "python_result": result,
                "input_sha256": sha(data), "input_bytes": len(data)}
    n = len(document["problem"]["objective"]["coefficients"])
    rows = document["problem"]["constraints"]
    if n > MAX_DIMENSION or len(rows) > MAX_ROWS:
        raise BridgeError("unsupported", "Supported bounds are n<=8 and row count<=16")
    _bounded_rationals(document)
    result = verifier.verify_json(text)
    if result["status"] != "accepted":
        return {"status": result["status"], "python_result": result,
                "input_sha256": sha(data), "input_bytes": len(data)}
    problem, certificate = verifier.parse_document(document)
    weights: list[str] = []
    inequality_index = equality_index = 0
    if certificate.kind != "unbounded":
        for row in rows:
            if row["sense"] == "=":
                weights.append(verifier.fraction_string(certificate.equality_multipliers[equality_index]))
                equality_index += 1
            else:
                weights.append(verifier.fraction_string(certificate.inequality_multipliers[inequality_index]))
                inequality_index += 1
    semantic = {
        "dimension": n, "row_count": len(rows), "kind": certificate.kind,
        "objective_sense": document["problem"]["objective"]["sense"],
        "objective": [canonical_fraction(x) for x in document["problem"]["objective"]["coefficients"]],
        "rows": [{"index": i, "sense": row["sense"],
                  "coefficients": [canonical_fraction(x) for x in row["coefficients"]],
                  "rhs": canonical_fraction(row["rhs"])} for i, row in enumerate(rows)],
        "row_multipliers": weights,
        "point": [verifier.fraction_string(x) for x in certificate.point],
        "direction": [verifier.fraction_string(x) for x in certificate.direction],
    }
    return {"status": "accepted", "python_result": result, "semantic": semantic,
            "input_sha256": sha(data), "input_bytes": len(data)}


def _lean_number(value: str) -> str:
    # Generated values are canonical Fraction strings, never arbitrary input text.
    number = Fraction(value)
    if abs(number.numerator).bit_length() > MAX_BITS or number.denominator.bit_length() > MAX_BITS:
        raise BridgeError("unsupported", "Generated rational exceeds the bit bound")
    return f"({number.numerator} : ℚ)" if number.denominator == 1 else f"(({number.numerator} : ℚ) / {number.denominator})"


def _vector(values: list[str]) -> str:
    return "![" + ", ".join(_lean_number(x) for x in values) + "]"


def _render_unchecked(info: dict[str, Any]) -> bytes:
    """Internal pure renderer. Its result is UNCHECKED until the live gates pass."""
    if info.get("status") != "accepted":
        raise BridgeError("invalid", "Renderer requires an accepted bounded input")
    semantic = info["semantic"]
    n, r = semantic["dimension"], semantic["row_count"]
    if type(n) is not int or type(r) is not int or not 0 <= n <= MAX_DIMENSION or not 0 <= r <= MAX_ROWS:
        raise BridgeError("invalid", "Renderer dimensions are outside the supported bounds")
    if not isinstance(info.get("input_sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", info["input_sha256"]):
        raise BridgeError("invalid", "Renderer input hash must be lowercase SHA-256 hex")
    senses = {"<=": "RowSense.le", ">=": "RowSense.ge", "=": "RowSense.eq"}
    objective_sense = {"max": "ObjectiveSense.maximize", "min": "ObjectiveSense.minimize"}
    matrix = "![" + ", ".join(_vector(row["coefficients"]) for row in semantic["rows"]) + "]"
    row_senses = "![" + ", ".join(senses[row["sense"]] for row in semantic["rows"]) + "]"
    problem = (f"({{\n    a := {matrix},\n    b := {_vector([row['rhs'] for row in semantic['rows']])},\n"
               f"    senses := {row_senses},\n    c := {_vector(semantic['objective'])},\n"
               f"    objectiveSense := {objective_sense[semantic['objective_sense']]}\n  }} : InputProblem {n} {r})")
    point, weights, direction = _vector(semantic["point"]), _vector(semantic["row_multipliers"]), _vector(semantic["direction"])
    kind = semantic["kind"]
    if kind == "optimal":
        accepted_type = "checkInputOptimal problem point weights = true"
        sound_type = (f"InputFeasible problem (realVector point) ∧\n"
                      f"  ∀ y : Fin {n} → ℝ, InputFeasible problem y → ObjectiveBound problem (realVector point) y")
        proof = "inputOptimal_sound_real problem point weights accepted"
    elif kind == "infeasible":
        accepted_type = "checkInputInfeasible problem weights = true"
        sound_type = f"¬ ∃ y : Fin {n} → ℝ, InputFeasible problem y"
        proof = "inputInfeasible_sound_real problem weights accepted"
    elif kind == "unbounded":
        accepted_type = "checkInputUnbounded problem point direction = true"
        sound_type = f"∀ B : ℝ, ∃ y : Fin {n} → ℝ, InputFeasible problem y ∧ ObjectiveBeyond problem B y"
        proof = "inputUnbounded_sound_real problem point direction accepted"
    else:
        raise BridgeError("invalid", "Unsupported certificate kind")
    definitions = [f"def problem : InputProblem {n} {r} :=\n  {problem}"]
    if kind != "infeasible":
        definitions.append(f"def point : Fin {n} → ℚ := {point}")
    if kind != "unbounded":
        definitions.append(f"def weights : Fin {r} → ℚ := {weights}")
    else:
        definitions.append(f"def direction : Fin {n} → ℚ := {direction}")
    source = ("import LPCertificates.Input\nimport EvidenceHarness\n\nopen LPCertificates\n"
              f"-- Original strict JSON SHA-256: {info['input_sha256']}\n"
              "-- Numeric-only trusted transcription; no parser refinement theorem.\n"
              "namespace CheckedInput\n\n" + "\n\n".join(definitions) + "\n\n"
              f"theorem accepted : {accepted_type} := by decide +kernel\n\n"
              f"theorem sound : {sound_type} :=\n  {proof}\n\n"
              f"#evidence_definition CheckedInput.problem =\n  {problem}\n"
              f"#evidence_check CheckedInput.accepted : {accepted_type}\n"
              f"#evidence_check CheckedInput.sound : {sound_type}\n"
              "#evidence_replay [Mathlib, EvidenceHarness] targets [CheckedInput.accepted, CheckedInput.sound]\n"
              "\nend CheckedInput\n")
    return source.encode("utf-8")


def _source_manifest(output: Path) -> dict[str, Any]:
    paths = sorted(p for folder in ("inputs", "semantic", "project")
                   for p in (output / folder).rglob("*") if p.is_file())
    return {"schema": SCHEMA + "/source-manifest", "files": [
        {"path": p.relative_to(output).as_posix(), "bytes": p.stat().st_size,
         "sha256": file_hash(p)} for p in paths]}


def _package_manifest(output: Path) -> dict[str, Any]:
    paths = sorted(p for p in output.rglob("*") if p.is_file()
                   and p.name != "package-manifest.json" and ".work" not in p.relative_to(output).parts)
    return {"schema": SCHEMA + "/package-manifest", "files": [
        {"path": p.relative_to(output).as_posix(), "bytes": p.stat().st_size,
         "sha256": file_hash(p)} for p in paths]}


def _kill_group(process: subprocess.Popen) -> None:
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        return
    try:
        process.wait(timeout=2)
    except subprocess.TimeoutExpired:
        pass
    # Kill descendants even if their group leader already exited.
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    process.wait(timeout=5)


def _limits() -> None:
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    resource.setrlimit(resource.RLIMIT_CPU, (TIMEOUT_SECONDS, TIMEOUT_SECONDS + 5))
    resource.setrlimit(resource.RLIMIT_AS, (ADDRESS_SPACE_BYTES, ADDRESS_SPACE_BYTES))
    resource.setrlimit(resource.RLIMIT_FSIZE, (64 * 1024**2, 64 * 1024**2))
    resource.setrlimit(resource.RLIMIT_NOFILE, (256, 256))


def _interrupt_signal(signum: int, frame: Any) -> None:
    raise KeyboardInterrupt("Termination signal " + str(signum))


class Runner:
    def __init__(self, output: Path, record: dict[str, Any], env: dict[str, str]):
        self.output, self.record, self.env = output, record, env

    def save(self) -> None:
        (self.output / "receipt.json").write_bytes(json_bytes(self.record))

    def run(self, label: str, argv: list[str], cwd: Path) -> str:
        logs = self.output / "logs"
        logs.mkdir(exist_ok=True)
        stdout, stderr = logs / (label + ".stdout.log"), logs / (label + ".stderr.log")
        entry: dict[str, Any] = {"label": label, "argv": argv, "cwd": str(cwd),
                                 "started_utc": utc()}
        self.record["commands"].append(entry)
        self.save()
        process = None
        failure = None
        try:
            with stdout.open("xb") as out, stderr.open("xb") as err:
                process = subprocess.Popen(argv, cwd=cwd, env=self.env, stdin=subprocess.DEVNULL,
                    stdout=out, stderr=err, shell=False, start_new_session=True, preexec_fn=_limits)
                entry["pid"] = process.pid
                deadline = time.monotonic() + TIMEOUT_SECONDS
                while process.poll() is None:
                    if time.monotonic() >= deadline:
                        failure = "timeout"
                        _kill_group(process)
                        break
                    if stdout.stat().st_size > MAX_LOG_BYTES or stderr.stat().st_size > MAX_LOG_BYTES:
                        failure = "output_limit"
                        _kill_group(process)
                        break
                    time.sleep(0.05)
                process.wait(timeout=5)
                # An exited leader may have left descendants that inherited logs.
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
        except BaseException as error:
            failure = "interrupted" if isinstance(error, KeyboardInterrupt) else "runner_error"
            if process is not None:
                _kill_group(process)
            raise
        finally:
            entry["ended_utc"] = utc()
            entry["exit_code"] = process.returncode if process is not None else None
            entry["termination"] = failure or ("exit" if process is not None else "launch_failed")
            for name, path in (("stdout", stdout), ("stderr", stderr)):
                if path.exists():
                    observed = path.stat().st_size
                    if observed > MAX_LOG_BYTES:
                        failure = failure or "output_limit"
                        with path.open("r+b") as stream:
                            stream.truncate(MAX_LOG_BYTES)
                    entry[name] = {"path": path.relative_to(self.output).as_posix(),
                                   "observed_bytes": observed, "bytes": path.stat().st_size,
                                   "sha256": file_hash(path), "truncated": observed > MAX_LOG_BYTES}
            if failure:
                entry["termination"] = failure
            self.save()
        if failure or entry["exit_code"] != 0:
            raise BridgeError("failed", label + " failed: " + (failure or str(entry["exit_code"])))
        text = stdout.read_text("utf-8") + stderr.read_text("utf-8")
        if re.search(r"(?mi)\b(?:error|warning):", text):
            raise BridgeError("failed", label + " emitted Lean diagnostics")
        return text


def _toolchain(lean_bin: Path) -> dict[str, Any]:
    # Explicit Linux-only support. Never fall through to an installer/shim.
    if sys.platform != "linux":
        raise BridgeError("unsupported", "This checked runner supports Linux only")
    binary_dir = no_symlink_path(lean_bin)
    if binary_dir.name != "bin" or not binary_dir.is_dir():
        raise BridgeError("failed", "Select the official distribution's regular bin directory")
    root = binary_dir.parent
    executable = no_symlink_path(binary_dir / "lean")
    if not stat.S_ISREG(executable.lstat().st_mode):
        raise BridgeError("failed", "The selected Lean executable must be a regular nonsymlink file")
    observed = {}
    for relative, (size, expected) in RELEASE_MEMBERS.items():
        path = no_symlink_path(root / relative)
        if not stat.S_ISREG(path.lstat().st_mode) or path.stat().st_size != size or file_hash(path) != expected:
            raise BridgeError("failed", "Compiler/runtime byte pin mismatch: " + relative)
        observed[relative] = {"bytes": size, "sha256": expected}
    if executable != root / "bin/lean":
        raise BridgeError("failed", "Selected executable differs from the byte-audited executable")
    return {"lean": str(executable), "prefix": str(root),
            "release": "4.24.0", "commit": LEAN_COMMIT, "members": observed}


def _dependencies(runner: Runner, phase: str) -> tuple[list[dict[str, Any]], list[Path]]:
    manifest = strict_json(read_regular(ROOT / "lake-manifest.json", MAX_INPUT_BYTES))
    packages = manifest.get("packages")
    if not isinstance(packages, list) or len(packages) != 9:
        raise BridgeError("failed", "Expected the nine pinned dependencies")
    mathlib = next((x for x in packages if x.get("name") == "mathlib"), {})
    if mathlib.get("rev") != MATHLIB_REV or mathlib.get("url") != "https://github.com/leanprover-community/mathlib4.git":
        raise BridgeError("failed", "Unexpected mathlib identity")
    identities, caches = [], []
    for index, package in enumerate(packages):
        name = package.get("name")
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", name):
            raise BridgeError("failed", "Invalid trusted dependency name")
        folder = (ROOT / ".lake/packages" / name).resolve(strict=True)
        output = runner.run(f"{phase}-dependency-{index:02d}", ["/usr/bin/git", "-C", str(folder),
                            "status", "--porcelain", "--untracked-files=no"], ROOT)
        if output.strip():
            raise BridgeError("failed", "Dependency has tracked modifications: " + name)
        revision = runner.run(f"{phase}-revision-{index:02d}", ["/usr/bin/git", "-C", str(folder), "rev-parse", "HEAD"], ROOT).strip()
        origin = runner.run(f"{phase}-origin-{index:02d}", ["/usr/bin/git", "-C", str(folder), "remote", "get-url", "origin"], ROOT).strip()
        if revision != package["rev"] or origin.removesuffix(".git") != package["url"].removesuffix(".git"):
            raise BridgeError("failed", "Dependency revision/origin mismatch: " + name)
        cache = folder / ".lake/build/lib/lean"
        if not cache.is_dir() and name != "Cli":
            raise BridgeError("failed", "Missing trusted dependency cache: " + name)
        identities.append({"name": name, "revision": revision, "origin": origin,
                           "tracked_status": "", "cache": str(cache) if cache.is_dir() else None,
                           "cache_status": "trusted_present" if cache.is_dir() else "absent_not_imported"})
        if cache.is_dir():
            caches.append(cache)
    return identities, caches


def _trusted_sources() -> dict[str, bytes]:
    paths = ["lean-toolchain", "lakefile.toml", "lake-manifest.json", "LPCertificates.lean",
             "LPCertificates/Core.lean", "LPCertificates/Rational.lean",
             "LPCertificates/Input.lean", "LPCertificates/Examples.lean", "scripts/ExpectedInput.lean"]
    sources = {path: read_regular(ROOT / path, 1024 * 1024) for path in paths}
    if sources["lean-toolchain"].strip() != b"leanprover/lean4:v4.24.0":
        raise BridgeError("failed", "Unexpected Lean toolchain pin")
    helper = read_regular(ROOT.parent / "math-evidence/lean/EvidenceHarness.lean", 1024 * 1024)
    if sha(helper) != HELPER_SHA256:
        raise BridgeError("failed", "Published evidence helper source pin mismatch")
    sources["EvidenceHarness.lean"] = helper
    return sources


def _markers(text: str, prefix: str) -> list[dict[str, Any]]:
    result = []
    for line in text.splitlines():
        index = line.find(prefix)
        if index >= 0:
            try:
                marker = strict_json(line[index + len(prefix):].encode())
                if not isinstance(marker, dict):
                    raise BridgeError("failed", "Evidence marker is not an object")
                result.append(marker)
            except (ValueError, UnicodeError) as error:
                raise BridgeError("failed", "Malformed evidence marker") from error
    return result


def _instance_gate(text: str) -> dict[str, Any]:
    targets = _markers(text, "MATH_EVIDENCE_TARGET ")
    definitions = _markers(text, "MATH_EVIDENCE_DEFINITION ")
    replay = _markers(text, "MATH_EVIDENCE_REPLAY ")
    if {x.get("target") for x in targets} != {"CheckedInput.accepted", "CheckedInput.sound"} or len(targets) != 2:
        raise BridgeError("failed", "Incomplete instance whole-type/axiom gate")
    if len(definitions) != 1 or definitions[0].get("target") != "CheckedInput.problem":
        raise BridgeError("failed", "Incomplete instance problem-body gate")
    for target in targets:
        if target.get("typeMatching") != "closed_whole_type_kernel_definitional_equality" or target.get("declarationKind") != "theorem":
            raise BridgeError("failed", "Unexpected instance target gate")
    for item in [*targets, *definitions]:
        axioms = item.get("axioms")
        if not isinstance(axioms, list) or any(x not in ALLOWED_AXIOMS for x in axioms):
            raise BridgeError("failed", "Unapproved instance axiom closure")
    if len(replay) != 1 or replay[0].get("baseModules") != ["Mathlib", "EvidenceHarness"] or set(replay[0].get("targets", [])) != {"CheckedInput.accepted", "CheckedInput.sound"} or not isinstance(replay[0].get("replayedDeclarations"), int) or replay[0]["replayedDeclarations"] <= 0:
        raise BridgeError("failed", "Incomplete instance same-kernel replay")
    return {"targets": targets, "definitions": definitions, "replay": replay}


def _expected_gate(text: str) -> None:
    targets = _markers(text, "MATH_EVIDENCE_TARGET ")
    expected = {"LPCertificates.inputOptimal_sound_real", "LPCertificates.inputInfeasible_sound_real", "LPCertificates.inputUnbounded_sound_real"}
    if len(targets) != 3 or expected != {x.get("target") for x in targets}:
        raise BridgeError("failed", "Incomplete independently specified Input expected-type gate")
    definitions = _markers(text, "MATH_EVIDENCE_DEFINITION ")
    definition_names = {"LPCertificates." + name for name in (
        "normalizeInput", "inputInequalityWeights", "inputEqualityWeights", "InputFeasible",
        "ObjectiveBound", "ObjectiveBeyond", "checkInputOptimal", "checkInputInfeasible", "checkInputUnbounded")}
    replay = _markers(text, "MATH_EVIDENCE_REPLAY ")
    if len(definitions) != 9 or {x.get("target") for x in definitions} != definition_names or len(replay) != 1:
        raise BridgeError("failed", "Incomplete Input definition-body/replay gate")
    if replay[0].get("baseModules") != ["Mathlib", "EvidenceHarness"] or set(replay[0].get("targets", [])) != expected or type(replay[0].get("replayedDeclarations")) is not int or replay[0]["replayedDeclarations"] <= 0:
        raise BridgeError("failed", "Incomplete Input same-kernel replay")
    for target in [*targets, *definitions]:
        if not isinstance(target.get("axioms"), list) or any(x not in ALLOWED_AXIOMS for x in target["axioms"]):
            raise BridgeError("failed", "Unapproved Input theorem axiom closure")
    if any(x.get("typeMatching") != "closed_whole_type_kernel_definitional_equality" for x in targets):
        raise BridgeError("failed", "Unexpected Input whole-type matching evidence")


def check_raw(raw_inputs: list[bytes], output_path: Path, lean_bin: Path) -> dict[str, Any]:
    output = new_output(output_path)
    record: dict[str, Any] = {"schema": SCHEMA, "status": "in_progress", "started_utc": utc(),
                              "commands": [], "inputs": [], "trust_limits": TRUST_LIMITS,
                              "bridge_sha256": file_hash(Path(__file__)),
                              "verifier_sha256": file_hash(ROOT / "verifier.py"),
                              "resource_bounds": {"timeout_seconds": TIMEOUT_SECONDS,
                                  "address_space_bytes": ADDRESS_SPACE_BYTES, "lean_heap_megabytes": 4096,
                                  "lean_threads": 1, "log_bytes_per_stream": MAX_LOG_BYTES}}
    runner = Runner(output, record, {"PATH": "/usr/bin:/bin", "LC_ALL": "C.UTF-8", "TZ": "UTC"})
    runner.save()
    work = output / ".work"
    try:
        if not 1 <= len(raw_inputs) <= MAX_BATCH:
            raise BridgeError("unsupported", "Supported batch size is 1 through 16")
        (output / "inputs").mkdir()
        (output / "semantic").mkdir()
        prepared = []
        for index, data in enumerate(raw_inputs):
            label = f"{index:04d}"
            info = inspect_input(data)
            (output / "inputs" / (label + ".json")).write_bytes(data)
            record["inputs"].append({"id": label, "status": info["status"],
                                      "input_sha256": info["input_sha256"], "input_bytes": info["input_bytes"],
                                      "python_result": info["python_result"]})
            if info["status"] != "accepted":
                raise BridgeError(info["status"], "Preflight certificate is " + info["status"])
            (output / "semantic" / (label + ".json")).write_bytes(json_bytes(info["semantic"]))
            prepared.append(info)
        toolchain = _toolchain(lean_bin)
        record["toolchain"] = toolchain
        lean = toolchain["lean"]
        version = runner.run("compiler-version", [lean, "--version"], ROOT)
        if "version 4.24.0," not in version or LEAN_COMMIT not in version:
            raise BridgeError("failed", "Actual compiler version/commit mismatch")
        dependencies, caches = _dependencies(runner, "pre")
        record["dependencies"] = dependencies
        sources = _trusted_sources()
        record["library_sources"] = {name: {"bytes": len(data), "sha256": sha(data)} for name, data in sources.items()}
        project = output / "project"
        project.mkdir()
        for name, data in sources.items():
            path = project / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        for index, info in enumerate(prepared):
            (project / f"Checked{index:04d}.lean").write_bytes(_render_unchecked(info))
        (output / "source-manifest.json").write_bytes(json_bytes(_source_manifest(output)))
        work.mkdir()
        lib = work / "lib/lean"
        lib.mkdir(parents=True)
        (work / "packages").mkdir()
        for dependency in dependencies:
            if dependency["cache"] is not None:
                (work / "packages" / dependency["name"]).symlink_to(dependency["cache"], target_is_directory=True)
        runner.env.update({"PATH": str(Path(lean).parent) + ":/usr/bin:/bin", "TMPDIR": str(work),
                           "LEAN_PATH": os.pathsep.join([str(lib), *map(str, caches)])})
        record["lean_path"] = runner.env["LEAN_PATH"]
        # All task library OLeans are rebuilt into this attempt's empty directory.
        modules = ["LPCertificates/Core", "LPCertificates/Rational", "LPCertificates/Input",
                   "LPCertificates/Examples", "LPCertificates", "EvidenceHarness"]
        record["products"] = []
        for index, module in enumerate(modules):
            target = lib / (module + ".olean")
            target.parent.mkdir(parents=True, exist_ok=True)
            runner.run(f"library-{index:02d}", [lean, "-j1", "-M4096", "--root=" + str(project), module + ".lean", "-o", str(target)], project)
            record["products"].append({"module": module, "bytes": target.stat().st_size,
                                        "sha256": file_hash(target), "retained": False})
        expected = runner.run("input-expected", [lean, "-j1", "-M4096", "--root=" + str(project), "scripts/ExpectedInput.lean"], project)
        _expected_gate(expected)
        record["library_expected_gate"] = "passed"
        for index, info in enumerate(prepared):
            label = f"{index:04d}"
            target = lib / ("Checked" + label + ".olean")
            text = runner.run("instance-" + label, [lean, "-j1", "-M4096", "--root=" + str(project), "Checked" + label + ".lean", "-o", str(target)], project)
            record["inputs"][index]["lean_evidence"] = _instance_gate(text)
            record["inputs"][index]["status"] = "lean_checked"
            record["products"].append({"module": "Checked" + label, "bytes": target.stat().st_size,
                                        "sha256": file_hash(target), "retained": False})
            runner.save()
        if _trusted_sources() != sources or _toolchain(Path(lean).parent) != toolchain:
            raise BridgeError("failed", "Trusted source or compiler/runtime changed during attempt")
        if file_hash(Path(__file__)) != record["bridge_sha256"] or file_hash(ROOT / "verifier.py") != record["verifier_sha256"]:
            raise BridgeError("failed", "Generator or Python verifier changed during attempt")
        post_dependencies, _ = _dependencies(runner, "post")
        if post_dependencies != dependencies:
            raise BridgeError("failed", "Dependency identities changed during attempt")
        if _source_manifest(output) != strict_json((output / "source-manifest.json").read_bytes()):
            raise BridgeError("failed", "Preserved input/source/semantic artifact changed during attempt")
        for entry in record["commands"]:
            for stream in ("stdout", "stderr"):
                evidence = entry[stream]
                path = output / evidence["path"]
                if path.is_symlink() or path.stat().st_size != evidence["bytes"] or file_hash(path) != evidence["sha256"]:
                    raise BridgeError("failed", "Recorded phase output changed during attempt")
        for product in record["products"]:
            path = lib / (product["module"] + ".olean")
            if path.is_symlink() or path.stat().st_size != product["bytes"] or file_hash(path) != product["sha256"]:
                raise BridgeError("failed", "Compiled product changed during attempt")
        record["postflight"] = "all input/source/compiler/dependency/output/product identities unchanged"
        record["status"] = "lean_checked"
    except BridgeError as error:
        record["status"], record["failure"] = error.status, str(error)
    except KeyboardInterrupt:
        record["status"], record["failure"] = "failed", "Interrupted"
    except Exception as error:
        record["status"], record["failure"] = "failed", type(error).__name__ + ": " + str(error)
    finally:
        # Portable packages intentionally contain sources/input/logs, not caches.
        if work.exists():
            shutil.rmtree(work)
        if record["status"] != "lean_checked":
            for entry in record["inputs"]:
                if entry["status"] == "lean_checked":
                    entry["status"] = "failed"
                    entry["attempt_not_accepted_reason"] = record["status"]
        record["ended_utc"] = utc()
        runner.save()
        (output / "package-manifest.json").write_bytes(json_bytes(_package_manifest(output)))
    return record


def validate_package(path: Path) -> list[bytes]:
    package = no_symlink_path(path)
    if not package.is_dir():
        raise BridgeError("invalid", "Expected a package directory")
    actual = set()
    for directory, folders, files in os.walk(package, followlinks=False):
        for name in folders + files:
            member = Path(directory) / name
            if member.is_symlink():
                raise BridgeError("invalid", "Package contains a symlink")
            if name in (".work", ".lake"):
                raise BridgeError("invalid", "Portable package contains a runtime cache")
        for name in files:
            member = Path(directory) / name
            if not stat.S_ISREG(member.lstat().st_mode):
                raise BridgeError("invalid", "Package contains a nonregular member")
            actual.add(member.relative_to(package).as_posix())
    if len(actual) > 400:
        raise BridgeError("unsupported", "Package exceeds the file-count bound")
    manifest = strict_json(read_regular(package / "package-manifest.json", 1024 * 1024))
    if not isinstance(manifest, dict) or set(manifest) != {"schema", "files"} or manifest["schema"] != SCHEMA + "/package-manifest" or not isinstance(manifest["files"], list):
        raise BridgeError("invalid", "Unsupported package manifest")
    declared = set()
    total = 0
    for item in manifest["files"]:
        if not isinstance(item, dict) or set(item) != {"path", "bytes", "sha256"}:
            raise BridgeError("invalid", "Malformed package member")
        name = item["path"]
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*", name) or any(x in (".", "..") for x in name.split("/")) or name in declared or name == "package-manifest.json":
            raise BridgeError("invalid", "Unsafe or duplicate package member path")
        if type(item["bytes"]) is not int or not 0 <= item["bytes"] <= 4 * 1024 * 1024 or not isinstance(item["sha256"], str) or not re.fullmatch(r"[0-9a-f]{64}", item["sha256"]):
            raise BridgeError("invalid", "Malformed member hash/size")
        total += item["bytes"]
        if total > 16 * 1024 * 1024:
            raise BridgeError("unsupported", "Package exceeds the total byte bound")
        data = read_regular(package / name, 4 * 1024 * 1024)
        if len(data) != item["bytes"] or sha(data) != item["sha256"]:
            raise BridgeError("invalid", "Package hash/size mismatch: " + name)
        declared.add(name)
    if actual != declared | {"package-manifest.json"}:
        raise BridgeError("invalid", "Package manifest does not cover exactly every regular member")
    receipt = strict_json(read_regular(package / "receipt.json", 4 * 1024 * 1024))
    if not isinstance(receipt, dict) or receipt.get("schema") != SCHEMA or receipt.get("status") != "lean_checked":
        raise BridgeError("invalid", "Package is not a completed checked-package report")
    records = receipt.get("inputs")
    if not isinstance(records, list) or not 1 <= len(records) <= MAX_BATCH:
        raise BridgeError("invalid", "Invalid package input inventory")
    raw_inputs = []
    expected_input_names = set()
    for index, entry in enumerate(records):
        label = f"{index:04d}"
        if not isinstance(entry, dict) or entry.get("id") != label or entry.get("status") != "lean_checked":
            raise BridgeError("invalid", "Invalid or incomplete input identity")
        raw = read_regular(package / "inputs" / (label + ".json"), MAX_INPUT_BYTES)
        info = inspect_input(raw)
        if info.get("status") != "accepted" or info["input_sha256"] != entry.get("input_sha256") or len(raw) != entry.get("input_bytes"):
            raise BridgeError("invalid", "Input snapshot does not match the checked report")
        if read_regular(package / "semantic" / (label + ".json"), MAX_INPUT_BYTES) != json_bytes(info["semantic"]):
            raise BridgeError("invalid", "Raw semantic table differs from strict original JSON")
        if read_regular(package / "project" / ("Checked" + label + ".lean"), 1024 * 1024) != _render_unchecked(info):
            raise BridgeError("invalid", "Generated source does not match the current trusted numeric renderer")
        expected_input_names.add("inputs/" + label + ".json")
        raw_inputs.append(raw)
    if {name for name in actual if name.startswith("inputs/")} != expected_input_names:
        raise BridgeError("invalid", "Unexpected input snapshots")
    sources = _trusted_sources()
    for name, trusted in sources.items():
        if read_regular(package / "project" / name, 1024 * 1024) != trusted:
            raise BridgeError("invalid", "Package library/helper source differs from the current trusted source: " + name)
    commands = receipt.get("commands")
    if not isinstance(commands, list):
        raise BridgeError("invalid", "Missing recorded commands")
    expected_labels = (["compiler-version"]
        + [f"pre-{kind}-{i:02d}" for i in range(9) for kind in ("dependency", "revision", "origin")]
        + [f"library-{i:02d}" for i in range(6)] + ["input-expected"]
        + [f"instance-{i:04d}" for i in range(len(records))]
        + [f"post-{kind}-{i:02d}" for i in range(9) for kind in ("dependency", "revision", "origin")])
    if len(commands) != len(expected_labels):
        raise BridgeError("invalid", "Missing or extra recorded phases")
    log_names = set()
    for entry, label in zip(commands, expected_labels):
        if not isinstance(entry, dict) or entry.get("label") != label or entry.get("exit_code") != 0 or entry.get("termination") != "exit":
            raise BridgeError("invalid", "Incomplete or failed recorded phase")
        if not isinstance(entry.get("argv"), list) or not entry["argv"] or any(type(x) is not str for x in entry["argv"]):
            raise BridgeError("invalid", "Malformed recorded argv")
        for stream in ("stdout", "stderr"):
            log_name = "logs/" + label + "." + stream + ".log"
            evidence = entry.get(stream)
            if not isinstance(evidence, dict) or evidence.get("path") != log_name or evidence.get("truncated") is not False:
                raise BridgeError("invalid", "Missing or truncated phase evidence")
            data = read_regular(package / log_name, MAX_LOG_BYTES)
            if evidence.get("bytes") != len(data) or evidence.get("observed_bytes") != len(data) or evidence.get("sha256") != sha(data):
                raise BridgeError("invalid", "Phase log differs from receipt")
            log_names.add(log_name)
        if label == "input-expected":
            _expected_gate(read_regular(package / entry["stdout"]["path"], MAX_LOG_BYTES).decode()
                           + read_regular(package / entry["stderr"]["path"], MAX_LOG_BYTES).decode())
        if label.startswith("instance-"):
            index = int(label.removeprefix("instance-"))
            gate = _instance_gate(read_regular(package / entry["stdout"]["path"], MAX_LOG_BYTES).decode()
                                  + read_regular(package / entry["stderr"]["path"], MAX_LOG_BYTES).decode())
            if records[index].get("lean_evidence") != gate:
                raise BridgeError("invalid", "Instance gate report differs from its recorded logs")
    # The reviewed historical renderer/source gates are unchanged by the binding
    # repair. Its saved packages remain inspectable; fresh recheck always runs
    # this current code and its exact-executable preflight/postflight.
    if receipt.get("bridge_sha256") not in {file_hash(Path(__file__)), HISTORICAL_BRIDGE_SHA256} or receipt.get("verifier_sha256") != file_hash(ROOT / "verifier.py"):
        raise BridgeError("invalid", "Package generator/verifier version differs from current trusted code")
    expected_files = {"receipt.json", "source-manifest.json", "package-manifest.json"} | log_names
    expected_files |= {"project/" + name for name in sources}
    for i in range(len(records)):
        expected_files |= {f"inputs/{i:04d}.json", f"semantic/{i:04d}.json", f"project/Checked{i:04d}.lean"}
    if actual != expected_files:
        raise BridgeError("invalid", "Unexpected or missing portable package members")
    if read_regular(package / "source-manifest.json", 1024 * 1024) != json_bytes(_source_manifest(package)):
        raise BridgeError("invalid", "Source manifest differs from preserved sources")
    return raw_inputs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser("check", help="Check supplied original JSON in a fresh Lean attempt")
    check.add_argument("documents", nargs="+", type=Path)
    recheck = commands.add_parser("recheck", help="Validate a package, then regenerate/check its saved original JSON")
    recheck.add_argument("package", type=Path)
    for command in (check, recheck):
        command.add_argument("--output", required=True, type=Path)
        command.add_argument("--lean-bin", required=True, type=Path)
    args = parser.parse_args(argv)
    previous_term = signal.signal(signal.SIGTERM, _interrupt_signal)
    try:
        if args.command == "check":
            if len(args.documents) > MAX_BATCH:
                raise BridgeError("unsupported", "Batch exceeds 16 documents")
            inputs = [read_regular(path, MAX_INPUT_BYTES) for path in args.documents]
        else:
            inputs = validate_package(args.package)
        record = check_raw(inputs, args.output, args.lean_bin)
        status = record["status"]
        result = {"status": status, "receipt": str(Path(os.path.abspath(args.output)) / "receipt.json"),
                  "failure": record.get("failure")}
    except (BridgeError, OSError, ValueError, UnicodeError, RecursionError) as error:
        status = error.status if isinstance(error, BridgeError) else "invalid"
        result = {"status": status, "failure": str(error)}
    except KeyboardInterrupt:
        status, result = "failed", {"status": "failed", "failure": "Interrupted before a running attempt"}
    finally:
        signal.signal(signal.SIGTERM, previous_term)
    print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))
    return {"lean_checked": 0, "rejected": 1, "invalid": 2, "unsupported": 3,
            "failed": 4, "in_progress": 5}.get(status, 4)


if __name__ == "__main__":
    raise SystemExit(main())
