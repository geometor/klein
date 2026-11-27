:title: Part I, Ch. II: The Delian Problem & Angle Trisection (1897 English)
:layout: book
:canonical_id: Ch. II
:order: 2
:tracks: English: ch_02-en | German: ch_02-de | Summary: ch_02-summary | Notes: ch_02-notes

.. _fp-part_1-ch_02-en:
.. _fp-part1-ch_02-en:
.. _fp-ch_02-en:
.. _fp-part1-ch2-delian-trisection-en:

Part I, Chapter II — The Delian Problem and the Trisection of the Angle
=======================================================================

.. rubric:: Part I, Chapter II (§§ 1–3; :cite:`Ginn & Co., 1897, pp. 13–15 <klein:1897>`)

§ 1. The Impossibility of Solving the Delian Problem with Straightedge and Compasses
------------------------------------------------------------------------------------

**1.** Let us apply the general theorem established in Chapter I immediately to the celebrated :term:`Delian problem <delian-problem>`: **the duplication of the cube**. Legend relates that during a plague at Athens, the oracle of Apollo at Delos commanded the citizens to double the volume of his cubical altar while retaining its cubical shape.

Taking the edge of the given cube as the unit of length (:math:`1`), its volume is :math:`1`; the sought edge :math:`x` of a cube of double volume must therefore satisfy the cubic equation

.. math::

   x^3 = 2, \qquad \text{or} \qquad x^3 - 2 = 0.

According to Chapter I, § 15, this equation cannot be solved by square roots—and therefore cannot be constructed with straightedge and compasses—provided :math:`x^3 - 2 = 0` is **irreducible** over the rational numbers. Now if a cubic polynomial with rational coefficients were reducible, at least one of its factors would have to be of the first degree, so the equation :math:`x^3 = 2` would possess a rational root :math:`x = \frac{p}{q}`, where :math:`p` and :math:`q` are integers relatively prime to each other (:math:`\gcd(p, q) = 1`). Substituting :math:`x = \frac{p}{q}` yields

.. math::

   p^3 = 2 q^3.

Hence :math:`p^3`, and therefore :math:`p` itself, must be an even integer: :math:`p = 2 p'`. Substituting this back gives :math:`8 p'^3 = 2 q^3`, or

.. math::

   4 p'^3 = q^3,

which forces :math:`q^3`, and hence :math:`q`, likewise to be even—contradicting our assumption that :math:`p` and :math:`q` have no common factor! Consequently, :math:`x^3 - 2 = 0` has no rational root; it is irreducible of degree :math:`3`, and since :math:`3` is not a power of :math:`2`, **the Delian problem cannot be solved with straightedge and compasses**.

§ 2. The General Equation :math:`x^3 = \lambda`
-----------------------------------------------

**2.** Before passing to the trisection of the angle, let us consider more generally the equation

.. math::

   x^3 = \lambda,

where :math:`\lambda` is no longer a fixed integer like :math:`2`, but an **arbitrary variable parameter** (capable of assuming real or complex values). What do we mean here by "rational operations" and "irreducibility"? Following Kronecker, we take as our :term:`domain of rationality <domain-of-rationality>` (*Rationalitätsbereich*) the totality of all rational functions of the parameter :math:`\lambda`—that is, quotients :math:`\frac{f(\lambda)}{\psi(\lambda)}` in which :math:`f(\lambda)` and :math:`\psi(\lambda)` are polynomials in :math:`\lambda`. All the theorems of Chapter I remain valid verbatim over this domain of rationality: an expression in :math:`\lambda` constructible universally with straightedge and compasses must satisfy an equation irreducible over the rational functions of :math:`\lambda` whose degree is a power of :math:`2`.

Now if :math:`x^3 - \lambda = 0` were reducible over this domain of rationality, at least one factor would be linear in :math:`x`, so some rational function :math:`x = \frac{f(\lambda)}{\psi(\lambda)}` (reduced to lowest terms, so that the polynomials :math:`f(\lambda)` and :math:`\psi(\lambda)` share no common factor) would satisfy

.. math::

   [f(\lambda)]^3 = \lambda \, [\psi(\lambda)]^3.

Comparing polynomial degrees on both sides gives :math:`3 \deg f = 1 + 3 \deg \psi`, which is impossible for integers (or equivalently, :math:`\lambda` divides :math:`[f(\lambda)]^3`, hence divides :math:`f(\lambda)`, whence :math:`\lambda^3` divides :math:`\lambda [\psi(\lambda)]^3`, forcing :math:`\lambda` to divide :math:`\psi(\lambda)` as well). Under our hypothesis of variable :math:`\lambda`, the equation :math:`x^3 - \lambda = 0` is therefore **irreducible**, and since its degree :math:`3` is not of the form :math:`2^h`, **it cannot be solved by square roots**.

§ 3. The Impossibility of Trisecting an Angle with Straightedge and Compasses
-----------------------------------------------------------------------------

**3.** Let us now separate the complex variability of :math:`\lambda` into modulus and argument by setting

.. math::

   \lambda = r(\cos\varphi + i\sin\varphi), \qquad \text{whence} \qquad \sqrt[3]{\lambda} = \sqrt[3]{r}\,\sqrt[3]{\cos\varphi + i\sin\varphi}.

Our problem resolves itself into two distinct geometric problems—extracting the cube root of an arbitrary positive real number :math:`r`, and extracting the cube root of an arbitrary unit complex number :math:`\cos\varphi + i\sin\varphi`—which we treat separately.

**I. General Multiplication of the Cube** (:math:`x^3 = r`).
The three roots of :math:`x^3 = r` are

.. math::

   \sqrt[3]{r}, \qquad \varepsilon\sqrt[3]{r}, \qquad \varepsilon^2\sqrt[3]{r},

where :math:`\varepsilon` and :math:`\varepsilon^2` denote the primitive complex cube roots of unity:

.. math::

   \varepsilon = \frac{-1 + i\sqrt{3}}{2}, \qquad \varepsilon^2 = \frac{-1 - i\sqrt{3}}{2}.

Taking for our :term:`domain of rationality <domain-of-rationality>` the totality of rational functions of :math:`r`, we know by § 2 that :math:`x^3 = r` is irreducible of degree :math:`3`. Hence *the problem of multiplying the cube by an arbitrary ratio* :math:`r` *does not admit, in general, of a construction by means of straightedge and compasses*.

**II. Trisection of the Angle** (:math:`x^3 = \cos\varphi + i\sin\varphi`).
By De Moivre's formula, the three roots of the equation :math:`x^3 = \cos\varphi + i\sin\varphi` are

.. math::

   x_1 = \cos\frac{\varphi}{3} + i\sin\frac{\varphi}{3}, \qquad
   x_2 = \cos\frac{\varphi + 2\pi}{3} + i\sin\frac{\varphi + 2\pi}{3}, \qquad
   x_3 = \cos\frac{\varphi + 4\pi}{3} + i\sin\frac{\varphi + 4\pi}{3}.

Geometrically, these three roots are represented in the complex plane by the vertices of an equilateral triangle inscribed in the unit circle centered at the origin, the root :math:`x_1` having the argument :math:`\frac{\varphi}{3}`. Hence the equation :math:`x^3 = \cos\varphi + i\sin\varphi` is the exact analytic expression of the **problem of trisecting the angle** :math:`\varphi`.

Suppose now that this equation were reducible over the domain of rationality formed by all rational functions of :math:`\cos\varphi` and :math:`\sin\varphi`. Then at least one of its three roots could be represented as a single-valued rational function :math:`R(\cos\varphi, \sin\varphi)`, whose value would necessarily remain **unchanged** upon substituting :math:`\varphi + 2\pi` for :math:`\varphi`. Yet if we carry out this change by a **continuous variation of the angle** :math:`\varphi` **from** :math:`\varphi` **to** :math:`\varphi + 2\pi`, the formulas above show immediately that the three roots undergo the cyclic permutation

.. math::

   x_1 \longrightarrow x_2 \longrightarrow x_3 \longrightarrow x_1.

Consequently, **no root remains unaltered**, and no root can be represented as a rational function of :math:`\cos\varphi` and :math:`\sin\varphi`! The equation :math:`x^3 = \cos\varphi + i\sin\varphi` is therefore irreducible of degree :math:`3 \neq 2^h` and cannot be solved by a finite number of square roots:

.. admonition:: Theorem (Impossibility of General Angle Trisection)

   **The trisection of an arbitrary angle** :math:`\varphi` **cannot be effected with straightedge and compasses**.

Evidently this demonstration and the general theorem apply when :math:`\varphi` is an *arbitrary* angle; for certain **special** values of :math:`\varphi` the cubic equation becomes reducible and the construction is perfectly possible—for example, when :math:`\varphi = \frac{\pi}{2}` (since :math:`\frac{\pi}{6} = 30^\circ` is constructible), whereas for :math:`\varphi = \frac{\pi}{3}` (:math:`60^\circ`) the resulting numerical cubic remains irreducible over :math:`\mathbb{Q}`.
