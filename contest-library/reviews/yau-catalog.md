# Independent review — Yau catalog and editorial source observations

**Status:** passed a bounded independent metadata and source-fidelity audit on 2026-10-13 UTC, by agent `proof_2014`. This does not certify every problem statement or every official solution mathematically correct. No formal verification is claimed.

**Spoilers:** this review discusses the separate editorial source observations. The [problem catalog](../catalogs/yau-analysis.md) contains topic metadata; [official solution access](../catalogs/yau-official-solutions.md), [editorial source observations](../catalogs/yau-source-issues.md), authored hints, and authored proofs remain separate.

## Coverage and numbering

The independently checked total is **152 numbered written Analysis problems in 26 papers, 2010–2025**: 59 Individual, 58 Team, and 35 in papers labeled “main” editorially because their source headings do not say Individual or Team. Thus the catalog's combined Individual/main count of 94 is correct.

| Year | Individual | Team | Editorial main | Total |
| --- | ---: | ---: | ---: | ---: |
| 2010 | 6 | 6 | 0 | 12 |
| 2011 | 6 | 6 | 0 | 12 |
| 2012 | 6 | 6 | 0 | 12 |
| 2013 | 6 | 6 | 0 | 12 |
| 2014 | 6 | 6 | 0 | 12 |
| 2015 | 6 | 6 | 0 | 12 |
| 2016 | 6 | 6 | 0 | 12 |
| 2017 | 6 | 6 | 0 | 12 |
| 2018 | 6 | 5 | 0 | 11 |
| 2019 | 5 | 5 | 0 | 10 |
| 2020 | 0 | 0 | 6 | 6 |
| 2021 | 0 | 0 | 6 | 6 |
| 2022 | 0 | 0 | 6 | 6 |
| 2023 | 0 | 0 | 6 | 6 |
| 2024 | 0 | 0 | 5 | 5 |
| 2025 | 0 | 0 | 6 | 6 |
| **Total** | **59** | **58** | **35** | **152** |

For each paper, coverage consists of the consecutive original numbers 1 through the count in this table. Counts, original labels, and starting PDF page positions were compared with the private primary-source extraction records. All 152 IDs are unique; paper links, year/category fields, numbers, pages, and official-solution availability/access fields are internally consistent. All 26 paper hashes were independently recomputed and match the catalog.

Combined Team PDFs were checked at their Analysis section boundaries: 2013 and 2016 Analysis occupy PDF pages 1–2; 2017 and 2018 Analysis occupy PDF page 1. Later Geometry or Probability sections were not counted as Analysis. Subparts were not counted as separate numbered problems. The 2019 labels preserve the original `1)` style. Visual inspection of both 2024 pages confirmed its five labels and their punctuation, including `Problem 5 .`; the catalog does not silently regularize those source labels.

The public metadata carries editorial titles, subjects, prerequisites, and difficulty judgments rather than full source statements. Difficulty levels use the declared common scale; the earlier preparation levels are retained as editorial provenance. Exact original conditions remain in the named [official archive members](https://yau-contest.com/index/reldown?en=1&id=9).

## Official solution mappings and scope limits

The three solution PDFs for 2020, 2021, and 2022 are present and readable in the official written archive. Each has original Problem headings 1–6 and six Solution markers. For each of the 18 mapped numbers, the start of the repeated problem statement matches the corresponding problem paper; the source member names and independently recomputed PDF hashes also match. This confirms access and numbering coverage, not correctness of the official proofs.

Both downloaded archive hashes were independently recomputed and match the manifest. Oral coverage remains a **40-file member inventory across 2012–2025**, not a count of 40 distinct papers or a verified oral problem catalog. Oral problem counts, numbering, language, and embedded solution coverage remain unverified. Written subjects other than Analysis remain member-level inventory only.

There are no 2026 paper or problem rows. The manifest has six 2026 filename/size inventory records, explicitly scoped as excluded current-year names only; they contain no member hashes. No 2026 member was extracted or inspected for this audit. The complete official archive hash naturally covers the downloaded ZIP bytes, which include those members.

## Editorial source observations

The nine retained observations were independently checked against rendered primary PDF pages, and their mathematical examples were checked. These are **editorial observations, not official errata**. They do not authorize replacing source hypotheses or claim that unflagged statements have been certified.

| Source observation | Independent result |
| --- | --- |
| 2010 Individual P5 | The chosen integrable step kernel sends the constant continuous function to a jump function with no continuous representative. The printed integrability hypothesis is insufficient. |
| 2014 Team P3 | The bounded annular function with an essential singularity defeats the factorization under the explicitly stated usual single-valued interpretation. The integer-power and finite-pole reasoning is valid under that convention. |
| 2015 Team P5 | Zero bounded and compact operators on an infinite-dimensional Hilbert space satisfy the hypotheses and leave an infinite-dimensional cokernel. |
| 2015 Team P6(2) | The harmonic polynomials satisfy smoothness on the disk closure. Their stated normalization gives norm one; angular orthogonality gives pairwise distance $\sqrt2$, so there is no $L^2$-convergent subsequence on the whole disk. |
| 2016 Team P4 | Translations on the stated complex torus give uncountably many holomorphic automorphisms, while the claimed full group is countable. The source does not restrict automorphisms to fix the origin. |
| 2016 Team P5 | The source's own nonzero first basis vector is an eigenvector for eigenvalue zero, contradicting the printed “no eigenvectors” claim under the ordinary definition. |
| 2021 main P4 | The zero-polynomial observation is valid under the explicitly stated standard convention allowing the zero polynomial. It does not assess the official argument for nonzero polynomials. |
| 2022 main P2 | The two disjoint disks and component-wise map satisfy the printed nonempty-open-set, holomorphic, globally nonconstant, and idempotence assumptions. The map is not the identity on the second component. |
| 2025 main P4 | The displayed example meets the printed closed-curve and nowhere-zero-derivative conditions and passes through the origin. The displayed differential form is undefined there. This is a definition issue; no repair of the further regular-homotopy claim is certified. |

Visual source checking rejected an initial proposed open-ball counterexample for **2018 Individual P4**: the original formula visibly contains the **closed-ball overbar**, which text extraction had lost. The final catalog removes that defect flag and records only a separate notation clarification. This audit makes no broader defect or correctness verdict for that problem.

The three authored full solutions in this edition are separate from these observations and have their own independent review records.

## Final audited artifact versions

| File | SHA-256 |
| --- | --- |
| `catalogs/yau-analysis.json` | `893c89e42071fd2211fa3da6f9da6ff570512dae38e1ad910ae72e8e5f901479` |
| `catalogs/yau-analysis.md` | `5d7de35eac374678a8c899dfe195b3ca5ea7df9b8c8edac46fac0187f5f13173` |
| `catalogs/yau-source-manifest.json` | `32f6fad07477946f960b3050ad9f70f11294a28cd33138c0b0b67d8bab20dd3f` |
| `catalogs/yau-official-solutions.md` | `d29d0fb6206bb161ca044a1c7ede144c1bb18f399789f77c804d575cb16c0a70` |
| `catalogs/yau-source-issues.md` | `a7b15522958915339e9d6b38776f0fa5e56ca3c39178f2349f4ab2e622efe9ae` |

No substantive catalog file was edited by this reviewer. The initial collector draft, the independent findings, and the final corrections were handled separately. Material changes to coverage, source mappings, or mathematical observations require renewed review.
