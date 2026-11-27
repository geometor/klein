:title: Part II, Ch. III: Transcendence of e — Critical & Symbolic Notes
:layout: book
:canonical_id: Ch. III
:order: 3
:tracks: English: ch_03-en | German: ch_03-de | Summary: ch_03-summary | Notes: ch_03-notes

.. _fp-part_2-ch_03-notes:
.. _fp-part2-ch_03-notes:
.. _fp-ch_03-notes:
.. _fp-part2-ch3-hermite-e-notes:

Part II, Chapter III — Critical & Symbolic Notes
================================================

.. rubric:: Equivalence of Hilbert's Gamma Integral and Gordan's Umbral Calculus, and Exact Verification

Mathematical & Symbolic Commentary
----------------------------------

* **Why Gordan's Symbol** :math:`h^r = r!` **Replaces Hilbert's Integral**: In :person:`Hilbert's <hilbert>` 1893 note (*Göttinger Nachrichten*), the multiplier :math:`M` was defined as the improper integral :math:`I = \int_0^\infty \varphi(z) e^{-z}\,dz`, and multiplying by :math:`e^k` split :math:`\int_0^\infty \varphi(z) e^{k-z}\,dz` at :math:`z = k` into :math:`\int_k^\infty = \int_0^\infty \varphi(h + k) e^{-h}\,dh` (an integer divisible by :math:`p`) plus the finite segment :math:`e^k \int_0^k \varphi(z) e^{-z}\,dz` (which shrinks to :math:`0` as :math:`p \to \infty`). :person:`Gordan <gordan>` (:cite:`1893 <gordan:1893>`) observed that the linear functional :math:`\mathcal{L}(z^r) = \int_0^\infty z^r e^{-z}\,dz = r!` acts purely algebraically on polynomials, and that the series identity :math:`e^k \cdot r! = (h + k)^r + k^r \sum_{m=1}^\infty \frac{k^m}{(r+1)\cdots(r+m)}` reproduces the exact same integer-plus-tail decomposition without a single integral sign!
* **Handling** :math:`C_0 = 0` **Without Loss of Generality**: If an assumed integer relation :math:`\sum_{k=m}^n C_k e^k = 0` has :math:`C_0 = \dots = C_{m-1} = 0` with :math:`C_m \neq 0`, dividing through by the non-zero real number :math:`e^m` immediately restores a relation of lower degree :math:`n - m` with non-zero constant term :math:`C'_0 = C_m \neq 0`.
* **Symbolic Transcendence Diagnostics in ``geometor.klein.constructibility``:** Passing ``sp.E`` (or rational/polynomial combinations such as ``2*sp.E + 1``) to :func:`geometor.klein.constructibility.analyze_constructibility` classifies it directly under ``kind="transcendental"`` with locus ``Famous Problems, Part II, Ch. III (§§ 1–3)`` and obstruction citing :person:`Hermite's <hermite>` Theorem (1873).
