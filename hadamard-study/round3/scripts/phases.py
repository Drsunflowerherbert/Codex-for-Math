"""Quadratic Boolean phase relations under partial four-color assignments.

Color i has bits a_i,b_i. A phase polynomial is ANF over F2, stored as a bitset
of square-free monomials of degree <=2. The constant monomial is bit zero.
Everything here is exact algebra; distinct phase values are relaxed to
independent signs only for necessary feasibility tests.
"""

from bisect import bisect_left
from collections import defaultdict
from functools import lru_cache


class PhaseAlgebra:
    def __init__(self, h, graphs):
        self.h = h
        n = 2 * h
        supports = [0] + [1 << i for i in range(n)]
        supports += [(1 << i) | (1 << j) for i in range(n) for j in range(i + 1, n)]
        self.supports = tuple(supports)
        self.index = {support: i for i, support in enumerate(supports)}
        self.contains = []
        self.removed = []
        for v in range(n):
            containing = [i for i, support in enumerate(supports) if support >> v & 1]
            self.contains.append(sum(1 << i for i in containing))
            self.removed.append({i: 1 << self.index[supports[i] ^ (1 << v)] for i in containing})
        self.initial = []
        for edges in graphs:
            polynomial = 1
            for u, v in edges:
                a, b, c, d = 2 * u, 2 * u + 1, 2 * v, 2 * v + 1
                terms = [0, 1 << a, 1 << b, 1 << c, 1 << d,
                         (1 << a) | (1 << b), (1 << a) | (1 << d),
                         (1 << c) | (1 << b), (1 << c) | (1 << d)]
                for support in terms:
                    polynomial ^= 1 << self.index[support]
            self.initial.append(polynomial)
        self.initial = tuple(self.initial)

    def substitute_bit(self, polynomial, variable, value):
        present = polynomial & self.contains[variable]
        result = polynomial ^ present
        if value:
            table = self.removed[variable]
            while present:
                bit = present & -present
                result ^= table[bit.bit_length() - 1]
                present ^= bit
        return result

    def assign(self, phases, vertex, color):
        return tuple(self.substitute_bit(self.substitute_bit(p, 2 * vertex, color & 1),
                                         2 * vertex + 1, color >> 1) for p in phases)

    def color_bit(self, colors, depth, vertex, bit):
        if colors[vertex] >= 0:
            return (colors[vertex] >> bit) & 1
        return 1 << self.index[1 << (2 * vertex + bit)]

    def evaluate(self, polynomial, colors):
        assignment = sum(((color >> bit) & 1) << (2 * j + bit)
                         for j, color in enumerate(colors) for bit in (0, 1))
        value = 0
        while polynomial:
            low = polynomial & -polynomial
            support = self.supports[low.bit_length() - 1]
            value ^= assignment & support == support
            polynomial ^= low
        return int(value)


def sign_of_constant(polynomial):
    return -1 if polynomial & 1 else 1


def closest_distance(value, possibilities):
    i = bisect_left(possibilities, value)
    if i == 0:
        return possibilities[0] - value
    if i == len(possibilities):
        return value - possibilities[-1]
    return min(value - possibilities[i - 1], possibilities[i] - value)


def grouped_row_possible(colors, depth, phases, targets):
    groups = defaultdict(lambda: [0] * 4)
    for i, color in enumerate(colors):
        if color < 0:
            continue
        p = phases[i]
        groups[p & ~1][color] += sign_of_constant(p)
    fixed = groups.pop(0, [0] * 4)
    scalars = [[] for _ in range(4)]
    cross = []
    for vector in groups.values():
        nonzero = [c for c in range(4) if vector[c]]
        if len(nonzero) == 1:
            c = nonzero[0]
            scalars[c].append(abs(vector[c]))
        elif nonzero:
            direction = 1 if vector[nonzero[0]] > 0 else -1
            cross.append(tuple(direction * x for x in vector))
    return row_group_decision(tuple(fixed), tuple(tuple(sorted(w)) for w in scalars),
                              tuple(sorted(cross)), len(colors) - depth, targets)


@lru_cache(maxsize=4096)
def row_group_decision(fixed, scalars, cross, remaining, targets):
    """Cache a feasibility class, after discarding irrelevant phase names."""
    scalar_sets = []
    for weights in scalars:
        reachable = {0}
        for weight in weights:
            reachable = {x + delta for x in reachable for delta in (-weight, weight)}
        scalar_sets.append(tuple(sorted(reachable)))
    offsets = {(0, 0, 0, 0)}
    for vector in cross:
        offsets = {tuple(x[c] + direction * vector[c] for c in range(4))
                   for x in offsets for direction in (-1, 1)}
    return any(sum(closest_distance(u[c] - fixed[c] - offset[c], scalar_sets[c])
                       for c in range(4)) <= remaining
               for u in targets for offset in offsets)


def signed_sum_possible(constant, coefficients, extra_domains=()):
    return signed_sum_decision(constant, tuple(sorted(abs(c) for c in coefficients if c)),
                               tuple(sorted(tuple(sorted(set(d))) for d in extra_domains)))


@lru_cache(maxsize=4096)
def signed_sum_decision(constant, coefficients, extra_domains):
    radius = sum(abs(c) for c in coefficients) + sum(max(abs(x) for x in d) for d in extra_domains)
    if abs(constant) > radius:
        return False
    bits = 1 << radius
    for c in coefficients:
        if c:
            c = abs(c)
            bits = (bits << c) | (bits >> c)
    for domain in extra_domains:
        updated = 0
        for delta in domain:
            updated |= bits << delta if delta >= 0 else bits >> -delta
        bits = updated
    return bool(bits >> (radius - constant) & 1)


def clear_decision_caches():
    row_group_decision.cache_clear()
    signed_sum_decision.cache_clear()


def decision_cache_statistics():
    return {name: dict(zip(("hits", "misses", "maxsize", "currsize"), function.cache_info()))
            for name, function in (("row", row_group_decision), ("lag", signed_sum_decision))}


def grouped_lag_possible(colors, depth, phases, graphs, algebra, expanded=True):
    for t, edges in enumerate(graphs):
        groups = defaultdict(int)
        constant = 2 if expanded else 1
        factor = 2 if expanded else 1
        p = phases[t]
        groups[p & ~1] += factor * sign_of_constant(p)
        extra = []
        for u, v in edges:
            p = phases[u] ^ phases[v]
            if colors[u] >= 0 and colors[v] >= 0:
                if colors[u] == colors[v]:
                    groups[p & ~1] += 2 * factor * sign_of_constant(p)
            elif expanded:
                a = algebra.color_bit(colors, depth, u, 0) ^ algebra.color_bit(colors, depth, v, 0)
                b = algebra.color_bit(colors, depth, u, 1) ^ algebra.color_bit(colors, depth, v, 1)
                for q in (p, p ^ a, p ^ b, p ^ a ^ b):
                    groups[q & ~1] += sign_of_constant(q)
            else:
                extra.append((0, 2 * sign_of_constant(p)) if p < 2 else (-2, 0, 2))
        constant += groups.pop(0, 0)
        if not signed_sum_possible(constant, tuple(c for c in groups.values() if c), tuple(extra)):
            return False
    return True
