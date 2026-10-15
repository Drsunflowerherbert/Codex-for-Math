# Independent mathematical review: E07–E10

Reviewer: `author_parameters` agent, which did not author E07–E10. Review date: 2026-10-15. Scope: the four completed Markdown examples named below. This is a mathematical text audit with separate symbolic crosschecks, not a formal proof assistant verification.

## Sources and common conventions

Retrieved Leon Simon's [*Introduction to Geometric Measure Theory*](https://math.stanford.edu/~lms/ntu-gmt-text.pdf) independently and inspected Chapter 1 §2, equations (2.1)–(2.2), Theorem 2.6; Chapter 2 §3, definition (3.2), Theorem 3.3, Remark 3.4(2), and Examples 3.5(1)–(3). The source's Hausdorff covering cost is the unit-ball volume times `(diameter/2)^k`; it is the normalization stated in all four examples. Theorem 2.6 identifies it with Lebesgue measure on the matching Euclidean dimension; Euclidean isometries and orthogonal projection give the same statement on affine k-planes. `H^0` counts fibers.

The source's area formula allows locally Lipschitz maps on an open neighborhood and Lebesgue-measurable subsets of that neighborhood. All maps here are smooth on such an open neighborhood. Closed parameter intervals/disks are therefore admissible measurable subsets; no extension of the theorem beyond its source hypotheses is needed. The weighted formula follows from Remark 3.4(2); weights on the displayed parameter set can be extended by zero to its neighborhood. All weights are Borel, nonnegative and bounded. The explicit finite bounds justify every later signed or vector-valued scalar component integral.

## E07 — `examples/E07-parabola.md`

Status: **passed, no mathematical corrections required**.

- Independently differentiated `gamma(t)=(t,t^2)`: speed is `sqrt(1+4t^2)`. The first coordinate makes the parametrization injective on the full closed interval, so its fiber count is one, including endpoints.
- Recomputed the weighted integral with `u=1+4t^2`: `(5 sqrt(5)-1)/12`. Recomputed length as `sqrt(5)/2 + asinh(2)/4`, with `asinh(2)=log(2+sqrt(5))`.
- Checked that the restriction is Lipschitz and that both pullbacks are integrable. The integral is with respect to `H^1|C`; the statement that `L^2(C)=0` has a correct Lipschitz-covering justification.
- The orientation warning is accurate: reversing an injective traversal preserves a scalar Hausdorff integral, while a circulation uses a signed tangent.

## E08 — `examples/E08-circle-multiplicity.md`

Status: **passed, no mathematical corrections required**.

- Independently counted fibers of `[0,4pi] -> C`: two preimages except at `(1,0)`, where there are exactly three (`0,2pi,4pi`). A singleton is `H^1`-null. The text does not claim multiplicity two at every image point.
- Speed equals one and the pulled-back weight is `cos(t)^2`. Its parameter integral is `2pi`, hence the geometric scalar integral is `pi` after accounting for multiplicity. A single traversal has only an endpoint exception and gives the same scalar integral.
- Checked `F(gamma(t))=gamma'(t)` for `F=(-y,x)`, so the double traversal's circulation is `4pi`. A reversed single traversal has circulation `-2pi` while its scalar weight integral remains `pi`.
- Checked the flux comparison separately: for `G(q)=q` and outward unit normal `q` on the unit circle, the integrand is one and outward flux is `2pi`. Inward normal reverses the flux. Positive Hausdorff measure itself chooses no orientation.
- All parameter maps and weights satisfy the weighted area formula, and length `2pi` follows with weight one, so bounded scalar, circulation and flux quantities are finite.

## E09 — `examples/E09-paraboloid-graph.md`

Status: **passed, no mathematical corrections required**.

- Independently computed the derivative matrix of `(x,y,x^2+y^2)`. Its Gram matrix has diagonal entries `1+4x^2`, `1+4y^2` and off-diagonal entries `4xy`; determinant is `1+4x^2+4y^2`.
- The graph map is injective by projection onto the first two coordinates. On the convex disk its Lipschitz bound is at most `sqrt(5)`; it is smooth on all of `R^2`. Thus Theorem 3.3 applies to the closed disk as a measurable subset, and the compact image is Borel.
- Recomputed the weighted integral as `2pi integral_0^1 r^3 sqrt(1+4r^2) dr = pi(25 sqrt(5)+1)/60`; recomputed area as `pi(5 sqrt(5)-1)/6`. The graph factor and the separate polar factor `r` are both present.
- Polar seam and origin are planar-null. The author does not silently remove the closed disk boundary from the graph map.
- Checked that the height integral is positive and smaller than the area. The normal-orientation distinction is correct: only the norm of the cross product enters the scalar integral.

## E10 — `examples/E10-sphere-moment.md`

Status: **passed, no mathematical corrections required**.

- Independently computed the spherical derivative Gram matrix as `diag(R^2, R^2 sin(theta)^2)`, giving Jacobian `R^2 sin(theta)` for `0<theta<pi`.
- The map is injective on `(0,pi) x (0,2pi)`. Its omitted image is precisely the displayed positive-x meridian, including both poles. The covering argument is valid: `N` sets of diameter at most `Rpi/N` have total normalized two-dimensional cost at most `pi^3 R^2/(4N)`, with diameter tending to zero. Thus the omitted image, not merely the parameter seam, is proved `H^2`-null.
- Independently obtained `integral z^2 dH^2 = 4pi R^4/3`, sphere area `4pi R^2`, and cap area `2pi Ra`. The cap formula is valid at both endpoints `a=0` and `a=2R`; the latitude boundary is `H^2`-null by the same Lipschitz-curve covering argument.
- The rotational-symmetry check sums the three second coordinate moments to `R^2` times sphere area and is consistent.
- Checked the separate vector flux: `G(q)=q`, outward normal `q/R`, flux `4pi R^3`; inward orientation reverses it without changing the scalar second moment.

## Computational crosschecks

Ran SymPy with exact symbolic expressions: E07's weighted integral and length; E08's `cos^2` integral on `[0,4pi]`; E09's Gram determinant, weighted integral and area; E10's full Gram matrix, second-moment integral and sphere area. All assertions passed. The cap formula was also independently derived by `1-cos(theta_0)=a/R`, including its endpoint values.

These calculations corroborate algebra and elementary integrals. They do **not** establish measurability, theorem hypotheses, multiplicity, null omitted images, or orientation; those were checked in the preceding independent text audit.

## Findings and resolution

No substantive or minor mathematical defect was found in this review, so no edits to E07–E10 were requested or applied. Remaining limits: these are elementary applications of the area formula, not proofs of that general theorem, and none has been Lean-verified.

## Reviewed input hashes

SHA-256 of the exact reviewed UTF-8 Markdown file bytes:

| File | SHA-256 |
| --- | --- |
| `examples/E07-parabola.md` | `e564f66f4a78f93a3b199f51a70fbc1e751cf9c7e3d29b5319bd7398b9a10928` |
| `examples/E08-circle-multiplicity.md` | `e67be62b3a670a4747a08b9426fe5516fe6e8fec4ca5e0c5b10c6916efde0334` |
| `examples/E09-paraboloid-graph.md` | `7607d6bf833da41ba662f8d3a97d76a12fd06ff3b3c666ef9922f679413c7f7b` |
| `examples/E10-sphere-moment.md` | `62d000a6322836d426260ab380e07051502fbcb303a65301f8a6bd46b39575f3` |
