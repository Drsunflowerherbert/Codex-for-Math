#!/usr/bin/env python3
"""Independent exact audit; does not import or execute the study's verifier.

Counts via carry-free positional polynomial encoding, unlike the study's cyclic
convolution recurrence. Only original standard-library code is executed.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json
import time

BASE = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
STUDY = BASE / 'finite-field-mixing'
CERT = json.loads((STUDY / 'certificates.json').read_text())


def polynomial_counts(p, pairs, k):
    """Compute F(z)^k modulo z^p-1 by exact carry-free integer packing."""
    q = [0] * p
    for a, b in pairs:
        q[a * b % p] += 1
    total = len(pairs)**k
    width = total.bit_length()
    mask = (1 << width) - 1
    encoded = sum(c << (j * width) for j, c in enumerate(q))**k
    out = [0] * p
    degree = 0
    while encoded:
        out[degree % p] += encoded & mask
        degree += 1
        encoded >>= width
    assert sum(out) == total
    return out


def varying_counts(p, factors, coefficients, shift):
    """Independent ordinary-polynomial product with nonzero coefficients/shift."""
    M = 1
    qs = []
    for (A, B), c in zip(factors, coefficients):
        assert c % p
        M *= len(A) * len(B)
        q = [0] * p
        for a in A:
            for b in B:
                q[c * a * b % p] += 1
        qs.append(q)
    width = M.bit_length()
    encoded = 1
    for q in qs:
        encoded *= sum(c << (j * width) for j, c in enumerate(q))
    out = [0] * p
    mask = (1 << width) - 1
    degree = shift
    while encoded:
        out[degree % p] += encoded & mask
        degree += 1
        encoded >>= width
    assert sum(out) == M
    return out, M


def subsets(p):
    return [tuple(x for x in range(p) if mask >> x & 1)
            for mask in range(1, 1 << p)]


def bound(p, counts, M, k):
    assert sum(counts) == M
    assert all((p*c-M)**2 <= (p-1)**2 * p**k * M for c in counts)
    if M > (p-1)**2 * p**k:
        assert min(counts) > 0


def diagonal(p):
    guarantees = [0]*6
    unneeded = [0]*6
    minima = {}
    dense_count = 0
    dense_prob = None
    for H in subsets(p):
        h = len(H)
        N = h*h
        pairs = list(product(H, repeat=2))
        for k in range(1, 7):
            counts = polynomial_counts(p, pairs, k)
            bound(p, counts, N**k, k)
            good = N**k > (p-1)**2 * p**k
            guarantees[k-1] += good
            unneeded[k-1] += not good and min(counts)>0
            if k == 4:
                old = minima.get(str(h))
                if old is None or min(counts) < old['minimum_count']:
                    minima[str(h)] = {'minimum_count':min(counts),'witness_H':list(H),
                                      'first_minimum_residue':counts.index(min(counts))}
                if h**4 >= p**3:
                    dense_count += 1
                    assert p*p*min(counts) >= N**4
                    value = Fraction(min(counts), N**4)
                    dense_prob = min(dense_prob, value) if dense_prob is not None else value
    row = next(r for r in CERT['diagonal_exhaustive'] if r['p']==p)
    assert guarantees == row['guaranteed_sets_by_k']
    assert unneeded == row['covering_sets_failing_sufficient_criterion_by_k']
    assert minima == row['four_product_minima_by_size']
    assert dense_count == row['dense_four_sets_checked']
    assert str(dense_prob) == row['dense_four_minimum_probability']
    threshold = next(h for h in range(1,p+1) if h**4>=p**3)
    assert threshold == row['minimum_h_with_h4_ge_p3']
    assert dense_count == sum(comb(p,h) for h in range(threshold,p+1))
    return {'p':p,'sets':2**p-1,'k_values':list(range(1,7)),
            'all_aggregate_fields_match':True,'dense_sets':dense_count,
            'dense_minimum_probability':str(dense_prob)}


def rectangular(p):
    checked=0
    guarantees=[0]*6
    for A in subsets(p):
        for B in subsets(p):
            pairs=list(product(A,B))
            N=len(pairs)
            checked+=1
            for k in range(1,7):
                counts=polynomial_counts(p,pairs,k)
                bound(p,counts,N**k,k)
                guarantees[k-1]+=N**k>(p-1)**2*p**k
                if k==4 and N*N>=p**3:
                    assert p*p*min(counts)>=N**4
    row=next(r for r in CERT['rectangular_exhaustive'] if r['p']==p)
    assert guarantees==row['guaranteed_pairs_by_k']
    assert checked==row['ordered_nonempty_set_pairs_checked']
    return {'p':p,'ordered_pairs':checked,'all_aggregate_fields_match':True}


def heterogeneous():
    p=3
    sets=subsets(p)
    pairs=list(product(sets,repeat=2))
    result=[]
    for k in [2,3]:
        checked=guaranteed=0
        for factors in product(pairs,repeat=k):
            # Nontrivial alternating coefficients and a nonzero shift exercise
            # a part of FF005 not explicitly sampled in the main certificate.
            counts,M=varying_counts(p,factors,[1+(j%2) for j in range(k)],1)
            bound(p,counts,M,k)
            guaranteed+=M>(p-1)**2*p**k
            checked+=1
        row=next(r for r in CERT['heterogeneous_exhaustive'] if r['number_of_pairs']==k)
        assert guaranteed==row['guaranteed_sequences']
        assert checked==row['sequences_checked']
        result.append({'p':p,'k':k,'ordered_sequences':checked,'nonzero_shift':1,
                       'coefficients':[1+(j%2) for j in range(k)],'checks_passed':True})
    return result


def direct_examples():
    rows=[]
    for row in CERT['independent_direct_enumeration']:
        A,B,p,k=row['A'],row['B'],row['p'],row['k']
        counts=[0]*p
        for flat in product(*([A,B]*k)):
            counts[sum(flat[i]*flat[i+1] for i in range(0,2*k,2))%p]+=1
        assert counts==row['counts']
        assert sum(counts)==row['tuples']
        rows.append({'p':p,'k':k,'counts':counts,'directly_enumerated_tuples':sum(counts)})
    return rows


def other_examples():
    ex=CERT['examples_and_counterexamples']
    for key in ['composite_modulus','strict_boundary_failure','criterion_not_necessary','small_set_can_fail']:
        row=ex[key]
        p=row.get('p',row.get('modulus'))
        A=row.get('A',row.get('H')); B=row.get('B',row.get('H'))
        assert polynomial_counts(p,list(product(A,B)),row['k'])==row['counts']
    row=ex['composite_modulus']
    assert len(row['H'])**4 == 16**3
    assert {4*a*b%16 for a in row['H'] for b in row['H']}=={0}
    row=ex['dependent_within_pairs']
    assert sorted(a for a,b in row['pairs'])==sorted(b for a,b in row['pairs'])==[1,2,3,4]
    assert {sum(a*b for a,b in t)%5 for t in product(row['pairs'],repeat=4)}=={4}
    assert {4*a*b%2 for a,b in product(range(2),repeat=2)}=={0}
    row=ex['nonuniform_full_support']
    weights=list(map(Fraction,row['marginal_weights']))
    probs=[sum(weights[a]*weights[b] for a,b in product(range(5),repeat=2) if a*b%5==t)
           for t in range(5)]
    assert probs==list(map(Fraction,row['product_weights']))
    assert probs[0]-probs[1]==Fraction(row['nontrivial_character_expectation'])==Fraction(79,80)
    assert (probs[0]-probs[1])**2>Fraction(1,5)
    row=ex['positive_divisor_lift']
    Q,p=row['P'],row['p']
    D=[d for d in range(1,Q+1) if Q%d==0]
    assert D==row['positive_divisors']
    assert sorted({d%p for d in D})==row['H']
    E=[a*b for a,b in row['factor_pairs']]
    assert E==row['numerators'] and all(Q*Q%e==0 for e in E)
    assert all(a in D and b in D for a,b in row['factor_pairs'])
    assert sum(E)==p*row['multiplier'] and row['multiplier']>0
    assert sum(Fraction(e,row['multiplier']) for e in E)==p
    return {'all_eight_recorded_examples_pass':True,'nonuniform_character_value':'79/80',
            'positive_divisor_lift':{'p':p,'Q':Q,'numerators':E,'denominator':row['multiplier']}}


def thresholds():
    for row in CERT['exact_threshold_table']:
        p=row['p']
        assert row['minimum_h_at_density_three_quarters']==next(h for h in range(1,p+1) if h**4>=p**3)
        for k in range(1,7):
            value=next((h for h in range(1,p+1) if h**(2*k)>(p-1)**2*p**k),None)
            assert value==row[f'minimum_h_for_{k}_product_criterion']
    return {'all_rows_match':True,'rows':len(CERT['exact_threshold_table'])}


def cyclotomic_identities():
    """Sparse group-ring verification of orthogonality and sum of squares."""
    def norm(q,p):
        out=Counter()
        for i,a in q.items():
            for j,b in q.items():
                out[(i-j)%p]+=a*b
        return out
    def increment(target,terms,scale):
        for j,c in terms.items():
            target[j]+=scale*c
    output=[]
    for p in [2,3,5]:
        for d in range(p):
            coeff=Counter(d*x%p for x in range(p))
            if d==0:
                assert coeff=={0:p}
            else:
                assert [coeff[j] for j in range(p)]==[1]*p
        checked=0
        for A in subsets(p):
            for B in subsets(p):
                for r in range(1,p):
                    T=[Counter(r*x*y%p for y in B) for x in range(p)]
                    S=Counter()
                    for x in A:
                        increment(S,T[x],1)
                    difference=Counter({0:p*len(A)*len(B)})
                    increment(difference,norm(S,p),-1)
                    for x in range(p):
                        if x not in A:
                            increment(difference,norm(T[x],p),-len(A))
                    for i,x in enumerate(A):
                        for y in A[i+1:]:
                            delta=Counter()
                            increment(delta,T[x],1)
                            increment(delta,T[y],-1)
                            increment(difference,norm(delta,p),-1)
                    # Degree < p and divisible by Phi_p iff all coefficients
                    # are equal, including missing (zero) coefficients.
                    assert len({difference[j] for j in range(p)})==1
                    checked+=1
        row=next(r for r in CERT['bilinear_sum_of_squares'] if r['p']==p)
        assert checked==row['identities_checked']
        output.append({'p':p,'identities_checked':checked,'all_identities_pass':True})
    return output


def coefficient_shift_examples():
    result=[]
    for row in CERT['nonzero_coefficients_and_shifts']:
        p,k=row['p'],row['k']
        checked=0
        for coefficients in product(range(1,p),repeat=k):
            for shift in range(p):
                counts,M=varying_counts(p,row['pairs'],coefficients,shift)
                bound(p,counts,M,k)
                assert M==row['total_tuples_per_case']
                checked+=1
        assert checked==row['all_nonzero_coefficient_vectors_and_shifts_checked']
        result.append({'p':p,'cases':checked,'all_checks_pass':True})
    return result


def main():
    start=time.monotonic()
    result={'status':'passed','independent_method':'carry-free integer encoding of ordinary polynomial products, folded modulo z^p-1',
            'imports_study_verifier':False,'downloaded_code_executed':False,
            'diagonal':[],'rectangular':[]}
    for p in [2,3,5,7,11,13,17]:
        result['diagonal'].append(diagonal(p))
        print(f'diagonal p={p} passed',flush=True)
    for p in [2,3,5,7]:
        result['rectangular'].append(rectangular(p))
        print(f'rectangular p={p} passed',flush=True)
    result['heterogeneous']=heterogeneous()
    result['direct_examples']=direct_examples()
    result['examples']=other_examples()
    result['thresholds']=thresholds()
    result['cyclotomic_identities']=cyclotomic_identities()
    result['coefficient_shift_examples']=coefficient_shift_examples()
    source=BASE/'catalog/sources/preprints_Short-Egyptian-fractions-September-25-2026_build_prescribed.tex'
    manifest=json.loads((BASE/'catalog/source_manifest.json').read_text())
    expected=next(r['sha256'] for r in manifest['files'] if r['file']==source.name)
    assert expected==sha256(source.read_bytes()).hexdigest()==CERT['source_sha256']
    assert sha256((STUDY/'verify.py').read_bytes()).hexdigest()==CERT['program_sha256']
    result['source_sha256']=expected
    result['study_program_hash_matches_certificate']=True
    result['review_program_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    result['reviewed_certificate_sha256']=sha256((STUDY/'certificates.json').read_bytes()).hexdigest()
    result['elapsed_seconds']=round(time.monotonic()-start,3)
    result['scope']={'universal_result':'ordinary proof audit, not established by enumeration',
                     'lean_compilation':False,'global_Egyptian_fraction_constant_audited':False}
    (OUT/'independent-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','elapsed_seconds':result['elapsed_seconds']}),flush=True)

if __name__=='__main__':
    main()
