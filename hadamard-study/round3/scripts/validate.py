"""Validate all reported structural solution tuples and their Hadamard matrices.

This is an exact validation run, not a comparative timing benchmark. The
independent reference is a separately authored, unpruned physical-edge search.
Every returned tuple is reconstructed and checked by the first-edition matrix
constructor and exact all-row-pairs verifier.
"""

import argparse
import hashlib
import json
from pathlib import Path
import sys


SCRIPT_DIR = Path(__file__).resolve().parent
ROUND3_DIR = SCRIPT_DIR.parent
STUDY_DIR = ROUND3_DIR.parent
for directory in (SCRIPT_DIR, STUDY_DIR / "scripts"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

from hadamard import sign_bytes, verify, williamson
from partial_singles import sequence_from_mask
from phase_search import search


CORE_ORDERS = tuple(range(1, 16, 2)) + (19, 21, 23)
DEFAULT_REFERENCE = ROUND3_DIR / "reviews" / "structure-independent.json"


def checked_tuples(values, core_order, label):
    """Require the exact sorted original-mask multiset domain, without repair."""
    if not isinstance(values, list):
        raise ValueError(f"{label}: expected a list of solution tuples")
    bound = 1 << ((core_order - 1) // 2)
    tuples = []
    for value in values:
        if (not isinstance(value, (list, tuple)) or len(value) != 4
                or any(type(mask) is not int or not 0 <= mask < bound for mask in value)):
            raise ValueError(f"{label}: malformed original-mask tuple {value!r}")
        row = tuple(value)
        if row != tuple(sorted(row)):
            raise ValueError(f"{label}: block masks are not sorted: {row!r}")
        tuples.append(row)
    if tuples != sorted(tuples) or len(tuples) != len(set(tuples)):
        raise ValueError(f"{label}: tuple list is unsorted or contains duplicates")
    return tuples


def load_reference(path):
    raw = path.read_bytes()
    document = json.loads(raw)
    if not isinstance(document, dict) or not isinstance(document.get("results"), list):
        raise ValueError("independent reference has no results list")
    records = {}
    for record in document["results"]:
        core = record.get("core_order")
        if type(core) is not int or core < 1 or core % 2 == 0 or core in records:
            raise ValueError("independent reference has an invalid or repeated core order")
        records[core] = checked_tuples(record.get("solutions"), core,
                                       f"independent reference m={core}")
    missing = set(CORE_ORDERS) - records.keys()
    if missing:
        raise ValueError(f"independent reference is missing core orders {sorted(missing)}")
    try:
        reference_name = path.resolve().relative_to(STUDY_DIR).as_posix()
    except ValueError:
        reference_name = str(path)
    return records, {"path": reference_name, "sha256": hashlib.sha256(raw).hexdigest(),
                     "method": document.get("method")}


def validate(reference_path=DEFAULT_REFERENCE, progress=None):
    reference, provenance = load_reference(Path(reference_path))
    results = []
    total_matrices = total_entries = total_pairs = 0
    for core in CORE_ORDERS:
        found = search(core, mode="expanded", order_strategy="collisions")
        tuples = checked_tuples(found["solutions"], core, f"phase search m={core}")
        if tuples != reference[core]:
            missing = sorted(set(reference[core]) - set(tuples))
            extra = sorted(set(tuples) - set(reference[core]))
            raise RuntimeError(f"m={core}: exact independent tuple equality failed; "
                               f"missing={missing[:5]}, extra={extra[:5]}")
        matrix_order = 4 * core
        expected_pairs = matrix_order * (matrix_order - 1) // 2
        matrix_checks = []
        for masks in tuples:
            sequences = [sequence_from_mask(core, mask) for mask in masks]
            matrix = williamson(sequences)
            result = verify(matrix)
            if (result.get("order") != matrix_order
                    or result.get("unordered_row_pairs_checked") != expected_pairs
                    or result.get("all_off_diagonal_dot_products_zero") is not True):
                raise RuntimeError(f"m={core}, masks={masks}: incomplete matrix verification")
            digest = hashlib.sha256(sign_bytes(matrix)).hexdigest()
            matrix_checks.append({"normalized_sequence_masks": list(masks),
                                  "matrix_sha256_ascii_sign_rows_final_lf": digest,
                                  "verification": result})
            total_matrices += 1
            total_entries += result["entries"]
            total_pairs += result["unordered_row_pairs_checked"]
        pairs = len(tuples) * expected_pairs
        results.append({"core_order": core, "hadamard_order": matrix_order,
                        "exact_sorted_tuple_list_equals_independent_reference": True,
                        "solutions": [list(value) for value in tuples],
                        "solving_normalized_multisets": len(tuples),
                        "all_constructed_matrices_verified": True,
                        "matrix_entries_checked": len(tuples) * matrix_order * matrix_order,
                        "unordered_matrix_row_pairs_checked": pairs,
                        "search_coverage_counts": found["counts"],
                        "coordinate_visit_order_one_based": found["coordinate_visit_order_one_based"],
                        "matrix_checks": matrix_checks})
        if progress is not None:
            progress(core, len(tuples), pairs)
    return {"validation": "passed", "schema_version": 1,
            "purpose": "exact validation; not a comparative timing benchmark",
            "arithmetic": "Python integers; full tuple equality and every unordered matrix row pair",
            "core_orders": list(CORE_ORDERS),
            "search_configuration": {"mode": "expanded", "order_strategy": "collisions"},
            "independent_reference": provenance,
            "matrix_constructor_and_verifier": "first edition scripts/hadamard.py williamson/verify",
            "totals": {"core_orders_checked": len(CORE_ORDERS),
                       "matrices_verified": total_matrices,
                       "matrix_entries_checked": total_entries,
                       "unordered_matrix_row_pairs_checked": total_pairs},
            "count_domain": "sorted multisets of four original normalized symmetric sequence masks; repetitions allowed",
            "results": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    args = parser.parse_args()

    def progress(core, tuples, pairs):
        print(f"m={core}: {tuples} exact tuples; {pairs} matrix row pairs checked", flush=True)

    result = validate(args.reference, progress=progress)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"validation": result["validation"], "output": str(args.output),
                      "totals": result["totals"]}, sort_keys=True))


if __name__ == "__main__":
    main()
