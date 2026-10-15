#!/usr/bin/env python3
"""Independent, standard-library Hadamard check using integer dot products.

This verifier imports no study code and uses no packed bits or XOR identities.
Input is an ASCII file with one row of '+'/'-' signs per line.  The SHA-256
identifies the original bytes, including line endings.  All distinct row pairs
and all row norms are checked over Python integers.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time


def parse_rows(raw: bytes, order: int) -> list[list[int]]:
    if order < 1:
        raise ValueError("order must be positive")
    try:
        lines = raw.decode("ascii").splitlines()
    except UnicodeDecodeError as error:
        raise ValueError("input is not ASCII") from error
    if len(lines) != order:
        raise ValueError(f"expected {order} rows; found {len(lines)}")
    rows: list[list[int]] = []
    for index, line in enumerate(lines):
        if len(line) != order:
            raise ValueError(f"row {index}: expected {order} signs; found {len(line)}")
        if set(line) - {"+", "-"}:
            raise ValueError(f"row {index}: contains a non-sign character")
        rows.append([1 if sign == "+" else -1 for sign in line])
    return rows


def check_rows(rows: list[list[int]], order: int) -> dict[str, int]:
    """Raise on the first failed condition; count every successful check."""
    if len(rows) != order or any(len(row) != order for row in rows):
        raise ValueError("matrix is not square of the expected order")
    if any(value not in (-1, 1) for row in rows for value in row):
        raise ValueError("matrix contains a value other than -1 or 1")
    diagonal_checks = 0
    pair_checks = 0
    for left_index, left in enumerate(rows):
        norm = sum(value * value for value in left)
        if norm != order:
            raise ValueError(f"row {left_index}: squared norm {norm} != {order}")
        diagonal_checks += 1
        for right_index in range(left_index):
            dot = sum(a * b for a, b in zip(left, rows[right_index]))
            if dot != 0:
                raise ValueError(
                    f"rows {left_index}, {right_index}: integer dot product {dot} != 0"
                )
            pair_checks += 1
    expected_pairs = order * (order - 1) // 2
    if pair_checks != expected_pairs:
        raise RuntimeError("internal check count mismatch")
    return {"row_norm_checks": diagonal_checks, "distinct_row_pair_checks": pair_checks}


def self_test() -> dict[str, str]:
    valid = b"++++\n+-+-\n++--\n+--+\n"
    rows = parse_rows(valid, 4)
    counts = check_rows(rows, 4)
    if counts != {"row_norm_checks": 4, "distinct_row_pair_checks": 6}:
        raise RuntimeError("valid-matrix self-test failed")
    damaged = [row.copy() for row in rows]
    damaged[1][0] *= -1
    try:
        check_rows(damaged, 4)
    except ValueError:
        pass
    else:
        raise RuntimeError("single-sign corruption self-test was accepted")
    for malformed, size in ((b"+++\n", 1), (b"x\n", 1), (b"+\n\n", 1)):
        try:
            parse_rows(malformed, size)
        except ValueError:
            pass
        else:
            raise RuntimeError("malformed-input self-test was accepted")
    return {"valid_4_by_4": "passed", "single_sign_corruption": "rejected", "malformed_inputs": "rejected"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--expected-order", type=int, default=668)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    test_result = self_test()
    raw = args.matrix.read_bytes()
    started = time.perf_counter()
    rows = parse_rows(raw, args.expected_order)
    counts = check_rows(rows, args.expected_order)
    result = {
        "status": "passed",
        "claim": "H H^T = n I_n by explicit integer row dot products",
        "matrix_file": str(args.matrix),
        "matrix_byte_count": len(raw),
        "matrix_sha256": hashlib.sha256(raw).hexdigest(),
        "order": args.expected_order,
        "entries_checked": args.expected_order**2,
        **counts,
        "elapsed_seconds": round(time.perf_counter() - started, 6),
        "self_tests": test_result,
        "implementation": "Python standard library; explicit integer multiplication and summation; no study-code imports",
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
