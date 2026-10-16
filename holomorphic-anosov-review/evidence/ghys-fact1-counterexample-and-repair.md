# Ghys 1995, p. 596, Fact 1: counterexample to an unnecessary strengthening

## Source and significance

Source: Étienne Ghys, *Holomorphic Anosov systems*, Inventiones mathematicae **119** (1995), 585–614, DOI [10.1007/BF01245193](https://doi.org/10.1007/BF01245193); [author's PDF](https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf), printed p. 596, Fact 1 in the proof of Lemma 4.3.

The source states, under its equality-of-diameters hypothesis, the existence of “closed discs Dj containing Kj with disjoint interiors and whose centers are on the same line”. That stronger assertion is false. The no-triple-intersection consequence actually used in the proof is true and has a short direct proof below. This is a harmless overstatement in a cited source, **not a counterexample to Zhang's theorem or to Ghys's needed combinatorial consequence**.

## Exact counterexample

Regard the real line as a subset of the complex plane, and set

\[
 K_1=[0,1],\qquad
 K_2=\operatorname{conv}\{1,2,\tfrac32+\tfrac{\sqrt3}{2}i\},\qquad
 K_3=[2,3],\qquad K=K_1\cup K_2\cup K_3.
\]

All three sets are nonempty connected compact sets. Their diameters are all 1. The union is connected and has diameter 3: its extreme pair is 0 and 3, and all other vertex-pair distances are at most 3; convexity of each component reduces verification to these vertex pairs. Thus

\[
 \operatorname{diam}K=3=\sum_{j=1}^3\operatorname{diam}K_j.
\]

Suppose the asserted containing disks \(D_1,D_2,D_3\) existed. Each has positive radius. Since \(1\in K_1\cap K_2\), disks \(D_1,D_2\) meet at 1. Disjoint interiors force them to be externally tangent there. Likewise \(D_2,D_3\) are externally tangent at 2. A tangency point of two disks lies on their center line, so the common line of all three centers contains both 1 and 2 and is the real axis. The middle disk's circle passes through both 1 and 2 and its center is real. Its center is consequently \(3/2\) and its radius is \(1/2\). But the triangle's third vertex has distance \(\sqrt3/2>1/2\) from that center, contradicting \(K_2\subset D_2\).

The accompanying JSON records elementary coordinate checks. Those numerical calculations support the geometry; the preceding exact argument supplies the proof.

## Direct proof of the consequence actually needed

Let a connected compact metric-space subset \(K\) be the union of finitely many nonempty compact subsets \(K_1,\ldots,K_N\), with \(d_j=\operatorname{diam}K_j>0\), and suppose

\[
 D:=\operatorname{diam}K=\sum_jd_j.
\]

Choose \(a,b\in K\) with \(d(a,b)=D\). The intersection graph of the \(K_j\) is connected: a disconnected intersection graph would split the finite closed cover into two disjoint, nonempty, relatively closed subsets of \(K\). Pick a shortest graph path from a set containing \(a\) to a set containing \(b\). For every consecutive pair choose an intersection point. The triangle inequality along this chain gives

\[
 D\leq\sum_{j\text{ on the path}}d_j\leq\sum_{j=1}^Nd_j=D.
\]

Every vertex must lie on that path because all \(d_j>0\). An edge joining nonconsecutive vertices would shorten the path, contradicting its minimality. The intersection graph is therefore exactly a path. In particular it contains no triangle. A point belonging to three distinct \(K_j\) would create a triangle in the intersection graph, which is impossible.

This proof works in any metric space. It supplies exactly the multiplicity-at-most-two conclusion needed in Ghys's dimension argument. It does not require the false disk-containment strengthening.

## Later primary comparison

J. Zhang, *On the global product structure for uniformly quasiconformal Anosov diffeomorphisms*, DCDS **45** (2025), 567–584, DOI [10.3934/dcds.2024102](https://doi.org/10.3934/dcds.2024102), [arXiv:2311.00251v2, §4](https://arxiv.org/html/2311.00251v2), states only this no-triple-intersection consequence as Fact 1. This later paper does not claim to be an erratum to Ghys. Its main theorem assumes transitivity, so it does not independently resolve the separate terse transitivity inference in Ghys Lemma 4.3.
