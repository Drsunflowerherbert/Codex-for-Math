"""Independent arithmetic, benchmark-record, and preservation audit.

Standard library only; imports no study module. This does not rerun timings.
"""

import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import statistics
import subprocess

ROUND = Path(__file__).resolve().parents[1]
STUDY = ROUND.parent
REPO = STUDY.parent
PRESERVED = "913b328b74712409a036cd49c954cd8a7dcd18b1"


def digest(value):
    return hashlib.sha256(json.dumps(value, separators=(",", ":")).encode()).hexdigest()


def sequence(m, mask):
    x = [1] * m
    for j in range(1, (m + 1) // 2):
        x[j] = x[-j] = -1 if mask & (1 << (j - 1)) else 1
    return x


def matrix(m, masks):
    """Construct entries by explicit quaternion block table, no circulant helper."""
    rows = [sequence(m, mask) for mask in masks]
    # Signed, one-based identifiers of the four symmetric circulant blocks.
    table = ((1, 2, 3, 4), (-2, 1, -4, 3),
             (-3, 4, 1, -2), (-4, -3, 2, 1))
    return [[(1 if table[a][b] > 0 else -1)
             * rows[abs(table[a][b]) - 1][(j - i) % m]
             for b in range(4) for j in range(m)]
            for a in range(4) for i in range(m)]


def eligible(m):
    """Enumerate complete rows directly, with explicit integer convolutions."""
    squares = {r * r for r in range(1, m + 1, 2)}
    three = {sum(t) for t in itertools.product(squares, repeat=3)}
    probes = []
    for f in range(1, (m + 1) // 2):
        t = [m - 4 * min(f * j % m, m - f * j % m) for j in range(m)]
        v = [m * z - sum(t) for z in t]
        if any(v):
            probes.append((v, 4 * m * sum(z * z for z in v)))
    result = []
    for mask in range(1 << ((m - 1) // 2)):
        x = sequence(m, mask)
        if 4 * m - sum(x) ** 2 not in three:
            continue
        if m % 3 == 0 and (sum(x[::3]) - sum(x[1::3])) ** 2 > 4 * m:
            continue
        if any(sum(sum(x[i] * v[(j + i) % m] for i in range(m)) ** 2
                   for j in range(m)) > limit for v, limit in probes):
            continue
        result.append(mask)
    return result


def audit():
    baseline = json.loads((ROUND / "reviews/structure-independent.json").read_text())
    expected = {r["core_order"]: r["solutions"] for r in baseline["results"]}
    leaves = {r["core_order"]: r["unpruned_RGS_colorings"] for r in baseline["results"]}
    subject = json.loads((ROUND / "reviews/subject-audit.json").read_text())
    subject_counts = {r["core_order"]: r["phase_generation_counts"] for r in subject["results"]}
    data = json.loads((ROUND / "data/validated-solutions.json").read_text())
    matrices = entries = row_pairs = 0
    for record in data["results"]:
        m = record["core_order"]
        assert record["solutions"] == expected[m]
        assert [r["normalized_sequence_masks"] for r in record["matrix_checks"]] == expected[m]
        for certificate in record["matrix_checks"]:
            h = matrix(m, certificate["normalized_sequence_masks"])
            n = len(h)
            assert all(len(row) == n and set(row) <= {-1, 1} for row in h)
            for i in range(n):
                assert sum(x * x for x in h[i]) == n
                for j in range(i):
                    assert sum(x * y for x, y in zip(h[i], h[j])) == 0, (m, i, j)
                    row_pairs += 1
            raw = b"".join(bytes(43 if x == 1 else 45 for x in row) + b"\n" for row in h)
            assert hashlib.sha256(raw).hexdigest() == certificate["matrix_sha256_ascii_sign_rows_final_lf"]
            entries += n * n
            matrices += 1
    assert (matrices, entries, row_pairs) == (135, 689008, 339854)

    bench = json.loads((ROUND / "evidence/benchmark.json").read_text())
    assert bench["cores"] == [15, 21, 23] and bench["repetitions"] == 3
    assert len(bench["raw_runs"]) == 45 and len(bench["single_generation_raw_runs"]) == 27
    assert bench["source_sha256_before"] == bench["source_sha256_after"]
    for path, sha in bench["source_sha256_before"].items():
        assert hashlib.sha256((STUDY / path).read_bytes()).hexdigest() == sha, path
    configs = {"round2-filtered", "structural-leaf", "structural-basic", "phase-natural", "phase-collisions"}
    assert Counter((r["core_order"], r["case"]) for r in bench["raw_runs"]) == Counter(
        {(m, c): 3 for m in bench["cores"] for c in configs})
    for r in bench["raw_runs"]:
        m, c, counts = r["core_order"], r["case"], r["counts"]
        assert r["exact_independent_tuple_list_equality"]
        assert r["solution_tuple_json_sha256"] == digest(expected[m])
        if c != "round2-filtered":
            assert counts["solutions"] == len(expected[m])
            assert counts["raw_RGS_color_leaves"] == leaves[m]
            assert counts["complete_color_assignments_entered"] + counts["structural_leaves_skipped_before_completion"] == leaves[m]
            assert counts["nodes_entered"] == sum(counts["nodes_by_depth"])
            assert counts["complete_color_assignments_entered"] == counts["nodes_by_depth"][-1]
            assert counts["structural_leaves_skipped_before_completion"] == sum(counts["skipped_leaves_by_prefix_depth"])
            assert counts["individual_sequence_pool_generated"] == counts["stored_pairs"] == 0
            if c.startswith("phase-"):
                order = c.removeprefix("phase-")
                assert counts == subject_counts[m][order + "/expanded"]

    single_lists = {m: eligible(m) for m in range(1, 24, 2)}
    single_validation = json.loads((ROUND / "evidence/partial-single-validation.json").read_text())
    comparisons = 0
    for record in single_validation["results"]:
        for configuration in record["configurations"]:
            assert configuration["eligible_masks"] == single_lists[record["core_order"]]
            comparisons += 1
    assert comparisons == 33
    for r in bench["single_generation_raw_runs"]:
        assert r["exact_single_mask_list_equality"]
        assert r["eligible_mask_json_sha256"] == digest(single_lists[r["core_order"]])
        c = r["counts"]
        if r["case"] != "round2-preparation":
            assert c["nodes_visited"] == sum(c["nodes_by_depth"])
            assert c["leaf_checks_reached"] + sum(c["original_masks_covered_by_pruning_stage"].values()) == c["raw_original_masks"]
            for stage, depths in c["nodes_pruned_by_stage_and_depth"].items():
                assert c["nodes_pruned_by_stage"][stage] == sum(depths)
                assert c["partial_nodes_pruned_by_stage"][stage] == sum(depths[:-1])
                assert c["original_masks_covered_by_pruning_stage"][stage] == sum(
                    amount * (1 << (len(depths) - 1 - d)) for d, amount in enumerate(depths))

    summary_checks = 0
    for raw_key, summary_key in (("raw_runs", "summary"), ("single_generation_raw_runs", "single_generation_summary")):
        for summary in bench[summary_key]:
            group = [r for r in bench[raw_key] if (r["core_order"], r["case"]) == (summary["core_order"], summary["case"])]
            assert len(group) == 3 and {r["repetition"] for r in group} == {1, 2, 3}
            assert all(r["counts"] == summary["counts"] for r in group)
            getters = {
                "external_process_wall_seconds": lambda r: r["external_process_wall_seconds"],
                "process_peak_rss_kib": lambda r: r.get("process_peak_rss_kib", r.get("process_peak_rss_kib_observed_after_search")),
                "total_in_process_seconds": lambda r: r["timing_seconds"]["total_in_process"] if "timing_seconds" in r else r["elapsed_seconds"],
            }
            if "timing_seconds" in group[0]:
                getters.update({k + "_seconds": lambda r, k=k: r["timing_seconds"][k] for k in ("preprocessing", "search")})
            for name, getter in getters.items():
                values = [getter(r) for r in group]
                assert summary[name] == {"min": min(values), "median": statistics.median(values), "max": max(values)}
                summary_checks += 1

    preserved = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", PRESERVED, "--", "hadamard-study"], cwd=REPO).decode().splitlines()
    for path in preserved:
        original = subprocess.check_output(["git", "show", PRESERVED + ":" + path], cwd=REPO)
        assert original == (REPO / path).read_bytes(), path
    return {"status": "passed", "study_module_imports": 0,
            "matrices_checked_by_explicit_integer_dot_products": matrices,
            "entries_checked": entries, "unordered_row_pairs_checked": row_pairs,
            "quadruple_benchmark_workers_audited": len(bench["raw_runs"]),
            "single_generation_benchmark_workers_audited": len(bench["single_generation_raw_runs"]),
            "benchmark_summary_metric_triples_recomputed": summary_checks,
            "measured_source_hashes_match_current_files": True,
            "independent_complete_single_enumeration_cores": list(single_lists),
            "single_validation_mask_lists_checked": comparisons,
            "preserved_commit": PRESERVED, "preserved_files_compared_byte_for_byte": len(preserved),
            "all_preserved_files_identical": True,
            "benchmark_scope": "record audit only; no new timing or RSS claims"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = audit()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
