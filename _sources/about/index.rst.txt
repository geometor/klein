:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor.klein`` is a dual-treatise bilingual Digital Scriptorium Book Codex, semantic knowledge graph, and exact symbolic verification engine for two landmark geometric works of :person:`Felix Klein <klein>` (1849–1925): *Vorträge über ausgewählte Fragen der Elementargeometrie* (*Famous Problems of Elementary Geometry*, 1895 / 1897) and *Vergleichende Betrachtungen über neuere geometrische Forschungen* (*The Erlangen Program*, 1872 / 1893). Together, these works define modern geometric epistemology—unifying the classical Euclidean straightedge-and-compass paradigm through Galois-theoretic field extensions with the group-theoretic classification of geometry as invariant theory on manifolds.

The edition reconstructs both treatises into synchronized four-track **Book Codices** powered by ``photon-platform/publish``. Every chapter and paragraph offers track-preserving alignment across *English Translation* (verified against early authorized English editions), *German Source* (transcribed verbatim from nineteenth-century Teubner and Deichert editiones principes), *Executive Summaries* (concise algebraic, group-theoretic, and axiomatic synopses), and *Translation & Mathematical Notes* (scholarly apparatus linking nineteenth-century terminology to contemporary algebraic geometry). Every mathematical claim—from the algebraic non-constructibility of the Delian cube, general angle trisection, and regular heptagon, to Gordan's proofs of the transcendence of :math:`e` (Hermite) and :math:`\pi` (Lindemann)—is converted into machine-addressable semantic structures.

In strict adherence to the GEOMETOR ethos, mathematical claims are backed by executable symbolic verification in :mod:`geometor.model` and SymPy rather than numerical floats. The repository implements Klein's single-circle straightedge construction of Gauss's regular 17-gon over the exact cyclotomic field :math:`K_{16}`, and verifies the invariant properties of the Principal Similarity, Affine Shear, Projective Homography, and Möbius Inversion groups. This links ``geometor.klein`` directly to ``geometor.elements`` for axiomatic origins, ``geometor.hoenen`` for the philosophical epistemics of geometric intuition, and ``geometor.explorer`` for dynamic SVG visualization.

The GEOMETOR Mission
--------------------

The **GEOMETOR** initiative, conceived and directed by **phi ARCHITECT**, is dedicated to the systematic recovery, symbolic formalization, and creative re-articulation of humanity's geometric heritage. GEOMETOR unites classical synthesis with modern algebraic rigor across three core pillars:

Extracting Historical Semantic Knowledge
    Moving beyond passive page scans, static facsimile bitmaps, and flat optical character recognition (OCR), GEOMETOR recovers the living deductive architecture of 2,300+ years of geometric, axiomatic, and philosophical treatises. Primary sources—spanning Euclid, Apollonius, Archimedes, Pappus, Johannes Kepler, Felix Klein, and Clark Kimberling—are analyzed to elevate enunciations, deductive steps, synthetic justifications, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs.

Exact Symbolic Grounding (``geometor.model``)
    Geometric constructions must not depend on floating-point approximations or visual artifacts. GEOMETOR anchors geometric entities in 100% exact symbolic algebra via `SymPy <https://www.sympy.org/>`_ and the principles of Rational Trigonometry (quadrance, spread, cross-ratio). Points, lines, circles, and conic loci are evaluated over exact algebraic fields, ensuring that tangencies, incidences, harmonic conjugates, and collinearities represent absolute mathematical truths rather than numerical estimates.

Repurposing Knowledge Across Mediums
    Extracted semantic architectures and exact symbolic models are re-deployed across a unified digital ecosystem: synchronized multi-track **Book Codices** and EPUB 3 editions powered by ``photon-platform/publish``, computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG exploration laboratories (``geometor.explorer``), ultra-high-definition visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

Primary Public-Domain Witnesses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **1895 German Editio Princeps of Famous Problems (B. G. Teubner, Leipzig)**: *Vorträge über ausgewählte Fragen der Elementargeometrie*, ausgearbeitet von :person:`F. Tägert <taegert>`, eine Festschrift zu der Pfingsten 1895 in Göttingen stattfindenden dritten Versammlung des Vereins zur Förderung des mathematischen und naturwissenschaftlichen Unterrichts (v + 66 S., mit 10 in den Text gedruckten Figuren und 2 lithographierten Tafeln). Transcribed and verified by page-by-page 300-DPI multimodal scan inspection.
* **1897 Authorized English Edition of Famous Problems (Ginn & Company, Boston & London)**: *Famous Problems of Elementary Geometry: The Duplication of the Cube, The Trisection of an Angle, The Quadrature of the Circle*, translated by :person:`Wooster Woodruff Beman <beman>` and :person:`David Eugene Smith <smith>` (ix + 80 pp.). Verified page-by-page against the 1897 Ginn folio scans. *(Rights note: R. C. Archibald's 1930/1956 supplementary bibliographic notes are strictly excluded; only the pure 1895/1897 public-domain treatises are included.)*
* **1872 German Editio Princeps of the Erlangen Program (Andreas Deichert, Erlangen)**: *Vergleichende Betrachtungen über neuere geometrische Forschungen: Programm zum Eintritt in die philosophische Facultät und den Senat der k. Friedrich-Alexanders-Universität zu Erlangen* (1872; reprinted with minor authorial note in *Mathematische Annalen* 43, 1893, pp. 63–100; Project Gutenberg ``#38033``).
* **1893 Authorized English Edition of the Erlangen Program (NYMS Bulletin)**: *A Comparative Review of Recent Researches in Geometry*, translated by :person:`Mellen Woodman Haskell <haskell>` with Klein's 1893 Prefatory Note (*Bulletin of the New York Mathematical Society* 2, July 1893, pp. 215–249; ``arXiv:0807.3161``).

Content / Code Separation & Exact Symbolic Verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In accordance with GEOMETOR Digital Scriptorium standards, zero executable Python scripts are embedded inside ``resources/``. All exact symbolic algebra and geometric constructions reside in ``src/geometor/klein/`` and ``demos/``:

* :mod:`geometor.klein.constructibility` — Exact SymPy Gauss–Wantzel polygon classifier, irreducible polynomial degree-:math:`2^h` & quartic cubic-resolvent Galois test, and Hermite–Lindemann transcendence diagnostics.
* :mod:`geometor.klein.heptadecagon` — Exact cyclotomic field canonicalizer over :math:`K_{16} = K_8(\sin\frac{2\pi}{17})` and Klein's von Staudt–Schröter single-circle straightedge construction of all 17 exact vertices ``V0``..``V16`` inside :class:`geometor.model.Model` (``len(model.circles) == 1``, ``0`` floating-point coordinates).
* :mod:`geometor.klein.erlangen` — Exact rational verification of invariants preserved and broken across the Principal Similarity Group, Affine Shear Group, Projective Homography Group, and Möbius Reciprocal-Radii Inversion Group, together with Cayley–Klein logarithmic cross-ratio additivity.
