# Continuation review: splitting, arithmetic, and common lifts

This expanded edition continues the corrected baseline
`a4a28796bdd63c5cbddbfba698c95d34728bd94c`; it does not restart the
completed foundational study. It adds four mathematical chapters, two
proof-level source comparisons, a reconstructive dependency map, and
reproducible exact checks. No source books or rendered source pages are
distributed.

## Main mathematical outputs

1. **Invariant complements become a computable obstruction.** A chosen
   linear section gives a block $C$, changed by $Ah-hB$. The cokernel
   classifies extensions with fixed endpoints. Reverse intertwiners give
   complete trace witnesses over a field; divided differences construct
   the inverse for coprime annihilators. Cyclic presentations explain
   Jordan gluing. Over integer lattices, a nonzero resultant can leave
   torsion invisible to rational trace tests.
2. **Averaging has a precise common mechanism.** A separability tensor
   repairs linear maps, sections, and retractions. Polynomial divided
   differences, group averaging, and matrix-unit formulas are derived
   explicitly. The chapter separates semisimplicity over one field from
   separability, and separates allowed extensions over a quotient algebra
   from extensions of its endpoint modules over a larger ring.
3. **Integral Fourier data live in a lattice.** The chapter proves the
   integral CRT defect and its resultant order, prime trace reconstruction,
   general cyclotomic trace divisibility, and prime-power overlap jets.
   Under exact spectral norm identities, the all-order sign certificate is
   membership in $J_m+2L_m$. Odd-order component parity is a consequence
   of the absence of two-torsion in the CRT defect. Even order requires
   the actual half-shifted lattice test.
4. **The fixed compression failure has an explicit residual.** Fiber
   averaging splits the real cyclic algebra orthogonally; individual
   normalized symmetric sign lifts have an exact binomial count.
   In the fixed core-nine fixture, the product theorem leaves six
   candidates, all with nonzero Gram defect $8(S_p-S_k)$ killed by
   compression. An unrestricted real lift exists, showing exactly what
   the discrete domain adds.

These are classical mechanisms and original explanatory calculations.
No literature-priority claim, search speedup, new search campaign, or
universal Hadamard existence result is claimed.

## Independent mathematical reviews

Different AI agents reviewed the completed manuscripts rather than merely
checking their outlines. Their conclusions are evidence of adversarial
review, not human peer review or formal proof checking.

**Sylvester and extensions.** The review rederived section-change signs,
endpoint-equivalence signs, the free-resolution cocycle, Baer addition,
reverse trace orientation in arbitrary characteristic, the Bézout inverse,
Smith factors, Jordan types, and the integral Ext resolution. It found one
wording error: the resultant $-2$ has *absolute value* two, which is the
order of the obstruction. This is corrected. A separate checker, importing
none of the author checker, tests 819 endpoint pairs, 8,761 extension blocks,
819 resultant identities, and 2,888 square-zero inverse cases.

**Averaging and separability.** Review confirmed the outer bimodule
identities, the repair lemma, derivative criterion, inseparable example,
group converse, and denominator-free matrix-algebra tensor. It corrected
the displayed telescoping explanation for the cubic repair: the missing
left/right factors are now present. It also distinguished a tensor-defined
coherent repair from an arbitrary vector-space projection onto one fixed
intertwiner space.

**Integral spectral gluing.** Independent reviews confirmed the full
trace inverse, the all-order affine theorem including order one, the
odd-order torsion reduction, the even-order counterexample, the distinction
between pairwise and whole-block gluing, Hasse-jet equivalence, and the
order-nine reduction to $I_6\oplus3E_3$. A separate Ramanujan-sum
calculation verified both inverse-matrix products at eleven fixed orders.
The nonsymmetric example was checked with the stated circulant convention:
complementary sign rows can fail the standard Williamson block array.
Symmetry or sufficient amicability remains necessary for that inference.

**Compression.** Independent coefficient arithmetic verified the entire
fixed set of 27 labeled lifts, six product-condition survivors, zero full
solutions, and every residual polynomial. It also verified the 27/648
counting distinction, nine single-row compression histograms, six rational
projector cases including even parameters, and the unrestricted real lift.
The integrated prose clarifies sums versus means, the zero-fiber affine
map, the singleton $\Delta(0,0)$, and the use of symmetry before squaring.

## Source comparison and local corrections

Contiguous proofs were inspected in Xi I–III, Hungerford, and Grillet,
with selected additional Lang pages. The two comparison documents give
exact printed/PDF ranges and evidence levels.

- Xi II contains both a quotient-lifting Jordan proof and a later
  image–kernel filtration construction. The latter remains useful for
  building an actual basis.
- The books' Cayley–Hamilton dependencies differ. Combining their routes
  without an independent annihilator argument can create circularity.
- Xi already proves tensor universality and exterior-basis independence.
  The graduate constructions add module generality and exactness, not a
  universal property missing from Xi.
- Xi III contains both the Hermitian and averaged-projection proofs of
  Maschke. Hungerford's radical/regular-trace proof has different,
  substantial prerequisites.
- Xi III proves finite-rank PID submodules free and a finite-module
  integrality criterion. Its local general invariant-factor statement
  still needs a complete proof from another inspected route.
- Lang's cyclotomic degree and integer-ring arguments use valuation,
  ramification, localization, and discriminant theory. They are an
  arithmetic extension rather than the shortest undergraduate route to
  cyclotomic irreducibility.

Two independent inspections of the supplied Xi I scan confirmed the
local coefficient typo in Example 7.80, printed page 193/PDF page 199:
the depressed cubic discriminant is $-4p^3-27q^2$. A symbolic
resultant computation and the example $x^3+x$ check the correction.
The general cubic exercise three pages earlier contains the correct term.
The earlier finite-rank tensor correction and Grillet convention
distinction are preserved.

The new Xi II proof readings have extracted-text evidence but not a new
visual verification of every formula glyph; the prescribed helper was
unavailable and image requests returned no usable renders. That boundary
is stated in the operator comparison. It does not justify claiming a
full scan audit. Xi I and III's cited new scan passages were rendered
privately. No whole-book or exercise-by-exercise replacement claim is made.

## Reproducible checks and build evidence

From this directory:

```sh
python3 scripts/check_examples.py
python3 scripts/check_phase2.py
python3 scripts/check_sylvester_review.py
bash scripts/build.sh
python3 scripts/audit_deliverable.py
```

The baseline checker retains its 18 groups. The continuation runner has
7 Sylvester, 5 averaging, 12 integral CRT, and 4 lifting groups, plus
one symbolic source-erratum check: 47 primary groups in total across
the two runners. The independent Sylvester checker is additional.
The continuation evidence records the executed script hashes and outputs.
The build record binds the PDF to its manuscript inputs; the audit checks
local links, hashes, section coverage, final LaTeX diagnostics, and source
separation. Visual inspection is recorded separately in the continuation
manifest after the final build. The final PDF has 125 pages; physical
pages 9, 62, 68, 73, 84, 86, 95, 96, 101, 109, and 111 were visually
inspected. They cover the dependency diagram, extension formulas,
averaging, the affine-lattice theorem, integral overlaps, the core-nine
proof, and both source-comparison formats. No clipping, missing glyphs,
or unreadable formulas were found on those pages. The final LaTeX pass
has no warnings or overfull boxes.

Passing finite checks is not a proof of a universally quantified theorem.
The written derivations establish the general claims under their stated
hypotheses; the checks target signs, orientations, counts, characteristics,
and small counterexamples where errors are easy to miss.

This reviewed original edition is prepared for authorized publication on the
existing public `research/algebra-structural-toolkit` branch. Source books and
source-page images remain in private reading storage outside the repository.
