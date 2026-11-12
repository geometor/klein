:title: Part II, Ch. III: The Transcendence of the Number e (1897 English)
:layout: book

.. _fp-part2-ch3-hermite-e-en:

Part II, Chapter III — The Transcendence of the Number e
========================================================

.. rubric:: Part II, Chapter III (§§ 1–3; :cite:`Ginn & Co., 1897, pp. 61–67 <klein:1897>`)

§ 1. Exponential Convergence and Strategy of the Indirect Proof
---------------------------------------------------------------

**1.** Our starting-point is the exponential power series

.. math::

   e^x = 1 + \frac{x}{1} + \frac{x^2}{2!} + \dots + \frac{x^n}{n!} + \dots,

which converges for every finite value of $x$. One must distinguish sharply here between *practical* and *theoretical* convergence: for $x = 1000$, computing $e^{1000}$ directly from this series would be practically unfeasible, yet theoretically the series certainly converges because beyond the $1000$-th term the factorial $n!$ in the denominator grows far more rapidly than $x^n$ in the numerator. Precisely this asymptotic fact—that for every fixed $x$,

.. math::

   \lim_{n \to \infty} \frac{x^n}{n!} = 0

—drives our entire transcendence proof.

**Proposition (:person:`Hermite's <hermite>` Theorem, :cite:`1873 <hermite:1873>`):** *The number $e$ is not algebraic; no equation with coprime integer coefficients ($C_0 \neq 0$) of the form*

.. math::

   F(e) = C_0 + C_1 e + C_2 e^2 + \dots + C_n e^n = 0

*can subsist.*

We proceed indirectly: assuming $F(e) = 0$, we multiply through by a suitably chosen integer $M$ so that

.. math::

   M F(e) = \bigl(M C_0 + M_1 C_1 + M_2 C_2 + \dots + M_n C_n\bigr) + \bigl(C_1 \varepsilon_1 + C_2 \varepsilon_2 + \dots + C_n \varepsilon_n\bigr) = 0,

where:

1. Each product $M e^k = M_k + \varepsilon_k$ splits into an **integer part** $M_k$ and a **remainder** $\varepsilon_k$;
2. The integer sum $M C_0 + M_1 C_1 + \dots + M_n C_n$ leaves a **non-zero remainder modulo a prime $p$**, and hence cannot vanish;
3. The remainder sum $C_1 \varepsilon_1 + \dots + C_n \varepsilon_n$ can be made **as small a proper fraction as we please** ($|\sum C_k \varepsilon_k| < 1$).

Since a non-zero integer plus a proper fraction can never equal zero, $F(e) = 0$ is impossible! Intuitively, $1, e, e^2, \dots, e^n$ can be approximated to extraordinary accuracy by integers $M, M_1, \dots, M_n$ that demonstrably fail to satisfy $F = 0$.

§ 2. Gordan's Umbral Symbol $h^r = r!$ and the Auxiliary Polynomial $\varphi(x)$
--------------------------------------------------------------------------------

**2.** Following :person:`Paul Gordan <gordan>` (:cite:`1893 <gordan:1893>`), let the umbral symbol $h^r$ stand simply as compact shorthand for the factorial $r!$: for any expanded polynomial $f(x) = \sum_r c_r x^r$, we write

.. math::

   f(h) = \sum_r c_r h^r = \sum_r c_r\, r!,

while for an *undeveloped* polynomial such as $f(k + h) = \sum_r c_r(k + h)^r$, we **first expand in powers of $h$** to obtain $\sum_r c'_r h^r$ and **only then replace $h^r$ by $r!$**.

Now introduce the remarkable auxiliary polynomial

.. math::

   \varphi(x) = \frac{x^{p-1}\bigl[(1 - x)(2 - x)\cdots(n - x)\bigr]^p}{(p - 1)!},

where $n$ is the degree of $F(e) = 0$ and $p$ is a **prime number chosen greater than both $n$ and $|C_0|$**, eventually allowed to increase without limit. Geometrically, the curve $y = \varphi(x)$ touches the $X$-axis without inflection at $x = 0$ (even multiplicity $p - 1$) and crosses it with inflectional tangency at $x = 1, 2, \dots, n$ (odd multiplicity $p$), hugging the $X$-axis tightly throughout $[0, n]$.

We establish **three fundamental properties** of $\varphi$:

1. **Asymptotic smallness as $p \to \infty$:** Setting $u = x(1 - x)(2 - x)\cdots(n - x)$, we have $\varphi(x) = \frac{u^p}{x\cdot (p - 1)!}$, which tends to $0$ as $p \to \infty$ for every fixed $x$. Moreover, replacing $-x$ by $+|x|$ in the factored numerator majors the sum of absolute values $\sum_{r=p-1}^{np+p-1} |c_r|\,|x|^r$, which therefore **also tends to $0$ as $p \to \infty$**.
2. **$\varphi(h)$ is an integer not divisible by $p$:** Expanding $\varphi(x)$ in powers of $x$ from lowest degree $p - 1$ to highest degree $np + p - 1$,

   .. math::

      \varphi(x) = \sum_{r=p-1}^{np+p-1} c_r x^r = \frac{c'_{p-1} x^{p-1}}{(p - 1)!} + \frac{c'_p x^p}{(p - 1)!} + \dots \pm \frac{x^{np+p-1}}{(p - 1)!},

   where all numerators $c'_r$ are integers. Upon replacing $x^r$ by $h^r = r!$, the denominator $(p - 1)!$ cancels in every term since $r \ge p - 1$. Every term from $r = p$ onward retains the factor $\frac{r!}{(p-1)!}$ divisible by $p$, whereas the **first term** ($r = p - 1$) equals

   .. math::

      \frac{(1\cdot 2\cdot 3 \cdots n)^p\,(p - 1)!}{(p - 1)!} = (n!)^p \not\equiv 0 \pmod p \qquad (\text{since } p > n).

   Hence $\varphi(h) \equiv (n!)^p \not\equiv 0 \pmod p$, and in particular $\varphi(h) \neq 0$.
3. **For each $k \in \{1, 2, \dots, n\}$, $\varphi(h + k)$ is an integer divisible by $p$:** Substituting $x = k + h$ into $\varphi(x)$, the $k$-th factor $(k - k - h)$ reduces to $-h$, raising the **lowest power of $h$ to $h^p$**:

   .. math::

      \varphi(h + k) = \frac{(k + h)^{p-1}\bigl[(1 - k - h)\cdots(-h)\cdots(n - k - h)\bigr]^p}{(p - 1)!} = \sum_{r=p}^{np+p-1} c'_r h^r.

   When we replace $h^r$ by $r!$ ($r \ge p$), the denominator $(p - 1)!$ cancels and **every single term**—starting with the $r = p$ term $(-1)^{kp} k^{p-1}[(k-1)!(n-k)!]^p \cdot p$—is an integer divisible by $p$!

§ 3. Completion of the Proof of Hermite's Theorem
-------------------------------------------------

**3.** Choose the multiplier $M = \varphi(h)$:

.. math::

   \varphi(h) F(e) = C_0 \varphi(h) + C_1 \varphi(h) e + C_2 \varphi(h) e^2 + \dots + C_n \varphi(h) e^n = 0.

To decompose $e^k \varphi(h) = \sum_r c_r (e^k h^r)$, expand $e^k$ for any single power $h^r = r!$:

.. math::

   \begin{aligned}
   e^k \cdot h^r &= r!\left(1 + \frac{k}{1!} + \frac{k^2}{2!} + \dots + \frac{k^r}{r!} + \frac{k^{r+1}}{(r+1)!} + \dots\right) \\
   &= \left[h^r + \binom{r}{1} h^{r-1} k + \binom{r}{2} h^{r-2} k^2 + \dots + k^r\right] + k^r\left[\frac{k}{r + 1} + \frac{k^2}{(r + 1)(r + 2)} + \dots\right].
   \end{aligned}

The first bracket has the exact umbral form $(h + k)^r$. In the second bracket ($k > 0$), term-by-term comparison with $e^k = 1 + \frac{k}{1!} + \frac{k^2}{2!} + \dots$ shows that the bracketed tail equals $q_{r,k}\, e^k$ for a positive proper fraction $0 < q_{r,k} < 1$:

.. math::

   e^k \cdot h^r = (h + k)^r + q_{r,k}\, k^r e^k \qquad (0 < q_{r,k} < 1).

Summing across $r = p - 1, \dots, np + p - 1$ yields

.. math::

   e^k \varphi(h) = \varphi(h + k) + \varepsilon_k, \qquad \text{where} \qquad \varepsilon_k = e^k \sum_r q_{r,k} c_r k^r.

By Property (1), $|\varepsilon_k| \le e^k \sum_r |c_r|\,k^r \to 0$ as $p \to \infty$. Substituting into $\varphi(h)F(e) = 0$ gives

.. math::

   \bigl[C_0 \varphi(h) + C_1 \varphi(h + 1) + \dots + C_n \varphi(h + n)\bigr] + \bigl[C_1 \varepsilon_1 + \dots + C_n \varepsilon_n\bigr] = 0.

By Properties (2) and (3) and $p > |C_0| > 0$, the first bracket is an integer congruent to $C_0 (n!)^p \not\equiv 0 \pmod p$, hence **at least $1$ in absolute value**; by Property (1), choosing the prime $p$ sufficiently large makes $|C_1 \varepsilon_1 + \dots + C_n \varepsilon_n| < 1$. This contradiction proves **Hermite's Theorem: $e$ is transcendental**.
