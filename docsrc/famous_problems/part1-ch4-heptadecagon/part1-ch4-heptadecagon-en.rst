:title: Part I, Ch. IV: The Construction of the Regular Polygon of 17 Sides (1897 English)
:layout: book

.. _fp-part1-ch4-heptadecagon-en:

Part I, Chapter IV — The Construction of the Regular Polygon of 17 Sides
========================================================================

.. rubric:: Part I, Chapter IV (§§ 1–9; :cite:`Ginn & Co., 1897, pp. 24–41 <klein:1897>`)

§§ 1–3. Primitive Roots Modulo 17 and Gauss's Periods
-----------------------------------------------------

**1.** Having seen in Chapter III that division of the circle into an odd prime number of equal parts by straightedge and compasses is possible only for :person:`Gauss's <gauss>` :term:`Fermat primes <fermat-prime>`, we shall now show in an elementary way how to actually inscribe the **regular polygon of $17$ sides** in the unit circle.

Since we possess as yet no construction of the regular $17$-gon derived from purely geometric considerations, we follow the algebraic path indicated by our general theory: we investigate the $16$ roots of the cyclotomic equation

.. math::

   x^{16} + x^{15} + \dots + x^2 + x + 1 = 0,

and translate the resulting nested square-root expression into a geometric construction. In transcendental form the roots are

.. math::

   \varepsilon_k = \cos\frac{2k\pi}{17} + i\sin\frac{2k\pi}{17} \qquad (k = 1, 2, \dots, 16),

with $\varepsilon_k = \varepsilon_1^k$, represented geometrically in the complex plane by the $16$ vertices different from $1$ of the regular $17$-gon inscribed in the unit circle centered at the origin. Once $\varepsilon_1$ is chosen as initial vertex, the angle belonging to $\varepsilon_k$ is $k$ times that of $\varepsilon_1$.

.. picture:: /_static/figures/fig_gauss_17gon_circle.svg
   :alt: Regular Heptadecagon Roots eps_k on the Unit Circle and Semicircle Chords S_k
   :caption: Regular Heptadecagon Roots on the Unit Circle (Klein Figs. 3–4): Conjugate root pairs z_m = eps_r + eps_(17-r) = 2 cos(2r pi/17) and semicircle chord magnitudes S_k = 2 sin(k pi/34).

**2.** The fundamental idea of :person:`Gauss's <gauss>` solution (:cite:`*Disquisitiones Arithmeticae*, 1801 <gauss:1801>`; see also :person:`Bachmann <bachmann>`, :cite:`*Die Lehre von der Kreisteilung*, Leipzig, 1872 <bachmann:1872>`) is to arrange the $16$ roots into a single cycle by means of a **primitive root modulo $17$**—an integer $a$ for which the least positive exponent satisfying $a^s \equiv +1 \pmod{17}$ is $s = 17 - 1 = 16$. The number $a = 3$ possesses this property:

.. math::

   \begin{alignedat}{4}
   3^1 &\equiv 3,  &\quad 3^5 &\equiv 5,  &\quad 3^9  &\equiv 14, &\quad 3^{13} &\equiv 12, \\
   3^2 &\equiv 9,  &\quad 3^6 &\equiv 15, &\quad 3^{10} &\equiv 8, &\quad 3^{14} &\equiv 2,  \\
   3^3 &\equiv 10, &\quad 3^7 &\equiv 11, &\quad 3^{11} &\equiv 7, &\quad 3^{15} &\equiv 6,  \\
   3^4 &\equiv 13, &\quad 3^8 &\equiv 16, &\quad 3^{12} &\equiv 4, &\quad 3^{16} &\equiv 1   \pmod{17}.
   \end{alignedat}

Ordering the roots $\varepsilon_k$ by these remainders gives the cycle

.. math::

   \varepsilon_3,\; \varepsilon_9,\; \varepsilon_{10},\; \varepsilon_{13},\; \varepsilon_5,\; \varepsilon_{15},\; \varepsilon_{11},\; \varepsilon_{16},\; \varepsilon_{14},\; \varepsilon_8,\; \varepsilon_7,\; \varepsilon_4,\; \varepsilon_{12},\; \varepsilon_2,\; \varepsilon_6,\; \varepsilon_1,

in which **each root is the cube of its predecessor** ($\varepsilon_{r'} = \varepsilon_r^3$). Gauss decomposes this $16$-cycle into sums containing $8$, $4$, $2$, and $1$ roots—corresponding to the divisors of $16$—called :term:`Gaussian periods <gaussian-periods>`, which can be calculated successively as roots of quadratic equations.

**3.** Replacing each root $\varepsilon_k$ symbolically by its exponent $k \pmod{17}$ and alternating by steps of $2$, we form:

* **Two $8$-periods** ($x_1$ from even positions in the cycle, $x_2$ from odd positions):

  .. math::

     \begin{aligned}
     x_1 &= 9 + 13 + 15 + 16 + 8 + 4 + 2 + 1, \\
     x_2 &= 3 + 10 + 5 + 11 + 14 + 7 + 12 + 6.
     \end{aligned}

* **Four $4$-periods** (alternating inside $x_1$ and $x_2$):

  .. math::

     \begin{alignedat}{2}
     y_1 &= 13 + 16 + 4 + 1,  &\qquad y_2 &= 9 + 15 + 8 + 2, \\
     y_3 &= 10 + 11 + 7 + 6,  &\qquad y_4 &= 3 + 5 + 14 + 12.
     \end{alignedat}

* **Eight $2$-periods** (alternating inside $y_1, y_2, y_3, y_4$):

  .. math::

     \begin{alignedat}{4}
     z_1 &= 16 + 1, &\quad z_2 &= 13 + 4, &\quad z_3 &= 15 + 2, &\quad z_4 &= 9 + 8, \\
     z_5 &= 11 + 6, &\quad z_6 &= 10 + 7, &\quad z_7 &= 5 + 12, &\quad z_8 &= 3 + 14.
     \end{alignedat}

§§ 4–5. Reality and Relative Magnitude of the Periods
-----------------------------------------------------

**4.** In every $2$-period $z_m$, the two exponents sum to $17$, pairing $\varepsilon_r$ with its complex conjugate $\varepsilon_{17-r} = \overline{\varepsilon_r}$. Hence **all the periods $z_m$, $y_j$, $x_i$ are real numbers**:

.. math::

   \begin{alignedat}{2}
   z_1 &= 2\cos\frac{2\pi}{17},     &\qquad z_5 &= 2\cos\frac{12\pi}{17}, \\
   z_2 &= 2\cos\frac{8\pi}{17},     &\qquad z_6 &= 2\cos\frac{14\pi}{17}, \\
   z_3 &= 2\cos\frac{4\pi}{17},     &\qquad z_7 &= 2\cos\frac{10\pi}{17}, \\
   z_4 &= 2\cos\frac{16\pi}{17},    &\qquad z_8 &= 2\cos\frac{6\pi}{17},
   \end{alignedat}

with $y_1 = z_1 + z_2$, $y_2 = z_3 + z_4$, $y_3 = z_5 + z_6$, $y_4 = z_7 + z_8$, $x_1 = y_1 + y_2$, and $x_2 = y_3 + y_4$.

**5.** To determine unambiguously which sign belongs to each square root in our quadratic equations, we establish the **relative magnitudes** of the periods by an elementary geometric artifice. Divide the upper semicircle of unit radius into $17$ equal arcs at $A_1, A_2, \dots, A_{17}$ starting from $O_{\text{arc}} = A_0$, and denote the chord lengths $A_0 A_k$ by $S_1, S_2, \dots, S_{17}$ (with diameter $S_{17} = 2$):

.. math::

   S_k = 2\sin\frac{k\pi}{34} = 2\cos\frac{(17 - k)\pi}{34}.

Matching $2\cos\frac{2h\pi}{17} = 2\cos\frac{4h\pi}{34}$ against $S_k$ for $h = 1, 2, \dots, 8$ gives $k = 17 - 4h$, i.e.:

.. math::

   \begin{alignedat}{4}
   z_1 &= +S_{13}, &\quad z_2 &= +S_1, &\quad z_3 &= +S_9, &\quad z_4 &= -S_{15}, \\
   z_5 &= -S_7,    &\quad z_6 &= -S_{11}, &\quad z_7 &= -S_3, &\quad z_8 &= +S_5.
   \end{alignedat}

Since $0 < S_1 < S_2 < \dots < S_{17} = 2$, we read off immediately

.. math::

   z_4 < z_6 < z_5 < z_7 < z_2 < z_8 < z_3 < z_1.

Furthermore, in $\triangle A_0 A_k A_{k+p}$ the triangle inequality gives $S_{k+p} < S_k + S_p$. Forming pairwise differences of $y_1, y_2, y_3, y_4$ yields:

.. math::

   \begin{aligned}
   y_1 - y_2 &= (S_{13} + S_1) - S_9 + S_{15} > 0, \\
   y_1 - y_4 &= S_{13} + S_1 + S_3 - S_5 > 0 \qquad (\text{since } S_{13} > S_5), \\
   y_2 - y_3 &= S_9 - S_{15} + S_7 + S_{11} > 0 \qquad (\text{since } S_9 + S_7 > S_{16} > S_{15}), \\
   y_2 - y_4 &= S_9 - S_{15} + S_3 - S_5 < 0 \qquad (\text{since } S_9 + S_3 < S_{15} + S_5), \\
   y_3 - y_4 &= -S_7 - S_{11} + S_3 - S_5 < 0.
   \end{aligned}

Hence the four $4$-periods obey the strict inequality chain

.. math::

   y_3 < y_2 < y_4 < y_1, \qquad \text{and similarly} \qquad x_2 < x_1.

§ 6. The Tower of Four Quadratic Equations and Normal Radical Form
------------------------------------------------------------------

**6.** Using the symbolic product rule $\varepsilon_k \cdot \varepsilon_p = \varepsilon_{k+p \pmod{17}}$ and $\sum_{k=1}^{16} \varepsilon_k = -1$, we compute the elementary symmetric functions at each level:

1. **First quadratic $(\xi)$ for $x_1, x_2$:** $x_1 + x_2 = -1$, and in the $64$-term expansion of $x_1 x_2$ every primitive root $\varepsilon_1, \dots, \varepsilon_{16}$ occurs exactly $4$ times, so $x_1 x_2 = -4$. Thus $x_1 > x_2$ solve

   .. math::

      (\xi) \qquad x^2 + x - 4 = 0 \implies x_1 = \frac{-1 + \sqrt{17}}{2}, \quad x_2 = \frac{-1 - \sqrt{17}}{2}.

2. **Second quadratic $(\eta)$ for $y_1, y_2$:** $y_1 + y_2 = x_1$, and expanding $y_1 y_2 = (13 + 16 + 4 + 1)(9 + 15 + 8 + 2)$ yields each of the $16$ roots once, so $y_1 y_2 = -1$. Since $y_1 > y_2$:

   .. math::

      (\eta) \qquad y^2 - x_1 y - 1 = 0 \implies y_1 = \frac{x_1 + \sqrt{x_1^2 + 4}}{2}, \quad y_2 = \frac{x_1 - \sqrt{x_1^2 + 4}}{2}.

3. **Third quadratic $(\eta')$ for $y_4, y_3$:** Similarly $y_3 + y_4 = x_2$ and $y_3 y_4 = -1$. Since $y_4 > y_3$:

   .. math::

      (\eta') \qquad y^2 - x_2 y - 1 = 0 \implies y_4 = \frac{x_2 + \sqrt{x_2^2 + 4}}{2}, \quad y_3 = \frac{x_2 - \sqrt{x_2^2 + 4}}{2}.

4. **Fourth quadratic $(\zeta)$ for $z_1, z_2$:** $z_1 + z_2 = y_1$, and $z_1 z_2 = (16 + 1)(13 + 4) = 12 + 3 + 14 + 5 = y_4$. Since $z_1 > z_2$:

   .. math::

      (\zeta) \qquad z^2 - y_1 z + y_4 = 0 \implies z_1 = \frac{y_1 + \sqrt{y_1^2 - 4y_4}}{2}, \quad z_2 = \frac{y_1 - \sqrt{y_1^2 - 4y_4}}{2}.

Thus $z_1 = 2\cos\frac{2\pi}{17}$ appears to involve four square roots: $\sqrt{17}$, $\sqrt{x_1^2 + 4}$, $\sqrt{x_2^2 + 4}$, and $\sqrt{y_1^2 - 4y_4}$. Are these four radicals algebraically independent? Expanding symbolically $(y_1 - y_2)(y_4 - y_3)$ across all $64$ signed terms gives $2(x_1 - x_2)$, i.e.:

.. math::

   (y_1 - y_2)(y_4 - y_3) = 2(x_1 - x_2) \iff \sqrt{x_1^2 + 4}\,\sqrt{x_2^2 + 4} = 2\sqrt{17}.

Hence $\sqrt{x_2^2 + 4}$ is rationally expressible in terms of $\sqrt{17}$ and $\sqrt{x_1^2 + 4}$ (confirming that $z_1$ satisfies an irreducible equation of degree $8 = 2^3$, not $16$). Substituting the numerical values yields the explicit nested radical chain:

.. math::

   \begin{aligned}
   x_1 &= \frac{-1 + \sqrt{17}}{2}, \\[4pt]
   y_1 &= \frac{-1 + \sqrt{17} + \sqrt{34 - 2\sqrt{17}}}{4}, \qquad
   y_4 = \frac{-1 - \sqrt{17} + \sqrt{34 + 2\sqrt{17}}}{4}, \\[6pt]
   z_1 &= 2\cos\frac{2\pi}{17} = \frac{-1 + \sqrt{17} + \sqrt{34 - 2\sqrt{17}}}{8} \\
       &\quad + \frac{1}{8}\sqrt{68 + 12\sqrt{17} - 16\sqrt{34 + 2\sqrt{17}} - 2(1 - \sqrt{17})\sqrt{34 - 2\sqrt{17}}}.
   \end{aligned}

§ 7. Historical Excursion on Restricted Instruments (Mascheroni, Brianchon, Poncelet, Steiner)
----------------------------------------------------------------------------------------------

**7.** Before translating these four quadratic equations into geometry, we insert a brief historical excursion on constructions with straightedge and compasses:

* In **ancient geometry**, straightedge and compasses were always employed side by side without distinguishing whether individual steps used one instrument or the other; the geometer's art lay simply in arranging the parts of a figure so as to avoid superfluous lines.
* In **1797**, the Italian geometer :person:`Lorenzo Mascheroni <mascheroni>` succeeded in executing all Euclidean constructions **with the compasses alone** in his :cite:`*Geometria del compasso* <mascheroni:1797>`, arguing that for instrument-makers and mechanics divider-arcs are practically more accurate than ruled lines. (Because Mascheroni's original treatise is prolix, Hutt provided a concise German summary, *Die Mascheroni'schen Constructionen*, Halle, 1880.)
* Conversely, in France the disciples of Carnot (*Géométrie de position*) strove to accomplish as much as possible **with the straightedge alone** (compare also :person:`Lambert <lambert>`, *Freie Perspective*, 1774, and :person:`Brianchon <brianchon>`, *Les applications de la théorie des transversales*, 1818, motivated by field surveying). Algebra answers immediately what pure straightedge lines can achieve: **with the straightedge alone we can construct precisely those algebraic expressions whose form is rational**.
* Finally, :person:`Poncelet <poncelet>` first conceived in his :cite:`*Traité des propriétés projectives* (1822, Vol. I, Nos. 351–357) <poncelet:1822>` the fundamental theorem—developed systematically by :person:`Steiner <steiner>` in his celebrated monograph :cite:`*Die geometrischen Constructionen, ausgeführt mittels der geraden Linie und eines festen Kreises* (1833) <steiner:1833>`—that **a single fixed circle with given center, together with the straightedge alone, suffices to construct every algebraic expression built from rational operations and square roots** (the :term:`Poncelet–Steiner theorem <poncelet-steiner-theorem>`).

§§ 8–9. The von Staudt–Schröter Single-Circle Construction of the 17-Gon
------------------------------------------------------------------------

**8.** To construct the regular $17$-gon with a **single fixed circle and straightedge alone**, we follow the elegant projective method of :person:`Karl Georg Christian von Staudt <staudt>` (:cite:`*Crelle's Journal*, Vol. XXIV, 1842 <staudt:1842>`), as modified by :person:`Heinrich Schröter <schroeter>` (:cite:`*Crelle's Journal*, Vol. LXXV, 1872 <schroeter:1872>`). (A Mascheroni compass-only construction of the regular $17$-gon was subsequently published by L. Gérard in *Mathematische Annalen*, Vol. XLVIII, 1896, pp. 390–392.)

Let the fixed unit circle have diameter $OA$ along the $Y$-axis ($O = (0, 0)$, center $C_0 = (0, 1)$, upper pole $A = (0, 2)$), with lower horizontal tangent $y = 0$ (the $X$-axis) and upper horizontal tangent $y = 2$:

.. math::

   x^2 + y(y - 2) = 0.

To solve any quadratic equation $x^2 - px + q = 0$ having real roots $x_1, x_2$:

1. Lay off on the upper tangent $y = 2$ (from $A$) the abscissa $\frac{4}{p}$, and on the lower tangent $y = 0$ (from $O$) the abscissa $\frac{q}{p}$.
2. Connect $\left(\frac{4}{p}, 2\right)$ and $\left(\frac{q}{p}, 0\right)$ by the transversal **line 3**, meeting the fixed circle in two points.
3. Project those two circle intersections from the upper pole $A(0, 2)$ by **lines 1 and 2** onto the $X$-axis $y = 0$: the intercepts cut off on the $X$-axis are precisely $x_1$ and $x_2$!

.. picture:: /_static/figures/fig_von_staudt_quadratic.svg
   :alt: Von Staudt-Schroeter Projective Quadratic Solver on the Fixed Circle C_0
   :caption: Von Staudt–Schröter Quadratic Solver (Klein § 8, Fig. 4): Transversal 3 joining (q/p, 0) and (4/p, 2) cuts C_0 in two points whose stereographic projections from A(0, 2) mark roots x_1, x_2 of x^2 - px + q = 0 on y = 0.

*Proof.* The projecting rays $1$ and $2$ from $A(0, 2)$ to $(x_1, 0)$ and $(x_2, 0)$ have equations $2x + x_1(y - 2) = 0$ and $2x + x_2(y - 2) = 0$. Multiplying them gives the degenerate conic

.. math::

   x^2 + \frac{x_1 + x_2}{2} x(y - 2) + \frac{x_1 x_2}{4}(y - 2)^2 = 0.

Subtracting the circle $x^2 + y(y - 2) = 0$ produces another conic through the four common points of the line-pair and the circle; factoring out the double-point tangent $y - 2 = 0$ at $A$ leaves the secant **line 3**:

.. math::

   \frac{x_1 + x_2}{2} x + \frac{x_1 x_2}{4}(y - 2) - y = 0 \iff \frac{p}{2}x + \frac{q}{4}(y - 2) - y = 0.

Setting $y = 2$ gives $x = \frac{4}{p}$, and setting $y = 0$ gives $x = \frac{q}{p}$. $\blacksquare$

**9.** We now apply this single-circle solver successively to $(\xi)$, $(\eta)$, $(\eta')$, and $(\zeta)$, needing only $x_1, x_2, y_1, y_4$, and $z_1$. On the upper tangent $y = 2$ and lower tangent $y = 0$ we require the successive abscissas:

.. math::

   \begin{array}{lcccc}
   \text{Upper tangent } (y = 2): & -4, & \dfrac{4}{x_1}, & \dfrac{4}{x_2}, & \dfrac{4}{y_1}, \\[8pt]
   \text{Lower tangent } (y = 0): & +4, & -\dfrac{1}{x_1}, & -\dfrac{1}{x_2}, & \dfrac{y_4}{y_1}.
   \end{array}

* **Step 1 — Solving $(\xi): x^2 + x - 4 = 0$ ($p = -1, q = -4$):** Connect $(+4, 0)$ below with $(-4, 2)$ above (which passes directly through the circle center $(0, 1)$). Projecting its two intersections with the fixed circle from $A(0, 2)$ cuts off $x_1 > 0$ and $x_2 < 0$ on the $X$-axis.
* **Projective Inversion $x' = \frac{4}{x}$ (Fig. 5):** For any abscissa $x$ on $y = 0$, the ray from $A(0, 2)$ to $(x, 0)$ meets the circle again at $\left(\frac{4x}{x^2 + 4}, \frac{2x^2}{x^2 + 4}\right)$, and projecting that circle point from $O(0, 0)$ onto the upper tangent $y = 2$ cuts off $x' = \frac{4}{x}$! Projectively, $x \mapsto x'$ is a perspective one-to-one correspondence sending $x = \infty \leftrightarrow x' = 0$ and fixing $x = x' = 2$, whence $x' = \frac{4}{x}$. Thus projecting the circle points already belonging to $x_1$ and $x_2$ from $O(0, 0)$ onto $y = 2$ immediately yields $\frac{4}{x_1}$ and $\frac{4}{x_2}$!
* **Step 2 — Solving $(\eta): y^2 - x_1 y - 1 = 0$ (Fig. 6):** Join $(-4, 2)$ above to $(+1, 0)$ below ($5y + 2x = 2$), cutting the vertical diameter $OA$ at the fixed division point $H = \left(0, \frac{2}{5}\right)$. Joining $\left(\frac{4}{x_1}, 2\right)$ through $\left(0, \frac{2}{5}\right)$ ($5y - 2x_1 x = 2$) meets $y = 0$ at $-\frac{1}{x_1}$! Now connect $\left(-\frac{1}{x_1}, 0\right)$ to $\left(\frac{4}{x_1}, 2\right)$ and project the upper circle intersection from $A(0, 2)$ onto $y = 0$ to obtain $y_1$.
* **Step 3 — Solving $(\eta'): y^2 - x_2 y - 1 = 0$ (Fig. 7):** Likewise join $\left(\frac{4}{x_2}, 2\right)$ through the same division point $\left(0, \frac{2}{5}\right)$ to cut off $-\frac{1}{x_2}$ on $y = 0$. Connect $\left(-\frac{1}{x_2}, 0\right)$ to $\left(\frac{4}{x_2}, 2\right)$ and project the positive-quadrant circle intersection from $A(0, 2)$ onto $y = 0$ to obtain $y_4$.
* **Step 4 — Solving $(\zeta): z^2 - y_1 z + y_4 = 0$ and Inscribing the $17$-Gon (Figs. 8–9):** Project the circle intersection on ray $A y_1$ from $O(0, 0)$ onto $y = 2$ to get $\frac{4}{y_1}$. Join $(+4, 2)$ above to $(y_4, 0)$ below, meeting the vertical axis $x = 0$ at $\left(0, \frac{2y_4}{y_4 - 4}\right)$; then join that axial point to $\left(\frac{4}{y_1}, 2\right)$ ($2y_1 x + (y_4 - 4)y = 2y_4$) to cut off $\frac{y_4}{y_1}$ on $y = 0$! Connecting $\left(\frac{y_4}{y_1}, 0\right)$ to $\left(\frac{4}{y_1}, 2\right)$ and projecting the upper circle intersection from $A(0, 2)$ cuts off $z_1 = 2\cos\frac{2\pi}{17}$ on $y = 0$, and simultaneously cuts off **$\cos\frac{2\pi}{17}$ directly on the horizontal diameter $y = 1$**! Erecting the perpendicular chord at $x = \cos\frac{2\pi}{17}$ immediately marks the **first and sixteenth vertices** $V_1, V_{16}$ of the regular $17$-gon on the fixed circle!

.. picture:: /_static/figures/fig_von_staudt_17gon.svg
   :alt: Complete Single-Circle Construction of the Regular Heptadecagon (17-Gon) in geometor.model
   :caption: Complete Single-Circle Construction of the Regular 17-Gon (Klein § 9, Fig. 9; rendered from geometor.klein.heptadecagon): Fixed circle C_0, periods X_1, X_2, Y_1, Y_4, Z_1, midpoint K_1 = (cos 2pi/17, 1), and all 17 exact vertices V_0..V_16.
