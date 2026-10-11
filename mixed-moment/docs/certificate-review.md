> Historical source review: mathematical statements and verdicts are retained. Quoted hashes identify the original supplied files, which may differ from privacy-normalized public receipts. Original/public hashes are recorded in `publication/SOURCE-MAP.json`; fresh publication checks are separate.

# Exact rational certificate review

The checked supplied archive reproduces all **17,805 supplied finite exact
checks**, with a regenerated `certificates.json` byte for byte identical to the
saved certificate. A separate implementation passes **20,072 finite exact
checks**. The provenance and rerun wrapper passes **993 checks**. These three
counts describe different check sets; they are not counts of formal theorems.

## Reproduce

From the project root, with Python 3 and its standard library:

```sh
python -B scripts/check_certificates.py
python -B scripts/independent_checks.py --lean-cases logs/lean-certificate-cases.json
```

The first command verifies provenance, executes the supplied checker in a
temporary scratch directory, compares the complete output, and runs the
independent checker. It writes
`certificates-verification.json` (historical report omitted from the minimal public set) and
`certificates-independent.json` (historical report omitted from the minimal public set).
The second command can rerun the independent arithmetic without executing
the source program and also produces the exact expectations used for separate
Lean examples in [`lean-certificate-cases.json`](../evidence/supplied/logs/lean-certificate-cases.json).
The standalone independent command does not authenticate the archive; use the
first command for the full provenance check.

Both scripts resolve default input paths relative to their own project root,
so the current working directory need not be the project. `--help` lists path
overrides. No network access or third-party package is used. The supplied
program runs under Python `-I -B` with only its script and supporting TeX
snapshot copied into scratch. Original source files are hashed before and
after; no source file is rewritten.

## Provenance established

| Item | Checked result |
|---|---|
| Actual archive | `source/openai-math-reviewed-supplement-2026-10-11.zip`, 523,782 bytes |
| Archive SHA-256 | `9e03b1ce33dc5d5fa62ab9478b06998bcb0eb32635fc11bccac065223e892a74` |
| Extracted files | All 107 files match their ZIP entries byte for byte |
| Inner SHA-256 manifest | All 106 listed files verified; its documented self-exclusion is the only omission |
| Inner manifest SHA-256 | `cfd20fd78b1000e6fa00aa5ad867377ff78d4427e8d97da525af55419fdd3678` |
| Supporting foundations snapshot SHA-256 | `3929650dfb36859d8f88281795d348043f903c41a70b0bf3598c21586a633852` |
| Recorded upstream revision | `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` |
| Regenerated certificate SHA-256 | `3ad750bc00cff156fe773e467db4521d8e46dce00bbd9faa432fca493e1c8621` |
| Theorem metadata | 21 distinct records `MM001`–`MM021`, 39 resolved dependency edges, valid topological order |
| Preservation | All 107 original extracted files and the archive unchanged |

The metadata agrees across the certificate, theorem records, verification
report, catalog, and package provenance. All 99 artifacts marked as copied
in package provenance also match their recorded sizes and hashes. These are
checks of the pinned supplied artifact and its internal consistency. They do
not freshly authenticate the remote repository revision or endorse unrelated
claims suggested by the source filename.

## Independent calculation paths

[`independent_checks.py`](../scripts/independent_checks.py) does not import or
execute the supplied `certificates.py`. It uses `fractions.Fraction` throughout.
The implementation deliberately changes several computational paths:

| Quantity | Supplied evaluator | Independent evaluator |
|---|---|---|
| Even moment \(m_{2r}\) | \(2/((2r+1)c_r)\) | Integrate the expanded polynomial: \(2\sum_{k=0}^{r}(-1)^k\binom rk/(2k+1)\) |
| Kernel \(c_{n/2}\) | Central binomial coefficient with signed support guard | Solve \((1-t^2)C(t)^2=1\), \(C(0)=1\), coefficient by coefficient; then compare to factorial coefficients |
| \(H^*(d)\) | Parity-based central binomial formula | Finite product of the two-step ratios, starting from \(H^*(0)=H^*(1)=1\) |
| Boundary rational parts | Recursive evaluator | Closed finite sums using the product-defined \(H^*\) |
| \(M(i,j)\) | Piecewise finite reduction sums | Fill the diagonal recurrence dynamically from full boundary triples |
| \(Z(i,j)\), \(i\ne j\) | Difference of two harmonic sums | Cancel the common terms first and sum only the finite interval between indices |
| Contact polynomial | Defect function applied coefficientwise | Truncated polynomial convolution \(tP(t)C(t)\) |

The boundary closed sums and diagonal recurrence still use the same
mathematical identities as the source. Algorithmic diversity checks their
finite arithmetic and interactions; it is not an independent proof of their
analytic origin. Both implementations also share Python's exact rational
arithmetic library.

The separate checks cover moments through 200; signed kernel indices from
−100 through 200; boundary recurrences through 100; \(0\le i,j\le24\), with
finite telescope lengths 1, 2, 5, and 10; and all 81 polynomials whose four
coefficients belong to \(\{-1,0,1\}\), for contact orders 1–8 and entry indices
0–9. They recompute every numerical table and example in the saved
certificate. The 2,500 additional finite tail-block checks compare the next
32 rational summands to the stated bound. A finite block check does not
establish a bound on an infinite tail.

## Exact examples

Every triple has coordinate order \((1,G,\zeta(2))\). Thus \((a,b,c)\) means
the formal expression \(a+bG+c\zeta(2)\), with no assumption that this
representation is unique after evaluation in the reals.

| Expression | Exact formal triple |
|---|---|
| \(M(0,1)\) | \((0,0,3/2)\) |
| \(M(1,0)\) | \((2,0,0)\) |
| \(M(2,0)\) | \((1,2,0)\) |
| \(Z(0,1)\) | \((1,0,0)\) |
| \(Z(2,2)\) | \((-5/4,0,1)\) |

For \(P=1,D=t\), the entry \(M(P,j)-(3/2)Z(D,j)\) has triples

| \(j\) | Exact triple |
|---|---|
| 0 | \((-3/2,4,0)\) |
| 1 | \((3/2,0,0)\) |
| 2 | \((5/4,0,0)\) |
| 3 | \((-1/8,0,3/4)\) |
| 4 | \((73/72,0,0)\) |

Here contact order 3 guarantees cancellation only for \(j<3\). The nonzero
third coordinate at \(j=3\) demonstrates the excluded endpoint; a later zero
coordinate at \(j=4\) does not extend the uniform theorem.

A nonintegral rational example uses
\(P=1+(2/3)t-(5/7)t^3\). Its contact polynomial through degree 8 is

\[
D=t+\frac23t^2+\frac12t^3-\frac8{21}t^4+\frac38t^5
  -\frac3{28}t^6+\frac5{16}t^7-\frac5{84}t^8.
\]

All entries \(0\le j<9\) have third coordinate zero; the next two third
coordinates are \(105/256\) and \(-55/896\). Complete rational triples are
recorded in the independent JSON log.

## Adversarial checks and exclusions

The checker verifies that seven deliberately corrupted certificate copies
are rejected: two signed-difference errors, a rational sign error, cancellation
incorrectly asserted at the excluded endpoint, a zeroed tail bound, changed
contact data, and a missing table row. The original certificate is never
modified for these tests.

The signed-index witnesses are especially relevant to Lean's natural-number
subtraction. At \((i,j)=(0,1)\), the \(G\)-coordinate uses the signed difference
\(-1\) and is zero; truncating the difference to zero produces 4. At
\((i,j)=(1,0)\), the \(\zeta(2)\)-coordinate uses \(-2\) and is zero; truncating
to zero produces \(3/2\). A guard or integer subtraction is required.

For each \(1\le L\le16\), \(P=t^{L-1},D=0\) passes contact below \(L\) and
has third coordinate \(3/2\) at \(j=L\). Omitting contact gives the triple
\((0,0,-3/2)\) for \(P=0,D=1,j=0\). Dropping the initial factor \(t\) from
the contact condition is exposed by \(P=D=1,j=0\), with triple
\((0,4,-3/2)\). Changing the multiplier to 1 is exposed by \(P=1,D=t,j=1\),
with triple \((1,0,1/2)\). Invalid negative array indices and zero series
lengths are rejected; only the explicit convention \(m_{-1}=0\) is retained.

The distinction between a nonzero formal coordinate and real nonmembership
is also checked as a statement of linear algebra. In the abstract quotient
map \((a,b,c)\mapsto(a,b+c)\), the formal vector \((0,0,-3/2)\) has the same
image as \((0,-3/2,0)\). This is a countermodel to the inference from a
nonzero third coordinate to nonmembership in the span of the first two
images. It asserts no relation between the actual constants \(G\) and
\(\zeta(2)\), and performs no numerical substitution for them.

No Python result here proves an integral identity, convergence of an infinite
series, Catalan irrationality, rational linear independence, or a theorem in
Lean. The original reviewed study's ordinary analytic arguments remain a
separate source of mathematical claims. The JSON expectations for Lean are
inputs to a separate kernel-checked verification step, not evidence that
that step has already run.
