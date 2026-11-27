:title: Part II, Ch. III: The Transcendence of the Number e (1897 English)
:layout: book
:canonical_id: Ch. III
:order: 3

.. _fp-part_2-ch_03-en:
.. _fp-part2-ch_03-en:
.. _fp-ch_03-en:
.. _fp-part2-ch3-hermite-e-en:

Part II, Chapter III — The Transcendence of the Number e
========================================================

.. rubric:: Part II, Chapter III (§§ 1–3; :cite:`Ginn & Co., 1897, pp. 61–67 <klein:1897>`)

§ 1. Exponential Convergence and Strategy of the Indirect Proof
---------------------------------------------------------------

**1.** Our starting-point is the exponential power series

.. math::

   e^x = 1 + \frac{x}{1} + \frac{x^2}{2!} + \dots + \frac{x^n}{n!} + \dots,

which converges for every finite value of :math:`x`. One must distinguish sharply here between *practical* and *theoretical* convergence: for :math:`x = 1000`, computing :math:`e^{1000}` directly from this series would be practically unfeasible, yet theoretically the series certainly converges because beyond the :math:`1000`-th term the factorial :math:`n!` in the denominator grows far more rapidly than :math:`x^n` in the numerator. Precisely this asymptotic fact—that for every fixed :math:`x`,

.. math::

   \lim_{n \to \infty} \frac{x^n}{n!} = 0

—drives our entire transcendence proof.

**Proposition (:person:`Hermite's <hermite>` Theorem, :cite:`1873 <hermite:1873>`):** *The number* :math:`e` *is not algebraic; no equation with coprime integer coefficients* (:math:`C_0 \neq 0`) *of the form*

.. math::

   F(e) = C_0 + C_1 e + C_2 e^2 + \dots + C_n e^n = 0

*can subsist.*

We proceed indirectly: assuming :math:`F(e) = 0`, we multiply through by a suitably chosen integer :math:`M` so that

.. math::

   M F(e) = \bigl(M C_0 + M_1 C_1 + M_2 C_2 + \dots + M_n C_n\bigr) + \bigl(C_1 \varepsilon_1 + C_2 \varepsilon_2 + \dots + C_n \varepsilon_n\bigr) = 0,

where:

1. Each product :math:`M e^k = M_k + \varepsilon_k` splits into an **integer part** :math:`M_k` and a **remainder** :math:`\varepsilon_k`;
2. The integer sum :math:`M C_0 + M_1 C_1 + \dots + M_n C_n` leaves a **non-zero remainder modulo a prime** :math:`p`, and hence cannot vanish;
3. The remainder sum :math:`C_1 \varepsilon_1 + \dots + C_n \varepsilon_n` can be made **as small a proper fraction as we please** (:math:`|\sum C_k \varepsilon_k| < 1`).

Since a non-zero integer plus a proper fraction can never equal zero, :math:`F(e) = 0` is impossible! Intuitively, :math:`1, e, e^2, \dots, e^n` can be approximated to extraordinary accuracy by integers :math:`M, M_1, \dots, M_n` that demonstrably fail to satisfy :math:`F = 0`.

§ 2. Gordan's Umbral Symbol :math:`h^r = r!` and the Auxiliary Polynomial :math:`\varphi(x)`
--------------------------------------------------------------------------------------------

**2.** Following :person:`Paul Gordan <gordan>` (:cite:`1893 <gordan:1893>`), let the umbral symbol :math:`h^r` stand simply as compact shorthand for the factorial :math:`r!`: for any expanded polynomial :math:`f(x) = \sum_r c_r x^r`, we write

.. math::

   f(h) = \sum_r c_r h^r = \sum_r c_r\, r!,

while for an *undeveloped* polynomial such as :math:`f(k + h) = \sum_r c_r(k + h)^r`, we **first expand in powers of** :math:`h` to obtain :math:`\sum_r c'_r h^r` and **only then replace** :math:`h^r` **by** :math:`r!`.

Now introduce the remarkable auxiliary polynomial

.. math::

   \varphi(x) = \frac{x^{p-1}\bigl[(1 - x)(2 - x)\cdots(n - x)\bigr]^p}{(p - 1)!},

where :math:`n` is the degree of :math:`F(e) = 0` and :math:`p` is a **prime number chosen greater than both** :math:`n` **and** :math:`|C_0|`, eventually allowed to increase without limit. Geometrically, the curve :math:`y = \varphi(x)` touches the :math:`X`-axis without inflection at :math:`x = 0` (even multiplicity :math:`p - 1`) and crosses it with inflectional tangency at :math:`x = 1, 2, \dots, n` (odd multiplicity :math:`p`), hugging the :math:`X`-axis tightly throughout :math:`[0, n]`.

We establish **three fundamental properties** of :math:`\varphi`:

1. **Asymptotic smallness as** :math:`p \to \infty`: Setting :math:`u = x(1 - x)(2 - x)\cdots(n - x)`, we have :math:`\varphi(x) = \frac{u^p}{x\cdot (p - 1)!}`, which tends to :math:`0` as :math:`p \to \infty` for every fixed :math:`x`. Moreover, replacing :math:`-x` by :math:`+|x|` in the factored numerator majors the sum of absolute values :math:`\sum_{r=p-1}^{np+p-1} |c_r|\,|x|^r`, which therefore **also tends to** :math:`0` **as** :math:`p \to \infty`.
2. :math:`\varphi(h)` **is an integer not divisible by** :math:`p`: Expanding :math:`\varphi(x)` in powers of :math:`x` from lowest degree :math:`p - 1` to highest degree :math:`np + p - 1`,

   .. math::

      \varphi(x) = \sum_{r=p-1}^{np+p-1} c_r x^r = \frac{c'_{p-1} x^{p-1}}{(p - 1)!} + \frac{c'_p x^p}{(p - 1)!} + \dots \pm \frac{x^{np+p-1}}{(p - 1)!},

   where all numerators :math:`c'_r` are integers. Upon replacing :math:`x^r` by :math:`h^r = r!`, the denominator :math:`(p - 1)!` cancels in every term since :math:`r \ge p - 1`. Every term from :math:`r = p` onward retains the factor :math:`\frac{r!}{(p-1)!}` divisible by :math:`p`, whereas the **first term** (:math:`r = p - 1`) equals

   .. math::

      \frac{(1\cdot 2\cdot 3 \cdots n)^p\,(p - 1)!}{(p - 1)!} = (n!)^p \not\equiv 0 \pmod p \qquad (\text{since } p > n).

   Hence :math:`\varphi(h) \equiv (n!)^p \not\equiv 0 \pmod p`, and in particular :math:`\varphi(h) \neq 0`.
3. **For each** :math:`k \in \{1, 2, \dots, n\}`, :math:`\varphi(h + k)` **is an integer divisible by** :math:`p`: Substituting :math:`x = k + h` into :math:`\varphi(x)`, the :math:`k`-th factor :math:`(k - k - h)` reduces to :math:`-h`, raising the **lowest power of** :math:`h` **to** :math:`h^p`:

   .. math::

      \varphi(h + k) = \frac{(k + h)^{p-1}\bigl[(1 - k - h)\cdots(-h)\cdots(n - k - h)\bigr]^p}{(p - 1)!} = \sum_{r=p}^{np+p-1} c'_r h^r.

   When we replace :math:`h^r` by :math:`r!` (:math:`r \ge p`), the denominator :math:`(p - 1)!` cancels and **every single term**—starting with the :math:`r = p` term :math:`(-1)^{kp} k^{p-1}[(k-1)!(n-k)!]^p \cdot p`—is an integer divisible by :math:`p`!

§ 3. Completion of the Proof of Hermite's Theorem
-------------------------------------------------

**3.** Choose the multiplier :math:`M = \varphi(h)`:

.. math::

   \varphi(h) F(e) = C_0 \varphi(h) + C_1 \varphi(h) e + C_2 \varphi(h) e^2 + \dots + C_n \varphi(h) e^n = 0.

To decompose :math:`e^k \varphi(h) = \sum_r c_r (e^k h^r)`, expand :math:`e^k` for any single power :math:`h^r = r!`:

.. math::

   \begin{aligned}
   e^k \cdot h^r &= r!\left(1 + \frac{k}{1!} + \frac{k^2}{2!} + \dots + \frac{k^r}{r!} + \frac{k^{r+1}}{(r+1)!} + \dots\right) \\
   &= \left[h^r + \binom{r}{1} h^{r-1} k + \binom{r}{2} h^{r-2} k^2 + \dots + k^r\right] + k^r\left[\frac{k}{r + 1} + \frac{k^2}{(r + 1)(r + 2)} + \dots\right].
   \end{aligned}

The first bracket has the exact umbral form :math:`(h + k)^r`. In the second bracket (:math:`k > 0`), term-by-term comparison with :math:`e^k = 1 + \frac{k}{1!} + \frac{k^2}{2!} + \dots` shows that the bracketed tail equals :math:`q_{r,k}\, e^k` for a positive proper fraction :math:`0 < q_{r,k} < 1`:

.. math::

   e^k \cdot h^r = (h + k)^r + q_{r,k}\, k^r e^k \qquad (0 < q_{r,k} < 1).

Summing across :math:`r = p - 1, \dots, np + p - 1` yields

.. math::

   e^k \varphi(h) = \varphi(h + k) + \varepsilon_k, \qquad \text{where} \qquad \varepsilon_k = e^k \sum_r q_{r,k} c_r k^r.

By Property (1), :math:`|\varepsilon_k| \le e^k \sum_r |c_r|\,k^r \to 0` as :math:`p \to \infty`. Substituting into :math:`\varphi(h)F(e) = 0` gives

.. math::

   \bigl[C_0 \varphi(h) + C_1 \varphi(h + 1) + \dots + C_n \varphi(h + n)\bigr] + \bigl[C_1 \varepsilon_1 + \dots + C_n \varepsilon_n\bigr] = 0.

By Properties (2) and (3) and :math:`p > |C_0| > 0`, the first bracket is an integer congruent to :math:`C_0 (n!)^p \not\equiv 0 \pmod p`, hence **at least** :math:`1` **in absolute value**; by Property (1), choosing the prime :math:`p` sufficiently large makes :math:`|C_1 \varepsilon_1 + \dots + C_n \varepsilon_n| < 1`. This contradiction proves **Hermite's Theorem**: :math:`e` **is transcendental**.
