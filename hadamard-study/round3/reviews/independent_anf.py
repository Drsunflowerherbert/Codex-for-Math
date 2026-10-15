#!/usr/bin/env python3
"""Independent Boolean ANF phase identities and cancellation-safe relaxations."""

import argparse
from collections import defaultdict
import json
from pathlib import Path

from independent_prefix import row_targets
from independent_structure import decode_tuple, edges_by_lag, forced_signs, rgs


ONE=frozenset({0})
ZERO=frozenset()


def multiply(a,b):
    out=set()
    for x in a:
        for y in b:
            z=x|y  # Boolean variables are idempotent.
            if z in out:
                out.remove(z)
            else:
                out.add(z)
    return frozenset(out)


def bit_poly(prefix,j,b):
    if j<len(prefix) and prefix[j]>=0:
        return ONE if prefix[j]>>b&1 else ZERO
    return frozenset({1<<(2*j+b)})


def exponent_polys(prefix,h,edges):
    polys=[]
    for lag in edges:
        out=ONE
        for u,v in lag:
            a=ONE ^ bit_poly(prefix,u,0) ^ bit_poly(prefix,v,0)
            b=ONE ^ bit_poly(prefix,u,1) ^ bit_poly(prefix,v,1)
            out=out ^ multiply(a,b)
        polys.append(out)
    return polys


def phase(poly):
    return (-1 if 0 in poly else 1),poly-{0}


def evaluate(poly,colors):
    ones=sum(((color>>b)&1)<<(2*j+b) for j,color in enumerate(colors) for b in range(2))
    return sum(monomial & ones == monomial for monomial in poly)%2


def reachable_row_sets(prefix,polys):
    grouped=defaultdict(lambda:[0]*4)
    for j,c in enumerate(prefix):
        sign,residual=phase(polys[j])
        grouped[residual][c]+=sign
    fixed=grouped.pop(ZERO,[0]*4)
    sets=[]
    for c in range(4):
        possible={fixed[c]}
        for coefficients in grouped.values():
            value=coefficients[c]
            possible={x+y for x in possible for y in (-value,value)}
        sets.append(possible)
    return sets


def row_possible(prefix,h,polys,targets):
    sets=reachable_row_sets(prefix,polys)
    distance=min(sum(min(abs(u-v) for v in possible) for u,possible in zip(target,sets)) for target in targets)
    return distance<=h-len(prefix)


def lag_possible(prefix,polys,edges):
    k=len(prefix)
    for t,lag in enumerate(edges):
        grouped=defaultdict(int)
        sign,residual=phase(polys[t])
        grouped[residual]+=sign
        unknown=[]
        for u,v in lag:
            sign,residual=phase(polys[u]^polys[v])
            if u<k and v<k:
                if prefix[u]==prefix[v]:
                    grouped[residual]+=2*sign
            else:
                unknown.append((0,2*sign) if not residual else (-2,0,2))
        fixed=1+grouped.pop(ZERO,0)
        possible={fixed}
        for value in grouped.values():
            possible={x+y for x in possible for y in (-value,value)}
        for values in unknown:
            possible={x+y for x in possible for y in values}
        if 0 not in possible:
            return False
    return True


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    study=Path(__file__).resolve().parents[2]
    baseline=json.loads((study/"round3/reviews/structure-independent.json").read_text())
    identity_checks=0
    valid_prefix_checks=0
    opposite_constant_example=None
    results=[]
    for record in baseline["results"]:
        m=record["core_order"]
        h=m//2
        edges=edges_by_lag(m)
        targets=row_targets(h)
        if m<=15:
            polynomials={}
            for colors in rgs(h):
                signs=forced_signs(colors,edges)
                for k in range(h+1):
                    polys=polynomials.setdefault(colors[:k],exponent_polys(colors[:k],h,edges))
                    for p,s in zip(polys,signs):
                        if (-1 if evaluate(p,colors) else 1)!=s:
                            raise ValueError(("ANF sign identity mismatch",m,colors,k))
                        identity_checks+=1
        for q in record["solutions"]:
            colors,signs=decode_tuple(m,q)
            for k in range(h+1):
                prefix=colors[:k]
                polys=exponent_polys(prefix,h,edges)
                if not row_possible(prefix,h,polys,targets) or not lag_possible(prefix,polys,edges):
                    raise ValueError(("ANF relaxation false negative",m,q,k))
                valid_prefix_checks+=1
                if opposite_constant_example is None:
                    for i in range(k):
                        for j in range(i):
                            a,p=phase(polys[i]);b,r=phase(polys[j])
                            if p and p==r and a==-b and prefix[i]==prefix[j]:
                                opposite_constant_example={"core_order":m,"valid_tuple":q,"prefix_colors":list(prefix),"vertices":[j+1,i+1],"same_residual_monomial_masks":sorted(p),"constant_signs":[b,a],"exact_sum_of_these_two_signs":0}
                                break
        results.append({"core_order":m,"valid_solution_prefixes_preserved":True})
    output={"status":"passed","method":"independent idempotent-monomial Boolean polynomial algebra; shared phase coefficients grouped before independent-phase relaxation; no subject imports",
            "ANF_identity_checks_over_all_small_color_completions_and_prefixes":identity_checks,
            "all_valid_solution_prefixes_preserved":valid_prefix_checks,
            "opposite_constant_sign_grouping_example":opposite_constant_example,
            "results":results}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in output.items() if k not in ("results","method")}))


if __name__ == "__main__":
    main()
