# Exact proofs and the scope of the bounded study

This document gives human proofs of classical facts used by the scripts. It does
not claim a new construction theorem, a classification of Hadamard matrices, or
a Lean formalization. All orders in this document are positive integers.

A **Hadamard matrix of order $n$** is a matrix
$H\in\{-1,+1\}^{n\times n}$ satisfying

$$HH^{\mathsf T}=nI_n.$$

Equivalently, its distinct rows have zero scalar product. The diagonal scalar
products are automatically $n$. Here $I_n$ is the identity matrix,
$\mathbf1$ is an all-one column vector of the indicated size, and
$J_n=\mathbf1\mathbf1^{\mathsf T}$.

## 1. Necessary orders

**Proposition.** If a Hadamard matrix of order $n$ exists, then $n=1$, $n=2$, or
$4\mid n$.

**Proof.** Multiplying columns by signs preserves all row scalar products. Do
this to make the first row entirely $+1$. If $n>1$, orthogonality with a second
row implies that this row contains equally many positive and negative entries,
so $n$ is even. Permute columns to put its $n/2$ positive entries first.

If $n>2$, there is a third row. Let $a$ and $b$ be its numbers of positive
entries in the first and second halves of the columns. Its scalar products
with the first and second rows give, respectively,

$$2(a+b)-n=0,\qquad 2(a-b)=0.$$

Thus $a=b$ and $n=4a$. The exceptional orders do occur: $[1]$ has order $1$,
and $\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ has order $2$. $\square$

This proves a necessary condition. It does not prove the existence of a matrix
at every order divisible by four.

## 2. Tensor closure and Sylvester doubling

**Proposition.** If $H$ and $K$ are Hadamard matrices of orders $a$ and $b$, then
their Kronecker product $H\otimes K$ is Hadamard of order $ab$.

**Proof.** Index rows by pairs $(i,u)$ and columns by $(j,v)$, and define
$(H\otimes K)_{(i,u),(j,v)}=H_{ij}K_{uv}$. Its entries are signs. The scalar
product of rows $(i,u)$ and $(i',u')$ is

$$\sum_{j,v}H_{ij}K_{uv}H_{i'j}K_{u'v}
=\left(\sum_jH_{ij}H_{i'j}\right)
 \left(\sum_vK_{uv}K_{u'v}\right)
=ab\,\delta_{ii'}\delta_{uu'}.$$

This is the required Gram matrix. $\square$

Taking $K=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ yields the Sylvester step

$$H\longmapsto\begin{pmatrix}H&H\\H&-H\end{pmatrix}.$$

Starting with $[1]$ gives a Hadamard matrix at every order $2^k$, $k\geq0$.

## 3. Prime Paley construction with the implemented signs

Let $p$ be a prime with $p\equiv3\pmod4$. Work in the field
$\mathbb F_p=\mathbb Z/p\mathbb Z$. Its quadratic character is

$$\chi(t)=\begin{cases}
0,&t=0,\\
1,&t\text{ is a nonzero square},\\
-1,&t\text{ is not a square}.
\end{cases}$$

The nonzero squares form a subgroup of $\mathbb F_p^\times$ of size
$(p-1)/2$: the squaring map has exactly the two preimages $x,-x$ for each
nonzero square. Its other coset consists of the nonsquares. Consequently
$\chi(st)=\chi(s)\chi(t)$, including when either argument is zero, and

$$\sum_{t\in\mathbb F_p}\chi(t)=0.$$

Also $\chi(-1)=-1$. Indeed, if $z^2=-1$, then multiplication by $z$ permutes
the nonzero field elements. Multiplying all these elements and cancelling
their nonzero product gives $z^{p-1}=1$. On the other hand,
$z^{p-1}=(-1)^{(p-1)/2}=-1$, a contradiction. This establishes the character
facts used below without an assumption about a primitive root.

### The character-sum identity

**Lemma.** For every nonzero $t\in\mathbb F_p$,

$$\sum_{u\in\mathbb F_p}\chi(u^2-t)=-1.$$

**Proof.** Count solutions $(u,v)$ of $u^2-v^2=t$. For a fixed $u$, the
number of $v$ is $1+\chi(u^2-t)$; this also holds when $u^2-t=0$. Thus the
number of solutions is $p+\sum_u\chi(u^2-t)$.

The change of variables $r=u-v$, $s=u+v$ is invertible because $2$ is
invertible in $\mathbb F_p$. It turns the equation into $rs=t$. Each of the
$p-1$ nonzero choices of $r$ gives exactly one $s=t/r$. Hence the number of
solutions is $p-1$, proving the formula. $\square$

If $i\ne j$, multiplicativity, completing the square, and the bijection
$u=2k-i-j$ now give

$$\begin{aligned}
\sum_k\chi(k-i)\chi(k-j)
&=\sum_k\chi((k-i)(k-j))\\
&=\sum_u\chi\bigl(u^2-(i-j)^2\bigr)=-1.
\end{aligned}$$

The factor $1/4$ in the completed square has character $+1$, so it disappears
from this equation. The lemma applies because $(i-j)^2\ne0$. For $i=j$ the
sum is $p-1$, since exactly one summand is zero and all the others are $1$.

### The matrix identity

Index a $p\times p$ matrix by $i,j\in\mathbb F_p$ and set

$$Q_{ij}=\chi(j-i),\qquad C=Q+I_p,\qquad
H=\begin{pmatrix}1&\mathbf1^{\mathsf T}\\-\mathbf1&C\end{pmatrix}.$$

**Theorem.** This $H$ is Hadamard of order $p+1$.

**Proof.** Its entries are signs: $Q$ has zero diagonal and sign entries off
the diagonal. The character facts and the identity just proved give

$$Q^{\mathsf T}=-Q,\qquad Q\mathbf1=0,\qquad
QQ^{\mathsf T}=pI_p-J_p.$$

Therefore

$$C\mathbf1=\mathbf1,\qquad
CC^{\mathsf T}=QQ^{\mathsf T}+Q+Q^{\mathsf T}+I_p
=(p+1)I_p-J_p.$$

Multiplying the displayed block matrix by its transpose yields

$$HH^{\mathsf T}=
\begin{pmatrix}
p+1&-\mathbf1^{\mathsf T}+\mathbf1^{\mathsf T}C^{\mathsf T}\\
-\mathbf1+C\mathbf1&J_p+CC^{\mathsf T}
\end{pmatrix}
=(p+1)I_{p+1}.$$

In particular, the first column below the corner is $-\mathbf1$. Together
with $C=Q+I_p$, that sign makes the off-diagonal blocks vanish. $\square$

This proof concerns primes $p\equiv3\pmod4$. It does not implement or prove
the other Paley construction, or the extension from primes to prime powers.

## 4. Symmetric circulants and periodic autocorrelation

Fix an odd core order $m=2h+1$. Sequence indices and matrix indices in this
section are taken modulo $m$. A **symmetric sign sequence** is a sequence
$x=(x_0,\ldots,x_{m-1})\in\{-1,+1\}^m$ with $x_j=x_{-j}$ for every $j$.
Its circulant matrix is defined by

$$\operatorname{circ}(x)_{ij}=x_{j-i}.$$

This convention agrees with `scripts/hadamard.py`. Symmetry of the sequence
gives $\operatorname{circ}(x)^{\mathsf T}=\operatorname{circ}(x)$.
Circulant matrices commute: if $P$ is the
cyclic shift with $P_{ij}=1$ exactly when $j=i+1$, then
$\operatorname{circ}(x)=\sum_{j=0}^{m-1}x_jP^j$, so all circulants are
polynomials in $P$.

Define the **periodic autocorrelation** at shift $s$ by

$$\operatorname{PAF}_x(s)=\sum_{j=0}^{m-1}x_jx_{j+s}.$$

Then $\operatorname{PAF}_x(0)=m$ and
$\operatorname{PAF}_x(-s)=\operatorname{PAF}_x(s)$ by reindexing. Direct
matrix multiplication gives

$$(\operatorname{circ}(x)\operatorname{circ}(x)^{\mathsf T})_{ij}
=\sum_kx_{k-i}x_{k-j}=\operatorname{PAF}_x(i-j).$$

**Proposition.** Four symmetric sign sequences $a,b,c,d$ define a
**Williamson quadruple** exactly when either of the following equivalent
conditions holds, with $A=\operatorname{circ}(a)$,
$B=\operatorname{circ}(b)$, $C=\operatorname{circ}(c)$,
$D=\operatorname{circ}(d)$:

$$A^2+B^2+C^2+D^2=4mI_m;$$

$$\operatorname{PAF}_a(s)+\operatorname{PAF}_b(s)
+\operatorname{PAF}_c(s)+\operatorname{PAF}_d(s)=0
\quad(1\leq s\leq h).$$

**Proof.** Symmetry identifies $\operatorname{circ}(x)^2$ with
$\operatorname{circ}(x)\operatorname{circ}(x)^{\mathsf T}$.
The diagonal sum is always $4m$. The $h$ tested shifts, together with their
negatives, cover every nonzero residue modulo the odd number $m$. The
entry formula therefore proves both implications. For $m=1$ the condition
on nonzero shifts is empty, and the same statement holds. $\square$

## 5. The Williamson array

**Theorem.** A Williamson quadruple gives a Hadamard matrix of order $4m$ by
the array

$$W=\begin{pmatrix}
A&B&C&D\\
-B&A&-D&C\\
-C&D&A&-B\\
-D&-C&B&A
\end{pmatrix}.$$

**Proof.** Every entry is a sign. Since the four blocks are symmetric, each
diagonal block of $WW^{\mathsf T}$ is
$S=A^2+B^2+C^2+D^2$. The six blocks above the block diagonal are

$$\begin{array}{ll}
(1,2):&-AB+BA-CD+DC,\\
(1,3):&-AC+BD+CA-DB,\\
(1,4):&-AD-BC+CB+DA,\\
(2,3):&BC+AD-DA-CB,\\
(2,4):&BD-AC-DB+CA,\\
(3,4):&CD-DC+AB-BA.
\end{array}$$

All are zero because circulants commute. The blocks below the diagonal are
their transposes. Thus $WW^{\mathsf T}=\operatorname{diag}(S,S,S,S)$, and
the Williamson identity $S=4mI_m$ proves the result. $\square$

The same multiplication proves the converse for this particular array of
symmetric circulants: if it is Hadamard, its diagonal blocks force the
Williamson identity. This is a statement about the specified block family.

## 6. Row-sum identity and its limits

Write $r_x=\sum_jx_j$. Summing autocorrelations over all shifts gives

$$\sum_{s=0}^{m-1}\operatorname{PAF}_x(s)
=\sum_{j,k}x_jx_k=r_x^2.$$

It follows that every Williamson quadruple satisfies

$$r_a^2+r_b^2+r_c^2+r_d^2=4m.$$

Equivalently, apply $A^2+B^2+C^2+D^2=4mI_m$ to $\mathbf1$, using
$\operatorname{circ}(x)\mathbf1=r_x\mathbf1$.

Multiplying a whole sequence by $-1$ preserves its symmetry and every
autocorrelation. We may therefore normalize each of the four sequences
independently to $x_0=+1$. A normalized sequence has $h$ independent signs
$x_1,\ldots,x_h$. If $k$ of them are negative, then

$$r_x=1+2\sum_{j=1}^hx_j=m-4k,\qquad 0\leq k\leq h.$$

In particular its row sum is odd and congruent to $m$ modulo $4$. Its
possible absolute row sums are exactly $1,3,\ldots,m$. To see the latter
claim, for any odd $t\leq m$ exactly one of $t,-t$ is congruent to $m$
modulo $4$. That choice lies between $2-m$ and $m$, so it equals $m-4k$
for an integer $k$ in the indicated range; choose any $k$ negative pairs.

Thus the arithmetic list of candidate absolute row-sum types is precisely

$$1\leq t_1\leq t_2\leq t_3\leq t_4\leq m,\qquad
t_i\text{ odd},\qquad \sum_{i=1}^4t_i^2=4m.$$

This is a necessary filter on a quadruple, and it does not replace the
individual autocorrelation equations. For example, at $m=5$ let
$u=(1,-1,-1,-1,-1)$ and $v=(1,1,-1,-1,1)$. The normalized symmetric
quadruple $(u,u,v,v)$ has squared row sums $9+9+1+1=20$. But
$\operatorname{PAF}_u(1)=\operatorname{PAF}_v(1)=1$, so its total
autocorrelation at shift $1$ is $4$, and it is not a Williamson quadruple.

## 7. Exact completeness of the bounded enumeration

For a fixed odd $m=2h+1$, let $N=2^h$. Enumerate the normalized symmetric
sequences by indices $a=0,\ldots,N-1$, with

$$x^{(a)}_0=1,\qquad
x^{(a)}_j=x^{(a)}_{m-j}=1-2\operatorname{bit}_{j-1}(a)
\quad(1\leq j\leq h).$$

Here $\operatorname{bit}_k(a)\in\{0,1\}$ is bit $k$ in the binary
expansion of $a$, with bit zero least significant. This is a bijection:
every choice of the $h$ independent signs has exactly one bit pattern.
Define its integer profile by

$$v_a=(\operatorname{PAF}_{x^{(a)}}(1),\ldots,
       \operatorname{PAF}_{x^{(a)}}(h))\in\mathbb Z^h.$$

The implemented pair-bucket algorithm is:

1. For every pair $0\leq a\leq b<N$, append $(a,b)$ to the bucket whose key
   is the exact vector $v_a+v_b$.
2. For every bucket key $q$, match every pair $(a,b)$ in that bucket with
   every pair $(c,d)$ in the bucket of key $-q$.
3. Emit the tuple only when $b\leq c$.

Every emitted tuple has $a\leq b\leq c\leq d$ and profile sum zero, so it
is a Williamson quadruple by Section 4. Conversely, take any normalized
solution, permute its four indices into $a\leq b\leq c\leq d$, and put
$q=v_a+v_b$. The pair $(a,b)$ is in the $q$ bucket, and $(c,d)$ is in the
$-q$ bucket because the total profile is zero. The algorithm matches them
and accepts $b\leq c$. Thus every normalized solution is covered up to
permutation of its four blocks. Independent sign normalization proves
completeness for existence among all symmetric sign sequences as well.

Each sorted index tuple is emitted exactly once: it fixes its first pair,
second pair, and first-pair key, and each such pair was inserted once.
This remains true with repeated indices or the zero key. At $m=1$ there
is one sequence, the profile is the empty vector, and the unique tuple is
$(0,0,0,0)$, so the boundary case is included.

The resulting count is a count of multisets of four normalized sequences
solving the autocorrelation equations. It is not a count of Hadamard
equivalence classes, Williamson equivalence classes, or inequivalent
matrices. No reduction by shifts, index multipliers, or other matrix
equivalences is asserted. The use of absolute row sums is a label for
grouping the found solutions; it does not discard any solutions.

Consequently an arithmetic row-sum type absent from a completed search at
a stated core order is absent from this symmetric circulant Williamson
family at that core order. This conclusion is confined to that family.

## 8. Meaning of an exact matrix verification

For two sign rows of length $n$, let $d$ be the number of positions where
their entries differ. Their scalar product is exactly

$$(n-d)-d=n-2d.$$

After checking that a matrix is square and all its entries are integer
signs, checking this expression for every unordered pair of distinct rows
establishes all off-diagonal entries of $HH^{\mathsf T}$. The diagonal
entries are already $n$. Thus an exact check of all $n(n-1)/2$ pairs
certifies the Hadamard identity for that supplied finite matrix. A file
hash identifies which bytes were checked; the hash alone is not an
orthogonality argument. At order $668$, the number of row pairs is
$668\cdot667/2=222778$.

## 9. Bounds on the conclusions and historical pointers

The finite Williamson computation covers exactly the reported odd core
orders $m=1,3,\ldots,15$. Its completeness proof has a parameter $m$, but
a completed computation at these eight values supplies no computational
claim for larger values. In particular, $m=167$ has

$$2^{(167-1)/2}=2^{83}$$

normalized symmetric sequences before forming pairs or quadruples. Even
listing all these single sequences is beyond the resources of this naive
bounded search. This resource limitation supplies no nonexistence
obstruction, either for Williamson quadruples at $m=167$ or for Hadamard
matrices at order $668$.

Paley prime constructions and tensor closure provide explicit infinite
families. A finite list of their instances, or a finite table of orders
reachable from selected seeds by tensor products, does not prove existence
at every positive multiple of four. Failure of an order to appear in such
a table only concerns the constructions included in that table.

The classical sources below are bibliographic pointers. The proofs and
matrix conventions above are supplied in this document. Publisher records
for Paley and Williamson were checked on 2026-10-15; their complete original
texts were not available through the browser used for this study.

- R. E. A. C. Paley, “On Orthogonal Matrices,” *Journal of Mathematics and
  Physics* **12** (1933), 311–320.
  [Original publisher record](https://onlinelibrary.wiley.com/doi/10.1002/sapm1933121311).
- J. Williamson, “Hadamard's determinant theorem and the sum of four
  squares,” *Duke Mathematical Journal* **11** (1944), 65–81.
  [Original publisher record](https://projecteuclid.org/journals/duke-mathematical-journal/volume-11/issue-1/Hadamards-determinant-theorem-and-the-sum-of-four-squares/10.1215/S0012-7094-44-01108-7.full).
- J. J. Sylvester (1867), “Thoughts on Inverse Orthogonal Matrices…”
  *Philosophical Magazine*, series 4, **34**, 461–475. This bibliographic
  pointer is recorded in the references of Paley's publisher page above;
  the original Sylvester article was not inspected here.
