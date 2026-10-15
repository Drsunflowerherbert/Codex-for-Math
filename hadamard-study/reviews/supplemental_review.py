#!/usr/bin/env python3
"""Replay the independent Paley, stored-witness, and source-data cross-checks.

The constructions and parsers below do not call the study's constructors or
parsers.  Integer scalar-product checking comes from this reviewer's verifier.
The final solution-set comparison imports only the enumerator being reviewed,
after an independent brute-force result has already been produced.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from independent_check import check_rows


def write_json(path: Path, result: dict) -> None:
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def check_paley(study: Path) -> dict:
    evidence = json.loads((study / "evidence/paley-primes-through-199.json").read_text())
    expected_primes = [p for p in range(3, 200, 4) if all(p % d for d in range(2, p))]
    if [row["prime"] for row in evidence["results"]] != expected_primes:
        raise ValueError("missing, duplicated, or invalid prime parameter")
    results = []
    for recorded in evidence["results"]:
        p = recorded["prime"]

        def chi(value: int) -> int:
            residue = pow(value % p, (p - 1) // 2, p)
            return -1 if residue == p - 1 else residue

        matrix = [[1] * (p + 1)]
        for i in range(p):
            matrix.append([-1] + [1 if i == j else chi(j - i) for j in range(p)])
        checks = check_rows(matrix, p + 1)
        raw = ("\n".join("".join("+" if value == 1 else "-" for value in row)
                         for row in matrix) + "\n").encode("ascii")
        digest = hashlib.sha256(raw).hexdigest()
        if digest != recorded["canonical_sign_bytes_sha256"]:
            raise ValueError(f"Paley matrix digest mismatch at p={p}")
        results.append({"prime": p, "order": p + 1, "canonical_sign_sha256": digest, **checks})
    return {
        "status": "passed",
        "method": "Euler criterion over each prime; explicit integer dot products; comparison of every canonical matrix digest",
        "matrices_checked": len(results),
        "row_pairs_checked": sum(row["distinct_row_pair_checks"] for row in results),
        "results": results,
    }


def check_witnesses(study: Path) -> dict:
    data = json.loads((study / "data/williamson-odd-through-15.json").read_text())
    patterns = (
        ((0, 1), (1, 1), (2, 1), (3, 1)),
        ((1, -1), (0, 1), (3, -1), (2, 1)),
        ((2, -1), (3, 1), (0, 1), (1, -1)),
        ((3, -1), (2, -1), (1, 1), (0, 1)),
    )
    witnesses = []
    for result in data["results"]:
        m = result["core_order"]
        for entry in result["realized_types_with_one_verified_witness_each"]:
            encoded = entry["sequences"]
            if len(encoded) != 4 or any(len(row) != m or set(row) - {"+", "-"} for row in encoded):
                raise ValueError("invalid stored sequence witness")
            seqs = [[1 if sign == "+" else -1 for sign in row] for row in encoded]
            if any(row[0] != 1 or any(row[j] != row[-j % m] for j in range(m)) for row in seqs):
                raise ValueError("stored witness is not normalized and symmetric")
            indices = [sum((row[j] == -1) << (j - 1) for j in range(1, (m + 1) // 2)) for row in seqs]
            if indices != entry["normalized_sequence_indices"] or indices != sorted(indices):
                raise ValueError("stored witness index mismatch")
            if sorted(abs(sum(row)) for row in seqs) != entry["absolute_row_sums"]:
                raise ValueError("stored witness row-sum label mismatch")
            matrix = []
            for block_row in patterns:
                for i in range(m):
                    matrix.append([sign * seqs[b][(j - i) % m]
                                   for b, sign in block_row for j in range(m)])
            checks = check_rows(matrix, 4 * m)
            witnesses.append({"core_order": m, "absolute_row_sums": entry["absolute_row_sums"], **checks})
    return {
        "status": "passed",
        "method": "independently reconstructed block arrays; explicit integer row dot products",
        "witnesses_checked": len(witnesses),
        "results": witnesses,
    }


def compare_sources(sign_path: Path, csv_path: Path) -> dict:
    csv_raw = csv_path.read_bytes()
    lines = csv_raw.decode("ascii").splitlines()
    if len(lines) != 668:
        raise ValueError("CSV row count is not 668")
    rows = []
    for line in lines:
        fields = line.split(",")
        if len(fields) != 668 or any(field not in ("1", "-1") for field in fields):
            raise ValueError("CSV token or column count is invalid")
        rows.append("".join("+" if field == "1" else "-" for field in fields))
    canonical = ("\n".join(rows) + "\n").encode("ascii")
    if canonical != sign_path.read_bytes():
        raise ValueError("the two sources do not encode the exact same entries")
    return {
        "status": "passed",
        "method": "independent ASCII comma splitting with literal token validation; byte-for-byte canonical sign comparison",
        "csv_bytes": len(csv_raw),
        "csv_sha256": hashlib.sha256(csv_raw).hexdigest(),
        "rows": 668,
        "columns": 668,
        "canonical_sign_bytes": len(canonical),
        "canonical_sign_sha256": hashlib.sha256(canonical).hexdigest(),
        "equal_to_independently_verified_sign_matrix": True,
    }


def compare_solution_sets(study: Path, independent_path: Path) -> dict:
    independent = json.loads(independent_path.read_text())
    # Import the subject only for the explicit comparison, never to generate
    # or filter the independently enumerated candidate tuples.
    import sys

    sys.path.insert(0, str(study / "scripts"))
    from enumerate_williamson import all_quadruples

    compared = []
    for result in independent["results"]:
        m = result["core_order"]
        actual = sorted(list(q) for q in all_quadruples(m))
        if actual != result["solving_sequence_index_multisets"]:
            raise ValueError(f"solution-set mismatch at m={m}")
        compared.append({"core_order": m, "exact_solution_multiset_equality": True,
                         "solution_count": len(actual)})
    return {
        "status": "passed",
        "comparison": "full sorted solution tuple sets, after independent direct brute force; every odd m<=15",
        "results": compared,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--study-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--matrix-signs", type=Path, required=True)
    parser.add_argument("--matrix-csv", type=Path, required=True)
    parser.add_argument("--independent-williamson", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    independent_path = args.independent_williamson or args.study_root / "reviews/williamson-independent.json"
    outputs = {
        "paley-independent.json": check_paley(args.study_root),
        "williamson-witnesses-independent.json": check_witnesses(args.study_root),
        "source-data-comparison-independent.json": compare_sources(args.matrix_signs, args.matrix_csv),
        "williamson-solution-set-comparison.json": compare_solution_sets(args.study_root, independent_path),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, result in outputs.items():
        write_json(args.output_dir / name, result)
        print(f"{name}: passed")


if __name__ == "__main__":
    main()
