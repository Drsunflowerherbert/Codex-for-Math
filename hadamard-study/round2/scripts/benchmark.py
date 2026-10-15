"""Reproducible sequential fresh-process benchmark; no external dependencies.

Run on Linux. Timed cases do not overlap. Each result includes preprocessing,
search, external process wall time (including startup/output), and ru_maxrss.
Three deterministic repetitions per case, rotated method order. No floating
point quantity participates in candidate rejection; floats here measure time.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import statistics
import subprocess
import sys
import tempfile
import time

CASES = [("baseline-mitm", "all"), ("filtered-mitm", "row"),
         ("filtered-mitm", "row-order3"), ("filtered-mitm", "all"),
         ("filtered-mitm-product-key", "all"), ("product-triples", "all")]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cores", type=int, nargs="+", default=[3, 15, 19, 21])
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if platform.system() != "Linux" or args.repeats < 1:
        parser.error("requires Linux and positive repetition count")
    script = Path(__file__).with_name("search.py")
    study = script.resolve().parents[2]
    measured_sources = [script, Path(__file__), study / "scripts/enumerate_williamson.py",
                        study / "scripts/hadamard.py"]
    def source_hashes():
        return {str(p.resolve().relative_to(study)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in measured_sources}
    hashes_before = source_hashes()
    runs = []
    solutions_by_core = {}
    with tempfile.TemporaryDirectory(prefix="hadamard-r2-benchmark-") as tmp:
        output = Path(tmp) / "worker.json"
        for core in args.cores:
            for repetition in range(args.repeats):
                # Rotate method order deterministically; no concurrent workers.
                ordered = CASES[repetition:] + CASES[:repetition]
                for method, filters in ordered:
                    started = time.perf_counter()
                    subprocess.run([sys.executable, str(script), "--core", str(core),
                                    "--method", method, "--filters", filters,
                                    "--output", str(output)], check=True, capture_output=True, text=True)
                    process_wall = time.perf_counter() - started
                    result = json.loads(output.read_text())
                    solution_bytes = json.dumps(result.pop("solutions"), separators=(",", ":")).encode()
                    digest = hashlib.sha256(solution_bytes).hexdigest()
                    expected = solutions_by_core.setdefault(core, digest)
                    if digest != expected:
                        raise RuntimeError(f"solution set mismatch for core {core}")
                    result.update({"repetition": repetition + 1,
                                   "external_process_wall_seconds": process_wall,
                                   "solution_tuple_json_sha256": digest})
                    runs.append(result)
            print(f"core {core}: {args.repeats} repetitions of all six cases; solution sets agree", flush=True)
    summary = []
    for core in args.cores:
        for method, requested_filters in CASES:
            enabled = "none" if method == "baseline-mitm" else requested_filters
            subset = [r for r in runs if r["core_order"] == core and r["method"] == method
                      and r["enabled_filters"] == enabled]
            counts = subset[0]["counts"]
            if any(r["counts"] != counts for r in subset):
                raise RuntimeError("nondeterministic candidate counts")
            record = {"core_order": core, "method": method, "enabled_filters": enabled,
                      "counts": counts, "solution_tuple_json_sha256": subset[0]["solution_tuple_json_sha256"]}
            for name, getter in (
                ("preprocessing_seconds", lambda r: r["timing_seconds"]["preprocessing"]),
                ("search_seconds", lambda r: r["timing_seconds"]["search"]),
                ("in_process_total_seconds", lambda r: r["timing_seconds"]["total_in_process"]),
                ("external_process_wall_seconds", lambda r: r["external_process_wall_seconds"]),
                ("process_peak_rss_kib", lambda r: r["process_peak_rss_kib"])):
                values = [getter(r) for r in subset]
                record[name] = {"median": statistics.median(values), "min": min(values), "max": max(values)}
            summary.append(record)
    hashes_after = source_hashes()
    if hashes_before != hashes_after:
        raise RuntimeError("measured source changed during benchmark")
    cpu_model = next((line.split(":", 1)[1].strip() for line in
                      Path("/proc/cpuinfo").read_text().splitlines() if line.startswith("model name")), "unknown")
    package = {"protocol": "sequential fresh Linux worker processes; deterministic rotated method order; all preprocessing charged; external wall includes startup and JSON output; entire-process peak RSS, not incremental allocations",
               "python": platform.python_version(), "platform": platform.platform(),
               "machine": platform.machine(), "cpu_model": cpu_model, "logical_cpus_visible": os.cpu_count(),
               "repetitions_per_case": args.repeats,
               "cores": args.cores,
               "source_sha256_before": hashes_before, "source_sha256_after": hashes_after,
               "measured_sources_unchanged_during_run": True,
               "all_cases_have_identical_solution_sets_within_each_core": True,
               "summary": summary, "raw_runs": runs}
    args.output.write_text(json.dumps(package, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
