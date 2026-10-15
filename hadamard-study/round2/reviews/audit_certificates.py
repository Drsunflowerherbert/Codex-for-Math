#!/usr/bin/env python3
"""Independently check rejection examples and every retained Hadamard array."""

import argparse
import json
from pathlib import Path

from independent_reductions import direct_energy, integer_probes, residue_energy, sequence


def verify_matrix(m, masks):
    seqs=[sequence(m,a) for a in masks]
    pattern=(((0,1),(1,1),(2,1),(3,1)),((1,-1),(0,1),(3,-1),(2,1)),
             ((2,-1),(3,1),(0,1),(1,-1)),((3,-1),(2,-1),(1,1),(0,1)))
    rows=[[sign*seqs[b][(j-i)%m] for b,sign in blockrow for j in range(m)]
          for blockrow in pattern for i in range(m)]
    checks=0
    for i,left in enumerate(rows):
        if sum(x*x for x in left)!=4*m:
            raise ValueError("row norm mismatch")
        for right in rows[:i]:
            if sum(a*b for a,b in zip(left,right)):
                raise ValueError(("nonorthogonal output array",m,masks))
            checks+=1
    return checks


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    records=json.loads(args.data.read_text())["results"]
    results=[]
    certificates=0
    for record in records:
        m=record["core_order"]
        square_set={t*t for t in range(1,m+1,2)}
        two={a+b for a in square_set for b in square_set}
        three={a+b+c for a in square_set for b in square_set for c in square_set}
        probes=dict(integer_probes(m))
        examples=0
        for field,pair in (("single_rejection_examples",False),("pair_rejection_examples",True)):
            for kind,example in record[field].items():
                masks=example["masks"] if pair else [example["mask"]]
                seqs=[sequence(m,a) for a in masks]
                if kind=="row":
                    residual=4*m-sum(sum(x)**2 for x in seqs)
                    allowed=two if pair else three
                    if residual != example["remaining_square_sum"] or residual in allowed:
                        raise ValueError(("invalid arithmetic rejection certificate",m,example))
                elif kind=="order3":
                    if m%3:
                        raise ValueError("order-three certificate at ineligible order")
                    energy=sum(residue_energy(x) for x in seqs)
                    if energy != example["energy"] or example["bound"]!=4*m or energy<=4*m:
                        raise ValueError(("invalid order-three rejection certificate",m,example))
                elif kind=="integer_probe":
                    v=tuple(example["integer_vector"])
                    if v!=probes[example["frequency_label"]]:
                        raise ValueError("rejection vector differs from specified probe bank")
                    energy=sum(direct_energy(x,v) for x in seqs)
                    bound=4*m*sum(t*t for t in v)
                    if energy!=example["energy"] or bound!=example["bound"] or energy<=bound:
                        raise ValueError(("invalid integer-energy rejection certificate",m,example))
                else:
                    raise ValueError("unknown rejection certificate type")
                certificates+=1
                examples+=1
        checks=sum(verify_matrix(m,q) for q in record["solutions"])
        if checks!=record["matrix_row_pairs_checked"]:
            raise ValueError("reported matrix-pair count mismatch")
        results.append({"core_order":m,"output_arrays_checked":len(record["solutions"]),
                        "direct_integer_row_pairs_checked":checks,
                        "rejection_certificates_checked":examples})
    output={"status":"passed","method":"independent sequence decoding, explicit matrix dot products, direct convolution energy and arithmetic certificate reconstruction; no study-module imports",
            "output_arrays_checked":sum(r["output_arrays_checked"] for r in results),
            "direct_integer_row_pairs_checked":sum(r["direct_integer_row_pairs_checked"] for r in results),
            "rejection_certificates_checked":certificates,"results":results}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in output.items() if k not in ("results","method")}))


if __name__ == "__main__":
    main()
