:title: GEOMETOR • klein

GEOMETOR • klein
================

.. rubric:: Dual-Treatise Bilingual Book Codex & Exact Symbolic Engine for Felix Klein (1849–1925)

Critical 4-track bilingual digital Book Codices (*English · Deutsch · Summary · Notes*), calibrated ``.euclid-graphic`` vector figures, exact SymPy / :mod:`geometor.model` constructibility and transformation-group verifiers, and cross-corpus concordance for the two foundational geometric monographs of :person:`Felix Klein <klein>`:

1. :cite:`*Famous Problems of Elementary Geometry* (1895 / 1897) <klein:1897>` — Klein's Göttingen Easter 1895 lectures establishing the algebraic degree-$2^h$ criterion for straightedge-and-compass constructibility, the impossibility of duplicating the cube, trisecting a general angle, and constructing the regular heptagon ($n = 7$), the Poncelet–Steiner–von Staudt–Schröter single-circle straightedge construction of :person:`Gauss <gauss>`'s regular 17-gon, and :person:`Gordan <gordan>`'s algebraic proofs of the transcendence of $e$ (:person:`Hermite <hermite>`, 1873) and $\pi$ (:person:`Lindemann <lindemann>`, 1882).
2. :cite:`*A Comparative Review of Recent Researches in Geometry ("The Erlangen Program")* (1872 / 1893) <klein:1893:erlangen>` — Klein's inaugural Erlangen monograph reorganizing all of geometry as the :term:`invariant theory <invariant-theory>` of :term:`transformation groups <transformation-group>` acting on $n$-dimensional :term:`manifolds <manifold>`.

----

Primary Codices (*Opera Geometrica*)
------------------------------------

:doc:`Famous Problems of Elementary Geometry (1895 / 1897) <famous_problems/index>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Vorträge über ausgewählte Fragen der Elementargeometrie, ausgearbeitet von F. Tägert (Leipzig: B. G. Teubner, 1895) · Authorized English Translation by W. W. Beman & D. E. Smith (Boston & London: Ginn & Co., 1897).*

Synchronized **10-unit, 4-track Book Codex** (*English · Deutsch · Summary · Notes*) verified page-by-page against high-resolution 1895 Teubner and 1897 Ginn folio scans (strictly preserving 100% public-domain witnesses without post-1930 annotations):

* **Conspectus & Part I (Algebraic Constructibility)**: :ref:`Codex TOC <fp-index>` · :ref:`Prefaces & Introduction <fp-intro-en>` · :ref:`Part I, Ch. I: Square-Root Equations (§§ 1–15) <fp-part1-ch1-square-roots-en>` · :ref:`Ch. II: Delian Cube & Angle Trisection (§§ 1–3) <fp-part1-ch2-delian-trisection-en>` · :ref:`Ch. III: Cyclotomy & Fermat Primes (§§ 1–8) <fp-part1-ch3-cyclotomy-en>` · :ref:`Ch. IV: Regular 17-Gon & Fixed Circle (§§ 1–9) <fp-part1-ch4-heptadecagon-en>` · :ref:`Ch. V: Higher Curves & Instruments (§§ 1–5) <fp-part1-ch5-higher-constructions-en>`.
* **Part II (Transcendence of e and π)**: :ref:`Part II, Ch. I: Cantor's Algebraic Countability & Continuum (§§ 1–3) <fp-part2-ch1-cantor-en>` · :ref:`Ch. II: Historical Survey of π (§§ 1–5) <fp-part2-ch2-history-pi-en>` · :ref:`Ch. III: Hermite's Theorem on e (§§ 1–3) <fp-part2-ch3-hermite-e-en>` · :ref:`Ch. IV–V: Lindemann's Theorem on π & the Integraph <fp-part2-ch4-lindemann-pi-en>`.

:doc:`The Erlangen Program — Comparative Review of Recent Researches in Geometry (1872 / 1893) <erlangen_program/index>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Vergleichende Betrachtungen über neuere geometrische Forschungen (Erlangen: A. Deichert, 1872; Math. Annalen 43, 1893) · Authorized English Translation by M. W. Haskell (Bulletin of the New York Mathematical Society 2, July 1893, pp. 215–249).*

Synchronized **6-unit, 4-track Book Codex** (*English · Deutsch · Summary · Notes*) presenting Klein's complete group-theoretic architecture of geometry together with all seven historical and mathematical Notes (Notes I–VII):

* **Synchronized 4-Track Book Codex**: :ref:`Codex TOC <ep-index>` · :ref:`Prefatory Note & Introduction <ep-prefatory-intro-en>` · :ref:`§§ 1–2: Principal Group & Adjoined Hierarchy <ep-sec-01-02-principal-hierarchy-en>` · :ref:`§§ 3–5: Projective Geometry, Transference & Space-Elements <ep-sec-03-05-projective-transference-en>` · :ref:`§§ 6–7: Reciprocal Radii & Lie's Sphere Geometry <ep-sec-06-07-inversion-lie-spheres-en>` · :ref:`§§ 8–10: Birational, Topological, Contact & Manifold Groups <ep-sec-08-10-higher-groups-manifolds-en>` · :ref:`Notes I–VII (Non-Euclidean Cayley–Klein Metrics) <ep-notes-i-vii-en>`.

----

Cross-Corpus Apparatus & Exact Symbolic Modules
-----------------------------------------------

* :ref:`Master Cross-Corpus Concordance (Klein ↔ Euclid, Kepler, Hilbert, Russell, Hoenen, Lemoine, Petersen, Pappus & Wildberger) <concordance>`
* :ref:`Systematic Bibliography (36 Primary & Sister-Corpus Editions) <bibliography>` · :ref:`Prosopographical Index (52 Mathematicians & Philosophers) <persons>` · :ref:`Bilingual Technical Glossary (25 Terms) <glossary>`
* :doc:`Exact Symbolic Python API (geometor.klein) <modules/index>` — ``analyze_constructibility``, ``construct_gauss_17gon_periods`` (1-circle Poncelet–Steiner model with 0 floats), ``verify_erlangen_invariants``, and ``verify_cayley_klein_additivity``.
* :ref:`Provenance, Textual Witnesses & Methodology <about-index>`

.. toctree::
   :maxdepth: 2
   :hidden:

   famous_problems/index
   erlangen_program/index
   concordance
   bibliography
   persons
   glossary
   modules/index
   log/index
   about/index
