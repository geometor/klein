:title: Part II, Ch. III: Transcendence of e — Analytical Summary
:layout: book
:canonical_id: Ch. III
:order: 3
:tracks: English: ch_03-en | German: ch_03-de | Summary: ch_03-summary | Notes: ch_03-notes

.. _fp-part_2-ch_03-summary:
.. _fp-part2-ch_03-summary:
.. _fp-ch_03-summary:
.. _fp-part2-ch3-hermite-e-summary:

Part II, Chapter III — Analytical Summary
=========================================

.. rubric:: Gordan's Elementary Umbral Proof of Hermite's Theorem (§§ 1–3)

Blueprint of the Modular-Asymptotic Contradiction
-------------------------------------------------

Klein presents :person:`Paul Gordan's <gordan>` 1893 integral-free proof (:cite:`1893 <gordan:1893>`) of :person:`Hermite's <hermite>` Theorem (:cite:`1873 <hermite:1873>`): :math:`e` satisfies no polynomial :math:`F(e) = \sum_{k=0}^n C_k e^k = 0` with :math:`C_k \in \mathbb{Z}`, :math:`C_0 \neq 0`.

1. **Auxiliary Polynomial & Umbral Operator (§ 2):** Define :math:`h^r \mapsto r!` after expanding in powers of :math:`h`, and set

   .. math::

      \varphi(x) = \frac{x^{p-1}\bigl[(1 - x)(2 - x)\cdots(n - x)\bigr]^p}{(p - 1)!} \qquad \bigl(p \text{ prime},\; p > \max(n, |C_0|)\bigr).

2. **Simultaneous Arithmetic & Analytic Control (§ 2):**

   * **Modulo** :math:`p` **non-vanishing at** :math:`0`: Multiplicity :math:`p - 1` at :math:`x = 0` makes :math:`\varphi(h) \equiv (n!)^p \not\equiv 0 \pmod p`.
   * **Modulo** :math:`p` **vanishing at** :math:`1, \dots, n`: Multiplicity :math:`p` at :math:`x = k` shifts the lowest power of :math:`h` in :math:`\varphi(h + k)` to :math:`h^p \mapsto p!`, forcing :math:`\varphi(h + k) \equiv 0 \pmod p`.
   * **Factorial damping as** :math:`p \to \infty`: Because :math:`(p - 1)!` outgrows :math:`u^p`, :math:`\sum_r |c_r|\,|x|^r \to 0` as :math:`p \to \infty`.

3. **Exponential Splitting (§ 3):** Truncating :math:`e^k \cdot r!` at degree :math:`r` yields :math:`e^k h^r = (h + k)^r + q_{r,k} k^r e^k` (:math:`0 < q_{r,k} < 1`), whence

   .. math::

      0 = \varphi(h) F(e) = \underbrace{C_0 \varphi(h) + \sum_{k=1}^n C_k \varphi(h + k)}_{\in\,\mathbb{Z},\;\equiv\, C_0(n!)^p \,\not\equiv\, 0 \pmod p} \;+\; \underbrace{\sum_{k=1}^n C_k \varepsilon_k}_{|\cdot|\,<\,1 \text{ for large } p},

   an impossible equality between a non-zero integer and a proper fraction.
