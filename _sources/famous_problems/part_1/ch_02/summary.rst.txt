:type: summary
:title: Part I, Ch. II: Delian Problem & Angle Trisection — Analytical Summary
:layout: book
:canonical_id: Ch. II
:order: 2

.. _fp-part_1-ch_02-summary:
.. _fp-part1-ch_02-summary:
.. _fp-ch_02-summary:
.. _fp-part1-ch2-delian-trisection-summary:

Part I, Chapter II — Analytical Summary
=======================================

.. rubric:: Impossibility of Cube Duplication and General Angle Trisection (§§ 1–3)

Synopsis of Arguments
---------------------

1. **Numerical Impossibility of the Delian Cube (§ 1):**
   Doubling the unit cube requires :math:`x^3 - 2 = 0`. Parity descent on :math:`p^3 = 2q^3` proves no rational root exists; for a cubic polynomial, absence of a linear factor is equivalent to irreducibility over :math:`\mathbb{Q}`. Since :math:`\deg(x^3 - 2) = 3 \neq 2^h`, :term:`the Delian problem <delian-problem>` is impossible with straightedge and compasses.
2. **Function-Field Generalization via Domains of Rationality (§ 2):**
   Adopting Kronecker's :term:`domain of rationality <domain-of-rationality>` :math:`\mathbb{C}(\lambda)` for a variable parameter :math:`\lambda`, degree comparison on :math:`[f(\lambda)]^3 = \lambda [\psi(\lambda)]^3` (:math:`3 \deg f = 1 + 3 \deg \psi`) proves :math:`x^3 - \lambda = 0` is irreducible over rational functions of :math:`\lambda`, ruling out any universal straightedge-and-compass construction of :math:`\sqrt[3]{\lambda}`.
3. **Riemannian Monodromy Proof of Angle Trisection Impossibility (§ 3):**
   Writing :math:`\lambda = \cos\varphi + i\sin\varphi`, trisecting a general angle :math:`\varphi` is equivalent to solving :math:`x^3 = \cos\varphi + i\sin\varphi` over the field :math:`\mathbb{Q}(\cos\varphi, \sin\varphi)`. Analytically continuing :math:`\varphi \mapsto \varphi + 2\pi` leaves every rational function of :math:`(\cos\varphi, \sin\varphi)` invariant while cyclically permuting the three roots :math:`x_1 \to x_2 \to x_3 \to x_1`. Hence no root lies in :math:`\mathbb{Q}(\cos\varphi, \sin\varphi)`, proving irreducibility of degree :math:`3 \neq 2^h`—while cleanly distinguishing *generic* impossibility from special constructible angles such as :math:`\varphi = \frac{\pi}{2}`.
