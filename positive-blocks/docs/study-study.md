# Hilbert Schmidt inequalities for positive block matrices

## Scope and conclusion

This is a self-contained study of one finite-dimensional supporting matrix lemma. For a positive semidefinite complex block matrix

\[
\Delta=\begin{pmatrix}A&B\\B^*&C\end{pmatrix}\succeq0,
\qquad A\in\mathbb C^{p\times p},\quad B\in\mathbb C^{p\times q},
\quad C\in\mathbb C^{q\times q},\quad p,q\ge1,
\]

we prove

\[
2\|B\|_{\rm HS}^{2}\le\|A\|_{\rm HS}^{2}+\|C\|_{\rm HS}^{2},
\qquad
\boxed{\ \|B\|_{\rm HS}^{2}\le\|A\|_{\rm HS}\|C\|_{\rm HS}\ }.
\]

The constants are optimal, even for scalar blocks. Complete equality criteria include zero diagonal blocks, different block dimensions, and rank-deficient blocks. All norms are **unnormalized** Hilbert–Schmidt norms: \(\|T\|_{\rm HS}^{2}=\operatorname{tr}(T^*T)=\sum_{ij}|T_{ij}|^2\).

The source is OpenAI/math family 325, revision `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, [main.tex lines 434–445](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/build/main.tex#L434-L445), section `sec:matrix`, paragraph “The positive block comparison.” The source uses equal-sized blocks; the proof below permits arbitrary \(p,q\). The product sharpening, exact gaps, equality classification, and examples are worked out here as elementary consequences. No novelty is claimed. This study does not establish or review the source manuscript's complete Crouzeix theorem, its other analytic estimates, or a Lean formalization.

## Definitions and elementary dependencies

A matrix \(H\) is positive semidefinite if it is Hermitian and \(v^*Hv\ge0\) for every complex column vector \(v\). Its principal blocks \(A,C\) are therefore Hermitian positive semidefinite. We use only finite-dimensional matrix arithmetic, cyclicity of trace (including \(\operatorname{tr}(UV)=\operatorname{tr}(VU)\) for compatible rectangular factors), the spectral theorem's positive square root/Gram factorization, and the elementary fact that a sum of squares vanishes exactly when each term vanishes.

A Gram factorization means

\[
\Delta=Z^*Z,\quad Z=[X\ Y],\quad
X\in\mathbb C^{d\times p},\quad Y\in\mathbb C^{d\times q}.
\]

Such a factorization always exists, with \(d=p+q\) by taking \(Z=\Delta^{1/2}\), or with \(d=\operatorname{rank}\Delta\) when \(\Delta\ne0\) by retaining its positive eigenvalues. Conversely every displayed Gram factorization certifies positivity. Write

\[
A=X^*X,\quad B=X^*Y,\quad C=Y^*Y,
\qquad P=XX^*,\quad Q=YY^*\quad(d\times d),
\]

and abbreviate \(a=\|A\|_{\rm HS}\), \(c=\|C\|_{\rm HS}\), \(\beta=\|B\|_{\rm HS}^{2}\). The symbols \(P,Q\) in this study are auxiliary Gram matrices, unrelated to the source's polynomial notation.

## PB1 The exact Gram identity

Trace cyclicity gives, with every matrix dimension explicit above,

\[
a^2=\operatorname{tr}(P^2)=\|P\|_{\rm HS}^{2},\qquad
c^2=\operatorname{tr}(Q^2)=\|Q\|_{\rm HS}^{2},\qquad
\beta=\operatorname{tr}(PQ).
\]

For example,
\(\operatorname{tr}_p(X^*YY^*X)=\operatorname{tr}_d(XX^*YY^*)\).
The last trace is real and nonnegative because it equals \(\|X^*Y\|_{\rm HS}^2\); no commutation of \(P,Q\) is assumed.

Expanding the square of the Hermitian matrix \(P-Q\),

\[
\boxed{\quad a^2+c^2-2\beta=\|P-Q\|_{\rm HS}^{2}\ge0.\quad} \tag{1}
\]

This proves the sum bound. It also proves that equality in the sum bound is equivalent to \(P=Q\), for **any** Gram factorization. Thus equality is independent of the chosen factorization, even when that factorization has redundant rows.

More generally, for every \(s>0\),

\[
s^2a^2+s^{-2}c^2-2\beta
=\|sP-s^{-1}Q\|_{\rm HS}^{2}. \tag{2}
\]

### A second proof using congruence and trace

Let \(J=\operatorname{diag}(I_p,-I_q)\). Positivity is preserved by congruence, so \(J\Delta J\succeq0\). With \(S=\Delta^{1/2}\),

\[
0\le\operatorname{tr}(S(J\Delta J)S)
=\operatorname{tr}(\Delta J\Delta J)
=a^2+c^2-2\beta.
\]

In fact \(S(J\Delta J)S=(SJS)^2\), and \(SJS\) is Hermitian. Hence the gap is exactly \(\|SJS\|_{\rm HS}^2\). This is the source's elementary trace argument, with rectangular off-diagonal blocks allowed.

## PB2 The product bound obtained by scaling

First handle zero blocks: if \(a=0\), then \(A=0\), and \(X^*X=0\) implies \(X=0\); hence \(B=0\). Similarly \(c=0\) implies \(B=0\). The product inequality is equality in either case.

Suppose now \(a,c>0\). For every \(s>0\), the congruence

\[
D_s\Delta D_s\succeq0,\qquad
D_s=\operatorname{diag}(s^{1/2}I_p,s^{-1/2}I_q)
\]

has diagonal blocks \(sA,s^{-1}C\) and off-diagonal block \(B\). Applying PB1 gives

\[
2\beta\le s^2a^2+s^{-2}c^2.
\]

Choose \(s=\sqrt{c/a}\); both terms on the right are \(ac\). Therefore \(\beta\le ac\). This choice is optimal because

\[
s^2a^2+s^{-2}c^2-2ac=(sa-s^{-1}c)^2\ge0.
\]

No inverse of \(A\) or \(C\) is used, so the argument includes singular diagonal blocks. Alternatively, Hilbert–Schmidt Cauchy–Schwarz applied to \(P,Q\) gives \(\beta=\operatorname{tr}(PQ)\le ac\) directly; scaling shows explicitly why the sum inequality already implies the stronger product inequality.

## PB3 Complete equality conditions and exact deficit

### Product equality

If \(a=0\) or \(c=0\), then \(B=0\), and product equality always holds. This includes one nonzero diagonal block. The following nonzero classification must not be applied to those cases.

Assume \(a,c>0\) and set \(t=c/a>0\). The following statements are equivalent:

1. \(\beta=ac\).
2. In any Gram factorization, \(Q=tP\), equivalently \(P/a=Q/c\).
3. \(\Delta\operatorname{diag}(tI_p,-I_q)\Delta=0\).
4. The block identities
   \[
   BB^*=tA^2,\qquad B^*B=t^{-1}C^2,\qquad BC=tAB
   \tag{3}
   \]
   hold.
5. There are an integer \(1\le r\le\min(p,q)\), matrices \(U\in\mathbb C^{p\times r}\), \(V\in\mathbb C^{q\times r}\) with \(U^*U=V^*V=I_r\), and a positive definite Hermitian \(H\in\mathbb C^{r\times r}\), such that
   \[
   A=UHU^*,\qquad B=\sqrt t\,UHV^*,\qquad C=tVHV^*.
   \tag{4}
   \]

Indeed, PB1 with the optimizing scale gives the exact identity

\[
\boxed{\quad ac-\beta=\frac{ac}{2}\left\|\frac Pa-\frac Qc\right\|_{\rm HS}^{2}.\quad} \tag{5}
\]

The right side vanishes precisely in statement 2. If 2 holds, then
\(\Delta\operatorname{diag}(tI_p,-I_q)\Delta=Z^*(tP-Q)Z=0\), proving 3. Expanding its four blocks gives 4 and the adjoint of its third identity. Conversely, its top-left block alone gives \(\beta=t a^2=ac\) on taking traces. Thus 1–4 are equivalent. Under the same PSD assumptions and the fixed value \(t=c/a\), either of the first two identities in (3) alone is already sufficient for product equality.

To obtain 5 from 2, choose a Gram factorization of minimum row dimension \(r=\operatorname{rank}\Delta\). Then \(ZZ^*=P+Q=(1+t)P\) is positive definite, so \(P\) is invertible. Put

\[
H=P,\qquad U=X^*P^{-1/2},\qquad
V=t^{-1/2}Y^*P^{-1/2}.
\]

Direct multiplication gives \(U^*U=V^*V=I_r\) and (4). Inverses are used only for this positive definite **minimal Gram** matrix, never for potentially singular \(A,C\).

Conversely (4) gives

\[
\Delta=\begin{pmatrix}U\\\sqrt t\,V\end{pmatrix}
H\begin{pmatrix}U\\\sqrt t\,V\end{pmatrix}^*\succeq0,
\]

and \(a=\|H\|_{\rm HS}\), \(c=t\|H\|_{\rm HS}\), \(\beta=t\|H\|_{\rm HS}^2=ac\). This proves all asserted equivalences.

### Sum equality

Equality \(2\beta=a^2+c^2\) holds exactly when \(P=Q\). Equivalently, it holds exactly when \(\Delta J\Delta=0\), or exactly when

\[
A^2=BB^*,\qquad C^2=B^*B,\qquad AB=BC. \tag{6}
\]

For the zero case, sum equality requires \(A=B=C=0\). In the nonzero case it requires product equality **and** \(a=c\); equivalently (4) holds with \(t=1\). To see this without another argument, write

\[
a^2+c^2-2\beta=(a-c)^2+2(ac-\beta).
\]

Both terms are nonnegative. The equivalence with \(\Delta J\Delta=0\) also follows from \(\|SJS\|_{\rm HS}^2=0\): one direction gives \(\Delta J\Delta=S(SJS)S=0\), and the converse follows by taking \(\operatorname{tr}(\Delta J\Delta J)=0\).

### Rank consequences and strictness

For nonzero product equality,

\[
\operatorname{rank}\Delta=\operatorname{rank}A
=\operatorname{rank}B=\operatorname{rank}C=r\le\min(p,q).
\]

This follows from (4), since \(H\) is invertible and \(U,V\) are isometries. In particular every equality matrix with both blocks nonzero is singular, and both inequalities are strict if \(\Delta\) is positive definite. If \(A,C\) are positive definite and \(p\ne q\), product equality is impossible. For equal dimensions and positive definite diagonal blocks, (4) can equivalently be written \(C=tW^*AW\), \(B=\sqrt t\,AW\) for a unitary \(W\).

Equal block ranks and singularity are necessary for nonzero product equality; equal diagonal norms are additionally necessary for sum equality. None of these tests is sufficient by itself; see Examples E07–E08 below. Equality does not require rank one or scalar diagonal blocks. Rank two is possible, including with rectangular \(B\), as Example E03 shows.

For arbitrary PSD blocks the elementary kernel inclusions

\[
\ker A\subseteq\ker B^*,\qquad \ker C\subseteq\ker B
\]

follow from \(Au=0\Rightarrow\|Xu\|^2=0\), and its counterpart for \(Y\). Consequently \(\operatorname{rank}B\le\min(\operatorname{rank}A,\operatorname{rank}C)\). These weaker rank statements do not require equality.

## PB4 Sharp constants and loss of positivity

The scalar Gram matrix \(\Delta=\begin{pmatrix}1&1\\1&1\end{pmatrix}\) has \(a=c=\beta=1\). Thus the largest universal coefficient in \(K\|B\|_{\rm HS}^2\le\|A\|_{\rm HS}^2+\|C\|_{\rm HS}^2\) is \(K=2\); equivalently the smallest coefficient in \(\|B\|_{\rm HS}^2\le K(\|A\|_{\rm HS}^2+\|C\|_{\rm HS}^2)\) is \(K=1/2\). The smallest coefficient in \(\|B\|_{\rm HS}^2\le K\|A\|_{\rm HS}\|C\|_{\rm HS}\) is \(K=1\). The same sharpness examples embed into any fixed \(p,q\ge1\) by appending zero rows and columns.

Even restricting to positive definite \(\Delta\), these constants cannot be improved: for \(0<\varepsilon<1\), take scalar diagonal blocks 1 and off-diagonal block \(1-\varepsilon\). The eigenvalues are \(\varepsilon\) and \(2-\varepsilon\), and the ratios approach their sharp values as \(\varepsilon\downarrow0\). Exact equality itself remains impossible in that class.

For fixed larger \(p,q\), use \(A=\operatorname{diag}(1,\varepsilon,\ldots,\varepsilon)\), \(C=\operatorname{diag}(1,\varepsilon,\ldots,\varepsilon)\), and \(B=(1-\varepsilon)e_1f_1^*\), where \(e_1\in\mathbb C^p\), \(f_1\in\mathbb C^q\) are the first coordinate vectors. The full block matrix has eigenvalues \(2-\varepsilon\) and \(\varepsilon\) with the latter repeated \(p+q-1\) times. Moreover \(a^2=1+(p-1)\varepsilon^2\), \(c^2=1+(q-1)\varepsilon^2\), and \(\beta=(1-\varepsilon)^2\). The same limiting ratios establish optimality for each fixed pair of dimensions even under positive definiteness.

Positivity of the **full block matrix** matters:

- With \(A=C=[1]\), \(B=[2]\), the blocks \(A,C\) are positive definite but \(\Delta\) has eigenvalues 3 and −1. Here \(\beta=4>ac=1\) and \(2\beta=8>a^2+c^2=2\).
- With \(A=C=[0]\), \(B=[1]\), every finite upper bound of either homogeneous form fails, because the right side is zero. The vector \((1,-1)\) has quadratic form −2.
- With \(A=C=I_2\), \(B\) the \(2\)-by-\(2\) all-ones matrix, all scalar entrywise bounds \(|B_{ij}|^2\le A_{ii}C_{jj}\) hold. Nevertheless \(\beta=4>ac=2\); the vector \((1,1,-1,-1)\) has quadratic form −4. Checking only those scalar principal two-by-two blocks is insufficient.

PSD is a sufficient hypothesis, not a characterization of all matrices satisfying these norm inequalities. For example \(\begin{pmatrix}-1&1\\1&-1\end{pmatrix}\preceq0\) satisfies equality. Multiplying a PSD block matrix by −1 preserves all three norms.

## PB5 A reusable compression corollary

Let \(K\in\mathbb C^{n\times n}\) be PSD, \(E\in\mathbb C^{n\times p}\), and \(F\in\mathbb C^{n\times q}\). Then

\[
\|E^*KF\|_{\rm HS}^{2}
\le\|E^*KE\|_{\rm HS}\|F^*KF\|_{\rm HS},
\]

and its sum version holds as well. Proof: apply PB1–PB2 to the PSD congruence \([E\ F]^*K[E\ F]\), or use Gram factors \(X=K^{1/2}E\), \(Y=K^{1/2}F\). The equality criteria above apply unchanged to these factors. This is the supporting comparison used when a positive matrix field is compressed; no analytic hypotheses from the source's headline theorem enter this corollary.

## Exact examples and what computation establishes

`exact-examples.json` records every matrix over the Gaussian rationals, its dimensions and ranks, exact squared norms, gap identities, and an exact positivity or nonpositivity certificate. `check_exact_examples.py` is original Python using only the standard library. No downloaded source program, package installation, numerical eigensolver, or floating-point arithmetic is used. Its Gram witnesses certify positivity of the individual examples; finite checks do not prove the general theorem. The universal proofs are PB1–PB5 above.

For the following Gram examples, \(\Delta=[X\ Y]^*[X\ Y]\); thus the full matrix is determined without any approximate square roots.

- **E01 Scalar sharpness.** \(X=Y=[1]\). Squared norms \((a^2,c^2,\beta)=(1,1,1)\). Both equalities hold.
- **E02 Complex unbalanced equality.** \(X=[1]\), \(Y=[2i]\). Then \(A=[1],B=[2i],C=[4]\), \((a^2,c^2,\beta)=(1,16,4)\). Product equality holds; the sum gap is 9.
- **E03 Rectangular rank two equality.** \(X=\operatorname{diag}(1,2)\), \(Y=\begin{pmatrix}1&0&0\\0&2i&0\end{pmatrix}\). Here \(A=\operatorname{diag}(1,4)\), \(C=\operatorname{diag}(1,4,0)\), \(B=\begin{pmatrix}1&0&0\\0&4i&0\end{pmatrix}\), \((a^2,c^2,\beta)=(17,17,17)\), and \(\operatorname{rank}\Delta=2\). Both equalities hold.
- **E04 Rectangular unbalanced equality.** Keep E03's \(X\), replace \(Y\) by \(\begin{pmatrix}3/2&0&0\\0&3i&0\end{pmatrix}\). Then \((a^2,c^2,\beta)=(17,1377/16,153/4)\), \(t=9/4\), and sum gap \(425/16\). Product equality holds.
- **E05 Nondiagonal Gaussian rational equality.** \(X=[1\ i]\), \(Y=[1\ (3/5)i\ 4/5]\). Both \(XX^*\) and \(YY^*\) equal \([2]\), so \((a^2,c^2,\beta)=(4,4,4)\). Here \(p=2,q=3\), the full block matrix has rank one, and both equalities hold.
- **E06 Strict positive definite example.** \(X=(1,0,0,0)^T\), \(Y=(1/2,1/2,1/2,1/2)^T\). Then \(\Delta=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}\), \((a^2,c^2,\beta)=(1,1,1/4)\), and sum gap \(3/2\). Both inequalities are strict.
- **E07 Equal ranks do not force equality.** \(X=I_2\), \(Y=\operatorname{diag}(1,2)\). All four ranks \(\operatorname{rank}\Delta,\operatorname{rank}A,\operatorname{rank}B,\operatorname{rank}C\) are 2, but \((a^2,c^2,\beta)=(2,17,5)\), and \(\beta^2=25<34=a^2c^2\).
- **E08 Equal norms do not force equality or a Loewner square bound.** \(X=\operatorname{diag}(2,1)\), \(Y=\operatorname{diag}(1,2)\). Then \((a^2,c^2,\beta)=(17,17,8)\), and sum gap 18. Moreover \(A^2-BB^*=\operatorname{diag}(12,-3)\) is not PSD. Thus the trace estimate is not the unasserted general matrix inequality \(BB^*\preceq A^2\).
- **E09 Zero left block.** \(X=[0\ 0]\), \(Y=[1\ i]\). Then \(A=B=0\), \(C=\begin{pmatrix}1&i\\-i&1\end{pmatrix}\), \((a^2,c^2,\beta)=(0,4,0)\). Product equality holds and sum inequality is strict.
- **E10 Zero right block.** \(X=[2]\), \(Y=[0\ 0]\). Squared norms \((16,0,0)\); product equality holds and sum inequality is strict.
- **E11 All zero.** \(X=[0\ 0]\), \(Y=[0\ 0\ 0]\). Both equalities hold.
- **E12–E14** are the three non-PSD counterexamples in PB4, with exact negative quadratic-form witnesses.
- **E15** is the negative semidefinite equality example in PB4, certified by \(-\Delta=[1\ {-1}]^*[1\ {-1}]\).
- **E16 Nondiagonal rank two rectangular equality.** Let \(X=\begin{pmatrix}1&i\\1&2\end{pmatrix}\), \(W=\begin{pmatrix}3/5&4/5&0\\0&0&i\end{pmatrix}\), and \(Y=2XW=\begin{pmatrix}6/5&8/5&-2\\6/5&8/5&4i\end{pmatrix}\). Since \(WW^*=I_2\), one has \(Q=4P\). Here \(A=\begin{pmatrix}2&2+i\\2-i&5\end{pmatrix}\), \((a^2,c^2,\beta)=(39,624,156)\), \(t=4\), and sum gap 351. Product equality holds with \(\operatorname{rank}\Delta=2\).

The script additionally checks a reproducible finite set of 180 Gaussian-rational Gram fixtures with \(1\le d\le3\), \(1\le p\le3\), and \(1\le q\le4\). It verifies trace identities, both inequalities (squaring only nonnegative quantities), exact ranks, and the intrinsic equality identities whenever equality occurs. This is test coverage, not a claim that finitely many cases verify all dimensions.

## Review and reuse boundaries

- Theorems PB1–PB5 are ordinary mathematical proofs reconstructed in this study; separate independent review is initially pending.
- JSON is provisional portable theorem/dependency data. It is not asserted to match a native MRS schema and has not been imported.
- Source provenance is pinned; a SHA-256 of the inspected TeX snapshot is recorded in `provenance.json`.
- No new Lean run, kernel-checked theorem, exact source-to-Lean theorem match, publication, or proof of the complete Crouzeix theorem is claimed.
