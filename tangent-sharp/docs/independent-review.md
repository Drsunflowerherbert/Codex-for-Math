# Review of the compiled conditional tangent project

## Assessment

The compiled main theorem and the compiled summability extension have the
requested meanings. No mathematical gap, incorrect quantifier, hidden
Diophantine assumption, or proof placeholder was found in the reviewed source.
Both results remain conditional on the explicitly displayed `PiDiophantine`
hypothesis. This review does not establish that hypothesis.

This is a separate review pass over the complete source chain and compiled
statements. The reviewer also contributed the initial ordinary proof and
`NearestPole.lean`; it should not be described as a blind review by an author
with no involvement in those components.

## Concrete checks

1. **The hypothesis matches the request.** `PiDiophantine` quantifies over
   every real exponent `ν > 2`, then chooses a threshold `Q`, then quantifies
   uniformly over all `q : ℕ` with `Q ≤ q` and `0 < q`, and all `p : ℤ`.
   The numerator and denominator are cast to the reals before division.
   Positive natural denominators enumerate exactly the positive integer
   denominators in the ordinary statement. Allowing the natural threshold
   to be zero makes no difference: it can be replaced by `max Q 1`.
   The inequality is the requested `q ^ (-ν) ≤ |π - p/q|`, with no omitted
   constant and no change to the order of quantifiers.

2. **H remains visible and unproved.** `Hypothesis.lean` defines a proposition;
   it does not supply an instance, assert an axiom, or prove the proposition.
   Both main limit statements and both absolute-series statements have an
   explicit argument `(h : PiDiophantine)`. The limit uses its exponent-three
   instance, and the series extension uses its exponent-`5/2` instance.

3. **The chosen odd integer is actually nearest.** The definitions are
   `poleIndex n = floor(n/π)`, `poleDenom n = 2*poleIndex n + 1`, and
   `poleOffset n = n - poleDenom n*π/2`. Positivity and oddness are proved.
   The two floor inequalities prove `|poleOffset n| ≤ π/2`, and
   `poleOffset_nearest` compares this distance with every odd denominator
   `r : ℤ`, including negative denominators. Its conclusion permits ties.
   Multiplication by the positive constant `2/π` converts that proved
   comparison into the nearest-odd comparison for `2n/π`.

4. **The eventual denominator argument is justified.** The source proves
   `poleDenom n ≤ 2n` for `n ≥ 1`, and proves that every fixed threshold is
   eventually exceeded. Thus applying H at `q = poleDenom n` is legitimate;
   neither denominator growth nor positivity is merely assumed.

5. **The pole-to-tangent bridge has the correct factor and exponent.** The
   compiled identity is
   `|x - q*π/2| = (q/2)*|π - 2*x/q|` for `q > 0`. Its consequence is the
   lower bound `(1/2)*q^(1-ν)`. The compiled cosine identity and sine chord
   inequality give `|cos x| ≥ q^(1-ν)/π`, and hence
   `|tan x| ≤ π*q^(ν-1)`. The numerator supplied to H is the integer `2n`.
   The positive cosine lower bound supplies the nonzero denominator needed
   when taking the reciprocal.

6. **The signed main limit is proved, with positive indexing.** The estimate
   at exponent three is `|tan n| ≤ 4π*n²` eventually. `LimitComparison.lean`
   divides by the positive cube for `n ≥ 1`, obtains the majorant `4π/n`,
   and uses its limit zero. The theorem
   `tan_div_cube_positive_tendsto_zero` explicitly enumerates the requested
   positive integers by `n+1`; it is not dependent on the zero term of the
   alternate natural-index sequence. The saved clean module build is
   `logs/limit-01.log`.

7. **The absolute-convergence extension uses a summable majorant.**
   `Summability.lean` obtains
   `|tan n|/n³ ≤ π*2^(3/2)*n^(-3/2)` eventually. The real-power algebra and
   comparison are proved in Lean, including the identity
   `n^(3/2)/n³ = n^(-3/2)` for positive `n`. The standard `p`-series theorem
   and eventual norm comparison then prove summability. The explicit
   positive-index theorem is `summable_abs_tan_div_cube_positive`.
   `logs/summability-01.log` records its clean module build after the main
   limit had passed.

8. **Ordinary tangent values are finite.** `NonPole.lean` proves nonzero
   cosine at every integer argument using mathlib's proved irrationality
   theorem for π. It neither uses nor attempts to prove H. This covers the
   finite initial portion of the ordinary series. Lean's totalized division
   at the optional natural-index zero term does not change either positive
   sequence theorem.

9. **The ordinary proof is consistent with the formal argument.** The proof
   in `docs/mathematical-proof.md` gives an explicit threshold, handles floor
   endpoints and nearest-pole ties, and has the same constants and exponents
   as the compiled main and extension sources. The simpler pointwise
   argument at exponent `5/2` is sufficient for the requested cubic series;
   an aggregate spacing argument is unnecessary. Standard irrationality of
   π is used only to explain that all classical initial terms are defined.

10. **The version and evidence records are concrete.** `lean-toolchain`
    pins `leanprover/lean4:v4.24.0`; `lakefile.toml` and `lake-manifest.json`
    pin mathlib commit `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` and exact
    transitive dependency revisions. The saved setup reproducibility check
    reports Lean 4.24.0 and an unchanged manifest hash. Earlier 4.19.0 setup
    failures are retained as historical logs, rather than presented as
    successful builds. Mathematical-proof, reusable-lemma, and passing-main
    milestones are preserved with theorem statements and progress records.

## Direct compiler and source audit

During this review, the pinned compiler successfully imported the compiled
`Limit`, `NonPole`, and `Summability` modules and printed the requested theorem
types. Direct `#print axioms` checks were run for the eventual quadratic bound,
both main limit theorems, the natural-argument nonpole theorem, the eventual
series majorant, and both absolute-series theorems. Every result listed exactly
the standard foundational axioms:

```text
[propext, Classical.choice, Quot.sound]
```

The previously saved nearest-pole and bridge inventories show the same list.
No `sorryAx` or project-defined axiom was present. A source scan of
`TangentLimit.lean` and all `TangentLimit/*.lean` found no `sorry`, `admit`,
`sorryAx`, `unsafe`, or `axiom` declaration. No source code was changed during
this review.

## Verification scope and remaining limits

The review checked the ordinary argument, the project proof source, compiled
theorem statements, module build evidence, and direct axiom inventories. It
does not reprove H or independently rebuild the entirety of mathlib from
source. The use of standard Lean foundational axioms and pinned mathlib is
the normal trust boundary of this formalization.

The supplied starter archive was assessed as reference material, rather than
as a source of an asserted theorem establishing H. Its saved inspection record
reports all 38 manifest hashes matching and no supplied Lean implementation;
this review read those records but did not rerun that archive extraction.

At this review pass, both mathematical goals and their explicit positive-index
formal statements have passed their module builds. The final aggregate build,
updated user-facing statement inventory, and distribution archive are final
packaging checks handled separately. No unresolved mathematical or theorem
semantic blocker was identified.
