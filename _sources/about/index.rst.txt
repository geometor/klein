:navigation: footer
:order: 10

.. _about-index:

about
=====

Historical, philological, and symbolic-verification provenance for ``geometor.klein``.

Primary Public-Domain Witnesses
-------------------------------

* **1895 German Editio Princeps of Famous Problems (B. G. Teubner, Leipzig)**: *Vorträge über ausgewählte Fragen der Elementargeometrie*, ausgearbeitet von :person:`F. Tägert <taegert>`, eine Festschrift zu der Pfingsten 1895 in Göttingen stattfindenden dritten Versammlung des Vereins zur Förderung des mathematischen und naturwissenschaftlichen Unterrichts (v + 66 S., mit 10 in den Text gedruckten Figuren und 2 lithographierten Tafeln). Transcribed and verified by page-by-page 300-DPI multimodal scan inspection.
* **1897 Authorized English Edition of Famous Problems (Ginn & Company, Boston & London)**: *Famous Problems of Elementary Geometry: The Duplication of the Cube, The Trisection of an Angle, The Quadrature of the Circle*, translated by :person:`Wooster Woodruff Beman <beman>` and :person:`David Eugene Smith <smith>` (ix + 80 pp.). Verified page-by-page against the 1897 Ginn folio scans. *(Rights note: R. C. Archibald's 1930/1956 supplementary bibliographic notes are strictly excluded; only the pure 1895/1897 public-domain treatises are included.)*
* **1872 German Editio Princeps of the Erlangen Program (Andreas Deichert, Erlangen)**: *Vergleichende Betrachtungen über neuere geometrische Forschungen: Programm zum Eintritt in die philosophische Facultät und den Senat der k. Friedrich-Alexanders-Universität zu Erlangen* (1872; reprinted with minor authorial note in *Mathematische Annalen* 43, 1893, pp. 63–100; Project Gutenberg ``#38033``).
* **1893 Authorized English Edition of the Erlangen Program (NYMS Bulletin)**: *A Comparative Review of Recent Researches in Geometry*, translated by :person:`Mellen Woodman Haskell <haskell>` with Klein's 1893 Prefatory Note (*Bulletin of the New York Mathematical Society* 2, July 1893, pp. 215–249; ``arXiv:0807.3161``).

Content / Code Separation & Exact Symbolic Verification
-------------------------------------------------------

In accordance with GEOMETOR Digital Scriptorium standards, zero executable Python scripts are embedded inside ``resources/``. All exact symbolic algebra and geometric constructions reside in ``src/geometor/klein/`` and ``demos/``:

* :mod:`geometor.klein.constructibility` — Exact SymPy Gauss–Wantzel polygon classifier, irreducible polynomial degree-$2^h$ & quartic cubic-resolvent Galois test, and Hermite–Lindemann transcendence diagnostics.
* :mod:`geometor.klein.heptadecagon` — Exact cyclotomic field canonicalizer over $K_{16} = K_8(\sin\frac{2\pi}{17})$ and Klein's von Staudt–Schröter single-circle straightedge construction of all 17 exact vertices ``V0``..``V16`` inside :class:`geometor.model.Model` (``len(model.circles) == 1``, ``0`` floating-point coordinates).
* :mod:`geometor.klein.erlangen` — Exact rational verification of invariants preserved and broken across the Principal Similarity Group, Affine Shear Group, Projective Homography Group, and Möbius Reciprocal-Radii Inversion Group, together with Cayley–Klein logarithmic cross-ratio additivity.
