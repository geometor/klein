:title: Part I, Ch. III: Cyclotomy & Fermat Primes — Analytical Summary
:layout: book

.. _fp-part1-ch3-cyclotomy-summary:

Part I, Chapter III — Analytical Summary
========================================

.. rubric:: Gauss–Wantzel Necessity Proof via Gauss's Lemma and Eisenstein's Criterion (§§ 1–8)

Architecture of the Proof
-------------------------

1. **Historical Trajectory (§ 1):**
   From :person:`Euclid's <euclid>` ancient polygons ($n = 2^a, 3, 5, 15$) to :person:`Gauss's <gauss>` 1796/1801 discovery of :term:`Fermat-prime <fermat-prime>` cyclotomy ($p = 3, 5, 17, 257, 65537$), :person:`Richelot's <richelot>` 1832 resolution of the $257$-gon, and :person:`Hermes's <hermes>` 1894 Göttingen trunk for the $65537$-gon.
2. **Bézout Partial-Fraction Decomposition (§ 2):**
   For coprime factors $n = \mu\nu$, $a\mu + b\nu = 1 \implies \frac{1}{\mu\nu} = \frac{a}{\nu} + \frac{b}{\mu}$ reduces $n$-division to prime-power $p^\alpha$-divisions.
3. **Characterization of Fermat Primes (§§ 3–4):**
   Two independent proofs (multiplicative order $2^s \equiv 1 \pmod p$ with $s = 2h \mid 2^h$, and algebraic divisibility $2^{h'} + 1 \mid 2^{h'(2n+1)} + 1$) show that $p = 2^h + 1$ can be prime only when $h = 2^\mu$.
4. **Gauss's Content Lemma (§ 6):**
   Monic rational factorizations of monic integer polynomials are necessarily integral—proved by inspecting the lowest-index coefficients $a_i, b_k$ not divisible by a prime $q \mid a_0 b_0$.
5. **Eisenstein Irreducibility for $\Phi_p(z)$ and $\Phi_{p^2}(z)$ (§§ 5, 7–8):**
   Shifting $z = x + 1$ puts both $\Phi_p(x + 1) = \frac{(x+1)^p - 1}{x}$ (degree $p - 1$) and $\Phi_{p^2}(x + 1) = \frac{(x+1)^{p^2} - 1}{(x+1)^p - 1} = x^{p(p-1)} + p\,\chi(x)$ (degree $p(p-1)$) into Eisenstein $p$-form. Hence:

   * Odd prime $p$ is constructible only if $p - 1 = 2^h$, i.e. $p = 2^{2^\mu} + 1$.
   * Every odd prime square $p^2$ ($p > 2$, such as $n = 9$ or $n = 25$) has irreducible degree $p(p - 1)$ divisible by $p$, so **repeated odd prime factors are never constructible**.
