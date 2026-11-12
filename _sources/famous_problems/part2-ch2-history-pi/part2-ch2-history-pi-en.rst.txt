:title: Part II, Ch. II: Historical Survey of Efforts to Compute and Construct π (1897 English)
:layout: book

.. _fp-part2-ch2-history-pi-en:

Part II, Chapter II — Historical Survey of the Attempts at the Computation and Construction of π
================================================================================================

.. rubric:: Part II, Chapter II (§§ 1–5; :cite:`Ginn & Co., 1897, pp. 55–60 <klein:1897>`)

Framing the 4000-Year Problem of Quadrature
-------------------------------------------

In Chapter IV we shall prove that $\pi$ belongs to the class of :term:`transcendental numbers <transcendental-number>` whose existence :person:`Cantor <cantor>` established in Chapter I. That proof, first achieved by :person:`Ferdinand Lindemann <lindemann>` in 1882 (:cite:`*Mathematische Annalen*, Vol. XX <lindemann:1882>`), settled definitively a problem that had occupied mathematicians for nearly $4000$ years: **the quadrature of the circle**. Because $\pi$ is not algebraic, it certainly cannot be constructed with straightedge and compasses; quadrature of the circle in the classical sense is impossible.

Yet few chapters of scientific history are more instructive than tracing how these necessarily fruitless efforts to square the circle stimulated major advances across mathematics. Our brief survey follows the admirable monograph of :person:`Ferdinand Rudio <rudio>`, :cite:`*Archimedes, Huygens, Lambert, Legendre. Vier Abhandlungen über die Kreismessung* (Leipzig, 1892) <rudio:1892>`.

§ 1. The Empirical Stage (Ahmes and Antiquity)
----------------------------------------------

**1.** In the earliest **empirical stage**, the ratio of circumference to diameter was sought by direct measurement or rule-of-thumb estimation:

* The oldest extant mathematical document, the **Rhind Papyrus** (c. 2000 B.C.), copied by the scribe **Ahmes**, already states the problem of transforming a circle into a square of equal area: *cut off $\frac{1}{9}$ of the diameter and construct a square upon the remainder*. Equating $\left(\frac{8}{9}d\right)^2 = \frac{\pi}{4}d^2$ yields the remarkably close approximation

  .. math::

     \pi \approx \left(\frac{16}{9}\right)^2 = \frac{256}{81} = 3.16049\dots.

* Much cruder is the round estimate $\pi = 3$ appearing in the Old Testament (1 Kings 7:23; 2 Chronicles 4:2).

§ 2. The Greek Geometers: Archimedes, Huygens, and the Quadratrix
-----------------------------------------------------------------

**2.** The Greeks rose decisively above empiricism. Above all, :person:`Archimedes <archimedes>` in his *Measurement of a Circle* (*Κύκλου μέτρησις*) bounded the circle rigorously between inscribed and circumscribed regular $96$-gons ($3\frac{10}{71} < \pi < 3\frac{1}{7}$). His polygonal method remained standard down to the invention of the differential calculus and received its sharpest geometric refinement from :person:`Christiaan Huygens <huygens>` in *De circuli magnitudine inventa* (1654).

Just as with cube duplication and angle trisection, the Greeks also sought to rectify and square the circle by **higher curves**. Consider first, in modern language, the sinusoid or **integral curve**

.. math::

   y = \arcsin x = \int_0^x \frac{dx}{\sqrt{1 - x^2}},

on which $\pi$ appears directly as a special ordinate of a transcendental function; any continuous mechanical instrument tracing such a curve ("a transcendental apparatus") yields a geometric construction of $\pi$.

The ancients called such a curve a :term:`quadratrix <quadratrix>` (*τετραγωνίζουσα*). The most celebrated is the **quadratrix of Dinostratus** (c. 350 B.C.), originally invented by :person:`Hippias <hippias>` of Elis (c. 420 B.C.) for trisecting angles (Figs. 14–15). Given a unit circle with perpendicular radii $OA$ (along the $X$-axis) and $OB$ (along the $Y$-axis), let a point $M$ move uniformly along radius $OB$ from $O$ to $B$ while a point $L$ moves uniformly along quadrant arc $AB$ from $A$ to $B$, departing and arriving simultaneously. The intersection $P(x, y)$ of ray $OL$ (at angle $\theta$) with the horizontal parallel to $OA$ through $M$ traces the quadratrix. Since $y$ and $\theta$ vary proportionally with $y = 1$ at $\theta = \frac{\pi}{2}$, we have

.. math::

   \theta = \frac{\pi}{2}y \qquad \text{and} \qquad \tan\theta = \frac{y}{x} \implies x = \frac{y}{\tan\!\left(\frac{\pi}{2}y\right)}.

Passing to the limit $y \to 0$ gives the $X$-axis intercept:

.. math::

   x_0 = \lim_{y \to 0} \frac{y}{\tan\!\left(\frac{\pi}{2}y\right)} = \frac{2}{\pi} \iff \frac{\;\frac{\pi}{2}\;}{1} = \frac{1}{x_0}.

Thus the radius $1$ is the **mean proportional** between the quadrant arc $\frac{\pi}{2}$ and the intercept $x_0 = \frac{2}{\pi}$! Without a continuous-motion mechanism to trace the curve, however, the quadratrix remains a geometric restatement of rectification rather than an executable construction (especially at $y = 0$, where ray $OL$ and the horizontal line coincide).

§§ 3–4. Modern Analysis (Euler's Identity) and Irrationality (Lambert, Legendre)
--------------------------------------------------------------------------------

**3.** The century from **1670 to 1770**—marked by :person:`Leibniz <leibniz>`, Newton, and :person:`Euler <euler>`—created modern analysis and infinite series, yielding abundant series representations for $\pi$ such as the Leibniz–Gregory series:

.. math::

   \frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots.

Above all, this era uncovered the deep analytic bond between **$e$ and $\pi$**. Natural logarithms and the base $e$ had entered in principle with Napier (1614), seemingly unrelated to circular arcs, until :person:`Euler <euler>` had the boldness to introduce imaginary exponents and discovered

.. math::

   e^{ix} = \cos x + i\sin x, \qquad \text{whence for } x = \pi: \qquad e^{i\pi} = -1\quad \bigl(1 + e^{i\pi} = 0\bigr).

This formula—one of the most remarkable in all mathematics—is the indispensable bridge for every modern transcendence proof of $\pi$, which always begins by establishing properties of the exponential function $e^z$.

**4.** After **1770**, critical rigor reclaimed its place: in 1770 :person:`Johann Heinrich Lambert <lambert>` published *Vorläufige Kenntnisse für die, so die Quadratur des Cirkuls suchen*, proving via continued fractions that $\pi$ is **irrational**, and in 1794 :person:`Adrien-Marie Legendre <legendre>` (*Éléments de géométrie*) proved conclusively that both $\pi$ and $\pi^2$ are irrational.

§ 5. Transcendence Proofs from Hermite (1873) and Lindemann (1882) to 1893
--------------------------------------------------------------------------

**5.** Another century elapsed before the problem was conquered at its algebraic root:

* In **1873**, :person:`Charles Hermite <hermite>` published :cite:`*Sur la fonction exponentielle* (*Comptes rendus*, 1873; separate memoir 1874) <hermite:1873>`, proving the **transcendence of $e$**.
* In **1882**, closely extending Hermite's analytic approximations, :person:`Ferdinand Lindemann <lindemann>` published :cite:`*Über die Zahl $\pi$* (*Mathematische Annalen*, Vol. XX, 1882) <lindemann:1882>`, proving the **transcendence of $\pi$** and settling the ancient quadrature problem forever.
* Because Hermite's and Lindemann's original memoirs were analytically intricate, :person:`Karl Weierstrass <weierstrass>` gave a first simplification (*Berliner Berichte*, 1885), incorporated into :person:`Paul Bachmann's <bachmann>` textbook *Vorlesungen über die Natur der Irrationalzahlen* (1892).
* Finally, the **spring of 1893** brought decisive elementary simplifications: first :person:`David Hilbert <hilbert>` (*Göttinger Nachrichten*, 1893), whose proof still retained a last analytic vestige of Hermite's integrals in the gamma identity

  .. math::

     \int_0^\infty z^\rho e^{-z}\,dz = \rho!,

  and immediately thereafter :person:`Adolf Hurwitz <hurwitz>` and :person:`Paul Gordan <gordan>` (*Göttinger Nachrichten*; *Comptes rendus*; all three collected in :cite:`*Mathematische Annalen*, Vol. XLIII, 1893 <gordan:1893>`), who eliminated integration altogether! In Chapters III and IV we follow **Gordan's purely elementary presentation**.
