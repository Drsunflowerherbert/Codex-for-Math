# Exact length Egyptian fraction transformations

## Purpose and scope

This study extracts two elementary, reusable transformations from family 025 of OpenAI's mathematics collection: removal of repeated denominators without changing the number of terms, and padding an expansion of one while retaining one specified denominator. The arguments are ordinary proofs, accompanied by original exact-arithmetic examples. They do not validate the manuscript's global short-expansion estimates or constitute Lean verification. The manuscript credits the two transformations to Takenouchi and to van Doorn and Tang respectively; no novelty is claimed here.

Source revision: `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.

- [Removing repetitions, source elementary.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/build/elementary.tex)
- [Prescribed denominator padding, source prescribed.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/build/prescribed.tex)

## 1 Finiteness at fixed value and length

Let x>0 and let k be a positive integer. There are finitely many nondecreasing positive integer lists d_1≤...≤d_k with sum_i 1/d_i=x.

Proof. For k=1 the denominator is determined, if it exists. For k>1, x≤k/d_1, so 1≤d_1≤floor(k/x). This gives finitely many first choices. For each choice, the remaining k−1 terms have positive sum x−1/d_1; if this sum is nonpositive that branch supplies no list. Apply induction to each positive remaining sum. The finite union of finite sets is finite. No denominator cutoff has been assumed.

The proof gives a complete finite enumeration algorithm. At a partial state with remaining value r>0, length j≥1, and lower bound D, the next denominator lies between max(D,ceil(1/r)) and floor(j/r). For strictly increasing lists, recurse with D=d+1; for nondecreasing lists use D=d. If j=1, accept exactly when 1/r is an integer satisfying the lower bound. Use exact rational arithmetic throughout.

## 2 Removing repetitions with no length cost

Theorem. If 0<x<1 is a sum of exactly k positive unit fractions with integer denominators, then it has an exactly k term representation with pairwise distinct integer denominators, all at least two.

Proof. A denominator one is impossible, and two occurrences of denominator two are impossible, because either would force a sum at least one. For a repeated even denominator 2p, p≥2, replace its two terms using

    2/(2p) = 1/(p+1) + 1/(p(p+1)).

For a repeated odd denominator 2p+1, p≥1, use

    2/(2p+1) = 1/(p+1) + 1/((p+1)(2p+1)).

Each step preserves positivity, reciprocal sum, and length. The sum of the denominators strictly increases: by (p−1)^2 in the even case and by 2p^2 in the odd case. After sorting, every step remains inside the finite set from Section 1. A strictly increasing integer statistic cannot continue forever on a finite set. Thus the process stops, and it can stop only when no denominator repeats. The reciprocal sum still excludes denominator one.

This is a termination proof, not a useful upper bound on runtime or final denominator size. Intermediate denominators need not all increase: for instance (3,3) becomes (2,6). The increasing statistic is their sum.

Examples:

- (3,3), sum 2/3, becomes (2,6).
- (4,4), sum 1/2, becomes (3,6).
- (5,5), sum 2/5, becomes (3,15).

Boundary failures are essential. The two-term representation 1=1/2+1/2 cannot be changed into two distinct positive unit fractions: a denominator one leaves no positive remainder, while two distinct denominators at least two contribute at most 1/2+1/3<1. Thus replacing x<1 by x≤1 is false. Positivity and integrality are used in both finiteness and the sum restrictions.

The operation does not retain arbitrary markers. If x=2/3, k=2 and denominator three must remain, the other reciprocal must also be 1/3; no distinct two-term marked representation exists.

## 3 Padding while retaining a specified denominator

Theorem. Let r≥3 and 1=Σ_{i=1}^r 1/n_i with strictly increasing positive integers n_i. For any chosen m among these denominators, there is a representation of one by exactly r+1 distinct positive unit fractions that still contains m.

Proof. Every n_i≥2. The identity

    1/s = 1/(s+1) + 1/(s(s+1))

splits one term into two distinct larger-denominator terms. If the largest denominator is not marked, split it. Both new denominators exceed all retained denominators.

If the marked denominator v is the largest, let s be the second largest. Split s unless v=s+1 or v=s(s+1). All other unchanged denominators are below s, so these are the only possible collisions.

Suppose a collision occurs and s=ab is composite, with a,b≥2. Instead use

    1/s = 1/(s+a) + 1/(b(s+a)).

The reciprocal identity follows from s=ab. Also

    s+1 < s+a < b(s+a) < s(s+1).

The last inequality is equivalent to b+1<ab+1, which holds because a≥2. Thus the two new denominators avoid both possible exceptional values of v, are distinct, and exceed every other unchanged denominator.

It remains to exclude a collision when s=p is prime. Since r≥3 and the third largest denominator is at least two and smaller than p, p>2. Write the sum of the other reciprocals as A/B, using their product as B; none of their denominators is divisible by p, so p does not divide B. If v=p+1, the equation

    1−A/B = (2p+1)/(p(p+1))

contradicts reduction modulo p after denominators are cleared. If v=p(p+1), the same calculation uses numerator p+2 and yields 0≡2B mod p, also impossible because p is odd. These exhaust the cases and prove the theorem.

Iteration retains m at every prescribed larger length. It does not preserve every original denominator, nor does it imply any denominator-size bound.

A routine example is 1=1/2+1/3+1/6. Keeping marker six, split three to obtain denominators (2,4,6,12).

A genuine composite-collision example is

    1 = 1/3+1/4+1/7+1/12+1/14+1/15+1/20+1/420.

Keep marker 420. The naive split of 20 would introduce 420 again. Taking 20=2·10 instead gives replacement denominators 22 and 220, and the resulting nine-term list retains 420 with all denominators distinct. This case tests a branch absent from every distinct expansion of one with at most six terms in our finite enumeration.

## 4 Executed exact arithmetic checks

`check_examples.py` is original study code using only Python's standard library and exact Fraction arithmetic. It checks reciprocal sums, term counts, distinctness, markers, and increasing termination statistics. It executes no downloaded repository code.

The completed run checked:

- 34 repeated-denominator inputs with values below one, retaining a full replacement trace.
- All increasing expansions of one of lengths 3, 4, 5 and 6 returned by the complete recursion: respectively 1, 6, 72 and 2320 lists.
- Padding each of those lists with each possible marker: 14307 checks.
- The separately constructed eight-term composite-collision example above.

All executed assertions passed. These finite checks are illustrations and regression checks; universal validity comes from the proofs, not the enumeration count. The counts concern sorted distinct expansions of exactly one and are not counts for arbitrary rational values or unrestricted representations.

## 5 Reuse instructions and limits

For fixed-length cleanup, first check 0<x<1 and a finite positive integer denominator list. For prescribed-marker padding, first check that the total is exactly one and that the input is already distinct with at least three terms. A proof system should carry these preconditions separately: applying cleanup to an expansion of one is not authorized by Section 2.

Portable JSON records are intended for later MRS import. The local native MRS schema has not been inspected or modified for these portable records. Independent mathematical review and any future Lean formalization should be recorded separately from the current author-level proof and exact-computation status.
