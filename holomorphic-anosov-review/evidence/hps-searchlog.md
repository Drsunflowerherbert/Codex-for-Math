# HPS source acquisition and bounded search log

Date: 16 October 2026. Private read-only source research; no contact, account changes, installs, or public writes.

## Acquired sources

| Source | Action and outcome | Local evidence |
|---|---|---|
| HPS1977, publisher DOI 10.1007/BFb0092042 | Opened publisher catalogue and relevant chapter records. Full content requires subscription there. | URLs in notes; publisher confirms authors, 1977, LNM583, and chapter ranges |
| [Complete HPS scan, UC eScholarship](https://escholarship.org/content/qt6m58s433/qt6m58s433_noSplash_8a35f009e454419ac236b82dfae5a96c.pdf) | HTTP GET succeeded, application/pdf, 3,613,746 bytes, 154 pages. | `HirschPughShub1977.pdf`, SHA256 `7a192838a2c5b84c34ac7ec200c242fed5728c3573dde2cdde75ce96c5d0dfc9` |
| HPS published §5, DOI 10.1007/BFb0092047 | Read author-uploaded original PDF through web tool. Morris Hirsch upload provenance is visible on ResearchGate publication 317569958 (13 June 2017). Corrected ResearchGate's malformed relative download link by removing the extra `publication/` segment. | [PDF](https://www.researchgate.net/profile/Morris-Hirsch/publication/317569958_Pseudo_hyperbolicity_and_plaque_families/links/594031150f7e9ba171b23704/Pseudo-hyperbolicity-and-plaque-families.pdf); UC corresponding page renders/OCR |
| HPS published §3, DOI 10.1007/BFb0092045 | Read author-uploaded original PDF through web tool, especially pp.25–31. | [PDF](https://www.researchgate.net/profile/Morris-Hirsch/publication/317568690_The_Cr_section_theorem_and_lipschitz_jets/links/59401769aca272371224cfad/The-Cr-section-theorem-and-lipschitz-jets.pdf) |
| Pugh–Shub–Wilkinson, arXiv:1112.2646v2 | HTTP GET succeeded, 1,826,437 bytes, 53 pages. Read Introduction, relevant §3/§4 discussion, and §11 cautionary remarks. | `PughShubWilkinson2012-holder.pdf` and text; SHA256 `794ae975ba281376c57c92dfe49e05ef067654355d75d18e4c918759eb8fa79c` |

The UC scan is image-only: `pdftotext` yielded page separators. I rendered and OCRed selected PDF pages 6–11, 59–69, 115–120, 131–140, using installed PyMuPDF/Tesseract. Relevant formulae and wording at PDF pp.65–68 were visually inspected as well. The scan's contents-table page labels are inconsistent with the publisher's chapter ranges; published §5 explicitly confirms the printed p.61/p.62 references corresponding to UC PDF66/PDF67.

## Failed or partial access, with exact status

- **Action:** HTTP GET of the 1970 AMS announcement at `https://www.ams.org/journals/bull/1970-76-05/S0002-9904-1970-12596-5/S0002-9904-1970-12596-5.pdf`. **Outcome:** HTTP403, no PDF obtained. No retry after that denial. This is no longer a substantive blocker because the 1977 original is accessible.
- **Action:** GET `https://link.springer.com/content/pdf/10.1007/BFb0092047.pdf`. **Outcome:** HTTP200 **HTML**, redirected to a chapter page reporting unsupported cookies; not a PDF. Saved as `hps-springer-chapter.html`, not treated as the original.
- **Action:** GET the correct ResearchGate §5 PDF URL locally. **Outcome:** HTTP403, local PDF not obtained. The independent web-reader action successfully read its 12 PDF pages, so the contents were checked; no source hash for that remote chapter is claimed.
- Author homepages: Berkeley Pugh URL returned HTTP403; guessed Berkeley Hirsch and Toronto Shub URLs returned404/inaccessible. No protected access was attempted.
- UC item landing page required JavaScript/robot verification in the web reader. The openly linked PDF URL succeeded directly; no challenge was bypassed.
- A child-agent independent errata-search delegation was attempted but could not start because the team thread limit had been reached. The mathematical audit and searches were completed by this reviewer.

## Bounded errata/counterexample searches

Representative queries included:

- `Hirsch Pugh Shub Invariant Manifolds 1977 pdf stable manifolds theorem`
- `"Hirsch Pugh Shub" "pdf"`
- `"Pseudo hyperbolicity and plaque families"`
- `"Hirsch" "Pugh" "Shub" "errata"`
- `"HPS" "errata" manifolds`
- `"Hirsch-Pugh-Shub" "gap"`
- `"Hirsch-Pugh-Shub" "counterexample" stable`
- `"Invariant Manifolds" errata site:math.berkeley.edu`
- `"Invariant Manifolds" erratum site:arxiv.org`
- `"Hirsch-Pugh-Shub" error site:arxiv.org`

No primary correction invalidating the ordinary Anosov stable-plaque theorem was found. Many searches returned generic/unrelated results, limiting the evidential weight of a negative search. No claim of exhaustive errata coverage is made.

The meaningful primary follow-up found was Pugh–Shub–Wilkinson's paper. It discusses stronger transverse Hölder claims and their additional hypotheses. It does not contradict the continuous leafwise \(C^1\) plaque dependence needed in Zhang Lemma2.5. The notes also record HPS's own explicit distinction between a smooth lamination and a smooth foliation.

## Result

No mathematical or source-access blocker remains for the assigned ordinary HPS foundations. The full differentiable-section/jet theorem remains an accepted external theorem after statement/use inspection; not every line of that theorem was independently re-proved. The global unstable-holonomy completeness step remains assigned elsewhere.

