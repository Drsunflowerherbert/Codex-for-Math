"""Certificate search tests: checked successes and honest bounded unknowns."""

from __future__ import annotations

import copy
from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import finder
import verifier


def problem(objective, rows, sense="max"):
    return {"version": 1, "problem": {"objective": {"sense": sense, "coefficients": objective},
                                     "constraints": rows}}


def row(coefficients, rhs, sense="<="):
    return {"coefficients": coefficients, "rhs": rhs, "sense": sense}


class RationalSystemTests(unittest.TestCase):
    def test_rational_solution_checked_in_original_equations(self):
        matrix = [[Fraction(2), Fraction(3)], [Fraction(1), Fraction(-1)]]
        solution = finder.solve_linear_system(matrix, [Fraction(7), Fraction(-1)], 2)
        self.assertEqual(solution, (Fraction(4, 5), Fraction(9, 5)))
        self.assertEqual(2 * solution[0] + 3 * solution[1], 7)
        self.assertEqual(solution[0] - solution[1], -1)

    def test_redundant_consistent_and_inconsistent_equations(self):
        solution = finder.solve_linear_system([[1, 1], [2, 2]], [1, 2], 2)
        self.assertIsNotNone(solution)
        self.assertEqual(solution[0] + solution[1], 1)
        self.assertEqual(2 * solution[0] + 2 * solution[1], 2)
        self.assertIsNone(finder.solve_linear_system([[1, 1], [2, 2]], [1, 3], 2))

    def test_zero_variable_system(self):
        self.assertEqual(finder.solve_linear_system([[]], [0], 0), ())
        self.assertIsNone(finder.solve_linear_system([[]], [1], 0))

    def test_empty_equations_have_zero_particular_solution(self):
        self.assertEqual(finder.solve_linear_system([], [], 2), (0, 0))

    def test_internal_dimension_guard(self):
        with self.assertRaises(ValueError):
            finder.solve_linear_system([[1]], [], 1)
        with self.assertRaises(ValueError):
            finder.solve_linear_system([[1]], [1], 2)


class FoundCertificateTests(unittest.TestCase):
    def assert_found(self, document, kind):
        result = finder.find(document)
        self.assertEqual(result["status"], "found")
        self.assertTrue(result["incomplete"])
        self.assertEqual(result["certificate_kind"], kind)
        certificate_document = result["certificate_document"]
        self.assertEqual(certificate_document["problem"], document["problem"])
        self.assertEqual(result["verification"], verifier.verify(certificate_document))
        self.assertTrue(result["verification"]["accepted"])
        self.assertGreaterEqual(result["search_counts"]["certificates_checked"], 1)
        return result

    def test_find_from_all_nine_accepted_example_problems(self):
        names = (
            "optimal_mixed_redundant", "optimal_min_fraction_equality",
            "optimal_zero_variables", "optimal_constant_no_rows",
            "infeasible_mixed", "infeasible_equalities", "infeasible_zero_variables",
            "unbounded_min_lower_dimensional", "unbounded_max_no_rows",
        )
        for name in names:
            with self.subTest(name=name):
                original = json.loads((ROOT / "examples" / (name + ".json")).read_text())
                document = {"version": original["version"], "problem": original["problem"]}
                self.assert_found(document, original["certificate"]["kind"])

    def test_mixed_lower_dimensional_optimum_hand_checked(self):
        document = problem([3, 2], [row([1, 1], 4), row([2, 2], 8),
                                   row([1, 0], 0, ">="), row([0, 1], 0, ">="),
                                   row([1, -1], 0, "=")])
        result = self.assert_found(document, "optimal")
        point = tuple(Fraction(x) for x in result["certificate_document"]["certificate"]["point"])
        self.assertEqual(point, (2, 2))
        self.assertEqual(3 * point[0] + 2 * point[1], 10)

    def test_negative_equality_multiplier_for_minimization(self):
        result = self.assert_found(problem(["3/2"], [row([3], 1, "=")], "min"), "optimal")
        certificate = result["certificate_document"]["certificate"]
        self.assertEqual(Fraction(certificate["point"][0]), Fraction(1, 3))
        self.assertEqual(Fraction(certificate["equality_multipliers"][0]), Fraction(-1, 2))
        self.assertEqual(result["verification"]["certified_objective_value"], "1/2")

    def test_infeasible_equalities_without_nonnegative_restriction(self):
        result = self.assert_found(problem([0], [row([1], 0, "="), row([2], 1, "=")]), "infeasible")
        values = [Fraction(value) for value in result["certificate_document"]["certificate"]["equality_multipliers"]]
        self.assertEqual(values[0] + 2 * values[1], 0)
        self.assertEqual(values[1], -1)

    def test_unbounded_free_variable_hand_checked(self):
        result = self.assert_found(problem([1], []), "unbounded")
        certificate = result["certificate_document"]["certificate"]
        base = Fraction(certificate["base_point"][0])
        direction = Fraction(certificate["direction"][0])
        self.assertGreater(direction, 0)
        self.assertGreater(base + 1000 * direction, base)

    def test_three_variable_optimum(self):
        result = self.assert_found(problem([1, 2, 3], [row([1, 0, 0], 1),
                                  row([0, 1, 0], 2), row([0, 0, 1], 3)]), "optimal")
        self.assertEqual(result["verification"]["certified_objective_value"], "14")

    def test_zero_objective_unbounded_feasible_set_is_optimal(self):
        self.assert_found(problem([0, 0], []), "optimal")

    def test_search_can_replace_an_invalid_supplied_example_witness(self):
        cases = {"rejected_negative_multiplier": "unbounded", "rejected_bad_combination": "optimal",
                 "rejected_infeasible_nonstrict": "optimal", "rejected_unbounded_bad_base": "unbounded",
                 "rejected_unbounded_bad_direction": "optimal", "rejected_unbounded_zero_gain": "optimal"}
        for name, kind in cases.items():
            with self.subTest(name=name):
                source = json.loads((ROOT / "examples" / (name + ".json")).read_text())
                self.assert_found({"version": 1, "problem": source["problem"]}, kind)

    def test_deterministic_and_input_preserving(self):
        document = problem([1, 1], [row([1, 0], 1), row([0, 1], 1)])
        snapshot = copy.deepcopy(document)
        self.assertEqual(finder.find(document), finder.find(document))
        self.assertEqual(document, snapshot)

    def test_output_is_never_found_if_verifier_does_not_accept(self):
        with patch.object(verifier, "verify", return_value={"accepted": False}):
            result = finder.find(problem([0], []))
        self.assertEqual(result["status"], "unknown")
        self.assertNotIn("certificate_document", result)


class UnknownAndInvalidTests(unittest.TestCase):
    def assert_unknown(self, document, reason):
        result = finder.find(document)
        self.assertEqual(result["status"], "unknown")
        self.assertTrue(result["incomplete"])
        self.assertEqual(result["reason"], reason)
        self.assertNotIn("certificate_document", result)
        self.assertNotIn("certificate_kind", result)
        self.assertNotIn("verification", result)
        return result

    def test_known_unbounded_ray_outside_grid_returns_unknown(self):
        # x=100y allows (100t,t), t>=0, with objective y=t, but no
        # positive integer direction in [-2,2]^2 can satisfy this equality.
        document = problem([0, 1], [row([1, -100], 0, "=")])
        known_certificate = {**copy.deepcopy(document), "certificate": {
            "kind": "unbounded", "base_point": [0, 0], "direction": [100, 1]}}
        self.assertTrue(verifier.verify(known_certificate)["accepted"])
        result = self.assert_unknown(document, "no_certificate_in_bounded_search")
        self.assertEqual(result["search_counts"]["direction_candidates"], 25)

    def test_variable_and_row_limits_are_unknown_not_invalid(self):
        self.assert_unknown(problem([1, 0, 0, 0], []), "search_limits_exceeded")
        self.assert_unknown(problem([1], [row([1], 1)] * 9), "search_limits_exceeded")

    def test_full_certificate_envelope_is_not_problem_only_input(self):
        document = problem([1], [])
        document["certificate"] = {"kind": "unbounded", "base_point": [0], "direction": [1]}
        result = finder.find(document)
        self.assertEqual(result["status"], "invalid")
        self.assertEqual(result["diagnostics"][0]["code"], "unknown_field")

    def test_verifier_schema_validation_is_retained(self):
        cases = (problem([1.0], []), problem([True], []), problem(["1/0"], []),
                 problem([1], [row([], 1)]), problem([1], [row([1], 1, "<")]),
                 {"version": True, "problem": {"objective": {"sense": "max", "coefficients": []}, "constraints": []}})
        for document in cases:
            with self.subTest(document=document):
                result = finder.find(document)
                self.assertEqual(result["status"], "invalid")
                self.assertTrue(result["incomplete"])

    def test_unknown_nested_fields_rejected(self):
        document = problem([1], [])
        document["problem"]["objective"]["constant"] = 0
        result = finder.find(document)
        self.assertEqual(result["status"], "invalid")
        self.assertEqual(result["diagnostics"][0]["code"], "unknown_field")

    def test_computed_rational_format_limit_is_unknown(self):
        for error in (ValueError("integer output limit"),
                      verifier.SchemaError("resource_limit", "computed", "computed rational too large")):
            with self.subTest(error=type(error).__name__):
                with patch.object(verifier, "fraction_string", side_effect=error):
                    result = finder.find(problem([1], [row([1], 1)]))
                self.assertEqual(result["status"], "unknown")
                self.assertEqual(result["reason"], "search_arithmetic_limit")
                self.assertTrue(result["incomplete"])
                self.assertNotIn("certificate_document", result)

    def test_duplicate_keys_and_nonstandard_constants_rejected(self):
        for source in ('{"version":1,"version":1,"problem":{}}', "NaN", "Infinity", "{"):
            self.assertEqual(finder.find_json(source)["status"], "invalid")

    def test_deep_json_has_no_parser_traceback(self):
        self.assertEqual(finder.find_json("[" * 11000 + "]" * 11000)["status"], "invalid")


class FinderCLITests(unittest.TestCase):
    def run_cli(self, document):
        return subprocess.run([sys.executable, str(ROOT / "finder.py"), "-"],
                              input=json.dumps(document), text=True, capture_output=True, check=False)

    def test_cli_found_unknown_invalid_exit_codes(self):
        cases = ((problem([1], []), "found", 0),
                 (problem([0, 1], [row([1, -100], 0, "=")]), "unknown", 1),
                 (problem([1.0], []), "invalid", 2))
        for document, status, code in cases:
            with self.subTest(status=status):
                result = self.run_cli(document)
                self.assertEqual(result.returncode, code)
                self.assertEqual(result.stderr, "")
                self.assertEqual(json.loads(result.stdout)["status"], status)

    def test_missing_file_is_invalid(self):
        result = subprocess.run([sys.executable, str(ROOT / "finder.py"), str(ROOT / "nonexistent-problem.json")],
                                text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stdout)["diagnostics"][0]["code"], "io")


if __name__ == "__main__":
    unittest.main()
