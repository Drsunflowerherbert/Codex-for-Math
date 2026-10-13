"""Independent restricted-literal audit and opt-in fresh Lean bridge checks.

Set LP_BRIDGE_LEAN_BIN to the pinned official Linux distribution's bin path to
run actual Lean checks. Saved receipts alone never satisfy the live test.
"""

from copy import deepcopy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))
import bridge  # noqa: E402
from test_independent import document, raw_certificate_accepts, row  # noqa: E402


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True,
                       allow_nan=False) + "\n").encode()


def digest(data):
    return hashlib.sha256(data).hexdigest()


class LiteralDecoder:
    """Parse only finite vectors and the two permitted rational literal forms."""

    rational = re.compile(r"\((-?[0-9]+) : ℚ\)")
    fraction = re.compile(r"\(\((-?[0-9]+) : ℚ\) / ([1-9][0-9]*)\)")
    sense = re.compile(r"RowSense\.(le|ge|eq)")

    def __init__(self, source):
        self.source, self.index = source, 0

    def space(self):
        while self.index < len(self.source) and self.source[self.index].isspace():
            self.index += 1

    def read(self):
        self.space()
        if self.source.startswith("![", self.index):
            self.index += 2
            values = []
            self.space()
            if self.source.startswith("]", self.index):
                self.index += 1
                return values
            while True:
                values.append(self.read())
                self.space()
                if self.source.startswith("]", self.index):
                    self.index += 1
                    return values
                if not self.source.startswith(",", self.index):
                    raise AssertionError("Unexpected finite-vector literal syntax")
                self.index += 1
        for pattern in [self.fraction, self.rational, self.sense]:
            match = pattern.match(self.source, self.index)
            if match:
                self.index = match.end()
                if pattern is self.sense:
                    return {"le": "<=", "ge": ">=", "eq": "="}[match[1]]
                return Q(int(match[1]), int(match[2]) if pattern is self.fraction else 1)
        raise AssertionError("Unexpected text in restricted Lean literal")

    def complete(self):
        value = self.read()
        self.space()
        if self.index != len(self.source):
            raise AssertionError("Unconsumed text in restricted Lean literal")
        return value


def decoded_definition(source, name):
    match = re.search(r"^def " + name + r" : .* := (.*)$", source, re.MULTILINE)
    if not match:
        return None
    return LiteralDecoder(match[1]).complete()


def independently_decode_problem(source):
    match = re.search(r"^def problem : InputProblem ([0-9]+) ([0-9]+) :=\n  \(\{\n    a := (.*),\n"
                      r"    b := (.*),\n    senses := (.*),\n    c := (.*),\n"
                      r"    objectiveSense := ObjectiveSense\.(maximize|minimize)\n  \} : InputProblem ([0-9]+) ([0-9]+)\)$",
                      source, re.MULTILINE)
    if not match:
        raise AssertionError("Problem definition differs from restricted raw-input layout")
    n, r = int(match[1]), int(match[2])
    if (n, r) != (int(match[8]), int(match[9])):
        raise AssertionError("Mismatched declared dimensions")
    a, b, senses, c = [LiteralDecoder(match[i]).complete() for i in range(3, 7)]
    if not (len(a) == len(b) == len(senses) == r and len(c) == n and all(len(v) == n for v in a)):
        raise AssertionError("Literal dimensions do not match declarations")
    return {"n": n, "r": r, "a": a, "b": b, "senses": senses, "c": c,
            "objective_sense": {"maximize": "max", "minimize": "min"}[match[7]]}


def accepted_documents():
    docs = [json.loads(p.read_text()) for p in sorted((ROOT / "examples").glob("*.json"))
            if p.name.startswith(("optimal_", "infeasible_", "unbounded_"))]
    docs.append(document([row([1, -1], "=", 0), row([1, 0], ">=", 1),
                          row([2, -2], "=", 0), row([3, 3], ">=", 6),
                          row([1, 0], "<=", 4)], c=(1, 2), sense="min",
                         kind="optimal", point=[1, 1],
                         inequality_multipliers=[3, 0, 0], equality_multipliers=[2, 0]))
    docs.append(document([row([0, 1], "=", 1), row([1, 0], "<=", 0)],
                         c=(-3, 2), kind="unbounded", base_point=[-2, 1], direction=[-1, 0]))
    docs.append(document([row(["+02/2"], ">=", "-0000"), row(["+06/2"], "=", "+0001")],
                         c=("+0006/4",), sense="min", kind="optimal", point=["+0002/6"],
                         inequality_multipliers=["-0"], equality_multipliers=["-0002/4"]))
    docs.append(document([], c=(), sense="min", kind="optimal", point=[],
                         inequality_multipliers=[], equality_multipliers=[]))
    return docs


def file_items(package, folders=None):
    paths = (sorted(p for folder in folders for p in (package / folder).rglob("*") if p.is_file())
             if folders else sorted(p for p in package.rglob("*") if p.is_file() and p.name != "package-manifest.json"))
    return [{"path": p.relative_to(package).as_posix(), "bytes": len(p.read_bytes()),
             "sha256": digest(p.read_bytes())} for p in paths]


def remake_manifests(package):
    (package / "source-manifest.json").write_bytes(encoded({
        "schema": bridge.SCHEMA + "/source-manifest", "files": file_items(package, ["inputs", "semantic", "project"])}))
    (package / "package-manifest.json").write_bytes(encoded({
        "schema": bridge.SCHEMA + "/package-manifest", "files": file_items(package)}))


def counterfeit_consistent_package(package):
    """No Lean run occurs here; deliberately forge a hash-consistent saved report."""
    package.mkdir()
    for folder in ["inputs", "semantic", "project"]:
        (package / folder).mkdir()
    data = encoded(json.loads((ROOT / "examples/optimal_mixed_redundant.json").read_text()))
    info = bridge.inspect_input(data)
    (package / "inputs/0000.json").write_bytes(data)
    (package / "semantic/0000.json").write_bytes(encoded(info["semantic"]))
    (package / "project/Checked0000.lean").write_bytes(bridge._render_unchecked(info))
    for name, source in bridge._trusted_sources().items():
        target = package / "project" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source)
    receipt = {"schema": bridge.SCHEMA, "status": "lean_checked", "commands": [],
               "inputs": [{"id": "0000", "status": "lean_checked", "input_sha256": digest(data),
                           "input_bytes": len(data)}]}
    (package / "receipt.json").write_bytes(encoded(receipt))
    remake_manifests(package)
    return data


class IndependentBridgeReview(unittest.TestCase):
    def test_generated_literals_decode_to_original_rows_objective_and_witness(self):
        docs = accepted_documents()
        self.assertEqual(len(docs), 13)
        for doc in docs:
            self.assertTrue(raw_certificate_accepts(doc), doc)
            data = encoded(doc)
            info = bridge.inspect_input(data)
            self.assertEqual(info["status"], "accepted")
            source = bridge._render_unchecked(info).decode()
            parsed = independently_decode_problem(source)
            raw, cert = doc["problem"], doc["certificate"]
            self.assertEqual(parsed["a"], [[Q(x) for x in r["coefficients"]] for r in raw["constraints"]])
            self.assertEqual(parsed["b"], [Q(r["rhs"]) for r in raw["constraints"]])
            self.assertEqual(parsed["senses"], [r["sense"] for r in raw["constraints"]])
            self.assertEqual(parsed["c"], [Q(x) for x in raw["objective"]["coefficients"]])
            self.assertEqual(parsed["objective_sense"], raw["objective"]["sense"])
            self.assertEqual(parsed["n"], len(raw["objective"]["coefficients"]))
            self.assertEqual(parsed["r"], len(raw["constraints"]))
            if cert["kind"] != "infeasible":
                key = "base_point" if cert["kind"] == "unbounded" else "point"
                self.assertEqual(decoded_definition(source, "point"), [Q(x) for x in cert[key]])
            if cert["kind"] == "unbounded":
                self.assertEqual(decoded_definition(source, "direction"), [Q(x) for x in cert["direction"]])
            else:
                iy = iz = 0
                weights = []
                for r in raw["constraints"]:
                    if r["sense"] == "=":
                        weights.append(Q(cert["equality_multipliers"][iz]))
                        iz += 1
                    else:
                        weights.append(Q(cert["inequality_multipliers"][iy]))
                        iy += 1
                self.assertEqual(decoded_definition(source, "weights"), weights)
            acceptance_type = {
                "optimal": "checkInputOptimal problem point weights = true",
                "infeasible": "checkInputInfeasible problem weights = true",
                "unbounded": "checkInputUnbounded problem point direction = true",
            }[cert["kind"]]
            self.assertIn("theorem accepted : " + acceptance_type + " := by decide +kernel", source)
            self.assertIn("#evidence_check CheckedInput.accepted : " + acceptance_type, source)
            self.assertIn(digest(data), source)
            self.assertNotIn("sorry", source)
            self.assertNotIn("native_decide", source)
            self.assertNotIn("axiom ", source)

    def test_decoder_refuses_extra_syntax(self):
        for literal in ["![1]", "![(1 : ℚ), System.cmd]", "![(1 : ℚ)] ; axiom bad : False", "![(1 : ℚ) / 0]", "eval 1"]:
            with self.assertRaises(AssertionError):
                LiteralDecoder(literal).complete()

    def test_untrusted_json_fields_senses_rationals_types_and_duplicates(self):
        baseline = accepted_documents()[0]
        for value in [True, False, 1.0, None, "1/0", "1/-2", "1; import Mathlib",
                      "1\naxiom bad : False", "$(touch /tmp/lp-bridge-injection)"]:
            doc = deepcopy(baseline)
            doc["problem"]["objective"]["coefficients"][0] = value
            self.assertEqual(bridge.inspect_input(encoded(doc))["status"], "invalid")
        for key in ["lean_source", "source_path", "../../Checked.lean", "import Mathlib"]:
            doc = deepcopy(baseline)
            doc[key] = "arbitrary untrusted text"
            self.assertEqual(bridge.inspect_input(encoded(doc))["status"], "invalid")
        doc = deepcopy(baseline)
        doc["problem"]["constraints"][0]["sense"] = "=\naxiom bad : False"
        self.assertEqual(bridge.inspect_input(encoded(doc))["status"], "invalid")
        for raw in [b"{", b"null", b"\xff", b'{"version":1,"version":1}',
                    b'{"version":1,"problem":{"objective":{"sense":"max","coefficients":[NaN]},"constraints":[]}}']:
            try:
                result = bridge.inspect_input(raw)
                self.assertEqual(result["status"], "invalid")
            except bridge.BridgeError as error:
                self.assertEqual(error.status, "invalid")

    def test_bridge_bounds_are_unsupported_or_invalid_never_accepted(self):
        cases = [encoded(document([], c=[0]*9, kind="optimal", point=[0]*9,
                                  inequality_multipliers=[], equality_multipliers=[])),
                 encoded(document([row([0], "<=", 0)]*17, c=(0,), kind="optimal", point=[0],
                                  inequality_multipliers=[0]*17, equality_multipliers=[])),
                 encoded(document([], c=(str(2**256),), kind="unbounded", base_point=[0], direction=[1])),
                 b" " * 65537]
        for raw in cases:
            with self.assertRaises(bridge.BridgeError) as caught:
                bridge.inspect_input(raw)
            self.assertEqual(caught.exception.status, "unsupported")

    def test_saved_receipt_only_validates_consistency_and_never_fresh_acceptance(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            raw = counterfeit_consistent_package(base / "package")
            # Hash consistency and a saved success flag cannot replace missing
            # compilation/gate evidence, so the counterfeit report is invalid.
            with self.assertRaises(bridge.BridgeError):
                bridge.validate_package(base / "package")
            with patch.object(bridge, "_toolchain", side_effect=bridge.BridgeError("failed", "blocked fresh compiler")):
                live = bridge.check_raw([raw], base / "fresh", base / "no-compiler")
            self.assertEqual(live["status"], "failed")
            self.assertNotEqual(live["status"], "lean_checked")
            self.assertEqual(live["commands"], [])

    def test_input_source_semantic_and_library_tampering_even_when_rehashed(self):
        mutations = [
            ("inputs/0000.json", lambda b: b.replace(b'"max"', b'"min"')),
            ("project/Checked0000.lean", lambda b: b + b"\naxiom untrusted : False\n"),
            ("project/Checked0000.lean", lambda b: b.replace("(1 : ℚ)".encode(), "(7 : ℚ)".encode(), 1)),
            ("semantic/0000.json", lambda b: b.replace(b'"max"', b'"min"')),
            ("project/LPCertificates/Input.lean", lambda b: b + b"\naxiom untrusted : False\n"),
        ]
        for name, mutate in mutations:
            with self.subTest(member=name), tempfile.TemporaryDirectory() as tmp:
                package = Path(tmp) / "package"
                counterfeit_consistent_package(package)
                member = package / name
                member.write_bytes(mutate(member.read_bytes()))
                remake_manifests(package)
                with self.assertRaises(bridge.BridgeError):
                    bridge.validate_package(package)

    def test_manifest_hash_duplicate_path_traversal_and_uncovered_members(self):
        mutations = [
            lambda m: m["files"][0].update(sha256="0"*64),
            lambda m: m["files"].append(deepcopy(m["files"][0])),
            lambda m: m["files"][0].update(path="../outside.lean"),
            lambda m: m["files"][0].update(path="/tmp/outside.lean"),
            lambda m: m["files"][0].update(bytes=True),
            lambda m: m.update(lean_source="import Mathlib"),
        ]
        for mutate in mutations:
            with tempfile.TemporaryDirectory() as tmp:
                package = Path(tmp) / "package"
                counterfeit_consistent_package(package)
                manifest = json.loads((package / "package-manifest.json").read_text())
                mutate(manifest)
                (package / "package-manifest.json").write_bytes(encoded(manifest))
                with self.assertRaises(bridge.BridgeError):
                    bridge.validate_package(package)
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp) / "package"
            counterfeit_consistent_package(package)
            (package / "uncovered.lean").write_text("axiom untrusted : False")
            with self.assertRaises(bridge.BridgeError):
                bridge.validate_package(package)

    def test_malformed_receipt_types_fail_closed(self):
        for receipt in [[], None, True, {"schema": bridge.SCHEMA, "status": "lean_checked", "inputs": [None]}]:
            with tempfile.TemporaryDirectory() as tmp:
                package = Path(tmp) / "package"
                counterfeit_consistent_package(package)
                (package / "receipt.json").write_bytes(encoded(receipt))
                remake_manifests(package)
                with self.assertRaises(bridge.BridgeError):
                    bridge.validate_package(package)

    def test_symlink_paths_and_existing_output_are_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            package = base / "package"
            counterfeit_consistent_package(package)
            (base / "alias").symlink_to(package, target_is_directory=True)
            with self.assertRaises(bridge.BridgeError):
                bridge.validate_package(base / "alias")
            with self.assertRaises(bridge.BridgeError):
                bridge.new_output(package)
            (package / "link").symlink_to(package / "receipt.json")
            with self.assertRaises(bridge.BridgeError):
                bridge.validate_package(package)

    def test_cli_invalid_json_never_launches_lean(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            bad = base / "input ; $(touch injection).json"
            bad.write_text('{"version":1,"version":1}')
            run = subprocess.run([sys.executable, str(ROOT / "bridge.py"), "check", str(bad),
                                  "--output", str(base / "fresh ; $(touch injection)"),
                                  "--lean-bin", str(base / "missing")],
                                 cwd=base, text=True, capture_output=True, check=False)
            self.assertEqual(run.returncode, 2, run.stderr)
            self.assertEqual(run.stderr, "")
            result = json.loads(run.stdout)
            self.assertEqual(result["status"], "invalid")
            receipt = json.loads(Path(result["receipt"]).read_text())
            self.assertEqual(receipt["commands"], [])
            self.assertFalse((base / "injection").exists())

    def test_fifo_input_is_rejected_without_blocking_or_lean_execution(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            fifo = base / "input.json"
            os.mkfifo(fifo)
            run = subprocess.run([sys.executable, str(ROOT / "bridge.py"), "check", str(fifo),
                                  "--output", str(base / "fresh"), "--lean-bin", str(base / "missing")],
                                 text=True, capture_output=True, timeout=3, check=False)
            self.assertEqual(run.returncode, 2, run.stderr)
            self.assertEqual(run.stderr, "")
            self.assertEqual(json.loads(run.stdout)["status"], "invalid")
            self.assertFalse((base / "fresh").exists())

    @unittest.skipUnless(os.environ.get("LP_BRIDGE_EXISTING_PACKAGE"), "Set LP_BRIDGE_EXISTING_PACKAGE for observed-package tamper checks")
    def test_observed_package_tampering_and_untrusted_saved_argv(self):
        original = Path(os.environ["LP_BRIDGE_EXISTING_PACKAGE"])
        raw = bridge.validate_package(original)
        self.assertEqual(len(raw), 13)
        mutations = [
            ("inputs/0000.json", lambda b: b.replace(b'"min"', b'"max"', 1)),
            ("semantic/0000.json", lambda b: b.replace(b'"min"', b'"max"', 1)),
            ("project/Checked0000.lean", lambda b: b + b"\naxiom untrusted : False\n"),
            ("project/Checked0000.lean", lambda b: b.replace("(1 : ℚ)".encode(), "(7 : ℚ)".encode(), 1)),
            ("project/LPCertificates/Input.lean", lambda b: b + b"\naxiom untrusted : False\n"),
        ]
        for name, mutate in mutations:
            with self.subTest(member=name), tempfile.TemporaryDirectory() as tmp:
                package = Path(tmp) / "package"
                shutil.copytree(original, package)
                member = package / name
                before = member.read_bytes()
                after = mutate(before)
                self.assertNotEqual(before, after)
                member.write_bytes(after)
                remake_manifests(package)
                with self.assertRaises(bridge.BridgeError):
                    bridge.validate_package(package)
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            package = base / "package"
            shutil.copytree(original, package)
            receipt = json.loads((package / "receipt.json").read_text())
            marker = base / "untrusted-command-ran"
            receipt["commands"][0]["argv"] = ["touch", str(marker)]
            (package / "receipt.json").write_bytes(encoded(receipt))
            remake_manifests(package)
            # Saved argv is merely metadata and never invoked by validation.
            # A live recheck must construct fresh trusted commands instead.
            self.assertEqual(bridge.validate_package(package), raw)
            self.assertFalse(marker.exists())

    @unittest.skipUnless(os.environ.get("LP_BRIDGE_LEAN_BIN"), "Set LP_BRIDGE_LEAN_BIN for actual fresh Lean checks")
    def test_fresh_lean_checks_fixture_and_metamorphic_batch(self):
        lean_bin = Path(os.environ["LP_BRIDGE_LEAN_BIN"])
        keep = os.environ.get("LP_BRIDGE_KEEP_OUTPUT")
        temporary = None
        if keep:
            output = Path(keep)
        else:
            temporary = tempfile.TemporaryDirectory()
            output = Path(temporary.name) / "fresh"
        try:
            docs = accepted_documents()
            raw = [encoded(doc) for doc in docs]
            self.assertTrue(all(raw_certificate_accepts(doc) for doc in docs))
            record = bridge.check_raw(raw, output, lean_bin)
            self.assertEqual(record["status"], "lean_checked", record.get("failure"))
            self.assertEqual(len(record["inputs"]), 13)
            self.assertTrue(all(item["status"] == "lean_checked" for item in record["inputs"]))
            commands = record["commands"]
            self.assertTrue(commands)
            self.assertTrue(all(command["exit_code"] == 0 for command in commands))
            labels = [command["label"] for command in commands]
            self.assertEqual(len(labels), len(set(labels)))
            self.assertEqual(sum(label.startswith("instance-") for label in labels), 13)
            self.assertFalse((output / ".work").exists())
            self.assertEqual(bridge.validate_package(output), raw)
            print("Independent fresh Lean package:", output)
            print("Fresh Lean commands:", len(commands), "instances:", len(record["inputs"]))
        finally:
            if temporary:
                temporary.cleanup()


if __name__ == "__main__":
    unittest.main()
