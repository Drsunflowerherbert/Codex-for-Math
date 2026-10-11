#!/usr/bin/env python3
"""Original exact arithmetic checks for the mixed-moment study.

Uses only Python's standard library. No network, third-party source code,
external executables, floating point, or substitutions for G or zeta(2).
A triple (a,b,c) denotes a + b*G + c*zeta(2) formally. The checks are
finite algebraic certificates, not proofs of integrability or infinite sums.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'catalog' / 'sources' / ('preprints_Catalans-constant-is-irrational-September-24-2026_build_sections_foundations.tex')
REVISION = 'fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb'
ZERO = (F(0), F(0), F(0))
COUNTS = {}


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    COUNTS[name] = COUNTS.get(name, 0) + 1


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(q, a):
    return tuple(F(q) * x for x in a)


def sub(a, b):
    return add(a, scale(-1, b))


@lru_cache(None)
def c(r):
    if r < 0:
        return F(0)
    return F(comb(2*r, r), 4**r)


def kernel(n):
    """c_(n/2), zero for negative or odd integers n."""
    return c(n // 2) if n >= 0 and n % 2 == 0 else F(0)


@lru_cache(None)
def m(i):
    if i == -1:
        return F(0)  # Only this negative index is an allowed convention.
    if i < -1:
        raise ValueError('Undefined moment index')
    return F(0) if i % 2 else F(2, 1) / ((i+1)*c(i//2))


@lru_cache(None)
def kminus(d):
    if d == 0:
        return F(0)
    if d == 1:
        return F(2)
    return ((d-1)*kminus(d-2) + m(d-2) + m(d-1)) / d


@lru_cache(None)
def kplus(d):
    if d in (0, 1):
        return F(0)
    return ((d-2)*kplus(d-2) + F(2, d-1)) / (d-1)


def hstar(d):
    if d < 0:
        raise ValueError('Undefined H-star index')
    return c(d//2) if d % 2 == 0 else F(1, d) / c((d-1)//2)


def kminus_closed(d):
    if d % 2 == 0:
        return hstar(d) * sum((F(2, z*z) / hstar(z)**2 for z in range(2,d+1,2)), F(0))
    return hstar(d) * sum((F(2,z) for z in range(1,d+1,2)), F(0))


def kplus_closed(d):
    if d == 0:
        return F(0)
    u = d-1
    return hstar(u) * sum((F(2,z*z) / hstar(z) for z in range(1,u+1) if z % 2 == u % 2), F(0))


def M0(i, j):
    if min(i,j) < 0:
        raise ValueError('M0 is defined here only on nonnegative indices')
    if i >= j:
        return kminus(i-j) - sum((m(i-j+k-1)/k for k in range(1,j+1)), F(0))
    d = j-i
    return kplus(d) - sum((m(k-d-1)/k for k in range(d+1,j+1)), F(0))


def M(i,j):
    return (M0(i,j), 4*kernel(i-j), F(3,2)*kernel(j-i-1))


@lru_cache(None)
def harmonic(n, order=1):
    return sum((F(1,k**order) for k in range(1,n+1)), F(0))


def Z0(i,j):
    return -harmonic(i,2) if i == j else (harmonic(i)-harmonic(j))/(i-j)


def Z(i,j):
    return (Z0(i,j), F(0), F(i == j))


def poly_M(P,j):
    return tuple(sum((F(p)*M(i,j)[a] for i,p in enumerate(P)), F(0)) for a in range(3))


def poly_Z(D,j):
    return tuple(sum((F(d)*Z(i,j)[a] for i,d in enumerate(D)), F(0)) for a in range(3))


def entry(P,D,j, factor=F(3,2)):
    return sub(poly_M(P,j), scale(factor,poly_Z(D,j)))


def contact_coefficient(P,D,j):
    return sum((F(p)*kernel(j-i-1) for i,p in enumerate(P)), F(0)) - (F(D[j]) if j < len(D) else F(0))


def contact_truncation(P,L):
    return [contact_coefficient(P,[],j) for j in range(L)]


def series_certificate(i,j,N):
    """An exact partial sum and rigorous upper tail bound from the proof."""
    if N < 1:
        raise ValueError('N must be positive')
    start = i+N
    partial = sum((m(i+u)/F(j+u+1) for u in range(N)),F(0))
    multiplier = max(F(1), F(i+N,j+N+1))
    tail_upper = multiplier * (m(start-2) + m(start-1))
    return {'i':i, 'j':j, 'terms':N, 'partial_sum':partial,
            'tail_lower':F(0), 'tail_upper':tail_upper,
            'tail_bound_formula':'max(1,(i+N)/(j+N+1))*(m_(i+N-2)+m_(i+N-1))'}


def serialize(obj):
    if isinstance(obj,F):
        return str(obj)
    if isinstance(obj,dict):
        return {str(k):serialize(v) for k,v in obj.items()}
    if isinstance(obj,(tuple,list)):
        return [serialize(v) for v in obj]
    return obj


def run():
    # Independently fixed low-index data make the certificate more than a
    # comparison of two calls to the same implementation.
    expected_M = {
        (0,0):(0,4,0), (0,1):(0,0,F(3,2)), (1,0):(2,0,0),
        (0,2):(2,0,0), (2,0):(1,2,0), (1,1):(-2,4,0),
        (0,3):(F(1,2),0,F(3,4)), (3,0):(F(16,9),0,0),
        (0,4):(F(14,9),0,0), (4,0):(F(13,12),F(3,2),0),
        (1,2):(-1,0,F(3,2)), (2,1):(2,0,0),
    }
    for pair,expected in expected_M.items():
        check('fixed_low_index_M', M(*pair) == tuple(map(F,expected)))
    expected_Z = {(0,0):(0,0,1), (0,1):(1,0,0),
                  (1,1):(-1,0,1), (0,2):(F(3,4),0,0),
                  (1,2):(F(1,2),0,0), (2,2):(-F(5,4),0,1)}
    for pair,expected in expected_Z.items():
        check('fixed_low_index_Z', Z(*pair) == tuple(map(F,expected)))

    for n in range(1,101):
        check('moment_recurrence', (n+1)*m(n) == n*m(n-2))
    for r in range(100):
        check('central_binomial_ratio', c(r+1) == F(2*r+1,2*r+2)*c(r))
        check('H_star_ratio', hstar(r+2) == F(r+1,r+2)*hstar(r))
    for d in range(101):
        check('minus_closed_form', kminus(d) == kminus_closed(d))
        check('plus_closed_form', kplus(d) == kplus_closed(d))
    for d in range(2,101):
        check('full_minus_boundary_recurrence',
              scale(d,M(d,0)) == add(scale(d-1,M(d-2,0)),(m(d-2)+m(d-1),F(0),F(0))))
        check('full_plus_boundary_recurrence',
              scale(d-1,M(0,d)) == add(scale(d-2,M(0,d-2)),(F(2,d-1),F(0),F(0))))
    for i in range(25):
        for j in range(25):
            check('M_diagonal_recurrence', sub(M(i,j),M(i+1,j+1)) == (m(i)/F(j+1),F(0),F(0)))
            check('Z_diagonal_recurrence', sub(Z(i,j),Z(i+1,j+1)) == (F(1,(i+1)*(j+1)),F(0),F(0)))
            check('Z_symmetry',Z(i,j) == Z(j,i))
            for N in (1,2,5,10):
                finite_M = sum((m(i+u)/F(j+u+1) for u in range(N)),F(0))
                finite_Z = sum((F(1,(i+u+1)*(j+u+1)) for u in range(N)),F(0))
                check('M_finite_series_telescope',sub(M(i,j),M(i+N,j+N)) == (finite_M,F(0),F(0)))
                check('Z_finite_series_telescope',sub(Z(i,j),Z(i+N,j+N)) == (finite_Z,F(0),F(0)))
    for i in range(1,101):
        check('rational_adjacent_diagonal',M(i,i-1) == (m(i-2)+m(i-1),F(0),F(0)))

    example_specs = [([1],1),([1],3),([1],7),([2,-3,1],6),([0,1],2),([1,F(2,3),0,F(-5,7)],9)]
    examples=[]
    for P,L in example_specs:
        D=contact_truncation(P,L)
        rows=[]
        for j in range(L+2):
            result=entry(P,D,j)
            defect=contact_coefficient(P,D,j)
            check('polynomial_defect_identity',result[2] == F(3,2)*defect)
            if j < L:
                check('Taylor_contact_cancellation',defect == 0 and result[2] == 0)
            rows.append({'j':j,'entry_coefficients_1_G_zeta2':result,'Taylor_defect_coefficient':defect})
        examples.append({'P_coefficients_low_to_high':P,'D_coefficients_low_to_high':D,'L':L,'entries':rows})

    # Exhaustive bounded polynomial coefficient tests, including perturbations
    # of D which deliberately destroy contact. No random sampling is used.
    from itertools import product
    for P in product((-1,0,1), repeat=4):
        for L in range(1,9):
            D=contact_truncation(P,L)
            for j in range(10):
                result=entry(P,D,j)
                check('bounded_polynomial_defect_identity',result[2] == F(3,2)*contact_coefficient(P,D,j))
                if j < L:
                    check('bounded_polynomial_contact_cancellation',result[2] == 0)
            Dbad=D.copy()
            Dbad[L-1] += 1
            check('contact_perturbation_detected',entry(P,Dbad,L-1)[2] == -F(3,2))

    failures = [
        {'name':'missing_contact','P':[0],'D':[1],'j':0,'entry':entry([0],[1],0),
         'claim':'Nonzero formal zeta(2) coefficient; no unconditional nonmembership claim.'},
        {'name':'strict_j_range','P':[1],'D':[],'L':1,'j':1,'entry':entry([1],[],1),
         'claim':'Contact order 1 holds, but j=L has zeta(2) coefficient 3/2.'},
        {'name':'wrong_multiplier','P':[1],'D':[0,1],'L':3,'j':1,
         'multiplier':F(1),'entry':entry([1],[0,1],1,F(1)),
         'claim':'Using multiplier 1 instead of 3/2 leaves coefficient 1/2.'},
    ]
    payload={
        'schema_version':1,'revision':REVISION,'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'status':'all finite exact arithmetic checks passed',
        'method':'Original Python standard-library Fraction arithmetic; formal coefficients of 1, G, zeta(2).',
        'limits':'These tests do not prove analytic integral identities, irrationality, linear independence, or Lean verification.',
        'check_counts':COUNTS,'total_checks':sum(COUNTS.values()),
        'm_0_through_16':[m(i) for i in range(17)],
        'rational_boundaries_0_through_16':[{'d':d,'k_minus':kminus(d),'k_plus':kplus(d)} for d in range(17)],
        'M_0_through_6':[[M(i,j) for j in range(7)] for i in range(7)],
        'Z_0_through_6':[[Z(i,j) for j in range(7)] for i in range(7)],
        'triple_order':['rational','G','zeta(2)'],
        'contact_examples':examples,'formal_non_cancellation_examples':failures,
        'exact_series_enclosures':[series_certificate(i,j,32) for i,j in ((0,0),(0,1),(1,0),(2,3),(5,1),(6,6))]
    }
    target=HERE/'certificates.json'
    target.write_text(json.dumps(serialize(payload),indent=2)+'\n')
    print(json.dumps({'status':payload['status'],'total_checks':payload['total_checks'],
                      'check_counts':COUNTS,'output':str(target)},indent=2))


if __name__=='__main__':
    run()
