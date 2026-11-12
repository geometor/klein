# GEMINI.md — `geometor/klein`

## Purpose

`geometor/klein` (`geometor-klein`) is the dual-treatise bilingual **Book Codex** and exact symbolic algebra / transformation-group engine for **Felix Klein** (1849–1925) within the GEOMETOR ecosystem:

1. **Book 1 — *Famous Problems of Elementary Geometry* (`docsrc/famous_problems/`)**:
   * **1895 German *Editio Princeps***: *Vorträge über ausgewählte Fragen der Elementargeometrie*, ausgearbeitet von F. Tägert (Leipzig: B. G. Teubner, 1895).
   * **1897 Authorized English Edition**: *Famous Problems of Elementary Geometry*, trans. W. W. Beman & D. E. Smith (Boston & London: Ginn & Co., 1897; strictly public-domain, excluding post-1930 R. C. Archibald notes).
2. **Book 2 — *The Erlangen Program* (`docsrc/erlangen_program/`)**:
   * **1872 German *Editio Princeps***: *Vergleichende Betrachtungen über neuere geometrische Forschungen* (Erlangen: Andreas Deichert, 1872; *Mathematische Annalen* 43, 1893).
   * **1893 Authorized English Edition**: *A Comparative Review of Recent Researches in Geometry*, trans. M. W. Haskell (*Bulletin of the New York Mathematical Society* 2, 1893).

## Key Modules (`src/geometor/klein/`)

* **`constructibility.py`**: Exact SymPy Gauss–Wantzel regular polygon classifier ($\varphi(n) = 2^k$, Fermat primes), real cyclotomic minimal polynomials $\psi_n(u)$ for $u = 2\cos(2\pi/n)$, Klein's degree-$2^h$ & depressed cubic-resolvent Galois test, and Hermite–Lindemann transcendence diagnostics.
* **`heptadecagon.py`**: Exact cyclotomic field engine `_K16Engine` (`canonicalize_17`) and Poncelet–Steiner single-circle straightedge construction (`construct_gauss_17gon_periods`) of all 17 exact regular heptadecagon vertices `V0`..`V16` on $C_0: x^2 + y(y - 2) = 0$ inside `geometor.model.Model` (`len(model.circles) == 1`, zero `sp.Float` atoms).
* **`erlangen.py`**: Exact rational invariant audit (`verify_erlangen_invariants`) across the Principal Similarity, Affine Shear, Projective Collineation, and Möbius Reciprocal-Radii Inversion groups, plus symbolic Cayley–Klein logarithmic cross-ratio distance additivity (`verify_cayley_klein_additivity`).
* **`codex.py`**: Structural verifier (`audit_codex`) for all 64 4-track RST files, apparatus JSON catalogs (`persons.json`, `citations.json`, `glossary.json`, `concordance.json`), and strict content/code separation (`0` `.py` files in `resources/`).
* **`__main__.py`**: CLI entry point `geometor-klein` (`polygons`, `heptadecagon`, `erlangen`, `audit`, with `--json` support).

## Verification Workflows

* **Lint**: `/home/phi/.local/bin/ruff check src demos tests docsrc/conf.py`
* **Unit Tests**: `/home/phi/PROJECTS/geometor/.venv/bin/python -m pytest tests`
* **Build Codex**: `/home/phi/.local/bin/publish build`
