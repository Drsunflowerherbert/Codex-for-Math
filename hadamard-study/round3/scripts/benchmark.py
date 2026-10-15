"""Sequential fresh-process comparison, including all preparation and startup.

No worker overlaps another. Exact tuple lists are checked against the independent
unpruned structural enumeration, not merely against another timed method.
"""

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import resource
import statistics
import subprocess
import sys
import tempfile
import time

HERE = Path(__file__).resolve().parent
ROUND = HERE.parent
STUDY = ROUND.parent
CASES = ("round2-filtered", "structural-leaf", "structural-basic",
         "phase-natural", "phase-collisions")


def load_reference():
    spec = importlib.util.spec_from_file_location("preserved_round2_search", STUDY / "round2/scripts/search.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def worker(core, case):
    if case == "round2-filtered":
        return load_reference().run(core, "filtered-mitm")
    if case.startswith("structural-"):
        from structure import search
        return search(core, "leaf" if case == "structural-leaf" else "all")
    from phase_search import search
    return search(core, "expanded", "natural" if case == "phase-natural" else "collisions")


def single_worker(core, configuration):
    started = time.perf_counter()
    if configuration == "round2-preparation":
        p = load_reference().Prepared(core, True)
        masks, counts = p.masks, p.counts
    else:
        from partial_singles import search
        result = search(core, "none" if configuration == "prefix-row" else "all")
        masks, counts = result["eligible_masks"], result["counts"]
    return {"core_order": core, "eligible_masks": masks, "counts": counts,
            "elapsed_seconds": time.perf_counter() - started,
            "process_peak_rss_kib_observed_after_search": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cores", nargs="+", type=int, default=[15, 21, 23])
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--worker-case", choices=CASES)
    parser.add_argument("--single-worker", choices=("round2-preparation", "prefix-row", "prefix-all"))
    parser.add_argument("--core", type=int)
    args = parser.parse_args()
    if args.worker_case or args.single_worker:
        result = (worker(args.core, args.worker_case) if args.worker_case
                  else single_worker(args.core, args.single_worker))
        args.output.write_text(json.dumps(result, sort_keys=True) + "\n")
        return
    if platform.system() != "Linux" or args.repeats < 1:
        parser.error("Linux and a positive repetition count required")
    sources = [HERE / name for name in ("benchmark.py", "structure.py", "phases.py", "phase_search.py", "partial_singles.py")]
    sources += [STUDY / name for name in ("round2/scripts/search.py", "scripts/enumerate_williamson.py", "scripts/hadamard.py")]
    def hashes():
        return {str(p.relative_to(STUDY)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    before = hashes()
    expected = {r["core_order"]: r["solutions"] for r in
                json.loads((ROUND / "reviews/structure-independent.json").read_text())["results"]}
    runs, singles = [], []
    with tempfile.TemporaryDirectory(prefix="hadamard-round3-") as tmp:
        output = Path(tmp) / "worker.json"
        for core in args.cores:
            for repetition in range(args.repeats):
                order = CASES[repetition % len(CASES):] + CASES[:repetition % len(CASES)]
                for case in order:
                    started = time.perf_counter()
                    subprocess.run([sys.executable, str(Path(__file__).resolve()), "--worker-case", case,
                                    "--core", str(core), "--output", str(output)], check=True, capture_output=True)
                    wall = time.perf_counter() - started
                    result = json.loads(output.read_text())
                    solutions = result.pop("solutions")
                    if solutions != expected[core]:
                        raise RuntimeError(("exact tuple set mismatch", core, case))
                    result.update({"case": case, "repetition": repetition + 1,
                                   "external_process_wall_seconds": wall,
                                   "solution_tuple_json_sha256": hashlib.sha256(json.dumps(solutions, separators=(",", ":")).encode()).hexdigest(),
                                   "exact_independent_tuple_list_equality": True})
                    runs.append(result)
            # Different domain: eligible single rows, no quadruple search here.
            expected_masks = None
            single_cases = ("round2-preparation", "prefix-row", "prefix-all")
            for repetition in range(args.repeats):
                for case in single_cases[repetition:] + single_cases[:repetition]:
                    started = time.perf_counter()
                    subprocess.run([sys.executable, str(Path(__file__).resolve()), "--single-worker", case,
                                    "--core", str(core), "--output", str(output)], check=True, capture_output=True)
                    wall = time.perf_counter() - started
                    result = json.loads(output.read_text())
                    masks = result.pop("eligible_masks")
                    if expected_masks is None:
                        expected_masks = masks
                    if masks != expected_masks:
                        raise RuntimeError(("eligible single mask mismatch", core, case))
                    result.update({"case": case, "repetition": repetition + 1,
                                   "external_process_wall_seconds": wall,
                                   "eligible_mask_json_sha256": hashlib.sha256(json.dumps(masks, separators=(",", ":")).encode()).hexdigest(),
                                   "exact_single_mask_list_equality": True})
                    singles.append(result)
            print(f"core {core}: all tuple sets and eligible single sets agree", flush=True)
    after = hashes()
    if before != after:
        raise RuntimeError("measured code changed during benchmark")
    def summarize(records):
        result = []
        for core in args.cores:
            for case in dict.fromkeys(r["case"] for r in records):
                subset = [r for r in records if r["core_order"] == core and r["case"] == case]
                if any(r["counts"] != subset[0]["counts"] for r in subset):
                    raise RuntimeError("nondeterministic generation counts")
                summary = {"core_order": core, "case": case, "counts": subset[0]["counts"]}
                for name in ("coordinate_visit_order_one_based", "decision_caches"):
                    if name in subset[0]:
                        summary[name] = subset[0][name]
                metrics = {"external_process_wall_seconds": lambda r: r["external_process_wall_seconds"],
                           "process_peak_rss_kib": lambda r: r.get("process_peak_rss_kib", r.get("process_peak_rss_kib_observed_after_search"))}
                if "timing_seconds" in subset[0]:
                    for name in ("preprocessing", "search", "total_in_process"):
                        metrics[name + "_seconds"] = lambda r, name=name: r["timing_seconds"][name]
                else:
                    metrics["total_in_process_seconds"] = lambda r: r["elapsed_seconds"]
                for name, getter in metrics.items():
                    values = [getter(r) for r in subset]
                    summary[name] = {"median": statistics.median(values), "min": min(values), "max": max(values)}
                result.append(summary)
        return result
    cpu = next((line.split(":", 1)[1].strip() for line in Path("/proc/cpuinfo").read_text().splitlines()
                if line.startswith("model name")), "unknown")
    result = {"protocol": "sequential fresh Linux processes; rotated case order; all preparation charged; external wall includes imports/startup/JSON; RSS observed immediately after search, includes interpreter/preparation/caches and excludes later output serialization peak; no overlapping benchmark workers",
              "repetitions": args.repeats, "cores": args.cores, "python": platform.python_version(),
              "platform": platform.platform(), "cpu_model": cpu, "logical_cpus_visible": os.cpu_count(),
              "source_sha256_before": before, "source_sha256_after": after,
              "measured_sources_unchanged": True, "all_exact_tuple_lists_match_independent_unpruned_baseline": True,
              "single_comparator_scope": "eligible row generation only; round2 preparation also builds full row profiles for later pair search, prefix comparators do not; these are not equal-work quadruple runtimes",
              "summary": summarize(runs), "raw_runs": runs,
              "single_generation_summary": summarize(singles), "single_generation_raw_runs": singles}
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
