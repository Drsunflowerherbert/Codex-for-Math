"""Independently authored exact Hadamard tools; Python standard library only.

No external code is imported. Sign matrices are lists of lists of integer +/-1.
The verifier checks every unordered pair of rows using Hamming distance.
"""

import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path


def parse_signs(raw):
    """Parse strict ASCII, one nonempty +/- row per line; final LF optional."""
    text = raw.decode("ascii")
    lines = text.splitlines()
    if not lines or any(not row or set(row) - {"+", "-"} for row in lines):
        raise ValueError("expected nonempty ASCII +/- rows")
    n = len(lines)
    if any(len(row) != n for row in lines):
        raise ValueError("matrix must be square")
    return [[1 if c == "+" else -1 for c in row] for row in lines]


def sign_bytes(matrix):
    return ("\n".join("".join("+" if x == 1 else "-" for x in row)
                      for row in matrix) + "\n").encode("ascii")


def parse_csv(raw):
    """Parse numeric +/-1 CSV as data, never expressions or executable input."""
    rows = list(csv.reader(io.StringIO(raw.decode("ascii"))))
    if not rows or any(not row or any(x not in ("1", "-1") for x in row) for row in rows):
        raise ValueError("expected nonempty CSV rows of literal 1 or -1")
    if any(len(row) != len(rows) for row in rows):
        raise ValueError("matrix must be square")
    return [[int(x) for x in row] for row in rows]


def parse_literal_sign_assignment(raw, name="H2060"):
    """Read the published row-per-line literal data; do not execute/import it.

    This intentionally accepts a tiny grammar: exact assignment header, numeric
    rows, closing bracket. No general Python expression parser is involved.
    """
    lines = raw.decode("ascii").splitlines()
    if len(lines) < 3 or lines[0] != name + " = [" or lines[-1] != "]":
        raise ValueError("invalid literal data container")
    matrix = []
    for line in lines[1:-1]:
        line = line.strip()
        if not line.startswith("[") or not line.endswith("],"):
            raise ValueError("expected a numeric list row ending with comma")
        values = line[1:-2].split(", ")
        if any(x not in ("1", "-1") for x in values):
            raise ValueError("expected literal integer signs only")
        matrix.append([int(x) for x in values])
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be square")
    return matrix


def verify(matrix):
    n = len(matrix)
    if n < 1 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be nonempty and square")
    if any(type(x) is not int or x not in (-1, 1) for row in matrix for x in row):
        raise ValueError("entries must be integer +/-1")
    packed = [sum((x == 1) << j for j, x in enumerate(row)) for row in matrix]
    checked = 0
    for i in range(n):
        for j in range(i):
            dot = n - 2 * (packed[i] ^ packed[j]).bit_count()
            if dot:
                raise ValueError(f"nonorthogonal rows {j},{i}: dot={dot}")
            checked += 1
    return {"order": n, "entries": n * n, "diagonal_norm_squared": n,
            "unordered_row_pairs_checked": checked,
            "all_off_diagonal_dot_products_zero": True,
            "arithmetic": "exact Python integers, XOR Hamming distances"}


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def paley_prime(p):
    """Paley type I for primes p == 3 mod 4, with explicit fixed convention."""
    if not is_prime(p) or p % 4 != 3:
        raise ValueError("requires a prime congruent to 3 modulo 4")
    squares = {x * x % p for x in range(1, p)}
    def chi(x):
        return 0 if x == 0 else (1 if x in squares else -1)
    return [[1] * (p + 1)] + [
        [-1] + [chi((j - i) % p) + (i == j) for j in range(p)]
        for i in range(p)
    ]


def circulant(sequence):
    m = len(sequence)
    return [[sequence[(j - i) % m] for j in range(m)] for i in range(m)]


def williamson(sequences):
    if len(sequences) != 4 or not sequences[0]:
        raise ValueError("four nonempty sequences required")
    m = len(sequences[0])
    if any(len(s) != m or any(type(x) is not int or x not in (-1, 1) for x in s)
           or any(s[i] != s[-i % m] for i in range(m)) for s in sequences):
        raise ValueError("four equally sized symmetric sign sequences required")
    blocks = [circulant(s) for s in sequences]
    # A,B,C,D; -B,A,-D,C; -C,D,A,-B; -D,-C,B,A.
    pattern = [[(0, 1), (1, 1), (2, 1), (3, 1)],
               [(1, -1), (0, 1), (3, -1), (2, 1)],
               [(2, -1), (3, 1), (0, 1), (1, -1)],
               [(3, -1), (2, -1), (1, 1), (0, 1)]]
    return [[sign * value for b, sign in block_row for value in blocks[b][i]]
            for block_row in pattern for i in range(m)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--format", choices=("signs", "csv", "h2060-data"), default="signs")
    parser.add_argument("--expected-sha256")
    args = parser.parse_args()
    raw = args.matrix.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if args.expected_sha256 and digest != args.expected_sha256:
        parser.error("SHA-256 mismatch")
    readers = {"csv": parse_csv, "signs": parse_signs,
               "h2060-data": parse_literal_sign_assignment}
    matrix = readers[args.format](raw)
    if args.format == "h2060-data" and len(matrix) != 2060:
        parser.error("H2060 data must have order 2060")
    result = verify(matrix)
    result.update({"sha256": digest, "bytes": len(raw), "input_format": args.format,
                   "canonical_sign_bytes_sha256": hashlib.sha256(sign_bytes(matrix)).hexdigest()})
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
