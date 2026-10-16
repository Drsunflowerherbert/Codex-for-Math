# Regularity proof audit: source/access/search ledger

This is a bounded access log, not a comprehensive literature search. Source-copy filenames below refer to excluded reference material; no third-party PDF, scan or OCR is bundled. Related HPS source retrievals and exact pages are in `hps-searchlog.md`.

## Sources actually inspected

1. Demailly, *Complex Analytic and Differential Geometry*, exact title-page version 21 June 2012. Official PDF: https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf . Local `source/demailly-agbook-2012.pdf`, 3,557,990 bytes; SHA-256 `d7c7654a7417e8322e5dcf8fe8ec818b4c1a18cf280b41f2df5a871b776d89a1`. Chapter I, (3.29)(a), printed p.28, and following proof text expressly include distributions/currents. Narrow continuous-coefficient proof independently reconstructed in `regularity-proof-audit.md`.
2. Ghys 1995 author original, https://perso.ens-lyon.fr/ghys/articles/holomorphicanosov.pdf . Local `references/Ghys1995.pdf` and text; Lemma2.1 and Proposition2.2 checked in prior review. No new claim of independently proving Ghys's full quasiconformal argument here.
3. Baouendi–Rothschild–Winkelmann–Zaitsev research article, https://www.maths.tcd.ie/report_series/tcdmath/tcdm0413.pdf . Local `references/baouendi-et-al.pdf`. Theorem3.5 quotes a sufficient BM version with no nonidentity element fixing an open set pointwise. This corroborates statement/hypothesis coverage, not the BM original proof.
4. HPS original/author-provided material obtained by delegated reviewer; full source hashes, pagination caveat, published chapter comparison, and checked proof paragraphs are in `hps-searchlog.md` and `hps-foundations.md`.

## BM access attempts and limits

- https://www.jstor.org/stable/1969226 : bibliographic record accessible; no usable full proof returned through web tool.
- Prior JSTOR PDF attempt stored as `references/bochner-montgomery1946-attempt.html` is an HTML challenge response. It must not be treated as the paper PDF.
- https://annals.math.princeton.edu/1946/47-4/p04 : guessed publisher route inaccessible; not evidence about the original text.
- Ordinary web queries used exact title; Bochner/Montgomery/1946/639; BM theorem/open-set hypothesis; BM corrections/errata. Several returned irrelevant word matches. Their negative results are weak and not represented as exhaustive errata clearance.
- Last combined read-only exec attempted exact-title/differentiable-transformations searches, a BM correction query, then Scholar `get_open_access_work` for `doi:10.2307/1969226` (metadata only). The exec was reported **aborted without a result** with no output. It is not known which nested request was active at cancellation; no completed result is relied upon.

