# A concrete destination: Hadamard and Williamson foundations

## Scope and the exact question

The confirmed existing direction is the paused Hadamard/Williamson project in
this repository. Its general existence question asks whether, for every positive
integer $k$, there is a matrix

$$H\in\{-1,1\}^{4k\times4k},\qquad HH^{\mathsf T}=4kI_{4k}.$$

The prior work at commit
`2834fea31fb4ca7203531ca220e55a2fb7640119` records three rounds of
bounded research in a restricted family. Its proofs and limitations are read
here as the starting point. No prior benchmark is presented as a fresh run,
and no historical claim about the smallest missing order or the worldwide
current status is imported without a separate literature audit. This chapter
does not restart the computational search.

The structural chain actually needed is

$$\text{Gram matrices}\longrightarrow\text{tensor constructions},
\qquad
\text{finite fields}\longrightarrow\text{quadratic characters},
$$

$$\text{cyclic group algebras}\longrightarrow\text{Fourier decomposition}
\longrightarrow\text{correlation equations and lifting constraints}.
$$

It makes direct use of Xi II's metric and tensor material and Xi III's groups,
representations, and finite fields. General Ext theory, schemes, and differential
topology have no established role in this chain.

## Gram matrices and the order restriction

The identity $HH^{\mathsf T}=nI$ says precisely that the rows are mutually
orthogonal in the usual positive real inner product and have squared length
$n$. It also gives $H^{-1}=n^{-1}H^{\mathsf T}$ and
$|\det H|=n^{n/2}$, attaining the determinant bound proved in the forms
chapter. Orthogonality alone does not enforce sign entries; both conditions
are essential.

Multiplying rows or columns by signs and permuting them preserves the
Hadamard condition. Normalize the first row to all $+1$. A second row must
have equally many signs, so $n$ is even. When $n>2$, permute its positive
entries into the first half and let a third row have $a$ positives in the
first half and $b$ in the second. Its products with the first two rows give

$$2(a+b)=n,\qquad2(a-b)=0.$$

Hence $n=4a$. This proves the necessary orders $1,2$, or a multiple of
$4$. It supplies no construction at each admissible order. The proof is over
the integers or reals; reducing the equation modulo $2$ would collapse all
signs and lose the argument.

## Tensor closure and what it leaves unsolved

If $H$ and $K$ have orders $a,b$, functoriality of the tensor product and
transpose gives

$$(H\otimes K)(H\otimes K)^{\mathsf T}
=(HH^{\mathsf T})\otimes(KK^{\mathsf T})=abI_{ab}.$$

Its entries remain signs. Tensoring with
$S=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ gives
$\begin{pmatrix}H&H\\H&-H\end{pmatrix}$ and yields all powers-of-two
orders from $[1]$. This is a genuine infinite construction theorem. It does
not produce all multiples of four without additional seeds or constructions.
The universal tensor identities explain why the construction transports
orthogonality, while the sign-entry requirement explains why arbitrary
orthogonal matrices are not sufficient seeds.

## Finite fields and a character identity proved by counting

Let $\mathbb F_q$ be a finite field of odd order. Its nonzero squares form
an index-two subgroup: the squaring map has exactly two preimages $x,-x$
for each nonzero square. Define the quadratic character
$\chi:\mathbb F_q\to\{0,\pm1\}$ with $\chi(0)=0$, $+1$ on
nonzero squares, and $-1$ on nonsquares. The quotient-group description
proves multiplicativity, and equal coset sizes prove $\sum_x\chi(x)=0$.

The multiplicative group of a finite field is cyclic. One short proof lets
$e$ be the least common multiple of its element orders. In a finite abelian
group, combine elements of maximal prime-power orders to obtain an element of
order $e$. Every nonzero field element is a root of $X^e-1$, so there
are at most $e$ of them, whereas Lagrange gives $e\le q-1$. Thus
$e=q-1$. It follows that
$\chi(-1)=(-1)^{(q-1)/2}$.

For $a\ne0$, the crucial correlation identity is

$$\sum_x\chi(x)\chi(x+a)=-1.$$

Count pairs $(x,y)$ with $y^2=x(x+a)$. For fixed $x$, their number
is $1+\chi(x(x+a))$, so the total is $q$ plus the displayed sum.
Scale $x=az$, $y=aw$ and rewrite as

$$(2z+1-2w)(2z+1+2w)=1.$$

Since $2$ is invertible, each nonzero first factor determines a unique
second factor and a unique $(z,w)$. There are $q-1$ pairs, proving the
sum. For $a=0$ the corresponding sum is $q-1$.
This argument uses a finite field of odd order, not the special fact that
its elements are residue classes modulo a prime.

## Paley constructions with explicit signs

Index $Q$ by $x,y\in\mathbb F_q$ and put $Q_{xy}=\chi(y-x)$.
The character identities give

$$Q\mathbf1=0,\qquad QQ^{\mathsf T}=qI-J,
\qquad Q^{\mathsf T}=\chi(-1)Q.$$

If $q\equiv3\pmod4$, set

$$H=\begin{pmatrix}1&\mathbf1^{\mathsf T}\\
\mathbf1&Q-I\end{pmatrix}.$$

Its entries are signs, its top row is orthogonal to every lower row because
$1+(Q-I)\mathbf1=0$, and its lower Gram block is

$$J+(Q-I)(Q^{\mathsf T}-I)
=J+qI-J-Q-Q^{\mathsf T}+I=(q+1)I.$$

Therefore $HH^{\mathsf T}=(q+1)I$. The prior study used the equivalent
sign convention with lower first column $-\mathbf1$ and core $Q+I$.
The conventions have been derived separately here so a copied sign does not
silently spoil orthogonality.

For $q\equiv1\pmod4$, define the symmetric conference matrix

$$C=\begin{pmatrix}0&\mathbf1^{\mathsf T}\\\mathbf1&Q\end{pmatrix}.$$

It has zero diagonal, off-diagonal signs, and $C^2=qI$.
The block matrix

$$\mathcal H=\begin{pmatrix}C+I&C-I\\C-I&-C-I\end{pmatrix}$$

has only sign entries. The diagonal Gram block is
$(C+I)^2+(C-I)^2=2(q+1)I$ and the off-diagonal block vanishes by
commutation. It is Hadamard of order $2(q+1)$.

These proofs add a short prime-power and conference-matrix development to the
prior study's prime, $q\equiv3\pmod4$ proof. They are classical
constructions, not new results or claims that the earlier scripts implemented
them. Finite fields of every prime-power order exist (Xi III Theorems
5.40–5.45, printed pp. 260–261, PDF pp. 266–267); these pages and their
proofs were inspected visually. Small exact instances are checked separately
in this deliverable, without resuming an enumeration campaign.

## Circulants as an integral group algebra

Fix $m\ge1$ and let $P$ be the cyclic shift with
$P_{ij}=1$ when $j=i+1\pmod m$. The map

$$\mathbb Z[z]/(z^m-1)\longrightarrow M_m(\mathbb Z),
\qquad f\longmapsto f(P)$$

is injective: the first row of $\sum_{j=0}^{m-1}a_jP^j$ is its
coefficient vector. Its image is the circulant algebra, so circulants commute.
Define $f^\iota(z)=f(z^{-1})$. Transpose corresponds to this involution.
For a real sequence $x$ with polynomial $X(z)=\sum_jx_jz^j$,
the coefficient of $z^s$ in $XX^\iota$ is

$$\operatorname{PAF}_x(s)=\sum_jx_jx_{j+s}.$$

This follows by collecting terms with exponent difference $s$; autocorrelation
is even in $s$. It is convolution with the reversed sequence, so the group
algebra retains the integral coefficients needed for exact verification.

If $x_j=x_{-j}$, then $X=X^\iota$ and the circulant is symmetric.
Four such sign sequences form a Williamson quadruple when

$$AA^{\mathsf T}+BB^{\mathsf T}+CC^{\mathsf T}+DD^{\mathsf T}
=4mI_m,$$

equivalently their four autocorrelations sum to zero at every nonzero shift.
Symmetry permits replacing the four Gram matrices by $A^2,B^2,C^2,D^2$.
Commutation and symmetry then make

$$W=\begin{pmatrix}
A&B&C&D\\-B&A&-D&C\\-C&D&A&-B\\-D&-C&B&A
\end{pmatrix}$$

Hadamard of order $4m$. Multiplying blocks, every diagonal Gram block is
the sum of the four squares, while an off-diagonal block has terms such as
$-AB+BA-CD+DC=0$. Transpose and commutation hypotheses are indispensable
in that cancellation. Existence in the Williamson family is sufficient for
a Hadamard matrix of that order; it is not a necessary characterization of
all Hadamard matrices.

## Fourier characters are Chinese remainder coordinates

Let $k$ have characteristic not dividing $m$ and contain a primitive
$m$th root $\zeta$. The roots of $z^m-1$ are distinct, so

$$k[z]/(z^m-1)\xrightarrow{\ \sim\ }k^m,
\qquad f\longmapsto(f(1),f(\zeta),\ldots,f(\zeta^{m-1}))$$

is a Chinese remainder isomorphism. Its inverse is the finite Fourier formula

$$a_j=\frac1m\sum_{r=0}^{m-1}f(\zeta^r)\zeta^{-rj}.$$

To verify it, the geometric sum $\sum_r\zeta^{r\ell}$ equals $m$
when $m\mid\ell$ and $0$ otherwise. In the regular representation,
the vector $(1,\zeta^r,\ldots,\zeta^{(m-1)r})$ is an eigenvector of
$P$ with eigenvalue $\zeta^r$. Thus all circulants diagonalize in the
same basis; this is the group representation decomposition into characters.

Over $\mathbb C$, divide these vectors by $\sqrt m$ to get a unitary
basis. A real symmetric circulant then has real eigenvalues, since
$X(\zeta^{-r})=X(\zeta^r)=\overline{X(\zeta^r)}$.
The correlation identity becomes

$$\sum_{X\in\{A,B,C,D\}}|X(\zeta^r)|^2=4m\qquad(0\le r<m).$$

The frequency-zero equation is the row-sum identity
$r_a^2+r_b^2+r_c^2+r_d^2=4m$. A single row or partial tuple must satisfy
the corresponding upper bounds, but separate feasible spectral values need
not come from any common sign coefficients.

The field assumptions explain failures: over $\mathbb Q$ the algebra need
not split into one-dimensional factors, although it splits after adjoining
$\zeta$; if the characteristic divides $m$, $z^m-1$ has repeated roots
and this semisimple Fourier argument breaks. Positivity and absolute-square
inequalities require the real/complex setting; they have no automatic meaning
over a finite field.

## A quotient test is not a lift theorem

For $d\mid m$, the group homomorphism $C_m\to C_d$ gives an algebra
quotient sending $z$ to the generator of order $d$. The compressed coefficient
is $y_r=\sum_{j\equiv r\ (d)}x_j$. Applying the quotient to the four
correlation identity gives

$$\sum_x C_{y_x}C_{y_x}^{\mathsf T}=4mI_d.$$

The right side remains $4m$, not $4d$, and compressed coefficients are
integer sums rather than signs. This is a necessary consequence of a full
solution. The quotient discards coefficients, so its converse needs a separate
common-lift theorem.

The prior proof gives an exact illustrative failure at $m=9$. The normalized
symmetric masks $(2,10,10,13)$, where bit $j-1$ negates positions
$\pm j$, compress at $d=3$ to

$$(3,1,1),\quad(3,-1,-1),\quad(3,-1,-1),\quad(-1,-1,-1).$$

Their total compressed autocorrelation is $(36,0,0)$ and their row-square
sum is $36$, so both proper cyclic quotients of $C_9$ pass. But their
uncompressed autocorrelation at shift $1$ sums to $-8$. This shows that
these particular lifts fail; it alone would not prove that every other lift
of the compressed multiset fails. The prior independent review separately
records a stronger no-common-lift fixture: the compressed multiset

$$(-1,-1,-1),\quad(-1,1,1),\quad(-1,3,3),\quad(3,-1,-1).$$

It too has total compressed autocorrelation $(36,0,0)$. There are 16
normalized symmetric sign rows at core nine; among their four-row multisets,
exactly 27 map to this specified compressed multiset. The new exact checker
independently reconstructs and rejects all 27 by their full autocorrelations.
Thus no common lift exists **in this normalized symmetric Williamson family**.
That is stronger evidence than one failed lift, and still says nothing about
nonexistence of arbitrary Hadamard matrices of order 36.

Even positive spectral residuals need not have a sign lift. At $m=7$, let
three sequences have negative positions $\{\pm1\}$, $\{\pm2\}$,
and $\{\pm3\}$. Their squared circulants sum to $20I+J$, leaving
$8I-J$ toward the target $28I$. This residual is positive definite:
its eigenvalues are $1$ on constants and $8$ on their orthogonal complement.
Nevertheless the odd Williamson product constraint below forces the fourth
sequence to be all positive; its row-sum square is $49$, while the remaining
row-square budget is $1$. No fourth Williamson row exists. A positive real
Gram factor does not necessarily satisfy the required discrete sign pattern.

## Why four colors appear in the prior reduction

Now let $m=2h+1$ be odd and normalize every sequence by $x_0=1$.
Write $T(z)=\sum_{j=0}^{m-1}z^j$ and
$N_x(z)=\sum_{x_j=-1}z^j$, so $X=T-2N_x$.
The identities $T^2=mT$ and $TN_x=|N_x|T$, substituted into the
Williamson equation and divided coefficientwise by $4$ in the integral
group algebra, give

$$\sum_xN_x^2+(m-R)T=m,\qquad R=\sum_x|N_x|.$$

Each $|N_x|$ is even by symmetry and normalization. Modulo $2$, squaring
removes cross terms and sends $z^j$ to $z^{2j}$. Since doubling permutes
residues modulo odd $m$, each nonzero position contains an odd number of
negative entries among the four rows. Equivalently

$$a_jb_jc_jd_j=-1\qquad(j\ne0).$$

This is the odd Williamson product theorem in the prior proof. Its hypotheses
are structural restrictions; it is not a constraint on arbitrary Hadamard
matrices.

Let $v_c=\mathbf1-2e_c\in\mathbb Z^4$, $c=1,2,3,4$.
The eight four-entry sign columns with product $-1$ are uniquely
$\varepsilon v_c$ with $\varepsilon=\pm1$, and

$$v_c^{\mathsf T}v_d=4[c=d],\qquad
\mathbf1^{\mathsf T}v_c=2.$$

Thus each nonzero column has a color $\kappa_j$ and sign
$\varepsilon_j$, reflected at opposite indices. For a nonzero shift $t$,
pair the correlation terms indexed by $j$ and $-t-j$. The pair involving
zero contributes $4\varepsilon_t$; the unique fixed term contributes
$4$. The remaining $h-1$ pairs define edges $E_t$ on the opposite-index
classes. Each contributes
$8\varepsilon_u\varepsilon_v[\kappa_u=\kappa_v]$. Hence exact
correlation is equivalent to

$$\varepsilon_t+1+
2\sum_{\{u,v\}\in E_t}\varepsilon_u\varepsilon_v
[\kappa_u=\kappa_v]=0.$$

If $c_t$ counts its monochromatic edges, reducing this equation modulo $4$
gives $\varepsilon_t=-(-1)^{c_t}$. All signs are therefore forced by a
complete coloring. The full integer equations still have to hold; the parity
consequence alone is insufficient.

Permuting the four block rows merely permutes color names. Naming colors in
order of first appearance, with at most four colors, gives a unique
restricted-growth representative of each orbit. This is a quotient by block
permutations, including repeated blocks. It is not classification up to all
Hadamard matrix equivalences, nor a quotient by arbitrary coordinate changes.

## Boolean polynomials and the precise relaxation boundary

Encode each color minus one by two bits $a_i,b_i$. In the Boolean algebra

$$B=\mathbb F_2[a_i,b_i\ (1\le i\le h)]/
(a_i^2-a_i,b_i^2-b_i),$$

every function on the bit cube has a unique squarefree polynomial. Induct on
the last bit: any function is $f_0+x(f_1-f_0)$, which proves existence and
uniqueness recursively. Equality of colors has polynomial

$$\delta_{uv}=(1+a_u+a_v)(1+b_u+b_v).$$

It is $1$ exactly when both bits agree. Therefore

$$n_t=1+\sum_{\{u,v\}\in E_t}\delta_{uv},\qquad
\varepsilon_t=(-1)^{n_t}$$

has degree at most two in the bits. Substituting a partial assignment preserves
this degree bound. Write a residual $n_i=\alpha_i+p_i$ with constant
$\alpha_i$ and zero-constant polynomial $p_i$, and put
$\eta_i=(-1)^{\alpha_i}$, $\xi_p=(-1)^p$. Then

$$\varepsilon_i=\eta_i\xi_{p_i},\qquad
\varepsilon_u\varepsilon_v=\eta_u\eta_v\xi_{p_u+p_v}.$$

These are exact identities of functions. Equal residual polynomials therefore
represent the same unknown phase even before its sign is known. Summing their
integer coefficients first can reveal cancellation that separate sign ranges
miss. Constants and linear terms must be included when deciding equality;
equal quadratic parts alone do not suffice.

The exponents are computed in $B$, of characteristic two. The correlation
coefficients and their sums are computed in $\mathbb Z$. The map
$p\mapsto(-1)^p$ converts addition of Boolean functions into multiplication
of signs; it is not a ring map allowing integer coefficients to be reduced
modulo two.

After grouping, a lag expression can have the exact form
$K+\sum_pc_p\xi_p$. Treating distinct $\xi_p$ as independent signs
gives a safe superset of its attainable values, hence a sound rejection test
when zero is absent. Presence of zero is only a necessary condition. Relations
such as $\xi_{p+q}=\xi_p\xi_q$ remain; even preserving all such linear
phase relations need not enforce the quadratic origin. For example, the
values of $a,b,ab$ cannot be $(0,0,1)$, though these three polynomials
are linearly independent over $\mathbb F_2$. A prospective stronger method
must specify which extra dependencies it keeps and prove its rejection rule.

The prior work's core-11 false-positive prefix is a concrete warning that
separately feasible row and lag relaxations can lack a common completion.
Its existing audit, not a new run here, supports that bounded observation.
Neither the algebraic reduction nor the word “exact” makes every downstream
relaxation complete.

## What to learn next for this direction

| Tool needed for the study | Source in the collection | Supplement supplied or still needed |
| --- | --- | --- |
| Orthogonality, Gram matrices, positive residuals | Xi II §§3.1–3.5, 3.8 | Gram-factor versus sign-factor distinction; examples above |
| Kronecker products and tensor identities | Xi II §6.2; Hungerford IV.5; Grillet XI.5–6 | Sylvester closure proof above |
| Cyclic groups, quotient rings, polynomial actions | Xi III §§1.2, 4.2–4.4; Hungerford III–IV; Grillet III, VIII | Integral cyclic-algebra involution and correlation dictionary above |
| Finite fields and multiplicative characters | Xi III §5.6; Hungerford V.5; Grillet IV.1.6 and V.1.3 | Quadratic-character sum and both Paley block proofs above |
| Character decomposition and invariant splitting | Xi III §§3.1–3.5; Grillet IX.2, IX.7–9 | Fourier inversion as CRT, with splitting/characteristic hypotheses above |
| Compression and common lifting | Quotients and maps throughout the core | A real additional theorem would have to couple sign lifts; none is assumed |
| Quadratic Boolean constraints | Polynomial rings, quotients, functions on finite fields | Boolean normal form and phase dependence above; algorithmic feasibility remains a separate subject |

The strongest useful next reading task is to reconstruct each displayed
dictionary and counterexample, then read the pinned prior proofs with the
coefficient rings visible. A later research proposal should target a specific
lost dependency, a genuinely wider construction family, or a proved lift
criterion. Such proposals are prospective; no improvement in search complexity
or progress toward universal existence is claimed by this foundational chapter.
