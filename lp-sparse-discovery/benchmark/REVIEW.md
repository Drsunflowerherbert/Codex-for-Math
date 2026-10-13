# Independent benchmark review

Reviewed on 2026-10-13 by a separate review agent from the benchmark author.
This is an ordinary code and arithmetic review, not formal verification.

**Outcome: approved for the stated fixture-only scope; no blocking defect
found.** The reviewed `benchmark.py` SHA-256 was
`375a36269dd53cd3b7350000c7de14bf95f29228aedef8f3fa8b2e6379b7b918`.

## Reproduction and arithmetic evidence

Running `python3 lp-sparse-discovery/benchmark/benchmark.py` succeeded. Its
standard output was byte-identical to `results.json`, with SHA-256
`c314baf34cb68412b97727e0dbfa75806cc9de3f2b71ba6bce7cc345c619b107`.
There are 13 fixtures and 44 runs, including first-success and exhaustive modes.
Fixture coefficients are `fractions.Fraction` values; the elimination and
certificate operations introduce no floating-point arithmetic.

The supplied 14-test regression suite also passed under independent execution
with `python3 -m unittest discover -s lp-sparse-discovery/benchmark -v`.
The README's fixture table matches the report, and it explicitly documents
the search-counter exclusions described below.

The reviewer separately re-evaluated every first certificate's weighted
normal identity, nonnegativity and budget check using exact rational
arithmetic. For both fixtures with original equalities, the reviewer also
re-evaluated the original normal identity and combined right-hand side.
The bound fixture gives equality weights `(1,1)` and RHS `11/3`; the projected
zero-row contradiction gives equality weight `-1` and RHS `-1`. The rational
contradiction has weights `(18/11,20/11)` and RHS `-1`.

Additional elimination probes checked empty consistent and inconsistent
systems, an overdetermined unique solution, an overdetermined inconsistency,
a negative rational solution, rejection of proportional columns, rejection
of a zero column, and zero-dimensional cases. All passed. The routine solves
only independent columns and rejects dependence explicitly; it does not
select an arbitrary solution by setting free variables to zero.

## Support and count checks

All bound fixtures have a feasible witness, checked before direct normal
support enumeration. All successful searches independently check their
reduced certificate. For exhaustive runs, the number of attempted subsets
equals

```
sum(binomial(column_count,j), j=0,...,column_rank).
```

For all 44 runs, attempted subsets partition into dependent rejections and
independent solves. Independent solves partition into inconsistencies,
negative solutions, direct budget rejections and accepted certificates.
Rank-test counts equal attempted-subset counts. These count support-loop
operations: they exclude the initial whole-column rank computation and the
separate original-equality reconstruction. They are not total RREF-call
counts or runtime measurements.

The expected minimum supports are also consistent with direct inspection.
The identity-normal examples require all specified coordinates; the sharp
contradiction requires the full positive circuit. The two other nonzero-normal
contradictions cannot use one row. The projected zero-row contradiction uses
one row, and the zero-objective bounds use no rows. Every other listed
nonzero-objective bound has an exhibited valid singleton certificate.

The augmented strategy counts the optional vertical residual as an enumerated
column, while `positive_inequality_support` counts only positive original
inequality weights. Zero-weight entries in enumerated supersets can therefore
repeat the same certificate; the report explicitly counts accepted candidates
including duplicate representations. Its minimum is labelled *observed*,
including in first-success runs.

## Scope

The experiment covers the supplied exact fixtures, not arbitrary inputs or
general LP status classification. Its finite-search justification depends on
the support theorems and feasibility assumptions in the study; successful
fixture execution alone is not a proof of that justification. Row order and
vertical augmentation comparisons are reproducible search-effort examples,
not broad solver-performance claims. No code from `lp-certificates` is used.
