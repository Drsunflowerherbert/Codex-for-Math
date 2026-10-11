"""Independent arithmetic/data audit. Standard library only; no repository imports.

This script reads certificates as data and proves nothing about universal validity.
An independently implemented final-pair enumeration cross-checks completeness for
the stated finite cases using (A*a-B)*(A*b-B)=B**2.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parents[1] / "egyptian-fractions"

def require(condition, detail):
    if not condition:
        raise ValueError(detail)

def total(values):
    return sum((Fraction(1, d) for d in values), Fraction())

def positive_ints(values):
    return all(type(d) is int and d > 0 for d in values)

def independent_expansions(value, length, lower=2):
    """Enumerate via strict prefix bounds and divisor pairs for the final two terms."""
    A, B = value.numerator, value.denominator
    require(A > 0 and length >= 1 and lower >= 1, "invalid enumeration state")
    if length == 1:
        if A == 1 and B >= lower:
            yield (B,)
        return
    if length == 2:
        # For a<b, u=A*a-B and v=A*b-B satisfy 0<u<B<v and uv=B**2.
        for u in range(1, B):
            if B * B % u:
                continue
            v = B * B // u
            if (u + B) % A or (v + B) % A:
                continue
            a, b = (u + B) // A, (v + B) // A
            if lower <= a < b:
                yield (a, b)
        return
    # Positive tails force d>1/value; strict increase forces value<length/d.
    for d in range(max(lower, B // A + 1), (length * B - 1) // A + 1):
        remainder = value - Fraction(1, d)
        for tail in independent_expansions(remainder, length - 1, d + 1):
            yield (d,) + tail

def main():
    cert = json.loads((SOURCE / "exact-examples.json").read_text())
    records = json.loads((SOURCE / "theorem-records.json").read_text())
    author = json.loads((SOURCE / "author-checks.json").read_text())
    hashes = {name: sha256((SOURCE / name).read_bytes()).hexdigest()
              for name in author["files_sha256"]}
    require(hashes == author["files_sha256"], "author manifest hash mismatch")
    require([r["id"] for r in records] == [f"EGY-{i:03}" for i in range(1, 7)],
            "unexpected theorem IDs")
    require(all(r["source_revision"] == cert["source_revision"] for r in records),
            "source revision mismatch")
    require((ROOT / "rerun/exact-examples.json").read_bytes()
            == (SOURCE / "exact-examples.json").read_bytes(), "rerun differs")
    require((ROOT / "rerun/check_examples.py").read_bytes()
            == (SOURCE / "check_examples.py").read_bytes(), "rerun script differs")

    cleanup_steps = Counter()
    maximum_steps = 0
    expected_cleanup = {(d,) * k for d in range(3, 13)
                        for k in range(2, min(5, d - 1) + 1)}
    seen_cleanup = set()
    for i, case in enumerate(cert["cleanup_cases"]):
        values = sorted(case["input"])
        require(positive_ints(values), ("cleanup input type", i))
        require(tuple(values) not in seen_cleanup, ("duplicate cleanup input", i))
        seen_cleanup.add(tuple(values))
        value = total(values)
        require(0 < value < 1 and str(value) == case["sum"], ("cleanup sum", i))
        for j, step in enumerate(case["steps"]):
            d = step["repeated_denominator"]
            require(values.count(d) >= 2, ("missing repeated denominator", i, j))
            p = d // 2
            replacement = ([p + 1, p * (p + 1)] if d % 2 == 0
                           else [p + 1, (p + 1) * d])
            increase = (p - 1) ** 2 if d % 2 == 0 else 2 * p * p
            require(step["replacement"] == replacement and increase > 0,
                    ("replacement or increase", i, j))
            require(step["denominator_sum_increase"] == increase,
                    ("recorded statistic", i, j))
            previous_sum = sum(values)
            previous_length = len(values)
            values.remove(d)
            values.remove(d)
            values = sorted(values + replacement)
            require(len(values) == previous_length and total(values) == value
                    and sum(values) - previous_sum == increase and min(values) >= 2,
                    ("cleanup invariant", i, j))
            cleanup_steps["even" if d % 2 == 0 else "odd"] += 1
        require(values == case["output"] and len(set(values)) == len(values),
                ("cleanup final output", i))
        require(case["exact_checks_passed"] is True, ("cleanup status", i))
        maximum_steps = max(maximum_steps, len(case["steps"]))
    require(seen_cleanup == expected_cleanup, "cleanup input coverage")

    inputs_by_length = defaultdict(set)
    markers_by_input = defaultdict(list)
    branches = Counter()
    def check_padding(case, where):
        values, out = case["input"], case["output"]
        marker, split = case["marker"], case["split_denominator"]
        repl = case["replacement"]
        require(positive_ints(values) and values == sorted(set(values))
                and len(values) >= 3 and total(values) == 1 and marker in values,
                ("padding input", where))
        require(positive_ints(out) and out == sorted(set(out))
                and len(out) == len(values) + 1 and total(out) == 1 and marker in out,
                ("padding output", where))
        require(split != marker and split in values
                and len(repl) == 2 and total(repl) == Fraction(1, split),
                ("padding split", where))
        require(out == sorted([d for d in values if d != split] + repl),
                ("padding reconstruction", where))
        require(case["exact_checks_passed"] is True, ("padding status", where))
        if marker != values[-1]:
            require(split == values[-1] and repl == [split + 1, split * (split + 1)],
                    ("unmarked maximum split", where))
            return "split_unmarked_maximum"
        require(split == values[-2], ("marked maximum split", where))
        if marker not in [split + 1, split * (split + 1)]:
            require(repl == [split + 1, split * (split + 1)], ("ordinary split", where))
            return "split_second_largest_without_collision"
        a = repl[0] - split
        require(a >= 2 and split % a == 0, ("composite factor", where))
        b = split // a
        require(b >= 2 and repl == [split + a, b * (split + a)]
                and split + 1 < repl[0] < repl[1] < split * (split + 1),
                ("composite collision repair", where))
        return "composite_collision"

    for i, case in enumerate(cert["padding_cases"]):
        branches[check_padding(case, i)] += 1
        ds = tuple(case["input"])
        inputs_by_length[len(ds)].add(ds)
        markers_by_input[ds].append(case["marker"])
    for ds, markers in markers_by_input.items():
        require(sorted(markers) == list(ds), ("each marker exactly once", ds))
    independent_counts = {}
    for length in range(3, 7):
        enumerated_list = list(independent_expansions(Fraction(1), length))
        enumerated = set(enumerated_list)
        require(len(enumerated) == len(enumerated_list), ("enumeration uniqueness", length))
        require(all(len(ds) == length and total(ds) == 1
                    and list(ds) == sorted(set(ds)) for ds in enumerated),
                ("independent enumerator soundness", length))
        require(enumerated == inputs_by_length[length], ("enumeration set mismatch", length))
        require(len(enumerated) == cert["enumeration_counts"][str(length)],
                ("declared enumeration count", length))
        independent_counts[str(length)] = len(enumerated)
    exceptional_branches = Counter()
    for i, case in enumerate(cert["exceptional_composite_cases"]):
        exceptional_branches[check_padding(case, ("exception", i))] += 1
    require(exceptional_branches == {"composite_collision": 1}, "special case coverage")
    require(branches["composite_collision"] == 0, "unexpected short exceptional case")

    # Direct exact checks of the two small counterexamples' arithmetic.
    require(total([2, 2]) == 1 and total([2, 3]) < 1, "closed endpoint arithmetic")
    require(Fraction(2, 3) - Fraction(1, 3) == Fraction(1, 3), "marker obstruction arithmetic")
    result = {
        "scope": "Independent ordinary proof review plus exact finite arithmetic/data audit; no Lean",
        "source_revision": cert["source_revision"],
        "original_hashes_match_author_manifest": True,
        "rerun_script_byte_identical": True,
        "rerun_output_byte_identical": True,
        "cleanup_cases": len(seen_cleanup),
        "cleanup_steps_by_parity": dict(cleanup_steps),
        "maximum_cleanup_steps": maximum_steps,
        "independent_enumeration_counts": independent_counts,
        "independent_enumeration_sets_equal_certificate_inputs": True,
        "padding_cases": len(cert["padding_cases"]),
        "each_input_marker_checked_exactly_once": True,
        "ordinary_padding_branches": dict(branches),
        "separate_exceptional_branches": dict(exceptional_branches),
        "all_checks_passed": True,
        "python_version": sys.version,
        "python_optimization_level": sys.flags.optimize,
        "source_sha256": hashes,
    }
    (ROOT / "independent-audit-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
