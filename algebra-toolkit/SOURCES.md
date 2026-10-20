# Source ledger and page conventions

## Evidence levels

The expanded edition adds contiguous proof readings documented in
[the operator supplement](PROOF-COMPARISON-OPERATORS.md) and
[the arithmetic supplement](PROOF-COMPARISON-ARITHMETIC.md).
Their ending ledgers give the new page ranges and distinguish extracted
proof reading from rendered-page verification. The original selected
readings below remain part of the baseline evidence, not a claim to have
read every intervening page.

**P** means the specified text, theorem, construction, or proof was inspected in
this task. **V** means a rendered source page was inspected, necessary for scans
or a suspected extraction problem. **T** means a contents or introductory
description was inspected; it establishes a location and stated scope, not that
every theorem or exercise was audited. **C** means a theorem is cited as a
standard result and is not fully reproved or source-audited here. The comparison
uses these distinctions rather than treating an index hit as proof coverage.

PDF page numbers are **one-based physical page positions in the supplied file**;
printed pages are the numbers visible on the book pages. The offsets below apply
to the ordinary Arabic-numbered body at the checked locations, not to Roman
frontmatter. A section range is a reading destination; a list of inspected pages
is the actual evidence, and should not be expanded into a full-book audit.

## Editions and physical files

| Key | Supplied source | File pages | Body page conversion |
| --- | --- | ---: | --- |
| Xi I | 席南华, 基础代数 第一卷, Science Press, 2016 | 207, local metadata | PDF = printed + 6 |
| Xi II | 席南华, 基础代数 第二卷, Science Press, 2018 | 334, local metadata | PDF = printed + 6 |
| Xi III | 席南华, 基础代数 第三卷, Science Press, 2021, second printing visible | 361, local metadata | PDF = printed + 6 |
| Hungerford | Thomas W. Hungerford, Algebra, Springer edition/reprint of the 1974 text; 1980 Springer preface and 2003 printing note | 523, local metadata | PDF = printed + 19 |
| Grillet | Pierre Antoine Grillet, Abstract Algebra, second edition, 2007 | 684, local metadata | PDF = printed + 12 |
| Mac Lane | Saunders Mac Lane, Categories for the Working Mathematician, second edition | 331, local metadata | PDF = printed + 13 |
| Hilton–Stammbach | Peter J. Hilton and Urs Stammbach, A Course in Homological Algebra, second edition | 376, local metadata | PDF = printed + 11 |
| Hall | Brian C. Hall, Lie Groups, Lie Algebras, and Representations, second edition, 2015 | 452, local metadata | PDF = printed + 13 |
| Hartshorne | Robin Hartshorne, Algebraic Geometry, Springer | 511, local metadata | PDF = printed + 15 |
| Lang | Serge Lang, Algebraic Number Theory, second edition; supplied reprint identifies 1986 edition with later copyright information | 372, local metadata | PDF = printed + 14 |
| Hirsch | Morris W. Hirsch, Differential Topology, 1976/reprint | 230 reported by Library reader; no local byte audit | PDF = printed + 10 at checked body pages |

Local SHA-256 fingerprints and byte sizes for the ten materialized files are
saved in `evidence/source-fingerprints.json`. They identify which supplied
editions underlie the references; they are not a distribution of source bytes.
The original Library filenames, which sometimes have OCR-like punctuation,
are not treated as authoritative edition statements.

## Xi I: concrete foundations and determinant characterizations

- **P/T:** title/edition and preface, PDF pp. 3–4; contents, pp. 5–6.
  The preface connects the course to Kostrikin's framework and names several
  other references, including Hungerford. This supports pedagogical context,
  not a claim that the books have identical proof coverage.
- **P:** Chapter 4 opening, printed pp. 75–76 (PDF pp. 81–82): oriented
  volume, multilinearity, and vanishing on dependent vectors.
- **P:** §4.4, printed p. 93 (PDF p. 99): several characterizations of the
  determinant, with the preceding exercises including Cauchy–Binet/Laplace
  identities. This is actual structural content, not merely a chapter title.
- **P/T:** §6.3 opening, printed p. 133 (PDF p. 139): factorization and
  examples whose irreducibility changes with the coefficient ring.
- **P/T:** §7.4 opening, printed p. 177 (PDF p. 183): elementary symmetric
  polynomials and invariance under ordering roots.
- **P:** §7.6 opening, printed p. 190 (PDF p. 196): resultant matrix and
  criterion, with the leading-coefficient degeneracy explicitly visible.
  This was an opening-page sample in the baseline. The continuation inspected
  the full proof sequence on PDF pp. 196–199 and its visible exercises;
  see the arithmetic supplement, including the narrow cubic-example erratum.
- Quotients of sets (§2.4, printed p. 30, PDF p. 36) and matrix-map
  organization (Chapter 3, starting p. 40, PDF p. 46) were located and sampled.

## Xi II: the principal source comparison

- **P:** §1.4–1.6 samples, printed pp. 16, 19–24 (PDF pp. 22, 25–30):
  independent subspaces, complements versus quotients, duals and evaluation.
- **P:** §2.4, printed pp. 67–71 (PDF pp. 73–77), selected text:
  quotient operator and induced-map diagram; characteristic-polynomial
  factorization; Cayley–Hamilton statement and dual operator discussion.
- **P:** §2.5, printed pp. 72–77 (PDF pp. 78–83), consecutive proof
  reading: Theorem 2.51 uses Bézout to split annihilated spaces; 2.52–2.53
  gives generalized eigenspaces; 2.56–2.57 gives Jordan form; the proof
  constructs chains by quotient induction and proves uniqueness by dimensions
  of images of powers.
- **P:** §3.1 opening, printed p. 85 (PDF p. 91), and §3.3 opening,
  printed p. 109 (PDF p. 115), with examples/exercises from metric linear
  algebra. **P:** Theorem 3.62 and its normal-operator argument, printed
  pp. 126–128 (PDF pp. 132–134).
- **T:** Chapters 4–5, printed pp. 161–262 (PDF pp. 167–268): affine and
  Euclidean geometry, transformations, convexity, indefinite spaces, quadrics,
  projective geometry. Their complete proofs were not audited; no blanket
  replacement claim about them is made.
- **P/V:** tensor Definition 6.1, printed p. 263 (PDF p. 269), defines
  all multilinear scalar functions on the indicated product spaces.
- **P:** tensor Definition 6.11 and Theorem 6.15, printed pp. 273–275
  (PDF pp. 279–281): basis construction, uniqueness, and universal property
  **with a proof**. Subsequent maps, associativity, distributivity, scalar
  extension, and Kronecker formulas were read on PDF pp. 280–284.
- **P:** §6.3 examples of contraction as trace/composition and structural
  tensors, printed pp. 280–283 (PDF pp. 286–289).
- **P/V:** Theorem 6.19 and following remark, printed p. 278
  (PDF p. 284). The finite-dimensional theorem is correct; the unrestricted
  infinite-dimensional extension fails for the definition on p. 263. See
  `VERIFICATION.md` for the explicit counterexample and its scope.
- **P:** §6.4 opening and definition, printed pp. 292–293 (PDF pp. 298–299):
  characteristic-zero assumption and exterior product via alternation.

## Xi III: selected scanned pages, not unreliable extraction

The Library extraction's earlier 150-page report is not the physical file
length. PyMuPDF counted **361 pages**. The scan's extracted text is extremely
sparse. The following evidence comes from rendered pages, not OCR guesses.

- **V/T:** contents, PDF pp. 5–6: group actions and structure, one-parameter
  groups (§2.5, p. 79), matrix Lie groups (§2.6, p. 85), representations
  (Chapter 3, p. 97), modules (§4.4, p. 186), algebras (§4.5, p. 197),
  $\mathfrak{sl}_2$ (§4.6, p. 215), Galois theory (Chapter 5, p. 224),
  and the representations appendix (p. 317).
- **V/P:** §3.2, printed pp. 109–111 (PDF pp. 115–117): complex
  Hermitian-form convention and Theorem 3.20's explicit finite-group averaging
  proof, with the compact-group integration comment distinguished from it.
- **V/P:** §3.7, printed pp. 152–153 (PDF pp. 158–159): dual action with
  inverse, transpose formula, and tensor action.
- **V/P:** §4.4, printed pp. 186–188 (PDF pp. 192–194): module motivation,
  unital left-module definition, examples, submodules, quotients and maps.
- **V/P:** §4.6, printed pp. 215–216 (PDF pp. 221–222): Lie module
  conditions and discussion of the enveloping algebra. The page explicitly
  sends the reader elsewhere for the PBW theory; the notes do not claim that
  this section proves PBW.
- **V/P:** §5.6, printed pp. 260–262 (PDF pp. 266–268): cyclic
  multiplicative group, finite-field existence and uniqueness, subfields and
  Frobenius. This supplies the finite-field prerequisites for the Paley bridge.
- **V/P:** §5.8, printed pp. 272–273, 275–277 (PDF pp. 278–279,
  281–283): Noether/Hilbert 90 constructions, norm/trace examples and
  trace-pairing and coefficient-formula exercises. The trace pairing on p. 277
  is an exercise, not a full proof at that location.
- **V/P:** §5.11 opening, printed p. 286 (PDF p. 292): the normal-basis
  theorem and beginning of its interpolation construction. The rest of that
  proof, full Galois computations/inverse questions, and the representation
  appendix remain selective reading destinations, not audited proofs here.

## Graduate sources: where the extra structure is actually built

**Grillet.** Title/preface and contents were inspected. The detailed samples
include VIII.6–7 (printed pp. 336–344, PDF pp. 348–350, 354–356),
X.1 and X.3 (pp. 393–395, 401–402; PDF pp. 405–407, 413–414),
XI.5–7 (pp. 434–437, 441–443, 447–448; PDF pp. 446–449,
453–455, 459–460), XII.4–5 (pp. 487–489, 493–494; PDF
pp. 499–501, 505–506), and XIII.2–4 (pp. 518–526; PDF pp. 530–531,
533–538). These support the module, splitting, balanced tensor,
Ext/Tor, and free-algebra comparisons. The general PID proof's key basis and
invariant-factor arguments were read; not every ancillary exercise was checked.
IX.7, printed pp. 380–385 (PDF pp. 392–397), was inspected for the
group-algebra correspondence, Maschke proof, and its nonstandard initial use
of “irreducible” for indecomposable. The p. 381 definition was checked as an
image. IV.1.6 (printed p. 157, PDF p. 169) was read for cyclic multiplicative
subgroups, and V.1.3 (printed pp. 192–193, PDF pp. 204–205) for the
finite-field existence/uniqueness proof and field-table exercises.
The other IV–VI destinations for norm/trace, orders/valuations and completions
are **T**, not a proof audit.

**Hungerford.** Prefaces, contents, and course suggestions were read, especially
printed p. xviii (PDF p. 15), which explicitly places torsion PID modules
before VII.1–5 in the proposed linear-algebra course. IV.6 begins at
printed p. 218 (PDF p. 237); selected text on torsion/cyclic modules and
the structure statements was read at PDF pp. 239–241. VII.4 starts at
p. 355 (PDF p. 374), VII.5 at p. 366 (PDF p. 385). The route and theorem
locations are verified, but a line-by-line comparison of all proofs in VII
was not completed. IV.4 (p. 199, PDF p. 218), IV.5 (p. 207, PDF p. 226),
are selective destinations grounded in contents. V.5's finite-field proofs
were then read at printed pp. 279–281 (PDF pp. 298–300), including
Theorem 5.3, Proposition 5.6, Corollary 5.7, Frobenius, and the explicit
exercise constructing fields of orders 9 and 25.

**Mac Lane.** III.1 (printed pp. 55–58, PDF pp. 68–71), III.2
(pp. 60–62, PDF pp. 73–75), IV.1 (pp. 79–80, PDF pp. 92–93), and
IV.2's duality example (pp. 88–89, PDF pp. 101–102) were read.
These are actual definitions, examples, and proofs of universality,
representability/Yoneda, and adjunction. VIII's abelian-category treatment and
later monads/Kan extensions are **T/C** in this study.

**Hilton–Stammbach.** Edition, contents, and introduction were read; III.1–2
and III.4 were sampled in detail (printed pp. 84–86, 89–90, 97–98;
PDF pp. 95–97, 100–101, 108–109). IV.1's definitions and homology
construction were read at pp. 117–118 (PDF pp. 128–129). The introduction
explicitly motivates the extension-first route before general derived functors.
The complete comparison theorem for resolutions and the full general Ext
classification are **C** here; our one-step cyclic cases are proved directly.

**Hall.** The supplied book is the second edition. §§4.3–4.7 were sampled
at printed pp. 90–101 (PDF pp. 103–114), including the unipotent
nonsemisimple example, unitary splitting proof, Schur argument, and
$\mathfrak{sl}_2$ classification proof. Later root systems, PBW, highest-weight
theory, and topology are **T**, not compared proof by proof against Xi.

**Hartshorne.** Contents and introduction, Chapter II opening, II.5,
II.8, and Chapter III opening were read at PDF pp. 9–10, 14–15, 74–75,
123–126, 187–189, 216. In printed pages these include II.5 at pp. 108–111,
II.8 at pp. 172–174, and III's opening at p. 201. The algebraic
differential universal property and the rational-residue-field cotangent
calculation are visible at these locations. The “A” notation distinguishes
externally referenced theorems. Affine finite projectivity and general
cohomological theorems are cited rather than re-audited in full.

**Lang.** Title/edition and contents were read. I.1 opening (printed p. 3,
PDF p. 17), I.9 Proposition 26 and its local-to-global proof (p. 29,
PDF p. 43), and III.1's complementary-module definition/proposition (p. 57,
PDF p. 71) were inspected. Full valuation, completion, ramification and class
field arguments remain **T/C**. A route to them is identified without claiming
that the current notes replace them.

**Hirsch.** Located by title in Library. Preface/contents, PDF pp. 8–10;
Chapter IV.1–2 samples, PDF pp. 96–105 (printed pp. 86–95). The
preface's declared avoidance of tensors/forms and IV.2.2's partition-of-unity
splitting proof are **P**. Local download via the Library helper returned
HTTP 401; no local physical-file metadata or fingerprint is claimed. The
read-only Library content route succeeded. The full transversality/Morse
proofs are not audited here.

## Existing Hadamard/Williamson research

The reference edition is pinned to repository commit
`2834fea31fb4ca7203531ca220e55a2fb7640119`, not a moving branch tip:

- [Study and original scope](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/2834fea31fb4ca7203531ca220e55a2fb7640119/hadamard-study/README.md).
- [Original constructions and exact sign conventions](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/2834fea31fb4ca7203531ca220e55a2fb7640119/hadamard-study/PROOFS.md).
- [Second-round structural and spectral proofs](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/2834fea31fb4ca7203531ca220e55a2fb7640119/hadamard-study/round2/PROOFS.md).
- [Third-round proofs, especially §§1–4, 9, 11–13](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/2834fea31fb4ca7203531ca220e55a2fb7640119/hadamard-study/round3/PROOFS.md).
- [Third-round limitations](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/2834fea31fb4ca7203531ca220e55a2fb7640119/hadamard-study/round3/LESSONS.md).
- [Prior independent adversarial review](https://github.com/Drsunflowerherbert/Codex-for-Math/blob/2834fea31fb4ca7203531ca220e55a2fb7640119/hadamard-study/round3/reviews/REVIEW.md).

Those documents and the relevant exact fixture descriptions were read from
Git objects. The new foundation chapter gives its own derivations, identifies
where it extends the scope of the earlier prime Paley proof, and retains the
distinction between previous audit evidence and newly executed finite checks.
Numerical historical/status claims and whole prior benchmark campaigns were
not rerun for this foundational task.
