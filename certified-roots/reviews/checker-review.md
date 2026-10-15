# Independent implementation review

Date: 15 October 2026. Reviewer: a separate automated review agent that did
not implement `verify.py` or author `tests/test_verify.py`. This is a source
inspection and reproducible finite audit, not a human review or a formal
verification of Python.

**Disposition: no blocking defect found in the hashed revision below.** The
checker implements the sufficient criterion stated in `STUDY.md` for the
exact rational polynomial system supplied in the certificate. Its accepted
claim is existence and uniqueness in the reported closed box, with the
reported center error bounds. It does not certify global uniqueness or
interpret a failed sufficient test as nonexistence.

## Source-to-theorem checks

- `Interval` converts operands only from exact integers or `Fraction` values.
  Addition, negation, subtraction and the four-endpoint multiplication rule
  give enclosing rational intervals. Odd powers preserve endpoint order;
  positive even powers include zero precisely when the interval crosses
  zero. Power zero evaluates the constant monomial as `[1,1]`.
- `_derivative_enclosure` differentiates each monomial by its exact exponent
  and lowers the selected exponent by one. A zero coefficient or zero
  selected exponent contributes zero. Thus it does not create negative
  exponents, and repeated-variable dependency can widen the answer rather
  than justify cancellation that the interval calculation has not proved.
- The nested sum forming `E` uses `Y[i][k] * J[k][j]`, followed by subtraction
  from the corresponding identity entry. Signed entries of `Y` pass through
  the full interval product. This agrees with `I-Y DF`, not `I-DF Y`.
- Exact rational Gaussian elimination permits row swaps, rejects a missing
  pivot, and checks the invertibility assumption needed to turn a fixed
  point of `T(x)=x-YF(x)` into a zero of `F`. Independent determinant tests
  below exercise both invertible and singular matrices.
- Positive radii make the weighted maximum norm well-defined. The code
  computes `q = max_i (Mr)_i/r_i`, the common maximum
  `eta = max_i d_i/r_i`, and the componentwise test `d+Mr <= r` separately.
  This matches the integral difference estimate, self-map proof, contraction
  proof and geometric error proof in the study. It accepts nonstrict
  self-inclusion, including boundary roots, and requires strict `q < 1`.
- The raw `weighted_error_bound` is `eta/(1-q)`; the stronger minimum with
  one follows from box membership. The coordinate output already takes
  `min(r_i, r_i*eta/(1-q))`. `SCHEMA.md` states this distinction explicitly.
  Bounds become `null` on failed certification, even if one separate test
  passed. No row-specific replacement for the common `eta` is made.
- Neither a residual, a derivative enclosure, a success flag nor an error
  bound is trusted from an input. Unknown keys are rejected and all
  mathematical outputs are recomputed. A saved report is not itself an
  input certificate and must be rerun when assurance is needed.

## Parser and interface checks

The file loader checks its inclusive 1 MiB limit before decoding strict UTF-8,
rejects duplicate keys at every object depth, and rejects floating/nonfinite
JSON values. Type comparisons reject booleans in exponent and version
positions. Rational strings use full ASCII matching, check numerator and
denominator digit limits before `Fraction` construction, and cannot contain
decimal notation, zero/negative denominators or executable expressions.
Dimensions, term key sets, total term count, per-term degree, positive radii,
and exact nonsingularity are checked before the certificate calculation.

The Python object API revalidates arithmetic shape but cannot reconstruct
duplicate JSON keys or a byte encoding already discarded by the caller. The
documentation makes the file-loader/API distinction. The companion JSON
Schema is explicitly structural and insufficient by itself; `verify.py`
remains authoritative for all mathematical and lexical constraints.

The three CLI outcomes have independently tested exit codes: `0` certified,
`1` valid but not certified, and `2` invalid input or invocation. An invalid
candidate cannot become successful by supplying a forged output field.

## Resolved robustness issue

During review, the checker author identified a valid-input serialization
failure: exact rational operations can produce numerator/denominator strings
longer than Python's default 4,300-digit conversion limit even though each
input rational has at most 128-digit parts. The repair serializes integers
with exact base-`10**500` chunks; it does not use floating arithmetic or change
the process-wide integer limit. Inspection confirms that every mathematical
report field and interval endpoint uses the repaired serializer.

The independent audit reproduces this using `F(x)=x^32`,
`c=1/(10^127+1)`, `r=1/(10^127+3)`, and `Y=1`. Its independently parsed output
is compared to the exact expressions `32*(c-r)^31`, `32*(c+r)^31`,
`1-32*(c-r)^31`, and `c^32/r`. Parsing uses 64-digit left-to-right chunks,
independently of the checker's 500-digit right-to-left serializer. The full
CLI JSON report also round-trips with exit code `1`, as mathematically
expected. Positive and negative 5,001-digit integer outputs are checked
against explicitly constructed strings.

## Reproduced commands and results

Environment: Python 3.12.14, standard library only. Commands run from the
repository root:

```text
python3 -m unittest discover -s certified-roots/tests -v
Ran 45 tests
OK

python3 certified-roots/reviews/independent_check.py
{"counts": {"affine_cases": 604, "hand_example_cases": 4, "long_output_cases": 6, "parser_boundary_cli_cases": 18, "power_cases": 924, "rank_cases": 681}, "status": "passed"}
```

The separate 2,237-case audit includes:

- All 81 two-by-two matrices with entries in `{-1,0,1}`, plus reproducible
  rational matrices of dimensions one, three and four, comparing elimination
  to a cofactor determinant definition: 681 cases in total.
- An exact affine oracle with signed matrices, rational centers and unequal
  radii, verifying residuals, both matrix enclosures, weighted constants,
  acceptance and error outputs: 604 cases. One constructed accepted case has
  `eta=q=9/10`, so the raw error bound is `9` and the coordinate bounds are
  capped by the box. This checks that the stronger scalar shortcut
  `eta+q<=1` is not required by the implementation.
- Every interval with integer endpoints between `-3` and `3`, at every power
  from zero through 32, comparing to exact power extrema: 924 cases.
- Escaped duplicate keys, deeply nested JSON, an oversized integer literal,
  floating/nonfinite tokens, inclusive byte-size and arithmetic limits, and
  all three CLI statuses plus missing-argument handling: 18 cases.
- The six long-output regression checks described above.
- Four separately hand-derived expected example outcomes: `q=1/70`,
  coordinate errors `1/138`; `q=3/22`, coordinate errors `2/95`; and the two
  failed examples with `q=501/500`, no certified error bound. These agree with
  the complete rational calculations in `EXAMPLES.md`.

The 45-test suite additionally checks explicit nonlinear Jacobian and
`I-YJ` enclosures at rational sample points, multiplication/subtraction signs,
singular roots, tampered coefficients and output claims, mismatched
dimensions, and exact comparison immediately below `q=1`. Sampling checks
implementation behavior; the interval inclusion proof, rather than sampled
points, justifies enclosure for every real point in the box.

## Reviewed file hashes

SHA-256, relative to the repository root. A later edit requires renewed review
of the changed file; these hashes identify this review's exact scope.

```text
e99f15513430c980e2c5dd0ab2a09c0e1c41963007125491df8f11d7f9940264  certified-roots/verify.py
e116be25ba4683dbea8e23648dfb1ee28c8b00e1fb74a889a5303b5b655d529b  certified-roots/STUDY.md
9b7954535b74f8dbb6099b2c59091a186ddc8792d1b6bc0886878c414250445a  certified-roots/EXAMPLES.md
3225926fb8d3e2824b3ac99f44d37d8c597115a1e640d092b5f10c365a4ba9b8  certified-roots/SCHEMA.md
a3d8541e689a0de5d4150a3ffc107aae78941c2b75adcdfe31ec913a16e1a04f  certified-roots/certificate.schema.json
295848feee8cf6b023863d9a8f96abcf2a34c78558c0cfbf27694863a4c2c5c9  certified-roots/tests/test_verify.py
904ef6da1c413ba0a686bdc3cde0d911883895013e3f7dca248bb2bfe9fb5293  certified-roots/examples/circle-line.json
3528298bfd450555079b9d49468429dd8b931de44d66f383423ed6a9c6928cdd  certified-roots/examples/circle-parabola.json
20588a667c8700a37faa7f8ea0f4294e9abeba1213249706d57ec20e7f578e2d  certified-roots/examples/tiny-residual-no-root.json
52083e36e8ad1258bb1ff79884fdabd7a463e2deb2a1637170516e8d9b54367f  certified-roots/examples/tiny-residual-two-roots.json
82e8f9841314cbb862f1d79414a2ea38503d5a578e347b72bad3e3e25ba1bde5  certified-roots/reviews/independent_check.py
```

## Remaining limits

The trust boundary includes the reviewed Python source, interpreter, exact
integer/`Fraction` operations, JSON parsing, and the mathematical proof.
Input-size and degree limits do not guarantee small intermediate expressions
or service-grade denial-of-service resistance; no hostile-workload hardening
claim is made. Very long valid outputs may need a chunk-aware parser rather
than a naive `Fraction(long_string)` in downstream applications. Only Python
3.12.14 was executed for this review; compatibility with other advertised
Python versions follows source-level inspection rather than a runtime matrix.

This review does not establish a formal proof of the executable, a verified
compiler/runtime, global root enumeration, certification of singular roots,
or correctness for nonpolynomial inputs. It reviews the contraction theorem's
correspondence with the executable, not the independent primary-source audit
of the historical comparison. No blocking issue remains within that scope.
