"""Adversarial, exact tests of the second-round pruning conditions."""

from itertools import combinations_with_replacement, product
import json
from pathlib import Path
import sys
import unittest

STUDY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(STUDY / "round2/scripts"))
from search import (Prepared, order3_energy, pair_search, probe_score,
                    product_search, square_sums, triangular_probes)
from enumerate_williamson import all_quadruples, paf, sequences


class ReductionTests(unittest.TestCase):
    def test_complete_solution_sets_against_unfiltered_baseline(self):
        for m in range(1, 16, 2):
            expected = sorted(all_quadruples(m))
            p = Prepared(m, filtered=True)
            for product_key in (False, True):
                actual, _ = pair_search(p, product_key=product_key)
                self.assertEqual(actual, expected, (m, product_key))
            self.assertEqual(product_search(p)[0], expected, m)

    def test_pair_baseline_matches_first_edition(self):
        for m in (1, 9, 15):
            expected = sorted(all_quadruples(m))
            self.assertEqual(pair_search(Prepared(m, filtered=False))[0], expected)

    def test_each_filter_ablation_preserves_full_solution_sets(self):
        for m in (1, 3, 9, 15):
            expected = sorted(all_quadruples(m))
            for filters in ("row", "row-order3", "all"):
                p = Prepared(m, filtered=True, filters=filters)
                self.assertEqual(pair_search(p)[0], expected, (m, filters))

    def test_every_true_single_and_pair_passes_every_filter(self):
        for m in range(1, 16, 2):
            p = Prepared(m, filtered=True)
            for q in all_quadruples(m):
                self.assertEqual(q[0] ^ q[1] ^ q[2] ^ q[3], p.full_mask)
                for a in q:
                    self.assertIn(a, p.mask_set)
                for a, b in combinations_with_replacement(q, 2):
                    # Only pairs of positions actually present in the tuple:
                    # combinations over values permits an invalid extra copy.
                    if a == b and q.count(a) < 2:
                        continue
                    self.assertEqual(p.pair_rejection(a, b), 0, (m, q, a, b))

    def test_integer_probe_formula_against_direct_matrix_vector_energy(self):
        for m in range(1, 16, 2):
            for s in sequences(m):
                profile = paf(s)
                for _, v, norm, corr in triangular_probes(m):
                    direct = sum(sum(s[(j - i) % m] * v[j] for j in range(m)) ** 2
                                 for i in range(m))
                    self.assertEqual(probe_score(profile, m, norm, corr), direct)

    def test_exact_order3_energy_and_equality_survives(self):
        for m in (3, 9, 15):
            for s in sequences(m):
                residue = [sum(s[r::3]) for r in range(3)]
                self.assertEqual(residue[1], residue[2])
                expected = (sum(x * x for x in residue)
                            - residue[0] * residue[1] - residue[0] * residue[2]
                            - residue[1] * residue[2])
                self.assertEqual(order3_energy(s), expected)
        p = Prepared(9, filtered=True)
        q = (7, 11, 13, 14)
        self.assertIn(q, pair_search(p)[0])
        self.assertEqual(p.e3[11], 36)
        self.assertEqual(p.pair_rejection(7, 11), 0)
        f3 = next(i for i, probe in enumerate(p.probes) if probe[0] == 3)
        self.assertEqual(p.energies[11][f3], p.limits[f3])
        self.assertEqual(p.energies[7][f3], 0)

    def test_squares_allow_repetition_and_negative_normalized_row_sums(self):
        for m in range(1, 16, 2):
            two, three = square_sums(m)
            w = [x * x for x in range(1, m + 1, 2)]
            self.assertEqual(two, {sum(t) for t in product(w, repeat=2) if sum(t) <= 4 * m})
            self.assertEqual(three, {sum(t) for t in product(w, repeat=3) if sum(t) <= 4 * m})
        p = Prepared(3, filtered=True)
        self.assertEqual(sum(p.seqs[1]), -1)
        self.assertIn((0, 1, 1, 1), product_search(p)[0])

    def test_product_does_not_improve_full_correlation_join_count(self):
        for m in (3, 9, 15):
            p = Prepared(m, filtered=True)
            plain, a = pair_search(p)
            augmented, b = pair_search(p, product_key=True)
            self.assertEqual(plain, augmented)
            self.assertEqual(a["joined_pair_combinations_before_sorted_order_test"],
                             b["joined_pair_combinations_before_sorted_order_test"])

    def test_product_and_row_sum_are_not_sufficient(self):
        p = Prepared(7, filtered=False)
        found = False
        for a, b, c in combinations_with_replacement(p.masks, 3):
            d = p.full_mask ^ a ^ b ^ c
            if d >= c and sum(p.squares[i] for i in (a, b, c, d)) == 28:
                if any(sum(p.profiles[i][t] for i in (a, b, c, d)) for t in range(3)):
                    found = True
                    break
        self.assertTrue(found)


if __name__ == "__main__":
    unittest.main(verbosity=2)
