> Historical source review: mathematical statements and verdicts are retained. Quoted hashes identify the original supplied files, which may differ from privacy-normalized public receipts. Original/public hashes are recorded in `publication/SOURCE-MAP.json`; fresh publication checks are separate.

# Final proof scope

The completed principal mathematical target is rational-polynomial
Taylor-contact cancellation for actual mixed-moment Lebesgue integrals.
The final verification totals and process exits are recorded in
`evidence/supplied/logs/final-verification-summary.json`; the independent reviews are
`final-statement-review.md` and `final-audit-review.md`.

The default aggregate build exited zero for the umbrella and all 16 component
modules. The final public audit passed for 513 named declarations, including
429 theorems, with all build/type/definition/axiom query exits zero. The complete
environment audit passed for 835 project-origin constants (729 theorem
constants, 103 definitions, and one each of inductive, constructor, and
recursor), including private and generated declarations. Its 406 fresh axiom
queries and 429 matched public-audit results cover every constant; only
`propext`, `Classical.choice`, and `Quot.sound` occur. The exact-check rerun
passed 17,805 supplied rational checks, 20,072 independent checks, and 993
provenance checks. The 77 rational Lean examples compiled. These finite checks
are separate from the analytic proofs. All final verification commands exited
zero; earlier failed attempts remain identifiable in the evidence.

For `P,D : Polynomial ℚ`, `L,j : ℕ`, and `j < L`, either contact condition

```lean
analyticContactFunction P D =O[𝓝[>] 0] (fun x => x ^ L)
analyticContactFunction P D =O[𝓝 0] (fun x => x ^ L)
```

implies

```lean
Analysis.polynomialColumn P j - (3 / 2 : ℝ) * Zeta.polynomialColumn D j =
  (rationalWitness P D j : ℝ) + (catalanWitness P j : ℝ) * Constants.catalan
```

The precise entry points are
`MixedMoments.integral_cancellation_of_analyticContact` and
`MixedMoments.integral_cancellation_of_analyticContact_nhds` in
`MixedMoments/Applications.lean`.
`integral_analyticContact_witnesses` additionally packages the one-sided
version as an existential over two rational numbers. The two-sided equality
already specifies those same rational witnesses. The natural-number domain
includes all source cases `L≥1, 0≤j<L`; when `L=0` the column range is empty.

The contact function is the actual real function
`x*P(x)/Real.sqrt(1-x²)-D(x)`, after casting the rational coefficients.
`Analysis.polynomialColumn` is the product-measure integral of
`|t|*P(t)*s^j/(sqrt(1-t²)*(1-t*s))` over the open rectangle
`(-1,1)×(0,1)`. `Zeta.polynomialColumn` is the integral of
`D(t)*s^j/(1-t*s)` over `(0,1)²`. Their `polynomialColumn_eq_iterated`
theorems identify these definitions with the source's iterated interval
integrals. Boundary values on null sets are immaterial.

`Constants.catalan` is the alternating odd reciprocal-square series.
`Zeta.zeta2` is the reciprocal-square series. The proof establishes absolute
integrability, the signed geometric exchange for M, the nonnegative exchange
for Z, the rational moments and their decay, harmonic Z formulas, actual M
recurrences, `M(0,0)=4*catalan`, and `M(0,1)=(3/2)*zeta2`.
`actualMomentRecurrenceData` supplies all six fields of the generic recurrence
interface. Consequently `M_eq_formalM` is unconditional in its natural
indices; the principal cancellation theorem has no assumed integrability,
boundary evaluation, or coordinate realization premise.

The rational core specifies coordinates in the free space `Fin 3 → ℚ`.
`Coordinates.eval` realizes them as real expressions in `1,catalan,zeta2`.
The exact polynomial defect identity for the actual integrals is
`integral_exact_defect`. Vanishing of its designated zeta coordinate yields
the explicit rational affine formula. Coordinate evaluation is not assumed
injective. A nonzero formal zeta coefficient therefore gives no arithmetic
nonmembership conclusion. Catalan irrationality and arithmetic independence
are not claimed.

The repaired `Series.momentSeries_tail_bound` is a genuine infinite-series
bound with explicit recurrence, nonnegativity, decay, and `2≤i+N` premises.
It is not a claim of the source's full `N≥1` range. The omitted source endpoint
is `i=0,N=1`, involving the separate convention `m(-1)=0`; there is no named
actual-integral tail corollary. This restriction was retained, not weakened
or hidden.

All 21 supplied records are mapped in the independent statement review.
Deferred clauses include arbitrary real-polynomial integrability interfaces,
the global analytic inverse-square-root generating-series sum, the optional
pi/Basel evaluation, a contact criterion for arbitrary analytic functions,
the actual two-polynomial pairing cancellation bridge, unique truncation and
classification of all contact solutions, the exceptional tail endpoint,
and the arbitrary-subfield extension. These broader clauses do not appear
as assumptions smuggled into the completed principal result. This round
closes with a compiled scoped core and an explicit coverage boundary.

Only two recovered proof files changed during finalization: the one-line
TailBounds tactic correction and the Applications import/three corollaries.
The new umbrella imports all 16 component modules. Exact source differences
and original hashes are in `final-source-changes.patch` and
`evidence/supplied/logs/final-source-changes.json`.

The final evidence distinguishes the default aggregate build, the stable
public declaration/type/definition/axiom audit, and the supplemental inventory
of every project-origin Lean environment constant, including private and
generated declarations. The exact rational checks and 77 compiled rational
examples are separate finite evidence. The historical 111-theorem subset
audit and interrupted full smoke audit retain their original scope/status.

The first finalization audit also remains explicitly failed in
`evidence/supplied/logs/certificates-lean-full-audit-first-failed.json`: its build and axiom
query exited zero, but its type and definition queries exited one because
`pp.width` is not an option in Lean 4.24.0. Its line-based parser also omitted
three wrapped axiom lists. The checker was repaired to use the locally
confirmed `format.width` option and parse multiline lists with exact name
matching. `final-audit-checker-changes.patch` records that repair. A fresh
full run of the corrected checker, rather than reclassification of the failed
run, supplies the final public-audit status. Initial and corrected checker
hashes and freeze records are retained; the Lean proof sources did not change.

Two supplemental attempts are also retained as failed evidence. The first
used the wrong Lean elaboration context and stopped before the inventory.
The second produced the complete inventory and allowed axiom lists, but its
blanket nonpartial check rejected five compiler-generated recursive runtime
helpers. The corrected check recognizes only those five exact names via
`Lean.Compiler.mkUnsafeRecName`, verifies each has a safe nonpartial source
definition, and inspects every other project declaration's kernel type and
value dependencies to exclude those helpers. All five remain in the full
type and axiom inventory. Their partial flag is disclosed rather than
relabeled as nonpartial; source `partial`, `unsafe`, and new axiom declarations
remain rejected. The fresh corrected attempt supplies the final supplemental
status.

Lean 4.24.0 (commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`) and
all nine locked dependency revisions were verified; mathlib is
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. Source and checker stability,
actual process exits, package revisions, and compiler hash are recorded in
the supplied final logs. Fresh publication checks and their input hashes are
recorded separately in `../evidence/publication/`.

## Publication dependency-scan precision

The preserved complete-environment query scans all kernel types and all
definition/theorem/opaque values, plus constructor references. It does not
traverse recursor reduction-rule right-hand sides. The separate publication
query `scripts/inductive_kernel_metadata.lean` checks those rules and the
inductive/constructor metadata without changing the preserved proof or query
sources. Its actual exit is zero: exactly three project-origin records and
one recursor rule exclude all five disclosed runtime helpers. Current receipt
and exact query hashes are recorded separately under `evidence/publication/`.
Historical helper-dependency statements should be read with this original
scan boundary; the combined publication checks supply the additional coverage.
