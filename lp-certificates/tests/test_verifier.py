"""Exact witness, schema-boundary, and adversarial tests for verifier.py."""

from __future__ import annotations

import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("lp_certificate_verifier", ROOT / "verifier.py")
assert spec is not None and spec.loader is not None
verifier = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = verifier
spec.loader.exec_module(verifier)


def document(objective, constraints, certificate, sense="max"):
    return {"version": 1, "problem": {"objective": {"sense": sense, "coefficients": objective},
            "constraints": constraints}, "certificate": certificate}


def row(coefficients, rhs, sense="<="):
    return {"coefficients": coefficients, "sense": sense, "rhs": rhs}


def optimal(point, inequalities, equalities=None):
    return {"kind": "optimal", "point": point, "inequality_multipliers": inequalities,
            "equality_multipliers": [] if equalities is None else equalities}


def infeasible(inequalities, equalities=None):
    return {"kind": "infeasible", "inequality_multipliers": inequalities,
            "equality_multipliers": [] if equalities is None else equalities}


def unbounded(base, direction):
    return {"kind": "unbounded", "base_point": base, "direction": direction}


class FixtureTests(unittest.TestCase):
    EXPECTED = {
        "optimal_mixed_redundant": ("accepted", "10"),
        "optimal_min_fraction_equality": ("accepted", "1/2"),
        "optimal_zero_variables": ("accepted", "0"),
        "optimal_constant_no_rows": ("accepted", "0"),
        "infeasible_mixed": ("accepted", None),
        "infeasible_equalities": ("accepted", None),
        "infeasible_zero_variables": ("accepted", None),
        "unbounded_min_lower_dimensional": ("accepted", None),
        "unbounded_max_no_rows": ("accepted", None),
        "rejected_negative_multiplier": ("rejected", None),
        "rejected_bad_combination": ("rejected", None),
        "rejected_infeasible_nonstrict": ("rejected", None),
        "rejected_unbounded_bad_base": ("rejected", None),
        "rejected_unbounded_bad_direction": ("rejected", None),
        "rejected_unbounded_zero_gain": ("rejected", None),
        "invalid_float": ("invalid", None),
        "invalid_duplicate_key": ("invalid", None),
    }

    def test_fixture_corpus(self):
        paths = sorted((ROOT / "examples").glob("*.json"))
        self.assertEqual({path.stem for path in paths}, set(self.EXPECTED))
        for path in paths:
            with self.subTest(example=path.stem):
                result = verifier.verify_json(path.read_text())
                status, value = self.EXPECTED[path.stem]
                self.assertEqual(result["status"], status)
                self.assertEqual(result["accepted"], status == "accepted")
                self.assertEqual(result.get("certified_objective_value"), value)
                self.assertEqual(bool(result["diagnostics"]), status != "accepted")

    def test_hand_computed_mixed_bound(self):
        # 1(x+y) + (3/4)(2x+2y) + (1/2)(x-y) = 3x+2y <= 10.
        # At x=y=2 all three contributing rows attain their RHS.
        self.assertEqual(Fraction(1) + 2 * Fraction(3, 4) + Fraction(1, 2), 3)
        self.assertEqual(Fraction(1) + 2 * Fraction(3, 4) - Fraction(1, 2), 2)
        self.assertEqual(4 + 8 * Fraction(3, 4), 10)
        result = verifier.verify_json((ROOT / "examples/optimal_mixed_redundant.json").read_text())
        self.assertTrue(result["accepted"])
        self.assertEqual(result["certified_objective_value"], "10")

    def test_hand_computed_equality_contradiction(self):
        # 2(x+y=0) - (2x+2y=1) would assert 0=-1.
        self.assertEqual(2 * 1 - 2, 0)
        self.assertEqual(2 * 0 - 1, -1)
        result = verifier.verify_json((ROOT / "examples/infeasible_equalities.json").read_text())
        self.assertTrue(result["accepted"])
        self.assertEqual(result["checks"][-1]["lhs"], "-1")

    def test_hand_computed_minimizing_ray(self):
        # (1+t,t), t>=0, satisfies y>=0 and x-y=1; -2x+y=-2-t.
        for parameter in (Fraction(0), Fraction(1, 3), Fraction(7), Fraction(1000)):
            x, y = 1 + parameter, parameter
            self.assertGreaterEqual(y, 0)
            self.assertEqual(x - y, 1)
            self.assertEqual(-2 * x + y, -2 - parameter)
        result = verifier.verify_json((ROOT / "examples/unbounded_min_lower_dimensional.json").read_text())
        self.assertTrue(result["accepted"])
        self.assertEqual(result["checks"][-1]["lhs"], "1")


class ExactAndTransformationTests(unittest.TestCase):
    def test_no_binary_float_roundoff(self):
        candidate = document(["3/10"], [row([1], 1), row([1], 1)],
                             optimal([1], ["1/10", "1/5"]))
        result = verifier.verify(candidate)
        self.assertTrue(result["accepted"])
        self.assertEqual(result["certified_objective_value"], "3/10")

    def test_large_rational_arithmetic(self):
        numerator = 10 ** 100 + 13
        candidate = document([str(numerator) + "/17"], [row([19], 7)],
                             optimal(["7/19"], [str(numerator) + "/323"]))
        result = verifier.verify(candidate)
        self.assertTrue(result["accepted"])
        self.assertEqual(Fraction(result["certified_objective_value"]), Fraction(7 * numerator, 323))

    def test_positive_row_scaling_preserves_certificate(self):
        # Multiplying a <= row by 3/7 requires dividing its multiplier by 3/7.
        original = document([2], [row([1], 3)], optimal([3], [2]))
        scaled = document([2], [row(["3/7"], "9/7")], optimal([3], ["14/3"]))
        self.assertTrue(verifier.verify(original)["accepted"])
        self.assertTrue(verifier.verify(scaled)["accepted"])

    def test_positive_objective_scaling_preserves_point(self):
        original = document([2], [row([1], 3)], optimal([3], [2]))
        scaled = document(["10/3"], [row([1], 3)], optimal([3], ["10/3"]))
        self.assertEqual(verifier.verify(original)["certified_objective_value"], "6")
        self.assertEqual(verifier.verify(scaled)["certified_objective_value"], "10")

    def test_alternative_optimal_multipliers(self):
        source = json.loads((ROOT / "examples/optimal_mixed_redundant.json").read_text())
        source["certificate"]["inequality_multipliers"] = ["5/2", 0, 0, 0]
        self.assertTrue(verifier.verify(source)["accepted"])

    def test_row_order_and_separate_multiplier_order(self):
        # Equality rows interleave inequality rows; each multiplier array has its own order.
        candidate = document([2, -1], [row([0, 1], 1, "="), row([1, 0], 4),
                             row([1, -1], 3, "="), row([1, 0], 0, ">=")],
                             optimal([4, 1], [1, 0], [0, 1]))
        self.assertTrue(verifier.verify(candidate)["accepted"])

    def test_minimization_with_positive_ge_multiplier(self):
        candidate = document(["3/2"], [row([1], "2/3", ">=")],
                             optimal(["2/3"], ["3/2"]), sense="min")
        self.assertEqual(verifier.verify(candidate)["certified_objective_value"], "1")

    def test_negative_free_equality_multiplier(self):
        candidate = document([-3], [row([2], 1, "=")], optimal(["1/2"], [], ["-3/2"]))
        self.assertTrue(verifier.verify(candidate)["accepted"])

    def test_free_variables_are_not_implicitly_nonnegative(self):
        candidate = document([0], [], optimal([-7], []))
        self.assertTrue(verifier.verify(candidate)["accepted"])

    def test_zero_dimensional_empty_problem(self):
        self.assertTrue(verifier.verify(document([], [], optimal([], [])))["accepted"])
        self.assertFalse(verifier.verify(document([], [], unbounded([], [])))["accepted"])

    def test_positive_rescaling_of_ray_and_contradiction(self):
        self.assertTrue(verifier.verify(document([1], [], unbounded([0], ["1/999"])))["accepted"])
        contradiction = document([0], [row([1], 0), row([1], 1, ">=")],
                                 infeasible(["1/999", "1/999"]))
        self.assertTrue(verifier.verify(contradiction)["accepted"])


class SemanticFailureTests(unittest.TestCase):
    def assert_rejected_by(self, candidate, code):
        result = verifier.verify(candidate)
        self.assertEqual(result["status"], "rejected")
        self.assertFalse(result["accepted"])
        self.assertIn(code, {entry["code"] for entry in result["diagnostics"]})
        self.assertNotIn("certified_objective_value", result)

    def test_infeasible_optimal_point(self):
        self.assert_rejected_by(document([0], [row([1], 1)], optimal([2], [0])), "point_feasibility")

    def test_unattained_bound(self):
        self.assert_rejected_by(document([1], [row([1], 1)], optimal([0], [1])), "bound_attained")

    def test_wrong_objective_coefficients(self):
        self.assert_rejected_by(document([2], [row([1], 1)], optimal([1], [1])), "coefficient_identity")

    def test_infeasibility_nonzero_combined_coefficients(self):
        self.assert_rejected_by(document([0], [row([1], -1)], infeasible([1])), "coefficient_identity")

    def test_infeasibility_negative_multiplier(self):
        self.assert_rejected_by(document([], [row([], 1)], infeasible([-1])), "multiplier_nonnegative")

    def test_infeasibility_rhs_must_be_strictly_negative(self):
        for rhs in (0, 1):
            with self.subTest(rhs=rhs):
                self.assert_rejected_by(document([], [row([], rhs)], infeasible([1])), "contradiction")

    def test_unbounded_ray_violates_inequality(self):
        self.assert_rejected_by(document([1], [row([1], 0)], unbounded([0], [1])), "recession_direction")

    def test_unbounded_ray_violates_equality(self):
        self.assert_rejected_by(document([1], [row([1], 0, "=")], unbounded([0], [1])), "recession_direction")

    def test_unbounded_base_violates_equality(self):
        self.assert_rejected_by(document([0, 1], [row([1, 0], 0, "=")],
                                         unbounded([1, 0], [0, 1])), "point_feasibility")

    def test_unbounded_requires_strict_improvement(self):
        for gain in (0, -1):
            with self.subTest(gain=gain):
                self.assert_rejected_by(document([1], [], unbounded([0], [gain])), "strict_improvement")


class SchemaTests(unittest.TestCase):
    def base(self):
        return document([1], [row([1], 1)], optimal([1], [1]))

    def assert_invalid(self, candidate, code=None):
        result = verifier.verify(candidate)
        self.assertEqual(result["status"], "invalid")
        self.assertFalse(result["accepted"])
        if code is not None:
            self.assertEqual(result["diagnostics"][0]["code"], code)

    def test_floats_bools_and_malformed_rationals(self):
        values = (1.0, True, False, None, {}, [], "1.0", "1e0", " 1", "1 ", "1/0",
                  "1/-2", "1/+2", "1/02", "1//2", "", "NaN", "Infinity")
        for value in values:
            with self.subTest(value=value):
                candidate = self.base()
                candidate["problem"]["objective"]["coefficients"] = [value]
                self.assert_invalid(candidate, "rational")

    def test_integer_and_fraction_strings_accepted(self):
        for value in (1, "1", "+1", "01", "2/2", "-0", "0/3"):
            with self.subTest(value=value):
                candidate = document([0], [row([1], value)], optimal([0], [0]))
                self.assertEqual(verifier.verify(candidate)["status"], "accepted")

    def test_all_rational_positions_checked(self):
        mutations = (
            lambda d: d["problem"]["objective"].update(coefficients=[True]),
            lambda d: d["problem"]["constraints"][0].update(coefficients=[True]),
            lambda d: d["problem"]["constraints"][0].update(rhs=True),
            lambda d: d["certificate"].update(point=[True]),
            lambda d: d["certificate"].update(inequality_multipliers=[True]),
        )
        for mutate in mutations:
            candidate = self.base()
            mutate(candidate)
            self.assert_invalid(candidate, "rational")
        equality = document([1], [row([1], 1, "=")], optimal([1], [], [True]))
        self.assert_invalid(equality, "rational")
        self.assert_invalid(document([1], [], unbounded([0], [True])), "rational")

    def test_unknown_fields_at_every_object(self):
        for location in ((), ("problem",), ("problem", "objective"),
                         ("problem", "constraints", 0), ("certificate",)):
            candidate = self.base()
            target = candidate
            for entry in location:
                target = target[entry]
            target["unexpected"] = 0
            self.assert_invalid(candidate, "unknown_field")

    def test_missing_fields(self):
        for field in ("version", "problem", "certificate"):
            candidate = self.base()
            del candidate[field]
            self.assert_invalid(candidate, "missing_field")

    def test_versions_senses_and_kinds(self):
        for version in (True, 1.0, "1", 0, 2):
            candidate = self.base()
            candidate["version"] = version
            self.assert_invalid(candidate, "version")
        for sense in ("MAX", "minimize", "=", None, [], True):
            candidate = self.base()
            candidate["problem"]["objective"]["sense"] = sense
            self.assert_invalid(candidate, "sense")
        for sense in ("<", ">", "==", None, [], True):
            candidate = self.base()
            candidate["problem"]["constraints"][0]["sense"] = sense
            self.assert_invalid(candidate, "sense")
        for kind in ("optimum", None, [], True):
            candidate = self.base()
            candidate["certificate"]["kind"] = kind
            self.assert_invalid(candidate, "kind")

    def test_all_vector_dimensions(self):
        changes = (
            lambda d: d["problem"]["constraints"][0].update(coefficients=[]),
            lambda d: d["certificate"].update(point=[]),
            lambda d: d["certificate"].update(inequality_multipliers=[]),
            lambda d: d["certificate"].update(equality_multipliers=[0]),
        )
        for mutate in changes:
            candidate = self.base()
            mutate(candidate)
            self.assert_invalid(candidate, "dimension")
        self.assert_invalid(document([1], [], unbounded([], [1])), "dimension")
        self.assert_invalid(document([1], [], unbounded([0], [])), "dimension")

    def test_arrays_and_objects_required(self):
        self.assert_invalid([], "object")
        self.assert_invalid(None, "object")
        candidate = self.base()
        candidate["problem"]["constraints"] = {}
        self.assert_invalid(candidate, "array")
        candidate = self.base()
        candidate["certificate"]["point"] = "1"
        self.assert_invalid(candidate, "array")

    def test_duplicate_keys_at_nested_and_root_positions(self):
        source = json.dumps(self.base())
        for duplicate in (source.replace('"version": 1', '"version": 1, "version": 1'),
                          source.replace('"sense": "max"', '"sense": "max", "sense": "min"')):
            result = verifier.verify_json(duplicate)
            self.assertEqual(result["status"], "invalid")
            self.assertEqual(result["diagnostics"][0]["code"], "duplicate_key")

    def test_nonstandard_json_constants_and_malformed_json(self):
        for source in ("NaN", "Infinity", "-Infinity", "{", "", '{"version": 1,}'):
            with self.subTest(source=source):
                self.assertEqual(verifier.verify_json(source)["status"], "invalid")

    def test_numeric_exponent_is_a_forbidden_float(self):
        source = json.dumps(self.base()).replace('"coefficients": [1]', '"coefficients": [1e0]', 1)
        result = verifier.verify_json(source)
        self.assertEqual(result["status"], "invalid")
        self.assertEqual(result["diagnostics"][0]["code"], "rational")

    def test_deeply_nested_json_is_invalid_without_traceback(self):
        result = verifier.verify_json("[" * 11000 + "]" * 11000)
        self.assertEqual(result["status"], "invalid")
        self.assertEqual(result["diagnostics"][0]["code"], "json")

    def test_verification_does_not_mutate_input(self):
        candidate = self.base()
        snapshot = copy.deepcopy(candidate)
        verifier.verify(candidate)
        self.assertEqual(candidate, snapshot)


class CommandLineTests(unittest.TestCase):
    def run_cli(self, argument, source=None):
        return subprocess.run([sys.executable, str(ROOT / "verifier.py"), str(argument)],
                              input=source, text=True, capture_output=True, check=False)

    def test_exit_codes_and_deterministic_output(self):
        examples = (("optimal_mixed_redundant", 0), ("rejected_negative_multiplier", 1),
                    ("invalid_duplicate_key", 2))
        for name, exit_code in examples:
            with self.subTest(name=name):
                first = self.run_cli(ROOT / "examples" / (name + ".json"))
                second = self.run_cli(ROOT / "examples" / (name + ".json"))
                self.assertEqual(first.returncode, exit_code)
                self.assertEqual(first.stdout, second.stdout)
                self.assertEqual(first.stderr, "")
                self.assertIn("status", json.loads(first.stdout))

    def test_stdin(self):
        source = (ROOT / "examples/unbounded_max_no_rows.json").read_text()
        result = self.run_cli("-", source)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(json.loads(result.stdout)["accepted"])

    def test_missing_file(self):
        result = self.run_cli(ROOT / "examples/does-not-exist.json")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stdout)["diagnostics"][0]["code"], "io")


if __name__ == "__main__":
    unittest.main()
