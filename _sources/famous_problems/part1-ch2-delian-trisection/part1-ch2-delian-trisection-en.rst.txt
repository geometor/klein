:title: Part I, Ch. II: The Delian Problem & Angle Trisection (1897 English)
:layout: book

.. _fp-part1-ch2-delian-trisection-en:

Part I, Chapter II — The Delian Problem and the Trisection of the Angle
=======================================================================

.. rubric:: Part I, Chapter II (§§ 1–3; :cite:`Ginn & Co., 1897, pp. 13–15 <klein:1897>`)

§ 1. The Impossibility of Solving the Delian Problem with Straightedge and Compasses
------------------------------------------------------------------------------------

**1.** Let us apply the general theorem established in Chapter I immediately to the celebrated :term:`Delian problem <delian-problem>`: **the duplication of the cube**. Legend relates that during a plague at Athens, the oracle of Apollo at Delos commanded the citizens to double the volume of his cubical altar while retaining its cubical shape.

Taking the edge of the given cube as the unit of length ($1$), its volume is $1$; the sought edge $x$ of a cube of double volume must therefore satisfy the cubic equation

.. math::

   x^3 = 2, \qquad \text{or} \qquad x^3 - 2 = 0.

According to Chapter I, § 15, this equation cannot be solved by square roots—and therefore cannot be constructed with straightedge and compasses—provided $x^3 - 2 = 0$ is **irreducible** over the rational numbers. Now if a cubic polynomial with rational coefficients were reducible, at least one of its factors would have to be of the first degree, so the equation $x^3 = 2$ would possess a rational root $x = \frac{p}{q}$, where $p$ and $q$ are integers relatively prime to each other ($\gcd(p, q) = 1$). Substituting $x = \frac{p}{q}$ yields

.. math::

   p^3 = 2 q^3.

Hence $p^3$, and therefore $p$ itself, must be an even integer: $p = 2 p'$. Substituting this back gives $8 p'^3 = 2 q^3$, or

.. math::

   4 p'^3 = q^3,

which forces $q^3$, and hence $q$, likewise to be even—contradicting our assumption that $p$ and $q$ have no common factor! Consequently, $x^3 - 2 = 0$ has no rational root; it is irreducible of degree $3$, and since $3$ is not a power of $2$, **the Delian problem cannot be solved with straightedge and compasses**.

§ 2. The General Equation $x^3 = \lambda$
-----------------------------------------

**2.** Before passing to the trisection of the angle, let us consider more generally the equation

.. math::

   x^3 = \lambda,

where $\lambda$ is no longer a fixed integer like $2$, but an **arbitrary variable parameter** (capable of assuming real or complex values). What do we mean here by "rational operations" and "irreducibility"? Following Kronecker, we take as our :term:`domain of rationality <domain-of-rationality>` (*Rationalitätsbereich*) the totality of all rational functions of the parameter $\lambda$—that is, quotients $\frac{f(\lambda)}{\psi(\lambda)}$ in which $f(\lambda)$ and $\psi(\lambda)$ are polynomials in $\lambda$. All the theorems of Chapter I remain valid verbatim over this domain of rationality: an expression in $\lambda$ constructible universally with straightedge and compasses must satisfy an equation irreducible over the rational functions of $\lambda$ whose degree is a power of $2$.

Now if $x^3 - \lambda = 0$ were reducible over this domain of rationality, at least one factor would be linear in $x$, so some rational function $x = \frac{f(\lambda)}{\psi(\lambda)}$ (reduced to lowest terms, so that the polynomials $f(\lambda)$ and $\psi(\lambda)$ share no common factor) would satisfy

.. math::

   [f(\lambda)]^3 = \lambda \, [\psi(\lambda)]^3.

Comparing polynomial degrees on both sides gives $3 \deg f = 1 + 3 \deg \psi$, which is impossible for integers (or equivalently, $\lambda$ divides $[f(\lambda)]^3$, hence divides $f(\lambda)$, whence $\lambda^3$ divides $\lambda [\psi(\lambda)]^3$, forcing $\lambda$ to divide $\psi(\lambda)$ as well). Under our hypothesis of variable $\lambda$, the equation $x^3 - \lambda = 0$ is therefore **irreducible**, and since its degree $3$ is not of the form $2^h$, **it cannot be solved by square roots**.

§ 3. The Impossibility of Trisecting an Angle with Straightedge and Compasses
-----------------------------------------------------------------------------

**3.** Let us now separate the complex variability of $\lambda$ into modulus and argument by setting

.. math::

   \lambda = r(\cos\varphi + i\sin\varphi), \qquad \text{whence} \qquad \sqrt[3]{\lambda} = \sqrt[3]{r}\,\sqrt[3]{\cos\varphi + i\sin\varphi}.

Our problem resolves itself into two distinct geometric problems—extracting the cube root of an arbitrary positive real number $r$, and extracting the cube root of an arbitrary unit complex number $\cos\varphi + i\sin\varphi$—which we treat separately.

**I. General Multiplication of the Cube ($x^3 = r$).**
The three roots of $x^3 = r$ are

.. math::

   \sqrt[3]{r}, \qquad \varepsilon\sqrt[3]{r}, \qquad \varepsilon^2\sqrt[3]{r},

where $\varepsilon$ and $\varepsilon^2$ denote the primitive complex cube roots of unity:

.. math::

   \varepsilon = \frac{-1 + i\sqrt{3}}{2}, \qquad \varepsilon^2 = \frac{-1 - i\sqrt{3}}{2}.

Taking for our :term:`domain of rationality <domain-of-rationality>` the totality of rational functions of $r$, we know by § 2 that $x^3 = r$ is irreducible of degree $3$. Hence *the problem of multiplying the cube by an arbitrary ratio $r$ does not admit, in general, of a construction by means of straightedge and compasses*.

**II. Trisection of the Angle ($x^3 = \cos\varphi + i\sin\varphi$).**
By De Moivre's formula, the three roots of the equation $x^3 = \cos\varphi + i\sin\varphi$ are

.. math::

   x_1 = \cos\frac{\varphi}{3} + i\sin\frac{\varphi}{3}, \qquad
   x_2 = \cos\frac{\varphi + 2\pi}{3} + i\sin\frac{\varphi + 2\pi}{3}, \qquad
   x_3 = \cos\frac{\varphi + 4\pi}{3} + i\sin\frac{\varphi + 4\pi}{3}.

Geometrically, these three roots are represented in the complex plane by the vertices of an equilateral triangle inscribed in the unit circle centered at the origin, the root $x_1$ having the argument $\frac{\varphi}{3}$. Hence the equation $x^3 = \cos\varphi + i\sin\varphi$ is the exact analytic expression of the **problem of trisecting the angle $\varphi$**.

Suppose now that this equation were reducible over the domain of rationality formed by all rational functions of $\cos\varphi$ and $\sin\varphi$. Then at least one of its three roots could be represented as a single-valued rational function $R(\cos\varphi, \sin\varphi)$, whose value would necessarily remain **unchanged** upon substituting $\varphi + 2\pi$ for $\varphi$. Yet if we carry out this change by a **continuous variation of the angle $\varphi$ from $\varphi$ to $\varphi + 2\pi$**, the formulas above show immediately that the three roots undergo the cyclic permutation

.. math::

   x_1 \longrightarrow x_2 \longrightarrow x_3 \longrightarrow x_1.

Consequently, **no root remains unaltered**, and no root can be represented as a rational function of $\cos\varphi$ and $\sin\varphi$! The equation $x^3 = \cos\varphi + i\sin\varphi$ is therefore irreducible of degree $3 \neq 2^h$ and cannot be solved by a finite number of square roots:

.. admonition:: Theorem (Impossibility of General Angle Trisection)

   **The trisection of an arbitrary angle $\varphi$ cannot be effected with straightedge and compasses.**

Evidently this demonstration and the general theorem apply when $\varphi$ is an *arbitrary* angle; for certain **special** values of $\varphi$ the cubic equation becomes reducible and the construction is perfectly possible—for example, when $\varphi = \frac{\pi}{2}$ (since $\frac{\pi}{6} = 30^\circ$ is constructible), whereas for $\varphi = \frac{\pi}{3}$ ($60^\circ$) the resulting numerical cubic remains irreducible over $\mathbb{Q}$.
