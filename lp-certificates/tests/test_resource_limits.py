import json
from fractions import Fraction
from pathlib import Path
import subprocess
import sys
import unittest

import verifier


def free_ray(coefficient, direction):
    return {"version": 1, "problem": {"objective": {"sense": "max", "coefficients": [coefficient]},
            "constraints": []}, "certificate": {"kind": "unbounded", "base_point": [0], "direction": [direction]}}


class ResourceLimits(unittest.TestCase):
    def test_reported_large_gain_fails_closed(self):
        value = "1" + "0" * 2199
        result = verifier.verify_json(json.dumps(free_ray(value, value)))
        self.assertEqual(result["status"], "invalid")
        self.assertFalse(result["accepted"])
        self.assertEqual(result["diagnostics"][0]["code"], "resource_limit")

    def test_cli_large_gain_has_no_traceback(self):
        value = "1" + "0" * 2199
        command = [sys.executable, str(Path(verifier.__file__).resolve()), "-"]
        process = subprocess.run(command, input=json.dumps(free_ray(value, value)),
                                 text=True, capture_output=True, timeout=10)
        self.assertEqual(process.returncode, 2)
        self.assertEqual(process.stderr, "")
        self.assertEqual(json.loads(process.stdout)["status"], "invalid")

    def test_numerator_and_denominator_budgets(self):
        for value in (1 << 1024, f"1/{1 << 1024}"):
            with self.subTest(value_type=type(value).__name__):
                self.assertEqual(verifier.verify(free_ray(value, 1))["status"], "invalid")
        self.assertTrue(verifier.verify(free_ray(str((1 << 1024) - 1), 1))["accepted"])

    def test_output_bit_budget(self):
        with self.assertRaises(verifier.SchemaError) as caught:
            verifier.fraction_string(Fraction(1 << 8192))
        self.assertEqual(caught.exception.code, "resource_limit")

    def test_output_runtime_format_budget(self):
        prior = sys.get_int_max_str_digits()
        try:
            sys.set_int_max_str_digits(640)
            # Each input is below 1024 bits and 640 digits; their exact product
            # remains representable. Direct output failure must still fail closed.
            with self.assertRaises(verifier.SchemaError) as caught:
                verifier.fraction_string(Fraction(1 << 2500))
            self.assertEqual(caught.exception.code, "resource_limit")
            self.assertTrue(verifier.verify(free_ray(1, 1))["accepted"])
        finally:
            sys.set_int_max_str_digits(prior)

    def test_dimensions_and_row_budget(self):
        document = free_ray(1, 1)
        document["problem"]["objective"]["coefficients"] = [0] * 33
        self.assertEqual(verifier.verify(document)["status"], "invalid")
        document = free_ray(1, 1)
        document["problem"]["constraints"] = [{"coefficients": [0], "sense": "<=", "rhs": 0}] * 129
        self.assertEqual(verifier.verify(document)["status"], "invalid")

    def test_json_byte_budget_and_text_type(self):
        result = verifier.verify_json(" " * (verifier.MAX_INPUT_BYTES + 1))
        self.assertEqual(result["diagnostics"][0]["code"], "resource_limit")
        self.assertEqual(verifier.verify_json(b"{}")["status"], "invalid")
        self.assertEqual(verifier.verify_json("\ud800")["status"], "invalid")

    def test_total_rational_budget(self):
        coefficient = (1 << 1000) - 1
        document = free_ray(0, 0)
        document["problem"]["objective"]["coefficients"] = [0] * 32
        document["problem"]["constraints"] = [
            {"coefficients": [coefficient] * 32, "sense": "<=", "rhs": 0}] * 5
        document["certificate"]["base_point"] = [0] * 32
        document["certificate"]["direction"] = [0] * 32
        self.assertEqual(verifier.verify(document)["diagnostics"][0]["code"], "resource_limit")


if __name__ == "__main__":
    unittest.main()
