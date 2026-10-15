# Independent mathematics review

Review date: 15 October 2026. Reviewer: a separate mathematics-review agent,
independent of the study, examples, and verifier authors. **Status: approved
for this bounded first edition; no unresolved mathematical blocker.** This is
a source-and-calculation review, not formal verification or a claim that a
finite test suite proves the implementation correct.

## Exact reviewed material

Paths below are relative to `certified-roots/`. SHA-256 hashes identify the
bytes reviewed; subsequent modifications require checking the affected scope.

| File | SHA-256 |
| --- | --- |
| `STUDY.md` | `e116be25ba4683dbea8e23648dfb1ee28c8b00e1fb74a889a5303b5b655d529b` |
| `EXAMPLES.md` | `9b7954535b74f8dbb6099b2c59091a186ddc8792d1b6bc0886878c414250445a` |
| `SCHEMA.md` | `3225926fb8d3e2824b3ac99f44d37d8c597115a1e640d092b5f10c365a4ba9b8` |
| `verify.py` | `e99f15513430c980e2c5dd0ab2a09c0e1c41963007125491df8f11d7f9940264` |
| `examples/circle-line.json` | `904ef6da1c413ba0a686bdc3cde0d911883895013e3f7dca248bb2bfe9fb5293` |
| `examples/circle-parabola.json` | `3528298bfd450555079b9d49468429dd8b931de44d66f383423ed6a9c6928cdd` |
| `examples/tiny-residual-no-root.json` | `20588a667c8700a37faa7f8ea0f4294e9abeba1213249706d57ec20e7f578e2d` |
| `examples/tiny-residual-two-roots.json` | `52083e36e8ad1258bb1ff79884fdabd7a463e2deb2a1637170516e8d9b54367f` |

The study and examples were read in full. The verifier was read for the
theorem-to-code bridge; implementation review and the main adversarial test
suite are a separate review responsibility. The schema prose was checked for
its mathematical input and output meanings.

## Theorem, proof, and scope

The theorem has the necessary hypotheses: a nonempty closed box with positive
radii; a continuously differentiable map on an open neighborhood of the box;
an invertible fixed preconditioner; and an interval enclosure of every
Jacobian entry throughout the box. Convexity keeps each integration segment
inside the region of valid derivative bounds. The use of the componentwise
fundamental theorem of calculus avoids an unjustified vector mean-value
identity with one common intermediate point.

The weighted maximum-norm estimate follows directly from
`|(I-Y DF(z))_ij| <= M_ij`. The exact acceptance conditions are sufficient:
`d + M r <= r` gives a self-map of the closed box, and `q < 1` gives a strict
contraction. Non-strict self-map inequalities correctly allow boundary roots;
strict contraction is necessary for the stated contraction argument.

Existence is proved without merely citing the conclusion of Banach's theorem:
the iteration starts at the center, remains in the box, and has successive
differences bounded by a convergent geometric series. Completeness supplies a
limit in the box, and continuity supplies a fixed point. Invertibility of `Y`
then gives a zero of `F`. The separate contraction argument proves at most
one zero anywhere in the entire stated closed box, including its boundary.

The roles of self-mapping and contraction are accurately separated. The
existence-only discussion explicitly invokes the separate Brouwer theorem;
the executable does not claim to implement a separate existence-only mode.
Contraction without a self-map does not establish a root inside the box.

The error proof is valid: with `e = ||xi-c||_r`, the inequality
`e <= q e + eta` gives `e <= eta/(1-q)`; box membership also gives `e <= 1`.
Multiplication by each positive radius gives the stated coordinate bounds.
The common maximum `eta` must be used; independent residual-coordinate
fractions cannot replace it in a coupled system. The additional exact-iterate
error estimate follows from the same geometric tail argument.

The text distinguishes the map `T` from its vector value `T(c)`, a fixed
preconditioner from a varying inverse Jacobian, and the interval enclosure of
the map image from that actual image. It claims uniqueness only in the
specified box. The examples' global root counts are separately established
by elementary algebra. The nonsingularity conclusion for every `DF(x)` in
the box is also valid: a null vector would contradict the strict matrix-norm
bound. Singular-root failure is therefore a genuine limitation of this
criterion, rather than evidence of nonexistence.

## Interval arithmetic and executable hypotheses

The rational interval addition, signed multiplication, and power rules are
valid enclosures. The positive even-power crossing-zero rule is correct;
the zeroth power represents a constant monomial. Natural interval dependency
loss can widen enclosures and cause rejection, but does not invalidate an
accepted mathematical certificate under correct execution.

The executable's polynomial-only input supplies global differentiability
automatically. It validates a square system, positive rational radii,
nonsingular rational `Y`, and exact nonnegative integer exponent vectors.
It recomputes residuals, polynomial derivatives, interval Jacobians, signed
matrix products, `M`, `q`, and self-map margins. No user-supplied residual,
Jacobian, or claimed result is accepted as a hypothesis. All certificate
arithmetic uses integers and fractions, so no untracked floating-point
rounding enters the proof calculation.

`SCHEMA.md` accurately explains that `weighted_error_bound` reports the raw
fraction `eta/(1-q)`, while each coordinate output is capped using box
membership. A raw weighted bound larger than one is a valid, weaker bound;
the theorem's stronger clipped weighted bound follows immediately. The
Python runtime, parser, exact arithmetic implementation, and reviewed code
remain trusted components. No Lean or other formal verification was run or
claimed by this review.

## Independent calculation checks

All displayed arithmetic and the correspondence between the four JSON
fixtures and their stated systems were independently checked. In particular,
the circle/parabola calculation correctly retains interval dependency loss
in entry `(2,1)` of `I-YJ`; the true derivative entry is zero, while the
reported interval is a safe wider enclosure.

Eight exact expectation checks were executed successfully with
`PYTHONDONTWRITEBYTECODE=1 python` against the reviewed verifier:

| Check | Independent expected result | Observed |
| --- | --- | --- |
| Circle/line fixture | `q=1/70`, `eta=5/7`, margins `19/7000`, coordinate errors `1/138` | Passed |
| Circle/parabola fixture | `q=3/22`, `eta=4/11`, margins `7/220, 1/40`, coordinate errors `2/95` | Passed |
| Tiny residual, two roots | `q=501/500`, first margin `-2000001/1000000000000`, rejection and null errors | Passed |
| Tiny residual, no root | Same absolute bounds and rejection as preceding fixture | Passed |
| `F(x)=x-1`, `B=[-1,1]`, `Y=1` | Accept the boundary root, `q=0` | Passed |
| `F(x)=0`, same box/preconditioner | Self-map true, `q=1`, reject | Passed |
| `F(x)=x-2`, same box/preconditioner | Contraction true, self-map false, reject | Passed |
| `F(x,y)=(x-1,y/10)`, center zero, unit radii, `Y=I` | Accept with `q=9/10`, `eta=1`, although `eta+q>1` | Passed |

The last check also returns raw weighted error `10` and box-capped coordinate
bounds `1,1`, agreeing with the documented output contract. These eight
checks supplement, and do not replace, independent implementation review and
the repository's full test suite.

## Primary-source cross-check

The cited sources were inspected on 15 October 2026. Rump's
[2010 account, Section 13, Theorems 13.1–13.3](https://www.tuhh.de/ti3/paper/rump/Ru10.pdf)
supports the mean-value enclosure and distinguishes interval-Newton and
strict-inclusion Krawczyk results. The study uses its own explicit contraction
proof and does not import an unstated stronger Krawczyk implication. Publisher
metadata confirms the historical links to
[Krawczyk (1969)](https://link.springer.com/article/10.1007/BF02234767)
and [Moore (1977)](https://doi.org/10.1137/0714040).

[Hauenstein–Sottile, version 2, Theorem 2 and Section 4](https://arxiv.org/abs/1011.1091v2)
support the stated alpha threshold, associated-root distance bound, and
distinction between exact rational certification and floating calculations
with incompletely controlled error. The revised study explicitly identifies
the nonsingular-Jacobian setting and the Euclidean/Hermitian norm convention,
and avoids claiming uniqueness in an arbitrary input box from alpha
association alone. No novelty claim is made for these classical methods.

## Findings and remaining limits

During review, minor wording requests clarified alpha-theory norm assumptions,
uniqueness in the specified box, and the raw weighted-error output. The
reviewed versions resolve those requests. No unresolved mathematical error
or publication blocker was found within this review's scope. General
nonpolynomial maps, complex-root certification, singular roots, global root
enumeration, and proof of interpreter correctness remain outside the first
edition's executable scope, as documented.
