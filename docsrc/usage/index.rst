:navigation: header
:order: 20
:nav_title: Usage

.. _klein-usage:

Using This Edition
==================

.. rubric:: Reader's Guide to the GEOMETOR Interactive Digital Edition

Welcome to the **GEOMETOR Klein** digital edition. This interactive edition unites Felix Klein's two monumental geometric works—*Famous Problems of Elementary Geometry* (1895 / 1897) and *The Erlangen Program* (1872 / 1893)—with primary German source texts, authorized English translations, analytical summaries, critical notes, and exact symbolic Python verification.

Synchronized Reading Tracks
---------------------------

Every chapter across both Book Codices (:doc:`/famous_problems/index` and :doc:`/erlangen_program/index`) is presented in four synchronized reading tracks:

* **English (`-en`)**: Authorized English translations by W. W. Beman & D. E. Smith (1897) and M. W. Haskell (1893).
* **German (`-de`)**: Original German edition texts edited from F. Tägert (1895) and Andreas Deichert / *Mathematische Annalen* (1872 / 1893).
* **Summary (`-summary`)**: Compact mathematical distillations isolating algebraic theorems, group hierarchies, and field extensions.
* **Notes (`-notes`)**: Scholarly commentary detailing philological context, geometric proofs, and connections to modern algebra and physics.

Toggle between tracks anytime using the track buttons in the book header bar at the top of each chapter page.

Primary-Source Folio Milestones
-------------------------------

This digital edition strictly relies on public-domain first editions and authoritative contemporary translations:

* ***Famous Problems of Elementary Geometry* (1895 / 1897)**:
  * German First Edition: *Vorträge über ausgewählte Fragen der Elementargeometrie*, ausgearbeitet von F. Tägert (Leipzig: B. G. Teubner, 1895).
  * Authorized English Translation: Translated by Wooster Woodruff Beman and David Eugene Smith (Boston & London: Ginn & Company, 1897).
* ***The Erlangen Program* (1872 / 1893)**:
  * German Inaugural Edition: *Vergleichende Betrachtungen über neuere geometrische Forschungen* (Erlangen: Andreas Deichert, 1872; *Mathematische Annalen* 43, 1893).
  * Authorized English Translation: Translated by Mellen Woodman Haskell (*Bulletin of the New York Mathematical Society* 2, 1893).

Interactive Diagrams & Deductive Links
--------------------------------------

The edition incorporates interactive vector figures and symbolic verification:

* **Geometric Elements (``:g:``)**: In-text geometric labels connect to construction lines, points, and conics.
* **Equations & Invariants (``:eq:``)**: Track invariant polynomials, cross-ratios, and minimal polynomials over algebraic number fields.
* **Justifications (``:just:``)**: Inline citations link algebraic steps to Euclidean postulates, Galois theory, or Cayley's projective metric foundations.

Full-Text Search with In-Page Highlighting
------------------------------------------

The built-in documentation search engine indexes all units, commentary notes, and module documentation.
Search queries pass search terms via `?highlight=`, highlighting queried expressions throughout the text.

Categories, Tags & Collection Views
-----------------------------------

Explore content through structured taxonomies:

* Filter treatises, notes, and logs by mathematical subject, historical era, or tag using the sidebar facets.
* On collection index pages like :doc:`/log/index`, use the view toggle buttons to display entries as **Cards**, **Banners**, or **Lists**.

People, Bibliography & Glossary Tooltips
----------------------------------------

Rich interconnected registers provide immediate context:

* **People (``:person:``)**: Hover or click names like :person:`Sophus Lie <lie>`, :person:`David Hilbert <hilbert>`, or :person:`Carl Friedrich Gauss <gauss>` to open detailed biographies in :doc:`/people/index`.
* **Citations (``:cite:``)**: Citations connect directly to full bibliographical records in :doc:`/bibliography`.
* **Terms (``:term:``)**: Foundational concepts like :term:`group of transformations <transformation-group>`, :term:`manifold <manifold>`, and :term:`reciprocal radii <reciprocal-radii>` link to definitions in :doc:`/glossary`.
* **Display Themes**: Switch between Light and Dark display modes using the theme toggle in the header navigation bar.

Command-Line & Python API
-------------------------

The companion package ``geometor.klein`` provides exact symbolic verifiers powered by SymPy:

.. code-block:: bash

   # Run CLI help and inspect available verifiers
   /home/phi/PROJECTS/geometor/.venv/bin/python -m geometor.klein --help

   # Run test suite
   /home/phi/PROJECTS/geometor/.venv/bin/pytest

Explore the complete API reference in :doc:`/modules/index`.
