#!/usr/bin/env python3
"""Audit recorded benchmark arithmetic, coverage, source identity, and costs."""

import argparse
import hashlib
import json
from math import comb
from pathlib import Path
import statistics


def digest_tuples(tuples):
    return hashlib.sha256(json.dumps(tuples,separators=(",",":")).encode()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--benchmark",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    study=Path(__file__).resolve().parents[2]
    data=json.loads(args.benchmark.read_text())
    first=json.loads((study/"reviews/williamson-independent.json").read_text())
    moderate=json.loads((study/"round2/reviews/moderate-independent.json").read_text())
    expected={r["core_order"]:r["solving_sequence_index_multisets"] for r in first["results"]}
    expected.update({r["core_order"]:r["solutions"] for r in moderate["results"]})
    repeats=data["repetitions_per_case"]
    if repeats != 3:
        raise ValueError("the audited protocol requires three repetitions")
    if data["source_sha256_before"] != data["source_sha256_after"] or not data["measured_sources_unchanged_during_run"]:
        raise ValueError("measured source identity changed during benchmark")
    for name,digest in data["source_sha256_after"].items():
        if hashlib.sha256((study/name).read_bytes()).hexdigest() != digest:
            raise ValueError("current source differs from benchmark source: "+name)
    cases=(("baseline-mitm","none"),("filtered-mitm","row"),
           ("filtered-mitm","row-order3"),("filtered-mitm","all"),
           ("filtered-mitm-product-key","all"),("product-triples","all"))
    if len(data["raw_runs"]) != len(data["cores"])*len(cases)*repeats:
        raise ValueError("missing or additional benchmark runs")
    summaries={(row["core_order"],row["method"],row["enabled_filters"]):row for row in data["summary"]}
    if len(summaries) != len(data["cores"])*len(cases):
        raise ValueError("duplicate or missing summary cases")
    checked=[]
    for m in data["cores"]:
        known_digest=digest_tuples(expected[m])
        joins=[]
        for method,filters in cases:
            runs=[r for r in data["raw_runs"] if r["core_order"]==m and r["method"]==method and r["enabled_filters"]==filters]
            if len(runs)!=repeats or sorted(r["repetition"] for r in runs)!=[1,2,3]:
                raise ValueError(("repetition coverage mismatch",m,method,filters))
            summary=summaries[m,method,filters]
            if any(r["solution_tuple_json_sha256"]!=known_digest for r in runs) or summary["solution_tuple_json_sha256"]!=known_digest:
                raise ValueError(("independent exact solution-set digest mismatch",m,method,filters))
            counts=runs[0]["counts"]
            if summary["counts"]!=counts or any(r["counts"]!=counts for r in runs):
                raise ValueError("nondeterministic or misreported candidate counts")
            if counts["solving_normalized_multisets"] != len(expected[m]):
                raise ValueError("incorrect solution count")
            raw_n=1<<(m//2)
            if counts["raw_normalized_sequences"] != raw_n:
                raise ValueError("incorrect raw candidate count")
            n=raw_n
            if filters!="none":
                single_counts=[counts[key] for key in ("single_after_row_square_feasibility","single_after_order3_energy","single_after_integer_probes")]
                if [raw_n]+single_counts != sorted([raw_n]+single_counts,reverse=True):
                    raise ValueError("single-stage counts not monotone")
                n=single_counts[-1]
            if method=="product-triples":
                if counts["triples_visited"]!=comb(n+2,3) or counts["stored_pairs"]!=0:
                    raise ValueError("triple-domain count mismatch")
                stages=[counts[key] for key in ("triples_visited","after_forced_fourth_mask_and_order","after_quadruple_row_square_sum","after_pair_energy_tests","full_PAF_quadruples_tested","solving_normalized_multisets")]
                if stages!=sorted(stages,reverse=True):
                    raise ValueError("triple-stage counts not monotone")
            else:
                if counts["pairs_considered_after_single_filters"]!=n*(n+1)//2:
                    raise ValueError("pair-domain count mismatch")
                stages=[counts[key] for key in ("pairs_considered_after_single_filters","pair_after_row_square_feasibility","pair_after_order3_energy","pair_after_integer_probes")]
                if stages!=sorted(stages,reverse=True) or counts["stored_pairs"]!=stages[-1]:
                    raise ValueError("pair-stage counts not monotone")
                joins.append(counts["joined_pair_combinations_before_sorted_order_test"])
            metrics=(
                ("preprocessing_seconds",lambda r:r["timing_seconds"]["preprocessing"]),
                ("search_seconds",lambda r:r["timing_seconds"]["search"]),
                ("in_process_total_seconds",lambda r:r["timing_seconds"]["total_in_process"]),
                ("external_process_wall_seconds",lambda r:r["external_process_wall_seconds"]),
                ("process_peak_rss_kib",lambda r:r["process_peak_rss_kib"]))
            for name,getter in metrics:
                values=[getter(r) for r in runs]
                if min(values)<0 or summary[name]!={"median":statistics.median(values),"min":min(values),"max":max(values)}:
                    raise ValueError(("summary arithmetic mismatch",m,method,filters,name))
            for run in runs:
                timings=run["timing_seconds"]
                if abs(timings["preprocessing"]+timings["search"]-timings["total_in_process"])>1e-9:
                    raise ValueError("preprocessing not correctly charged")
                if run["external_process_wall_seconds"]<timings["total_in_process"] or run["process_peak_rss_kib"]<=0:
                    raise ValueError("invalid process measurement")
        if len(set(joins))!=1:
            raise ValueError("full-profile join count changed under necessary filters")
        baseline=summaries[m,"baseline-mitm","none"]
        filtered=summaries[m,"filtered-mitm","all"]
        checked.append({"core_order":m,"independent_solution_count":len(expected[m]),
                        "full_profile_join_combinations_all_MITM_cases":joins[0],
                        "all_six_cases_have_independently_verified_exact_tuple_digest":True,
                        "baseline_over_filtered_median_external_wall_ratio":baseline["external_process_wall_seconds"]["median"]/filtered["external_process_wall_seconds"]["median"],
                        "baseline_over_filtered_median_peak_RSS_ratio":baseline["process_peak_rss_kib"]["median"]/filtered["process_peak_rss_kib"]["median"]})
    result={"status":"passed","benchmark_file":str(args.benchmark),"raw_runs_audited":len(data["raw_runs"]),
            "checks":"exact independent tuple digests; source hashes; repetitions; candidate-domain counts; stage monotonicity; all summary min/median/max arithmetic; preprocessing and search accounting",
            "measurement_scope":"Linux worker ru_maxrss observed after search includes interpreter and preparation/search; external wall includes startup and output; timing ratios are observations, not portable guarantees",
            "results":checked}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":"passed","raw_runs_audited":len(data["raw_runs"])}))


if __name__ == "__main__":
    main()
