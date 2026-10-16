# Independent check of Ghys 1995, Lemma 4.3, Fact 1 (p. 596)

*Publication note: any `extension/evidence/`, `working-reference/`, or source-copy filenames in these notes identify excluded working references. Third-party PDFs, scans, OCR and raw article-response logs are not bundled. Included search/access metadata is under `../evidence/`; use the primary-source URLs for original texts.*


The proposed counterexample refutes the exact disk-containment conclusion. The weaker no-triple-intersection conclusion actually used in Lemma 4.3 is valid and has a direct repair.

## Counterexample to the disk conclusion

In the complex plane let `K1=[0,1]`, `K3=[2,3]`, and let `K2` be the filled equilateral triangle with vertices `1`, `2`, and `3/2 + i sqrt(3)/2`. Each compact set has diameter 1. Their union is connected and has diameter 3: its endpoints 0 and 3 realize that diameter; all other pairwise distances are at most 3 (equivalently the union lies in the convex hull of these five vertices, whose vertex-pair distances are at most 3).

Suppose closed disks `Dj` contain `Kj`, have pairwise disjoint interiors, and have collinear centers. All three radii are positive. The disks `D1,D2` both contain 1, so they must be externally tangent at 1. Likewise `D2,D3` are externally tangent at 2. The two tangency points lie on the common line of centers, which is therefore the real axis. Consequently the center of `D2` is real and its distances to 1 and 2 are equal to its radius. Its center must be `3/2` and its radius `1/2`. It cannot contain the apex `3/2 + i sqrt(3)/2`. Contradiction.

This checks all hypotheses of the printed Fact 1, including connectedness of the union and nonemptiness and positive diameter of every `Kj`.

## Repair of the conclusion needed by Ghys

**Claim.** If a connected compact set `K` is the union of finitely many nonempty compact sets `K1,...,KN`, all of positive diameter, and

`diam(K) = sum_j diam(Kj)`,

then the intersection graph of this cover is a path. In particular, no point is in three distinct `Kj`.

**Proof.** The intersection graph is connected: otherwise the unions over two groups of graph components would be disjoint nonempty compact sets separating `K`. Choose `a,b` realizing `D=diam(K)`. Choose sets containing `a` and `b`, and a simple intersection-graph path `Ki0,...,Kim` joining these sets. Pick one point in each successive intersection. The resulting polygonal chain from `a` to `b` has each segment contained between two points of a single `Kir`; hence

`D <= sum_{r=0}^m diam(Kir) <= sum_{j=1}^N diam(Kj) = D`.

All inequalities are equalities. Since every diameter is positive, the simple path includes every vertex. There can be no edge joining nonconsecutive vertices in that path: such an edge would give a shortcut from its first endpoint to its second, yielding another simple path between the original endpoint sets that omits at least one positive-diameter set, contradicting the same displayed inequality. The entire graph is therefore the path. A triple intersection would give a triangle in the graph, which is impossible. QED.

The proof works in any metric space; no containing disks are needed. Thus this independently confirmed error in a cited source does **not** invalidate the no-triple step or Zhang's reliance on the resulting Ghys proposition. The section reviewer remains responsible for the surrounding measure and Markov-partition hypotheses.

Source checked: local `references/Ghys1995.pdf`, p. 596; text `references/Ghys1995-layout.txt`, Fact 1 and the immediately following paragraph.
