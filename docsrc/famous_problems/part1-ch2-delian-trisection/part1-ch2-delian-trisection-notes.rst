:title: Part I, Ch. II: Delian Problem & Angle Trisection — Critical & Symbolic Notes
:layout: book

.. _fp-part1-ch2-delian-trisection-notes:

Part I, Chapter II — Critical & Symbolic Notes
==============================================

.. rubric:: Klein's Monodromy Method vs. Wantzel's Real Cubic $4u^3 - 3u = \cos\varphi$

Function-Theoretic Monodromy vs. Real Trigonometric Cubics
----------------------------------------------------------

Characteristically for the author of *Lectures on the Icosahedron* (1884) and the *Erlangen Program*, :person:`Klein <klein>` proves the impossibility of angle trisection in § 3 via **Riemann-surface monodromy**: as $z = e^{i\varphi}$ winds once around the unit circle, the algebraic function $z^{1/3}$ undergoes a 3-cycle $(x_1\; x_2\; x_3)$, immediately proving irreducibility over $\mathbb{C}(\cos\varphi, \sin\varphi)$ without computing a single trigonometric identity!

To complement Klein's generic function-field proof with :person:`Wantzel's <wantzel>` (:cite:`1837 <wantzel:1837>`) concrete **numerical** counterexample over $\mathbb{Q}$, apply the triple-angle cosine identity $\cos\varphi = 4\cos^3(\varphi/3) - 3\cos(\varphi/3)$ at $\varphi = \frac{\pi}{3} = 60^\circ$ ($\cos 60^\circ = \frac{1}{2}$). Setting $u = 2\cos 20^\circ$ yields

.. math::

   u^3 - 3u - 1 = 0 \qquad \left(\text{equivalently } 8\cos^3 20^\circ - 6\cos 20^\circ - 1 = 0\right).

By the Rational Root Theorem, the only candidate rational roots of $u^3 - 3u - 1 = 0$ are $u = \pm 1$, neither of which vanishes ($(\pm 1)^3 - 3(\pm 1) - 1 \in \{-3, +1\}$). Hence $u^3 - 3u - 1$ is irreducible over $\mathbb{Q}$ of degree $3 \neq 2^h$, proving that **even the specific constructible angle $60^\circ$ cannot be trisected with straightedge and compasses**. Both `x**3 - 2` and `u**3 - 3*u - 1` are verified symbolically in :func:`geometor.klein.constructibility.analyze_constructibility`.

Cross-Corpus Links in GEOMETOR
------------------------------

* **Pappus's Plane, Solid, and Linear Classification (`geometor/pappus`):** In :cite:`*Synagoge* Books III & IV <pappus:collection>`, :person:`Pappus <pappus>` reproved the failure of planar geometers who tried to solve *solid* problems (cube duplication and angle trisection) by *plane* loci (lines and circles) instead of conic sections. Klein's Chapter II supplies the exact algebraic proof that Pappus's ancient intuition lacked (and :ref:`Chapter V <fp-part1-ch5-higher-constructions-en>` exhibits the exact conic and conchoid/cissoid constructions).
* **Euclid's Angle Bisection vs. Trisection (`geometor/euclid`):** Compare quadratic angle bisection (:cite:`*Elements* I.9 <euclid:elements>`, solving $2\cos^2(\varphi/2) - 1 = \cos\varphi$ of degree $2^1$) with cubic trisection of degree $3$.
