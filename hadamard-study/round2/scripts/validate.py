"""Bind exact filter outputs to independent complete baselines and certificates.

Run after benchmark.py. Does not time algorithms for comparison. Every generated
tuple is also converted to a Hadamard array and exactly checked. Preserves
original sequence masks, including gaps caused by filtering.
"""

from itertools import combinations_with_replacement
import hashlib
import json
from pathlib import Path

from search import Prepared, order3_energy, pair_search, product_search, square_sums
from hadamard import verify, williamson

ROUND = Path(__file__).resolve().parents[1]
STUDY = ROUND.parent


def witness_certificates(p):
    two, three = square_sums(p.m)
    single = {}
    for a in range(len(p.seqs)):
        residual = 4 * p.m - p.squares[a]
        if residual not in three:
            single.setdefault("row", {"mask": a, "row_sum": sum(p.seqs[a]),
                                      "remaining_square_sum": residual, "not_in_three_square_set": True})
            continue
        if p.m % 3 == 0 and order3_energy(p.seqs[a]) > 4 * p.m:
            single.setdefault("order3", {"mask": a, "energy": order3_energy(p.seqs[a]), "bound": 4 * p.m})
            continue
        for k, (energy, limit) in enumerate(zip(p.energies[a], p.limits)):
            if energy > limit:
                single.setdefault("integer_probe", {"mask": a, "frequency_label": p.probes[k][0],
                    "integer_vector": list(p.probes[k][1]), "energy": energy, "bound": limit})
                break
    pairs = {}
    for a, b in combinations_with_replacement(p.masks, 2):
        reason = p.pair_rejection(a, b)
        if reason == 1:
            pairs.setdefault("row", {"masks": [a, b], "remaining_square_sum": 4 * p.m - p.squares[a] - p.squares[b],
                                     "not_in_two_square_set": True})
        elif reason == 2:
            pairs.setdefault("order3", {"masks": [a, b], "energy": p.e3[a] + p.e3[b], "bound": 4 * p.m})
        elif reason == 3 and "integer_probe" not in pairs:
            k = next(k for k, limit in enumerate(p.limits) if p.energies[a][k] + p.energies[b][k] > limit)
            pairs["integer_probe"] = {"masks": [a, b], "frequency_label": p.probes[k][0],
                "integer_vector": list(p.probes[k][1]), "energy": p.energies[a][k] + p.energies[b][k], "bound": p.limits[k]}
        if len(pairs) == 3:
            break
    return {"single_rejection_examples": single, "pair_rejection_examples": pairs}


def main():
    first = json.loads((STUDY / "reviews/williamson-independent.json").read_text())
    moderate = json.loads((ROUND / "reviews/moderate-independent.json").read_text())
    expected = {r["core_order"]: r["solving_sequence_index_multisets"] for r in first["results"]}
    expected.update({r["core_order"]: r["solutions"] for r in moderate["results"]})
    benchmark = json.loads((ROUND / "evidence/benchmark.json").read_text())
    records = []
    for m, baseline in sorted(expected.items()):
        p = Prepared(m, filtered=True)
        solutions, counts = pair_search(p)
        if [list(q) for q in solutions] != baseline:
            raise RuntimeError(f"independent baseline mismatch at {m}")
        if pair_search(p, product_key=True)[0] != solutions:
            raise RuntimeError("product-key mismatch")
        if m <= 15 and product_search(p)[0] != solutions:
            raise RuntimeError("product-triple mismatch")
        digest = hashlib.sha256(json.dumps(baseline, separators=(",", ":")).encode()).hexdigest()
        measured = [r for r in benchmark["summary"] if r["core_order"] == m]
        if any(r["solution_tuple_json_sha256"] != digest for r in measured):
            raise RuntimeError("benchmark solution-set mismatch")
        checked_pairs = 0
        for q in solutions:
            result = verify(williamson([p.seqs[a] for a in q]))
            checked_pairs += result["unordered_row_pairs_checked"]
        records.append({"core_order": m, "exact_independent_solution_set_equality": True,
                        "counts": counts, "solutions": baseline,
                        "solution_tuple_json_sha256": digest,
                        "every_output_array_exactly_verified": True,
                        "matrix_row_pairs_checked": checked_pairs,
                        "benchmark_case_count_compared": len(measured),
                        **witness_certificates(p)})
    output = {"status": "passed", "baseline": "first-edition independent direct exhaustive four-multisets for odd m<=15; independent unfiltered full-lag MITM for m19,21",
              "all_false_negative_checks_use_complete_baselines": True,
              "all_benchmarked_solution_digests_match": True, "results": records}
    (ROUND / "data/validated-solutions.json").write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"Validated {sum(len(r['solutions']) for r in records)} exact tuples across {len(records)} core orders")
    print(f"Checked {sum(r['matrix_row_pairs_checked'] for r in records)} row pairs across all output arrays")


if __name__ == "__main__":
    main()
