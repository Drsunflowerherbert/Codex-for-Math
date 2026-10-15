#!/usr/bin/env python3
"""Independent exact checks of reduction criteria and adversarial edge cases."""

import argparse
import importlib.util
from itertools import combinations, combinations_with_replacement
import json
from math import gcd
from pathlib import Path


def sequence(m, mask):
    return tuple(1 if j == 0 else 1 - 2 * ((mask >> (min(j, m-j)-1)) & 1)
                 for j in range(m))


def full_paf(x):
    return tuple(sum(x[j] * x[(j+t) % len(x)] for j in range(len(x)))
                 for t in range(1, len(x)))


def integer_probes(m):
    probes = []
    for f in range(1, m//2+1):
        t = [m - 4 * min(f*j % m, m - f*j % m) for j in range(m)]
        total = sum(t)
        v = tuple(m*value-total for value in t)
        if any(v):
            probes.append((f, v))
    return probes


def direct_energy(x, v):
    m = len(x)
    return sum(sum(x[(j-i) % m] * v[j] for j in range(m))**2 for i in range(m))


def residue_energy(x):
    sums = [sum(x[j] for j in range(r, len(x), 3)) for r in range(3)]
    if sums[1] != sums[2]:
        raise ValueError("residue sums violate symmetry")
    expanded = sum(s*s for s in sums) - sum(sums[i]*sums[j] for i,j in combinations(range(3),2))
    if expanded != (sums[0]-sums[1])**2:
        raise ValueError("order-three energy formula mismatch")
    return expanded


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    study = Path(__file__).resolve().parents[2]
    baseline_path = study / "reviews/williamson-independent.json"
    baseline = json.loads(baseline_path.read_text())
    spec = importlib.util.spec_from_file_location("round2_subject", study / "round2/scripts/search.py")
    subject = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(subject)
    results = []
    symmetry_checks = 0
    probe_formula_checks = 0
    for record in baseline["results"]:
        m = record["core_order"]
        masks = range(1 << (m//2))
        seqs = [sequence(m, a) for a in masks]
        pafs = [full_paf(x) for x in seqs]
        squares = [sum(x)**2 for x in seqs]
        possible_squares = set(squares)
        two = {a+b for a in possible_squares for b in possible_squares}
        three = {a+b+c for a in possible_squares for b in possible_squares for c in possible_squares}
        probes = integer_probes(m)
        limits = [4*m*sum(t*t for t in v) for _,v in probes]
        energies = []
        for a,x in enumerate(seqs):
            scores = []
            for _,v in probes:
                direct = direct_energy(x,v)
                vpaf = full_paf(v)
                formula = m*sum(t*t for t in v) + sum(r*s for r,s in zip(pafs[a],vpaf))
                if direct != formula or direct < 0:
                    raise ValueError(("integer-probe energy identity",m,a))
                probe_formula_checks += 1
                scores.append(direct)
            energies.append(scores)
        after_row = [a for a in masks if 4*m-squares[a] in three]
        after_order3 = [a for a in after_row if m%3 or residue_energy(seqs[a]) <= 4*m]
        after_probes = [a for a in after_order3 if all(e<=bound for e,bound in zip(energies[a],limits))]
        prepared = subject.Prepared(m, True)
        if prepared.masks != after_probes:
            raise ValueError(("single-filter survivor mismatch",m))
        for a,b in combinations_with_replacement(after_probes,2):
            expected = 0
            if 4*m-squares[a]-squares[b] not in two:
                expected = 1
            elif m%3 == 0 and residue_energy(seqs[a])+residue_energy(seqs[b]) > 4*m:
                expected = 2
            elif any(x+y>bound for x,y,bound in zip(energies[a],energies[b],limits)):
                expected = 3
            if prepared.pair_rejection(a,b) != expected:
                raise ValueError(("pair-filter mismatch",m,a,b))
        expected_tuples = [tuple(q) for q in record["solving_sequence_index_multisets"]]
        for q in expected_tuples:
            if (q[0]^q[1]^q[2]^q[3]) != (1 << (m//2))-1:
                raise ValueError(("product theorem false negative",m,q))
            if any(sum(pafs[a][t] for a in q) for t in range(m-1)):
                raise ValueError(("first-edition record fails full PAF",m,q))
            if sum(squares[a] for a in q) != 4*m:
                raise ValueError(("row-square identity",m,q))
            if any(a not in after_probes for a in q):
                raise ValueError(("single-filter false negative",m,q))
            if any(prepared.pair_rejection(q[i],q[j]) for i,j in combinations(range(4),2)):
                raise ValueError(("pair-filter false negative",m,q))
            if m%3 == 0 and sum(residue_energy(seqs[a]) for a in q) != 4*m:
                raise ValueError(("order-three total energy",m,q))
            for u in range(1,m+1):
                if gcd(u,m) != 1:
                    continue
                transformed=[]
                for a in q:
                    transformed.append(sum((seqs[a][u*j % m] == -1) << (j-1) for j in range(1,m//2+1)))
                if tuple(sorted(transformed)) not in expected_tuples:
                    raise ValueError(("unit-multiplier closure",m,q,u))
                symmetry_checks += 1
        method_counts = {}
        for method in ("baseline-mitm","filtered-mitm","filtered-mitm-product-key","product-triples"):
            actual = subject.run(m,method)
            if [tuple(q) for q in actual["solutions"]] != expected_tuples:
                raise ValueError(("exact tuple-set mismatch",m,method))
            method_counts[method] = actual["counts"]
        joined = [method_counts[name]["joined_pair_combinations_before_sorted_order_test"]
                  for name in ("baseline-mitm","filtered-mitm","filtered-mitm-product-key")]
        if len(set(joined)) != 1:
            raise ValueError(("redundant full-PAF/product-key join count differs",m,joined))
        for filters in ("row","row-order3","all"):
            ablation=subject.Prepared(m,True,filters=filters)
            if subject.pair_search(ablation)[0] != expected_tuples:
                raise ValueError(("filter-ablation exact tuple-set mismatch",m,filters))
        results.append({"core_order":m,"solutions":len(expected_tuples),
                        "raw_sequences":len(seqs),"after_row":len(after_row),
                        "after_order3":len(after_order3),"after_integer_probes":len(after_probes),
                        "exact_solution_sets_match_all_four_methods":True,
                        "exact_solution_sets_match_all_three_filter_ablations":True,
                        "join_count_all_three_MITM_methods":joined[0]})
    q=(7,11,13,14)
    e3=[residue_energy(sequence(9,a)) for a in q]
    if e3 != [0,36,0,0]:
        raise ValueError("equality fixture changed")
    probe3=dict(integer_probes(9))[3]
    norm=sum(x*x for x in probe3)
    if direct_energy(sequence(9,11),probe3) != 36*norm:
        raise ValueError("integer-probe equality fixture failed")
    if subject.probe_score((0,),1,0,(0,)) != 0:
        raise ValueError("zero-vector score mishandled")
    if (0^1^1^1) == 0:
        raise ValueError("wrong-product-target negative control failed")
    p5=subject.Prepared(5,True)
    ranks={mask:rank for rank,mask in enumerate(p5.masks)}
    rank_xor=ranks[1]^ranks[2]^ranks[3]^ranks[3]
    if rank_xor == p5.full_mask:
        raise ValueError("filtered-rank negative control did not distinguish masks")
    square_set3={sum(sequence(3,a))**2 for a in range(2)}
    remainder3=12-sum(sequence(3,0))**2-sum(sequence(3,1))**2
    if remainder3 != 2 or remainder3 in {a+b for a,b in combinations(square_set3,2)}:
        raise ValueError("no-repetition negative control failed")
    if sum(sequence(3,1)) >= 0:
        raise ValueError("signed-row-sum negative control failed")
    abs_rows3=[abs(sum(sequence(3,a))) for a in (0,1,1,1)]
    if abs_rows3 == sorted(abs_rows3):
        raise ValueError("second simultaneous sorting negative control failed")
    triple7=[sequence(7,a) for a in (1,2,4)]
    triple_gram=[[sum(sum(x[(k-i)%7]*x[(k-j)%7] for k in range(7))
                      for x in triple7) for j in range(7)] for i in range(7)]
    if triple_gram != [[20*(i==j)+1 for j in range(7)] for i in range(7)]:
        raise ValueError("full-PSD/no-completion counterexample Gram mismatch")
    if (7^1^2^4) != 0 or 28-sum(sum(x)**2 for x in triple7) != 1:
        raise ValueError("full-PSD/no-completion product/row mismatch")
    output={"status":"passed","baseline":str(baseline_path),
            "baseline_domain":"all first-edition raw sorted normalized symmetric multisets, odd m<=15",
            "total_original_solutions":sum(r["solutions"] for r in results),
            "integer_probe_formula_checks_against_direct_convolution":probe_formula_checks,
            "unit_multiplier_solution_closure_checks":symmetry_checks,
            "adversarial_cases":{
                "m1_empty_profiles_and_probe_pool":"passed",
                "m9_tuple_7_11_13_14_order3_energies":e3,
                "m9_mask11_frequency3_integer_probe_at_exact_threshold":"retained",
                "zero_energy_and_zero_test_vector":"retained",
                "m3_repeated_blocks_and_remaining_square_1_plus_1":"retained",
                "m3_wrong_XOR_target_zero":"would reject valid tuple (0,1,1,1)",
                "m5_filtered_rank_XOR":"would reject valid original tuple (1,2,3,3)",
                "positive_signed_row_sum_only":"would reject m3 normalized negative-row-sum blocks",
                "simultaneous_mask_order_and_absolute_row_sum_order":"would reject valid m3 tuple",
                "m7_full_PSD_but_no_completion":{"masks":[1,2,4],"sum_Gram":"20 I + J","residual":"8 I - J; eigenvalues 1,8","forced_fourth_mask":0,"required_remaining_row_square":1,"forced_fourth_row_square":49}},
            "results":results}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":"passed","solutions":output["total_original_solutions"],"probe_identity_checks":probe_formula_checks,"symmetry_checks":symmetry_checks}))


if __name__ == "__main__":
    main()
