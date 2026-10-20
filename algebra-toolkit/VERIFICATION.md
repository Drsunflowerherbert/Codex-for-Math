# Verification record, corrections, and limits

## What the evidence means

The notes contain ordinary written proofs and explicitly cited structural
theorems. They have undergone a separate self-review for hypotheses, notation,
and failure cases, plus exact computational spot checks written independently
of the earlier repository search implementations. There is no claim of a
separate human reviewer, Lean/kernel verification, a full-book audit, or a new
result about universal Hadamard existence.

`evidence/exact-checks.json` records the actually executed finite checks,
software versions and their scope. `evidence/pdf-build.json` and the LaTeX logs
record compilation; compilation verifies neither mathematical correctness nor
source fidelity. Source fidelity is supported by the specific inspected pages
listed in the source ledger, including image inspection where required.

## Central statements checked by written derivation

| Statement | Hypotheses and check |
| --- | --- |
| Quotient factorization and first isomorphism theorem | Maps, domains, kernels and representative independence are explicit; no complement is assumed |
| Dual exactness and annihilator identities | Algebraic dual; finite dimension for the double-dual isomorphism and dimension arguments; basis extension for restriction surjectivity |
| Direct sums and splitting | Idempotent equations proved for modules; vector-space splitting distinguished from module/equivariant splitting; sections form an affine Hom space |
| Operator/module correspondence | Intertwiner equation checked; finite-dimensional operator modules distinguished from all finitely generated $k[t]$-modules |
| Canonical forms | Nonzero annihilator obtained without Cayley–Hamilton; Euclidean Smith mechanism explained; arbitrary PID version cited; splitting-field hypothesis retained for Jordan form |
| Polynomial projectors | Congruences, image/kernel identification, and independence from Bézout representative checked; canonical primary spaces distinguished from chosen cyclic summands |
| Cyclic Hom and commutant dimensions | Computed from the image of $1$ and divisibility; no unjustified extension to two-variable polynomial rings |
| Hom–tensor formulas | Currying needs no finite dimension; the canonical tensor map identifies its domain with finite-rank maps, and finite dimension of either source or target suffices for all Hom; noncommutative module sides specified |
| Symmetric/exterior constructions | Quotient universal properties; alternation includes repeated-vector vanishing in characteristic $2$; averaging needs invertible factorial |
| Determinants and minors | Exterior basis proof precedes determinant definition; rank test, Cauchy–Binet and characteristic coefficients derived; determinant of a map between different spaces is a line map |
| Forms and spectral theorem | Congruence versus similarity; Hermitian convention explicit; positive-definite complex finite-dimensional hypotheses retained; real and indefinite failures exhibited |
| Ext/Tor and homology | One-step resolution requires a nonzero element of a domain; explicit nonsplit $k[t]$ extension; field Ext/Tor vanishing separated from arbitrary complex homology |
| Representations | Maschke needs finite group and invertible order; Schur's scalar result needs algebraic closure and finite dimension; dual action has inverse; Lie tensor action has a sum |
| Trace pairing | Finite separable extension for nondegeneracy; scalar-extension/CRT proof and purely inseparable counterexample included |
| Bundles and sheaves | Smooth paracompact bundle splitting distinguished from arbitrary pointwise choices and algebraic sheaf extensions; no category-independent Ext vanishing claim |
| Hadamard bridge | Integer/real Gram equations; odd finite fields for character sum; exact Paley signs; cyclic Fourier splitting/characteristic hypotheses; compression and phase relaxation retain only necessary implications |

The proofs are inspectable in the chapters. The table is a review index, not
an independent formal certificate.

## Independently computed finite checks

The script `scripts/check_examples.py` reconstructs fixtures directly and does
not import the previous Hadamard project's search or verification code.
Its 18 check groups include:

- Polynomial CRT idempotents over $\mathbb Q$ and characteristics $2,3,5,7$;
  a conjugated mixed Jordan fixture checks the actual operator projections.
- Kernel-growth block reconstruction, and the commutant dimension independently
  computed as the nullity of a $100\times100$ commutator equation matrix.
  A real nonsplitting $t^2+1$ summand preserves the kernel data while
  increasing the dimension from ten to twelve, exhibiting the missing-hypothesis
  failure excluded by the corrected exercise.
- Sixteen cyclic-Hom dimension comparisons using direct intertwiner equations
  rather than the gcd formula being checked.
- Exterior minors, rectangular Cauchy–Binet, and characteristic coefficients;
  Kronecker determinant/trace; adjoints for a nonorthonormal Hermitian form.
- Explicit module-section failure over four small prime fields; a nonzero
  field-complex homology example with chain-homotopy equations; the
  $\mathfrak{sl}_2$ polynomial commutators for highest weights zero through six.
- Quadratic-character sums and both Paley block constructions for six small
  primes, plus an actual nonprime-field fixture
  $\mathbb F_9=\mathbb F_3[u]/(u^2+1)$ producing order 20.
- Williamson block signs at core three, the core-nine proper-quotient false
  positive, and all 27 possible normalized symmetric lifts of the **fixed**
  stronger compressed multiset from the prior audit. None is a Williamson lift.
  This is a bounded adversarial-fixture replay, not an expanded search campaign.
- The core-seven positive spectral residual with no fourth Williamson row;
  all 16 two-color-bit equality inputs and the exact Boolean phase identity.
  The explicit edge-orbit correlation formula is also compared with direct
  integer correlations for all 1,364 four-color labelings at cores
  $3,5,7,9,11$, using three sign fixtures per labeling (4,092 assignments),
  including the parity-forced signs. This is a bounded identity check,
  not a search for or classification of solutions.

Finite checks can catch sign, transpose, coefficient and characteristic errors
in these examples. They do not prove the universal theorems or classify all
Hadamard matrices. The infinite-dimensional tensor counterexample is proved by
unbounded rank, not established by a finite truncation test.

## Corrections incorporated in the local continuation

The continuation review supplied six focused corrections. Exercise 4 now
specifies $\dim_kV=10$, and the chapter's parallel example identifies only
the $\lambda$-primary blocks until a total dimension is known. Exercise 6,
its answer, and the Hom/tensor summary use the exact finite-rank image
criterion; finite dimension of either space suffices. Maschke's projection
is explicitly an endomorphism of $V$. The second congruence example begins
“Similarly.” Contraction is defined for $r\ge1$ and set to zero on
$\Lambda^0V$. Finally, $E_t$ is defined from the involution orbits, with
the zero pair and fixed point removed before passing to opposite-index
classes. The original source findings below are retained; this continuation
did not rematerialize or independently reread the source books.

## Cited results, distinguished from complete proofs here

- The full finitely generated module structure theorem over an arbitrary PID
  (Grillet VIII.6; Hungerford IV.6). The notes give the Euclidean matrix
  construction and derive the operator consequences; they do not pretend every
  PID is Euclidean.
- General derived-functor theory, independence of resolutions, and the complete
  Ext/extension correspondence (Hilton–Stammbach III–IV; Grillet XII).
  The cyclic class calculation and its extension interpretation are proved
  directly in the notes.
- Exhaustion of finite-dimensional complex $\mathfrak{sl}_2$ irreducibles
  (Hall §4.6). The polynomial models and their irreducibility are proved here;
  the exhaustion proof was read but is cited rather than reproduced fully.
- Primitive-element theorem for finite separable extensions; finite-field
  existence; the general commutative-algebra/sheaf correspondence; finite
  projectivity on affine schemes; implicit-function, partition-of-unity and
  other geometric prerequisites. Their uses and sources are stated, without
  implying all are reproved in this study.
- Prior study benchmarks, search completeness records, and historical matrix
  witnesses remain attributed to their pinned source edition. Only the small
  fixtures listed above were newly executed. No current worldwide open-problem
  status or smallest unresolved order is certified.

## Confirmed source correction

**Xi II, Theorem 6.19's following remark, printed p. 278 / PDF p. 284.**
The remark extends the finite-dimensional identification
$\mathcal T_q^p(V)\cong(V^*)^{\otimes p}\otimes V^{\otimes q}$ to
infinite-dimensional spaces. Definition 6.1 on printed p. 263 / PDF p. 269
defines the left side as all multilinear functions on
$V^p\times(V^*)^q$. Both pages were rendered and inspected.

For $p=q=1$, evaluation $(v,\lambda)\mapsto\lambda(v)$ belongs to
that function space. If it were a finite tensor sum, there would be
$\alpha_i\in V^*$ and $w_i\in V$ such that

$$\lambda(v)=\sum_{i=1}^r\alpha_i(v)\lambda(w_i)
\qquad\text{for every }v,\lambda.$$

Functionals separate vectors, so
$v=\sum_i\alpha_i(v)w_i$ for every $v$. This puts an infinite-dimensional
space in a finite-dimensional span, a contradiction. The corrected statement
retains finite-dimensionality, or restricts the multilinear function space to
the image of finite tensor sums. The finite-dimensional theorem and the
tensor universal property are unaffected. This is one local confirmed
overstatement, not a blanket judgment of the text.

## Convention differences and missing hypotheses, not source mistakes

- Grillet IX.7's initial “irreducible” means indecomposable (printed pp. 381,
  383; PDF pp. 393, 395). It differs from the simple-module convention in
  these notes, Xi and Hall. The apparent unconditional complete-reducibility
  statement must be translated using his definition, not declared false.
- Xi's Hermitian convention is linear in the first argument; these notes use
  conjugate-linearity in the first. Adjoint and coordinate formulas are
  translated explicitly.
- Xi II's alternating-tensor model explicitly assumes characteristic zero.
  Its factorial denominators are valid there; moving the model to arbitrary
  characteristic without that assumption would be our error, not its theorem.
- A Jordan form needs a splitting minimal polynomial; semisimple
  $k[t]$-modules need square-free irreducible factors and can lack eigenvectors
  over the base field. Commuting operators require individual diagonalizability
  before the simultaneous eigenbasis argument.
- A positive spectral residual and individually feasible compressed rows need
  not have one common discrete lift. No linear splitting theorem supplies it.
- Fourier eigenvalues over $\mathbb C$ are exact algebraic values in the
  proof; floating-point approximations are not used to certify sign matrices.

## OCR issues and unverified comparisons

Xi III's local PDF has 361 pages, whereas its earlier Library extraction
reported 150. Sparse extraction and corrupted symbols are source-access
limitations, not mathematical errors. The key cited pages were read as images.
Xi I–II also have corrupted extracted signs and indices, so suspected substantive
claims were checked against the intended notation and, where material, images.
The exact source fingerprints allow later reinspection.

The following comparisons remain deliberately limited: the entire exercises
of any two books; Xi II Chapters 4–5 versus a putative replacement; the whole
Xi III appendix or Galois computations against Hall/Lang; complete Hungerford
VII proof alternatives; and the destination books' full advanced prerequisite
coverage. They are not promoted from contents evidence into proven replacement
claims. No source book is called filler or wholly replaceable here.

## Remaining access limitation

The exact failed action was local materialization of the Library item titled
`Differential Topology (Morris W. Hirsch).pdf` using the provided download
helper. It returned `hosted apps tools/list request failed with HTTP status
401`. This is a failed local-download action, not a successful or uncertain
transfer and not an automatic sandbox-approval denial. The same source's
read-only Library pages were successfully read afterward. Consequently the
Hirsch content needed here is sourced, but no physical local PDF page count,
byte hash, or full local-PDF audit is claimed.

There is no pending mathematical/source blocker to using the present notes.
Completing the optional unverified comparisons would be a new, larger audit;
recovering a local Hirsch copy is only necessary for that sort of byte-level
or full visual audit.
