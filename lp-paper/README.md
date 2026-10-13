# Linear Programming by Sparse Certificates

A 14-page English expository paper about the completed linear-programming
certificate research, with full ordinary proofs, a deterministic exact hand
algorithm, worked examples, and explicit testing and formal-verification limits.

- [Read the PDF](sparse-lp-certificates.pdf)
- [Editable LaTeX source](sparse-lp-certificates.tex)
- [Review and rendering evidence](REVIEW.md)
- [Artifact SHA-256 values](SHA256SUMS)

The research basis is repository commit
`e4f337c3aa52ec4c3f2aab078d7c91b32ee0015f`, especially
`lp-sparse-discovery/`, `lp-certificates/notes/mathematics.md`, and the
October 13 publication report. The paper synthesizes those completed results;
it introduces no new LP algorithm or general performance claim over simplex.
The support and existence arguments are ordinary mathematics. The selected
Lean results concern certificate soundness, with their documented trust boundary.

To compile with a standard TeX Live or MiKTeX installation and the packages
listed in the source:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error sparse-lp-certificates.tex
```

The distributed PDF was built with pdfTeX 1.40.26 and TeX Live 2025/dev. All fonts
are embedded. PDF metadata can vary across compilations; the supplied checksum
identifies the reviewed distributed PDF, not all future builds from the source.

This directory is an isolated paper deliverable. Existing research proofs,
code, notices, and publication manifests are preserved. It assigns no new
repository or third-party license. References are linked; third-party PDFs,
images, dependency sources, and private archives are not redistributed.
