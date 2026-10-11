> Publication note: the review reports 3139 build jobs at an earlier stage; the delivered final build receipt records 3138 jobs. This numerical build-progress count does not change theorem coverage or the 78 declaration audits.

# Independent review of the sharp tangent-series argument

Reviewed on 2026-10-11, starting at approximately 03:05 UTC. The final independent
source and consumer checks completed successfully at **03:10:50 UTC**.

**Final verdict: the sharp absolute summability target is compiler verified**, with
`PiDiophantine` retained explicitly. Divergence for every real `s ≤ 1` is proved
unconditionally. The printed target dependency lists contain only Lean's standard
foundational axioms `propext`, `Classical.choice`, and `Quot.sound`.

This document records both the earlier mathematical review and the later fresh
verification. Earlier sections' pending-status remarks describe their stage at
the time; the final verification section supersedes those remarks.

## Conclusion at the ordinary-proof stage

The proposed proof is mathematically correct. Under the explicitly assumed
`TangentLimit.PiDiophantine`, the absolute tangent series over positive integers
is summable for every real exponent `s > 1`. The converse, for every `s ≤ 1`,
uses only the proved irrationality of π and does not need that hypothesis.
Nothing in this argument asserts conditional convergence of the signed series.

The hypothesis is an input. Irrationality alone supplies only a positive lower
bound for each fixed exceptional denominator. It does not establish the
all-exponent Diophantine statement.

## Essential checks

1. **Exceptional denominators.** For fixed positive integer `q`, irrationality
   gives a positive distance from `qπ` to the integers. Taking the minimum over
   the finitely many exceptional denominators then gives a uniform positive
   constant. A minimum over finitely many *numerators* would not suffice;
   numerator uniformity must first be proved for each denominator.

2. **Dyadic geometry.** For `N ≥ 1` and `N ≤ n < 2N`,
   `0 ≤ floor(n/π) < N`, since `π > 2`. Thus the odd pole denominator is positive
   and below `2N`, and the nonzero difference of two pole indices has absolute
   value below `N`. All denominators used by the spacing proof therefore fall
   inside the range of the uniform lower bound.

3. **Zero pole-index difference.** When two pole indices are equal, signed
   offsets differ by the distinct integer arguments. Their separation is at
   least one. This case cannot be sent to a positive-denominator approximation
   lemma. The chosen block scale is at most one half, so it also covers this
   case.

4. **Signs and packing.** The approximation bound separates signed offsets.
   Absolute distances on opposite sides need not be separated, so each sign
   is packed separately. On either side, the first absolute distance is at
   least `δ`, and consecutive ordered distances differ by at least `δ`.
   The `j`-th positive distance is therefore at least `jδ`. There are at most
   `N` points per side.

5. **Analytic constant.** The existing theorem supplies
   `|tan n| ≤ π / (2 |d_n|)`. Applying the one-sided packing estimate twice gives
   the block bound `(π/δ) H_N`, exactly as in the saved proof. No stronger
   cotangent bound is required.

6. **Exponents.** Taking `α = (s+3)/2` gives `2 < α < s+1` exactly when `s > 1`.
   The weighted block exponent is `(1-s)/2 < 0`. The estimate
   `H_(2^j) ≤ j+1` follows by adding at most one per doubling. Its product with
   the decaying geometric factor is summable.

7. **Unconditional lower bound.** Nonzero cosine at every integer argument
   permits the tangent subtraction identity. Since `0 < sin 1` and both cosine
   factors have absolute value at most one,
   `sin 1 ≤ |tan n| + |tan(n+1)|`. When `s ≤ 1` and the base is a positive
   integer, the corresponding weight is at least its reciprocal. Pairing
   `2j+1` and `2j+2` therefore dominates
   `sin 1 / (2(j+1))`. This argument covers negative exponents and the endpoint
   `s = 1`.

## Formalization hazards to check in the final audit

- The sharp positive-integer theorem must explicitly use `(n+1 : ℕ)` with a
  real exponent in the denominator, and retain a `PiDiophantine` argument.
- The nonsummability theorem must have no `PiDiophantine` argument, instance,
  or axiom in its dependency closure.
- At base zero, real powers are totalized in Lean. A theorem over all naturals
  can be used as a shifted precursor, but the final positive statement must
  not rest on a zero-index convention.
- Any uniform Diophantine helper must quantify over all integer numerators,
  not just positive numerators, because signed pole-index differences occur.
- Packing requires both a nonzero first-distance bound and pairwise spacing.
  Pointwise bounds alone yield a weaker threshold and cannot establish the
  target.
- Summability of weighted dyadic block sums must be connected to summability
  of the original nonnegative sequence by a proved partition/reindexing
  argument. A standalone geometric estimate is not the target.
- No `sorry`, `admit`, new axioms, or unconditional π Diophantine claims may
  enter the final theorem dependencies.

The completed formal source, exact theorem types, fresh compiler logs, pins,
hashes, and `#print axioms` output remain to be reviewed after integration.

## Source review of the integrated development

At approximately 03:07 UTC, independently read all seven new source modules:
`UniformDiophantine`, `PoleSpacing`, `FinitePacking`, `DyadicSummability`,
`Divergence`, `BlockEstimates`, and `SharpSummability`. No mathematical defect
or unintended strengthening of hypotheses was found.

The implementation resolves the essential obligations concretely:

- `piDiophantine_uniform` states a weighted integer-distance bound for every
  positive natural denominator and every integer numerator. Its finite-cutoff
  induction obtains a fixed-denominator gap from proved π irrationality.
- `blockDelta_le_abs_poleOffset_sub` uses a positive natural pole-index
  difference in either orientation, and treats equal pole indices separately.
  No approximation at denominator zero is used.
- `sum_reciprocal_abs_le_harmonic` splits a labeled finite set by sign. Its
  one-sided lemma first derives injectivity from strict positive spacing and
  then orders the actual image points with `Finset.orderEmbOfFin`.
- `sum_range_two_pow_eq` proves an actual finite dyadic partition, retaining
  the zero term separately. `summable_of_dyadic_block_bound` bounds every
  finite partial sum by the dyadic partial sum, hence by a convergent majorant.
  The integration therefore proves summability of the original sequence.
- `Divergence` uses the original series plus its one-step shift, rather than
  disjoint pairs. This valid simplification dominates a positive constant
  times the shifted harmonic series. Its final theorem has only `(s : ℝ)` and
  `(hs : s ≤ 1)` as arguments.
- `BlockEstimates` uses monotonicity of positive-base real powers and the
  existing sine-chord tangent estimate. It contains no Diophantine assumption.
- The final positive-integer equivalence retains `(h : PiDiophantine)` and
  delegates its necessary direction to the separate unconditional theorem.
  There are no new claims about conditional convergence of signed series.

A source scan of the project modules found no `sorry`, `admit`, `axiom`, or
`unsafe` token. Component compiler and axiom logs for dyadic infrastructure
and divergence were also read, but fresh independent final checks remain
pending. The integration was undergoing its first compile at review time, so
this section does **not** claim compiler-verified target completion.

## Final independent verification

Re-read the final `SharpSummability`, `BlockEstimates`, and narrowed-import
`FinitePacking` sources after project integration. The sufficient direction now
uses the reusable `summable_of_dyadic_rpow_harmonic_bound` directly. This keeps
the same valid proof: `α = (s+3)/2`, weighted block exponent `α-1-s < 0`, harmonic
packing bound, and the proved dyadic summability bridge. A redundant dyadic-power
identity was removed from `BlockEstimates`; no mathematical obligation was lost.

Independently executed these commands from
`<project>`, after sourcing `scripts/environment.sh`:

```bash
lake env lean TangentLimit/SharpSummability.lean
lake env lean <historical-workspace>/scratch/AuditSharp.lean
```

The direct fresh source check started at 2026-10-11 **03:10:38 UTC**, finished at
**03:10:50 UTC**, exited **0**, and produced no diagnostics. Logs are
`<historical-workspace>/scratch/independent-direct-check.log` and the adjacent `.meta` file.
No Lake build metadata was edited by these direct Lean checks.

The standalone consumer check started at **03:10:38 UTC**, finished at
**03:10:48 UTC**, and exited **0**. The independently written `AuditSharp.lean`
imports the project's final public entry point, prints the hypothesis
definition, checks the target and separate divergence statements, prints their
axiom dependencies, and elaborates three explicit consumer examples. Logs are
`<historical-workspace>/scratch/independent-axiom-check.log` and the adjacent `.meta` file.

The final printed target type is exactly:

```lean
TangentLimit.summable_abs_tan_div_rpow_positive_iff
    (h : TangentLimit.PiDiophantine) (s : ℝ) :
  (Summable fun n : ℕ =>
    |Real.tan ((n + 1 : ℕ) : ℝ)| / (((n + 1 : ℕ) : ℝ) ^ s)) ↔ 1 < s
```

The independent unconditional declaration has exactly these mathematical inputs:

```lean
TangentLimit.not_summable_abs_tan_div_rpow_positive
    (s : ℝ) (hs : s ≤ 1) :
  ¬ Summable (fun n : ℕ =>
    |Real.tan ((n + 1 : ℕ) : ℝ)| / (((n + 1 : ℕ) : ℝ) ^ s))
```

`#print TangentLimit.PiDiophantine` confirms the original definition is unchanged:
for each real `ν > 2`, a cutoff is assumed after which every positive natural
denominator and every integer numerator obey the prescribed approximation lower
bound. No unconditional proof or instance of that hypothesis was introduced.

`#print axioms` for the natural and positive sufficient theorems, the positive
equivalence, the exponent-one divergence theorem, the general real-exponent
divergence theorem, and the hypothesis definition returned only
`[propext, Classical.choice, Quot.sound]`. In particular there is no `sorryAx` or
custom mathematical axiom. An independent repeat source scan of all project
modules found no `sorry`, `admit`, `axiom`, or `unsafe` token.

Also inspected root's final full build, 76-exported-declaration inventory,
source audit, and the two-private-helper audit. These report a successful
3139-job build, 37 original declarations plus 39 additions, and only standard
foundational axioms. These root-generated logs corroborate the independent
target checks; they are current-run logs rather than historical publication
evidence.

### Pins and reviewed source hashes

The independently observed compiler is Lean **4.24.0**, compiler commit
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`. The manifest pins mathlib to
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The original project HEAD remains
`d00a89dd9ce6c8ef782234d28c93e69cb712c947` on local branch
`codex/tangent-sharp-20261011`; the new sources were reviewed as local changes.

| Reviewed file | SHA-256 |
| --- | --- |
| `TangentLimit.lean` | `adfc96738b249377095a6be42eb0d739183e1d849a97a5a2f20d870fa3029de9` |
| `UniformDiophantine.lean` | `610813720b74dff4f03dea571bba7fd89d8915784be1092d88ce64c8a8ec18c2` |
| `PoleSpacing.lean` | `9faf23dbd9c48d93538e86746e13bfc20fe511aaa440bf8c01ca7f58acf35f48` |
| `FinitePacking.lean` | `f878ddd581eba232c227dc77973d02f3c898c6888419d032479b0576914c76c6` |
| `DyadicSummability.lean` | `8407909d22436551d60b8e71e7e88e790c53019c8b1ae647962a9dc755a8132c` |
| `Divergence.lean` | `6c3c2ca8bf67d07e29c1dbf4d845b214fac1cd905b81c00468065c32905e7158` |
| `BlockEstimates.lean` | `2eb3fc83f5f9d530875b840a5fc5424fb7cf18892721ed1d28500de256f6c303` |
| `SharpSummability.lean` | `70600b3724d7bc17b55a0fbe5ee5c51b762db7528d4579fd5c0db2e74456e1b0` |
| Independent `AuditSharp.lean` | `67bc26db193f594ae913abbdd96eec53c415ecfecf5cb8e51e0df28d11b18a7a` |

The review found no remaining mathematical or formal blocker to the requested
conditional absolute-summability equivalence. Its explicit limitation is that
`PiDiophantine` remains assumed. No claim concerning conditional convergence of
the signed series is made. This review did not push, open a PR, merge, or alter
credentials, permissions, or source code.
