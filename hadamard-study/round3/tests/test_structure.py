"""Bounded regression tests for the structural search and its exact relaxations.

Run with ``python -m unittest discover -s hadamard-study/round3/tests -v``.
The complete search checks stop at core order 11; larger orders below are
fixed algebra fixtures, not benchmark runs.
"""

import itertools
import json
from pathlib import Path
import sys
import unittest


ROUND3 = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROUND3 / "scripts"))

import partial_singles
import phase_search
import phases
import structure


def rgs_colorings(h, order):
    """Enumerate canonical color names in a specified coordinate order."""
    colors = [-1] * h

    def visit(depth, used):
        if depth == h:
            yield tuple(colors)
            return
        vertex = order[depth]
        for color in range(min(used + 1, 4)):
            colors[vertex] = color
            yield from visit(depth + 1, max(used, color + 1))
        colors[vertex] = -1

    yield from visit(0, 0)


def substituted(algebra, colors, vertices):
    result = algebra.initial
    for vertex in vertices:
        result = algebra.assign(result, vertex, colors[vertex])
    return result


def direct_tuple_paf(m, masks):
    sequences = [partial_singles.sequence_from_mask(m, mask) for mask in masks]
    return tuple(sum(x[j] * x[(j + lag) % m]
                     for x in sequences for j in range(m))
                 for lag in range(m))


class BooleanPhaseTests(unittest.TestCase):
    def test_full_anf_evaluation_matches_graph_signs_exhaustively(self):
        for m in range(1, 10, 2):
            h = m // 2
            graphs = structure.quotient_edges(m)
            algebra = phases.PhaseAlgebra(h, graphs)
            for colors in itertools.product(range(4), repeat=h):
                with self.subTest(m=m, colors=colors):
                    evaluated = tuple((-1) ** algebra.evaluate(p, colors)
                                      for p in algebra.initial)
                    self.assertEqual(evaluated, structure.full_signs(colors, graphs))

    def test_substitution_respects_arbitrary_assigned_coordinate_sets(self):
        for m in range(1, 8, 2):
            h = m // 2
            algebra = phases.PhaseAlgebra(h, structure.quotient_edges(m))
            for colors in itertools.product(range(4), repeat=h):
                expected = tuple(algebra.evaluate(p, colors) for p in algebra.initial)
                for mask in range(1 << h):
                    vertices = tuple(i for i in reversed(range(h)) if mask >> i & 1)
                    residuals = substituted(algebra, colors, vertices)
                    self.assertEqual(tuple(algebra.evaluate(p, colors) for p in residuals),
                                     expected, (m, colors, vertices))
                    assigned_variables = sum(3 << (2 * i) for i in vertices)
                    for p in residuals:
                        for index, support in enumerate(algebra.supports):
                            if p >> index & 1:
                                self.assertFalse(support & assigned_variables)

    def test_shared_residual_with_opposite_constants_cancels(self):
        # Independently recorded fixture: vertices 2 and 6 share the final
        # color's high bit, with opposite constant signs.
        prefix = (0, 1, 1, 1, 0, 1)
        graphs = structure.quotient_edges(15)
        algebra = phases.PhaseAlgebra(7, graphs)
        residuals = substituted(algebra, prefix, range(len(prefix)))
        self.assertGreaterEqual(residuals[1] & ~1, 2)
        self.assertEqual(residuals[1] ^ residuals[5], 1)
        self.assertEqual(phases.sign_of_constant(residuals[1]), 1)
        self.assertEqual(phases.sign_of_constant(residuals[5]), -1)
        for final_color in range(4):
            colors = prefix + (final_color,)
            signs = structure.full_signs(colors, graphs)
            self.assertEqual(signs[1] + signs[5], 0)
            self.assertEqual(tuple((-1) ** algebra.evaluate(p, colors)
                                   for p in residuals), signs)

    def test_grouped_prefix_filters_can_pass_without_any_completion(self):
        prefix = (0, 0, 0, 1)
        colors = prefix + (-1,)
        graphs = structure.quotient_edges(11)
        algebra = phases.PhaseAlgebra(5, graphs)
        residuals = substituted(algebra, prefix, range(4))
        self.assertTrue(phases.grouped_row_possible(
            colors, 4, residuals, structure.row_targets(5)))
        self.assertTrue(phases.grouped_lag_possible(
            colors, 4, residuals, graphs, algebra, expanded=True))
        # Include the noncanonical fourth color: the relaxation is not made
        # sufficient by dropping the restricted-growth requirement.
        for final_color in range(4):
            complete = prefix + (final_color,)
            signs = structure.full_signs(complete, graphs)
            self.assertFalse(structure.full_correlation(complete, signs, graphs))

    def test_repeated_edges_keep_integer_multiplicity_but_cancel_mod_two(self):
        # Synthetic algebra fixture: graph multiplicities are meaningful even
        # though the actual odd cyclic quotient graphs have no parallel edges.
        repeated = (((0, 1), (0, 1)),)
        single = (((0, 1),),)
        algebra = phases.PhaseAlgebra(2, repeated)
        self.assertEqual(algebra.initial, (1,))  # 1 + delta + delta = 1.
        self.assertEqual(structure.full_signs((0, 0), repeated), (-1,))
        self.assertEqual(structure.full_signs((0, 0), single), (1,))
        # Here a single edge gives 1+1+2*(-1)=0; two give -2 instead.
        colors, signs, constants = (0, 0), (1, -1), (0, 1)
        self.assertTrue(structure.full_correlation(colors, signs, single))
        self.assertFalse(structure.full_correlation(colors, signs, repeated))
        for expanded in (False, True):
            self.assertTrue(phases.grouped_lag_possible(
                colors, 2, constants, single, algebra, expanded=expanded))
            self.assertFalse(phases.grouped_lag_possible(
                colors, 2, constants, repeated, algebra, expanded=expanded))


class CanonicalCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        evidence = json.loads((ROUND3 / "reviews" / "structure-independent.json").read_text())
        if evidence["status"] != "passed":
            raise AssertionError("independent structural baseline did not pass")
        cls.baseline = {r["core_order"]: r for r in evidence["results"]}

    def test_rgs_has_one_representative_per_row_multiset_in_both_orders(self):
        for m in range(1, 10, 2):
            h = m // 2
            graphs = structure.quotient_edges(m)
            algebra = phases.PhaseAlgebra(h, graphs)
            all_multisets = {
                structure.masks_from_structure(colors, structure.full_signs(colors, graphs))
                for colors in itertools.product(range(4), repeat=h)
            }
            for strategy in ("natural", "collisions"):
                order = phase_search.coordinate_order(algebra, strategy)
                self.assertEqual(sorted(order), list(range(h)))
                colorings = list(rgs_colorings(h, order))
                self.assertEqual(len(colorings), structure.rgs_completions(h, 0))
                multisets = [structure.masks_from_structure(
                    colors, structure.full_signs(colors, graphs)) for colors in colorings]
                self.assertEqual(len(multisets), len(set(multisets)))
                self.assertEqual(set(multisets), all_multisets, (m, strategy))

    def test_search_outputs_match_preserved_independent_baseline(self):
        for m in range(1, 12, 2):
            expected = self.baseline[m]["solutions"]
            expected_leaves = self.baseline[m]["unpruned_RGS_colorings"]
            for mode in ("leaf", "all"):
                with self.subTest(m=m, method="structure", mode=mode):
                    result = structure.search(m, mode)
                    self.assertEqual(result["solutions"], expected)
                    self.assertEqual(result["counts"]["raw_RGS_color_leaves"], expected_leaves)
            for strategy in ("natural", "collisions"):
                for mode in ("row", "relations", "expanded"):
                    with self.subTest(m=m, method="phases", mode=mode, order=strategy):
                        result = phase_search.search(m, mode, strategy)
                        self.assertEqual(result["solutions"], expected)
                        counts = result["counts"]
                        self.assertEqual(counts["raw_RGS_color_leaves"], expected_leaves)
                        self.assertEqual(counts["complete_color_assignments_entered"]
                                         + counts["structural_leaves_skipped_before_completion"],
                                         expected_leaves)

    def test_valid_solution_survives_nonprefix_phase_assignment(self):
        masks = (3, 8, 9, 13)
        colors, signs = [], []
        for j in range(4):
            column = tuple(1 - 2 * ((mask >> j) & 1) for mask in masks)
            sign = 1 if column.count(-1) == 1 else -1
            colors.append(column.index(-sign))
            signs.append(sign)
        graphs = structure.quotient_edges(9)
        self.assertEqual(tuple(signs), structure.full_signs(colors, graphs))
        algebra = phases.PhaseAlgebra(4, graphs)
        for assigned in ((3,), (3, 1), (2, 0, 3)):
            partial = [color if i in assigned else -1 for i, color in enumerate(colors)]
            residuals = substituted(algebra, colors, assigned)
            self.assertTrue(phases.grouped_row_possible(
                partial, len(assigned), residuals, structure.row_targets(4)))
            for expanded in (False, True):
                self.assertTrue(phases.grouped_lag_possible(
                    partial, len(assigned), residuals, graphs, algebra, expanded=expanded))


class CancellationBoundTests(unittest.TestCase):
    def test_zero_fill_would_reject_an_actual_williamson_member(self):
        m, mask, masks = 9, 8, (3, 8, 9, 13)
        self.assertEqual(direct_tuple_paf(m, masks), (36,) + (0,) * 8)
        vector = (1,) * m
        probe = partial_singles.make_probe(m, "constant", "constant", vector)
        # First three pairs are positive; the last pair is still unknown.
        partial = tuple(vector[j] + sum(probe.coefficients[i][j] for i in range(3))
                        for j in range(m))
        self.assertEqual(partial, (7,) * m)
        self.assertEqual(sum(x * x for x in partial), 441)
        self.assertEqual(probe.limit, 324)
        completed = partial_singles.sequence_from_mask(m, mask)
        energy = partial_singles.direct_probe_energy(completed, vector)
        lower = partial_singles.energy_lower_bound(partial, probe.suffix_radii[3])
        self.assertEqual(energy, 225)
        self.assertEqual(lower, 225)
        self.assertLessEqual(lower, energy)
        self.assertLessEqual(lower, probe.limit)


class DecisionCacheTests(unittest.TestCase):
    def setUp(self):
        phases.clear_decision_caches()

    def test_signed_sum_decisions_equal_direct_integer_sumsets(self):
        coefficient_cases = ((), (1,), (2, 2), (1, -2, 3), (0, -3, 3), (-2, 4))
        domain_cases = ((), ((0, 2),), ((-2, 0, 2),), ((-1, 1), (0, 2)))
        for coefficients in coefficient_cases:
            for domains in domain_cases:
                reachable = {0}
                for domain in tuple((-c, c) for c in coefficients) + domains:
                    reachable = {x + value for x in reachable for value in domain}
                for constant in range(-8, 9):
                    self.assertEqual(phases.signed_sum_possible(constant, coefficients, domains),
                                     -constant in reachable, (constant, coefficients, domains))

    def test_signed_sum_cache_ignores_sign_order_and_domain_duplicates(self):
        first = phases.signed_sum_possible(2, (2, -4, 0), ((2, 0, 2), (-1, 1)))
        before = phases.decision_cache_statistics()["lag"]
        second = phases.signed_sum_possible(2, (4, -2), ((1, -1), (0, 2)))
        after = phases.decision_cache_statistics()["lag"]
        self.assertEqual(first, second)
        self.assertEqual(after["misses"], before["misses"])
        self.assertEqual(after["hits"], before["hits"] + 1)

    def test_row_cache_ignores_phase_names_and_whole_group_signs(self):
        colors = (0, 1, 0, 2, -1)
        targets = structure.row_targets(5)
        # A cross-color phase, a scalar phase, and one constant sign.
        first = phases.grouped_row_possible(colors, 4, (2, 3, 4, 0, 0), targets)
        before = phases.decision_cache_statistics()["row"]
        # Rename both residual phases and reverse their overall coefficients.
        second = phases.grouped_row_possible(colors, 4, (9, 8, 17, 0, 0), targets)
        after = phases.decision_cache_statistics()["row"]
        vectors = [(a + b, -a, 1, 0)
                   for a, b in itertools.product((-1, 1), repeat=2)]
        expected = any(sum(abs(u[c] - v[c]) for c in range(4)) <= 1
                       for u in targets for v in vectors)
        self.assertEqual(first, expected)
        self.assertEqual(second, expected)
        self.assertEqual(after["misses"], before["misses"])
        self.assertEqual(after["hits"], before["hits"] + 1)


if __name__ == "__main__":
    unittest.main()
