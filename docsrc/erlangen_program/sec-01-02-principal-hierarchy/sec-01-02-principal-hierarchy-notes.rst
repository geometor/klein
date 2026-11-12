:title: §§ 1–2: Principal Group & Transformation Hierarchy — Symbolic Notes
:layout: book

.. _ep-sec-01-02-principal-hierarchy-notes:

§§ 1–2: Principal Group & Transformation Hierarchy — Critical & Symbolic Notes
==============================================================================

.. rubric:: Exact Symbolic Verification of Invariant Shedding in ``geometor.klein.erlangen``

Visualizing the Erlangen Subsumption Ladder
-------------------------------------------

.. figure:: /_static/figures/fig_erlangen_hierarchy.svg
   :alt: Klein's Erlangen Hierarchy: Principal Group, Affine Group, Projective Group, and Reciprocal Radii
   :align: center

   **Klein's Erlangen Hierarchy (§§ 1–3 & § 6).** As the transformation group expands from the **Principal Group** (similarities) to **Affine shears** and **Projective collineations**, metric angles and quadrance ratios are progressively shed until only incidence and the $4$-point collinear cross-ratio survive; branching to **Reciprocal Radii** (Möbius circle inversion) merges lines and circles into generalized circles while preserving conformal angles and $4$-point quadrance cross-ratios.

Exact Symbolic Verification Over $\mathbb{Q}$ (:mod:`geometor.klein.erlangen`)
------------------------------------------------------------------------------

In :func:`geometor.klein.erlangen.verify_erlangen_invariants`, we instantiate rational test configurations inside ``geometor.model.Model`` (with zero floating-point approximations) and apply exact representatives of Klein's four planar groups:

1. **Principal Group (§ 1 — Rational Similarity):** $(x, y) \mapsto (3x - 4y + 2,\; 4x + 3y - 1)$ (Pythagorean rotation-dilation scaling lengths by $5$ and quadrances by $25$).
2. **Affine Group (§ 2 — Area-Scaling Shear):** $(x, y) \mapsto (x + 2y + 1,\; 3y - 2)$ (fixes the line at infinity $w = 0$ without fixing the circular points $I, J$).
3. **Projective Group (§ 3 — Full Homography):** $(x, y) \mapsto \left(\frac{2x + y + 1}{x + y + 3},\; \frac{x + 3y + 2}{x + y + 3}\right)$ (moves the line at infinity to a finite horizon).
4. **Reciprocal Radii (§ 6 — Möbius Circle Inversion):** $(x, y) \mapsto \left(\frac{4x}{x^2 + y^2},\; \frac{4y}{x^2 + y^2}\right)$ (inverts across $x^2 + y^2 = 4$).

Using Rational Trigonometry invariants (:person:`Norman Wildberger <wildberger>`, :cite:`2005 <wildberger:2005>`; ``geometor.model.invariants``), every invariant is tested by exact symbolic subtraction in SymPy:

.. list-table:: Exact Erlangen Invariant Survival Matrix (``verify_erlangen_invariants()``)
   :header-rows: 1
   :widths: 32 17 17 17 17

   * - Algebraic Invariant
     - Principal (§ 1)
     - Affine (§ 2)
     - Projective (§ 3)
     - Inversion (§ 6)
   * - **Line Spread** $s(\ell_{12}, \ell_{13})$ (Angle)
     - **Preserved** ($\frac{9}{10}$)
     - Broken ($\frac{81}{130}$)
     - Broken ($\frac{25}{74}$)
     - *(Conformal)*
   * - **Quadrance Ratio** $\frac{Q(T_1, T_2)}{Q(T_1, T_3)}$
     - **Preserved** ($\frac{4}{5}$)
     - Broken ($\frac{1}{13}$)
     - Broken ($\frac{185}{117}$)
     - Broken ($\frac{65}{18}$)
   * - **Parallelism** ($\det(\ell, \ell') = 0$)
     - **Preserved**
     - **Preserved**
     - Broken
     - Broken
   * - **Collinear Division Ratio** $\frac{Q(A,B)}{Q(A,C)}$
     - **Preserved** ($\frac{1}{9}$)
     - **Preserved** ($\frac{1}{9}$)
     - Broken ($\frac{25}{147}$)
     - Broken ($\frac{5}{27}$)
   * - **Collinear Cross-Ratio** $(A, B; C, D)$
     - **Preserved** ($\frac{4}{3}$)
     - **Preserved** ($\frac{4}{3}$)
     - **Preserved** ($\frac{4}{3}$)
     - *(On circle)*
   * - **4-Point Quadrance Cross-Ratio** $\frac{Q_{AC} Q_{BD}}{Q_{AD} Q_{BC}}$
     - **Preserved** ($\frac{16}{9}$)
     - **Preserved** ($\frac{16}{9}$)
     - **Preserved** ($\frac{16}{9}$)
     - **Preserved** ($\frac{16}{9}$)

Philological Note on Footnote 8 (Group Inverses, 1893)
------------------------------------------------------

In 1872, following the finite permutation terminology of :person:`Galois <galois>`, Serret, and Camille Jordan, Klein defined a group solely by closure under composition ($g_1, g_2 \in G \implies g_1 g_2 \in G$). For a *finite* set of bijections, closure automatically implies $g^{-1} = g^{k-1} \in G$; for *infinite* continuous families (such as contractions $x \mapsto \lambda x$ with $0 < \lambda < 1$), closure alone defines only a semigroup. Klein's 1893 bracketed addition in Footnote 8 explicitly supplies the inverse axiom required by :person:`Sophus Lie's <lie>` *Theorie der Transformationsgruppen*.
