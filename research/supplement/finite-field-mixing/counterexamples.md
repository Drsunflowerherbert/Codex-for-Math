# Hypothesis boundaries

The claims here are about finite-field product sums. They do not say that
the sufficient cardinality criterion is necessary, or that four is an
optimal number of products. All tuples may repeat.

## 1. A composite modulus breaks the argument

Take modulus 16 and H = {0,2,4,6,8,10,12,14}. Its size is 8, so
h^4 = 16^3. Every product is divisible by 4. The four-product sum has
support exactly {0,4,8,12}, not all residues modulo 16.

The naively substituted error factor is 15/16 < 1. At frequency r = 4,
however, every exponential exp(2*pi*i*r*a*b/16) equals 1, whereas the
claimed normalized bilinear bound would be 1/2. The failed step is
field cancellation in r(b-b'). Nonzero factors in a composite residue
ring can multiply to zero.

This counterexample concerns Z/16Z, not the finite field with 16 elements.
Those are different algebraic structures. No counterexample to a
properly formulated finite-field trace-character extension is claimed.

## 2. Dependence inside a pair

Over F_5 take H = {1,2,3,4}. Choose X uniformly and set Y = X^(-1).
The possible pairs are (1,1), (2,3), (3,2), (4,4), each equally likely.
Both marginals are uniform, but every product equals 1. Four independent
copies of the pair sum only to 4. The density hypothesis holds because
4^4 >= 5^3.

Uniform marginals therefore do not imply the product-distribution bound.

## 3. Dependence between products

Over F_2 choose independent uniform X,Y from the whole field, then reuse
the same product U = XY four times. Each U_i has the intended product
marginal, but U_1+U_2+U_3+U_4 = 0. Residue 1 is absent.

The proof's Fourier factorization uses independence of the products;
correct individual marginal distributions are insufficient.

## 4. Nonuniform weights change quantitative bounds

Over F_5 give X and Y independent marginal weights

    Pr(X=0) = 9/10; Pr(X=a) = 1/40 for a != 0.

Every residue has positive probability. Their product has mass 99/100
at zero and 1/400 at each nonzero residue. Every nonzero Fourier
coefficient equals 79/80, exceeding the uniform bound 1/sqrt(5).

This disproves the claimed probability bound under arbitrary weights.
It does not disprove covering with full support: positive weighting of
all tuples preserves exactly which sums are possible. If zero weights
are permitted on the declared set, even the effective support may shrink.

## 5. Equality in the general sufficient criterion

Over F_2 take A = {0}, B = {0,1}. Then N = |A||B| = 2 and

    (p-1)*(sqrt(p/N))^k = 1

for every positive k. Every product and sum equals zero. Thus replacing
the strict inequality by <= 1 is false in general. For k = 4 the exact
tuple counts are [16,0].

This is separate from the four-product density endpoint: h^4 >= p^3
forces the stronger error factor <= (p-1)/p, which is strictly below 1.

## 6. The criterion is sufficient, not necessary

Take H = {0,1}. The one-product count vector is [3,1,0,...,0].
For four products its coefficients before reduction modulo p are

    (3 + z)^4 = 81 + 108z + 54z^2 + 12z^3 + z^4.

Over F_5 every residue is reached, although the sufficient Fourier
criterion fails. Over F_7 residues 5 and 6 are absent. These two exact
examples show both that the criterion is not necessary and that some
size assumption is needed for a uniform four-product guarantee.

## 7. Further elementary boundaries

- Empty sets: a uniform sample cannot be defined and no tuple exists.
- Zero frequency: its character average is 1. For H = F_2 this exceeds
  sqrt(2)/2, so the nonzero-frequency qualification cannot be omitted.
- Zero coefficients: even full-field sets give a constant sum if every
  coefficient is zero. Remove zero-coefficient terms before applying
  the count threshold.
- Distinctness: in F_2 four distinct product values cannot be chosen,
  although H = F_2 satisfies the size hypothesis. The theorem permits
  repeated choices.
- Positive lifts: a zero or signed integer sum need not yield a positive
  multiplier. The source uses strictly positive divisors, so its lifted
  sum is positive and divisible by p.

The ordinary proofs and interfaces are in `study.md`, Sections 1–8.
Exact values are stored under `examples_and_counterexamples` in
`certificates.json`; `verify.py` asserts them using exact arithmetic.
