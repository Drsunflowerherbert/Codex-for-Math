# E01 — Change the order to create the missing derivative

## Problem

Let

$$
D=\{(x,y)\in\mathbb R^2:0<x<y<1\}.
$$

Compute $\int_D e^{y^2}\,d\mathcal L^2(x,y)$ without finding an antiderivative of $y\mapsto e^{y^2}$.

## Data and hypotheses

The measure is two-dimensional Lebesgue measure $\mathcal L^2$; the one-dimensional integrals below use $\mathcal L^1$. Define the function on the whole plane by

$$
F(x,y)=\mathbf 1_D(x,y)e^{y^2}.
$$

Here $F$ is a function, whereas $F(x,y)$ is its value at the point $(x,y)$. The region $D$ is open and hence Borel measurable. The function $F$ is Borel measurable, is nonnegative, and satisfies $0\leq F\leq e\mathbf 1_{(0,1)^2}$. Consequently $\int_{\mathbb R^2}|F|\,d\mathcal L^2\leq e<\infty$ before any interchange is made.

## Solution

**1. Translate the region into sections.** Fix $y\in(0,1)$. The permitted values of $x$ are exactly $0<x<y$, so the horizontal section has length $y$. Fix $x\in(0,1)$ instead. The permitted values of $y$ are $x<y<1$. Thus the two descriptions are

$$
D=\{(x,y):0<y<1,\ 0<x<y\}
 =\{(x,y):0<x<1,\ x<y<1\}.
$$

These are descriptions of the same set, not a rule for swapping the symbols $dx$ and $dy$ while keeping the bounds unchanged.

**2. Integrate in the useful direction.** Fubini's theorem, justified by the absolute-integrability bound above, gives

$$
\begin{aligned}
\int_D e^{y^2}\,d\mathcal L^2(x,y)
&=\int_0^1\left(\int_0^y e^{y^2}\,dx\right)dy\\
&=\int_0^1 y e^{y^2}\,dy.
\end{aligned}
$$

In the inner integral, $y$ is fixed, so $e^{y^2}$ is constant as a function of $x$. Multiplying that value by the section length produces the factor $y$.

**3. Finish with a one-variable substitution.** Put $u=y^2$, so $du=2y\,dy$. Then

$$
\int_0^1 y e^{y^2}\,dy
=\frac12\int_0^1e^u\,du
=\boxed{\frac{e-1}{2}}.
$$

Equivalently, this also evaluates the nested expression

$$
\int_0^1\left(\int_x^1 e^{y^2}\,dy\right)dx
=\frac{e-1}{2}.
$$

The inner integral in this last expression is perfectly well-defined; lacking an elementary antiderivative does not make a function nonintegrable.

**4. A sum check.** Uniform convergence of the exponential power series on $[0,1]$ permits termwise integration here and gives

$$
\int_0^1 y e^{y^2}\,dy
=\sum_{k=0}^{\infty}\frac{1}{k!}\int_0^1y^{2k+1}\,dy
=\sum_{k=0}^{\infty}\frac{1}{2(k+1)k!}
=\frac12\sum_{j=1}^{\infty}\frac1{j!}.
$$

The last series is $(e-1)/2$. Alternatively, the nonnegative partial sums and monotone convergence justify this same termwise calculation.

## Why the theorem applies

Both factor measures are $\sigma$-finite. The region indicator makes the varying domain into a measurable function on a fixed product space. The bound $|F|\leq e\mathbf 1_{(0,1)^2}$ verifies Fubini's absolute-integrability hypothesis independently of the answer. Because $F$ is nonnegative, Tonelli also allows either order before finiteness is known. Every section in this example is Borel measurable; the weaker almost-everywhere assertion for arbitrary Lebesgue-measurable functions is discussed in E03.

## Pitfalls

- Keeping $x<y<1$ as the inner $x$-bounds is meaningless: the bounds must describe the variable being integrated.
- The integral $\int_D e^{y^2}\,d\mathcal L^2$ integrates a function over a set. It does not integrate the set or identify a function with one of its values.
- Replacing strict inequalities by non-strict ones is harmless here because the added line segments have $\mathcal L^2$-measure zero. E02 explains why such a boundary argument needs verification for a general region.

## Reusable technique

Tags: `region-sections`, `Fubini`, `Tonelli`, `indicator-extension`, `order-selection`, `power-series`.

When an inner primitive looks unhelpful, write both section descriptions explicitly. Integrating in the other direction can supply the derivative factor needed for a substitution. First verify measurability and nonnegativity or absolute integrability.

## Sources

- John K. Hunter, [*Measure Theory*](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf), Theorem 5.18 (Fubini), printed p. 61; Theorem 4.6 (monotone convergence). Source ID: `hunter-measure`. The region, computation, and sum check above are worked out directly.
