# Schweitzer catalog self-audit

Audit date: 13 October 2026 UTC, initially completed at 04:44 UTC and revised at 04:45 UTC after an independent reviewer correction. This is a bounded **self-audit by the metadata author**, not an independent review. The root agent is separately cross-checking the catalog. This audit checks source fidelity, coverage accounting, and public-content scope; it does **not** review the correctness of third-party mathematical proofs.

## Measured coverage

| Measure | Result |
|---|---:|
| Year-level records | 17: 2009–2025 |
| Downloaded archived PDF documents | 23 |
| Years with observed numbered statements | 16 |
| Observed statement numbers | 171 |
| Additional problems reported, statements not located | 11, all in 2012 |
| Sum of observed and reported-only counts | 182 |
| Detailed topic/prerequisite entries | 42: 2022–2025 |
| Observed organizer/official solution numbers | 160, across 15 years |
| Observed organizer-hosted explicitly unofficial solution numbers | 11, all in 2023 |
| Archived years whose solution version is marked preliminary official | 2: 2022 and 2024 |
| Authored Schweitzer proofs in this edition | 0 |
| 2026 problem, solution, hint, or submission records | 0 |

| Year | Observed statements | Reported-only count | Detailed entries |
|---|---:|---:|---:|
| 2009 | 12 | 0 | 0 |
| 2010 | 11 | 0 | 0 |
| 2011 | 10 | 0 | 0 |
| 2012 | 0 | 11 | 0 |
| 2013 | 12 | 0 | 0 |
| 2014 | 11 | 0 | 0 |
| 2015 | 11 | 0 | 0 |
| 2016 | 10 | 0 | 0 |
| 2017 | 10 | 0 | 0 |
| 2018 | 11 | 0 | 0 |
| 2019 | 10 | 0 | 0 |
| 2020 | 11 | 0 | 0 |
| 2021 | 10 | 0 | 0 |
| 2022 | 10 | 0 | 10 |
| 2023 | 11 | 0 | 11 |
| 2024 | 11 | 0 | 11 |
| 2025 | 10 | 0 | 10 |

## Source-fidelity checks

Every referenced source-document identifier resolves to a document of the corresponding year. All 23 document URLs point to the organizer's `www.bolyai.hu/files/` archive. Downloaded bytes and recorded SHA-256 hashes were compared against the private research copies. No 2026 PDF is among these documents. The hub snapshot was retrieved at `2026-10-13T04:38:29.126044+00:00`; its hash is recorded in the metadata.

The four detailed standalone papers were re-extracted and their distinct statement headings compared against the catalog: 2022 has 1–10, 2023 has 1–11, 2024 has 1–11, and 2025 has 1–10. Earlier combined papers were inspected for their numbered statement and solution sections. PDF text extraction sometimes splits headings across lines; this is why a simple line-count was not used to infer coverage. The original numbering and source papers remain authoritative.

The [2012 source](https://www.bolyai.hu/files/Schweitzer_2012_jelentes.pdf) is a two-page results report. It says 11 problems were selected but does not provide their statements or solutions. Its catalog record therefore has zero observed statements, no problem URL, and a solution status limited to “not located in inspected archive.” This does not assert that official 2012 materials do not exist elsewhere.

The [2023 solution document](https://www.bolyai.hu/files/Schweitzer_2023_elozetes_megoldasok.pdf) explicitly calls its solutions unofficial. Organizer hosting has not been converted into a claim of official status. The 2022 and 2024 preliminary qualifications are retained; their archived English problem papers explicitly describe preliminary official Hungarian solutions. The other organizer/committee reports are identified by provenance, with no claim that their proofs were independently checked.

The 2019 filename is marked corrected and the 2022 solution filename modified. These are version-provenance flags only: this edition does not invent a specific erratum or claim to have compared prior versions. The [2025 solution document](https://www.bolyai.hu/files/SCHWEITZER_2025_MEGOLDAS.pdf), page 4, reports a wording defect in Problem 3 involving bases equal to 1. That issue is recorded separately. The original positive-integer conditions have not been silently strengthened.

An independent source check by the Jarník/IMC archive agent identified an additional wording warning for 2023 Problem 8. I re-read the organizer-hosted unofficial solution document on printed page 13 and confirmed the warning. The catalog now records its unofficial source qualification in a separate errata record and flags 2023/8 in the default problem index. No counterexample, solution, or silently repaired statement was copied. This independent correction does not make the remainder of this self-audit independent.

All 42 difficulty values were normalized to the shared taxonomy: advanced-undergraduate preparation maps to **advanced**, and early-graduate/graduate preparation maps to **very advanced**. The original preparation descriptions remain in the separate `preparation_estimate` field. These are editorial preparation estimates, not official contest ratings.

## Public-content and spoiler checks

The three public catalog files contain source URLs, numbering, short editorial topic labels, prerequisites, difficulty estimates, and provenance. They contain no third-party PDF bytes and no full problem-statement or solution-text fields. No full problem compilation is reproduced. A scan found no email addresses or credential-token patterns in these files.

The default Markdown catalog links only the standalone problem papers for 2022–2025. Earlier documents that combine statements with answers are linked from the separate solution-link index. The machine-readable metadata retains solution URLs for provenance and marks combined sources as answer-bearing; a renderer must continue to suppress these links from default problem browsing. The catalog itself contains no hints or authored proofs.

The 2026 hub notice is cited solely to document the no-AI/current-program exclusion. No 2026 program problem or submission was retrieved, indexed, solved, or reproduced. The archived competition windows have ended, but this has not been treated as a public redistribution license. No explicit redistribution license was located in the inspected hub or PDFs. The 23 personal research copies remain outside the repository.

## Limitations

Years before 2009 are not covered. The actual 2012 statements and solutions remain missing. Detailed subject classification before 2022 is not included. An official 2023 solution version was not located in the inspected hub. No earlier-version comparison, complete website-wide licensing investigation, exhaustive search for every possible official solution, or mathematical proof review is claimed. Topics, prerequisites, and difficulty are editorial judgments.

Audited files: [schweitzer.json](../catalogs/schweitzer.json), [schweitzer.md](../catalogs/schweitzer.md), and [schweitzer-solutions.md](../catalogs/schweitzer-solutions.md).
