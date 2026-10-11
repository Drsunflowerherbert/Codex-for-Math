> Historical source review: mathematical statements and verdicts are retained. Quoted hashes identify the original supplied files, which may differ from privacy-normalized public receipts. Original/public hashes are recorded in `publication/SOURCE-MAP.json`; fresh publication checks are separate.

# Independent final statement and scope review

This review checks the recovered Lean statements against all 21 records in
`research/supplement/mixed-moments/theorems.json`
and the corresponding `study.md`. The reviewer did not author the proofs,
change Lean sources, or run builds. The prior proof notes and independent
development reviews were inspected.

The scoped principal result is cancellation for **actual integrals of rational
polynomials**, with explicit rational witnesses, under the stated analytic
contact hypothesis and the strict natural-index restriction `j < L`. Its
proof structure discharges the real-array decomposition and both boundary
values. No arithmetic independence assumption is required. Completion of this
result is compatible with several broader source-record clauses remaining
deferred. This review does not label all 21 source records Lean verified.

This is a source-statement review. Fresh compilation, declaration inventory,
source stability, and transitive axiom results must come from the final build
and audit evidence. The recovery's interrupted full audit is not a pass, and
its earlier 111-theorem audit covers only `Rational` and `Cancellation`.

The initial stabilized source snapshot is
`evidence/supplied/logs/final-frozen-inputs-initial.json`, frozen at 2026-10-11 04:27:50 UTC.
At that stage the reviewer independently recomputed every listed file hash
and found no mismatch. In particular, `Applications.lean` is 4,768
bytes with SHA-256
`6b2de7509ddb9c78b6ef5cbc5e147ebd031bef8521ff855b2c4451350bc550de`, and
`TailBounds.lean` is 4,104 bytes with SHA-256
`de8d5dc29f933d86705f679f89e3d2ed4f65086bb40470d44a7cf4737a2f0f16`.
The source record file `theorems.json` is 18,237 bytes with SHA-256
`cec34a1946f671e62d4cc9258032f19ab693e9204acb63dd9fc83872d49a70a0`;
the accompanying `study.md` is 24,947 bytes with SHA-256
`e8778fe759b0b50930c3a6fb4c58259aafe8d9276c0ceb00e95b3408d4603a00`.

The reviewer inspected `evidence/supplied/logs/applications-build.json` and its full command
output. The actual command `bash scripts/with-lean.sh lake build
MixedMoments.Applications` completed with exit **0** at 04:27:31 UTC. Its
before/after hashes agree and match the frozen snapshot. The output includes
the repaired `MixedMoments.TailBounds` and all application dependencies.
This establishes the application build, including the actual contact
corollaries described below. The reviewer also inspected
`evidence/supplied/logs/final-default-build.json` and its output: the default command
`bash scripts/with-lean.sh lake build` completed with exit **0** at 04:28:26
UTC, with unchanged hashes agreeing with the frozen snapshot. The umbrella
imports all 16 component modules, including the 77 rational certificate
examples. Neither build alone certifies the theorem/axiom audit; its later
completed result is reconciled below.

The first fresh full-audit attempt subsequently failed on checker defects:
the type/definition queries used the unsupported pretty-printer option
`pp.width`, and three wrapped axiom lists were not captured by the original
parser. Its failed report is preserved as
`evidence/supplied/logs/certificates-lean-full-audit-first-failed.json`. The checker correction
uses `format.width` and multiline parsing. No Lean proof source changed.
A fresh full audit, with no reuse of the failed run as a pass, was required.
Its revised checker hash and stability receipt are recorded below.

The final revised snapshot is `evidence/supplied/logs/final-frozen-inputs.json`, frozen at
2026-10-11 04:50:19 UTC. The reviewer independently recomputed all 24 hashes
and found no mismatch. Every Lean proof and umbrella source hash is unchanged
between the two snapshots. The changed inputs are the public checker,
supplemental environment checker, and supplemental environment query source;
their initial/final hashes are both retained in the respective snapshots.
In particular, `scripts/audit_lean.py` changed from SHA-256
`bfd3013eb5d5c2b08ae9776d2de11a627239e26cbf3c5d69595a05adaf2a6a70` to
`c98d5daa3f7f55f4839d904349d81408ae7eb8d2cf21a93637771e975b30deab`.

The fresh corrected public audit completed with actual exit **0** at
2026-10-11 04:44:00 UTC. The reviewer independently inspected the process
receipt `evidence/supplied/logs/final-public-audit.json` and the report
`evidence/supplied/logs/certificates-lean-final-audit.json`. Its status is `passed`: 17 modules
(the 16 components plus umbrella), 513 named public declarations, 429
theorems, and 84 definitions/abbreviation/structure entries. Build, exact
type query, definition query, and axiom query all have exit zero. The source,
configuration, and module inventory stayed unchanged.

The reviewer independently compared the 429 theorem names against the 429
recorded axiom lists, found exact agreement, and found that their union is
exactly `{propext, Classical.choice, Quot.sound}`. Every source hash in the
audit agrees with the revised frozen snapshot; the audit's checker hash
agrees with the current checker. All 513 exact type outputs are present,
including the two universe-polymorphic names printed with universe suffixes.
The exact outputs for `M_eq_formalM`, `integral_exact_defect`, both analytic
contact cancellation theorems, the existential witness theorem, and
`Series.momentSeries_tail_bound` agree with the statement/assumption review
below. All nine application theorem axiom lists contain only the three
allowed logical axioms.

The principal statement review and public declaration audit are accepted.
The fresh supplemental audit also completed with actual exit **0** at
2026-10-11 04:51:45 UTC, as independently inspected in
`evidence/supplied/logs/final-environment-audit.json` and `evidence/supplied/logs/full-environment-audit.json`.
Its status is `passed`. The full provenance-selected inventory contains 835
constants: 729 theorem declarations, 103 definitions, one inductive, one
constructor, and one recursor. It contains all 513 public source declarations
and includes private/generated declarations. All 835 axiom results are
resolved: 406 fresh ordinary `#print axioms` results plus 429 full-public-audit
results reused only after exact source/configuration/checker hash matching
and exact environment name inclusion. Their union remains within the three
allowed logical axioms. The reviewer independently matched all 25 supplemental
input hashes to current files and checked every inventory record is resolved.

The full inventory explicitly retains five generated partial runtime helpers:
`MixedMoments.central._unsafe_rec`, `MixedMoments.hStar._unsafe_rec`,
`MixedMoments.kminus._unsafe_rec`, `MixedMoments.kplus._unsafe_rec`, and
`MixedMoments.moment._unsafe_rec`. Each is the exact compiler-generated name
for a safe, nonpartial source definition; each has `partial=true`,
`unsafe=false`, and a non-proposition-valued type. The reviewer inspected and
hash-checked Lean 4.24.0's `addAndCompilePartialRec` implementation, which
generates these runtime copies using `Compiler.mkUnsafeRecName` and
`DefinitionSafety.partial`. The supplemental report inspects every other
project kernel type/value/constructor dependency and records **no references**
to these five helpers. Source partial declarations, unsafe declarations, and
axiom declarations are absent. These helpers are disclosed, not relabeled as
nonpartial, and are not proof shortcuts or mathematical assumptions.

The two failed supplemental attempts remain historical failed evidence: the
first stopped on the elaboration-context error, and the second rejected the
five generated helpers under an overly broad nonpartial criterion. The fresh
corrected report performs the explicit helper classification and exclusion
checks described above; it does not reclassify a failed attempt as a pass.

Final evidence hashes are:

| Evidence | SHA-256 |
|---|---|
| `evidence/supplied/logs/certificates-lean-final-audit.json` | `39a71ca2a8744c975788c84f9337bc921a54b71a2be86727d06537a344fd6a4b` |
| `evidence/supplied/logs/full-environment-audit.json` | `d07cb5df9da0fbcd0280988b5f000da942db7c73caeeba6c1d27fc3534190703` |
| `scripts/audit_lean.py` | `c98d5daa3f7f55f4839d904349d81408ae7eb8d2cf21a93637771e975b30deab` |
| `scripts/audit_environment.py` | `f90117002546c74d7a287ec058e5e567ff440895aa45e1381571e5d8bfc1712a` |
| `scripts/full_environment_inventory.lean` | `4a6ec90000411d752e4d709d6c3a1ef9d67727ea3e5e79a207ff850927d6d269` |

The scoped principal statement, default build, public audit, and qualified
complete environment audit are accepted. The coverage deferrals below remain
explicit, with no remaining verification blocker for this compiled scope.

## Actual objects and discharged assumptions

`MixedMoments.Analysis.M` is defined by the Lebesgue interval integral

\[
 M(i,j)=\int_{-1}^{1}\int_0^1
 \frac{|t|t^i s^j}{\sqrt{1-t^2}(1-ts)}\,ds\,dt.
\]

`Analysis.polynomialColumn P j` is the product-measure integral of the same
kernel with `P.eval₂ (Rat.castHom ℝ) t` in place of `t^i`.
`Analysis.polynomialColumn_eq_iterated` identifies it with the source's
iterated notation. It is not defined by its proposed formal-coordinate
decomposition. `Analysis.integrable_columnKernel` proves the integrability
needed by finite linearity and Fubini.

`MixedMoments.Zeta.Z` is the product-measure integral of `t^i*s^j/(1-ts)` on
the open unit square. `Zeta.polynomialColumn D j` is the corresponding actual
polynomial integral, and `Zeta.polynomialColumn_eq_iterated` supplies the
iterated form. The polynomial APIs in both analytic modules take
`Polynomial ℚ`; they do not quantify over arbitrary real polynomials.

`Constants.catalan` is the usual series
`∑' n, (-1 : ℝ)^n / (2*n+1)^2`. `Zeta.zeta2` is the reciprocal-square
series. The evaluation of these particular actual integrals is supplied by
`Analysis.M_zero_zero_eq_catalan` and `BoundaryZeta.M_zero_one`, respectively.
The source's optional equality `zeta2 = pi^2/6` is not needed for cancellation
and is not a declared result here.

`MomentRecurrenceData` exposes six proof obligations: the diagonal
recurrence, the two boundary recurrences, and the starts `M(0,0)=4G`,
`M(1,0)=2`, and `M(0,1)=(3/2)ζ`. For an arbitrary real array,
`realM_eq_eval_formalM` remains conditional on this data. The final
application `actualMomentRecurrenceData` fills every field using the actual
analytic declarations. Thus `M_eq_formalM` has only the natural indices as
arguments, rather than an assumed decomposition or boundary evaluation.

The general moment-series specializations in `Decomposition.lean` retain
their explicitly written starting-value hypotheses. They should not be
reported as unconditional evaluations for arbitrary `G`, `ζ`, or sequences.
The stronger actual-integral application is a separate theorem.

## Mapping of every supplied theorem record

In this table, “matched” means the listed source statement or its specified
specialization is supplied by the named declarations and definitions. It is
not a substitute for the final compilation/axiom audit. Every short name is
in namespace `MixedMoments` unless an `Analysis.`, `Zeta.`, `Series.`,
`Constants.`, or `BoundaryZeta.` prefix is written.

| Record | Lean statements checked | Exact coverage and deferred clauses |
|---|---|---|
| MM001 — absolute integrability of M | `Analysis.integrable_productKernel`, `Analysis.integrable_absoluteKernel`, `Analysis.M_eq_productIntegral`, `Analysis.M_eq_swappedIntegral`, `Analysis.integrable_polynomialKernel`, `Analysis.polynomialIntegral_eq_iterated` | Actual monomials and rational-polynomial kernels are covered. The record's arbitrary **real-polynomial** interface is not declared. Polynomial reverse-order equality follows from integrability and Fubini, but there is no separately named polynomial swapped-order corollary. Do not claim the record's full coefficient domain. |
| MM002 — absolute integrability of Z | `Zeta.integrable_kernel`, `Zeta.Z_eq_iterated`, `Zeta.Z_symm`, `Zeta.integrable_polynomialKernel`, `Zeta.polynomialIntegral_eq_sum` | Actual monomials and rational-polynomial kernels are covered. Arbitrary real-polynomial APIs and a separately named two-polynomial iterated/swapped-order theorem are deferred. |
| MM003 — central recurrence and generating series | `central_zero`, `central_succ_ratio`, `central_eq_choose`, `kernel_even`; `inverseSqrtFormalSeries`, `inverseSqrtFormalSeries_square`, `inverseSqrtApproxReal_remainder` | The exact rational recurrence, normalized binomial formula, formal series, and local finite approximations are covered. The analytic infinite-series equality `∑ c_r*t^(2r)=1/sqrt(1-t^2)` for every `abs(t)<1` is **not declared**. The formal square identity is not that analytic summation theorem. |
| MM004 — rational one-variable moments | `Analysis.moment_eq_rat`, `Analysis.moment_odd`, `moment_even`, `moment_eq_if`, `moment_recurrence_positive`, `momentExt_of_neg`, `Analysis.moment_tendsto_zero` | The natural-index actual moments are identified with the rational parity formulas and tend to zero. The positive-index recurrence is expressed over the rational sequence with an explicit integer extension and transferred by `Analysis.moment_eq_rat`. The convention `m(-1)=0` is algebraic; negative-index integrals are not defined. |
| MM005 — M moment series | `Analysis.summable_integral_norm_monomial`, `Analysis.integrable_absoluteKernel`, `Analysis.M_eq_series`, `Analysis.M_eq_rationalMomentSeries` | Matched for all natural `i,j`. The integrated absolute-value control handles the signed expansion on negative `t`; this is more than pointwise geometric convergence. |
| MM006 — M diagonal recurrence/reduction | `Analysis.M_diagonal`, `Analysis.M_finite_diagonal`, `mRationalPart`, `mRationalPart_finite_diagonal`, final application `M_eq_formalM` | Actual diagonal recurrence and finite iteration are matched. The two study branches can be read through the definition of the rational part after actual decomposition; they are not separate named analytic boundary-reduction declarations. Empty finite sums are retained. |
| MM007 — harmonic evaluation of Z | `Zeta.Z_diagonal`, `Zeta.Z_offDiagonal`, `Zeta.harmonic_cast`, `Zeta.harmonicTwo_cast`, `Zeta.Z_eq_zRationalPart`, `Zeta.Z_zero_one` | Matched for natural `i,j`, with `i ≠ j` explicit off diagonal. The quotient uses real/rational subtraction, not truncated natural subtraction; `Z(0,1)=1` checks the orientation. |
| MM008 — M boundary recurrences | `Analysis.M_minus_boundary_recurrence`, `Analysis.M_plus_boundary_recurrence`, `Analysis.M_one_zero`, `Analysis.M_zero_two` | Matched after writing the source index as `d+2`. This covers every source `d≥2` with positive denominators. At index two the old plus-boundary multiplier is zero, so the Catalan start does not propagate to positive even plus indices. |
| MM009 — Catalan start | `Constants.catalan`, `Constants.integral_catalan_kernel_interval`, `Analysis.M_zero_zero_eq_catalan` | Matched for the actual M integral and series-defined Catalan constant. No irrationality is asserted. |
| MM010 — zeta start | `Constants.integral_zetaLogKernel`, `Constants.odd_reciprocal_sq_eq`, `BoundaryZeta.M_zero_one` | Matched for actual `M(0,1)=(3/2)*Zeta.zeta2`. The direct logarithmic-kernel representation and odd reciprocal-square evaluation justify the constant without a Basel-value assumption. |
| MM011 — optional pi evaluation | No project declaration proving `M(0,1)=pi^2/4` or `Zeta.zeta2=pi^2/6` | Deferred. Neither the ordinary proof in the study nor a possible mathlib theorem is evidence that this record has been instantiated in the project. |
| MM012 — rational boundary arrays/closed forms | `kminus`, `kplus`, their start and recurrence theorems; `hStar`, `hStar_pos`, `hStar_step`, `hStar_even`, `hStar_odd`; four parity-specific `kminus_*_closed`, `kplus_*_closed` theorems; `two_step_recurrence_unique` | The rational arrays, normalization, and finite closed sums are matched with all denominators and empty sums controlled. Generic real recurrence uniqueness is declared; there is no separately named rational uniqueness theorem for the pair of boundary arrays. The recursive definitions themselves fix the arrays uniquely. |
| MM013 — universal M decomposition | `formalM`, `realM_eq_eval_formalM`, final applications `actualMomentRecurrenceData`, `M_eq_formalM` | The final actual-integral application matches the stated specified-coordinate identity for natural indices, with the integer kernel's negative/odd zero convention. Its absence of decomposition or boundary hypotheses is essential. The earlier generic recurrence theorem alone would leave this record conditional. |
| MM014 — exact polynomial defect identity | `rationalWitness`, `catalanWitness`, `polynomialDefect`, `exact_defect_identity`, `polynomialDefect_eq_formalContactSeries_coeff`, final `integral_exact_defect` | Matched for rational polynomials and natural columns by the actual-integral application. The Catalan witness uses the equivalent finite support sum `4*∑ p_i*kernel(i-j)`; its nonzero indices are exactly `i=j+2r`. The defect is identified with formal-series coefficients and, for low orders, the finite approximation coefficients used by analytic contact. It is not a separate general derivative/Taylor-series theorem. |
| MM015 — analytic contact/jet vanishing | `polynomial_coeff_zero_of_isBigO_eval_pow`, `polynomial_eval_isBigO_pow_of_coeff_zero`, `analyticContact_nhds_iff_coefficientContact`, `analyticContact_right_iff_coefficientContact` | Matched for real polynomials and, crucially, the specific rational-polynomial function `tP(t)/sqrt(1-t^2)-D(t)`. The record's universal theorem for every real analytic `F` is deferred. This specialization supplies all contact information needed by MM016. |
| MM016 — rational-polynomial Taylor-contact cancellation | `analyticContact_implies_coefficientContact`, `analyticContact_nhds_implies_coefficientContact`, `integral_cancellation_of_coefficientContact`, `integral_cancellation_of_analyticContact`, `integral_cancellation_of_analyticContact_nhds`, `integral_analyticContact_witnesses` | The final big-O applications match the principal target with actual integrals and explicit witnesses. `P,D : Polynomial ℚ`, `L,j : ℕ`, the precise contact filter, and `j<L` remain visible. Lean permits `L=0`, which is harmless because there is then no admissible column. Thus the source's `L≥1` cases are included. The named existential big-O witness theorem uses positive-side contact; the two-sided equality also supplies the same explicit rational witnesses. |
| MM017 — polynomial-test-function cancellation | `pairedEntry`, `pairedDefect`, `paired_entry_zeta_coordinate`, `paired_cancellation`, `paired_cancellation_of_contact`, `paired_cancellation_of_natDegree_lt`; both analytic `polynomialIntegral_eq_sum` declarations | Formal-coordinate pairing and evaluated formal-pairing cancellation are covered. The actual two-polynomial integrals have finite expansions, but no final named equality between those integrals and the evaluated `pairedEntry` or corresponding actual-integral paired cancellation is declared. That bridge is deferred; do not silently substitute the formal pairing for the actual integral. |
| MM018 — unique contact truncation | `contactTruncation`, `contactTruncation_coeff`, `contactTruncation_contact`, `contactTruncation_analyticContact` | Constructive rational contact and its exact coefficients are covered. The truncation coefficients vanish at every `j≥L`. No declared uniqueness theorem among degree-less-than-`L` polynomials, or classification of all solutions by divisibility of their difference by `X^L`, is present. Those additional clauses are deferred. |
| MM019 — exact rational series tail bound | `Series.momentSeries_tail`, `Series.momentSeries_upper_bound`, `Series.momentSeries_tail_bound`; actual series and moment identification theorems | The exact tail and its nonnegative upper bound are supplied for nonnegative recurrent sequences with the explicitly required decay. The upper-bound theorem requires `2≤i+N`. For the source's `N≥1` range this omits exactly `i=0,N=1`, which involves `m(-1)=0`. Actual-moment premises can be discharged by the analytic/rational-series declarations; any added named actual-integral corollary must retain the range. There is no general negative-index sequence hypothesis hidden in the natural-index theorem. |
| MM020 — rational adjacent diagonal | `mRationalPart_adjacent_diagonal`, `Series.momentSeries_adjacent`, `Series.momentSeries_one_zero`, `Analysis.M_eq_momentSeries`, `Analysis.M_one_zero` | The series identity gives actual adjacent entries with source `i≥2`; the source endpoint `i=1` is `M(1,0)=m(-1)+m(0)=2`. Together these cover the source statement. The rational-array theorem also includes its explicit `-1` convention. There is no single named actual-integral theorem packaging both cases. |
| MM021 — coefficient-field extension | No subfield-parametric polynomial or cancellation interface | Deferred. The public main interface remains rational-polynomial cancellation. Arbitrary real coefficients cannot be inserted while retaining the conclusion `ℚ+ℚG`. |

## Contact, indices, and tail restrictions

`analyticContactFunction P D x` is exactly
`x*(P.map (Rat.castHom ℝ)).eval x / Real.sqrt (1-x^2) - (D.map (Rat.castHom ℝ)).eval x`.
The positive square-root branch is retained near zero: the finite inverse
square-root approximation has constant coefficient one and its rationalizing
denominator tends to two. This is the substantive analytic bridge, not a
definition of big-O contact in terms of coefficients.

The right-sided filter is exactly `𝓝[>] 0`; the two-sided filter is `𝓝 0`.
The right-sided forward implication proves coefficient vanishing using the
eventual positivity of `x`, and does not merely assume a two-sided bound.
The final actual-integral corollaries should consume these respective proven
implications. No integrability, decomposition, or boundary-constant premise
should remain on those corollaries after application of the actual bridge.

The column condition is strictly `j<L`. The example `P=1,D=X,L=3` has
specified triples `(-3/2,4,0)`, `(3/2,0,0)`, and `(5/4,0,0)` in columns zero
through two. Column three is `(-1/8,0,3/4)`. This verifies the boundary of the
coefficient-cancellation mechanism; it is not an arithmetic nonmembership
counterexample.

Index differences inside `kernel` are formed in `ℤ` before testing negativity
and parity. Natural subtraction in `mRationalPart` is guarded by its correct
branch. Off-diagonal harmonic denominators use subtraction in the coefficient
field. `momentExt` explicitly totalizes all negative indices to zero, but this
is an auxiliary algebraic convention. It does not create negative-index
analytic moments, nor broaden the supplied oracle's accepted input domain.

The tail-bound range `2≤i+N` prevents natural subtraction from replacing the
source's exceptional negative index with zero. In particular, substituting
`i=0,N=1` into the displayed natural-index RHS would use `a 0+a 0`, not the
source's `m(-1)+m(0)`. Any endpoint extension needs a separately proved case
with the explicit convention; the present range should not be omitted in a
report of the theorem. The generic sequence theorem also explicitly assumes
nonnegativity, its recurrence, and convergence to zero. Those assumptions
are proved for the actual canonical sequence, not for arbitrary sequences.

## Formal coordinates and analytic claims

`Coordinates` is the free space `Fin 3 → ℚ`.
`Coordinates.eval G ζ v = v₀+v₁G+v₂ζ`. No injectivity of this evaluation map
is asserted or used. A nonzero designated third coordinate proves failure
of that formal coordinate cancellation only. It does **not** prove that the
evaluated real number lies outside `ℚ+ℚG`.

The integral convergence arguments are independent of this free-coordinate
calculus. The M proof controls signed geometric terms by `absoluteMoment` and
a summable series of integrated norms. The Z proof uses nonnegative geometric
terms. Their geometric identities are established on the open rectangles and
transferred almost everywhere. Totalized endpoint values of Lean division and
square root do not serve as an integrability proof.

The boundary substitutions use interior derivative hypotheses together with
integrability of the original and transformed integrands. They do not demand
regular derivatives at the singular endpoints. The Catalan logarithmic-kernel
expansion has integrated absolute-value control despite alternating signs.
The zeta logarithmic-kernel expansion has nonnegative terms.

No reviewed theorem claims Catalan irrationality, independence of
`1,G,zeta2`, determinant nonvanishing, a two-adic valuation result, or the
original source's particular parameterized row construction. The source
repository path containing “irrational” does not expand this project's proof
scope.

## Verification boundary and acceptance

The source statements and proof interfaces support the bounded final claim:
actual-integral rational-polynomial cancellation under the displayed analytic
contact condition, with rational witnesses and `j<L`. The other clauses
listed above remain separately identified. No new analytic study is needed
to state that scope accurately.

Acceptance requires fresh successful builds of the repaired tail module and
the actual application module, a default full-project build, and a stable
project-wide declaration/type/axiom audit. The audit must account for every
public declaration, reject placeholders/custom axioms, and inspect transitive
dependencies of the actual application theorems. The standard logical axioms
`propext`, `Classical.choice`, and `Quot.sound` are distinct from unproved
project assumptions.

Earlier 17,805 supplied exact checks, 20,072 independent checks, 993 provenance
checks, 77 rational examples, and the 111-theorem rational audit are valuable
separate evidence. None is a whole-project analytic pass. The final audit
result and source hashes govern the final verification claim; this review
must be reconciled with any last edits to `Applications.lean` or
`TailBounds.lean` before packaging.

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
