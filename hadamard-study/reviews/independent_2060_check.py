#!/usr/bin/env python3
"""Check the literal order-2060 data without running or importing its file.

Parsing accepts a fixed assignment header, literal sign rows, and a fixed
closing bracket.  Verification uses positive-support intersections, distinct
from both the study's XOR verifier and the reviewer's scalar-product verifier.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time


def parse_literal_rows(raw: bytes, variable: str, order: int) -> tuple[list[int], str]:
    lines = raw.decode("ascii").splitlines()
    if len(lines) != order + 2:
        raise ValueError("unexpected number of lines")
    if lines[0] != f"{variable} = [" or lines[-1] != "]":
        raise ValueError("unexpected header or footer")
    masks = []
    canonical = hashlib.sha256()
    for row_index, line in enumerate(lines[1:-1]):
        stripped = line.strip()
        if not (stripped.startswith("[") and stripped.endswith("],")):
            raise ValueError(f"row {row_index}: invalid row delimiters")
        fields = [field.strip() for field in stripped[1:-2].split(",")]
        if len(fields) != order or any(field not in ("1", "-1") for field in fields):
            raise ValueError(f"row {row_index}: invalid sign literal or row length")
        mask = 0
        signs = []
        for column, field in enumerate(fields):
            if field == "1":
                mask |= 1 << column
                signs.append("+")
            else:
                signs.append("-")
        masks.append(mask)
        canonical.update(("".join(signs) + "\n").encode("ascii"))
    return masks, canonical.hexdigest()


def check_positive_supports(masks: list[int], order: int) -> dict[str, int]:
    if len(masks) != order or any(mask < 0 or mask >> order for mask in masks):
        raise ValueError("invalid number or width of support masks")
    sizes = [mask.bit_count() for mask in masks]
    checks = 0
    for left in range(order):
        for right in range(left):
            common = (masks[left] & masks[right]).bit_count()
            dot = order - 2 * sizes[left] - 2 * sizes[right] + 4 * common
            if dot:
                raise ValueError(f"rows {left}, {right}: dot product {dot} is nonzero")
            checks += 1
    if checks != order * (order - 1) // 2:
        raise RuntimeError("pair-check count mismatch")
    return {"row_norms_implied_by_literal_signs": order, "distinct_row_pair_checks": checks}


def self_test() -> dict[str, str]:
    raw = b"H4 = [\n[1, 1, 1, 1],\n[1, -1, 1, -1],\n[1, 1, -1, -1],\n[1, -1, -1, 1],\n]\n"
    masks, _ = parse_literal_rows(raw, "H4", 4)
    check_positive_supports(masks, 4)
    corrupted = masks.copy()
    corrupted[1] ^= 1
    try:
        check_positive_supports(corrupted, 4)
    except ValueError:
        pass
    else:
        raise RuntimeError("single-sign corruption was accepted")
    for malformed in (raw + b"print('unexpected code')\n", raw.replace(b"1, 1, 1, 1", b"1, 1, 1, 0"), raw.replace(b"H4 = [", b"H4 = run(")):
        try:
            parse_literal_rows(malformed, "H4", 4)
        except ValueError:
            pass
        else:
            raise RuntimeError("non-literal input was accepted")
    return {"valid_4_by_4": "passed", "single_sign_corruption": "rejected", "nonliteral_inputs": "rejected"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data_file", type=Path)
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    tests = self_test()
    raw = args.data_file.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != args.expected_sha256:
        raise ValueError("raw data SHA-256 mismatch")
    started = time.perf_counter()
    order = 2060
    masks, canonical_digest = parse_literal_rows(raw, "H2060", order)
    checks = check_positive_supports(masks, order)
    result = {
        "status": "passed",
        "claim": "H H^T = 2060 I_2060 for the supplied literal sign data",
        "data_file": str(args.data_file),
        "raw_bytes": len(raw),
        "raw_sha256": digest,
        "canonical_sign_sha256": canonical_digest,
        "order": order,
        "entries_checked": order * order,
        **checks,
        "arithmetic": "exact Python integers; dot = n - 2|P_i| - 2|P_j| + 4|P_i intersection P_j|",
        "external_file_was_executed_or_imported": False,
        "self_tests": tests,
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
