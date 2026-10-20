#!/usr/bin/env python3
"""Independent exact fixtures for 10-sylvester-extensions.md.

No network, source documents, floating-point arithmetic, or file mutations.
Run from the toolkit directory: python3 scripts/check_sylvester.py
Requires SymPy. Finite-field ranks are computed directly by modular elimination.
"""
from itertools import product
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

t = s.symbols("t")
checks = []


def done(label, count=None):
    suffix = "" if count is None else f" ({count} cases)"
    checks.append(label)
    print("PASS " + label + suffix)


def mat_symbols(prefix, rows, cols):
    return s.Matrix(rows, cols, s.symbols(f"{prefix}0:{rows * cols}"))


def block(A, B, C):
    return A.row_join(C).col_join(s.zeros(B.rows, A.cols).row_join(B))


def is_zero(M):
    return all(s.expand(x) == 0 for x in M)


def sylvester_matrix(A, B):
    return s.kronecker_product(s.eye(B.rows), A) - s.kronecker_product(B.T, s.eye(A.rows))


def eval_poly(poly, A):
    out = s.zeros(A.rows)
    for coeff in s.Poly(poly, t).all_coeffs():
        out = out * A + coeff * s.eye(A.rows)
    return out


def companion(poly):
    coeffs = s.Poly(poly, t).monic().all_coeffs()
    n = len(coeffs) - 1
    out = s.zeros(n)
    for i in range(1, n):
        out[i, i-1] = 1
    for i in range(n):
        out[i, n-1] = -coeffs[-i-1]
    return out


def rank_mod(M, prime):
    rows = [[int(M[i, j]) % prime for j in range(M.cols)] for i in range(M.rows)]
    rank = 0
    for j in range(M.cols):
        pivot = next((i for i in range(rank, M.rows) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][j], -1, prime)
        rows[rank] = [(x * inv) % prime for x in rows[rank]]
        for i in range(M.rows):
            if i != rank:
                multiplier = rows[i][j]
                rows[i] = [(x - multiplier*y) % prime for x, y in zip(rows[i], rows[rank])]
        rank += 1
        if rank == M.rows:
            break
    return rank


def residue_tuple(M, prime):
    return tuple(int(x) % prime for x in M)


# 1. Generic rectangular maps test signs and the reverse trace orientation.
A, B = mat_symbols("a", 2, 2), mat_symbols("b", 3, 3)
C, h = mat_symbols("c", 2, 3), mat_symbols("h", 2, 3)
g = mat_symbols("g", 3, 2)
D = A*h - h*B
P = block(s.eye(2), s.eye(3), h)
Pinv = block(s.eye(2), s.eye(3), -h)
assert is_zero(Pinv * block(A, B, C) * P - block(A, B, C+D))
assert is_zero(P * block(A, B, C) - block(A, B, C-D) * P)
assert s.expand(s.trace(g*D) - s.trace((g*A-B*g)*h)) == 0
assert s.expand(s.trace(g*C) - s.trace(C*g)) == 0
done("section-change sign, endpoint-equivalence sign, rectangular trace adjoint")


# 2. The free-resolution telescoping identity, independently on coefficients.
B = s.Matrix([[0, -2, 1], [1, 0, 0], [0, 1, 3]])
for j in range(1, 7):
    for w in s.eye(3).columnspace():
        q = sum((t**(j-1-ell) * (B**ell)*w for ell in range(j)), s.zeros(3, 1))
        assert is_zero((t*s.eye(3)-B)*q - (t**j*w - B**j*w))
done("free-resolution telescoping identity", 18)


# 3. Construct the Bezout/divided-difference inverse on each basis matrix.
bezout_count = 0
for apoly, bpoly in [
    (t**3, (t-1)**2),
    (t**2+1, t**2+2),
    ((t+2)**2, (t-3)**3),
]:
    A, B = companion(apoly), companion(bpoly)
    u, v, gcd = s.gcdex(apoly, bpoly, t)
    assert s.expand(u*apoly + v*bpoly) == 1 == gcd
    assert is_zero(eval_poly(apoly, A))
    assert is_zero(eval_poly(bpoly, B))

    def inverse(D):
        out = s.zeros(A.rows, B.rows)
        for (degree,), coeff in s.Poly(bpoly, t).terms():
            for ell in range(degree):
                out += coeff * A**(degree-1-ell) * D * B**ell
        return eval_poly(v, A)*out

    for i in range(A.rows):
        for j in range(B.rows):
            E = s.zeros(A.rows, B.rows)
            E[i, j] = 1
            assert is_zero(A*inverse(E)-inverse(E)*B-E)
            assert is_zero(inverse(A*E-E*B)-E)
            bezout_count += 1
done("both sides of constructive Bezout inverse", bezout_count)


# 4. Finite geometric inverse for distinct Jordan eigenvalues.
geometric_count = 0
for aa in range(1, 5):
    for bb in range(1, 5):
        N = s.zeros(aa)
        M = s.zeros(bb)
        for i in range(aa-1):
            N[i, i+1] = 1
        for i in range(bb-1):
            M[i, i+1] = 1
        d = s.Rational(3)
        K = sylvester_matrix(N, M)
        I = s.eye(aa*bb)
        assert K**(aa+bb-1) == s.zeros(aa*bb)
        inverse = sum(((-1)**r * d**(-r-1) * K**r for r in range(aa+bb-1)), s.zeros(aa*bb))
        assert (d*I+K)*inverse == I == inverse*(d*I+K)
        geometric_count += 1
N = s.Matrix([[0, 1], [0, 0]])
C = mat_symbols("z", 2, 2)
inv = -C-N*C+C*N+2*N*C*N
assert is_zero(N*inv-inv*(s.eye(2)+N)-C)
done("finite geometric inverse and characteristic-independent nilpotent formula", geometric_count)


# 5. Exhaust ALL C for two J2 blocks over F2 and F3; solve through the image.
finite_count = 0
for prime in (2, 3):
    image = {residue_tuple(N*s.Matrix(2, 2, vals)-s.Matrix(2, 2, vals)*N, prime)
             for vals in product(range(prime), repeat=4)}
    assert len(image) == prime**2
    classes = {}
    for vals in product(range(prime), repeat=4):
        C = s.Matrix(2, 2, vals)
        alpha = int(C[1, 0]) % prime
        beta = int(s.trace(C)) % prime
        canonical = s.Matrix([[beta, 0], [alpha, 0]])
        assert residue_tuple(C-canonical, prime) in image
        assert (residue_tuple(C, prime) in image) == (alpha == beta == 0)
        assert int(s.trace(N*C)) % prime == alpha
        assert int(s.trace(C)) % prime == beta
        T = block(N, N, C)
        assert residue_tuple(T**4, prime) == (0,)*16
        actual = tuple(rank_mod(T**power, prime) for power in (1, 2, 3))
        expected = (3, 2, 1) if alpha else ((2, 1, 0) if beta else (2, 0, 0))
        assert actual == expected, (prime, vals, actual, expected)
        # Original chosen lift of w2 gives the cyclic residue alpha + beta*t.
        e = s.Matrix([0, 0, 0, 1])
        assert residue_tuple(T**2*e, prime) == (beta, alpha, 0, 0)
        classes[(alpha, beta)] = classes.get((alpha, beta), 0)+1
        finite_count += 1
    assert len(classes) == prime**2 and set(classes.values()) == {prime**2}
    C = s.eye(2)
    T = block(N, N, C)
    assert rank_mod(T**2, prime) == (0 if prime == 2 else 1)
done("all J2/J2 quotient classes, witness coordinates, and Jordan ranks over F2/F3", finite_count)


# 6. Smith types for primary powers, including degree-two irreducibles over Q.
smith_count = 0
for pp in (t, t*t+1):
    for aa in range(1, 5):
        for bb in range(1, 5):
            mm = min(aa, bb)
            for cc in [s.Integer(0), s.Integer(1)] + [pp**j * (1+pp) for j in range(mm+2)]:
                presentation = s.Matrix([[pp**aa, -cc], [0, pp**bb]])
                smith = smith_normal_form(presentation, domain=s.QQ.poly_ring(t))
                first = s.Poly(smith[0, 0], t).monic().as_expr()
                second = s.Poly(smith[1, 1], t).monic().as_expr()
                expected_first = s.Poly(s.gcd(s.gcd(pp**aa, pp**bb), cc), t).monic().as_expr()
                expected_second = s.div(pp**(aa+bb), expected_first, t)[0]
                assert s.expand(first-expected_first) == 0
                assert s.expand(second-expected_second) == 0
                if cc and s.degree(expected_first, t) < mm*s.degree(pp, t):
                    P = s.div(pp**aa, expected_first, t)[0]
                    Q = s.div(pp**bb, expected_first, t)[0]
                    q = s.div(cc, expected_first, t)[0]
                    ss, rr, gcd = s.gcdex(P, q, t)
                    assert gcd == 1
                    left = s.Matrix([[1, 0], [rr*Q, 1]])
                    right = s.Matrix([[ss, q], [-rr, P]])
                    reduced = left*presentation*right
                    assert is_zero(reduced-s.diag(expected_first, expected_second))
                    assert s.expand(left.det()) == 1 == s.expand(right.det())
                smith_count += 1
done("cyclic primary Smith factors and explicit unimodular reduction", smith_count)


# 7. Determinant-resultant identity with repeated and nonsplit factors.
resultant_count = 0
for A, B in [
    (N, s.eye(2)+N),
    (companion((t+2)**3), companion((t-1)**2)),
    (companion(t*t+1), companion(t*t+2)),
    (companion((t*t+1)**2), companion(t*t+1)),
    (s.Matrix([[0]]), s.Matrix([[2]])),
    (s.Matrix([[2, 3], [4, 5]]), s.Matrix([[1, 7, 2], [0, 3, 4], [0, 0, 6]])),
]:
    delta = sylvester_matrix(A, B)
    resultant = s.resultant(A.charpoly(t).as_expr(), B.charpoly(t).as_expr(), t)
    assert delta.det() == resultant
    if resultant:
        smith = smith_normal_form(delta, domain=s.ZZ)
        order = abs(s.prod(smith[i, i] for i in range(smith.rows)))
        assert order == abs(resultant)
    resultant_count += 1
assert sylvester_matrix(s.Matrix([[0]]), s.Matrix([[2]])) == s.Matrix([[-2]])
assert s.Matrix([[-2]]).inv()*s.Matrix([[-1]]) == s.Matrix([[s.Rational(1, 2)]])
assert abs(s.Matrix([[1, 1], [0, 2]]).det()) == 2
done("determinant/resultant identity, integral cokernel orders, and index-two example", resultant_count)

print(f"All {len(checks)} exact-check groups passed.")
