> Historical source review: mathematical statements and verdicts are retained. Quoted hashes identify the original supplied files, which may differ from privacy-normalized public receipts. Original/public hashes are recorded in `publication/SOURCE-MAP.json`; fresh publication checks are separate.

# Independent Lean review

This review is performed by the certificate-checking agent, which did not
author the Lean modules. It distinguishes the statements actually proved
from the eventual analytic theorem in the supplied study. The rational
certificate review is separate in [certificate-review.md](certificate-review.md).

The stable algebraic snapshot audit rebuilt `Rational` and `Cancellation` and
successfully queried all 111 listed public theorems with `#print axioms`.
Every reported axiom belonged to `{propext, Classical.choice, Quot.sound}`;
none used `sorryAx` or a project-specific axiom. The complete query source,
output, source hashes, and results are in
[`certificates-lean-rational-audit.json`](../evidence/supplied/logs/certificates-lean-rational-audit.json).
Both sources remained unchanged during that inspection. A final full-project
audit is still required while the remaining analytic modules are completed.

The reproducible full-project checker is
[`audit_lean.py`](../scripts/audit_lean.py):

```sh
python -B scripts/audit_lean.py
```

It records exact `#check @name` types for every explicitly named public
declaration, `#print` bodies for definitions and structures, and `#print axioms`
results for every public theorem or lemma. Full names distinguish the
rational arrays from actual integrals and series. The report includes the
complete generated query sources and Lean output, checks that source and
configuration files stayed unchanged, and rejects local placeholder proofs,
custom axioms, and unsafe proof-evaluation shortcuts.

## Rational arrays and cancellation

The reviewed `Rational.lean` and `Cancellation.lean` definitions match the
finite rational formulas in the supplied mixed-moment study. Their public
theorem statements retain the required domains and hypotheses. The review
found no mathematical mismatch in these two modules.

The kernel accepts an integer, tests negativity before conversion to a
natural number, and then enforces even parity. In `formalM`, both differences
are formed in `ℤ`: `i-j` and `j-i-1`. The natural subtractions in the rational
part are confined to the appropriate `j ≤ i` or `i < j` branch, so they do
not introduce spurious kernel values. The rational off-diagonal denominator
for `Z` is formed in `ℚ`, avoiding natural truncated subtraction there too.

The central sequence is defined by the correct ratio, is proved positive,
and is identified with the normalized central binomial coefficient. The
moment recurrence and closed even/odd formulas use natural indices. A
separately named `momentExt` explicitly sets all negative integer inputs to
zero. The positive-index recurrence and adjacent-diagonal theorems use only
its `-1` value, matching the source convention. This auxiliary totalization
is not an assertion that negative-index analytic integrals exist or vanish;
the Python oracle rejects inputs below `-1`.

The plus recurrence is correctly indexed as `n+2`. At `n=0` (source index
`d=2`), the old plus-boundary rational part has coefficient zero and the new
value is 2. The full `formalM 0 2` triple is `(2,0,0)`, so the exceptional
Catalan coordinate of `formalM 0 0` is not propagated into the positive even
plus boundary. The integer kernel shifted recurrence also treats its
negative argument at the initial index explicitly.

`Coordinates` is the free rational coordinate space `Fin 3 → ℚ`.
`Coordinates.eval` is an evaluation map into the reals for arbitrary
parameters `G` and `ζ`; it is not asserted to be injective. Consequently,
the proved vanishing of the third formal coordinate implies the displayed
rational affine representation, but the code makes no converse
nonmembership claim from a nonzero coordinate.

`CoefficientContact P D L` is exactly the finite condition that the specified
defect coefficients vanish for all natural `j < L`. Thus nonnegativity of
the column is enforced by its type, the strict upper bound is retained, and
`L=0` is harmless: contact is vacuous but there is no column satisfying
`j < 0`. The condition is explicitly described as algebraic contact. It
does not, by definition alone, establish an analytic Taylor or big-O
statement for `tP/sqrt(1-t²)`.

The defect identity is universal over rational polynomials, not merely
tested examples. Finite support is used throughout; the correction
polynomial contributes its `j`th coefficient to the formal `ζ` coordinate
even when that index is outside its support, because the coefficient is
then zero. The multiplier is exactly `3/2`. The paired-polynomial theorem
requires either the weighted defect to vanish or every supported column
to be strictly below the contact order.

The transfer theorem `cancellation_of_decompositions` explicitly assumes
both real-array decompositions, for every natural pair `i,j`. Its conclusion
concerns the finite polynomial contractions defined in the file. Thus the
transfer theorem does not itself prove that an arbitrary array is an
integral, that its decomposition holds, or that coefficient contact follows
from analytic contact. These are substantive separate proof obligations.

The explicit `P=1,D=X,L=3` example is consistent with the independently
computed rational data: the first three entries have zero third coordinate,
and the excluded column `j=3` has triple `(-1/8,0,3/4)`. Its nonzero-coordinate
theorem does not assert that the evaluated real number is outside
`ℚ + ℚ G`.

The generated `Certificates.lean` statements have also been independently
compared against the Python rational expectations: all 36 `M` triples,
36 `Z` triples, and five `P=1,D=X` entry triples agree, for a total of 77.
`certificates-lean-statements.json` (historical report omitted from the minimal public set)
records the source hash and each comparison. Statement comparison does not
substitute for compiling the proof terms; that is included in the final
project build and axiom audit.

## Analytic statements reviewed in development

`Integrals.lean` defines actual iterated Lebesgue interval integrals for
`M`, rather than defining them by rational formulas. Its totalized endpoint
values do not affect Lebesgue integrals. It establishes the weight, basic
moments, full mixed kernel, and outer slices are integrable. The signed
geometric expansion on the negative half of the rectangle is controlled
using a separate `absoluteMoment` sequence. This distinction is essential:
odd signed moments vanish, whereas odd absolute moments do not. The
nonnegative absolute geometric majorant and summable integral norms justify
the exchange of the integral with the infinite sum.

The resulting `M_eq_series`, `M_diagonal`, and both actual boundary
recurrences are unconditional for natural indices. The earlier helper
`M_diagonal_of_intervalIntegrable` retains two explicit integrability
premises, which the unconditional theorem now discharges. The basic moment
integrals are also identified with the independently defined rational
sequence, and their decay follows from the proved rational square bound.

`Series.lean` concerns real infinite sums with explicit moment recurrence,
nonnegativity, decay, or summability premises as required by each result.
The summability theorem uses bounded sums of a nonnegative telescoping
majorant. This is an actual infinite-series argument once compiled; it
does not identify a series with an integral without a separate theorem.
The plus-boundary theorem again handles the zero multiplier at its
initial index correctly.

`Zeta.lean` defines `Z` as the product-measure integral on the open unit
square. The displayed geometric expansion is restricted to that square,
where its ratio is strictly below 1. Its integrability proof uses
nonnegative terms with summable integrals, including control of the
singular corner. The series identity and its diagonal/off-diagonal
evaluations therefore concern actual integrals, not coordinate definitions.
The off-diagonal orientation is checked by `Z 0 1 = 1`.

`Decomposition.lean` adds a substantive bridge from recurrence hypotheses to
the full real-array decomposition. `MomentRecurrenceData` contains the
diagonal recurrence, both boundary recurrences, and all three boundary
values. Its uniqueness proof uses nonzero leading coefficients and then
diagonal induction. In particular, the boundary values are hypotheses of
the structure, rather than identities built into the definition of an
arbitrary real array. Its moment-series specialization still exposes the
two independent boundary identities and decay as premises in the general
sequence theorem. The canonical rational-moment specialization discharges
decay using `RationalSeries.lean`, leaving only the two boundary identities.

`Constants.lean` defines Catalan's constant by its usual series and relates
it to the logarithmic kernel using a summable series of integral norms.
That argument uses absolute control even though the Catalan terms have
alternating signs. Its header explicitly separates the logarithmic
integral evaluation from identifying that integral with an `M` boundary.

`FormalContact.lean` identifies the finite contact convolution with the
coefficients of an actual `PowerSeries ℚ` product. Its monomial proof checks
the shift before using natural subtraction, giving the required zero value
when `j < i+1`. This formal-series identity does not by itself identify the
series with the analytic inverse square root or prove a big-O contact
criterion. `FormalSquareRoot.lean` supplies the exact formal square identity,
and `TaylorContact.lean` uses it to discharge the analytic contact implication
by finite polynomial approximation.

The approximation argument retains the positive real square-root branch:
the approximating polynomial has constant coefficient one and its
rationalizing denominator tends to 2 at zero. The difference from
`1/sqrt(1-x²)` therefore has the required big-O remainder. The final
polynomial coefficient argument is genuinely one-sided on `𝓝[>] 0`, with
division by `x` justified eventually by `x>0`; it does not infer a two-sided
condition from one-sided contact. This proves the contact implication needed
for cancellation without taking an infinite analytic generating-series
identity as a premise.

`BoundaryZeta.lean` evaluates the actual `M(0,1)` using the decreasing
substitution `t ↦ sqrt(1-t²)`. The transformed integrand is minus one half
of the paired slice; the reversed interval orientation supplies the second
minus sign. The resulting multiplier is `3/2` times the actual reciprocal
square series. The substitution theorem uses derivatives only on the
interior and explicitly supplies integrability of both integrands, so it
does not assume differentiability at the singular endpoint.

These development observations will be reconciled against the final
compiled declarations and recorded axiom dependencies before final review.
They are not an assertion that every in-progress file has already compiled.
