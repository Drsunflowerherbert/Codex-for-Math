# Returning to algebra: a compact working guide

## The essential memory spine

Retain the following statements with their hypotheses and the type of every map.
The rest of the toolkit should be reconstructible from them.

1. A map $V/U\to X$ is a map $V\to X$ that kills $U$.
2. Dualization is precomposition; evaluation gives $V\cong V^{**}$ in finite
   dimension. An identification with $V^*$ needs extra data.
3. A direct sum is encoded by projections, and $P^2=P$ gives
   $V=\operatorname{im}P\oplus\ker P$.
4. A split exact sequence has a section. Sections differ by a map from the
   quotient to the kernel; existence does not imply a preferred choice.
5. An operator is a $k[t]$-module. The PID structure theorem classifies
   finite-dimensional operators through invariant factors; Jordan form needs
   splitting of the minimal polynomial.
6. Coprime annihilator factors produce polynomial idempotents by Bézout.
7. Tensor products represent bilinear or balanced maps. A formula on pure
   tensors must respect the defining relations.
8. $W\otimes V^*\cong\operatorname{Hom}(V,W)$ when $V$ is
   finite-dimensional. Trace is evaluation; not every infinite-rank operator
   is an algebraic tensor.
9. Tensor, symmetric and exterior algebras are free constructions with specified
   relations. $\Lambda^r$ transports alternating data; the top exterior
   power gives a determinant line.
10. Forms transform by congruence, operators by similarity. A positive metric
    supplies adjoints, orthogonal projections, and the normal spectral theorem.
11. Exactness is image equals kernel. Over a field short exact sequences split
    and positive Ext/Tor vanish; homology of an arbitrary complex need not.
12. A representation is a module over a group algebra. Maschke needs invertible
    group order; Schur's scalar conclusion needs finite dimension and an
    algebraically closed field.

For Hadamard/Williamson add five facts: Gram orthogonality is an integral
identity; tensors multiply valid orders; cyclic Fourier coordinates are CRT
coordinates; compression loses lifting information; and equality of Boolean
phases must be distinguished from independence of their signs.

## A selective route, with stopping tests

**First return: regain the language.** Read the quotient/duality/splitting
chapter, with Xi II §§1.4–1.6 and 2.4 beside it. Stop when you can construct
the quotient map and its dual, describe the affine space of sections, and
explain why an invariant complement is an additional demand. Xi I can be a
reference for matrix maps and determinant characterizations rather than a
sequential restart.

**Second return: recover operator theory from one theorem.** Choose Grillet
VIII.6–7 or Hungerford IV.6 then VII.4–5 as the principal module route.
Read Xi II §2.5's actual Bézout and quotient-induction proofs as a comparison,
not a second complete linear algebra course. Stop when you can obtain primary
projections, invariant factors, Jordan blocks under the field hypothesis, and
the block counts from kernel growth.

**Third return: turn multilinearity into maps.** Read Xi II §6.2, especially
Theorem 6.15 and the Hom/scalar-extension examples. Then use Grillet XI.5–6
and XIII.2–4 for balanced products, quotient constructions, and characteristic
issues. Read Mac Lane III.1–2 and IV.1 when the universal examples are already
familiar. Stop when you can define tensor-induced maps without a basis and
derive Cauchy–Binet from $\Lambda^r(gf)$.

**Keep a metric branch active.** Read Xi II §§1.7, 3.3–3.5 and 3.8 as
needed for forms, adjoints, normal operators, and projections. This is central
for Hadamard Gram matrices. Defer the rest of affine/projective geometry only
according to current goals, without concluding that the content was replaced.

**Introduce homology at its first real obstruction.** Read the exactness
chapter here, then Hilton–Stammbach III.1–4 and IV.1–3 if you want the
general construction. Grillet X.1, X.3 and XII are an alternative. Stop the
first pass after computing the $k[t]/(t^2)$ extension and explaining
nonzero field-complex homology. Spectral sequences and derived categories are
not prerequisites for the current Hadamard bridge.

**For the confirmed problem direction.** Read the Hadamard bridge in order:
Gram matrices and tensor closure; Xi III §5.6 finite fields; the character-sum
proof and Paley blocks; cyclic group algebra and Fourier CRT; then the pinned
third-round proofs with their color and Boolean equations. Use Xi III Chapter 3
or Grillet IX.7 for group algebras and representations, keeping Grillet's
initial indecomposable/irreducible convention visible. Read the prior limitations
before proposing a larger search. The essential stopping test is being able
to say exactly which implication is necessary, sufficient, or only a relaxation.

Hall's further Lie theory, Lang's local arithmetic, Hartshorne's scheme/sheaf
theory, and Hirsch's transversality/bundle development can then be pursued as
separate branches. Their prerequisite bridges are recorded, not placed in front
of every use of linear algebra.

## Reconstruction exercises

These are deliberately small. Their purpose is to test whether a tool can be
rebuilt, not to begin the later difficult problem-set campaign.

1. **Quotient versus complement.** For $U\subseteq V$, construct
   $(V/U)^*\cong U^\circ$ and show why no complement is needed. Then describe
   all sections of $V\to V/U$ once one has been chosen.
2. **One invariant line.** In $k[t]/(t^2)$, list the subspace killed by
   $t$. Prove it has no $t$-invariant complement, and identify the associated
   nonzero Ext class.
3. **Recover a projection.** Assuming $T^2(T-I)^2=0$, derive the projector
   $3T^2-2T^3$ from polynomial congruences. Check the argument in
   characteristics $2$ and $3$ without dividing by those integers.
4. **Recover Jordan data.** An operator has only eigenvalue $\lambda$ and
   successive kernel dimensions $0,4,7,9,10,10$. Find all its block sizes,
   minimal polynomial, and the dimension of its commutant.
5. **Nonsplitting field.** Classify multiplication by $t$ on
   $\mathbb R[t]/(t^2+1)$ as a real module and after complexification.
   Explain which use of “semisimple” is valid before extension.
6. **Tensor universality.** Construct the currying bijection and
   $W\otimes V^*\to\operatorname{Hom}(V,W)$, specifying precisely which
   one needs finite-dimensional $V$. Prove the finite-rank obstruction.
7. **Determinants from wedges.** Derive the minors formula for
   $\Lambda^2f$ and the $2\times2$ Cauchy–Binet identity for a
   $2\times3$ matrix times a $3\times2$ matrix.
8. **Forms versus operators.** Give two congruent real symmetric matrices
   that are not similar. Derive $H^{-1}A^*H$ from the defining adjoint
   identity, stating the Hermitian linearity convention.
9. **Homology survives.** For $d:k^3\to k^2$,
   $d(x,y,z)=(x,y)$, compute the two homology groups of the two-term complex,
   and write an explicit contractible/homology decomposition.
10. **The right group action.** Verify the inverse in the dual action, and
    differentiate it to obtain the minus sign in the Lie algebra dual action.
11. **Character sum.** Reproduce the count of
    $y^2=x(x+a)$ over an odd finite field. Identify every use of $a\ne0$
    and $2\ne0$, then check one Paley block multiplication.
12. **Compression and phase dependence.** Check the core-nine compressed
    autocorrelation example. Explain why failure of its chosen lifts alone
    cannot prove absence of all lifts. Separately give a numerical assignment
    to three formally independent signs that violates
    $\xi_{p+q}=\xi_p\xi_q$.

## Brief answer checks

For Exercise 1, pull back along the quotient, and use $s'=s+i h$.
For 2, the killed subspace is $kt$ and the class is $1\in k$ under
$\operatorname{Ext}^1_{k[t]}(k,k)\cong k$. For 3, require a polynomial
to be zero modulo $t^2$ and one modulo $(t-1)^2$; the integer identity
remains valid after any reduction of characteristic.

For 4, the differences are $4,3,2,1,0$, so the sizes are $4,3,2,1$.
The minimal polynomial is $(t-\lambda)^4$ and the commutant dimension is
$\sum_{i,j}\min(i,j)=30$ for $i,j=1,2,3,4$. For 5, the real module
is simple; after complexification it is the direct sum of the $i$ and $-i$
eigenspaces. It is semisimple over $\mathbb R[t]$ but not real
diagonalizable.

For 6, currying needs no finite dimension, while surjectivity of the indicated
Hom/tensor map does. For 7, sum the three intermediate $2$-subsets.
For 8, $I$ and $2I$ suffice, and $h(x,y)=\bar x^{\mathsf T}Hy$ is
the convention used here. For 9, $H_1$ is the $z$-axis and $H_0=0$;
the $(x,y)$ coordinates map isomorphically to $k^2$.
For 10, transpose reverses products and differentiation of an inverse at the
identity contributes a minus sign. For 11, the count is $q-1$.
For 12, choose all three phase signs negative: the product of the first two
is positive, contradicting the third. These checks indicate the target, while
the chapters provide the proofs to reconstruct.

## What can be deferred

Defer a formula once its map or universal property can be reconstructed.
Defer a subject when it has no role in the current destination. Do not defer
the hypotheses, the equivalence relation, or a known failure case. For this
collection, an effective memory sheet contains definitions and four or five
counterexamples, with links back to proofs, rather than a long inventory of
named theorems.
