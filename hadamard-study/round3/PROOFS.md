# Round 3: structure before complete sequences

The main search uses four-color coordinate patterns, not a pool of complete
single sequences. This document proves that representation, its existing
block-permutation quotient, and its sound prefix exclusions. It also gives
an independent single-sequence branch-and-bound comparator and an additional
quotient obstruction. No priority claim or proof-assistant formalization is
made.

The motivating public disk-covering reports distinguish early necessary
exclusions of entire structural classes or partial branches from expensive
work on complete candidates. Their full geometric proof data are withheld;
no undisclosed exclusion formula is reconstructed here. The reports are
research-process evidence, rather than a proof of the Hadamard reductions
below. See [the source lessons](DISK_LESSONS.md) and
[source records](SOURCES.md).

## 1. Definitions and the product theorem

Fix an odd core order $m=2h+1$. For a nonzero residue $j$ modulo $m$, let
$[j]\in\{1,\ldots,h\}$ be the representative of its pair $\{j,-j\}$.
A normalized symmetric sequence satisfies
$x_0=1$ and $x_j=x_{-j}\in\{-1,1\}$. Write

$$C_x(i,j)=x_{j-i},\qquad
P_x(t)=\sum_{j\bmod m}x_jx_{j+t},\qquad r_x=\sum_jx_j.$$

A Williamson quadruple is an ordered tuple $(a,b,c,d)$ of such sequences
with

$$\sum_x C_x^2=4mI_m,\quad\text{equivalently}\quad
\sum_xP_x(t)=0\quad(1\leq t\leq h).\tag{1}$$

Circulants here are symmetric. Their Gram-entry formula is
$(C_x^2)_{ij}=P_x(i-j)$, while $P_x(0)=m$ and $P_x(-t)=P_x(t)$.
This proves the stated equivalence. The standard Williamson array and its
Hadamard proof are in [the first edition](../PROOFS.md).

We use the odd-order product theorem

$$a_jb_jc_jd_j=-1\quad(j\ne0).\tag{2}$$

For completeness, its short algebraic proof is as follows. In
$\mathbb Z[z]/(z^m-1)$ put $T=\sum_{j=0}^{m-1}z^j$ and
$N_x=\sum_{j:x_j=-1}z^j$. The sequence polynomial is $X_x=T-2N_x$.
Let $P_{ij}=[j=i+1\pmod m]$. Substitution $z\mapsto P$ is injective,
since the first row of $\sum_ju_jP^j$ is its coefficient vector.
Thus (1) gives
$\sum_xX_x^2=4m\cdot1$. Using $T^2=mT$ and $TN_x=|N_x|T$, expand
and divide the integer coefficients by four to obtain

$$\sum_xN_x^2+(m-R)T=m\cdot1,\qquad R=\sum_x|N_x|.$$

Every $|N_x|$ is even, since its positions occur in nonzero opposite
pairs. Reduce modulo two. Cross terms disappear in $N_x^2$, and doubling
permutes residues because $m$ is odd. At a nonzero exponent $2j$, the
number of negative entries among the four sequences is therefore odd.
This proves (2). The detailed version and attribution appear in
[the second-round proofs](../round2/PROOFS.md).

## 2. Orthogonal colors for coupled coordinates

Let $\mathbf1=(1,1,1,1)^{\mathsf T}$ and

$$v_c=\mathbf1-2e_c\quad(c=1,2,3,4),\qquad
V=(v_1\ v_2\ v_3\ v_4)=J_4-2I_4.$$

Then

$$v_c^{\mathsf T}v_d=4[c=d],\qquad
\mathbf1^{\mathsf T}v_c=2,\qquad V^{\mathsf T}V=4I_4.\tag{3}$$

For each nonzero coordinate define its four-entry column
$s_j=(a_j,b_j,c_j,d_j)^{\mathsf T}$. By (2), it is one of the eight
columns having an odd number of negatives. Each has a unique expression

$$s_j=\varepsilon_jv_{\kappa_j},\qquad
\varepsilon_j\in\{-1,1\},\quad\kappa_j\in\{1,2,3,4\}.\tag{4}$$

Indeed, a column with one negative is $+v_c$, where $c$ is its negative
position; a column with three negatives is $-v_c$, where $c$ is its
positive position. The data on $1,\ldots,h$ determine all nonzero
coordinates by reflection. At coordinate zero $s_0=\mathbf1$.

Consequently

$$s_i^{\mathsf T}s_j=4\varepsilon_i\varepsilon_j
[\kappa_i=\kappa_j]\quad(i,j\ne0),\qquad
s_0^{\mathsf T}s_j=2\varepsilon_j.\tag{5}$$

Here and below signs and colors at a nonzero residue mean those at its
representative $[j]$.

## 3. Shift graphs and signs forced by colors

For a fixed nonzero shift $t$, start with the $m$ directed indices $j$
representing edges from $j$ to $j+t$ modulo $m$. Reflection pairs their
indices by

$$j\longleftrightarrow-t-j.$$

The indices $0,-t$ form one pair, incident with coordinate zero. There
is exactly one fixed index, $j=-t/2$; its endpoints are opposite residues.
Remove this pair and this fixed index. The remaining $m-3$ indices form
$h-1$ two-element orbits. Each orbit gives an unordered edge between
$[j]$ and $[j+t]$. Let $E_t$ be this edge list, retaining multiplicities
if an implementation produces them.

**Lemma (exact edge equation).** Equation (1) at shift $t$ is equivalent
to

$$\varepsilon_t+1+
2\sum_{\{u,v\}\in E_t}\varepsilon_u\varepsilon_v
[\kappa_u=\kappa_v]=0.\tag{6}$$

**Proof.** The total autocorrelation is
$\sum_j s_j^{\mathsf T}s_{j+t}$. The two zero-incident terms contribute
$4\varepsilon_t$ by (5). The fixed opposite-endpoint term contributes
$4$, because its two columns are equal. Each remaining reflected pair
contributes $8\varepsilon_u\varepsilon_v[\kappa_u=\kappa_v]$.
Their sum is four times the left side of (6). $\square$

Write $c_t$ for the number of monochromatic edges in $E_t$, with
multiplicity. The sum in (6) has parity $c_t$. Since its required value
is $-(\varepsilon_t+1)/2$, we obtain

$$\boxed{\varepsilon_t=-(-1)^{c_t}.}\tag{7}$$

Thus an assignment of the $h$ colors alone forces all $h$ signs. There
is no remaining independent sign search at a completed coloring.

**Theorem (exact color criterion).** Choose any colors
$\kappa_1,\ldots,\kappa_h$, define all signs by (7), and reconstruct
the columns by (4). The resulting quadruple is Williamson if and only if
every equation (6) holds for $t=1,\ldots,h$.

**Proof.** The reconstruction gives normalized symmetric sign sequences
obeying (2). Equation (6) is exactly the corresponding full
autocorrelation equation, not an approximation to it. Conversely, any
Williamson quadruple has the unique data (4), and (6) forces its signs
to be precisely (7). $\square$

Checking only the parity that gave (7) is insufficient. For example,
at $m=5$, if both coordinates have the same color, (7) forces both signs
positive. The single edge then has weight $+1$, whereas (6) requires
weight $-1$.

### Shape of the shift graphs

Let $g=\gcd(t,m)$ and $\ell=m/g$. The original undirected shift graph
has $g$ cycles of odd length $\ell$. Reflection preserves the cycle
containing zero and exchanges the other cycles in pairs. Folding the
zero cycle produces a path from zero to the fixed opposite edge.
Deleting the zero endpoint and the fixed loop leaves a path on
$(\ell-1)/2$ vertices. Each exchanged pair of cycles folds to a cycle
of length $\ell$. Hence $E_t$ has one such path and $(g-1)/2$ disjoint
cycles. In particular its maximum degree is two.

These actual odd cyclic quotient graphs are simple: their cycles have length
at least three, and the only folded loop was removed. The list-based formulas
and code retain integer multiplicity if supplied a more general edge list;
synthetic repeated-edge regressions test that arithmetic. Composite lengths
introduce the disjoint cycles, not parallel edges.

When $g=1$ it is a path; it need not be a path for composite $m$.
For example, at $m=9,t=3$, vertices $1,2,4$ form a triangle and vertex
$3$ is isolated. The proofs of (6) and (7) do not require a path.

## 4. Canonical colors count the existing block multisets

A permutation $\pi$ of the four block rows sends $v_c$ to $v_{\pi(c)}$,
since its permutation matrix fixes $\mathbf1$. Thus it permutes color
names and leaves every $\varepsilon_j$ unchanged. Conversely, applying
one permutation of the color names has exactly this effect on the four
sequence rows. The representation (4) is unique, so these correspondences
work in both directions.

Canonical color strings are **restricted-growth strings**: for $h>0$,

$$\kappa_1=1,\qquad
1\leq\kappa_j\leq\min(4,1+\max_{i<j}\kappa_i).\tag{8}$$

Every coloring can be put into this form by naming its colors in order
of first appearance. That order is unique, so every color-name orbit
has exactly one string (8). Unused colors cause no ambiguity: their
permutations do not change the string, and their corresponding sequence
rows are identical to one another. Repeated rows are therefore covered.
For $h=0$, use the unique empty coloring.

It follows that accepted canonical colorings are in bijection with the
same multisets of four normalized sequences previously represented by
sorted original masks. This removes exactly the already allowed block
permutations. It introduces no quotient by coordinate shifts, index
multipliers, or Hadamard equivalence, and its counts are not counts of
inequivalent Hadamard matrices.

The same bijection holds for any fixed permutation $\pi$ of the vertex
assignment order. Apply (8) to
$(\kappa_{\pi(1)},\ldots,\kappa_{\pi(h)})$: every used color again has
a unique first appearance, so naming colors in that order gives exactly
one representative of each color-name orbit. Original coordinate
positions remain attached to the vertices and to the reconstructed mask
bits. The ordering changes which variable is assigned first; it does
not change the shift graphs or identify different coordinate arrays.

## 5. Safe sign forcing at a color prefix

At a prefix, some coordinate colors are assigned and the others are
unknown. The assigned vertices may be any initial segment of a fixed
assignment order; they need not be $1,\ldots,k$ in natural coordinate
order. For the purpose of the parity $c_t$, first remove even edge
multiplicities from $E_t$. Consider the following sufficient condition:
every unknown vertex is either isolated or has exactly two assigned
neighbors of the same color.

Under this condition there is no edge between two unknown vertices.
An isolated vertex contributes nothing. If an unknown vertex has two
assigned neighbors of color $c$, its incident contribution is
$[\kappa=c]+[\kappa=c]=0$ modulo two, independently of its color.
Hence all unknown-color contributions cancel, and the parity is exactly
the parity of the monochromatic assigned-assigned edges. Equation (7)
then forces $\varepsilon_t$ before the coloring is complete.

If this sufficient condition fails, retaining both signs is safe. No
necessity or maximality is claimed for this rule. In particular, failure
to force a sign is not a proof that both signs have genuine completions.

## 6. Coupled row-square targets and a prefix obstruction

Define the signed color counts

$$z_c=\sum_{j:\kappa_j=c}\varepsilon_j,\qquad S=\sum_cz_c.$$

Using (4), the four sequence row sums satisfy

$$r_i=1+2S-4z_i.$$

Expanding their squared sum gives

$$\sum_{i=1}^4r_i^2=4+8S+16\sum_cz_c^2.$$

Every Williamson quadruple has row-square sum $4m=4+8h$, by summing
(1) over every shift. Therefore its signed color counts lie in

$$Z_h=\left\{z\in\mathbb Z^4:
\sum_{c=1}^4(2z_c^2+z_c)=h\right\}.\tag{9}$$

This set is finite: each integer term $2z^2+z$ is nonnegative and
grows quadratically. Each coordinate is $O(\sqrt h)$, so direct
four-coordinate target enumeration is $O(h^2)$, before any sequence
enumeration.

### Exact row feasibility under the prefix relaxation

Suppose $k$ coordinate colors are assigned and $u=h-k$ remain. Among the
assigned positions of color $c$, let $T_c$ be the sum of the forced signs
and $n_c$ the number whose signs are still allowed to be either value.
The attainable signed counts for this relaxation are the arithmetic
progressions

$$I_c=\{T_c-n_c,T_c-n_c+2,\ldots,T_c+n_c\}.\tag{10}$$

Let $\operatorname{dist}(q,I)=\min_{p\in I}|q-p|$; the parity gaps in
$I$ matter. Define

$$D=\min_{U\in Z_h}\sum_{c=1}^4\operatorname{dist}(U_c,I_c).\tag{11}$$

**Proposition.** If $D>u$, the prefix has no Williamson completion.
Moreover, $D\leq u$ is exact feasibility for the relaxation that treats
the unforced assigned signs independently and lets each future position
contribute an arbitrary $\pm e_c$.

**Proof.** Each actual completion supplies assigned signed counts
$p_c\in I_c$. Each of its $u$ remaining positions changes the vector by
one $\pm e_c$. Its final target $U$ must therefore satisfy
$\|U-p\|_1\leq u$, implying (11).

Conversely, choose a minimizing target and a closest $p_c\in I_c$.
The vector difference can be traversed in $D$ unit coordinate steps.
Every $p_c$ has the parity of the number of assigned positions of color
$c$, so $\sum_cp_c\equiv k\pmod2$. Equation (9) implies
$\sum_cU_c\equiv h\pmod2$. Thus $D\equiv h-k=u\pmod2$.
If $D\leq u$, insert $(u-D)/2$ cancelling pairs of steps to obtain
exactly $u$ future positions. This realizes the relaxed row-square
condition. It does not enforce their actual color-parity sign relations
or their autocorrelations. $\square$

### A whole partial branch missed by independent row tests

Take $m=11$, $h=5$, and assign three coordinate states
$+v_1,+v_1,+v_4$. Their current signed counts are $(2,0,0,1)$, whose
coordinate sum is $3$; only two states remain. All targets in $Z_5$ are
permutations of $(1,-1,-1,0)$, whose coordinate sum is $-1$.
Indeed the possible individual costs at most five in (9) are $0,1,3$,
and their only four-term decomposition of five is $3+1+1+0$.
Two unit steps cannot change the sum by four, so the coupled criterion
rejects this branch.

Independent row feasibility misses this obstruction. The assigned
partial row sums are $(-1,7,7,3)$. Allowing each unknown row sign
independently permits final sums $(-5,3,3,-1)$, whose squares total
$44=4m$. The two all-negative columns realizing those changes each
have product $+1$, so they are forbidden coupled states. This is why
four separate row-sum ranges lose structural information.

## 7. Safe lag capacity at a prefix

For an edge $\{u,v\}\in E_t$, its true term is
$\varepsilon_u\varepsilon_v[\kappa_u=\kappa_v]$. Enclose it in a
finite integer set as follows:

- Assigned different colors: $\{0\}$.
- Assigned equal colors with both signs forced: the singleton containing
  their sign product.
- Assigned equal colors with an unforced sign: $\{-1,1\}$.
- An unknown endpoint color: $\{-1,0,1\}$.

Take the Minkowski sum of these sets over the edge list, including its
multiplicities. The target set is
$\{-(1+\varepsilon_t)/2\}$ if that sign is forced, and $\{-1,0\}$
otherwise. If the two sets are disjoint, reject the prefix.

**Soundness.** Every actual completion chooses one allowed value for
each edge and one allowed target. Their sum must be the same by (6).
Disjoint sets therefore exclude every completion. The relaxation permits
different edges to choose inconsistent values of shared unknown colors
or signs, so an intersection is only a necessary condition.

The implementation evaluates this sumset directly by its radius and
parity. If the singleton terms sum to $F$, there are $b$ copies of
$\{-1,1\}$ and $q$ copies of $\{-1,0,1\}$, then the sumset is every
integer between $F-b-q$ and $F+b+q$ when $q>0$. When $q=0$, it consists
of that range with the parity $F+b$. This follows by adding the two
elementary integer progressions, and covers $b=q=0$ as well.

A simple illustration is $m=5$ with the first coordinate state fixed as
$+v_A$. Each shift graph is the same edge $\{1,2\}$. The first shift's
equation is individually satisfiable by setting the second state to
$-v_A$. The second shift's equation is individually satisfiable by
setting it to $-v_B$ with $B\ne A$. These requirements cannot both hold.
Thus even separate exact feasibility checks for each shift need not
imply a common completion. Domain propagation or branching must couple
the constraints; the independent term sets above make no stronger claim.

Because each $E_t$ consists of a path and cycles, one could compute
stronger per-shift feasible sets by a finite-state dynamic program,
conditioning on a starting label for a cycle. That strengthening is not
needed for the soundness of the implemented independent-term enclosure.

### Even the first combined prefix filters have false positives

At $m=11$, the canonical color prefix $1112$ has one coordinate left.
The parity rule forces $\varepsilon_3=\varepsilon_4=+1$ and leaves the
other signs free. Its sets (10) are
$I_1=\{-1,1,3\}$, $I_2=\{1\}$, $I_3=I_4=\{0\}$.
The target $(-1,1,-1,0)\in Z_5$ has distance one, so the row test passes.
The first four lag enclosures are the full range $[-3,3]$ and the fifth
is $[-2,2]$; all intersect their allowed targets.

There is nevertheless no extension. Choosing last color one or two
uses too few colors for a $Z_5$ target, which must have three nonzero
coordinates. Choosing new color three gives $11123$, whose forced signs
are $(-,+,+,+,+)$. Its signed color counts are $(1,1,1,0)$, with cost
$9$ in (9), rather than $h=5$. The necessary prefix filters therefore
reduce search without replacing it.

## 8. Completeness of the canonical prefix search

The search visits every restricted-growth color string by extending each
prefix with exactly the choices allowed in (8), along its fixed vertex
assignment order. All graph tests and phase substitutions retain the
original vertex positions. It applies only the
necessary prefix tests proved above, or the strengthened necessary tests
of Section 9. Hence the canonical coloring of
any Williamson multiset is never rejected: its actual signs agree with
every forced sign, its actual row counts witness (11), and its actual
edge terms witness every lag capacity check.

At a complete coloring, all monochromatic-edge parities are known, so
(7) fixes every sign. Every edge term is then a singleton, and checking
all exact equations (6) is equivalent to (1). The accepted leaves are
therefore exactly the canonical Williamson colorings. The bijection in
Section 4 proves that each sorted normalized sequence multiset is
reported once. Actual sequence masks need be reconstructed only for
accepted leaves; no complete single-sequence pool or pair table is
required for this coverage argument.

The same proof covers $m=1$: the color string, sign list, and lag list
are empty, the four sequences are all $(1)$, and there is one multiset.
The proof is parameterized by odd $m$; it does not assert that a program
has completed any unreported order.

The initial implementation is [scripts/structure.py](scripts/structure.py).
Its `leaf` mode checks only completed canonical colorings; `row`, `lag`,
and `all` enable the respective prefix tests. The `row_targets`,
`sign_domains`, `row_prefix_possible`, and `lag_prefix_possible` functions
implement Sections 5–7. The recurrence
$R(r,k)=kR(r-1,k)+[k<4]R(r-1,k+1)$, with $R(0,k)=1$, counts canonical
extensions of a prefix using $k$ colors. Charging a pruned prefix all
$R(r,k)$ of its extensions gives disjoint subtree accounting, rather
than a sample of skipped leaves.

## 9. Stronger prefix reasoning through shared Boolean phases

The independent sign domains in Sections 5–7 discard relations between
signs that have not individually been forced. Those relations can be
retained exactly before taking a new relaxation.

Encode color $\kappa_i-1\in\{0,1,2,3\}$ by two bits $a_i,b_i$.
All polynomial arithmetic in the next display is over $\mathbb F_2$,
with Boolean variables, so repeated monomials cancel. The indicator of
equal colors has algebraic normal form

$$\begin{aligned}
\delta_{uv}
&=(1+a_u+a_v)(1+b_u+b_v)\\
&=1+a_u+a_v+b_u+b_v+a_ub_u+a_ub_v+a_vb_u+a_vb_v.
\end{aligned}$$

It follows from (7) that

$$n_t=1+\sum_{\{u,v\}\in E_t}\delta_{uv},\qquad
\varepsilon_t=(-1)^{n_t}.$$

Each $n_t$ is a Boolean polynomial of degree at most two. Substitute the
assigned color bits at a prefix, collect its squarefree monomials, and
write the result uniquely as $n_i=\alpha_i+p_i$, where $\alpha_i$ is
constant and $p_i$ has zero constant term. Define
$\eta_i=(-1)^{\alpha_i}$ and $\xi_p=(-1)^{p}$, with $\xi_0=1$.
Then

$$\varepsilon_i=\eta_i\xi_{p_i},\qquad
\varepsilon_u\varepsilon_v=
\eta_u\eta_v\xi_{p_u+p_v}.$$

Thus $p_u=p_v$ forces their sign product even if neither individual
sign is known. More generally, equal residual polynomials identify a
shared unknown phase, with a known constant sign factor.

These are identities on all assignments of the remaining color bits.
Restricting to canonical color completions cannot invalidate them.
Distinct residual polynomials need not be independent: for example,
$\xi_{p+q}=\xi_p\xi_q$. The necessary tests below deliberately relax
such remaining relations, so passing them is not a feasibility proof.

### Grouped row-count feasibility

Among the positions whose colors are assigned, define integer vectors

$$G_p=\sum_{i\text{ assigned}:p_i=p}\eta_i e_{\kappa_i}.$$

Their actual signed color-count vector is exactly
$G_0+\sum_{p\ne0}\xi_pG_p$. Enclose it in the finite set

$$\mathcal A=\left\{G_0+\sum_{p\ne0}\sigma_pG_p:
\sigma_p\in\{-1,1\}\right\}.$$

Here equal residual phases remain shared; only distinct phases are
allowed to vary independently. If $u$ coordinates remain uncolored,
the grouped row rejection rule is

$$\min_{U\in Z_h,\ A\in\mathcal A}\|U-A\|_1>u.$$

**Soundness.** Every actual prefix count vector belongs to $\mathcal A$,
and each future coordinate still changes it by one $\pm e_c$.
The distance of an actual target is therefore at most $u$.
The unit-step parity remains automatic: changing any $\sigma_p$ changes
$A$ by an even vector, so $\sum_cA_c\equiv k\pmod2$ for $k$ assigned
positions. This is the same distance proof as Section 6, with a tighter
set of assigned count vectors. It is still a relaxation of the full
color and phase problem.

### Grouped lag enclosure with unknown-color edges

In (6), omit edges of assigned different colors. For assigned equal
colors, write their contribution as
$2\eta_u\eta_v\xi_{p_u+p_v}$. Also write
$\varepsilon_t=\eta_t\xi_{p_t}$. Collect coefficients of every equal
residual phase over the **integers**, including the initial constant one.
All zero-phase terms go into the constant.

For an edge with unknown endpoint color, a safe remaining contribution
set is $\{-2,0,2\}$. If $p_u+p_v=0$, its sign product is the known
$\eta_u\eta_v$, and the tighter set
$\{0,2\eta_u\eta_v\}$ is valid. Take the Minkowski sum of these sets
and the grouped terms $\{-c_p,c_p\}$, translated by the collected
constant. If zero is absent, reject.

Every completion realizes one element of this sumset, since the grouping
is an exact identity and each unknown-edge set contains its actual term.
The rejection is consequently sound. Opposite coefficients on a shared
phase cancel before relaxing it; treating their signs independently
would lose that information.

### An alternative exact compilation of every lag term

There is also a phase identity that expands the unknown-color indicators.
Put $A_{uv}=a_u+a_v$ and $B_{uv}=b_u+b_v$ over $\mathbb F_2$.
As a real-valued identity on Boolean inputs,

$$4\delta_{uv}=(1+(-1)^{A_{uv}})(1+(-1)^{B_{uv}}).$$

Multiply (6) by two and use this identity. The exact doubled lag equation
becomes

$$2+2(-1)^{n_t}+
\sum_{\{u,v\}\in E_t}
\sum_{\lambda\text{ in }(0,A_{uv},B_{uv},A_{uv}+B_{uv})}
(-1)^{n_u+n_v+\lambda}=0.$$

The inner sum has four entries with multiplicity, even when some phases
coincide or become zero after substitution. In particular, assigned
equal colors give four copies, and assigned different colors cancel.
All exponents still have degree at most two. After prefix substitution,
absorb each constant phase into its integer coefficient, group identical
nonconstant residual polynomials, and move the zero phase into $K$.
The resulting expression $K+\sum_pc_p\xi_p$ is an exact functional
identity. Replacing distinct $\xi_p$ by independent signs yields another
safe sumset test for whether zero is possible.

The exponents are computed over $\mathbb F_2$; the collected $K,c_p$ and
the rejection sumset are computed over $\mathbb Z$. Reducing those
coefficients modulo two, or cancelling a factor that does not divide
all of them and $K$, is not justified. This compilation and the mixed
unknown-edge enclosure are alternative relaxations: neither is asserted
to dominate the other, because independently relaxing the four expanded
phases can lose relations inside one edge. Their usefulness must be
measured. The exact leaf equations remain (6).

The implementation is [scripts/phases.py](scripts/phases.py), called by
[scripts/phase_search.py](scripts/phase_search.py). `PhaseAlgebra` performs
the exact polynomial substitutions. `grouped_row_possible` represents
$\mathcal A$ by factoring single-coordinate group contributions into
scalar sumsets and enumerating the remaining vector offsets; this is an
exact factorization of the independent-phase relaxation.
`grouped_lag_possible` uses the mixed enclosure in `relations` mode or
the doubled compilation in `expanded` mode. The `row` mode omits these
lag tests. All retain the same exact complete-color leaf acceptance
criterion and canonical output domain.

## 10. Independent alternative: single-sequence partial assignments

The experimental comparator in
[scripts/partial_singles.py](scripts/partial_singles.py) uses a different
branch space. It assigns the $h$ independent signs of one normalized
symmetric sequence before collecting complete surviving sequences.

If $a$ negative signs are already assigned and $u$ are unknown, its
attainable row sums are exactly

$$\{m-4k:a\leq k\leq a+u\}.\tag{12}$$

Let $W_m=\{t^2:1\leq t\leq m,\ t\text{ odd}\}$. A necessary single-member
condition is $4m-r_x^2\in W_m+W_m+W_m$, with repetition allowed.
If none of (12) satisfies this condition, every completion of the node
is excluded. Tracking which counts remain feasible is safe cardinality
propagation, before the sequence is complete.

### Cancellation-safe energy bounds

For an integer test vector $v$, let $P$ be the cyclic shift matrix.
At a partial assignment write

$$C_x^{\mathsf T}v=A+\sum_{i\in U}y_iB_i,\qquad
B_i=((P^i)^{\mathsf T}+(P^{-i})^{\mathsf T})v,\quad y_i\in\{-1,1\},$$

where $A$ contains the fixed position-zero term and the assigned
symmetric pairs. For each component put $R_j=\sum_{i\in U}|(B_i)_j|$.
Every completion satisfies

$$\|C_x^{\mathsf T}v\|^2\geq
L_v:=\sum_j\max(0,|A_j|-R_j)^2.\tag{13}$$

Indeed, the unknown sum in component $j$ lies between $-R_j$ and $R_j$,
so its distance after adding $A_j$ from zero is at least the displayed
quantity. Summing the component bounds proves (13). Dependence among
components can make this bound weak, but cannot make it unsound.

For every member of a Williamson quadruple,
$\|C_x^{\mathsf T}v\|^2\leq4m\|v\|^2$, because the four energies sum to
that value and are nonnegative. Hence $L_v>4m\|v\|^2$ safely excludes a
partial single sequence. The comparator uses integer vectors and exact
integer sums. At leaves it checks the same complete-sequence row-sum,
order-three, and triangular-probe conditions as the second round.
This comparator produces eligible single sequences, not Williamson
quadruples; complete-sequence eligibility itself is a necessary filter.

### Why unknown entries cannot be filled with zero for rejection

At $m=9$, take $v=\mathbf1$. Assign the position-zero sign and the pairs
$\pm2,\pm3,\pm4$ positive, leaving $\pm1$ unknown. Filling the two
unknown entries with zero gives row sum seven and energy
$9\cdot7^2=441>4m\|v\|^2=324$. But completing that pair negatively gives
the normalized mask $1$, row sum five, and energy $225$.
This sequence is a member of the Williamson multiset $(1,9,9,14)$.
Its colors are $(4,4,4,1)$ and its signs are $(-,+,+,-)$; the four
weighted edge sums in (6) are $(0,-1,-1,0)$, verifying that assertion.
Thus the zero-filled partial energy could reject an actual member.
Bound (13) explicitly allows cancellation and does not make this error.

### A stronger optional exact certificate

For any integer vector $w$, completing a square gives

$$\|A+\sum_i y_iB_i\|^2\geq
2w^{\mathsf T}A-\|w\|^2+2\sum_i y_i(w^{\mathsf T}B_i).\tag{14}$$

If exactly $q$ unknown signs must be negative, put
$c_i=w^{\mathsf T}B_i$. The exact minimum of its final linear term
before multiplication by two is
$\sum_ic_i-2\sum_{i\text{ among the }q\text{ largest}}c_i$.
Take the minimum over every feasible $q$ from (12) for a safe lower
bound in (14). This accounts for cardinality as well as cancellation
without generating full sign assignments. It is a proved additional
certificate, not a claim that the comparator implements or benefits
from its optimization.

## 11. Additional quotient obstruction before full sequences

Let $d\mid m$ be odd and $k=m/d$. Compress a sequence into
$y_r=\sum_{j\equiv r\pmod d}x_j$. The ring homomorphism sending the
cyclic generator of order $m$ to one of order $d$ sends (1) to

$$\sum_x C_y^2=4mI_d.\tag{15}$$

It preserves the coefficient $4m$; it does not replace it by $4d$.
The compression is symmetric, $y_r=y_{-r}$.

This necessary condition also has a coupled prefix form. Group the
$h$ nonzero opposite-coordinate pairs by their residue pair modulo
$d$. Group zero contains $(k-1)/2$ pairs, and each other group
$r=1,\ldots,(d-1)/2$ contains $k$ pairs. Write $z_r\in\mathbb Z^4$
for their signed color counts. The four-entry compressed columns are

$$Y_0=\mathbf1+2Vz_0,\qquad Y_r=Y_{-r}=Vz_r\quad(r>0).$$

The diagonal part of (15), using (3), is exactly

$$\underbrace{\sum_c(z_0)_c+2\|z_0\|^2}_{\phi_0(z_0)}
+\sum_{r=1}^{(d-1)/2}\underbrace{\|z_r\|^2}_{\phi_r(z_r)}=h.\tag{16}$$

For a partial state assignment, suppose group $r$ has current counts
$z_r^0$ and $u_r$ positions left. Its exact unrestricted future count
set consists of the integer vectors with

$$\|z_r-z_r^0\|_1\leq u_r,\qquad
\|z_r-z_r^0\|_1\equiv u_r\pmod2.$$

This is the same unit-step argument as Section 6. Compute the attainable
integer cost set for each $\phi_r$ on that domain. If $h$ is absent
from their Minkowski sum, reject the entire partial branch. This is
exact feasibility for the quotient-diagonal relaxation, not for (15)
or for the original Williamson equations. The costs are nonnegative,
so discarding values above $h$ is safe. This structural criterion is
derived here as an additional option; it is not part of the main
canonical-color benchmark unless explicitly reported as implemented.

### Every proper quotient can pass while the full problem fails

At $m=9$, the original normalized masks $(2,10,10,13)$ have row sums
$(5,1,1,-3)$ and XOR $15$. They therefore pass the product constraint
and the row-square identity. Their length-three compressed sequences
are, respectively,

$$(3,1,1),\quad(3,-1,-1),\quad(3,-1,-1),\quad(-1,-1,-1).$$

Their total compressed autocorrelation is $(36,0,0)$, so they satisfy
all of (15) at $d=3$; the row-square identity is (15) at $d=1$.
These are all proper cyclic quotient lengths of nine. Nevertheless
their original total autocorrelation at shift one is $-8$.
For example, their nonzero columns are
$+v_4,-v_4,+v_4,-v_1$; $E_1$ is the path $1$--$2$--$3$--$4$,
whose weighted monochromatic sum is $-2$. Equation (6) has left side
$1+1+2(-2)=-2$, giving total autocorrelation $4(-2)=-8$.
Proper quotient acceptance therefore does not establish a lift.

## 12. Traversal, memoization, and a bounded diagnostic

The implemented `collisions` order chooses a fixed permutation before visiting
any coloring. At each choice it restricts each initial quadratic phase part to
the still unassigned vertices, counts equal quadratic signatures (including
the zero phase), and prefers the most collisions. Ties prefer fewer remaining
quadratic monomials and then the smallest original coordinate. Section 4's
fixed-order RGS argument applies. This score predicts possible relations only;
linear terms can prevent equality of the full residual phases. Every actual
cancellation still requires equality of the full ANF residual, with its
constant factor retained. Ordering time is included in preparation.

The two decision caches identify only proved equivalent feasibility problems.
For a lag sum, independent signs make coefficient order and coefficient sign
irrelevant, so the key retains the integer constant, sorted absolute nonzero
coefficients, and the sorted finite extra domains. For a row sum, a cross-color
vector may be negated because its phase ranges over both signs; its name may
be discarded after grouping. The key retains the fixed vector, sorted scalar
weights per color, sorted cross vectors up to this sign, the remaining count,
and the target set. It does not identify different full polynomial states.
Each cache has at most 4096 entries and is cleared before each search.

There is a simple obstruction to making a residual phase constant very early.
For two initial phases (including the zero phase), form their ANF difference.
For every quadratic monomial, record the physical vertices containing its two
bits. This gives an edge, or a loop when both bits belong to one vertex.
If neither endpoint has been assigned, that quadratic monomial survives
substitution unchanged. Substituting assigned bits into another term cannot
create or cancel a quadratic term on two still free bits. Consequently, an
assigned set that makes the difference constant must cover every such edge.
The converse fails: surviving linear terms can still prevent constancy.

The independently checked [bounded diagnostic](evidence/quadratic-obstruction.json)
enumerates every assigned subset for each pair. At core 21, 40 phase pairs
need at least six assigned vertices to remove the quadratic terms, and 15 need
seven. At core 23 the corresponding counts are 11 and 55. These are statements
about constant-phase detection under the free four-color completion relaxation.
They do not bound arbitrary exclusion rules or even rules that exploit the
smaller canonical RGS completion domain. In particular, a prefix can fail a
sum constraint without any individual phase becoming constant.

Even the grouped row and expanded lag tests together are insufficient. At
core 11, the color prefix `(0,0,0,1)` passes both. Assigning any of the four
colors to its last coordinate, reconstructing the signs, and checking (6)
gives no solution. Thus independently relaxed phase sums can all be feasible
without one common completion realizing them.

## 13. What the structural reductions establish

The canonical-color representation reduces the full search domain before
individual sequence generation. Its prefix rules reject complete
families of remaining color assignments, with written proofs of soundness.
They remain necessary relaxations until the exact leaf equations are
checked. The alternative single-sequence branch space tests whether cheap
partial row and cancellation-safe energy bounds are useful earlier than
the complete-sequence filters; its outcome is an empirical comparison,
not an assumption in the color-search proof.

All completeness claims concern the stated odd symmetric circulant
Williamson family and the already used block multiset quotient. They do
not imply existence or nonexistence of arbitrary Hadamard matrices, and
no unreported large-order computation follows from a parameterized proof.
In particular, none of the reductions alone resolves core order $167$
or a general existence theorem for multiples of four.
