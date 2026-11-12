=====
klein
=====

**Dual-treatise bilingual Book Codex and exact symbolic constructibility & Erlangen transformation-group engine for Felix Klein's Famous Problems of Elementary Geometry (1895 / 1897) and The Erlangen Program (1872 / 1893).**

.. image:: docsrc/_static/figures/fig_von_staudt_17gon.svg
   :alt: Complete Poncelet-Steiner Single-Circle Construction of the Regular Heptadecagon (17-Gon)
   :align: center

Overview
--------

``geometor-klein`` unites the two foundational geometric treatises of **Felix Klein** (1849–1925) in a synchronized 4-track Digital Scriptorium **Book Codex** (*English · Deutsch · Summary · Notes*) paired with **100% exact SymPy and** ``geometor.model`` **symbolic verifiers**:

1. **Book 1 — Famous Problems of Elementary Geometry (1895 / 1897)**:
   *Vorträge über ausgewählte Fragen der Elementargeometrie* (ausgearbeitet von F. Tägert, Leipzig: B. G. Teubner, 1895) and its authorized English translation by W. W. Beman & D. E. Smith (Boston & London: Ginn & Co., 1897) — resolving the classical problems of **duplication of the cube**, **trisection of the angle**, **division of the circle into equal parts** (including Gauss's regular $17$-gon constructed on a single fixed circle via von Staudt and Schröter), and **quadrature of the circle** (Cantor's countability proof, Hermite's transcendence of $e$, Lindemann's transcendence of $\pi$ via Gordan's umbral calculus, and Abdank-Abakanowicz's mechanical integraph).
2. **Book 2 — The Erlangen Program (1872 / 1893)**:
   *Vergleichende Betrachtungen über neuere geometrische Forschungen* (Erlangen: Andreas Deichert, 1872; *Mathematische Annalen* 43, 1893) and its authorized English translation by M. W. Haskell (*Bulletin of the New York Mathematical Society* 2, 1893) — formulating geometry on a manifold as the **invariant theory of its transformation group**, from the Euclidean Principal Group (*Hauptgruppe*) through the Affine, Projective, Möbius Reciprocal-Radii, Lie Sphere, Birational, and Topological (*Analysis situs*) groups, together with Note V on Cayley–Klein non-Euclidean metrics.

.. image:: docsrc/_static/figures/fig_erlangen_group_lattice.svg
   :alt: Transformation-Group Lattice and Invariant Cascade of Klein's Erlangen Program
   :align: center

Key Capabilities
----------------

- **64-File Synchronized Dual Book Codex**: 10 four-track units for *Famous Problems* and 6 four-track units for *The Erlangen Program*, grounded strictly in 100% public-domain primary witnesses (zero post-1930 editorial notes) and linked across **9 GEOMETOR sister corpora** (``euclid``, ``kepler``, ``hilbert``, ``bertrand-russell``, ``hoenen``, ``lemoine``, ``petersen``, ``pappus``, ``wildberger``).
- **Exact Symbolic Constructibility Analyzer** (:mod:`geometor.klein.constructibility`):
  Gauss–Wantzel regular $n$-gon classifier ($\varphi(n) = 2^k$, Fermat primes $F_0..F_4$), real cyclotomic minimal polynomials $\psi_n(u)$ for $u = 2\cos(2\pi/n)$, Klein's degree-$2^h$ criterion with depressed cubic-resolvent Galois test ($D_4$ vs. $A_4, S_4$), and Hermite–Lindemann transcendence diagnostics for $e$ and $\pi$.
- **Single-Circle Regular Heptadecagon Engine** (:mod:`geometor.klein.heptadecagon`):
  Exact polynomial-quotient canonicalizer ``canonicalize_17`` over $K_{16} = \mathbb{Q}(\cos\frac{2\pi}{17}, \sin\frac{2\pi}{17})$ and Klein's von Staudt–Schröter construction inscribing all **17 exact regular heptadecagon vertices** ``V0``..``V16`` inside :class:`geometor.model.Model` using **straightedge lines and a single fixed circle** $C_0: x^2 + y(y - 2) = 0$ (``len(model.circles) == 1``, ``0`` floating-point coordinates).
- **Erlangen Group-Invariant & Cayley–Klein Verifier** (:mod:`geometor.klein.erlangen`):
  Exact rational verification of invariants preserved and broken across the Principal Similarity, Affine Shear, Projective Collineation, and Möbius Reciprocal-Radii Inversion groups, plus symbolic proof of Cayley–Klein logarithmic cross-ratio distance additivity.

Quickstart
----------

Python API
~~~~~~~~~~

.. code-block:: python

   import sympy as sp
   from geometor.klein import (
       analyze_constructibility,
       audit_codex,
       construct_gauss_17gon_periods,
       verify_cayley_klein_additivity,
       verify_erlangen_invariants,
   )

   # 1. Gauss-Wantzel & Galois constructibility checks
   assert analyze_constructibility(17).is_constructible is True
   assert analyze_constructibility(7).is_constructible is False
   assert analyze_constructibility(sp.pi).is_constructible is False

   # 2. Exact Poncelet-Steiner single-circle regular 17-gon in geometor.model
   res = construct_gauss_17gon_periods(inscribe_polygon=True)
   assert len(res.model.circles) == 1 and len(res.vertices) == 17
   assert res.radical_dependence_residual == 0

   # 3. Erlangen group-hierarchy invariants & codex audit
   erl = verify_erlangen_invariants()
   ck = verify_cayley_klein_additivity()
   assert ck.multiplicative_identity_residual == 0
   assert audit_codex().is_valid is True

Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   geometor-klein polygons --max-n 24
   geometor-klein heptadecagon
   geometor-klein erlangen --json
   geometor-klein audit

Links
-----

- **Documentation**: https://geometor.github.io/klein
- **Source Repository**: https://github.com/geometor/klein
- **Issues**: https://github.com/geometor/klein/issues
