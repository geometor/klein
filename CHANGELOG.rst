=========
changelog
=========

0.1.2 (2026-11-14)
------------------

- Standardized top-level ``About`` page (``docsrc/about/index.rst`` promoted to top header ``:order: 10``) with the three-pillar GEOMETOR semantic-extraction mission and archival provenance; retired ``docsrc/mission/`` stubs cleanly into Home and ``About``.

0.1.1 (2026-11-14)
------------------

- Standardized Book Title Page, top-level header navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author and Translator profiles in People, and English structural terminology.

0.1.0 (2026-11-12)
------------------

* Establish dual-treatise 4-track bilingual Book Codex (``English · Deutsch · Summary · Notes``, 64 RST track files across 16 units) for Felix Klein's *Famous Problems of Elementary Geometry* (1895 Teubner DE ed. F. Tägert / 1897 Ginn & Co. EN trans. W. W. Beman & D. E. Smith, strictly public-domain) and *The Erlangen Program* (1872 Deichert DE / 1893 NYMS *Bulletin* EN trans. M. W. Haskell).
* Implement ``geometor.klein`` exact symbolic package (``constructibility``, ``heptadecagon``, ``erlangen``, ``codex``, and ``geometor-klein`` CLI with ``--json`` diagnostics) targeting Python ``>=3.13`` with zero ``float`` / ``sp.Float`` coordinates in ``geometor.model.Model``.
* Realize Gauss's quadratic period tower and the von Staudt–Schröter Poncelet–Steiner single-circle straightedge construction of all 17 exact regular heptadecagon vertices ``V0``..``V16`` on $C_0: x^2 + y(y - 2) = 0$ (``len(model.circles) == 1``).
* Generate 10 theme-adaptive ``.euclid-graphic`` SVG figures across *Famous Problems* and *The Erlangen Program*, wired via ``.. picture::`` directives.
* Curate bilingual apparatus (``persons.json``, ``citations.json``, ``glossary.json``, ``concordance.json``, ``sources_manifest.json``) linking ``geometor/klein`` across 9 GEOMETOR sister corpora (``euclid``, ``kepler``, ``hilbert``, ``bertrand-russell``, ``hoenen``, ``lemoine``, ``petersen``, ``pappus``, ``wildberger``).
