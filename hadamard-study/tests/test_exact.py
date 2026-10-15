"""Meaningful exact checks against independent formulas and full tiny searches."""

from itertools import combinations_with_replacement, product
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from hadamard import (circulant, is_prime, paley_prime, parse_csv,
                      parse_literal_sign_assignment, parse_signs, sign_bytes, verify, williamson)
from enumerate_williamson import all_quadruples, paf, sequences


def slow_gram(matrix):
    return [[sum(x * y for x, y in zip(a, b)) for b in matrix] for a in matrix]


class ExactTests(unittest.TestCase):
    def test_parser_rejects_invalid_data(self):
        for raw in (b"", b"++\n", b"++\n+0\n", b"++\n\n+-\n", b"+ \n+-\n", b"\xff"):
            with self.subTest(raw=raw), self.assertRaises((ValueError, UnicodeDecodeError)):
                parse_signs(raw)

    def test_csv_parser_treats_input_as_literal_data(self):
        self.assertEqual(parse_csv(b"1,1\n1,-1\n"), [[1, 1], [1, -1]])
        for raw in (b"", b"1,1\n", b"1,0\n1,-1\n", b"=1,1\n1,-1\n", b"1, 1\n1,-1\n"):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                parse_csv(raw)

    def test_assignment_parser_accepts_only_literal_sign_rows(self):
        self.assertEqual(parse_literal_sign_assignment(b"H2060 = [\n [1, 1],\n [1, -1],\n]\n"),
                         [[1, 1], [1, -1]])
        for raw in (b"H2060 = []\n", b"H2060 = [\n [1+0],\n]\n",
                    b"H2060 = [\n [1],\n]\nprint(1)\n", b"H2060 = [\n [True],\n]\n",
                    b"H2060 = [\n [__import__('os')],\n]\n"):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                parse_literal_sign_assignment(raw)

    def test_verifier_detects_shape_entries_and_corruption(self):
        for matrix in ([], [[1, -1]], [[1, 0], [1, -1]], [[True]], [[1, 1], [1, 1]]):
            with self.subTest(matrix=matrix), self.assertRaises(ValueError):
                verify(matrix)
        matrix = paley_prime(11)
        matrix[7][9] *= -1
        with self.assertRaises(ValueError):
            verify(matrix)

    def test_verifier_against_every_two_by_two_sign_matrix(self):
        for flat in product((-1, 1), repeat=4):
            matrix = [list(flat[:2]), list(flat[2:])]
            expected = slow_gram(matrix) == [[2, 0], [0, 2]]
            try:
                verify(matrix)
                actual = True
            except ValueError:
                actual = False
            self.assertEqual(expected, actual)

    def test_paley_against_explicit_gram_and_character_sums(self):
        for p in (3, 7, 11, 19, 23, 31):
            matrix = paley_prime(p)
            gram = slow_gram(matrix)
            self.assertEqual(gram, [[(p + 1) * (i == j) for j in range(p + 1)]
                                    for i in range(p + 1)])
            verify(parse_signs(sign_bytes(matrix)))
            chi = lambda a: 0 if a % p == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
            for d in range(1, p):
                self.assertEqual(sum(chi(x) * chi(x + d) for x in range(p)), -1)
        for p in (1, 5, 9, 15, 27, 35):
            with self.assertRaises(ValueError):
                paley_prime(p)
        self.assertFalse(is_prime(1))

    def test_sequence_enumeration_is_complete_normalized_symmetric(self):
        for m in range(1, 16, 2):
            seqs = list(sequences(m))
            self.assertEqual(len(set(seqs)), 2 ** ((m - 1) // 2))
            for s in seqs:
                self.assertEqual(s[0], 1)
                self.assertEqual(len(s), m)
                self.assertTrue(all(s[j] == s[-j % m] for j in range(m)))
                self.assertEqual(sum(s) % 4, m % 4)

    def test_pair_bucket_search_against_unpruned_full_quadruples(self):
        for m in (1, 3, 5, 7, 9):
            seqs = list(sequences(m))
            expected = set()
            for q in combinations_with_replacement(range(len(seqs)), 4):
                # All lags, independently computed (not the search's half-lag PAF).
                if all(sum(seqs[a][i] * seqs[a][(i + t) % m]
                           for a in q for i in range(m)) == 0 for t in range(1, m)):
                    expected.add(q)
            actual = list(all_quadruples(m))
            self.assertEqual(len(actual), len(set(actual)))
            self.assertEqual(set(actual), expected)
            for q in actual:
                matrix = williamson([seqs[a] for a in q])
                gram = slow_gram(matrix)
                self.assertEqual(gram, [[4 * m * (i == j) for j in range(4 * m)]
                                       for i in range(4 * m)])
                verify(matrix)

    def test_williamson_rejects_nonsymmetric_input(self):
        with self.assertRaises(ValueError):
            williamson([(1, 1, -1)] * 4)
        with self.assertRaises(ValueError):
            williamson([(1,)] * 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
