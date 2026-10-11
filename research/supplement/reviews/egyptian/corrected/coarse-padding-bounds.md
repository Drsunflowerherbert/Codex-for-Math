# Coarse denominator bounds for exact marker padding

## Scope

This optional corollary makes explicit a coarse bound already supplied by the construction in EGY-003. It accompanies the [corrected study](study.md) and does not alter EGY-001 through EGY-006. It gives an existential bound for expansions produced by that padding construction. It makes no assertion about optimal denominators, efficient computation, or the manuscript's global short-expansion estimates. No novelty or Lean-verification claim is made.

## One padding step

Corollary EGY-COR-001. Let r≥3 be an integer and let positive integers n_1<⋯<n_r satisfy

    1=Σ_{i=1}^r 1/n_i.

Choose a marker m among the n_i, and let M=n_r. There exists a strictly increasing list of exactly r+1 positive integer denominators with reciprocal sum one, containing the exact denominator m, whose maximum M′ satisfies

    M′≤M(M+1).

Proof. Use the construction of EGY-003. Every original denominator is at least two: a denominator one would exhaust the sum while other positive terms remain. In particular M≥2. EGY-003 already proves positivity, integrality, distinctness, length and preservation of the exact marker. We check the maximum in every branch of that construction.

If the largest denominator is unmarked, set s=M and replace it by s+1 and s(s+1). Both new denominators and every retained denominator are at most M(M+1). In this branch the new maximum is exactly M(M+1).

If the largest denominator is marked, the construction splits the second largest denominator s<M. In the ordinary branch its replacements are s+1 and s(s+1). Since 2≤s≤M and multiplication of nonnegative numbers is monotone,

    s+1≤s(s+1)≤M(M+1).

All retained denominators are at most M≤M(M+1), so the desired bound follows.

In the exceptional composite branch, write s=ab with a,b≥2. Its replacements s+a and b(s+a) satisfy the strict inequalities established in EGY-003:

    s+1<s+a<b(s+a)<s(s+1)≤M(M+1).

Retained denominators are again at most M. The prime-exception cases are impossible by EGY-003, so these branches exhaust the valid inputs. This proves the one-step bound.

## Iterated padding

Corollary EGY-COR-002. Under the same assumptions, let t≥0 be an integer and set M_0=M. There exists a strictly increasing list of exactly r+t positive integer denominators with reciprocal sum one, containing the exact denominator m, whose maximum M_t satisfies

    M_t≤(M_0+1)^(2^t)−1.

Proof. When t=0, use the original list and equality holds in the displayed bound. Apply EGY-COR-001 successively. At every stage the result still has distinct positive integer denominators, reciprocal sum one, the same marker and at least three terms. All required hypotheses are therefore preserved. If M_j denotes the maximum after j stages, choose the next result using that construction, so

    M_{j+1}≤M_j(M_j+1).

For every j, M_j is nonnegative, and hence

    M_{j+1}+1≤M_j²+M_j+1≤(M_j+1)².

Starting with M_0+1=(M_0+1)^(2^0), induction gives

    M_j+1≤(M_0+1)^(2^j).

Indeed, squaring the induction bound is valid because both sides are nonnegative, and doubles the exponent from 2^j to 2^(j+1). Subtract one and take j=t. The constructed list has exactly r+t terms and retains m by the same induction, completing the proof.

These estimates are intentionally coarse. They establish that the explicit padding argument has a denominator-size bound, while making no claim that its double-exponential form is necessary or sharp.

## Evidence status

The proofs above are elementary deductions from the reviewed padding construction. They have not received an additional separate independent review or Lean formalization. Direct checks of the one-step maximum on the existing finite certificates are recorded in validation-results.json; those checks are supplementary and are not the universal proof. Machine-readable corollary records are in [coarse-padding-bound-records.json](coarse-padding-bound-records.json).
