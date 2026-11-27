:type: summary
:title: Part I, Ch. IV: Regular 17-Gon Construction — Analytical Summary
:layout: book
:canonical_id: Ch. IV
:order: 4

.. _fp-part_1-ch_04-summary:
.. _fp-part1-ch_04-summary:
.. _fp-ch_04-summary:
.. _fp-part1-ch4-heptadecagon-summary:

Part I, Chapter IV — Analytical Summary
=======================================

.. rubric:: Architecture of the Gauss–von Staudt–Schröter–Klein Regular Heptadecagon (§§ 1–9)

Overview of the Two-Stage Demonstration
---------------------------------------

Chapter IV is the constructive centerpiece of Part I, turning :person:`Gauss's <gauss>` algebraic discovery of March 30, 1796 (:cite:`1801 <gauss:1801>`) into a complete **single-circle straightedge construction** governed by the :term:`Poncelet–Steiner theorem <poncelet-steiner-theorem>`.

Stage I — Algebraic Tower of Gaussian Periods (§§ 1–6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the primitive root :math:`g = 3 \pmod{17}`, the :math:`16` primitive :math:`17`-th roots of unity are arranged into the cyclic orbit :math:`\varepsilon_{3^m}` (:math:`m = 1, \dots, 16`) and partitioned by alternating decimation into :term:`Gaussian periods <gaussian-periods>`:

.. list-table:: Quadratic Period Tower of the Regular :math:`17`-Gon
   :header-rows: 1
   :widths: 16 24 28 32

   * - Level
     - EN / DE Symbols
     - Quadratic Equation
     - Exact Sign & Root Value
   * - :math:`8`-**periods**
     - :math:`x_1, x_2` / :math:`\eta_0, \eta_1`
     - :math:`(\xi): x^2 + x - 4 = 0`
     - :math:`x_1 = \frac{-1 + \sqrt{17}}{2} > 0 > x_2`
   * - :math:`4`-**periods** (even)
     - :math:`y_1, y_2` / :math:`\eta'_0, \eta'_1`
     - :math:`(\eta): y^2 - x_1 y - 1 = 0`
     - :math:`y_1 = \frac{x_1 + \sqrt{x_1^2 + 4}}{2} > 0 > y_2`
   * - :math:`4`-**periods** (odd)
     - :math:`y_4, y_3` / :math:`(\eta'_0), (\eta'_1)`
     - :math:`(\eta'): y^2 - x_2 y - 1 = 0`
     - :math:`y_4 = \frac{x_2 + \sqrt{x_2^2 + 4}}{2} > 0 > y_3`
   * - :math:`2`-**periods**
     - :math:`z_1, z_2` / :math:`\eta''_0, \eta''_1`
     - :math:`(\zeta): z^2 - y_1 z + y_4 = 0`
     - :math:`z_1 = 2\cos\frac{2\pi}{17} > z_2 = 2\cos\frac{8\pi}{17} > 0`

* **Semicircle Chord Inequality (§ 5):** Representing every :math:`2`-period via :math:`S_k = 2\sin\frac{k\pi}{34}` proves geometrically that :math:`y_3 < y_2 < y_4 < y_1` and :math:`x_2 < x_1`.
* **Radical Dependence (§ 6):** Because :math:`(y_1 - y_2)(y_4 - y_3) = 2(x_1 - x_2)`, the third radical satisfies :math:`\sqrt{x_1^2 + 4}\,\sqrt{x_2^2 + 4} = 2\sqrt{17}`, confirming that :math:`\mathbb{Q}(\cos\frac{2\pi}{17})` has degree :math:`2^3 = 8` (not :math:`16`) over :math:`\mathbb{Q}`.

Stage II — Projective Single-Circle Realization (§§ 7–9)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following :person:`Poncelet <poncelet>` (:cite:`1822 <poncelet:1822>`), :person:`Steiner <steiner>` (:cite:`1833 <steiner:1833>`), :person:`von Staudt <staudt>` (:cite:`1842 <staudt:1842>`), and :person:`Schröter <schroeter>` (:cite:`1872 <schroeter:1872>`), every quadratic :math:`t^2 - pt + q = 0` is solved on the **single fixed circle** :math:`C_0: x^2 + y(y - 2) = 0` using straightedge lines alone:

1. **Staudt Transversal (§ 8):** Join :math:`\left(\frac{q}{p}, 0\right)` on :math:`y = 0` to :math:`\left(\frac{4}{p}, 2\right)` on :math:`y = 2`, and project the circle intersections from :math:`A(0, 2)` onto :math:`y = 0`.
2. **Projective Involution (§ 9):** Stereographic projection from :math:`A(0, 2)` followed by projection from :math:`O(0, 0)` implements the rational map :math:`x \mapsto x' = \frac{4}{x}` between the two parallel tangents; harmonic projection through :math:`\left(0, \frac{2}{5}\right)` and :math:`\left(0, \frac{2y_4}{y_4 - 4}\right)` constructs :math:`-\frac{1}{x_1}`, :math:`-\frac{1}{x_2}`, and :math:`\frac{y_4}{y_1}` without ever resetting compasses.
3. **Direct Cosine Bisection:** The final projecting ray from :math:`A(0, 2)` to :math:`(z_1, 0)` cuts the horizontal diameter :math:`y = 1` at :math:`K_1 = \left(\cos\frac{2\pi}{17}, 1\right)`, whose vertical chord inscribes :math:`V_1` and :math:`V_{16}` directly on :math:`C_0`.
