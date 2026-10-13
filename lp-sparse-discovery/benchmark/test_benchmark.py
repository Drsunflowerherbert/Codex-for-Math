"""Ordinary exact-arithmetic regression checks, not formal verification."""

from fractions import Fraction as Q
from itertools import combinations
import json
from pathlib import Path
import unittest

import benchmark as bench


class ExactBenchmarkTests(unittest.TestCase):
    def setUp(self):
        self.fixtures = {fixture.name: fixture for fixture in bench.fixtures()}

    def test_unique_rational_solution(self):
        self.assertEqual(bench.independent_solution(
            (bench.vector(["2/3", "1/2"]), bench.vector(["-3/5", -1])),
            bench.vector([0, -1])), bench.vector(["18/11", "20/11"]))

    def test_dependent_columns_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "dependent"):
            bench.independent_solution((bench.vector([1, 2]), bench.vector([2, 4])),
                                       bench.vector([3, 6]))

    def test_independent_but_inconsistent_system(self):
        self.assertIsNone(bench.independent_solution((bench.vector([1, 0]),),
                                                    bench.vector([1, 1])))

    def test_empty_support(self):
        self.assertEqual(bench.independent_solution((), bench.vector([0, 0])), ())
        self.assertIsNone(bench.independent_solution((), bench.vector([0, 1])))

    def test_all_certificates_rechecked_by_direct_coordinate_sums(self):
        # Recompute identities from serialized data, without search's dot helper.
        report = bench.report()
        for entry in report["fixtures"]:
            fixture = entry["fixture"]
            normals = [[Q(value) for value in row] for row in fixture["normals"]]
            budgets = [Q(value) for value in fixture["budgets"]]
            for run in entry["runs"]:
                certificate = run["first_certificate"]
                weights = [Q(value) for value in certificate["inequality_weights"]]
                self.assertTrue(all(weight >= 0 for weight in weights))
                combined = [sum((weights[i] * normals[i][j] for i in range(len(weights))), Q(0))
                            for j in range(fixture["dimension"])]
                cost = sum((weights[i] * budgets[i] for i in range(len(weights))), Q(0))
                if fixture["kind"] == "bound":
                    self.assertEqual(combined, list(map(Q, fixture["objective"])))
                    self.assertLessEqual(cost, Q(fixture["bound"]))
                    if run["strategy"] == "augmented":
                        self.assertEqual(cost + Q(certificate["vertical_residual_weight"]),
                                         Q(fixture["bound"]))
                else:
                    self.assertEqual(combined, [Q(0)] * fixture["dimension"])
                    self.assertEqual(cost, Q(-1))

    def test_sharp_examples_have_expected_positive_weights(self):
        bound = bench.search(self.fixtures["sharp-normal-support-k"], "direct", True)
        self.assertEqual(bound["first_certificate"]["inequality_weights"], ["1"] * 3)
        contradiction = bench.search(self.fixtures["sharp-contradiction-support-k-plus-one"],
                                     "augmented", True)
        self.assertEqual(contradiction["first_certificate"]["inequality_weights"], ["1"] * 4)

    def test_rational_contradiction_weights(self):
        result = bench.search(self.fixtures["rational-contradiction"], "augmented", True)
        self.assertEqual(result["first_certificate"]["inequality_weights"], ["18/11", "20/11"])

    def test_cheap_row_survives_budget_filter(self):
        fixture = self.fixtures["cheaper-redundant-row"]
        self.assertFalse(bench.verify_weights(fixture, bench.vector([1, 0, 0])))
        result = bench.search(fixture, "direct", True)
        self.assertEqual(result["first_certificate"]["inequality_weights"], ["0", "1/2", "0"])
        self.assertEqual(result["counts"]["budget_rejections"], 1)

    def test_affine_reconstruction_in_original_space(self):
        result = bench.search(self.fixtures["rational-equality-reduction"], "direct", True)
        original = result["first_certificate"]["original_identity"]
        self.assertEqual(original["equality_weights"], ["1", "1"])
        self.assertEqual(original["original_combination_rhs"], "11/3")
        contradiction = bench.search(self.fixtures["zero-projected-row-contradiction"],
                                     "augmented", True)
        original = contradiction["first_certificate"]["original_identity"]
        self.assertEqual(original["equality_weights"], ["-1"])
        self.assertEqual(original["original_combination_rhs"], "-1")

    def test_zero_objective_requires_no_direct_rows(self):
        direct = bench.search(self.fixtures["zero-objective-positive-budget"], "direct", True)
        augmented = bench.search(self.fixtures["zero-objective-positive-budget"], "augmented", True)
        self.assertEqual(direct["first_certificate"]["enumerated_indices"], [])
        self.assertEqual(augmented["first_certificate"]["vertical_residual_weight"], "1")

    def test_row_order_changes_first_success_but_not_full_counts(self):
        late = bench.search(self.fixtures["late-singleton-row-order"], "direct", False)
        early = bench.search(self.fixtures["early-singleton-row-order"], "direct", False)
        self.assertEqual(late["first_certificate"]["first_success_subsets_attempted"], 8)
        self.assertEqual(early["first_certificate"]["first_success_subsets_attempted"], 2)
        self.assertEqual(late["counts"], early["counts"])
        self.assertEqual(late["counts"]["subsets_attempted"], 64)

    def test_exhaustive_counts_match_combinatorial_budget(self):
        for entry in bench.report()["fixtures"]:
            for run in entry["runs"]:
                if run["mode"] != "exhaustive":
                    continue
                n = run["column_count"]
                r = run["column_rank"]
                expected = sum(sum(1 for _ in combinations(range(n), size))
                               for size in range(r + 1))
                self.assertEqual(run["counts"]["subsets_attempted"], expected)
                self.assertEqual(run["counts"]["independent_solves"] +
                                 run["counts"]["dependent_subsets_rejected"], expected)

    def test_bad_certificate_identity_and_sign_are_rejected(self):
        fixture = self.fixtures["sharp-normal-support-k"]
        self.assertFalse(bench.verify_weights(fixture, bench.vector([1, 1, 0])))
        self.assertFalse(bench.verify_weights(fixture, bench.vector([1, 1, -1])))
        self.assertFalse(bench.verify_weights(fixture, bench.vector([1])))

    def test_committed_report_is_reproducible(self):
        stored = json.loads(Path(__file__).with_name("results.json").read_text())
        self.assertEqual(stored, bench.report())


if __name__ == "__main__":
    unittest.main()
