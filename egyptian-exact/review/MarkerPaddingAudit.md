# Independent audit of marker-preserving padding

Date: 2026-10-11. Source: independently derived from the supplied theorem statement;
the original Library ZIP was not available to this reviewer.

## Accepted statement

Let `S` be a finite set of positive integer denominators, with at least three
elements, such that

\[
\sum_{s\in S}\frac1s=1.
\]

For every specified `m ∈ S`, there is a finite set `S'` of positive integer
denominators such that

\[
|S'|=|S|+1,\qquad \sum_{s\in S'}\frac1s=1,\qquad m\in S'.
\]

If `M = max S`, the construction also gives

\[
\max S'\le M(M+1).
\]

The proof preserves every original denominator except one chosen denominator
different from `m`. This audit makes no marker-preservation claim for duplicate
cleanup, and makes no sharp maximum-denominator claim.

## Preliminary facts

Every denominator in `S` is at least two: a denominator one already contributes
the full sum one, and at least two other positive terms would make the total
strictly larger than one. Write `M = max S`, and let `d` be the second-largest
denominator. Since `S` has at least three distinct elements, there is an element
`c < d`; both `c` and `d` are at least two, so `d ≥ 3`.

There is exactly one original denominator greater than `d`, namely `M`.
Consequently, when replacing `d`, new denominators greater than `d` can collide
with an old denominator only by equaling `M`.

## Two splitting identities

For `t ≥ 2`, the ordinary split is

\[
\frac1t=\frac1{t+1}+\frac1{t(t+1)}.
\]

Its two denominators are positive, strictly greater than `t`, distinct, and
bounded above by `t(t+1)`.

If `t = ab` with `a,b ≥ 2`, the factor split is

\[
\frac1{ab}=\frac1{a(b+1)}+\frac1{ab(b+1)}.
\]

Put `u = a(b+1) = t+a` and `v = ab(b+1) = t(b+1) = bu`. Then
`t < u < v`, and both are at most `t(t+1)`, because `a ≤ t` and `b ≤ t`.

These identities are exact rational equalities. No iteration or termination
argument is used for padding.

## Construction and complete collision analysis

### The marker is not the maximum

If `m ≠ M`, apply the ordinary split to `M`. Both new denominators exceed every
original denominator, so they are absent from `S`; they are distinct and positive.
Removing `M` and adding them preserves `m`, increases cardinality by exactly one,
and preserves the reciprocal sum. The largest new denominator is `M(M+1)`.

### The marker is the maximum

Suppose `m = M`. Try the ordinary split of the second-largest denominator `d`.
Its denominators `d+1` and `d(d+1)` are both greater than `d`; they are distinct
because `d ≥ 3`. Therefore the only possible collisions are

\[
M=d+1 \quad\text{or}\quad M=d(d+1).
\]

If neither equality holds, this split is valid, even when `d(d+1) < M`.
It preserves the marker `M`, and all final denominators are at most `M(M+1)`.

If either equality holds, `d` is composite, as proved below. Choose a factorization
`d = ab` with `a,b ≥ 2`, and use the factor split instead.

* If `M = d+1`, then `u = d+a ≥ d+2 > M` and `v > u`. Both are above all original
  denominators, so neither collides.
* If `M = d(d+1)`, then `a < d` and `b < d`. Hence
  `d < u = d+a < 2d < d(d+1) = M`, and
  `d < v = d(b+1) < d(d+1) = M`. Both lie strictly between `d` and `M`, where
  there are no original denominators. They do not collide with each other because
  `v = bu` and `b ≥ 2`.

In both cases the replacement removes `d`, keeps `M = m`, and adds two positive,
distinct denominators absent from the remaining original set. Thus cardinality
increases by one, the reciprocal sum stays one, and the marker remains present.
The maximum bound follows from `u,v ≤ d(d+1) ≤ M(M+1)` and preservation of all
other original denominators, which were at most `M`.

## Why `d` is composite in the two collision cases

Suppose for contradiction that `d = p` is prime. Let `R = S \ {p,M}`. All
elements of `R` are strictly less than `p`, and positive. Set

\[
A=\prod_{r\in R}r,\qquad T=\sum_{r\in R}\frac Ar.
\]

Empty products and sums are respectively one and zero. Every `A/r` is an
integer, and no `r` is divisible by `p`, so `p` does not divide `A`.

* If `M = p+1`, clearing denominators in
  `1 = 1/p + 1/(p+1) + T/A` gives
  \[
  p(p+1)A=(p+1)A+pA+p(p+1)T.
  \]
  Reduction modulo `p` implies `p ∣ A`, a contradiction.
* If `M = p(p+1)`, clearing denominators in
  `1 = 1/p + 1/[p(p+1)] + T/A` gives
  \[
  p(p+1)A=(p+1)A+A+p(p+1)T.
  \]
  Reduction modulo `p` implies `p ∣ 2A`. Since `p ∤ A` and `p` is prime,
  `p ∣ 2`, hence `p=2`. This contradicts the established `d ≥ 3`.

Thus `d ≥ 3` is not prime, and it admits a factorization `d = ab` with
`a,b ≥ 2`, as required.

## Exact regression example for the product collision

The product collision is real and must not be omitted:

\[
S=\{2,6,7,14,15,20,420\},\qquad m=M=420.
\]

The reciprocal sum is exactly one: after multiplying by 420, the numerators are
`210 + 70 + 60 + 30 + 28 + 21 + 1 = 420`.
The second-largest denominator is `d=20`, and `d(d+1)=420` is the marker.
The ordinary split of 20 would collide with 420. Using `20=2·10` instead gives

\[
\frac1{20}=\frac1{22}+\frac1{220},
\]

and produces the valid eight-term set
`{2,6,7,14,15,22,220,420}` with the same sum and marker.

## Formalization obligations

An eventual Lean theorem must expose positivity, distinctness, length, sum, and
marker membership for the final representation. If the coarse bound is stated,
it must also relate the original and final maxima. The proof needs a formal
prime cancellation or cleared-denominator lemma; merely asserting that the
second-largest denominator is composite is not sufficient. In particular,
handling only the collision `M=d+1` leaves the valid example above uncovered.

The preceding sections present the ordinary mathematical audit. The compiled
implementation audit follows; the primary cleanup theorem is a separate proof.

## Compiled implementation audit

The completed Lean implementation was independently reviewed later on 2026-10-11
and is accepted.
The reviewed modules are `Egyptian/PaddingArithmetic.lean`,
`Egyptian/PaddingCollision.lean`, `Egyptian/SafeSplit.lean`,
`Egyptian/PaddingSelection.lean`, and `Egyptian/Padding.lean`.

The actual public theorem `pad_one_preserving_denominator` assumes exactly:

* a finite list of natural-number denominators;
* positivity of every member;
* `input.Nodup`;
* `3 ≤ input.length`;
* `reciprocalSum input = 1`;
* membership of the specified natural-number `marker` in `input`.

Its conclusion gives a list `out` with positive members, `out.Nodup`,
`out.length = input.length + 1`, `reciprocalSum out = 1`, and `marker ∈ out`.
There is no hidden sorted-input hypothesis, input-size bound, or marker exception.

The actual public theorem `pad_one_preserving_denominator_bounded` adds an
arbitrary natural bound `B` and the assumption `∀ d ∈ input, d ≤ B`. It gives the
same conclusion and additionally `∀ d ∈ out, d ≤ B * (B + 1)`. Thus choosing an
actual maximum as `B` gives the accepted coarse maximum-denominator theorem.
An explicit hypothesis `0 < B` is unnecessary: positivity and nonempty input
already imply it. The unbounded wrapper supplies `input.sum` as a valid bound
and drops the final bound field; it does not advertise `input.sum` as a maximum.

### Proof audit

* `expose_top_two` sorts a permutation in decreasing order, uses `Nodup` to
  obtain strict decrease, and uses length at least three together with exclusion
  of denominator one to establish `3 ≤ d`. Its output gives all tail denominators
  strictly less than `d` and `d < M`.
* The maximal-marker branch swaps `M,d` before calling the prime obstruction,
  retains `M` in the tail of the replaced denominator, and proves that both new
  denominators are absent from `M :: t`. It invokes both successor- and
  product-collision repairs.
* The nonmaximal-marker branch removes `M`. `marker ≠ M` and original membership
  imply membership in `d :: t`, which is retained. The two new denominators are
  strictly above `M` and therefore absent from that retained tail.
* `safe_split` separately checks new positivity, distinctness of the new pair,
  and nonmembership of each in the retained tail. The retained tail is `Nodup`
  because the input is `Nodup`. Its length equation is exactly a one-term
  increase, and its reciprocal-sum equation follows from the supplied exact
  identity.
* `padding_pair` derives proper factors from nonprimality and proves both factors
  are at least two. In the successor-collision branch, its two terms exceed `M`;
  in the product-collision branch they are below `M` and above `d`. In the
  ordinary branch, the negated collision disjunction proves both new terms
  differ from `M`.
* The bound is first proved as `M(M+1)` for each new and retained term. The public
  bounded theorem obtains `M ≤ B` through the permutation and input bound,
  then uses multiplication monotonicity to obtain `B(B+1)`.

No mismatch was found between these Lean interfaces and the audited mathematical
statements. Sorted output is not promised or needed for the padding theorem.

### Independent compiler evidence

`review/PaddingPublicHarness.lean` imports the compiled `Egyptian.Padding` module,
prints the actual fully explicit types of both public theorems and ten helper
theorems, prints their axiom dependencies, and type-checks independent explicit
instances of both requested public interfaces. The command

```text
tooling/lean-4.24.0-linux/bin/lake env lean review/PaddingPublicHarness.lean
```

completed with exit code zero and no warnings. Its complete output is saved in
`review/padding-public-compile.log`. Every inspected theorem depends only on
`propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or additional axiom
appears. The earlier independent prime-obstruction prototype and its successful
log remain in `review/PrimeCollisionPrototype.lean` and
`review/prime-collision-compile.log`.

The source, compiled artifact, compiler, dependency-pin, and evidence hashes for
this review snapshot are recorded in `review/padding-reviewed-hashes.json`.
