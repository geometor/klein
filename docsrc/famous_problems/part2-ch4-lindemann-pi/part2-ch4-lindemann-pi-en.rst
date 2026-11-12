:title: Part II, Chs. IV–V: The Transcendence of π and the Integraph (1897 English)
:layout: book

.. _fp-part2-ch4-lindemann-pi-en:

Part II, Chapters IV–V — The Transcendence of π and the Integraph
=================================================================

.. rubric:: Part II, Chapter IV (§§ 1–7, pp. 68–77) & Chapter V (§§ 1–3, pp. 78–80; :cite:`Ginn & Co., 1897 <klein:1897>`)

Chapter IV, § 1. Statement of Lindemann's Theorem for Conjugate Exponents
-------------------------------------------------------------------------

**1.** :person:`Lindemann's <lindemann>` proof of the transcendence of $\pi$ (:cite:`1882 <lindemann:1882>`) is a direct generalization of :person:`Hermite's <hermite>` method (:cite:`1873 <hermite:1873>`). Whereas Hermite proved that $\sum_{k=0}^n C_k e^k = 0$ is impossible for integer exponents $k$, Lindemann replaces each power $e^k$ by a symmetric sum of exponentials over :term:`conjugate algebraic numbers <conjugate-values>`:

**Lindemann's Theorem:** *The number $e$ cannot satisfy an equation with non-zero integer coefficients ($C_0 \neq 0$) of the form*

.. math::

   C_0 + C_1\bigl(e^{k_1} + e^{k_2} + \dots + e^{k_N}\bigr) + C_2\bigl(e^{l_1} + e^{l_2} + \dots + e^{l_{N'}}\bigr) + \dots = 0,

*where $k_1, \dots, k_N$ are the roots (real or complex, non-zero) of an algebraic equation with integer coefficients*

.. math::

   a k^N + a_1 k^{N-1} + \dots + a_N = 0 \qquad (a > 0,\; a_N \neq 0),

*and likewise $l_1, \dots, l_{N'}$ are the roots of $b l^{N'} + b_1 l^{N'-1} + \dots + b_{N'} = 0$ ($b > 0,\; b_{N'} \neq 0$), and so forth.* (In :person:`Leibniz's <leibniz>` terminology—where $x^\lambda$ for irrational algebraic $\lambda$ was called *interscendental*—$e$ is not even interscendental, but transcendental of a higher order.)

Because the leading coefficients $a, b, \dots$ need not equal $1$, symmetric functions of $k_1, \dots, k_N$ may be fractions; however, multiplying the roots by $a$ yields the **algebraic integers** $a k_1, \dots, a k_N$ satisfying the monic integer equation

.. math::

   (a k)^N + a_1(a k)^{N-1} + a_2 a (a k)^{N-2} + \dots + a_N a^{N-1} = 0,

whose rational symmetric functions are **ordinary rational integers**.

Chapter IV, §§ 2–3. The Auxiliary Polynomial $\psi(x)$ and Proof of Lindemann's Theorem
---------------------------------------------------------------------------------------

**2.** Retaining :person:`Gordan's <gordan>` umbral factorial symbol $h^r = r!$ (:cite:`1893 <gordan:1893>`), we introduce the generalized multiplier $M = \psi(h)$, where

.. math::

   \psi(x) = \frac{x^{p-1}\bigl[(k_1 - x)\cdots(k_N - x)\bigr]^p\,\bigl[(l_1 - x)\cdots(l_{N'} - x)\bigr]^p \cdots a^{Np + N'p + \dots} b^{Np + N'p + \dots}\cdots}{(p - 1)!},

and $p$ is a prime number chosen larger than $|C_0|$, $a, b, \dots$, and $|a_N|, |b_{N'}|, \dots$, eventually tending to $\infty$. The powers of $a, b, \dots$ ensure that in the expansions of both $\psi(h)$ and $\sum_{\nu=1}^N \psi(k_\nu + h)$, every symmetric coefficient numerator is an ordinary integer. Exactly as in Chapter III, $\psi$ satisfies three decisive properties:

1. **$\psi(h)$ is an integer not divisible by $p$:** Ordering $\psi(h) = \sum_{r=p-1}^{Np + N'p + \dots + p - 1} c_r h^r$, every numerator $(p - 1)!\,c_r$ is an integer; upon setting $h^r = r!$, all terms for $r \ge p$ contain the prime factor $p$, whereas the leading term ($r = p - 1$) equals

   .. math::

      (-1)^{p(N + N' + \dots)}\,a_N^p\,b_{N'}^p \cdots a^{(N-1)p + N'p + \dots}\,b^{Np + (N'-1)p + \dots} \not\equiv 0 \pmod p.

2. **Asymptotic vanishing as $p \to \infty$:** For any fixed finite complex argument $x$, writing $\psi(x) = \frac{K^p}{x\cdot (p - 1)!}$ shows that both $\psi(x)$ and $\sum_r |c_r|\,|x|^r$ tend to $0$ as $p \to \infty$.
3. **Every conjugate sum $\sum_{\nu=1}^N \psi(k_\nu + h)$ is an integer divisible by $p$:** In $\psi(k_\nu + h)$, the $\nu$-th factor $(k_\nu - k_\nu - h)$ equals $-h$, raising the lowest power of $h$ to $h^p$. Summing across $\nu = 1, \dots, N$ yields symmetric functions of the algebraic integers $a k_\nu, b l_\mu, \dots$:

   .. math::

      \sum_{\nu=1}^N \psi(k_\nu + h) = \sum_{r=p}^{Np + N'p + \dots + p - 1} C'_r h^r,

   where $(p - 1)!\,C'_r \in \mathbb{Z}$, so replacing $h^r$ by $r!$ ($r \ge p$) leaves an integer divisible by $p$!

**3.** Now multiply the assumed relation by $\psi(h)$. Because $k_\nu = k' + i k''$ may be complex with modulus $|k_\nu| = \sqrt{k'^2 + k''^2}$, the exponential splitting of Chapter III takes the complex-majorized form

.. math::

   e^{k_\nu}\cdot h^r = (k_\nu + h)^r + q_{r, k_\nu}\, k_\nu^r\, e^{|k_\nu|} \qquad \bigl(|q_{r, k_\nu}| < 1\bigr).

Summing over $r$ and over the conjugate roots $\nu = 1, \dots, N$ decomposes each block into an integer divisible by $p$ plus an arbitrarily small remainder:

.. math::

   \Biggl[C_0 \psi(h) + C_1 \sum_{\nu=1}^N \psi(k_\nu + h) + C_2 \sum_{\mu=1}^{N'} \psi(l_\mu + h) + \dots\Biggr]
   + \Biggl[C_1 \sum_{\nu=1}^N e^{|k_\nu|}\sum_r c_r k_\nu^r q_{r, k_\nu} + \dots\Biggr] = 0.

The first bracket is an integer congruent to $C_0 \psi(h) \not\equiv 0 \pmod p$ (hence $\ge 1$ in magnitude), whereas for sufficiently large $p$ the second bracket has modulus $< 1$—an impossibility! *(Note: if $C_0 = 0$ initially, multiplying by a suitable exponential or shifting exponents reduces to $C_0 \neq 0$.)*

Chapter IV, § 4. Lindemann's Corollary (Arbitrary Algebraic Exponents & Coefficients)
-------------------------------------------------------------------------------------

**4.** From Lindemann's Theorem we deduce immediately a far wider proposition (**Lindemann's Corollary**, or the **Lindemann–Weierstrass Theorem**):

* **Step A — Unrelated algebraic exponents with integer coefficients:** Suppose $C'_0 + C'_1 e^{k_1} + C'_2 e^{l_1} + \dots = 0$ ($C'_i \in \mathbb{Z}$, not all zero) for distinct algebraic numbers $k_1, l_1, \dots$. Forming the Galois product across all conjugate roots $k_\alpha$ ($\alpha = 1, \dots, N$), $l_\beta$ ($\beta = 1, \dots, N'$), etc.,

  .. math::

     \prod_{\alpha, \beta, \dots} \bigl(C'_0 + C'_1 e^{k_\alpha} + C'_2 e^{l_\beta} + \dots\bigr) = C_0 + C_1\bigl(e^{k_1} + \dots + e^{k_N}\bigr) + C_2\bigl(e^{k_1 + k_2} + \dots\bigr) + \dots,

  collects exponents into symmetric conjugate families satisfying integer equations, which by Lindemann's Theorem cannot vanish; hence no factor can vanish!
* **Step B — Arbitrary algebraic coefficients and algebraic exponents:** Next suppose $C_0 + C_1 e^k + C_2 e^l + \dots = 0$ where both the exponents $k, l, \dots$ (distinct) **and** the coefficients $C_0, C_1, C_2, \dots$ (not all zero) are algebraic numbers. Forming the product across all conjugates $C_0^{(\alpha)}, C_1^{(\beta)}, C_2^{(\gamma)}, \dots$ of the coefficients yields a non-trivial exponential polynomial whose coefficients are symmetric functions of algebraic numbers—hence rational numbers, and after clearing denominators, integers—which cannot vanish by Step A!

**General Statement of Lindemann's Corollary:** *In any non-trivial equation $C_0 + C_1 e^k + C_2 e^l + \dots = 0$ with distinct exponents, the coefficients $C_0, C_1, \dots$ and exponents $k, l, \dots$ cannot all be algebraic numbers.*

Chapter IV, §§ 5–7. Transcendence of $\pi$, $y = e^x$, and $y = \arcsin x$
--------------------------------------------------------------------------

**5. Transcendence of $\pi$:** Consider :person:`Euler's <euler>` equation

.. math::

   1 + e^{i\pi} = 0.

Here the coefficients $1, 1$ and the zero exponent in $1 = 1\cdot e^0$ are algebraic; by Lindemann's Corollary, the exponent $i\pi$ **cannot be algebraic**. Since $i = \sqrt{-1}$ is algebraic, **$\pi$ is a** :term:`transcendental number <transcendental-number>`!

**6. Arithmetic Avoidance of the Exponential Curve $y = e^x$:** Excluding the single trivial point $(x = 0, y = 1)$ (where $y - e^x = 0$ collapses to identical zero exponents $1\cdot e^0 - 1\cdot e^0 = 0$), the relation $y - e^x = 0$ (equivalently $x = \ln y$) forbids $x$ and $y$ from being algebraic simultaneously: **to every non-zero algebraic $x$ corresponds a transcendental $e^x$, and to every positive algebraic $y \neq 1$ corresponds a transcendental natural logarithm $\ln y$**. Geometrically, if we mark all algebraic points $(x, y) \in \overline{\mathbb{Q}}^2$—which cover the plane everywhere densely—the curve $y = e^x$ threads right through them **without meeting a single algebraic point except $(0, 1)$**!

**7. Arithmetic Avoidance of the Sinusoid $y = \arcsin x$:** Writing $y = \arcsin x$ in exponential form,

.. math::

   2 i x - e^{iy} + e^{-iy} = 0,

shows similarly that—excluding the origin $(x = 0, y = 0)$—$x$ and $y$ can never be algebraic simultaneously: **the curve $y = \arcsin x$ passes through no algebraic point of the plane except $(0, 0)$**.

Chapter V, §§ 1–3. The Integraph and the Geometric Construction of $\pi$
------------------------------------------------------------------------

**1.** Lindemann's Theorem settles the ancient quadrature of the circle in the most sweeping sense: **not only is $\pi$ unconstructible with straightedge and compasses, there does not even exist any higher algebraic curve $F(x, y) = 0$ with rational coefficients on which $\pi$ occurs as the ordinate for an algebraic abscissa!** Any genuine geometric construction of $\pi$ must employ a continuous *transcendental apparatus*.

**2.** Precisely such a continuous mechanical instrument is the :term:`integraph <integraph>`, invented by the engineer :person:`Bruno Abdank-Abakanowicz <abakanowicz>` (:cite:`*Die Integraphen*, Teubner, 1889; *Les intégraphes*, Gauthier-Villars, 1889 <abakanowicz:1889>`) and constructed by G. Coradi of Zürich. Given any differential curve $y = f(x)$, as a guiding stylus follows $(x, y)$ along $y = f(x)$, the linkage forms the auxiliary right triangle with vertices $(x, y)$, $(x, 0)$, and $(x - 1, 0)$, whose hypotenuse makes angle $\vartheta$ with the $X$-axis satisfying

.. math::

   \tan\vartheta = y = f(x).

A weighted, sharp-edged vertical steering roller is held strictly parallel to this variable hypotenuse so that its contact point $(X, Y)$ on the paper cannot slip sideways and advances with exact slope $\frac{dY}{dX} = y$, tracing the **integral curve**

.. math::

   Y = F(x) = \int f(x)\,dx

in one continuous stroke!

.. picture:: /_static/figures/fig_integraph_quadrature.svg
   :alt: Abdank-Abakanowicz's Mechanical Integraph Quadrature of the Circle x^2 + y^2 = r^2
   :caption: Mechanical Quadrature of the Circle by Abdank-Abakanowicz's Integraph (Klein Ch. V, §§ 2–3, Fig. 16): Guiding stylus on x^2 + y^2 = r^2 sets roller slope tan(theta) = y, tracing Y = (r^2/2) arcsin(x/r) + (x/2) sqrt(r^2 - x^2) with exact intercepts +-pi*r^2/4 and +-pi*r^2/2.

**3.** Selecting the **circle** $x^2 + y^2 = r^2$ as differential curve, the integraph traces the multi-branched integral curve

.. math::

   Y = \int \sqrt{r^2 - x^2}\,dx = \frac{r^2}{2}\arcsin\frac{x}{r} + \frac{x}{2}\sqrt{r^2 - x^2},

consisting of congruent repeating branches:

* Along the **$Y$-axis ($X = 0$)**, the branches cut off the exact ordinates $0,\; \pm\frac{\pi r^2}{2},\; \pm\pi r^2,\; \dots$;
* Along the **vertical tangents $X = \pm r$**, the branches cut off $\pm\frac{\pi r^2}{4},\; \pm\frac{3\pi r^2}{4},\; \dots$.

Setting $r = 1$, the integraph pen traces $\frac{\pi}{4}$, $\frac{\pi}{2}$, and $\pi$ directly, smoothly, and sharply—realizing an actual constructive quadrature of the circle by continuous mechanical motion along the very path envisioned by the ancient inventors of the :term:`quadratrix <quadratrix>`.
