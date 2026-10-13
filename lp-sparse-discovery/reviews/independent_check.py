"""Independent fixture audit with exact determinants and Cramer rule.

Uses only the Python standard library. Imports local benchmark fixtures and
calls the implementation under review, but does not reuse its rank or solve
functions in the audit oracle. This is ordinary testing, not formal proof.
"""

from fractions import Fraction as F
from itertools import combinations, product
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1] / 'benchmark'
spec = importlib.util.spec_from_file_location('review_benchmark', ROOT / 'benchmark.py')
b = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = b
spec.loader.exec_module(b)

def det(a):
    n = len(a)
    if n == 0:
        return F(1)
    return sum(((-1)**j * a[0][j] * det([row[:j]+row[j+1:] for row in a[1:]])
                for j in range(n)), F(0))

def minor(columns, rows):
    return [[columns[j][i] for j in range(len(columns))] for i in rows]

def rank(columns, d):
    for s in range(min(len(columns), d), 0, -1):
        for cs in combinations(columns, s):
            if any(det(minor(cs, rows)) for rows in combinations(range(d), s)):
                return s
    return 0

def solve(columns, target):
    s = len(columns)
    if s == 0:
        return () if all(v == 0 for v in target) else None
    for rows in combinations(range(len(target)), s):
        a = minor(columns, rows)
        denominator = det(a)
        if denominator:
            answer = []
            for j in range(s):
                modified = [row[:] for row in a]
                for ri, ti in enumerate(rows):
                    modified[ri][j] = target[ti]
                answer.append(det(modified) / denominator)
            if all(sum((answer[j]*columns[j][i] for j in range(s)), F(0)) == target[i]
                   for i in range(len(target))):
                return tuple(answer)
            return None
    raise ValueError('dependent support')

def independent_search(f, strategy, first_only):
    a, beta = f.normals, f.budgets
    if strategy == 'direct':
        cols, target = a, f.objective
    else:
        cols = tuple(row+(rhs,) for row, rhs in zip(a,beta))
        target = (F(0),)*f.dimension+(F(-1),)
        if f.kind == 'bound':
            cols += ((F(0),)*f.dimension+(F(1),),)
            target = f.objective+(f.bound,)
    r = rank(cols,len(target))
    counts = dict.fromkeys(['subsets_attempted','rank_tests','dependent_subsets_rejected',
                           'independent_solves','inconsistent_independent_systems',
                           'negative_solutions_rejected','budget_rejections',
                           'certificates_checked'], 0)
    found = None
    minimum = None
    for size in range(r+1):
        for support in combinations(range(len(cols)),size):
            counts['subsets_attempted'] += 1
            counts['rank_tests'] += 1
            selected = tuple(cols[i] for i in support)
            if rank(selected,len(target)) != size:
                counts['dependent_subsets_rejected'] += 1
                continue
            counts['independent_solves'] += 1
            answer = solve(selected,target)
            if answer is None:
                counts['inconsistent_independent_systems'] += 1
                continue
            if any(w<0 for w in answer):
                counts['negative_solutions_rejected'] += 1
                continue
            weights = [F(0)]*len(a)
            vertical = F(0)
            for j,w in zip(support,answer):
                if j<len(a):
                    weights[j] = w
                else:
                    vertical = w
            cost = sum((w*t for w,t in zip(weights,beta)),F(0))
            if strategy == 'direct' and cost > f.bound:
                counts['budget_rejections'] += 1
                continue
            counts['certificates_checked'] += 1
            positive = sum(w>0 for w in weights)
            minimum = positive if minimum is None else min(minimum,positive)
            if found is None:
                found = {'enumerated_indices':list(support),
                         'inequality_weights':list(map(str,weights)),
                         'positive_inequality_support':positive,
                         'vertical_residual_weight':str(vertical),
                         'combination_rhs':str(cost),
                         'first_success_subsets_attempted':counts['subsets_attempted'],
                         'first_success_independent_solves':counts['independent_solves']}
            if first_only:
                return counts,found,minimum,r
    return counts,found,minimum,r

data = json.loads((ROOT/'results.json').read_text())
assert len(data['fixtures']) == len(b.fixtures()) == 13
runs_checked = 0
identities_checked = 0
affine_parametrizations_checked = 0
for fixture,entry in zip(b.fixtures(),data['fixtures']):
    assert fixture.name == entry['fixture']['name']
    if fixture.feasible_witness is not None:
        assert all(sum((a*z for a,z in zip(row,fixture.feasible_witness)),F(0)) <= rhs
                   for row,rhs in zip(fixture.normals,fixture.budgets))
    original = fixture.original
    if original is not None:
        n = len(original.x0)
        scalar = lambda left,right: sum((x*y for x,y in zip(left,right)),F(0))
        assert all(scalar(row,original.x0) == rhs
                   for row,rhs in zip(original.equality_rows,original.equality_rhs))
        assert all(scalar(row,column) == 0 for row in original.equality_rows
                   for column in original.null_columns)
        assert rank(original.null_columns,n) == fixture.dimension
        assert rank(original.equality_rows,n)+fixture.dimension == n
        assert tuple(tuple(scalar(row,column) for column in original.null_columns)
                     for row in original.inequality_rows) == fixture.normals
        assert tuple(rhs-scalar(row,original.x0) for row,rhs in
                     zip(original.inequality_rows,original.inequality_rhs)) == fixture.budgets
        if fixture.kind == 'bound':
            assert tuple(scalar(original.objective,column) for column in
                         original.null_columns) == fixture.objective
            assert original.bound-scalar(original.objective,original.x0) == fixture.bound
            point = tuple(original.x0[j]+sum((w*column[j] for w,column in
                          zip(fixture.feasible_witness,original.null_columns)),F(0))
                          for j in range(n))
            assert all(scalar(row,point) == rhs
                       for row,rhs in zip(original.equality_rows,original.equality_rhs))
            assert all(scalar(row,point) <= rhs
                       for row,rhs in zip(original.inequality_rows,original.inequality_rhs))
        affine_parametrizations_checked += 1
    for run in entry['runs']:
        counts,found,minimum,r = independent_search(fixture,run['strategy'],run['mode']=='first_success')
        assert counts == run['counts'], fixture.name
        assert minimum == run['minimum_positive_inequality_support_observed'],fixture.name
        assert r == run['column_rank'],fixture.name
        assert bool(found) == run['candidate_found'],fixture.name
        assert all(found[k] == run['first_certificate'][k] for k in found),fixture.name
        original = fixture.original
        if original is not None:
            weights = tuple(map(F,found['inequality_weights']))
            identity = run['first_certificate']['original_identity']
            mu = tuple(map(F,identity['equality_weights']))
            c = original.objective if fixture.kind=='bound' else (F(0),)*len(original.x0)
            assert all(sum((w*row[j] for w,row in zip(weights,original.inequality_rows)),F(0))+
                       sum((w*row[j] for w,row in zip(mu,original.equality_rows)),F(0)) == c[j]
                       for j in range(len(c)))
            cost = (sum((w*t for w,t in zip(weights,original.inequality_rhs)),F(0))+
                    sum((w*t for w,t in zip(mu,original.equality_rhs)),F(0)))
            assert str(cost) == identity['original_combination_rhs']
            assert cost <= original.bound if fixture.kind=='bound' else cost == -1
            identities_checked += 1
        runs_checked += 1

toy_count = 0
for m in (2,3):
    for a in product((-1,0,1),repeat=m):
        for beta in product((0,1),repeat=m):
            for q in (-2,-1,0,1,2):
                for eta in (-1,0,1,2):
                    f = b.bound_fixture('toy',[[v] for v in a],beta,[q],eta,[0])
                    results = []
                    for strategy in ('direct','augmented'):
                        actual = b.search(f,strategy,False)
                        counts,found,minimum,r = independent_search(f,strategy,False)
                        assert actual['counts'] == counts
                        assert actual['candidate_found'] == (found is not None)
                        assert actual['minimum_positive_inequality_support_observed'] == minimum
                        results.append((found is not None,minimum))
                    assert results[0] == results[1]
                    toy_count += 1

zero_dimensional_runs = 0
for beta,eta in product((0,1),(-1,0,1)):
    f = b.bound_fixture('zero-dimensional',[[]],[beta],[],eta,[])
    for strategy in ('direct','augmented'):
        actual = b.search(f,strategy,False)
        counts,found,minimum,r = independent_search(f,strategy,False)
        assert actual['counts'] == counts
        assert actual['candidate_found'] == (eta >= 0) == (found is not None)
        assert actual['minimum_positive_inequality_support_observed'] == minimum
        zero_dimensional_runs += 1
f = b.contradiction_fixture('false-constant-row',[[]],[-1])
actual = b.search(f,'augmented',False)
counts,found,minimum,r = independent_search(f,'augmented',False)
assert actual['counts'] == counts
assert actual['candidate_found'] and found is not None and minimum == 1
zero_dimensional_runs += 1

# Cardinality of augmented generator support and inequality support differ.
f = b.bound_fixture('first-success-support',[ [1], [1] ],[3,1],[1],2,[0])
direct = b.search(f,'direct',True)
augmented = b.search(f,'augmented',True)
assert direct['first_certificate']['positive_inequality_support'] == 1
assert augmented['first_certificate']['positive_inequality_support'] == 2
assert augmented['first_certificate']['inequality_weights'] == ['1/2','1/2']
for strategy,actual in [('direct',direct),('augmented',augmented)]:
    counts,found,minimum,r = independent_search(f,strategy,True)
    assert actual['counts'] == counts
    assert actual['minimum_positive_inequality_support_observed'] == minimum

print(json.dumps({'fixture_runs_checked':runs_checked,'original_identities_checked':identities_checked,
                  'affine_parametrizations_checked':affine_parametrizations_checked,
                  'finite_toy_inputs_checked':toy_count,'toy_search_runs_checked':2*toy_count,
                  'additional_zero_dimensional_search_runs_checked':zero_dimensional_runs,
                  'first_success_support_counterexample_runs_checked':2,
                  'independent_method':'determinant minors and Cramer rule; exact Fraction arithmetic'},indent=2))
