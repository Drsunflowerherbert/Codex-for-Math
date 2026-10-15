# Source and status audit

Checked **2026-10-15 (UTC)**. This ledger distinguishes a mathematical theorem,
an independently checkable finite witness, a source's status report, and an
inference from dated reports. No external repository code or posted shell
decoder was executed for this audit.

## Current finite result and attribution

- [Epoch AI, Hadamard Matrix of Order 668](https://epoch.ai/frontiermath/open-problems/hadamard)
  presently labels the task **“Solved (human + AI)”**. Its solution update
  reports that a public puzzle encodes all previously missing admissible orders
  through 2000, including 668, and names an internal Anthropic Claude model.
  Its attribution remains provisional. The same page's older About text still
  calls 668 the smallest unknown order; use the solution update, and record this
  internal inconsistency. The page supplies a 2026 citation but no precise
  publication/update timestamp found in the HTML. This is a finite existence
  report, not a resolution of the general conjecture. Page license: CC BY 4.0.

- Levent Alpöge's primary X thread consists of the
  [sign payload](https://x.com/__alpoge__/status/2087504785952182273),
  [decoder](https://x.com/__alpoge__/status/2087504788938510427), and
  [attribution reply](https://x.com/__alpoge__/status/2087504790435840207).
  Direct X retrieval returned HTTP 403. The official
  [X oEmbed endpoint](https://publish.twitter.com/oembed?url=https%3A%2F%2Ftwitter.com%2F__alpoge__%2Fstatus%2F2087504790435840207&omit_script=true)
  returned **August 12, 2026** and the reply:
  “weekend fun w @tehwalris, Saul Reynolds-Haertle, and of course claude:)) i only claim bad suggestions!!”.
  oEmbed truncates the long payload and decoder; it establishes announcement
  metadata, not full data provenance or how the mathematics was discovered.

- [MathOverflow answer 514202](https://mathoverflow.net/a/514202), originally by
  **natalia**, names **Levent Alpöge, Philippe Voinov, Saul Reynolds-Haertle,
  and Claude**. Its separately attributed contribution by **David E Speyer**
  reports his direct verification of the downloaded order-668 matrix:
  `H H^T = 668 I`. The
  [revision history](https://mathoverflow.net/posts/514202/revisions) and
  [Stack Exchange API](https://api.stackexchange.com/2.3/posts/514202/revisions?site=mathoverflow)
  date the original answer to **2026-08-12 14:52:41 UTC**, and Speyer's first
  verification edit to **2026-08-13 12:00:29 UTC** (revision 3). It is a
  community wiki; do not attribute every paragraph to Speyer. API content
  license: CC BY-SA 4.0. These sources do not establish a division of
  mathematical labor among the four credited contributors.

## Accessible order-668 data

| Artifact | Access and audit information |
| --- | --- |
| Sumeet Motwani's CSV | Linked by Speyer in the [public Drive folder](https://drive.google.com/drive/folders/111dYn72d8bElNjYRHn2WTLXnUpwwJ8fX). The file [hadamard_668.csv](https://drive.google.com/file/d/1kxRbFEF5QFn7lWTSDhEDJCAETTgaSAsV/view) was directly readable as data: 668 rows, 668 columns, entries `-1,1`; 1,115,894 bytes; SHA-256 `5eaef5f4c814469a1f0815756876b83e8c4944ff7ccf4f023ee479de5e8f9a8b`. No explicit data license was found. |
| nreff text fixture | [Pinned raw matrix](https://raw.githubusercontent.com/nreff/hadamard-search/30afdda2a8ecfcc9733e26f979a1c5af36e73975/fixtures/known/hm-668/matrix.txt). Its [pinned provenance record](https://github.com/nreff/hadamard-search/blob/30afdda2a8ecfcc9733e26f979a1c5af36e73975/fixtures/known/hm-668/README.md) reports reconstruction from the X payload on 2026-08-12; 446,892 bytes; SHA-256 `bdeb5059d77e2703211082627b60441b8c888c928a55cc6f295e011941a387b0`. This audit treats those reconstruction and verification statements as repository claims until checked locally. |
| Compact seed | [Pinned four length-166 sign sequences](https://raw.githubusercontent.com/nreff/hadamard-search/30afdda2a8ecfcc9733e26f979a1c5af36e73975/fixtures/known/hm-668/spence-sequences.txt). The repository identifies a cyclic type-H4* difference family with negative-support parameters `(166;82,83,83,83;164)` and a Wallis–Whiteman bordered construction. Its [construction note](https://github.com/nreff/hadamard-search/blob/30afdda2a8ecfcc9733e26f979a1c5af36e73975/docs/research/hm-668-construction.md) explicitly leaves the seed's discovery method unresolved. |

The external repository was pinned using the GitHub API to commit
[`30afdda2a8ecfcc9733e26f979a1c5af36e73975`](https://github.com/nreff/hadamard-search/commit/30afdda2a8ecfcc9733e26f979a1c5af36e73975),
dated **2026-08-13 05:03:04 UTC**, unsigned. Its
[repository metadata](https://api.github.com/repos/nreff/hadamard-search)
returned `license: null`; its recursive tree had no LICENSE/COPYING/NOTICE file.
Public accessibility is not an explicit redistribution license. The data can be
read and checked without copying the repository's implementation into this study.
Different text/CSV encodings naturally have different byte digests; mathematical
equality requires comparing their parsed entries.

## The post-2000 frontier requires a dated qualification

[Matteo Cati and Dmitrii V. Pasechnik, *A database of constructions of Hadamard
matrices*, arXiv:2411.18897v2](https://arxiv.org/abs/2411.18897v2), revised
**2025-08-30**, is primary construction/database research (CC BY-SA 4.0).
In [Table 4, PDF p.18](https://arxiv.org/pdf/2411.18897v2#page=18), `n(m)`
records the least known exponent for order `2^m n`; omitted entries have `m=2`.
The first twelve exceptional odd parts are
`167,179,223,283,311,347,359,419,443,479,487,491`, followed by `515(3)`.
Section 6, PDF p.10, explicitly says the old Miyamoto claim for `4*515`
could not be verified because details were missing. The PDF and TeX source were
checked; the experimental HTML omits Table 4.

The [external repository's frontier note](https://github.com/nreff/hadamard-search/blob/30afdda2a8ecfcc9733e26f979a1c5af36e73975/docs/research/hm-2060-frontier.md)
is dated **2026-08-13** and calls 2060 the next public, verifiable gap after the
twelve newly filled cases. That is consistent with the 2025 table plus the
reported August update. It is an inference from a dated construction record,
not a nonexistence theorem or a fully audited current frontier.

There is a material later **explicit order-2060 construction claim**:
[Loïc Schneider's repository](https://github.com/schneiderlo/hadamard-2060/tree/ad794186b6788328a2de6e6f6d68f7c493464735).
Its initial commit is dated **2026-08-25**; the pinned revision
`ad794186b6788328a2de6e6f6d68f7c493464735` is dated **2026-10-01** and carries
an [MIT license naming Loic Schneider](https://github.com/schneiderlo/hadamard-2060/blob/ad794186b6788328a2de6e6f6d68f7c493464735/LICENSE).
GitHub commit metadata uses the author handle `schneiderlo`; the pinned Sage
source below spells the credited name **Loïc Schneider**.
Its README supplies an explicit matrix, reports exact Gram and
all-row-pair checks, and gives SHA-256
`8c81090db76e2b503561ba82598b514e0c2e39940a3703783c5b1b2c6b80a37a`
for the 14,882,482-byte
[H2060.py data assignment](https://raw.githubusercontent.com/schneiderlo/hadamard-2060/ad794186b6788328a2de6e6f6d68f7c493464735/H2060.py).
The data assignment can be parsed as a literal without executing its file.
[Sage's primary source at commit 0835358cba62dc19fccdff54f32e52fded9f22b0](https://github.com/sagemath/sage/blob/0835358cba62dc19fccdff54f32e52fded9f22b0/src/sage/combinat/matrices/hadamard_matrix.py#L1207),
dated **2026-10-11**, credits Schneider's length-103 T-sequences and an order-5
Williamson quadruple and explicitly implements their Cooper–Wallis construction
at order 2060. This audit inspected those primary sources without executing them.
Consequently, **2060 must not be presented as securely unresolved on October 15**.
The August frontier note is obsolete as an unqualified current status source.

A further relevant source is
[Hadi Kharaghani, Ali Mohammadian, Behruz Tayfeh-Rezaie, Vlad Zaitsev,
*A Search for Hadamard Matrices of Near-Williamson Type*, arXiv:2605.08661v2](https://arxiv.org/html/2605.08661v2),
**2026-09-06**, CC0. Section 2.3 lists new near-Williamson examples at order
103, among other orders; Section 1 explains how these give amicable
Williamson-type matrices. This is a broader family than the symmetric circulant
one enumerated here. This study **does not certify the smallest currently
unresolved Hadamard order**.
The arXiv landing page still displayed the older title/author list when checked;
the pinned v2 full text supplies the four authors and revised scope.

## Classical constructions for the finite study

- **R. E. A. C. Paley**, [*On Orthogonal Matrices*](https://doi.org/10.1002/sapm1933121311),
  *Journal of Mathematics and Physics* **12**, 311–320, first published
  **April 1933**. Publisher metadata was accessible; original full text was
  not obtained. Cati–Pasechnik, Section 4.1, Theorem 1, gives an accessible
  modern statement: prime powers `q = 3 mod 4` yield a skew Hadamard matrix of
  order `q+1`. This study restricts to primes so arithmetic can be independently
  implemented over integers modulo `q`.

- **John Williamson**, [*Hadamard's determinant theorem and the sum of four
  squares*](https://doi.org/10.1215/S0012-7094-44-01108-7), *Duke Mathematical
  Journal* **11**(1), 65–81, **1 March 1944**. Bibliographic metadata was
  checked; original full text was inaccessible.

- **Curtis Bright, Ilias Kotsireas, Vijay Ganesh**, [*Applying Computer Algebra
  Systems with SAT Solvers to the Williamson Conjecture*, arXiv:1804.01172v2](https://arxiv.org/html/1804.01172v2),
  **2019-05-14**, CC BY 4.0. Section 2.1, Theorem 2 and Definitions 3–5,
  supply an accessible exact theorem and conventions: circulant entry
  `M[i,j]=x[(j-i) mod m]`; symmetric row `x[i]=x[m-i]`; the four nonzero-shift
  periodic autocorrelations sum to zero. Symmetric commuting sign matrices with
  square sum `4m I` give a Hadamard matrix via the displayed four-block array.
  Section 2.2 permits individual sequence negation and reordering. These justify
  `x[0]=+1` normalization and searching unordered quadruples; they do not by
  themselves quotient every literature equivalence.

- **W. H. Holzmann, H. Kharaghani, B. Tayfeh-Rezaie**,
  [*Williamson matrices up to order 59*](https://link.springer.com/article/10.1007/s10623-007-9163-5),
  *Designs, Codes and Cryptography* **46**, 343–352, published **2008-01-05**
  (March 2008 issue). The primary abstract reports exhaustive odd-order
  enumeration through 59 and no Williamson matrices at `35,47,53,59`.
  This is a failure of the symmetric circulant Williamson family; it does not
  rule out Hadamard matrices of orders `4m`. The September 2026 near-Williamson
  work relaxes symmetry of one sequence and therefore does not contradict it.

The tractable target is an independent Paley proof/check and complete normalized
symmetric circulant Williamson enumeration at odd `m <= 15`. At `m=15`, fixing
`x[0]=1` leaves `2^7=128` sequences. There are `C(131,4)=11,716,640` unordered
quadruples with repetitions, or only `C(129,2)=8,256` unordered sequence pairs
for a correlation-signature meet-in-the-middle table. These are direct counting
arguments for this study, not claims of new mathematics. The published
equivalence-class counts are not expected to equal counts under only our
normalization and reordering.
