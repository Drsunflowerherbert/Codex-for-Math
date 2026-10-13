"""Bridge boundary tests. These tests do not substitute for live Lean acceptance."""

from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import bridge  # noqa: E402


def fixture(name="optimal_mixed_redundant"):
    return (ROOT / "examples" / (name + ".json")).read_bytes()


def encode(document):
    return json.dumps(document).encode()


def constant(n=1, rows=()):
    return {"version": 1, "problem": {"objective": {"sense": "max", "coefficients": [0] * n},
            "constraints": list(rows)}, "certificate": {"kind": "optimal", "point": [0] * n,
            "inequality_multipliers": [0] * len(rows), "equality_multipliers": []}}


class InputAndRenderingTests(unittest.TestCase):
    def test_nine_accepted_fixture_inputs(self):
        count = 0
        for path in sorted((ROOT / "examples").glob("*.json")):
            if path.stem.startswith(("optimal_", "infeasible_", "unbounded_")):
                info = bridge.inspect_input(path.read_bytes())
                self.assertEqual(info["status"], "accepted", path.name)
                self.assertEqual(info["input_sha256"], bridge.sha(path.read_bytes()))
                self.assertIn(b"by decide +kernel", bridge._render_unchecked(info))
                count += 1
        self.assertEqual(count, 9)

    def test_original_mixed_rows_are_not_python_normalized(self):
        info = bridge.inspect_input(fixture())
        rows = info["semantic"]["rows"]
        self.assertEqual(rows[2]["coefficients"], ["1", "0"])
        self.assertEqual(rows[2]["sense"], ">=")
        self.assertEqual(info["semantic"]["row_multipliers"], ["1", "3/4", "0", "0", "1/2"])
        source = bridge._render_unchecked(info).decode()
        self.assertIn("RowSense.ge, RowSense.ge, RowSense.eq", source)
        self.assertIn("ObjectiveSense.maximize", source)

    def test_original_min_objective_is_not_negated(self):
        info = bridge.inspect_input(fixture("unbounded_min_lower_dimensional"))
        original = json.loads(fixture("unbounded_min_lower_dimensional"))
        self.assertEqual(info["semantic"]["objective"], [str(x) for x in original["problem"]["objective"]["coefficients"]])
        self.assertIn(b"ObjectiveSense.minimize", bridge._render_unchecked(info))

    def test_interleaved_multiplier_order_and_negative_equality(self):
        document = {"version": 1, "problem": {"objective": {"sense": "max", "coefficients": [-3]},
                    "constraints": [{"coefficients": [1], "rhs": 0, "sense": ">="},
                                    {"coefficients": [2], "rhs": 1, "sense": "="},
                                    {"coefficients": [1], "rhs": 1, "sense": "<="}]},
                    "certificate": {"kind": "optimal", "point": ["1/2"],
                                    "inequality_multipliers": [0, 0], "equality_multipliers": ["-3/2"]}}
        info = bridge.inspect_input(encode(document))
        self.assertEqual(info["semantic"]["row_multipliers"], ["0", "-3/2", "0"])

    def test_noncanonical_rationals_are_canonicalized_but_bytes_bound(self):
        first = constant()
        first["problem"]["objective"]["coefficients"] = ["+000/3"]
        first["certificate"]["point"] = ["-000/2"]
        second = constant()
        left, right = bridge.inspect_input(encode(first)), bridge.inspect_input(encode(second))
        self.assertEqual(left["semantic"], right["semantic"])
        self.assertNotEqual(left["input_sha256"], right["input_sha256"])

    def test_zero_dimensions_and_empty_vectors(self):
        source = bridge._render_unchecked(bridge.inspect_input(encode(constant(0))))
        self.assertIn(b"InputProblem 0 0", source)
        self.assertIn(b"def point : Fin 0", source)
        self.assertIn(b"![]", source)

    def test_render_is_deterministic_and_not_a_checked_status(self):
        info = bridge.inspect_input(fixture())
        self.assertEqual(bridge._render_unchecked(info), bridge._render_unchecked(info))
        self.assertEqual(info["status"], "accepted")
        self.assertNotIn("lean_evidence", info)

    def test_renderer_refuses_injected_hash(self):
        info = bridge.inspect_input(fixture())
        info["input_sha256"] = "0\naxiom injected : False"
        with self.assertRaises(bridge.BridgeError):
            bridge._render_unchecked(info)

    def test_renderer_refuses_injected_dimension(self):
        info = bridge.inspect_input(fixture())
        info["semantic"]["dimension"] = "1; axiom bad : False"
        with self.assertRaises(bridge.BridgeError):
            bridge._render_unchecked(info)

    def test_untrusted_syntax_is_invalid_not_lean_source(self):
        document = constant()
        document["certificate"]["point"] = ["0)\naxiom bad : False"]
        self.assertEqual(bridge.inspect_input(encode(document))["status"], "invalid")

    def test_duplicate_keys_and_float_invalid(self):
        self.assertEqual(bridge.inspect_input(fixture("invalid_duplicate_key"))["status"], "invalid")
        self.assertEqual(bridge.inspect_input(fixture("invalid_float"))["status"], "invalid")

    def test_invalid_utf8(self):
        with self.assertRaises(bridge.BridgeError) as result:
            bridge.inspect_input(b"\xff")
        self.assertEqual(result.exception.status, "invalid")

    def test_input_byte_limit(self):
        with self.assertRaises(bridge.BridgeError) as result:
            bridge.inspect_input(b" " * (bridge.MAX_INPUT_BYTES + 1))
        self.assertEqual(result.exception.status, "unsupported")

    def test_dimension_limit(self):
        with self.assertRaises(bridge.BridgeError) as result:
            bridge.inspect_input(encode(constant(9)))
        self.assertEqual(result.exception.status, "unsupported")

    def test_row_limit(self):
        rows = [{"coefficients": [0], "sense": "<=", "rhs": 0}] * 17
        with self.assertRaises(bridge.BridgeError) as result:
            bridge.inspect_input(encode(constant(rows=rows)))
        self.assertEqual(result.exception.status, "unsupported")

    def test_bit_boundary_and_unreduced_literals(self):
        document = constant()
        document["certificate"]["point"] = [str(2**256 - 1)]
        self.assertEqual(bridge.inspect_input(encode(document))["status"], "accepted")
        document["certificate"]["point"] = [str(2**256)]
        with self.assertRaises(bridge.BridgeError) as result:
            bridge.inspect_input(encode(document))
        self.assertEqual(result.exception.status, "unsupported")
        document["certificate"]["point"] = [f"{2**257}/{2**257}"]
        with self.assertRaises(bridge.BridgeError):
            bridge.inspect_input(encode(document))


class FileAndAttemptTests(unittest.TestCase):
    def test_existing_output_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "old"
            output.mkdir()
            sentinel = output / "keep"
            sentinel.write_bytes(b"previous work")
            with self.assertRaises(bridge.BridgeError):
                bridge.new_output(output)
            self.assertEqual(sentinel.read_bytes(), b"previous work")

    def test_symlink_leaf_and_parent_output_refused(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = root / "target"
            target.mkdir()
            link = root / "link"
            link.symlink_to(target, target_is_directory=True)
            for path in (link, link / "fresh"):
                with self.assertRaises(bridge.BridgeError):
                    bridge.new_output(path)
            self.assertFalse((target / "fresh").exists())

    def test_input_symlink_and_fifo_refused_without_blocking(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            source.write_bytes(b"{}")
            link = root / "link"
            link.symlink_to(source)
            fifo = root / "fifo"
            os.mkfifo(fifo)
            for path in (link, fifo):
                with self.assertRaises(bridge.BridgeError):
                    bridge.read_regular(path, bridge.MAX_INPUT_BYTES)

    def test_parent_traversal_output_refused(self):
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaises(bridge.BridgeError):
                bridge.new_output(Path(temporary) / ".." / "bridge-escape")

    def test_preflight_rejection_never_launches_toolchain(self):
        with tempfile.TemporaryDirectory() as temporary, mock.patch.object(bridge, "_toolchain") as toolchain:
            output = Path(temporary) / "attempt"
            result = bridge.check_raw([fixture("rejected_negative_multiplier")], output, Path("/missing"))
            self.assertEqual(result["status"], "rejected")
            self.assertEqual(result["commands"], [])
            toolchain.assert_not_called()
            self.assertTrue((output / "receipt.json").exists())

    def test_unsupported_preflight_never_launches_toolchain(self):
        with tempfile.TemporaryDirectory() as temporary, mock.patch.object(bridge, "_toolchain") as toolchain:
            result = bridge.check_raw([encode(constant(9))], Path(temporary) / "attempt", Path("/missing"))
            self.assertEqual(result["status"], "unsupported")
            toolchain.assert_not_called()

    def test_toolchain_failure_leaves_failed_record(self):
        with tempfile.TemporaryDirectory() as temporary, mock.patch.object(bridge, "_toolchain", side_effect=bridge.BridgeError("failed", "no pinned compiler")):
            result = bridge.check_raw([fixture()], Path(temporary) / "attempt", Path("/missing"))
            self.assertEqual(result["status"], "failed")
            self.assertNotEqual(result["status"], "lean_checked")

    def test_batch_limit(self):
        with tempfile.TemporaryDirectory() as temporary:
            result = bridge.check_raw([fixture()] * 17, Path(temporary) / "attempt", Path("/missing"))
            self.assertEqual(result["status"], "unsupported")


class EvidenceAndProcessTests(unittest.TestCase):
    def test_empty_and_malformed_evidence_rejected(self):
        for text in ("", "MATH_EVIDENCE_TARGET not-json", "MATH_EVIDENCE_TARGET []"):
            with self.assertRaises(bridge.BridgeError):
                bridge._instance_gate(text)
        with self.assertRaises(bridge.BridgeError):
            bridge._expected_gate("")

    def test_interruption_signal_raises(self):
        with self.assertRaises(KeyboardInterrupt):
            bridge._interrupt_signal(signal.SIGTERM, None)

    def test_shell_false_keeps_argument_literal(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            record = {"commands": []}
            runner = bridge.Runner(output, record, {"PATH": "/usr/bin:/bin"})
            literal = "$(touch forbidden) `touch forbidden` ; exit 9"
            text = runner.run("literal", [sys.executable, "-c", "import sys; print(sys.argv[1])", literal], output)
            self.assertEqual(text.strip(), literal)
            self.assertFalse((output / "forbidden").exists())
            self.assertEqual(record["commands"][0]["exit_code"], 0)

    def test_timeout_cancels_process_group_and_records_failure(self):
        with tempfile.TemporaryDirectory() as temporary, mock.patch.object(bridge, "TIMEOUT_SECONDS", 0.2), mock.patch.object(bridge, "_limits", lambda: None):
            output = Path(temporary)
            record = {"commands": []}
            runner = bridge.Runner(output, record, {"PATH": "/usr/bin:/bin"})
            code = "import subprocess,time; p=subprocess.Popen(['/bin/sleep','30']); print(p.pid, flush=True); time.sleep(30)"
            with self.assertRaises(bridge.BridgeError):
                runner.run("timeout", [sys.executable, "-c", code], output)
            self.assertEqual(record["commands"][0]["termination"], "timeout")
            child = int((output / "logs/timeout.stdout.log").read_text().strip())
            state = Path(f"/proc/{child}/stat")
            self.assertTrue(not state.exists() or state.read_text().split()[2] == "Z")

    def test_output_cap_is_failed_and_bounded(self):
        with tempfile.TemporaryDirectory() as temporary, mock.patch.object(bridge, "MAX_LOG_BYTES", 1024):
            output = Path(temporary)
            record = {"commands": []}
            runner = bridge.Runner(output, record, {"PATH": "/usr/bin:/bin"})
            with self.assertRaises(bridge.BridgeError):
                runner.run("overflow", [sys.executable, "-c", "print('x'*10000)"], output)
            self.assertEqual(record["commands"][0]["termination"], "output_limit")
            self.assertLessEqual((output / "logs/overflow.stdout.log").stat().st_size, 1024)

    def test_fake_receipt_is_not_fresh_lean_acceptance(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            (output / "receipt.json").write_bytes(bridge.json_bytes({"schema": bridge.SCHEMA, "status": "lean_checked", "inputs": []}))
            (output / "package-manifest.json").write_bytes(bridge.json_bytes(bridge._package_manifest(output)))
            with self.assertRaises(bridge.BridgeError):
                bridge.validate_package(output)

    def test_nonobject_receipt_fails_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            (output / "receipt.json").write_bytes(b"[]")
            (output / "package-manifest.json").write_bytes(bridge.json_bytes(bridge._package_manifest(output)))
            with self.assertRaises(bridge.BridgeError):
                bridge.validate_package(output)

    def test_nonobject_input_record_fails_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            (output / "receipt.json").write_bytes(bridge.json_bytes({"schema": bridge.SCHEMA, "status": "lean_checked", "inputs": [None]}))
            (output / "package-manifest.json").write_bytes(bridge.json_bytes(bridge._package_manifest(output)))
            with self.assertRaises(bridge.BridgeError):
                bridge.validate_package(output)

    def test_manifest_path_injection_and_duplicate_refused(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            for path in ("../escape", "/absolute", "a//b"):
                manifest = {"schema": bridge.SCHEMA + "/package-manifest", "files": [{"path": path, "bytes": 0, "sha256": "0" * 64}]}
                (output / "package-manifest.json").write_bytes(bridge.json_bytes(manifest))
                with self.assertRaises(bridge.BridgeError):
                    bridge.validate_package(output)


if __name__ == "__main__":
    unittest.main()
