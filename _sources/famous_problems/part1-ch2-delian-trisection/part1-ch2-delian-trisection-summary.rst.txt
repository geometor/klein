:title: Part I, Ch. II: Delian Problem & Angle Trisection — Analytical Summary
:layout: book

.. _fp-part1-ch2-delian-trisection-summary:

Part I, Chapter II — Analytical Summary
=======================================

.. rubric:: Impossibility of Cube Duplication and General Angle Trisection (§§ 1–3)

Synopsis of Arguments
---------------------

1. **Numerical Impossibility of the Delian Cube (§ 1):**
   Doubling the unit cube requires $x^3 - 2 = 0$. Parity descent on $p^3 = 2q^3$ proves no rational root exists; for a cubic polynomial, absence of a linear factor is equivalent to irreducibility over $\mathbb{Q}$. Since $\deg(x^3 - 2) = 3 \neq 2^h$, :term:`the Delian problem <delian-problem>` is impossible with straightedge and compasses.
2. **Function-Field Generalization via Domains of Rationality (§ 2):**
   Adopting Kronecker's :term:`domain of rationality <domain-of-rationality>` $\mathbb{C}(\lambda)$ for a variable parameter $\lambda$, degree comparison on $[f(\lambda)]^3 = \lambda [\psi(\lambda)]^3$ ($3 \deg f = 1 + 3 \deg \psi$) proves $x^3 - \lambda = 0$ is irreducible over rational functions of $\lambda$, ruling out any universal straightedge-and-compass construction of $\sqrt[3]{\lambda}$.
3. **Riemannian Monodromy Proof of Angle Trisection Impossibility (§ 3):**
   Writing $\lambda = \cos\varphi + i\sin\varphi$, trisecting a general angle $\varphi$ is equivalent to solving $x^3 = \cos\varphi + i\sin\varphi$ over the field $\mathbb{Q}(\cos\varphi, \sin\varphi)$. Analytically continuing $\varphi \mapsto \varphi + 2\pi$ leaves every rational function of $(\cos\varphi, \sin\varphi)$ invariant while cyclically permuting the three roots $x_1 \to x_2 \to x_3 \to x_1$. Hence no root lies in $\mathbb{Q}(\cos\varphi, \sin\varphi)$, proving irreducibility of degree $3 \neq 2^h$—while cleanly distinguishing *generic* impossibility from special constructible angles such as $\varphi = \frac{\pi}{2}$.
