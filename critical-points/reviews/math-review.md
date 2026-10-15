# Independent mathematical review

Review date: 15 October 2026. Reviewer: the independent `math_review` research
agent, which did not author the study, examples, or implementation.

**Verdict: PASS for the first edition.** No mathematical blocker or required
correction was found in the files identified below. This is an ordinary
mathematical review, supported by separate exact symbolic computations; it is
not a proof-assistant certificate or a proof of correctness of the Python
implementation on every input.

## Exact reviewed scope

The following SHA-256 values identify the frozen files reviewed:

| File, relative to `critical-points/` | SHA-256 |
| --- | --- |
| `STUDY.md` | `e7c4c3578a0fbf0ae7ac8207a501cdfe5d057b8b9903bfdf3f1b30a4b7d73751` |
| `EXAMPLES.md` | `62fe0b982b0c1d5a712eeeda4785946036cf4f70d73a42f12464c961789e6a85` |
| `README.md` | `d99e22e450edc221ebefec68c8c16c4062bfa746f2473c6217c9e72432fc7185` |
| `examples.json` | `a42b30963b1737c4a5651887bdd78a4ebd4f463d326feb345216c59d56b9a832` |

The implementation was read to check the documentation's mathematical contract,
but its independent implementation audit is recorded separately. This review
does not cover later changes to the four hashed files.

## Findings on the proof

1. **Hypotheses and normalization are sufficient.** A real symmetric rank-one
   Hessian has a nonzero diagonal entry. The prescribed rational shear, with a
   coordinate interchange when needed, sends it to
   `diag(0, lambda)` after multiplication by the sign of that entry, with
   `lambda > 0`. The maps are invertible and preserve degree. The sign equals
   the sign of the unique nonzero eigenvalue. Subtracting the original critical
   value and reversing minimum/maximum when the sign is negative are both
   handled correctly.

2. **The analytic splitting includes the non-isolated case.** The analytic
   implicit function theorem applies because `F_yy(0) != 0`. Taylor's integral
   remainder has value `lambda/2 > 0`, so its positive analytic square root
   supplies a locally invertible transverse coordinate. This proves
   `F = g(x) + z^2` analytically, including when `g` is identically zero.
   Neither a merely formal substitution nor an unproved isolation hypothesis
   is used to justify real inequalities.

3. **The classification is exhaustive.** A nonzero analytic residual has a
   finite first nonzero order, at least three. Even positive leading terms
   produce strict extrema; odd order produces both signs on the critical
   graph; even negative leading terms give negative values on that graph and
   positive values in the transverse direction. A zero residual gives a whole
   equality curve and hence a minimum which is not strict before sign reversal.
   The definitions of saddle and non-strict extremum are explicit and
   consistent between the study, table, examples, and README.

4. **The coefficient recurrence is exact.** In
   `F_y = lambda*y + R`, every monomial of `R` has total degree at least two.
   Inserting the new coefficient `c_n*x^n` can affect the coefficient of degree
   `n` only through `lambda*y`. This proves the stated recurrence and rational
   arithmetic claim. A branch jet through `N` suffices to compute the residual
   through `N`. The text correctly distinguishes a zero jet from an identity.

5. **The complex Milnor calculation proves the needed local isolation.**
   The holomorphic unit factorization of `F_y` gives
   `C{x,y}/(F_y) = C{x}` under substitution on its unique local graph.
   The image of `F_x` is `g'`, so the Jacobian quotient has dimension `m-1`
   when `ord(g)=m`. This also proves isolation over the complex numbers.
   A zero residual instead has an infinite-dimensional quotient and a curve of
   critical points. Real isolation is not silently substituted for complex
   isolation.

6. **The conservative stopping bound addresses the local/global issue.**
   If the gradient polynomials have a global gcd `D`, local complex isolation
   forces `D(0) != 0`. Removing that local unit preserves the Jacobian ideal
   and leaves globally coprime curves. Their local intersection multiplicity
   is bounded by their projective Bézout intersection number, at most
   `(d-1)^2`. Consequently a nonzero residual has order at most
   `(d-1)^2+1`. The contrapositive identity certificate is valid. The new
   degree-five example correctly exhibits a distant common critical line:
   global isolation of all critical points is unnecessary.

## Primary-source hypothesis checks

I opened the version-pinned abstract/HTML/PDF sources directly, then inspected
the downloaded PDFs with `pdftotext`. Their SHA-256 values match
[`evidence/sources.json`](../evidence/sources.json):

| Source | PDF SHA-256 |
| --- | --- |
| Płoski, `1305.5102v1` | `55f5ee9c01cb7f4ff3a8031129a1e4034edaee27c3c912956b2bd8f2f2300d49` |
| Marais and Steenpass, `1303.7114v3` | `6b69136f9c54f07232bb130b36f593c58c35330429e215e1d0c8fc26da7d7593` |

[Płoski, version 1, Theorem 1.1, page 2](https://arxiv.org/pdf/1305.5102v1)
requires a complex polynomial of degree `d > 1`, an isolated singularity of its
zero curve at the origin, and `ord_0(F) < d`. Its bound is
`mu <= (d-1)^2-floor(d/2)`. The study proves the local complex isolation when
the residual is nonzero and has `ord_0(F)=2`; hence this theorem applies for
`d >= 3`. It needs neither irreducibility nor isolation everywhere. Degree two
is correctly handled separately. The exclusion of degree four belongs to the
separate equality characterization in Theorem 1.4, not Theorem 1.1. I also
checked Remark 1.5. The optional cutoff is therefore justified, including for
the quartic stress test. The
[version-pinned HTML](https://arxiv.org/html/1305.5102v1) independently displays
the same statements. The web fetch of the version-pinned PDF initially returned
HTTP 406; inspection of the successfully downloaded PDF resolved access and
confirmed its internal version identifier.

[Marais and Steenpass, version 3, Theorem 11, pages 5–6](https://arxiv.org/pdf/1303.7114v3)
is a theorem about formal real power series and explicitly assumes an isolated
singularity. It supplies signed nondegenerate squares and a residual of order
at least three. The study describes that scope accurately and uses its own
convergent analytic argument for the zero-residual case. It does not attribute
the non-isolated case or analytic convergence to this formal theorem.

## Independent example checks

Using SymPy 1.14.0 without importing `classifier.py`, I checked all 22 final
catalog entries. Every expanded term list equals its displayed polynomial;
every gradient vanishes at the origin; every Hessian has rank exactly one.
Independent substitutions and explicit branch formulas verified every expected
normalized leading coefficient, residual order, and classification. The zero
cases were checked by exact substitution, not by a finite zero jet alone.

For the quartic family I used Lagrange inversion of
`phi + 2*s*phi^3 = t`, with `t=x^2`, rather than the production recurrence.
The coefficient of `t^(2k+1)` is
`(-1)^k * binomial(3k,k) * (2*s)^k / (2k+1)`. This independently gives

```text
phi = x^2 - 2*s*x^6 + 12*x^10 - 96*s*x^14 + 880*x^18 + O(x^22)
g   = s*x^8 - 4*x^12 + 24*s*x^16 - 176*x^20 + O(x^21).
```

Both signs satisfy the critical equation through degree 21. The residual
coefficients agree with the documented expansion, and the separate direct
sum-of-squares and signed-path arguments agree with the classification. Thus
degree four really can require residual order eight, with local complex Milnor
number seven. The shear, swap, negative-Hessian, shifted-value, tiny rational,
degree-six delayed-order, infinite algebraic branch, and distant critical-line
examples also check correctly. These finite computations support the examples;
the ordinary proof supplies the universal degree-bound argument.

## Limitations checked

The documentation correctly limits the executable representation to exact
rational coefficients. It distinguishes that contract from the theorem for
arbitrary real polynomials and from possible ordered algebraic-field
extensions. Resource budgets may yield `unresolved`; no insufficient zero jet
is claimed to certify identity. Arbitrary analytic inputs do not inherit a
polynomial degree cutoff. The smooth-flat examples correctly show that even
the entire Taylor series can fail to determine the local type outside the
analytic category. No certified neighborhood radius, global extremum,
polynomial-time complexity, novelty claim, or Lean verification is asserted.
No remaining mathematical blocker was identified.
