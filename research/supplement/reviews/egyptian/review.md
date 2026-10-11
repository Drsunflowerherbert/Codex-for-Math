# Independent review of exact length Egyptian fraction transformations

## Verdict and scope

All six theorem records, EGY-001 through EGY-006, are mathematically sound under their stated hypotheses. Their ordinary proofs pass this independent review. No theorem repair or counterexample to those statements was found. The original arithmetic script reproduces the stored certificate byte for byte, and a separately implemented enumeration matches the entire sets of tested expansions, not only their counts.

One sentence in the study needs correction: the padding construction does imply a coarse denominator-size bound. Three further clarifications would make the computational evidence safer to reuse: restrict the executable enumeration to exact rational inputs, state the example routines' domain contracts and operational guard, and separate direct computational coverage from ordinary-proof evidence in the theorem metadata.

This review covers the four named study files and their author-check manifest, plus the two cited elementary source lemmas. It does not review the manuscript's global short-expansion estimates, certify historical attribution from the cited original publications, claim novelty, or perform Lean verification. The original files remain unchanged.

The source revision recorded by the study is fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb. Relevant source locations are the lemma “Removing repetitions” in [elementary.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/build/elementary.tex) and the lemma “Preserving a prescribed denominator while padding” in [prescribed.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Short-Egyptian-fractions-September-25-2026/build/prescribed.tex). Both locally saved source passages agree with the study's mathematical arguments.

## Finiteness and complete enumeration

EGY-001 is correct even for arbitrary real x>0. For a sorted length-k representation, every denominator is at least d_1, so x≤k/d_1 and d_1≤floor(k/x). For k>1, the remainder after choosing d_1 must be strictly positive because k−1 positive terms remain. Induction therefore applies separately to finitely many positive remainders. The k=1 case has at most one solution. No unstated global denominator cutoff is needed.

For the executable enumeration, x must be an exactly represented positive rational, k a positive integer, and the lower bound a positive integer. If the remaining sum is r, the next denominator d satisfies 1/d≤r and r≤j/d, giving ceil(1/r)≤d≤floor(j/r). The lower bound is intentionally loose when j>1: equality 1/d=r cannot occur, but the explicit positive-remainder test removes it. In a strict list with j>1, the upper equality r=j/d cannot occur either; retaining it in the search only creates an empty branch.

Soundness follows inductively from subtracting exactly 1/d, requiring a positive remainder when more terms remain, and accepting a final term only when its reciprocal is exactly the remaining value. Completeness follows because the first denominator of every valid list is in the searched interval and its tail satisfies the recursive lower bound. Uniqueness follows because a strictly increasing list has a unique first denominator and unique ordered tail. Termination follows from finite branching and the strict decrease of j. The code's default start=2 is complete for the tested expansions of one with at least three distinct terms, because denominator one would exhaust the sum. It is not a claim to enumerate every positive-integer representation for arbitrary inputs, such as the singleton [1].

The independent enumerator uses stricter prefix bounds, floor(1/r)+1≤d≤ceil(j/r)−1 for j>1, and an algebraically different last-two-term test. If r=A/B in lowest terms and 1/a+1/b=A/B with a<b, then

    (Aa−B)(Ab−B)=B².

Set u=Aa−B and v=Ab−B. Positivity gives u,v>0; a<b gives u<v; hence u<B<v. Conversely every factor pair uv=B² with 0<u<B, A dividing u+B and v+B, and a=(u+B)/A satisfying the lower bound supplies exactly one admissible pair. Thus scanning u=1,…,B−1 is finite and complete. This independent final-pair construction returned exactly the same input sets as the certificates.

## Cleanup and termination

EGY-002 is correct. From a positive total x<1, no denominator can equal one, and no denominator two can occur twice. Every repeated even denominator is therefore 2p with p≥2, and every repeated odd denominator is 2p+1 with p≥1.

The even replacement sums to 1/p=2/(2p). Its denominator-sum change is

    (p+1)+p(p+1)−4p=(p−1)²>0.

The odd replacement sums to 2/(2p+1). Its denominator-sum change is

    (p+1)+(p+1)(2p+1)−2(2p+1)=2p²>0.

In both cases the replacement denominators are positive integers at least two and are distinct from one another. They may coincide with other retained denominators; the proof does not assume otherwise. Sorting after each replacement preserves the fixed total and length, placing the state in the finite set from EGY-001. Strictly increasing denominator sum prevents any state from recurring and hence prevents an infinite path. A repeated denominator always permits a further replacement, so a terminal state must be distinct. This argument works for any choice among repeated denominators, not only the smallest one selected by the script.

The 10,000-step runtime guard in the example implementation is separate from this proof. Mathematical termination does not imply that every valid input is processed before that guard. The guard never comes close to firing on the recorded cases: their maximum is five replacements. A safe computational contract says that the routine either returns the checked result or reports an operational limit, without asserting a universal 10,000-step bound.

EGY-005 correctly shows why x<1 cannot simply be replaced by x≤1. In a two-term representation of one, denominator one is impossible because the other reciprocal is positive. Two distinct remaining denominators contribute at most 1/2+1/3=5/6<1. EGY-006 is also correct: if one of two reciprocals totaling 2/3 has denominator three, the other reciprocal is exactly 1/3.

## Exact marker padding

EGY-003 is correct. Its assumptions imply every denominator is at least two. Splitting an unmarked largest denominator s as 1/(s+1)+1/(s(s+1)) creates two distinct integers larger than all retained denominators, so the marker remains.

When the marker v is largest and s is second largest, every other retained denominator is strictly below s. The ordinary split can therefore collide only with v, and only when v=s+1 or v=s(s+1).

If s=ab is composite with a,b≥2, the alternate split is valid since

    1/(s+a)+1/(b(s+a))=(b+1)/(b·a(b+1))=1/s.

The strict chain s+1<s+a<b(s+a)<s(s+1) holds: the first inequality uses a≥2, the middle one b≥2, and the last follows from b(s+a)=s(b+1)<s(s+1), because b<s=ab. Thus both replacements avoid every retained denominator and both exceptional marker values. The study's stated equivalent inequality b+1<ab+1 is correct.

If s=p is prime, at least one smaller input denominator exists because r≥3. Consequently p>2 and p is odd. Let A/B be the sum of all reciprocals other than those with denominators p and v, with B their product. Each of those denominators lies strictly between zero and p, so p divides none of them and hence p does not divide B. No reduced-form assumption on A/B is needed. Clearing denominators for v=p+1 gives

    (B−A)p(p+1)=B(2p+1),

whose reduction modulo p forces B≡0. For v=p(p+1), the right side instead is B(p+2), forcing 2B≡0. Both are impossible. This excludes the prime collision, rather than assuming the integer factor search will succeed.

The separate example [3,4,7,12,14,15,20,420] has exact reciprocal sum one. With marker 420, splitting 20 naively would repeat 420. The factorization 20=2·10 gives [22,220] and the output [3,4,7,12,14,15,22,220,420]. Every output denominator is distinct and the exact marker survives.

EGY-004 follows by induction on R−r. The zero-step case uses the input itself. Each subsequent result again has positive integer, distinct denominators, sum one, at least three terms, and the same marker, so the hypotheses of EGY-003 remain available.

The scope restrictions matter. The singleton [1] shows that the r≥3 condition cannot be replaced by r≥1: there is no two-term positive expansion of one retaining denominator one. Keeping all original denominators while adding any positive reciprocal is impossible because their sum is already one. The proof promises preservation of exactly the specified marker, not preservation of the whole input set.

## Required prose correction on denominator size

Study line 74 says the padding result does not imply “any denominator-size bound.” That is too strong for the explicit construction just proved. If M is the largest input denominator, every replacement denominator is at most M(M+1), including the alternate composite split. Therefore an output can be selected with

    M′≤M(M+1).

Iterating and using M′+1≤(M+1)² gives, after t padding steps,

    M_t≤(M_0+1)^(2^t)−1.

These are coarse bounds from the construction, with no optimality claim. The sentence should say that no sharp or economical denominator-size estimate is established. The separate cleanup paragraph only disclaims a useful bound and does not need the same correction.

## Exact arithmetic and certificate audit

The original script was copied unchanged into the review's rerun directory and executed there under ordinary, unoptimized Python. It imports only the standard library. Its output exactly matches the original certificate bytes. Every original file still matches its pre-review hash; the four checksummed files also match author-checks.json.

The independent audit reads JSON as data and does not import or execute downloaded repository code. It reconstructs each cleanup trace, checks the actual identities and denominator-sum increments, checks all padding outputs and split descriptions, verifies that every input marker occurs exactly once, and compares full input sets with the factor-pair enumeration.

- Cleanup inputs: 34, exactly the declared [d,…,d] cases for 3≤d≤12 and 2≤k≤min(5,d−1)
- Cleanup replacements: 80 total, comprising 47 even and 33 odd steps; maximum trace length five
- Strict expansions of one: 1 at length three, 6 at length four, 72 at length five, and 2,320 at length six
- Unique enumerated inputs in all four lengths: 2,399
- Marked padding checks: 3·1+4·6+5·72+6·2320=14,307
- Padding branches within the enumerated inputs: 11,908 unmarked-maximum splits and 2,399 ordinary second-largest splits
- Composite collisions within those input lengths: zero
- Separate composite collision: one checked eight-term input

All independent checks pass. The special example supplements the enumeration; it is not evidence that all eight-term expansions were enumerated. No seven-term expansion enumeration was performed. The assertions of no short composite collision hold for lengths three through six; no distinct expansion of one exists at length two, while length one has no applicable second-largest-denominator padding case.

The original script does not directly test EGY-004 over arbitrary larger lengths, nor does it encode the impossibility arguments in EGY-005 or EGY-006. Those are ordinary-proof conclusions. The independent audit adds exact arithmetic checks of 1/2+1/3<1 and 2/3−1/3=1/3, but these arithmetic checks alone do not enumerate all hypothetical counterexamples. Metadata should distinguish this coverage from direct finite transformation tests.

## Reuse and validation caveats

The original functions are examples under known-good inputs, not defensive theorem validators. They do not explicitly verify that every denominator is a positive integer, that enumeration x is a positive Fraction, or that k and start have the required integer domains. Python assertions may also be disabled by optimization; a production validator should use explicit checks and exceptions. None of these issues invalidates the recorded run, whose input domains and arithmetic were independently verified.

For later formalization, retain exact hypotheses, the finite-state argument, the strict growth statistic, and the modulo-p exclusions separately. Preserve the distinction between a finite executable regression suite and a proof applying to all inputs. Do not relabel these results as Lean-checked or use this review to validate unreviewed global estimates.

## Review artifacts

- proposed-revisions.md contains minimal replacement wording and metadata recommendations
- independent_audit.py contains the standalone certificate audit and independent final-pair enumeration
- independent-audit-results.json records the completed check totals and source hashes
- review-records.json records the separate ordinary-proof review statuses for EGY-001 through EGY-006
- rerun/check_examples.py is the unchanged copied original script; rerun/exact-examples.json is its byte-identical output
- original-sha256-before.txt and original-sha256-after.txt record preservation of the source inputs
