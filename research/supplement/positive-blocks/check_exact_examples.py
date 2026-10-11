"""Original Gaussian-rational arithmetic checks for the positive-block study.

Python standard library only. This is finite example verification, not a formal
proof verifier. Repository code is not imported or executed. Run from any cwd.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import random
import sys

ROOT = Path(__file__).resolve().parent
REVISION = 'fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb'

@dataclass(frozen=True)
class QI:
    re: F = F(0)
    im: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, 're', F(self.re))
        object.__setattr__(self, 'im', F(self.im))
    def __add__(self, other):
        other = qi(other)
        return QI(self.re + other.re, self.im + other.im)
    __radd__ = __add__
    def __neg__(self):
        return QI(-self.re, -self.im)
    def __sub__(self, other):
        return self + (-qi(other))
    def __rsub__(self, other):
        return qi(other) + (-self)
    def __mul__(self, other):
        other = qi(other)
        return QI(self.re*other.re - self.im*other.im,
                  self.re*other.im + self.im*other.re)
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = qi(other)
        d = other.abs2()
        if not d:
            raise ZeroDivisionError('zero Gaussian rational')
        z = self * other.conj()
        return QI(z.re/d, z.im/d)
    def conj(self):
        return QI(self.re, -self.im)
    def abs2(self):
        return self.re*self.re + self.im*self.im
    def __bool__(self):
        return bool(self.re or self.im)
    def text(self):
        if not self.im:
            return str(self.re)
        if not self.re:
            return str(self.im) + '*i'
        return str(self.re) + ('+' if self.im > 0 else '') + str(self.im) + '*i'


def qi(z):
    return z if isinstance(z, QI) else QI(F(z))


def mat(rows):
    m = [[qi(z) for z in row] for row in rows]
    assert m and m[0] and len({len(row) for row in m}) == 1
    return m


def shape(m):
    return len(m), len(m[0])


def adj(m):
    return [[z.conj() for z in row] for row in zip(*m)]


def mul(a, b):
    ar, ac = shape(a)
    br, bc = shape(b)
    assert ac == br
    return [[sum((a[i][k]*b[k][j] for k in range(ac)), QI())
             for j in range(bc)] for i in range(ar)]


def scale(t, a):
    return [[qi(t)*z for z in row] for row in a]


def sub(a, b):
    assert shape(a) == shape(b)
    return [[z-w for z, w in zip(ra, rb)] for ra, rb in zip(a, b)]


def trace(a):
    n, m = shape(a)
    assert n == m
    return sum((a[i][i] for i in range(n)), QI())


def hs2(a):
    return sum((z.abs2() for row in a for z in row), F(0))


def rank(a):
    a = [row[:] for row in a]
    nr, nc = shape(a)
    out = 0
    for j in range(nc):
        pivot = next((k for k in range(out, nr) if a[k][j]), None)
        if pivot is None:
            continue
        a[out], a[pivot] = a[pivot], a[out]
        d = a[out][j]
        a[out] = [z/d for z in a[out]]
        for k in range(nr):
            if k != out and a[k][j]:
                t = a[k][j]
                a[k] = [z-t*w for z, w in zip(a[k], a[out])]
        out += 1
        if out == nr:
            break
    return out


def block(a, b, c):
    return [ra+rb for ra, rb in zip(a, b)] + [rb+rc for rb, rc in zip(adj(b), c)]


def encoded(a):
    return [[z.text() for z in row] for row in a]


def quadratic(d, v):
    vc = mat([[z] for z in v])
    return mul(adj(vc), mul(d, vc))[0][0]


def gram_case(case_id, title, x, y, expected=None, retain=True):
    x, y = mat(x), mat(y)
    assert len(x) == len(y)
    a, b, c = mul(adj(x), x), mul(adj(x), y), mul(adj(y), y)
    p, q = mul(x, adj(x)), mul(y, adj(y))
    z = [rx+ry for rx, ry in zip(x, y)]
    delta = block(a, b, c)
    assert delta == mul(adj(z), z)
    aa, cc, beta = hs2(a), hs2(c), hs2(b)
    assert aa == hs2(p) and cc == hs2(q)
    assert trace(mul(p, q)) == QI(beta)
    gap = aa + cc - 2*beta
    assert gap == hs2(sub(p, q)) and gap >= 0
    product_squared_gap = aa*cc - beta*beta
    assert product_squared_gap >= 0
    sum_eq, prod_eq = gap == 0, product_squared_gap == 0
    assert sum_eq == (p == q)
    ranks = {k: rank(m) for k, m in [('Delta', delta), ('A', a), ('B', b), ('C', c)]}
    assert ranks['B'] <= min(ranks['A'], ranks['C'])
    t = None
    if not aa or not cc:
        assert beta == 0 and prod_eq
        assert sum_eq == (aa == 0 and cc == 0)
    elif prod_eq:
        t = beta/aa  # In an equality case this is exactly c/a, with no radicals.
        assert t > 0 and t*t*aa == cc
        assert q == scale(t, p)
        assert mul(b, adj(b)) == scale(t, mul(a, a))
        assert mul(adj(b), b) == scale(1/t, mul(c, c))
        assert mul(b, c) == scale(t, mul(a, b))
        assert len(set(ranks.values())) == 1
    else:
        # If Q is a positive scalar multiple of P, equality would follow.
        # A ratio of traces avoids square roots and supplies a direct converse check.
        tp, tq = trace(p), trace(q)
        assert tp.im == tq.im == 0 and tp.re > 0 and tq.re > 0
        assert q != scale(tq.re/tp.re, p)
    if sum_eq:
        assert mul(a, a) == mul(b, adj(b))
        assert mul(c, c) == mul(adj(b), b)
        assert mul(a, b) == mul(b, c)
    if expected is not None:
        assert (aa, cc, beta, sum_eq, prod_eq) == expected, (case_id, aa, cc, beta)
    out = {
        'id': case_id, 'title': title,
        'dimensions': {'gram_rows': len(x), 'p': len(x[0]), 'q': len(y[0])},
        'certificate': 'Delta=[X Y]*[X Y]; exact matrix identity checked',
        'squared_norms': {'A': str(aa), 'C': str(cc), 'B': str(beta)},
        'sum_gap': str(gap),
        'product_squared_gap': str(product_squared_gap),
        'product_squared_gap_definition': '||A||HS^2*||C||HS^2 - (||B||HS^2)^2',
        'sum_equality': sum_eq, 'product_equality': prod_eq,
        'nonzero_equality_t': None if t is None else str(t),
        'ranks': ranks, 'all_exact_checks_passed': True,
    }
    if retain:
        out.update({k: encoded(v) for k, v in [('X', x), ('Y', y), ('A', a), ('B', b), ('C', c), ('Delta', delta), ('P', p), ('Q', q)]})
    return out


def non_psd_case(case_id, title, a, b, c, v, expected, negative_gram=None):
    a, b, c = mat(a), mat(b), mat(c)
    delta = block(a, b, c)
    assert a == adj(a) and c == adj(c)
    value = quadratic(delta, v)
    assert value.im == 0 and value.re < 0
    aa, cc, beta = hs2(a), hs2(c), hs2(b)
    assert (aa, cc, beta) == expected
    out = {
        'id': case_id, 'title': title, 'dimensions': {'p': len(a), 'q': len(c)},
        'A': encoded(a), 'B': encoded(b), 'C': encoded(c), 'Delta': encoded(delta),
        'certificate': 'Hermitian Delta has an exact strictly negative quadratic-form witness',
        'negative_witness': [qi(z).text() for z in v], 'quadratic_form': value.text(),
        'squared_norms': {'A': str(aa), 'C': str(cc), 'B': str(beta)},
        'sum_gap': str(aa+cc-2*beta), 'product_squared_gap': str(aa*cc-beta*beta),
        'sum_inequality_holds': 2*beta <= aa+cc,
        'product_inequality_holds': beta*beta <= aa*cc,
        'ranks': {k: rank(m) for k, m in [('Delta', delta), ('A', a), ('B', b), ('C', c)]},
        'all_exact_checks_passed': True,
    }
    if negative_gram is not None:
        w = mat(negative_gram)
        assert scale(-1, delta) == mul(adj(w), w)
        out['negative_semidefinite_certificate'] = {'W': encoded(w), 'identity': '-Delta=W*W'}
    return out


def main():
    i = QI(0, 1)
    cases = [
        gram_case('E01', 'Scalar sharpness', [[1]], [[1]], (F(1), F(1), F(1), True, True)),
        gram_case('E02', 'Complex unbalanced product equality', [[1]], [[2*i]], (F(1), F(16), F(4), False, True)),
        gram_case('E03', 'Rectangular rank two equality', [[1, 0], [0, 2]], [[1, 0, 0], [0, 2*i, 0]], (F(17), F(17), F(17), True, True)),
        gram_case('E04', 'Rectangular unbalanced equality', [[1, 0], [0, 2]], [[F(3, 2), 0, 0], [0, 3*i, 0]], (F(17), F(1377, 16), F(153, 4), False, True)),
        gram_case('E05', 'Nondiagonal Gaussian rational equality', [[1, i]], [[1, F(3, 5)*i, F(4, 5)]], (F(4), F(4), F(4), True, True)),
        gram_case('E06', 'Strict positive definite', [[1], [0], [0], [0]], [[F(1, 2)]]*4, (F(1), F(1), F(1, 4), False, False)),
        gram_case('E07', 'Equal ranks insufficient', [[1, 0], [0, 1]], [[1, 0], [0, 2]], (F(2), F(17), F(5), False, False)),
        gram_case('E08', 'Equal norms insufficient', [[2, 0], [0, 1]], [[1, 0], [0, 2]], (F(17), F(17), F(8), False, False)),
        gram_case('E09', 'Zero left block', [[0, 0]], [[1, i]], (F(0), F(4), F(0), False, True)),
        gram_case('E10', 'Zero right block', [[2]], [[0, 0]], (F(16), F(0), F(0), False, True)),
        gram_case('E11', 'All zero rectangular', [[0, 0]], [[0, 0, 0]], (F(0), F(0), F(0), True, True)),
        non_psd_case('E12', 'Positive definite diagonal blocks insufficient', [[1]], [[2]], [[1]], [1, -1], (F(1), F(1), F(4))),
        non_psd_case('E13', 'No finite constant without block positivity', [[0]], [[1]], [[0]], [1, -1], (F(0), F(0), F(1))),
        non_psd_case('E14', 'Entrywise two by two tests insufficient', [[1, 0], [0, 1]], [[1, 1], [1, 1]], [[1, 0], [0, 1]], [1, 1, -1, -1], (F(2), F(2), F(4))),
        non_psd_case('E15', 'Negative semidefinite equality', [[-1]], [[1]], [[-1]], [1, -1], (F(1), F(1), F(1)), [[1, -1]]),
        gram_case('E16', 'Nondiagonal rank two rectangular equality', [[1, i], [1, 2]], [[F(6, 5), F(8, 5), -2], [F(6, 5), F(8, 5), 4*i]], (F(39), F(624), F(156), False, True)),
    ]
    # Independent exact extra checks for the stated caveats.
    x, y = mat([[2, 0], [0, 1]]), mat([[1, 0], [0, 2]])
    a, b = mul(adj(x), x), mul(adj(x), y)
    assert sub(mul(a, a), mul(b, adj(b))) == mat([[12, 0], [0, -3]])
    a, b, c = mat([[1, 0], [0, 1]]), mat([[1, 1], [1, 1]]), mat([[1, 0], [0, 1]])
    assert all(b[j][k].abs2() <= a[j][j].re*c[k][k].re for j in range(2) for k in range(2))
    rng = random.Random(325)
    def entry():
        return QI(F(rng.randrange(-2, 3), rng.randrange(1, 4)),
                  F(rng.randrange(-2, 3), rng.randrange(1, 4)))
    sweep = []
    for d in range(1, 4):
        for p in range(1, 4):
            for q in range(1, 5):
                for k in range(5):
                    x = [[entry() for _ in range(p)] for _ in range(d)]
                    y = [[entry() for _ in range(q)] for _ in range(d)]
                    sweep.append(gram_case(f'S{d}{p}{q}{k}', 'Seeded finite Gram fixture', x, y, retain=True))
    assert len(sweep) == 180
    examples = {
        'schema': 'portable-mathematics-exact-examples-v1',
        'source_revision': REVISION,
        'complex_encoding': 'Every entry is a string denoting a Gaussian rational; i^2=-1. Fractions are exact.',
        'proof_status': 'Finite exact checks and matrix certificates only; not a general theorem proof or formal kernel verification.',
        'named_examples': cases,
        'seeded_sweep': {'seed': 325, 'case_count': len(sweep), 'cases': sweep},
    }
    (ROOT/'exact-examples.json').write_text(json.dumps(examples, indent=2)+'\n')
    script_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    summary = {
        'status': 'passed',
        'python_version': sys.version.split()[0],
        'dependencies': 'Python standard library only',
        'arithmetic': 'fractions.Fraction pairs for Gaussian rationals; no floating point',
        'named_examples': len(cases),
        'positive_semidefinite_named_examples': 12,
        'non_psd_named_examples': 4,
        'seeded_gram_fixtures': len(sweep),
        'all_exact_checks_passed': True,
        'checked_identities': ['Delta=Z*Z', '||A||HS^2=||XX*||HS^2', '||C||HS^2=||YY*||HS^2', '||B||HS^2=tr(XX*YY*)', 'sum deficit identity', 'product inequality squared with nonnegative sides', 'sum equality iff P=Q', 'product equality normalized Gram and intrinsic block identities', 'rank bound and equal-rank consequence in nonzero equality cases', 'negative quadratic form witnesses'],
        'script_sha256': script_sha,
        'examples_sha256': hashlib.sha256((ROOT/'exact-examples.json').read_bytes()).hexdigest(),
        'external_code_executed': False,
        'formal_verification': False,
        'universal_proof_location': 'study.md',
    }
    (ROOT/'checks.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    main()
