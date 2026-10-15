# Round-two source review: rigorous Williamson search reductions

Reviewed **2026-10-15 (UTC)**. The first-edition source ledger is preserved.
Here `m` is an odd sequence length, `h=(m-1)/2`, each sequence is symmetric,
and `x[0]=+1`. All partial-tuple filters below select **fully specified**
sequences. No external code was executed for this review.

## Primary references and attribution

1. **John Williamson**, [*Hadamard's determinant theorem and the sum of four
   squares*](https://doi.org/10.1215/S0012-7094-44-01108-7), *Duke Mathematical
   Journal* **11**(1), 65–81, March 1944. The original full text could not be
   retrieved here. Attribution of the odd product theorem is explicit in the
   two accessible author manuscripts below; this review does not claim to have
   inspected Williamson's original proof.

2. **Curtis Bright**, [*A New Form of Williamson's Product Theorem*,
   arXiv:1711.07056v1](https://arxiv.org/html/1711.07056v1), **2017-11-19**,
   CC0. Theorem 1 states the odd product theorem and credits Williamson (1944).
   The proof of the even-order Theorem 2 supplies the positive-support
   group-ring identity used in the short odd-order proof below. The odd-order
   specialization below is our explicit derivation, rather than a quotation of
   the inaccessible 1944 proof.

3. **Curtis Bright, Ilias Kotsireas, Vijay Ganesh**, [*Applying Computer Algebra
   Systems with SAT Solvers to the Williamson Conjecture*,
   arXiv:1804.01172v2](https://arxiv.org/html/1804.01172v2), **2019-05-14**,
   CC BY 4.0. Relevant locations: Section 2.3, Theorem 7 and Corollaries 8–9
   (Fourier characterization and partial-tuple PSD rejection); Section 2.4,
   Theorem 12 and Corollary 13 (compression and row-sum identity); Section 2.5,
   Theorem 14 (odd product theorem); Sections 4.1–4.2 (candidate filtering).
   Section 2.2 permits sequence negation and reordering. These operations do
   not justify keeping both initial-sign and nonnegative-row-sum normalizations
   simultaneously.

4. **Dragomir Ž. Đoković, Ilias S. Kotsireas**, [*Compression of Periodic
   Complementary Sequences and Applications*, arXiv:1302.0571v1](https://arxiv.org/html/1302.0571v1),
   **2013-02-04**; journal version *Designs, Codes and Cryptography* **74**(2),
   365–377 (2015), [DOI](https://doi.org/10.1007/s10623-013-9862-z).
   Theorem 2 gives the complementary PAF/PSD equivalence; equation (12) gives
   a PSD bound. Definition 3 and Theorem 3 establish the compression formula
   and preservation of complementarity. The arXiv manuscript carries the
   perpetual nonexclusive arXiv license; no broad text-reuse license is inferred.

## Odd product theorem: exact reduction, not an ansatz

For a Williamson quadruple, the cited theorem is

\[
a_i b_i c_i d_i=-a_0 b_0 c_0 d_0\quad(1\le i\le h).
\]

After initial-sign normalization the right side is `-1`. Encode each independent
position by a bit equal to one when its sign is negative. If `A,B,C,D` are the
resulting `h`-bit masks and `M=2^h-1`, every solution therefore satisfies

```text
A xor B xor C xor D = M
D = M xor A xor B xor C.
```

This is a necessary consequence of the Williamson equations and retains every
normalized odd-order solution. By contrast, demanding a multiplier subgroup,
extra periodicity, or one predetermined row-sum pattern would be an additional
restriction unless completeness were separately proved.

A self-contained proof is available in the cyclic group ring. Let `u^m=1`,
`J=sum_i u^i`, `P_X=sum_{x_i=+1}u^i`, and `p_X=P_X(1)`. Since `X=2P_X-J`,
`J^2=mJ`, and `P_X J=p_X J`, expansion of the defining square-sum identity gives

\[
\sum_X P_X^2=(\sum_Xp_X-m)J+m\,1.
\]

Symmetry and `x[0]=1` imply every `p_X` is odd. Reducing the identity modulo two
therefore gives `sum_X P_X^2 = J+1`. In characteristic two,
`P_X^2=sum_{x_i=+1}u^(2i)`. Because `m` is odd, doubling indices is a bijection.
Thus, at every nonzero coordinate, the number of positive signs among the four
sequences is odd. Their product is consequently `-1`. This proves the mask rule.

For an unordered-pair meet-in-the-middle implementation, the mask rule can be
included in the matching key: a pair with XOR `p` and PAF-sum signature `s`
must match a pair with XOR `M xor p` and signature `-s`. Duplicate handling and
the final exact PAF check are still required.

## Row sums with initial signs fixed

For a sequence with `w` negative independent positions,

\[
r_x=1+2(h-2w)=m-4w,
\qquad \sum_X r_X^2=4m.
\]

The second identity is the zero-frequency PSD condition. Candidate filtering may
retain exactly the signed row sums that occur in a four-square decomposition,
and partial tuples may be rejected when no remaining allowed row sums complete
that equation. The congruence `r_x = m mod 4` must be respected. A valid
normalized row sum can be negative.

Direct finite arithmetic gives the following complete magnitude patterns and
their forced normalized signs; order within a row is immaterial.

| m | Magnitudes | Signed normalized row sums |
| --- | --- | --- |
| 21 | `1,1,1,9` | `1,1,1,9` |
| 21 | `1,3,5,7` | `1,-3,5,-7` |
| 21 | `3,5,5,5` | `-3,5,5,5` |
| 23 | `1,1,3,9` | `-1,-1,3,-9` |
| 23 | `3,3,5,7` | `3,3,-5,7` |

These patterns are elementary derivations for this study, not new published
classification results. All feasible patterns must be searched for an exhaustive
claim at either length.

## Exact integer quadratic-form filters

Let `C_x[i,j]=x[(j-i) mod m]`. The matrix identity implies that every selected
partial tuple `S` has a positive-semidefinite residual

\[
4mI-\sum_{x\in S}C_xC_x^T\succeq0.
\]

Consequently, for every integer vector `v`,

\[
\sum_{x\in S}\|C_x^Tv\|^2\le4m\|v\|^2.
\]

This is our direct linear-algebra derivation of an exact rejection test. A fixed
finite set of integer vectors gives necessary conditions evaluated solely with
integers. It need not detect every violation of the full Fourier PSD bound.
Passing such tests is not a completion certificate; final PAF cancellation
remains the exact acceptance criterion. Vectors may be chosen using approximate
Fourier intuition, provided the actual rejection is computed on their fixed
integer coordinates.

The word **partial** refers to omitting whole candidate sequences. Zero-filling
unassigned entries inside one candidate does not give a valid lower bound:
unknown contributions can cancel. Also, `v=e_0 +/- e_d` gives only
`|sum_S PAF_x(d)| <= (4-|S|)m`; this is redundant for one or two selected
sequences and is consequently a weak singleton/pair filter.

## Compression and the exact order-three bin at m=21

For `m=c*d`, define the compressed sequence
`y[j]=sum_(q=0)^(c-1) x[j+q*d]`. Its entries lie in
`{-c,-c+2,...,c}`; symmetry gives `y[j]=y[-j]`. Direct expansion, also the proof
of Đoković–Kotsireas Theorem 3, gives

\[
\operatorname{PAF}_y(s)
=\sum_{q=0}^{c-1}\operatorname{PAF}_x(s+qd).
\]

Therefore every Williamson quadruple compresses to four integer sequences whose
combined PAF is `[4m,0,...,0]`. This preserves a necessary condition, not a
sufficient lifting condition. Completeness requires retaining every possible
lift of surviving compressions, or using compression only as a filter on the
fully enumerated original candidates. The target energy remains `4m`, not
`4d`. No requirement `y[0]=1` is justified.

At `m=21`, let `u_j=sum_{i=j mod 3}x_i`. Symmetry implies `u_1=u_2`. At Fourier
frequency seven, with `omega^3=1`,

\[
\widehat x(7)=u_0+u_1\omega+u_2\omega^2=u_0-u_1\in\mathbb Z.
\]

Hence a partial tuple must satisfy `sum_S (u_0-u_1)^2 <= 84`; a complete one
must give equality. Repeating either integer pattern `(2,-1,-1)` or `(0,1,-1)`
over the 21 coordinates yields the same eigenspace quadratic-form test. This is
an exact specialization derived here, not a separate literature theorem. There
is no analogous order-three frequency at prime length 23.

Order 21 is therefore the natural first extension for evaluating the reductions.
Length 23 can follow measured time and memory evidence. A larger bound alone
does not demonstrate improved search criteria; useful comparisons preserve the
same solution counts while reporting each filter's candidate/pair rejections
and computational cost.
