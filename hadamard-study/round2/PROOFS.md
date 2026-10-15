# Round 2: sound Williamson criteria and search reductions

This document proves the criteria used in the second bounded experiment. They
are classical Williamson constraints and consequences of its matrix identity;
no new theorem or Lean formalization is claimed. The first edition, including
the Hadamard construction proof, remains in [the original proofs](../PROOFS.md).

Throughout, $m=2h+1$ is a positive odd integer. A candidate is a **complete**
sign sequence $x=(x_0,\ldots,x_{m-1})$ with

$$x_0=1,\qquad x_j=x_{-j}\in\{-1,1\},$$

where indices are residues modulo $m$. Define

$$C_x(i,j)=x_{j-i},\qquad
P_x(s)=\sum_{j=0}^{m-1}x_jx_{j+s},\qquad r_x=\sum_jx_j.$$

The circulant $C_x$ is symmetric. The four-sequence Williamson condition is

$$\sum_{x\in(a,b,c,d)}C_xC_x^{\mathsf T}=4mI_m.\tag{1}$$

Here and below a sum over a tuple counts repeated sequences with their
multiplicities. By direct multiplication,
$(C_xC_x^{\mathsf T})_{ij}=P_x(i-j)$, and $P_x(-s)=P_x(s)$. Thus (1) is
equivalent to

$$P_a(s)+P_b(s)+P_c(s)+P_d(s)=0\quad(1\leq s\leq h).\tag{2}$$

The diagonal equations hold automatically because $P_x(0)=m$. These are
criteria for symmetric circulant Williamson quadruples at odd core order
$m$, whose standard block array gives a Hadamard matrix of order $4m$.

## 1. The odd-order product theorem

**Theorem (Williamson's product theorem, normalized form).** Every quadruple
satisfying (1) has

$$a_jb_jc_jd_j=-1\quad\text{for every }j\ne0.\tag{3}$$

**Proof.** Work in the cyclic polynomial ring
$R=\mathbb Z[z]/(z^m-1)$, in which every element has a unique expression
$\sum_{j=0}^{m-1}u_jz^j$. Polynomial multiplication is cyclic convolution.
For a sequence $x$ put

$$X_x=\sum_jx_jz^j,\qquad
T=\sum_jz^j,\qquad
N_x=\sum_{j:x_j=-1}z^j.$$

Then $X_x=T-2N_x$. Let $P_{ij}$ be $1$ when $j=i+1$ modulo $m$ and
$0$ otherwise. Substitution of this cyclic shift matrix for $z$ sends
$X_x$ to $C_x$. This substitution is injective: the first row of
$\sum_ju_jP^j$ is $(u_0,\ldots,u_{m-1})$. Since each $C_x$ is symmetric,
(1) therefore gives the identity

$$X_a^2+X_b^2+X_c^2+X_d^2=4m\cdot1\quad\text{in }R.$$

Write $R_-=|N_a|+|N_b|+|N_c|+|N_d|$, where $|N_x|$ denotes the number
of negative positions. We have $T^2=mT$ and $TN_x=|N_x|T$, since
multiplication by a monomial permutes the terms of $T$. Expanding the four
squares gives

$$4mT-4R_-T+4\sum_xN_x^2=4m\cdot1.$$

Divide its integer coefficients by four **before** reducing modulo two:

$$\sum_xN_x^2+(m-R_-)T=m\cdot1.\tag{4}$$

Every negative support consists of pairs $\{j,-j\}$: position zero is
positive, and an odd cyclic group has no other position equal to its own
negative. Hence $R_-$ is even and $m-R_-$ is odd.

In characteristic two the cross terms in a square vanish, so

$$N_x^2\equiv\sum_{j:x_j=-1}z^{2j}\pmod2.$$

Because $m$ is odd, $j\mapsto2j$ permutes the residues modulo $m$.
For any nonzero $j$, compare the coefficient of $z^{2j}$ in (4). Its
right-hand side is zero, while its $T$ term is odd. Therefore the number
of sequences in the quadruple having a negative entry at position $j$
is odd. The product of their four entries is consequently $-1$.
$\square$

For unnormalized symmetric sign sequences, independently multiplying each
sequence by its position-zero sign preserves (1) and yields
$a_jb_jc_jd_j=-a_0b_0c_0d_0$. Oddness, symmetry, and the normalization
are substantive hypotheses of the proof above.

### Exact mask form

Retain the original bit-mask labels from the first edition:

$$x^{(a)}_j=x^{(a)}_{m-j}=1-2\operatorname{bit}_{j-1}(a)
\quad(1\leq j\leq h),\qquad 0\leq a<2^h.$$

Let $M=2^h-1$ be the mask with all $h$ bits set, and let $\oplus$ denote
bitwise XOR. At each bit, (3) means that the four negative-entry bits have
odd sum. Thus every normalized solution satisfies

$$a\oplus b\oplus c\oplus d=M,\qquad
d=M\oplus a\oplus b\oplus c.\tag{5}$$

Filtered candidates retain these original masks. An index into a shorter
filtered list cannot be substituted for a sequence's mask in (5). At
$m=1$, $h=0$ and $M=0$, and the statement is the empty-bit identity.

## 2. Exact row-sum restrictions on singles and pairs

For any sequence, summing its autocorrelations over every shift gives

$$\sum_{s=0}^{m-1}P_x(s)=r_x^2.$$

Consequently (2) implies

$$r_a^2+r_b^2+r_c^2+r_d^2=4m.\tag{6}$$

If $k$ of a normalized sequence's $h$ independent signs are negative,
$r_x=m-4k$. Its possible absolute row sums are exactly the odd integers
$1,3,\ldots,m$: for any such $t$, exactly one of $t,-t$ is congruent to
$m$ modulo four and lies in the range $2-m,\ldots,m$.
Define the finite square set

$$W_m=\{t^2:1\leq t\leq m,\ t\text{ odd}\}.$$

The notation $W_m+W_m$ and $W_m+W_m+W_m$ means sums with repetition
allowed. Every member of a valid quadruple must obey

$$4m-r_x^2\in W_m+W_m+W_m,\tag{7}$$

and every pair of its members must obey

$$4m-r_x^2-r_y^2\in W_m+W_m.\tag{8}$$

These follow from the squared row sums of the missing members in (6).
They are safe rejection tests, even when the two selected sequences are
equal. They also imply the simpler bounds $r_x^2\leq4m-3$ and
$r_x^2+r_y^2\leq4m-2$.

The sets in (7) and (8) are global arithmetic sets. They do not assume an
unproved restriction on the masks of the missing sequences, their order
in a filtered list, or the available suffix of that list. Passing these
tests guarantees an arithmetic decomposition of the remaining square
sum, and does not guarantee a Williamson completion.

The implementation stores only two-square and three-square sums at most
$4m$. This truncation is safe: each tested remainder is at most $4m$,
and all summands are positive. Every intermediate two-square sum in a
relevant three-square decomposition is therefore also at most $4m$.

For later comparison, define the full half-lag profile
$q_a=(P_{x^{(a)}}(1),\ldots,P_{x^{(a)}}(h))$. The identity above also gives

$$r_{x^{(a)}}^2=m+2\sum_{s=1}^h(q_a)_s.$$

Thus a pair's full profile sum already determines its row-square sum.
Testing (8) before storing a pair can reject it early; adding the same
row-square information to a full-profile key supplies no independent
constraint.

## 3. Exact energy rejection for a partial tuple

Here a **partial tuple** consists of some complete candidate sequences
from the eventual four-member tuple. It does not mean a sequence with
unknown entries.

**Proposition.** If complete sequences $x_1,\ldots,x_k$, $k\leq4$, occur
together in a Williamson quadruple, then for every real vector $v$,

$$\sum_{i=1}^k\|C_{x_i}^{\mathsf T}v\|^2
\leq4m\|v\|^2.\tag{9}$$

**Proof.** Apply $v^{\mathsf T}(\cdot)v$ to (1). The four contributions are
the nonnegative squares $\|C_x^{\mathsf T}v\|^2$. Removing any of them
can only decrease the sum. $\square$

Equivalently, the residual matrix
$4mI_m-\sum_{i=1}^kC_{x_i}C_{x_i}^{\mathsf T}$ must be positive
semidefinite. One integer vector violating (9) is an exact certificate
that the selected members have no completion within this family.
Rejection uses a **strict** $>$ comparison; equality is allowed.

### Integer evaluation from autocorrelations

For an integer test vector $v=(v_0,\ldots,v_{m-1})$, define
$P_v(s)=\sum_jv_jv_{j+s}$ and $L_v=\sum_jv_j^2$. Directly expanding the
square and grouping terms by their index difference gives

$$\begin{aligned}
E_v(x):=\|C_x^{\mathsf T}v\|^2
&=\sum_{s=0}^{m-1}P_x(s)P_v(s)\\
&=mL_v+2\sum_{s=1}^hP_x(s)P_v(s).\tag{10}
\end{aligned}$$

All quantities in (10) are integers. For a single sequence the rejection
test is $E_v(x)>4mL_v$; for a pair it is
$E_v(x)+E_v(y)>4mL_v$. Equation (9) proves these tests sound for any
chosen integer vectors, including a deterministic finite bank.

The implemented triangular probes are specified without trigonometry.
For each $f=1,\ldots,h$, and each $j=0,\ldots,m-1$, put

$$u_{f,j}=(fj)\bmod m,\qquad
t_{f,j}=m-4\min(u_{f,j},m-u_{f,j}),$$

$$v_{f,j}=m\,t_{f,j}-\sum_{k=0}^{m-1}t_{f,k}.\tag{11}$$

These are integer vectors and have zero coordinate sum. Centering them
does not add an assumption about a solution: (9) holds for every vector.
The probes need not be linearly independent or pure Fourier modes for
their rejection inequalities to be valid. A zero vector may be omitted,
since its inequality is $0\leq0$. At $m=1$ the bank is empty.

This finite bank is an exact collection of necessary inequalities. Passing
it does not certify that the residual matrix is positive semidefinite,
and it does not certify that all Fourier power spectral density bounds
hold. In particular, “exact” refers to integer evaluation and sound
rejection, not to completeness of the finite probe bank. The tests apply
to fully assigned sign sequences; no argument here justifies filling
unknown signs with zero and treating the resulting energy as a lower
bound.

## 4. An exact order-three specialization

Suppose $3\mid m$. Compress a sequence into its three residue sums

$$c_r(x)=\sum_{j\equiv r\pmod3}x_j\quad(r=0,1,2).$$

Symmetry gives $c_1(x)=c_2(x)$. Set
$\delta_x=c_0(x)-c_1(x)$, and let $w$ be the integer vector with the
repeating pattern $(2,-1,-1)$. Grouping the terms in
$(C_x^{\mathsf T}w)_j=\sum_tx_tw_{j-t}$ by $t$ modulo three gives

$$C_x^{\mathsf T}w=\delta_xw.$$

For example, at $j\equiv0$ its value is
$2c_0-c_1-c_2=2\delta_x$, and at the other residues its value is
$-c_0+c_1=-\delta_x$. Since $\|w\|^2=2m>0$, (9) implies the exact
single and pair conditions

$$\delta_x^2\leq4m,\qquad \delta_x^2+\delta_y^2\leq4m.\tag{12}$$

For a full Williamson quadruple the sum of all four $\delta^2$ values
equals $4m$. In Fourier language $\delta_x^2$ is the power at the
nonzero order-three frequency: if $\omega^3=1$ and $\omega\ne1$, then
$\sum_jx_j\omega^j=c_0+c_1\omega+c_1\omega^2=\delta_x$.
No floating-point root of unity is needed to compute it.

The triangular bank already contains this same inequality. When $3\mid m$,
its frequency $f=m/3$ belongs to $1,\ldots,h$. The values in (11) repeat
as $(m,-m/3,-m/3)$ before centering, so their sum is $m^2/9$. Hence

$$v_{m/3}=\frac{4m^2}{9}\,w.$$

This nonzero integer scaling cancels from both sides of the single and
pair energy inequalities, giving exactly (12). The earlier order-three
stage can save the cost of evaluating the remaining probes, but adds no
further rejection beyond the full triangular bank. Comparing the row,
row-plus-order-three, and all-probe stages measures this cheaper-stage
effect; it does not establish independence of the order-three criterion
from that bank.

This is a necessary test obtained by projecting a complete sequence onto
three residue sums. It does not enumerate compressed objects or assert
that arbitrary passing compressed data lift to Williamson sequences.
It is applied only when $3$ divides $m$.

## 5. Why safe spectral filters remain necessary conditions

For a proper partial tuple, even the full positive semidefinite condition
need not imply completion. An exact example occurs at $m=7$. Let the
three normalized sequences have negative positions $\{\pm1\}$,
$\{\pm2\}$, and $\{\pm3\}$, respectively. Their masks are $1,2,4$.
Their squared row sums are each $9$, and their circulants satisfy

$$C_1^2+C_2^2+C_4^2=20I_7+J_7.$$

To verify this identity in the cyclic ring, write
$N_j=z^j+z^{-j}$. Then $\sum_{j=1}^3N_j=T-1$ and
$\sum_{j=1}^3N_j^2=T+5$, since $\{\pm2,\pm4,\pm6\}$ consists of the
six nonzero residues modulo seven. Expanding
$\sum_{j=1}^3(T-2N_j)^2$ gives $20+T$.
The residual is $8I_7-J_7$, which is positive definite: it has eigenvalue
$1$ on the constant vectors and eigenvalue $8$ on their orthogonal
complement. Every test (9) therefore passes for this three-member tuple.

However, (5) forces its fourth mask to be $7\oplus1\oplus2\oplus4=0$,
the all-positive sequence with squared row sum $49$, whereas (6) requires
the remaining square to be $28-27=1$. Hence no Williamson completion
exists. The search combines criteria and finally checks the full
autocorrelation equations. For exactly four complete sign sequences,
full residual positive semidefiniteness would imply (1), since its trace
is zero; the limited probe bank does not establish that premise.

## 6. Coverage of the filtered full-profile pair search

Let $S$ be the original masks retained after the single-sequence row-sum
test (7), the available order-three test (12), and all chosen integer
energy tests. Every member of every normalized Williamson solution
belongs to $S$, by the proofs above.

For every $a\leq b$ in $S$, allow repetition, and retain the pair if it
passes (8) and the selected pair energy tests, including (12) when
applicable. Every pair drawn from a valid quadruple passes these tests.
Store the pair under the full profile key $q_a+q_b$.

Match every retained pair $(a,b)$ under key $q$ with every retained pair
$(c,d)$ under key $-q$, and emit only if $b\leq c$. Every emitted tuple
satisfies (2) and is therefore a Williamson solution. Conversely, sort
any valid normalized tuple as $a\leq b\leq c\leq d$. Its two pairs
survive, and their keys are exact negatives. The match is visited and
accepted. Thus the filters preserve completeness for the family at every
core order where the finite algorithm is fully executed.

Each sorted tuple is emitted once, because it determines its first pair,
second pair, and first-pair key. This argument includes repeated masks,
zero profile keys, and the empty profile at $m=1$. Counts remain counts
of multisets of four normalized sequences, without a classification by
Hadamard or Williamson equivalence.

### Adding the product mask to a full-profile key

An optional pair key is $(a\oplus b,q_a+q_b)$. Its unique complementary
key is

$$(M\oplus(a\oplus b),-q_a-q_b).\tag{13}$$

The product theorem proves that every solution's two pairs match (13),
so this change is sound and retains the same coverage and uniqueness.
However, an exact complementary match of **full** profiles already
satisfies (2) and hence already satisfies the product theorem. Therefore
adding the product mask cannot eliminate any mathematically matched
quadruple from the full-profile join. Any measured runtime or storage
difference is an implementation effect; this is not an additional
solution reduction after exact full-profile matching.

## 7. Coverage of product-forced triple enumeration

A separate algorithm uses (5) before looking up the final sequence:

1. Visit every triple $a\leq b\leq c$ from $S$, allowing repetition.
2. Compute $d=M\oplus a\oplus b\oplus c$ using the original masks.
3. Require $c\leq d$ and $d\in S$.
4. Check the full row-sum identity (6), the selected necessary pair
   inequalities, and finally all full-profile equations (2).

Every emitted tuple is valid by its final check. For any valid sorted
tuple, its first three masks are visited, (5) computes its actual fourth
mask, and all subsequent necessary tests pass. It is therefore emitted.
Uniqueness follows because the sorted tuple has a unique first triple.
The product equation itself needs no loop over a fourth mask.

This removes that fourth independent choice from a direct quadruple
enumeration. It does not establish that triple enumeration is faster
than the full-profile pair method: before additional bounds there are
$2^h$ single masks, quadratically many pairs, and cubically many triples.
The bounded experiments compare the methods empirically while preserving
the same set of valid sorted tuples.

## 8. Correspondence with the implementation

The executable is [scripts/search.py](scripts/search.py). Its functions
implement the following proved operations:

| Function or entry point | Mathematical operation |
| --- | --- |
| Imported `sequences` and `paf` | Original-mask sequence bijection and the full half-lag profile in (2). |
| `square_sums` | Global sums in (7) and (8), truncated safely at $4m$. |
| `triangular_probes` | Integer vectors (11), their squared norms, and their autocorrelations. |
| `probe_score` | Exact energy formula (10). |
| `order3_energy` | The integer $\delta_x^2$ in (12), only for $3\mid m$. |
| `Prepared` | Build all complete candidates and apply the sound single-sequence tests. |
| `Prepared.pair_rejection` | Apply (8), the order-three pair bound, and the integer-vector pair bounds. |
| `pair_search` | The complete full-profile pair search of Section 6, with optional product key (13). |
| `product_search` | The forced-fourth-mask search of Section 7; it tests pairs $(a,b)$ and $(c,d)$ and then all of (2). |

The `baseline-mitm` method retains every normalized sequence and every
pair and uses the original full-profile match. The `filtered-mitm` method
adds the proved single and pair tests. The
`filtered-mitm-product-key` method also uses (13). The `product-triples`
method uses the separate coverage argument of Section 7. All four share
the same mathematical output domain for each odd $m$ where they finish.

For the filtered methods, `--filters row`, `--filters row-order3`, and
`--filters all` select, respectively, the row-sum tests alone, those tests
plus the available order-three test, or all the proved filters. Selecting
any of these subsets preserves the same completeness argument and final
solution set.

The coverage proofs hold for arbitrary positive odd $m$. The executable
deliberately accepts only $1\leq m\leq23$, and an accepted input bound
does not claim that every supported order or method was actually run.
Completed runs, resource measurements, and comparisons are recorded
separately from these proofs.

## 9. Scope and attribution

All rejection arguments here concern the odd, normalized, symmetric
circulant Williamson family. Normalization loses no existence case
within that family because independently negating a complete sequence
preserves its autocorrelations. A completed search at a stated finite
core order can establish nonexistence only within that family at that
order. Applying the product theorem at larger $m$ supplies a constraint;
it does not constitute a completed search there, or a Hadamard existence
or nonexistence theorem at arbitrary orders.

For example, the $m=167$ domain still contains $2^{83}$ normalized
symmetric sequences before single-sequence filtering. The product
identity and safe energy bounds do not by themselves make its complete
enumeration feasible or supply an obstruction at Hadamard order $668$.

The odd-order product statement is recorded as Theorem 14 in
Curtis Bright, Ilias Kotsireas, and Vijay Ganesh,
[“Applying Computer Algebra Systems with SAT Solvers to the Williamson
Conjecture,” arXiv:1804.01172v2](https://arxiv.org/html/1804.01172v2#S2.SS5).
That paper attributes the theorem to Williamson (1944); its Sections 2.3
and 2.4 discuss spectral and compression tests. The cited version and
statement were inspected on 2026-10-15. The proofs above supply the exact
criteria used here and distinguish the finite integer probes from a full
Fourier test. Williamson's original article is listed in the first
edition's bibliography.
