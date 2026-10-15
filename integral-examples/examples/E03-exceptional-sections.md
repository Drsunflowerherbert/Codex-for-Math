# E03 — A null measurable set with one nonmeasurable section

## Problem

Find a Lebesgue-measurable set $E\subset\mathbb R^2$ for which the vertical section

$$
E_x=\{y\in\mathbb R:(x,y)\in E\}
$$

is not Lebesgue measurable for one value of $x$. Reconcile this with Fubini's theorem, and prove the correct almost-everywhere statement for sections of arbitrary Lebesgue-measurable sets.

## Data and hypotheses

Use complete Lebesgue measures $\mathcal L^1$ and $\mathcal L^2$. Choose a non-Lebesgue-measurable set $V\subset[0,1]$ and define

$$
E=\{0\}\times V.
$$

Such a $V$ exists under the usual axiom of choice. For completeness, choose one representative from each equivalence class in $[0,1]$ under $s\sim t$ when $s-t\in\mathbb Q$. The translates $V+q$, for $q\in\mathbb Q\cap[-1,1]$, are disjoint, cover $[0,1]$, and lie in $[-1,2]$. If $V$ were measurable with measure zero, their countable union could not cover $[0,1]$. If it had positive measure, countably many disjoint translates would have infinite measure inside $[-1,2]$. These two alternatives prove nonmeasurability.

## Solution

**1. Joint measurability does hold.** The set $E$ lies in the Borel set $N=\{0\}\times[0,1]$. For every $\varepsilon>0$,

$$
N\subset(-\varepsilon,\varepsilon)\times[0,1],
\qquad \mathcal L^2(N)\leq2\varepsilon.
$$

Hence $\mathcal L^2(N)=0$. Completeness of $\mathcal L^2$ implies that its subset $E$ is Lebesgue measurable and has measure zero. Thus the function $\mathbf 1_E$ is Lebesgue measurable and belongs to $L^1(\mathbb R^2)$, with integral $0$.

**2. Inspect each section.** At $x=0$, the section is $E_0=V$, which is not Lebesgue measurable. For every $x\ne0$, $E_x=\varnothing$, so its measure and the integral of its indicator are $0$. In particular

$$
y\longmapsto\mathbf 1_E(0,y)=\mathbf 1_V(y)
$$

is a nonmeasurable section function. One must not write its Lebesgue integral as though it were defined.

For comparison, every horizontal section is either $\{0\}$ or $\varnothing$, so it is measurable and has measure zero. In this direction the section-measure function is identically $0$, even though deciding which of the two section sets occurs depends on membership in $V$.

**3. Interpret the iterated integral correctly.** On the full-measure set $\mathbb R\setminus\{0\}$ the vertical inner integral exists and equals $0$. Extend that outer integrand by the value $0$ at the exceptional point. Its integral is $0$, agreeing with $\int\mathbf 1_E\,d\mathcal L^2=0$. This is an extension of an almost-everywhere defined inner integral; it is not an assertion that the original inner integral existed at $x=0$.

**4. Prove the general section statement.** Let $A\subset\mathbb R^{m+n}$ be Lebesgue measurable. Borel regularity and completion provide Borel sets $B,N\subset\mathbb R^{m+n}$ such that

$$
A\mathbin{\triangle}B\subset N,
\qquad \mathcal L^{m+n}(N)=0.
$$

Here $\triangle$ denotes symmetric difference. For every $x\in\mathbb R^m$, the sets $B_x$ and $N_x$ are Borel subsets of $\mathbb R^n$: the section is the preimage under the continuous map $y\mapsto(x,y)$. Since $\mathbf 1_N\in L^1$, Fubini applied to this Borel function gives

$$
\int_{\mathbb R^m}\mathcal L^n(N_x)\,d\mathcal L^m(x)=0.
$$

Its nonnegative integrand is therefore zero outside a measurable $\mathcal L^m$-null set $Z$. For $x\notin Z$,

$$
A_x\mathbin{\triangle}B_x\subset N_x,
\qquad \mathcal L^n(N_x)=0.
$$

Completeness of $\mathcal L^n$ now implies that $A_x$ is Lebesgue measurable and has the same measure as $B_x$. Thus **vertical sections are Lebesgue measurable for almost every $x$**. Interchanging the coordinate blocks proves the corresponding horizontal assertion. This argument does not prove measurability at parameters in $Z$, and the example shows why it cannot.

## Why the theorem applies

In Step 4, Fubini is applied to the Borel null envelope $N$, whose indicator is absolutely integrable. It is not prematurely applied to a possibly nonmeasurable section of $A$. For an $L^1$ Lebesgue-measurable function, completed-measure Fubini similarly gives measurable, integrable sections almost everywhere and equality after the almost-everywhere defined outer integrand is extended on a null set.

A set in the uncompleted product $\sigma$-algebra $\mathcal L(\mathbb R^m)\otimes\mathcal L(\mathbb R^n)$ has measurable sections at **every** parameter. Indeed, sets with measurable sections form a $\sigma$-algebra containing all measurable rectangles. The example $E$ therefore belongs to the completed planar Lebesgue $\sigma$-algebra but not to that uncompleted product $\sigma$-algebra.

## Pitfalls

- “Jointly Lebesgue measurable” does not imply that every section is Lebesgue measurable.
- Completeness of each factor measure does not make the uncompleted product measure complete.
- Changing a jointly measurable function on a planar null set can damage exceptional one-dimensional sections. It does not change the joint Lebesgue integral.
- This construction requires a nonmeasurable set; it is not an explicit numerical algorithm for testing membership in $V$.

## Reusable technique

Tags: `exceptional-sections`, `completion`, `Borel-representative`, `null-envelope`, `Fubini`, `Vitali-set`.

To justify a section argument for completed measures, replace the joint object by a Borel representative, control the difference inside a Borel null envelope, and use Fubini on that envelope. Record the exceptional parameter set rather than suppressing it.

## Sources

- John K. Hunter, [*Measure Theory*](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf), Example 5.20 and Theorem 5.21, printed p. 62; Theorems 2.27–2.28 (Borel regularity and completion). Source ID: `hunter-measure`. The null-set construction is the classical completion example; the representative-and-envelope proof and its integral interpretation are detailed above.
