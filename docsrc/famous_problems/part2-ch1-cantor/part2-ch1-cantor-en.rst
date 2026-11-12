:title: Part II, Ch. I: Cantor's Demonstration of Transcendental Numbers (1897 English)
:layout: book

.. _fp-part2-ch1-cantor-en:

Part II, Chapter I — Cantor's Demonstration of the Existence of Transcendental Numbers
======================================================================================

.. rubric:: Part II: Transcendental Numbers and the Quadrature of the Circle — Chapter I (§§ 1–3; :cite:`Ginn & Co., 1897, pp. 49–54 <klein:1897>`)

§ 1. Rational, Algebraic, and Transcendental Numbers on the Continuum
---------------------------------------------------------------------

**1.** Represent real numbers as usual by points along the axis of abscissas. If we restrict ourselves to **rational numbers**, the corresponding points fill the axis **densely throughout** (*überall dicht*)—in every interval, however small, infinitely many rational points lie. Nevertheless, as the ancients already discovered, the continuum of points on the line is not exhausted by rationals: between them enter the irrational numbers, and we must ask whether fundamental distinctions exist *within* the irrationals themselves.

We first define **algebraic numbers**: every real root $\omega$ of an algebraic equation with integer coefficients,

.. math::

   a_0 \omega^n + a_1 \omega^{n-1} + \dots + a_{n-1}\omega + a_n = 0,

is called an *algebraic number* (rational numbers arising as the special case $a_0 \omega + a_1 = 0$ of degree $n = 1$). Now we pose the decisive question: *Does the totality of all real algebraic numbers exhaust the real continuum, or does it still form only a discrete, perforated set into whose gaps new numbers may be inserted?* Such non-algebraic real numbers—incapable of satisfying any polynomial equation with integer coefficients—are called :term:`transcendental numbers <transcendental-number>`.

This question was first answered affirmatively by :person:`Joseph Liouville <liouville>` (*Comptes rendus*, 1844; *Journal de Liouville*, Vol. XVI, 1851), who proved the existence of transcendental numbers by means of continued fractions. Liouville's method, however, is rather intricate; the investigation becomes remarkably simple through the set-theoretic principles created by :person:`Georg Cantor <cantor>` in his foundational memoir :cite:`*Über eine Eigenschaft des Inbegriffes aller reellen algebraischen Zahlen* (*Crelle's Journal*, Vol. 77, 1874 [1873]) <cantor:1874>`, combined with the diagonal simplification Cantor presented before the *Naturforscherversammlung* at Halle in 1891.

§ 2. Countability, Power (*Mächtigkeit*), and Algebraic Height
--------------------------------------------------------------

**2.** :person:`Cantor's <cantor>` proof rests on showing that **the real algebraic numbers form a countable (*abzählbare*) aggregate, whereas the continuum does not**. Countability means that all real algebraic numbers can be arranged in a definite numbered sequence $\omega_1, \omega_2, \omega_3, \dots$ in one-to-one correspondence with the positive integers $1, 2, 3, \dots$.

At first sight a paradox seems to arise: the positive integers form only a proper part of the algebraic numbers, yet pairing them one-to-one seems to make the part equal to the whole! That objection rests on a false analogy with finite sets: for infinite aggregates, the Euclidean maxim that *the part is smaller than the whole* loses its meaning—just as the positive integers $1, 2, 3, \dots, n, \dots$ stand in exact one-to-one correspondence with the positive even integers $2, 4, 6, \dots, 2n, \dots$. In place of "larger" and "smaller," Cantor introduces **power** (*Mächtigkeit*): *two infinite aggregates have the same power if they can be placed in one-to-one correspondence*.

To prove that the totality of real algebraic numbers has the same power as $\mathbb{Z}^+$, write every algebraic number as a real root of its unique **irreducible** integer equation

.. math::

   a_0 \omega^n + a_1 \omega^{n-1} + \dots + a_{n-1}\omega + a_n = 0 \qquad \bigl(a_0 > 0,\; \gcd(a_0, a_1, \dots, a_n) = 1\bigr),

and define the :term:`algebraic height <algebraic-height>` $N$ of the equation by

.. math::

   N = n - 1 + |a_0| + |a_1| + \dots + |a_n|.

For each positive integer $N$, **only finitely many equations**—and hence only finitely many real algebraic numbers, say $\varphi(N)$ in number—possess height $N$, since $n \le N$ and $N - (n - 1)$ admits only finitely many decompositions into non-negative integers $|a_i|$. Discarding reducible equations and complex roots yields the opening rows of Cantor's enumeration:

.. list-table:: Real Algebraic Numbers Ordered by Cantor Height $N = 1, 2, 3, 4$
   :header-rows: 1
   :widths: 8 8 24 28 8 24

   * - $N$
     - $n$
     - $(|a_0|, |a_1|, \dots)$
     - Irreducible Equations (Real Roots)
     - $\varphi(N)$
     - Real Algebraic Roots $\omega$
   * - **$1$**
     - $1$
     - $(1, 0)$
     - $\omega = 0$
     - **$1$**
     - $0$
   * - **$2$**
     - $1$
     - $(1, 1)$
     - $\omega \pm 1 = 0$
     - **$2$**
     - $-1,\; +1$
   * - **$3$**
     - $1$
     - $(1, 2),\; (2, 1)$
     - $\omega \pm 2 = 0,\; 2\omega \pm 1 = 0$ *(note $\omega^2 + 1 = 0$ has no real roots)*
     - **$4$**
     - $-2,\; -\frac{1}{2},\; +\frac{1}{2},\; +2$
   * - **$4$**
     - $1, 2$
     - $(1, 3), (3, 1)$; $(1, 1, 1), (1, 0, 2), (2, 0, 1)$
     - $\omega \pm 3 = 0$, $3\omega \pm 1 = 0$, $\omega^2 \pm \omega - 1 = 0$, $\omega^2 - 2 = 0$, $2\omega^2 - 1 = 0$
     - **$12$**
     - $\pm 3,\; \pm\frac{1}{3},\; \frac{\pm 1 \pm \sqrt{5}}{2},\; \pm\sqrt{2},\; \pm\frac{1}{\sqrt{2}}$

Ordering roots within each finite height class $N = 1, 2, 3, 4, \dots$ by increasing magnitude enumerates **every real algebraic number** in a single sequence $\omega_1, \omega_2, \omega_3, \dots$.

§ 3. Cantor's Diagonal Construction of Transcendental Numbers
-------------------------------------------------------------

**3.** Conversely, the continuum of all real numbers—even within an arbitrarily tiny interval—is **not countable**, and Cantor's 1891 diagonal procedure immediately exhibits infinitely many :term:`transcendental numbers <transcendental-number>` inside any prescribed neighborhood.

Write every real algebraic number $\omega_1, \omega_2, \omega_3, \dots$ in infinite decimal form (noting that any decimal not ending in an infinite string of $9$'s has a unique representation). Suppose we wish to construct transcendental numbers sharing a prescribed $5$-decimal prefix $0.c_1 c_2 c_3 c_4 c_5\dots$:

* Choose the **$6$-th decimal digit** different from $9$ and different from the $6$-th decimal digit of $\omega_1$;
* Choose the **$7$-th decimal digit** different from $9$ and different from the $7$-th decimal digit of $\omega_2$;
* In general, choose the **$(5 + k)$-th decimal digit** different from $9$ and different from the $(5 + k)$-th decimal digit of $\omega_k$.

The resulting decimal fraction never terminates in repeating $9$'s and differs from *every* algebraic number $\omega_k$ in our complete table at the $(5 + k)$-th decimal place! Hence it is necessarily a **transcendental number**. Indeed, because at every decimal step (avoiding $9$ and one diagonal digit) we retain a free choice among **eight** digits, we can form—so to speak—$8^\infty$ transcendental numbers inside any interval, however small: *there are infinitely more transcendental numbers than algebraic numbers*.
