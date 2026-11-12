:title: Prefaces & Introduction (1897 English)
:layout: book

.. _fp-intro-en:

Famous Problems of Elementary Geometry — Prefaces & Introduction
================================================================

.. rubric:: *The Duplication of the Cube, The Trisection of an Angle, The Quadrature of the Circle* — Authorized Translation of :person:`F. Klein's <klein>` *Vorträge über ausgewählte Fragen der Elementargeometrie*, ausgearbeitet von :person:`F. Tägert <taegert>`, by :person:`W. W. Beman <beman>` and :person:`D. E. Smith <smith>` (:cite:`Boston & London: Ginn & Co., 1897, pp. iii–ix, 1–4 <klein:1897>`)

Author's Preface (Easter, 1895)
-------------------------------

At Easter, 1895, the usual holiday course for teachers of mathematics and physics in the higher schools was held in Göttingen. In my lectures in connection with this course I discussed certain famous problems of elementary geometry, with the special purpose of showing how modern mathematics views the question of the possibility of geometric constructions with straightedge and compasses.

:person:`Herr Oberlehrer Tägert <taegert>`, of Ems, who attended the lectures, worked out his notes with great care directly afterward, and thus produced the present little volume, which is now published as a *Festschrift* for the third general meeting of the *Verein zur Förderung des mathematischen und naturwissenschaftlichen Unterrichts*, to be held in Göttingen at Whitsuntide, 1895 (:cite:`Leipzig: B. G. Teubner, 1895 <klein:1895>`).

May this modest work contribute in wider circles toward bringing university research in mathematics into closer touch with the instruction of the schools!

Göttingen, Easter, 1895. — :person:`F. KLEIN <klein>`.

Translators' Preface (July, 1897)
---------------------------------

Ever since :person:`Professor Felix Klein <klein>` came to America in the summer of 1893 as the official commissioner of the German university exhibit at the World's Columbian Exposition in Chicago, and conducted his memorable Evanston Colloquium after the Congress of Mathematics, teachers throughout the English-speaking world have followed his educational writings with the keenest interest.

In these Göttingen lectures of 1895, Professor Klein brings the decisive methods of modern algebra, number theory, and analysis directly to bear upon the three most celebrated geometric problems handed down from Greek antiquity:

1. **The Duplication of the Cube** (:term:`the Delian problem <delian-problem>`),
2. **The Trisection of an Arbitrary Angle**, and
3. **The Quadrature of the Circle** (together with the division of the circle into $n$ equal parts).

No problems in elementary geometry arouse livelier curiosity in the student, yet almost nowhere in elementary textbooks are rigorous, accessible proofs of their impossibility under Euclidean postulates to be found. With Professor Klein's cordial authorization and kind revision of the proofs, we offer this faithful English rendering of his monograph in the hope that it may prove serviceable alike to teachers of geometry and to university students entering higher algebra.

:person:`WOOSTER WOODRUFF BEMAN <beman>` (University of Michigan, Ann Arbor) · :person:`DAVID EUGENE SMITH <smith>` (Michigan State Normal School, Ypsilanti), July, 1897.

Introduction
------------

1. Practical and Theoretical Constructions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the study of geometric constructions it is essential from the very outset to draw a sharp distinction between **practical** and **theoretical** constructibility.

If we wish merely to execute a figure *practically*—as is required in geodesy, physical measurement, or mechanical drawing—any graduated scale, protractor, pantograph, or numerical table suffices to reach whatever degree of accuracy the imperfection of our physical senses and drawing instruments allows. From this empirical standpoint, trisecting a given angle with a divided circle or laying off $\pi = 3.14159\dots$ from a finely divided millimeter rule presents no difficulty whatever; every construction is an approximation bounded by an unavoidable margin of physical error.

Wholly different is the question of **theoretical constructibility**. Here we ask a strictly mathematical question of exact logic: *Can a required magnitude be determined with absolute rigor by applying a prescribed, sharply restricted set of ideal geometric operations a finite number of times?* In classical elementary geometry since :person:`Euclid <euclid>` (:cite:`*Elements*, Book I, Postulates 1–3 <euclid:elements>`), these prescribed operations are exclusively the drawing of straight lines through given points (**the unmarked straightedge**) and the describing of circles with given centers and radii (**the compasses**).

Now among the most famous problems bequeathed to us by antiquity are the **duplication of the cube** (:term:`the Delian problem <delian-problem>`), the **trisection of an arbitrary angle**, the **construction of the regular heptagon** ($n = 7$), and the **quadrature of the circle** ($\pi$). In elementary instruction one constantly hears the assertion that these problems *cannot* be solved with straightedge and compasses; yet in the ordinary textbooks one searches in vain for any proof of this impossibility. Almost the solitary exception in the pedagogical literature is :person:`Julius Petersen <petersen>`, who in his admirable works (:cite:`*Methods and Theories for the Solution of Problems of Geometrical Constructions* and *Theorie der algebraischen Gleichungen*, 1878–1879 <petersen:1879>`) presents elementary algebraic proofs of impossibility.

Meanwhile, nineteenth-century mathematics—through the discoveries of :person:`Gauss <gauss>` (:cite:`1801 <gauss:1801>`), :person:`Wantzel <wantzel>` (:cite:`1837 <wantzel:1837>`), :person:`Abel <abel>`, and :person:`Galois <galois>` for algebraic equations, and of :person:`Hermite <hermite>` (:cite:`1873 <hermite:1873>`), :person:`Lindemann <lindemann>` (:cite:`1882 <lindemann:1882>`), :person:`Weierstrass <weierstrass>`, :person:`Hilbert <hilbert>`, :person:`Hurwitz <hurwitz>`, and :person:`Gordan <gordan>` (:cite:`1893 <gordan:1893>`) for :term:`transcendental numbers <transcendental-number>`—has resolved every one of these ancient questions with complete simplicity and finality. To place these decisive proofs within reach of every teacher of mathematics is the aim of the following lectures.

2. Statement of the Problem in Algebraic Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How can one possibly prove that a proposed geometric construction *cannot* be carried out by any finite combination of straight lines and circles, however ingenious? Purely synthetic geometry offers no handle on the totality of all conceivable constructions; **analytic geometry and algebra**, on the other hand, survey that totality at a single stroke.

Suppose a finite system of segments $a, b, c, \dots$ is initially given. Choosing a unit segment (or retaining homogeneous ratios) and introducing rectangular Cartesian axes, every given point has coordinates rational in $a, b, c, \dots$:

* Drawing a **straight line** through two known points produces a linear equation $Ax + By + C = 0$ whose coefficients are rational functions of the coordinates of those points; intersecting two straight lines solves two linear equations and therefore yields coordinates formed purely by **rational operations** (addition, subtraction, multiplication, and division).
* Describing a **circle** with known center and radius produces a quadratic equation $(x - x_0)^2 + (y - y_0)^2 = r^2$; intersecting a straight line with a circle—or intersecting two circles, whose difference immediately yields the linear equation of their common chord—requires solving a quadratic equation and therefore adjoins at most a **square root** of a known expression.

Conversely, every rational combination ($a \pm b$, $\frac{ab}{c}$ via fourth proportionals and parallel lines) and every square root ($\sqrt{ab}$ via the mean proportional in a semicircle) can actually be constructed with straightedge and compasses. Repeating such steps any finite number of times, we arrive at our **Fundamental Theorem**:

.. admonition:: Fundamental Criterion of Euclidean Constructibility

   **An analytic expression is constructible with straightedge and compasses if, and only if, it can be derived from the known quantities by a finite number of rational operations and extractions of square roots.**

Accordingly, to demonstrate that a geometric problem is *impossible* with straightedge and compasses, we translate the problem into an algebraic equation for the unknown segment $x$ and prove that $x$ cannot be expressed by a finite tower of rational operations and square roots. Our inquiry naturally divides into two parts:

* **Part I (Algebraic Expressions):** Problems whose unknown $x$ satisfies an algebraic equation over the :term:`domain of rationality <domain-of-rationality>` of the given data, where we determine the exact algebraic conditions for solvability by square roots—settling the Delian cube, angle trisection, the regular heptagon, and :person:`Gauss's <gauss>` constructible regular $17$-gon.
* **Part II (Transcendental Numbers and $\pi$):** Problems—above all the quadrature and rectification of the circle—whose characteristic constant ($e$ or $\pi$) satisfies *no* algebraic equation with rational coefficients whatsoever, culminating in :person:`Cantor's <cantor>` continuum proof, :person:`Gordan's <gordan>` proofs of :person:`Hermite's <hermite>` and :person:`Lindemann's <lindemann>` theorems, and mechanical integration via :person:`Abdank-Abakanowicz's <abakanowicz>` :term:`integraph <integraph>`.
