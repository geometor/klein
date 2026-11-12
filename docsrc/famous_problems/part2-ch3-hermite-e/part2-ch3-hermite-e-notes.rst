:title: Part II, Ch. III: Transcendence of e — Critical & Symbolic Notes
:layout: book

.. _fp-part2-ch3-hermite-e-notes:

Part II, Chapter III — Critical & Symbolic Notes
================================================

.. rubric:: Equivalence of Hilbert's Gamma Integral and Gordan's Umbral Calculus, and Exact Verification

Mathematical & Symbolic Commentary
----------------------------------

* **Why Gordan's Symbol $h^r = r!$ Replaces Hilbert's Integral:** In :person:`Hilbert's <hilbert>` 1893 note (*Göttinger Nachrichten*), the multiplier $M$ was defined as the improper integral $I = \int_0^\infty \varphi(z) e^{-z}\,dz$, and multiplying by $e^k$ split $\int_0^\infty \varphi(z) e^{k-z}\,dz$ at $z = k$ into $\int_k^\infty = \int_0^\infty \varphi(h + k) e^{-h}\,dh$ (an integer divisible by $p$) plus the finite segment $e^k \int_0^k \varphi(z) e^{-z}\,dz$ (which shrinks to $0$ as $p \to \infty$). :person:`Gordan <gordan>` (:cite:`1893 <gordan:1893>`) observed that the linear functional $\mathcal{L}(z^r) = \int_0^\infty z^r e^{-z}\,dz = r!$ acts purely algebraically on polynomials, and that the series identity $e^k \cdot r! = (h + k)^r + k^r \sum_{m=1}^\infty \frac{k^m}{(r+1)\cdots(r+m)}$ reproduces the exact same integer-plus-tail decomposition without a single integral sign!
* **Handling $C_0 = 0$ Without Loss of Generality:** If an assumed integer relation $\sum_{k=m}^n C_k e^k = 0$ has $C_0 = \dots = C_{m-1} = 0$ with $C_m \neq 0$, dividing through by the non-zero real number $e^m$ immediately restores a relation of lower degree $n - m$ with non-zero constant term $C'_0 = C_m \neq 0$.
* **Symbolic Transcendence Diagnostics in ``geometor.klein.constructibility``:** Passing ``sp.E`` (or rational/polynomial combinations such as ``2*sp.E + 1``) to :func:`geometor.klein.constructibility.analyze_constructibility` classifies it directly under ``kind="transcendental"`` with locus ``Famous Problems, Part II, Ch. III (§§ 1–3)`` and obstruction citing :person:`Hermite's <hermite>` Theorem (1873).
