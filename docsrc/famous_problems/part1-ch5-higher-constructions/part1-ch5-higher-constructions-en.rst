:title: Part I, Ch. V: General Considerations on Algebraic Constructions (1897 English)
:layout: book

.. _fp-part1-ch5-higher-constructions-en:

Part I, Chapter V — General Considerations on Algebraic Constructions
=====================================================================

.. rubric:: Part I, Chapter V (§§ 1–5; :cite:`Ginn & Co., 1897, pp. 42–48 <klein:1897>`)

§ 1. Paper Folding (Wiener and Sundara Row)
-------------------------------------------

**1.** We now lay aside constructions restricted to straightedge and compasses. Before leaving elementary methods altogether, however, we mention a new and remarkably simple geometric procedure: **paper folding**. :person:`Hermann Wiener <wiener>` showed how by folding paper one may obtain the planar nets of all the regular polyhedra (see W. Dyck, *Katalog der Münchener mathematischen Ausstellung von 1893*, Nachtrag, p. 52). Singularly, around the very same time an Indian mathematician, :person:`T. Sundara Row <sundara-row>` of Madras, published a suggestive little treatise, :cite:`*Geometrical Exercises in Paper Folding* (Madras: Addison & Co., 1893) <sundara-row:1893>`, developing the same idea systematically and showing how to construct by points curves such as the ellipse, the cissoid, and others.

§ 2. Solving Cubic and Biquadratic Equations by Conic Sections
--------------------------------------------------------------

**2.** Let us now inquire by what geometric instruments problems leading to equations of the **third or higher degree** can be solved, and in particular how the ancients succeeded in solving the :term:`duplication of the cube <delian-problem>` and the trisection of the angle.

The most natural auxiliaries—extensively cultivated in antiquity—are the **conic sections**. Expressed in modern analytic language, suppose we wish to solve graphically either the cubic equation

.. math::

   x^3 + a x^2 + b x + c = 0

or the biquadratic (quartic) equation

.. math::

   x^4 + a x^3 + b x^2 + c x + d = 0.

Setting $x^2 = y$ reduces the two equations respectively to

.. math::

   x y + a y + b x + c = 0 \qquad \text{and} \qquad y^2 + a x y + b y + c x + d = 0.

In both cases the roots $x$ are the abscissas of the intersections of **two conics**:

* The fixed **parabola** $x^2 = y$ with vertical axis.
* For the **cubic** (Fig. 10), the **hyperbola** $xy + ay + bx + c = 0$, whose asymptotes are parallel to the coordinate axes. Of the four intersections required by Bézout's theorem, one lies at infinity on the $Y$-axis, leaving **three finite intersections** whose abscissas are the three roots of the cubic.
* For the **biquadratic** (Fig. 11), the hyperbola $y^2 + axy + by + cx + d = 0$ retains the horizontal asymptote while its second asymptote is inclined; all **four intersections** with $x^2 = y$ now lie at finite distance.

(For the historical methods of the Greek geometers, see M. Cantor, *Geschichte der Mathematik*, Leipzig, 1894, 2nd ed.; H. G. Zeuthen, *Die Kegelschnitte im Altertum*, Copenhagen, 1886; and R. Baltzer, *Analytische Geometrie*, Leipzig, 1882.)

§ 3. The Cissoid of Diocles and the Delian Problem
--------------------------------------------------

**3.** Besides conic sections, the ancients invented higher algebraic curves expressly to solve solid problems, notably the :term:`cissoid <cissoid>` and the :term:`conchoid <conchoid>`.

The **cissoid of** :person:`Diocles <diocles>` (c. 150 B.C., Fig. 12) is traced from a circle of unit diameter tangent at $(1, 0)$ to the vertical line $x = 1$ and passing through the origin $O(0, 0)$. Through the vertex $O$ draw any ray at angle $\theta$ to the $X$-axis, meeting the circle at distance $\cos\theta$ and the vertical tangent $x = 1$ at distance $\frac{1}{\cos\theta}$, and lay off from $O$ along the ray the difference $r$ of those two segments:

.. math::

   r = \frac{1}{\cos\theta} - \cos\theta = \frac{\sin^2\theta}{\cos\theta}.

Passing to Cartesian coordinates ($x = r\cos\theta$, $y = r\sin\theta$) yields the cubic equation

.. math::

   (x^2 + y^2)x - y^2 = 0.

The cissoid is an algebraic curve of the **third order**, symmetric about the $X$-axis, with a **cusp** at the origin $O$, having the vertical line $x = 1$ as asymptote, and cutting the line at infinity in the two imaginary **circular points**.

.. picture:: /_static/figures/fig_conchoid_cissoid.svg
   :alt: Classical Higher Curves: Cissoid of Diocles for Cube Duplication and Conchoid of Nicomedes for Angle Trisection
   :caption: Classical Higher Algebraic Curves (Klein Ch. V, §§ 3–4, Figs. 12–13): Left — Cissoid of Diocles (x^2 + y^2)x - y^2 = 0 constructing the cube root of 2; Right — Conchoid of Nicomedes trisecting angle MOY with exact Bezout root count 8 - 2 - 2 - 1 = 3.

To solve the :term:`Delian problem <delian-problem>` by means of the cissoid, rewrite its equation in the form

.. math::

   \left(\frac{y}{x}\right)^3 = \frac{y}{1 - x}.

A ray $\frac{y}{x} = \lambda$ through the origin cuts off the ordinate $\lambda$ on the vertical asymptote $x = 1$, and meets the cissoid at a point satisfying $\frac{y}{1 - x} = \lambda^3$. Now $\frac{y}{1 - x} = \lambda^3$ is the equation of the straight line joining $(1, 0)$ to that cissoid point, which cuts off on the $Y$-axis ($x = 0$) the intercept $\lambda^3$! Reversing the steps constructs $\sqrt[3]{2}$ immediately:

1. Lay off the intercept $2$ on the $Y$-axis at $(0, 2)$ and join $(0, 2)$ to $(1, 0)$.
2. Mark the intersection $P$ of that segment with the cissoid.
3. Draw the ray $OP$ from the origin to the vertical tangent $x = 1$: the ordinate cut off on $x = 1$ equals $\sqrt[3]{2}$.

§ 4. The Conchoid of Nicomedes and Angle Trisection
---------------------------------------------------

**4.** The **conchoid of** :person:`Nicomedes <nicomedes>` (c. 150 B.C., Fig. 13) is generated from a fixed pole $O(0, 0)$ at perpendicular distance $a$ from a fixed line $x = a$. Through $O$ pass a pencil of rays and lay off on each ray, in both directions from its intersection with $x = a$, a constant segment $b$. Depending on whether $b > a$, $b < a$, or $b = a$, the origin $O$ is a **node** (looped branch), an **isolated conjugate point**, or a **cusp**. From the proportion $r : x = \pm b : (x - a)$ we obtain the Cartesian equation

.. math::

   (x^2 + y^2)(x - a)^2 - b^2 x^2 = 0.

The conchoid is thus of the **fourth order**, has a double point at the origin $O$ and two branches asymptotic to $x = a$, and—by virtue of the factor $(x^2 + y^2)$—passes through the **circular points at infinity**.

To **trisect any given angle** $\varphi = \angle MOY$:

1. On the inclined side $OM$, lay off an arbitrary length $OM = b$.
2. With center $M$ and radius $b$, describe a circle, and through $M$ draw the vertical line $x = a$ ($a = b\sin\varphi$) perpendicular to the $X$-axis as asymptote of the conchoid with pole $O$ and interval $b$.
3. Connect $O$ to the intersection $A$ of the circle and the outer branch of the conchoid: then $\angle AOY = \frac{1}{3}\varphi$! (Indeed, if $N$ is where $OA$ meets the vertical line $x = a$, then $NA = b = MA$ and $\triangle NMA$ is isosceles while $\angle OMN = 90^\circ$ gives the exterior-angle relation $\varphi = 3\,\angle AOY$.)

**Algebraic Counting of Intersections:** Our earlier Galois analysis showed that angle trisection is an irreducible problem of the **third degree**, admitting the three roots $\frac{\varphi}{3}, \frac{\varphi + 2\pi}{3}, \frac{\varphi + 4\pi}{3}$. Every algebraic curve construction must necessarily furnish *all three* roots simultaneously—otherwise the trisection cubic would split! Let us verify this in the figure:

* The circle (degree $2$) and conchoid (degree $4$) intersect in $2 \times 4 = 8$ points.
* **Two** intersections fall at the double point $O(0, 0)$, and **two** fall at the imaginary circular points at infinity—none of which solve our problem, leaving $8 - 2 - 2 = 4$ finite intersections.
* Among these four finite points lies the collinear point $B$ on ray $OM$ extended ($OMB = 2b$), which is constructible rationally beforehand without the curve.
* Removing $B$ leaves **precisely $3$ intersections**, corresponding to the three algebraic roots $\frac{\varphi}{3}, \frac{\varphi + 2\pi}{3}, \frac{\varphi + 4\pi}{3}$!

§ 5. Continuous Mechanical Instruments vs. Pointwise Approximation
------------------------------------------------------------------

**5.** Whenever higher algebraic curves are invoked for geometric construction, practical execution demands an **instrument that traces the curve by a continuous movement**; plotting isolated points and joining them freehand is merely an approximation method, not an exact construction. :person:`Nicomedes <nicomedes>` himself invented a simple mechanical trammel for tracing the conchoid—the oldest curve-drawing mechanism known after straightedge and compasses (M. Cantor, Vol. I, p. 302; compare :person:`Pappus <pappus>`, :cite:`*Collection*, Book IV <pappus:collection>`). Modern linkages and curve-tracers are catalogued in W. Dyck's *Katalog* (pp. 227–230, 340; Nachtrag, pp. 42–43).
