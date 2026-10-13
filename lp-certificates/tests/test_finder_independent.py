"""Independent raw-row audit of the deliberately incomplete LP finder."""

from copy import deepcopy
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))
import finder  # noqa: E402
import verifier  # noqa: E402
from test_independent import original_feasible, raw_certificate_accepts, row  # noqa: E402


def problem(rows, c=(1,), sense="max"):
    return {"version": 1,
            "problem": {"objective": {"sense": sense, "coefficients": list(c)},
                        "constraints": deepcopy(list(rows))}}


class IndependentFinderReview(unittest.TestCase):
    def audit_answer(self, raw, result):
        self.assertTrue(result["incomplete"])
        self.assertIn(result["status"], ["found", "unknown", "invalid"])
        if result["status"] == "found":
            cert = result["certificate_document"]
            self.assertEqual(cert["problem"], raw["problem"])
            self.assertEqual(cert["version"], raw["version"])
            self.assertTrue(raw_certificate_accepts(cert), cert)
            self.assertTrue(result["verification"]["accepted"])
            self.assertEqual(result["certificate_kind"], cert["certificate"]["kind"])
        else:
            for key in ["certificate_document", "certificate_kind", "verification"]:
                self.assertNotIn(key, result)
        return result["status"]

    def test_all_accepted_fixture_problems_have_independently_valid_found_witness(self):
        accepted = [p for p in (ROOT / "examples").glob("*.json")
                    if p.name.startswith(("optimal_", "infeasible_", "unbounded_"))]
        self.assertEqual(len(accepted), 9)
        for path in accepted:
            full = json.loads(path.read_text())
            raw = {"version": full["version"], "problem": full["problem"]}
            answer = finder.find(raw)
            self.assertEqual(self.audit_answer(raw, answer), "found", path.name)
            self.assertEqual(answer, finder.find(deepcopy(raw)), path.name)

    def test_bounded_exhaustive_one_dimensional_search_output(self):
        # This experiment audits emitted witnesses, not a general completeness claim.
        rows = [row([a], sense, b)
                for a, sense, b in product([-1, 0, 1], ["<=", ">=", "="], [-1, 0, 1])]
        counts = {"found": 0, "unknown": 0, "invalid": 0}
        kinds = {"optimal": 0, "infeasible": 0, "unbounded": 0}
        for pair, c, sense in product(product(rows, repeat=2), [-1, 0, 1], ["max", "min"]):
            raw = problem(pair, (c,), sense)
            result = finder.find(raw)
            status = self.audit_answer(raw, result)
            counts[status] += 1
            self.assertNotEqual(status, "invalid", raw)
            if status == "found":
                kinds[result["certificate_kind"]] += 1
                cert = result["certificate_document"]["certificate"]
                if cert["kind"] == "infeasible":
                    self.assertFalse(any(original_feasible(raw["problem"], [Q(k, 2)]) for k in range(-4, 5)))
        self.assertEqual(sum(counts.values()), 4374)
        self.assertTrue(all(n > 0 for n in kinds.values()))
        print("Independent finder counts:", counts, "found kinds:", kinds)

    def test_supported_unbounded_problem_can_return_unknown(self):
        # Exact feasible improving ray (1,3) falls outside the integer direction grid.
        raw = problem([row([3, -1], "=", 0)], (1, 0))
        witness = {**deepcopy(raw), "certificate": {
            "kind": "unbounded", "base_point": [0, 0], "direction": [1, 3]}}
        self.assertTrue(raw_certificate_accepts(witness))
        answer = finder.find(raw)
        self.assertEqual(self.audit_answer(raw, answer), "unknown")
        self.assertEqual(answer["reason"], "no_certificate_in_bounded_search")

    def test_search_limits_are_unknown_without_problem_classification(self):
        cases = [problem([], (1, 0, 0, 0)),
                 problem([row([0], "<=", 0)] * 9, (0,)),
                 problem([row([0], "<=", 0)] * 8 + [row([0], "<=", -1)], (0,))]
        for raw in cases:
            answer = finder.find(raw)
            self.assertEqual(self.audit_answer(raw, answer), "unknown")
            self.assertEqual(answer["reason"], "search_limits_exceeded")

    def test_zero_dimensions_free_negative_points_and_minimization(self):
        cases = [problem([], ()), problem([row([], "=", 1)], ()),
                 problem([row([1], "=", -3)], (0,)),
                 problem([row([1], ">=", "2/3")], ("3/2",), "min"),
                 problem([row([1, -1], "=", 0)], (-2, 1), "min")]
        for raw in cases:
            answer = finder.find(raw)
            self.assertEqual(self.audit_answer(raw, answer), "found", raw)

    def test_noncanonical_exact_representations_preserved(self):
        raw = problem([row(["+02/2"], ">=", "0002/3")], ("+06/4",), "min")
        answer = finder.find(raw)
        self.assertEqual(self.audit_answer(raw, answer), "found")
        self.assertEqual(answer["verification"]["certified_objective_value"], "1")

    def test_untrusted_schema_and_injection_strings(self):
        baseline = problem([row([1], "<=", 1)])
        bad_values = [True, False, 1.0, None, "1; import Mathlib", "1\naxiom bad : False",
                      "$(touch /tmp/lp-finder-injection)", "1/0", "1/-2"]
        for value in bad_values:
            raw = deepcopy(baseline)
            raw["problem"]["objective"]["coefficients"] = [value]
            self.assertEqual(self.audit_answer(raw, finder.find(raw)), "invalid")
        for field, value in [("sense", "<=\naxiom bad : False"), ("coefficients", []), ("rhs", False)]:
            raw = deepcopy(baseline)
            raw["problem"]["constraints"][0][field] = value
            self.assertEqual(self.audit_answer(raw, finder.find(raw)), "invalid")
        for extra in ["certificate", "lean_source", "../../source.lean", "import Mathlib"]:
            raw = deepcopy(baseline)
            raw[extra] = "untrusted"
            self.assertEqual(self.audit_answer(raw, finder.find(raw)), "invalid")
        texts = ["{", "[" * 11000 + "]" * 11000,
                 '{"version":1,"version":1,"problem":{}}',
                 '{"version":1,"problem":{"objective":{"sense":"max","coefficients":[NaN]},"constraints":[]}}',
                 json.dumps(baseline).replace('"sense": "max"', '"sense": "min", "sense": "max"')]
        for text in texts:
            self.assertEqual(finder.find_json(text)["status"], "invalid")

    def test_cli_found_unknown_invalid_are_explicit(self):
        cases = [(json.dumps(problem([], (1,))), 0, "found"),
                 (json.dumps(problem([row([3, -1], "=", 0)], (1, 0))), 1, "unknown"),
                 ("{", 2, "invalid")]
        for text, code, status in cases:
            run = subprocess.run([sys.executable, str(ROOT / "finder.py"), "-"],
                                 input=text, text=True, capture_output=True, check=False)
            self.assertEqual(run.returncode, code)
            self.assertEqual(run.stderr, "")
            answer = json.loads(run.stdout)
            self.assertEqual(answer["status"], status)
            self.assertTrue(answer["incomplete"])

    def test_huge_rational_regression_fails_closed(self):
        huge = "1" + "0" * 2199
        raw = problem([], (huge,))
        full = {**deepcopy(raw), "certificate": {
            "kind": "unbounded", "base_point": [0], "direction": [huge]}}
        # Previously multiplication was valid but decimal evidence formatting
        # raised ValueError at 4400 digits. Bounded inputs must now be invalid.
        self.assertEqual(verifier.verify(full)["status"], "invalid")
        self.assertEqual(finder.find(raw)["status"], "invalid")
        self.assertEqual(verifier.verify_json(json.dumps(full))["status"], "invalid")

    def test_arithmetic_evidence_limit_fails_closed(self):
        # Each input is below 1024 bits, while the sum of fractions may have a
        # denominator exceeding the independent output resource bound.
        denominator = 2**1000
        raw = problem([row([f"1/{denominator + k}"], "<=", 0) for k in range(1, 17)], (0,))
        full = {**raw, "certificate": {
            "kind": "optimal", "point": [0],
            "inequality_multipliers": [1] * 16, "equality_multipliers": []}}
        self.assertEqual(verifier.verify(full)["status"], "invalid")
        self.assertFalse(verifier.verify(full)["accepted"])

    def test_reduced_process_digit_limit_returns_invalid_without_exception(self):
        # Lowering a process-local formatting limit exercises fail-closed
        # diagnostics; it does not change persistent runtime configuration.
        script = """
import json, sys
sys.path.insert(0, sys.argv[1])
import verifier
sys.set_int_max_str_digits(640)
d = 2**1000
doc = {"version": 1, "problem": {"objective": {"sense": "max", "coefficients": [0]},
    "constraints": [{"coefficients": [f"1/{d+k}"], "sense": "<=", "rhs": 0} for k in range(1, 9)]},
    "certificate": {"kind": "optimal", "point": [0], "inequality_multipliers": [1]*8,
                    "equality_multipliers": []}}
print(json.dumps(verifier.verify(doc)))
"""
        run = subprocess.run([sys.executable, "-c", script, str(ROOT)],
                             text=True, capture_output=True, check=False)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(run.stderr, "")
        answer = json.loads(run.stdout)
        self.assertEqual(answer["status"], "invalid")
        self.assertFalse(answer["accepted"])


if __name__ == "__main__":
    unittest.main()
