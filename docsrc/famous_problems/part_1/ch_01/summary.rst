:type: summary
:title: Part I, Ch. I: Square-Root Equations — Analytical Summary
:layout: book
:canonical_id: Ch. I
:order: 1

.. _fp-part_1-ch_01-summary:
.. _fp-part1-ch_01-summary:
.. _fp-ch_01-summary:
.. _fp-part1-ch1-square-roots-summary:

Part I, Chapter I — Analytical Summary
======================================

.. rubric:: Step-by-Step Logical Architecture of Klein's Degree-:math:`2^h` Theorem (§§ 1–15)

Logical Chain of Proof
----------------------

Without invoking abstract Galois group machinery prematurely, :person:`Klein <klein>` proves :person:`Wantzel's <wantzel>` (:cite:`1837 <wantzel:1837>`) theorem entirely by elementary polynomial algebra over a :term:`domain of rationality <domain-of-rationality>` :math:`K_0`:

1. **Radical Order & Algebraic Independence (§§ 1–4):**
   Every constructible quantity :math:`x` has a finite :term:`radical order <radical-order>` :math:`\mu` and depends on :math:`m` square roots :math:`Q_1, \dots, Q_m`, pruned from the bottom up so that no :math:`Q_k` is a rational function of the remaining :math:`m - 1` radicals over :math:`K_0`.
2. **Rationalized Normal Form (§§ 5–6):**
   Successive conjugation :math:`(c - d Q_k)` eliminates every :math:`Q_k` from denominators (:math:`c + d Q_k \neq 0` by independence), expressing :math:`x = \alpha + \beta Q_\mu` and ultimately expanding :math:`x` as a :math:`K_0`-linear combination of multilinear products :math:`Q_{i_1}\cdots Q_{i_r}`.
3. **The** :math:`2^m` **Conjugate Branches &** :math:`F(x) = 0` (**§§ 7–9**):
   Flipping :math:`\pm Q_k` across all :math:`m` independent square roots yields :math:`2^m` formal :term:`conjugate values <conjugate-values>` :math:`x_1, \dots, x_{2^m}`. Because flipping each highest-order radical permutes the linear factors :math:`(x - x_i)`, the symmetric product :math:`F(x) = \prod_{i=1}^{2^m} (x - x_i)` has coefficients in :math:`K_0` and degree :math:`2^m`.
4. **Conjugate Propagation Under Any Rational Polynomial (§ 10):**
   If :math:`f(x) \in K_0[x]` satisfies :math:`f(x_1) = 0`, writing :math:`f(\alpha + \beta Q_\mu) = A + B Q_\mu = 0` forces :math:`B = 0` (otherwise :math:`Q_\mu = -A/B` violates § 4) and hence :math:`A = 0`, so :math:`f(\alpha - \beta Q_\mu) = A - B Q_\mu = 0`. Descending through all :math:`m` radicals proves :math:`f(x_i) = 0` for all :math:`i = 1, \dots, 2^m`.
5. **Irreducible Minimal Polynomial & Power Factorization (§§ 11–14):**
   The monic minimal polynomial :math:`\varphi(x) \in K_0[x]` of :math:`x_1` divides every polynomial vanishing at :math:`x_1`. Repeatedly dividing :math:`F(x)` by :math:`\varphi(x)` yields :math:`F(x) = [\varphi(x)]^\nu`, whence :math:`2^m = \deg(\varphi)\cdot\nu` and :math:`\deg(\varphi) = 2^h`.
6. **Contrapositive Obstruction & Galois Sufficiency Caveat (§ 15):**
   Any problem whose irreducible polynomial has degree :math:`M \neq 2^h` is **impossible** with straightedge and compasses. Conversely, :math:`M = 2^h` is necessary *but not sufficient* in general (e.g., an :math:`S_4` or :math:`A_4` quartic of degree :math:`4 = 2^2` fails because its cubic resolvent is irreducible).
