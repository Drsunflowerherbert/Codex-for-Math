# Mathematical proof reconstructed from the supplied mathematical contract

This note does not reproduce or claim to have inspected the unavailable Library
archive. All arguments below were independently reconstructed and reviewed.

Let a representation be a finite list of positive integers. Its value is the
sum of reciprocal denominators. Its weight is the sum of denominators.

## Finiteness

For each real x and natural N, consider the positive nondecreasing lists with
length N and value x. For N=0 there is at most the empty list. For N>0 and x≤0
there are no such lists, because the reciprocal sum is positive.

If x>0 and the first denominator is a, every denominator is at least a. Thus
x≤N/a and xa≤N, so a≤N/x. Choose a natural B>N/x. The first denominator lies
in the finite set {0,…,B−1}. For each choice a, the tail has length N−1 and
value x−1/a and is positive and nondecreasing. Induction applies for every real
residual, including a nonpositive residual. A finite union of finite tail
families proves finiteness. This is a mathematical assertion for all real x;
an executable exact enumerator takes rational x.

## Duplicate replacements

For odd d=2k+1, the identity

    2/d = 1/(k+1) + 1/[d(k+1)]

has denominator-weight gain 2k². For even d=2k>0,

    2/d = 1/(k+1) + 1/[k(k+1)]

has gain (k−1)². If the complete value is below one and d is repeated, then
d≥3: a duplicated 1 already contributes two and a duplicated 2 contributes
one. Consequently the odd case has k≥1 and the even case has k≥2, and both
gains are strictly positive. New denominators are positive. Two terms replace
two terms, and reciprocal sum is exactly preserved. Other entries may collide
with the new denominators; this does not harm any of those invariants.

## Distinctness and termination

Sort the input. The sorted representations of its length and value form a
nonempty finite set. Choose one with maximum weight. If it contains a duplicate,
expose two copies by a permutation, replace them by the appropriate pair, and
sort again. Positivity, length, value, and sortedness persist while weight
strictly grows, contradicting maximality. The chosen state is distinct.

For explicit termination, finite states have weights bounded by some natural B.
A forward step strictly increases weight, so B−weight strictly decreases.
The Lean relation is R(next,current), as required for well-founded recursion.
It is confined to the subtype of admissible states. No universal iteration
count, sharp size bound, or marker preservation follows from this argument.

## Boundary one

If 1/a+1/b=1 with positive integer a,b, neither denominator is one. Therefore
a,b≥2. Clearing denominators gives a+b=ab. The nonnegative product
(a−2)(b−2) implies a+b≤4. Both denominators must equal two. Thus [2,2] is a
positive length-two representation of one, and no distinct positive length-two
representation of one exists.

## Exact checks and caveats

[4,4,6]→[3,6,6]→[3,4,12] preserves value 2/3 and length but loses denominator 6.
[6,10,10,30]→[6,6,30,30] preserves value 2/5, grows weight 56→72, and creates
two duplicate pairs from one. These examples forbid using duplicate count as a
termination rank or treating arbitrary markers as cleanup invariants.

The compiled padding theorem has a separate mathematical and compiler audit in
`review/MarkerPaddingAudit.md`; that audit includes both ordinary-splitting
collision cases and the accepted coarse bound M'≤M(M+1).
