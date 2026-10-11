# Exact small-prime checks

All calculations use integer tuple counts or exact rational numbers. The
universal statements are proved separately in study.md. These finite tests
are not proof-assistant verification and do not establish optimal thresholds.

## Diagonal sets

Every nonempty H was checked at k = 1,...,6 for each listed prime.
The density column is the smallest integer h with h^4 >= p^3.
The criterion column is the smallest h with h^4 > p^2(p-1).
The minimum probability ranges over every tested H at or above the density
threshold and every target residue, for four independent uniform products.

| p | All nonempty H | Density h | Four-product criterion h | Dense H checked | Exact minimum probability |
|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 2 | 2 | 1 | 15/32 |
| 3 | 7 | 3 | 3 | 1 | 80/243 |
| 5 | 31 | 4 | 4 | 6 | 12849/65536 |
| 7 | 127 | 5 | 5 | 29 | 53952/390625 |
| 11 | 2047 | 7 | 6 | 562 | 511960/5764801 |
| 13 | 8191 | 7 | 7 | 4096 | 410184/5764801 |
| 17 | 131071 | 9 | 9 | 65536 | 2418176/43046721 |

Every dense case satisfies Pr(sum = target) >= 1/p^2. In particular, the
minimum h supplied by the exact four-product criterion can be lower than
the source density cutoff, as at p = 11. This is a sufficient-method
threshold, not a claim about the smallest h that really guarantees coverage.

## Other exhaustive suites

| Suite | Inputs | Cases |
|---|---|---:|
| Diagonal H, k = 1,...,6 | p = 2,3,5,7,11,13,17 | 848862 |
| Ordered rectangular (A,B), k = 1,...,6 | p = 2,3,5,7 | 102888 |
| Ordered two-pair sequences | p = 3 | 2401 |
| Ordered three-pair sequences | p = 3 | 117649 |
| Bilinear sum-of-squares identities | p = 2,3,5; every nonempty A,B; every r != 0 | 3951 |

The diagonal and rectangular suites overlap; the row counts are test cases,
not disjoint mathematical objects. For every count vector C and total M,
the assertion checked is (p*C[t]-M)^2 <= (p-1)^2*p^k*M.

## Coefficients and shifts

| p | k | Total tuples per input | Coefficient/shift cases |
|---:|---:|---:|---:|
| 2 | 3 | 8 | 2 |
| 3 | 3 | 216 | 24 |
| 5 | 3 | 8000 | 320 |

These use the fixed pairs listed in certificates.json and exhaust all
nonzero coefficient vectors and all shifts for those pairs.

## Direct tuple enumeration cross-check

| p | k | Tuples | Exact residue-count vector |
|---:|---:|---:|---|
| 2 | 4 | 256 | [136, 120] |
| 3 | 3 | 64 | [22, 21, 21] |
| 5 | 3 | 216 | [38, 43, 45, 47, 43] |
| 7 | 3 | 15625 | [2172, 2236, 2284, 2236, 2224, 2236, 2237] |

The direct tuple counts agree with iterative convolution independently
of the Fourier proof. All explicit counterexamples and the Q = 30, p = 7
positive-divisor lift also pass exact assertions.

Full case aggregates, minimum-count witnesses by cardinality, exact size
thresholds, program hash, and source hash are in certificates.json.
Run python verify.py to regenerate that report. No dependency installation
or downloaded-code execution is used.
