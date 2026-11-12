:navigation: header
:order: 30
:layout: book
:title: Concordance

.. _concordance:

CROSS-CORPUS CONCORDANCE
========================

.. rubric:: Bidirectional Loci Across Klein (1872/1893 & 1895/1897) and Nine GEOMETOR Sister Corpora

This master concordance maps the algebraic constructibility criteria, restricted-instrument theorems, transcendence proofs, and transformation-group hierarchies of :person:`Felix Klein <klein>` across :cite:`*Famous Problems of Elementary Geometry* (1895/1897) <klein:1897>` and :cite:`*The Erlangen Program* (1872/1893) <klein:1893:erlangen>` directly to nine sister repositories in the **GEOMETOR** ecosystem: ``euclid``, ``kepler``, ``hilbert``, ``bertrand-russell``, ``hoenen``, ``lemoine``, ``petersen``, ``pappus``, and ``wildberger``.

.. contents:: Thematic Loci
   :local:
   :depth: 2
   :backlinks: none

Summary Matrix
--------------

.. list-table:: Master Concordance of Constructibility & Transformation Groups
   :header-rows: 1
   :widths: 26 24 22 28

   * - Foundational Theme
     - *Famous Problems* (1895/1897)
     - *Erlangen Program* (1872/1893)
     - GEOMETOR Sister Corpora
   * - :ref:`Euclidean Straightedge-and-Compass Postulates & Iterated Square-Root Towers <conc-euclidean-postulates-square-roots>`
     - Introduction & Part I, Ch. I (§§ 1–15, EN pp. 1–12 / DE S. 1–10)
     - § 1 (Principal Group of Similarities)
     - ``geometor/euclid`` (Book I, Postulates 1–3; Book II, Prop. 14; Book VI, Props. 12–13); ``geometor/petersen`` (Algebraic Appendix & Theorie der algebraischen Gleichungen (1878)); ``geometor/hilbert`` (Chapter VII (§§ 36–39: Geometrical Constructions Based Upon Axioms I–V))
   * - :ref:`Delian Cube Duplication, Angle Trisection, and Plane vs. Solid Problems <conc-delian-trisection-solid-problems>`
     - Part I, Ch. II (§§ 1–3, EN pp. 13–15 / DE S. 10–12) & Ch. V (§§ 2–5, EN pp. 42–47 / DE S. 32–37)
     - § 10 (Galois Group Analogy for Algebraic Equations)
     - ``geometor/pappus`` (Book III (Delian Mean Proportionals) & Book IV (Plane, Solid, and Linear Problems; Conchoid Trisection)); ``geometor/euclid`` (Book I, Prop. 9 (Angle Bisection) & Book XI, Props. 31–33 (Parallelepipeds & Cubes))
   * - :ref:`Cyclotomy, Kepler's Unknowable Heptagon (n = 7), and Gauss's Heptadecagon (n = 17) <conc-cyclotomy-heptagon-heptadecagon>`
     - Part I, Ch. III (§§ 1–8, EN pp. 16–23 / DE S. 13–19) & Ch. IV (§§ 1–6, EN pp. 24–33 / DE S. 19–25)
     - § 10 (Commutative / Abelian Group Reductions)
     - ``geometor/kepler`` (Book I, Props. XLV–XLVII (De heptagono et figuris inscibilibus)); ``geometor/euclid`` (Book IV, Props. 11, 15, 16 (Regular 5-, 6-, and 15-gons))
   * - :ref:`Restricted Instruments: Poncelet–Steiner Fixed Circle, Mascheroni Compasses, and Geometrography <conc-restricted-instruments-geometrography>`
     - Part I, Ch. IV (§§ 7–9, EN pp. 33–41 / DE S. 25–32) & Ch. V (§ 1, Paper Folding)
     - §§ 2–3 (Projective Straightedge Constructions vs. Metric Circle)
     - ``geometor/lemoine`` (Part I (Operational Symbols R_1, R_2, C_1, C_2, C_3) & Poncelet-Steiner / Mascheroni Comparisons); ``geometor/pappus`` (Complete Quadrilateral Harmonic Construction & Perspectivity)
   * - :ref:`Cantor's Continuum, Transcendence of e and pi, and Quadrature of the Circle <conc-cantor-continuum-transcendence-pi>`
     - Part II, Chs. I–V (EN pp. 49–80 / DE S. 38–66)
     - § 8.2 (Analysis Situs & Continuous Manifolds)
     - ``geometor/bertrand-russell`` (PoM Part V (Infinity and Continuity, Cantor's Aleph_0 vs. Continuum) & Part VI); ``geometor/hoenen`` (Caput III (§ 2.6, Continuous Extension vs. Point-Sets) & Caput VII)
   * - :ref:`The Erlangen Hierarchy: Principal Group, Affine Geometry, and Projective Collineations <conc-erlangen-principal-projective-hierarchy>`
     - Part I, Ch. IV (§ 7, Rational Projective vs. Quadratic Euclidean Operations)
     - Introduction & §§ 1–5 (EN pp. 215–230 / DE S. 3–21)
     - ``geometor/pappus`` (Props. 129–145 (Cross-Ratio Invariance Under Central Projection)); ``geometor/hilbert`` (Chapters V–VI (Desargues's & Pascal's Theorems) & 1902 Appendix on Transformation Groups)
   * - :ref:`Cayley–Klein Projective Metrics, the Absolute Quadric, and Rational Trigonometry <conc-cayley-klein-non-euclidean-metrics>`
     - Introduction (Theoretical Exactitude vs. Empirical Approximation)
     - §§ 1–2, § 6, § 10.2 & Note V (On the So-Called Non-Euclidean Geometry)
     - ``geometor/wildberger`` (Quadrance, Spread, Cross-Ratio, and Projective Null Conic Metrics); ``geometor/bertrand-russell`` (EFG Ch. I (§§ 30–43: Cayley & Klein) & PoM Ch. XLVIII (§§ 405–411: Projective Theory of Distance)); ``geometor/hoenen`` (Caput II–IV (Critique of Non-Euclidean Projective Interpretations & Structuralism))
   * - :ref:`Reciprocal Radii (Möbius Inversion), Plücker Line Geometry, and Lie's Sphere Geometry <conc-reciprocal-radii-lie-contact>`
     - Part I, Ch. V (§§ 3–4: CircularPoints at Infinity on Cissoid & Conchoid)
     - §§ 5–9 & Note VII (EN pp. 226–238, 248 / DE S. 15–32, 42)
     - ``geometor/petersen`` (Chapter III (Method of Rotation, Similarity, and Inversion / Reciprocal Radii)); ``geometor/lemoine`` (Transformation by Reciprocal Radii & Apollonius Contact Constructions)

----

Detailed Analytical Concordance Entries
---------------------------------------

.. _conc-euclidean-postulates-square-roots:

1. Euclidean Straightedge-and-Compass Postulates & Iterated Square-Root Towers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Famous Problems (1895 / 1897):** Introduction & Part I, Ch. I (§§ 1–15, EN pp. 1–12 / DE S. 1–10)
* **Erlangen Program (1872 / 1893):** § 1 (Principal Group of Similarities)

**Cross-Corpus Relations:**

* **geometor/euclid** — *The Thirteen Books of Euclid's Elements (Heath, 1908)*, ``Book I, Postulates 1–3; Book II, Prop. 14; Book VI, Props. 12–13``: Klein's Fundamental Theorem (Hauptsatz) translates Euclid's Postulates 1–3 into the analytic closure of rational operations $(+, -, \cdot, /)$ and square roots $\sqrt{R}$.
* **geometor/petersen** — *Methods and Theories for the Solution of Problems of Geometrical Constructions (1879)*, ``Algebraic Appendix & Theorie der algebraischen Gleichungen (1878)``: Klein explicitly singles out Julius Petersen in the Introduction (EN p. 2 / DE S. 2) as the sole textbook author presenting elementary algebraic impossibility proofs for geometric constructions.
* **geometor/hilbert** — *Grundlagen der Geometrie (1899 / 1902)*, ``Chapter VII (§§ 36–39: Geometrical Constructions Based Upon Axioms I–V)``: Hilbert refines Klein's quadratic-tower criterion by isolating the Pythagorean subfield (sqrt(1 + omega^2), solvable with straightedge and segment-transferrer Eichmass) inside the full Euclidean square-root field.

.. _conc-delian-trisection-solid-problems:

2. Delian Cube Duplication, Angle Trisection, and Plane vs. Solid Problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Famous Problems (1895 / 1897):** Part I, Ch. II (§§ 1–3, EN pp. 13–15 / DE S. 10–12) & Ch. V (§§ 2–5, EN pp. 42–47 / DE S. 32–37)
* **Erlangen Program (1872 / 1893):** § 10 (Galois Group Analogy for Algebraic Equations)

**Cross-Corpus Relations:**

* **geometor/pappus** — *Synagoge (Collection), Books III, IV & VII*, ``Book III (Delian Mean Proportionals) & Book IV (Plane, Solid, and Linear Problems; Conchoid Trisection)``: Klein's degree-2^h impossibility proofs for x^3 = 2 and x^3 = cos(phi) + i*sin(phi), paired with conic intersections, Diocles' cissoid, and Nicomedes' conchoid in Ch. V, supply the exact Galois-algebraic proof of Pappus's ancient classification of plane, solid, and linear loci.
* **geometor/euclid** — *The Thirteen Books of Euclid's Elements (Heath, 1908)*, ``Book I, Prop. 9 (Angle Bisection) & Book XI, Props. 31–33 (Parallelepipeds & Cubes)``: Contrasts elementary quadratic angle bisection (Euclid I.9) with the irreducible cubic monodromy of general angle trisection.

.. _conc-cyclotomy-heptagon-heptadecagon:

3. Cyclotomy, Kepler's Unknowable Heptagon (n = 7), and Gauss's Heptadecagon (n = 17)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Famous Problems (1895 / 1897):** Part I, Ch. III (§§ 1–8, EN pp. 16–23 / DE S. 13–19) & Ch. IV (§§ 1–6, EN pp. 24–33 / DE S. 19–25)
* **Erlangen Program (1872 / 1893):** § 10 (Commutative / Abelian Group Reductions)

**Cross-Corpus Relations:**

* **geometor/kepler** — *Harmonices Mundi, Liber I (1619)*, ``Book I, Props. XLV–XLVII (De heptagono et figuris inscibilibus)``: Kepler argued philosophically and algebraically that the regular heptagon (n = 7) is 'unknowable' (inscibilis) because its side ratio obeys a cubic equation irreducible to planar bisections; Klein Ch. III (§§ 5–7) proves rigorouly via Eisenstein's criterion that z^6 + ... + 1 = 0 (real cubic u^3 + u^2 - 2u - 1 = 0) has degree 6 != 2^h, while p = 17 = 2^(2^2) + 1 splits into four quadratics.
* **geometor/euclid** — *The Thirteen Books of Euclid's Elements (Heath, 1908)*, ``Book IV, Props. 11, 15, 16 (Regular 5-, 6-, and 15-gons)``: Klein Ch. III, § 2 explains Euclid IV.16 (regular 15-gon) arithmetically via Bezout partial fractions 1/15 = 2/3 - 3/5.

.. _conc-restricted-instruments-geometrography:

4. Restricted Instruments: Poncelet–Steiner Fixed Circle, Mascheroni Compasses, and Geometrography
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Famous Problems (1895 / 1897):** Part I, Ch. IV (§§ 7–9, EN pp. 33–41 / DE S. 25–32) & Ch. V (§ 1, Paper Folding)
* **Erlangen Program (1872 / 1893):** §§ 2–3 (Projective Straightedge Constructions vs. Metric Circle)

**Cross-Corpus Relations:**

* **geometor/lemoine** — *Géométrographie, ou Art des constructions géométriques (1902)*, ``Part I (Operational Symbols R_1, R_2, C_1, C_2, C_3) & Poncelet-Steiner / Mascheroni Comparisons``: Klein's sharp distinction between theoretical instrument classes—straightedge alone (rational field), Mascheroni compasses alone, and Poncelet–Steiner–von Staudt–Schröter straightedge + one fixed circle—parallels Lemoine's quantitative operational measure of ruler vs. compass simplicity.
* **geometor/pappus** — *Synagoge (Collection), Book VII*, ``Complete Quadrilateral Harmonic Construction & Perspectivity``: Pure straightedge constructions (Lambert, Brianchon, von Staudt) construct precisely projective rational functions via harmonic ranges, requiring one fixed metric circle C_0 to adjoin square roots.

.. _conc-cantor-continuum-transcendence-pi:

5. Cantor's Continuum, Transcendence of e and pi, and Quadrature of the Circle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Famous Problems (1895 / 1897):** Part II, Chs. I–V (EN pp. 49–80 / DE S. 38–66)
* **Erlangen Program (1872 / 1893):** § 8.2 (Analysis Situs & Continuous Manifolds)

**Cross-Corpus Relations:**

* **geometor/bertrand-russell** — *The Principles of Mathematics (1903) & An Essay on the Foundations of Geometry (1897)*, ``PoM Part V (Infinity and Continuity, Cantor's Aleph_0 vs. Continuum) & Part VI``: Klein's exposition of Cantor's countability of algebraic numbers by height N and diagonal uncountability of the continuum (Part II, Ch. I) anticipates Russell's Cantorian resolution of spatial continuity in 1903.
* **geometor/hoenen** — *De Noetica Geometriae (1954)*, ``Caput III (§ 2.6, Continuous Extension vs. Point-Sets) & Caput VII``: Contrasts point-set enumerations of algebraic vs. transcendental coordinates with intuitive continuous geometric extension traced by mechanical curve-integrators (Integraph, Ch. V).

.. _conc-erlangen-principal-projective-hierarchy:

6. The Erlangen Hierarchy: Principal Group, Affine Geometry, and Projective Collineations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Famous Problems (1895 / 1897):** Part I, Ch. IV (§ 7, Rational Projective vs. Quadratic Euclidean Operations)
* **Erlangen Program (1872 / 1893):** Introduction & §§ 1–5 (EN pp. 215–230 / DE S. 3–21)

**Cross-Corpus Relations:**

* **geometor/pappus** — *Synagoge (Collection), Book VII*, ``Props. 129–145 (Cross-Ratio Invariance Under Central Projection)``: Elevates Pappus's cross-ratio invariance from an isolated synthetic lemma to the defining invariant of the projective collineation group encompassing the Principal Group.
* **geometor/hilbert** — *Grundlagen der Geometrie (1899 / 1902)*, ``Chapters V–VI (Desargues's & Pascal's Theorems) & 1902 Appendix on Transformation Groups``: Connects Klein's continuous group hierarchy directly to Hilbert's axiomatic Characterization of Desarguesian skew-fields, Pappian commutative fields, and Helmholtz–Lie transformation axioms.

.. _conc-cayley-klein-non-euclidean-metrics:

7. Cayley–Klein Projective Metrics, the Absolute Quadric, and Rational Trigonometry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Famous Problems (1895 / 1897):** Introduction (Theoretical Exactitude vs. Empirical Approximation)
* **Erlangen Program (1872 / 1893):** §§ 1–2, § 6, § 10.2 & Note V (On the So-Called Non-Euclidean Geometry)

**Cross-Corpus Relations:**

* **geometor/wildberger** — *Divine Proportions (2005) & Universal Hyperbolic Geometry*, ``Quadrance, Spread, Cross-Ratio, and Projective Null Conic Metrics``: Wildberger's quadrance Q and spread s strip away transcendental logarithms from Klein's Cayley–Klein metric d(A,B) = c*log(A,B;I_1,I_2), expressing Principal, hyperbolic, elliptic, and Möbius invariants as pure rational functions over Q.
* **geometor/bertrand-russell** — *An Essay on the Foundations of Geometry (1897) & Principles of Mathematics (1903)*, ``EFG Ch. I (§§ 30–43: Cayley & Klein) & PoM Ch. XLVIII (§§ 405–411: Projective Theory of Distance)``: Russell explicitly adopts Klein's 1871–1872 projective classification of hyperbolic, elliptic, and parabolic geometries relative to the Absolute while debating whether cross-ratio metrics replace philosophical intuition of distance.
* **geometor/hoenen** — *De Noetica Geometriae (1954)*, ``Caput II–IV (Critique of Non-Euclidean Projective Interpretations & Structuralism)``: Hoenen examines Klein's Principle of Transference (§§ 4–5) and Cayley–Klein models (Note V), arguing that relative consistency inside projective Euclidean models presupposes an intuitive ambient continuum.

.. _conc-reciprocal-radii-lie-contact:

8. Reciprocal Radii (Möbius Inversion), Plücker Line Geometry, and Lie's Sphere Geometry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Famous Problems (1895 / 1897):** Part I, Ch. V (§§ 3–4: CircularPoints at Infinity on Cissoid & Conchoid)
* **Erlangen Program (1872 / 1893):** §§ 5–9 & Note VII (EN pp. 226–238, 248 / DE S. 15–32, 42)

**Cross-Corpus Relations:**

* **geometor/petersen** — *Methods and Theories for the Solution of Problems of Geometrical Constructions (1879)*, ``Chapter III (Method of Rotation, Similarity, and Inversion / Reciprocal Radii)``: Petersen's constructive problem-solving transformations (translation, rotation, homothety, circle inversion) instantiate in planar synthesis the exact subgroups systematized in §§ 1 & 6 of Klein's Erlangen Program.
* **geometor/lemoine** — *Géométrographie (1902)*, ``Transformation by Reciprocal Radii & Apollonius Contact Constructions``: Links Lie's contact geometry of tangency among circles and spheres (§ 7) to classical Apollonius contact constructions.
