# Independent Schweitzer catalog audit

Accepted after correction on 2026-10-13 at 04:46 UTC. Reviewer: the Jarník/IMC archive agent, independent of the Schweitzer metadata author. This bounded audit covers source identity, numbering, coverage accounting, availability labels, source-reported wording warnings and publication scope. It does not review the mathematics in third-party solutions.

## Coverage and numbering

I re-extracted the 23 private archived PDFs with `pdftotext -layout`, compared numbered statement sections with the year records, and inspected split headings that a simple regular expression missed. The 2009 Problem 5, 2017 Problem 8 and 2018 Problem 3 headings are split by PDF text layout; they are present and are not coverage gaps. The four detailed standalone problem papers reproduce the catalog's problem numbers and page assignments exactly.

| Year | Observed statement numbers | Detailed entries |
| --- | --- | ---: |
| 2009 | 1–12 | 0 |
| 2010 | 1–11 | 0 |
| 2011 | 1–10 | 0 |
| 2012 | None in retrieved report; 11 reported only | 0 |
| 2013 | 1–12 | 0 |
| 2014 | 1–11 | 0 |
| 2015 | 1–11 | 0 |
| 2016 | 1–10 | 0 |
| 2017 | 1–10 | 0 |
| 2018 | 1–11 | 0 |
| 2019 | 1–10 | 0 |
| 2020 | 1–11 | 0 |
| 2021 | 1–10 | 0 |
| 2022 | 1–10 | 10 |
| 2023 | 1–11 | 11 |
| 2024 | 1–11 | 11 |
| 2025 | 1–10 | 10 |

The totals are 17 year records, 171 observed statement numbers and 42 detailed entries. The 11 reported-only 2012 problems are additional, so 182 is an observed-plus-reported count, not 182 accessible statements. The solution-number totals are 160 organizer/committee numbers across 15 years and 11 explicitly unofficial numbers in 2023. No authored Schweitzer proof is included.

## Requested source checks

The [2012 report](https://www.bolyai.hu/files/Schweitzer_2012_jelentes.pdf) has two pages, reports that the committee selected 11 problems, and then gives results. It contains no numbered problem statements or solution sections. The metadata correctly records zero observed statements and limits the missing-source conclusion to the inspected archive. It does not claim that official materials do not exist elsewhere.

The title of the [2023 solution document](https://www.bolyai.hu/files/Schweitzer_2023_elozetes_megoldasok.pdf) contains “nem hivatalos,” meaning unofficial. That qualification is retained in the metadata and separate solution register. Its presence on the organizer's website has not been treated as proof of official status.

The [2024 English question paper](https://www.bolyai.hu/files/Schweitzer_2024_Feladatsor_angol.pdf) has exactly Problems 1–11, all on page 1; page 2 gives instructions. I visually checked page 1. Its instructions explicitly identify the later Hungarian solution publication as preliminary official. The catalog preserves that qualification instead of presenting it as a final reviewed version.

The [2025 solution document](https://www.bolyai.hu/files/SCHWEITZER_2025_MEGOLDAS.pdf), printed page 4, identifies a wording defect in Problem 3. I visually checked that page. The existing separate errata record describes the source warning, while the problem index keeps the original positive-integer conditions and flags the issue. No silent strengthening of the statement is made.

## Correction found and resolved

The original draft missed a further source-reported wording issue for 2023 Problem 8. On printed page 13 of the organizer-hosted unofficial solution document, a note explicitly says that the original problem was imprecisely posed. I checked the extracted text and rendered page. I notified the metadata author and parent, and the author added a source-qualified separate errata record, a Problem 8 status flag, and a warning in the default index. The source remains labeled unofficial. The counterexample and a repaired formulation are not reproduced in the catalog.

The difficulty values were also normalized to the collection's canonical vocabulary. The final metadata has 14 **advanced** and 28 **very advanced** entries; the earlier preparation descriptions are retained in `preparation_estimate`. These are editorial judgments, not official ratings. I checked the corrected files before acceptance.

## Provenance, spoilers and publication scope

All 23 PDF SHA-256 hashes and byte counts match the private research files. The official hub HTML snapshot hash also matches its record. Retrieval timestamps, organizer URLs and private local research paths are recorded. Every source-document year is at most 2025; I did not inspect any 2026 program problem or submission.

The default Markdown catalog's four direct PDF links open standalone question papers for 2022–2025. Answer-bearing older reports and modern solution documents are linked from the separate solution register. The JSON contains solution URLs and errata provenance for explicit metadata inspection; a future renderer must keep those out of default problem browsing.

The three public Schweitzer catalog files contain original editorial labels and metadata, with no full problem-statement/solution text fields or third-party PDF bytes. No PDF is present anywhere in the `contest-library/` worktree at this check. Credential-token and email-pattern scans of these three files returned no matches. The metadata does not claim a redistribution license or infer one from public access. Authorized research copies remain under `/tmp/contest-library-research/schweitzer/`, outside the repository.

## Final artifact identity and limits

These hashes identify the corrected artifacts accepted by this reviewer:

| File | SHA-256 |
| --- | --- |
| `catalogs/schweitzer.json` | `4c303e05f103cfdff41026945fd44392d0019ddd30b8929babf34af00606c8d3` |
| `catalogs/schweitzer.md` | `333d269a76d71b9c276ab9a3e03d361a9fd94caa97f94b66bca3c42961c0a2fd` |
| `catalogs/schweitzer-solutions.md` | `ac92c88816209e9f817968d00f2d9c8cd58464b1d7fb8803b46b0423ae6f4909` |

No blocking issue remains in this bounded metadata audit. Years before 2009, actual 2012 statements/solutions, detailed classifications before 2022 and an official 2023 solution version remain outside or missing from the catalog. This audit does not establish exhaustive archive coverage, validate third-party mathematical proofs, compare all earlier versions or provide formal verification.
