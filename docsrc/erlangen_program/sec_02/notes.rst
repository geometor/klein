:type: notes
:title: § 2: Erlangen Subsumption Ladder & Exact Invariant Survival — Symbolic Notes
:layout: book
:canonical_id: § 2
:order: 3

.. _ep-sec_02-notes:
.. _ep-sec-02-notes:

§ 2: Erlangen Subsumption Ladder — Critical & Symbolic Notes
============================================================

.. rubric:: Exact Symbolic Verification of Invariant Shedding in ``geometor.klein.erlangen``

Visualizing the Erlangen Subsumption Ladder
-------------------------------------------

.. figure:: /_static/figures/fig_erlangen_hierarchy.svg
   :alt: Klein's Erlangen Hierarchy: Principal Group, Affine Group, Projective Group, and Reciprocal Radii
   :align: center

   **Klein's Erlangen Hierarchy (§§ 1–3 & § 6).** As the transformation group expands from the **Principal Group** (similarities) to **Affine shears** and **Projective collineations**, metric angles and quadrance ratios are progressively shed until only incidence and the :math:`4`-point collinear cross-ratio survive; branching to **Reciprocal Radii** (Möbius circle inversion) merges lines and circles into generalized circles while preserving conformal angles and :math:`4`-point quadrance cross-ratios.

Exact Symbolic Verification Over :math:`\mathbb{Q}` (:mod:`geometor.klein.erlangen`)
------------------------------------------------------------------------------------

In :func:`geometor.klein.erlangen.verify_erlangen_invariants`, we instantiate rational test configurations inside ``geometor.model.Model`` (with zero floating-point approximations) and apply exact representatives of Klein's four planar groups:

1. **Principal Group (§ 1 — Rational Similarity):** :math:`(x, y) \mapsto (3x - 4y + 2,\; 4x + 3y - 1)` (Pythagorean rotation-dilation scaling lengths by :math:`5` and quadrances by :math:`25`).
2. **Affine Group (§ 2 — Area-Scaling Shear):** :math:`(x, y) \mapsto (x + 2y + 1,\; 3y - 2)` (fixes the line at infinity :math:`w = 0` without fixing the circular points :math:`I, J`).
3. **Projective Group (§ 3 — Full Homography):** :math:`(x, y) \mapsto \left(\frac{2x + y + 1}{x + y + 3},\; \frac{x + 3y + 2}{x + y + 3}\right)` (moves the line at infinity to a finite horizon).
4. **Reciprocal Radii (§ 6 — Möbius Circle Inversion):** :math:`(x, y) \mapsto \left(\frac{4x}{x^2 + y^2},\; \frac{4y}{x^2 + y^2}\right)` (inverts across :math:`x^2 + y^2 = 4`).

Using Rational Trigonometry invariants (:person:`Norman Wildberger <wildberger>`, :cite:`2005 <wildberger:2005>`; ``geometor.model.invariants``), every invariant is tested by exact symbolic subtraction in SymPy:

.. list-table:: Exact Erlangen Invariant Survival Matrix (``verify_erlangen_invariants()``)
   :header-rows: 1
   :widths: 32 17 17 17 17

   * - Algebraic Invariant
     - Principal (§ 1)
     - Affine (§ 2)
     - Projective (§ 3)
     - Inversion (§ 6)
   * - **Line Spread** :math:`s(\ell_{12}, \ell_{13})` (Angle)
     - **Preserved** (:math:`\frac{9}{10}`)
     - Broken (:math:`\frac{81}{130}`)
     - Broken (:math:`\frac{25}{74}`)
     - *(Conformal)*
   * - **Quadrance Ratio** :math:`\frac{Q(T_1, T_2)}{Q(T_1, T_3)}`
     - **Preserved** (:math:`\frac{4}{5}`)
     - Broken (:math:`\frac{1}{13}`)
     - Broken (:math:`\frac{185}{117}`)
     - Broken (:math:`\frac{65}{18}`)
   * - **Parallelism** (:math:`\det(\ell, \ell') = 0`)
     - **Preserved**
     - **Preserved**
     - Broken
     - Broken
   * - **Collinear Division Ratio** :math:`\frac{Q(A,B)}{Q(A,C)}`
     - **Preserved** (:math:`\frac{1}{9}`)
     - **Preserved** (:math:`\frac{1}{9}`)
     - Broken (:math:`\frac{25}{147}`)
     - Broken (:math:`\frac{5}{27}`)
   * - **Collinear Cross-Ratio** :math:`(A, B; C, D)`
     - **Preserved** (:math:`\frac{4}{3}`)
     - **Preserved** (:math:`\frac{4}{3}`)
     - **Preserved** (:math:`\frac{4}{3}`)
     - *(On circle)*
   * - **4-Point Quadrance Cross-Ratio** :math:`\frac{Q_{AC} Q_{BD}}{Q_{AD} Q_{BC}}`
     - **Preserved** (:math:`\frac{16}{9}`)
     - **Preserved** (:math:`\frac{16}{9}`)
     - **Preserved** (:math:`\frac{16}{9}`)
     - **Preserved** (:math:`\frac{16}{9}`)

