:title: Part I, Ch. III: The Division of the Circle into Equal Parts (1897 English)
:layout: book

.. _fp-part1-ch3-cyclotomy-en:

Part I, Chapter III — The Division of the Circle into Equal Parts
=================================================================

.. rubric:: Part I, Chapter III (§§ 1–8; :cite:`Ginn & Co., 1897, pp. 16–23 <klein:1897>`)

§ 1. History of the Problem
---------------------------

**1.** The problem of dividing a given circle into $n$ equal parts has come down from antiquity; for more than two millennia mathematicians knew the possibility of solving it with straightedge and compasses only when $n = 2^h$, $3$, $5$, or the product of any two or three of these numbers (:person:`Euclid <euclid>`, :cite:`*Elements*, Book IV <euclid:elements>`).

In his *Disquisitiones Arithmeticae* (:cite:`1801 <gauss:1801>`), :person:`Gauss <gauss>` extended this series of numbers at a single stroke by showing that the division into $p$ equal parts is **possible for every prime number of the form**

.. math::

   p = 2^{2^\mu} + 1,

**and impossible for all other odd prime numbers and their powers**.

* If in $p = 2^{2^\mu} + 1$ we set $\mu = 0$ and $\mu = 1$, we obtain $p = 3$ and $p = 5$, cases already known to the ancients.
* For $\mu = 2$ we obtain $p = 2^{2^2} + 1 = 17$, the celebrated regular heptadecagon completely discussed by :person:`Gauss <gauss>` (discovered March 30, 1796).
* For $\mu = 3$ we obtain $p = 2^{2^3} + 1 = 257$, likewise a :term:`Fermat prime <fermat-prime>`; the regular polygon of $257$ sides is constructible, and :person:`Richelot <richelot>` published an extended investigation of it in *Crelle's Journal*, Vol. IX (:cite:`1832, pp. 1–26, 146–161, 209–230, 337–357 <richelot:1832>`), entitled *De resolutione algebraica aequationis $X^{257} = 1$, sive de divisione circuli per bisectionem anguli septies repetitam in partes $257$ inter se aequales commentatio coronata*.
* Similarly for $\mu = 4$, since $2^{2^4} + 1 = 65537$ is a prime number. To the regular polygon of $65537$ sides :person:`Professor Hermes <hermes>` of Lingen devoted ten years of his life, examining with care all the roots furnished by Gauss's method; his manuscripts are preserved in the collection of the mathematical seminary at Göttingen (compare a communication of Professor Hermes in :cite:`No. 3 of the *Göttinger Nachrichten* for 1894 <hermes:1894>`).
* On the other hand, $\mu = 5$, $\mu = 6$, and $\mu = 7$ yield *no* prime numbers (for $\mu = 5$, :person:`Euler <euler>` showed $2^{32} + 1 = 641 \times 6700417$). For $\mu = 8$ no one has yet determined whether $2^{256} + 1$ is prime or composite. The proof that the huge numbers corresponding to $\mu = 5, 6, 7$ are composite has required a great expenditure of labor and ingenuity; it is therefore quite possible that $\mu = 4$ is the last exponent for which a prime solution exists.

.. picture:: /_static/figures/fig_constructibility_polygons.svg
   :alt: Gauss-Wantzel Polygon Constructibility (n = 3..18): Euler totient powers of 2 vs odd prime obstructions
   :caption: Gauss–Wantzel Polygon Constructibility (n = 3..18): Constructible regular polygons (green, totient phi(n) = 2^k) contrasted with non-constructible polygons n = 7, 9, 11, 13, 14, 18 (red dashed).

§§ 2–4. Reduction to Prime Powers and Gauss's Prime Numbers
-----------------------------------------------------------

**2.** We may immediately restrict the problem of dividing the circle into $n$ equal parts to the cases where $n$ is a prime number $p$ or a prime power $p^\alpha$. For if $n = \mu\nu$ is composite with $\mu$ and $\nu$ relatively prime ($\gcd(\mu, \nu) = 1$), Euclidean division furnishes integers $a$ and $b$ (one positive, one negative) such that

.. math::

   1 = a\mu + b\nu, \qquad \text{whence} \qquad \frac{1}{\mu\nu} = \frac{a}{\nu} + \frac{b}{\mu}.

To divide the circle into $\mu\nu = n$ equal parts, it therefore suffices to superpose $a$ parts of the $\nu$-division with $b$ parts of the $\mu$-division. Thus for $n = 15 = 3 \cdot 5$, we have

.. math::

   \frac{1}{15} = \frac{2}{3} - \frac{3}{5},

which is precisely the arithmetic content of :person:`Euclid's <euclid>` construction of the regular pentadecagon (:cite:`*Elements* IV.16 <euclid:elements>`).

**3.** As will appear in § 5, division into $p$ equal parts ($p$ prime) is possible only when $p = 2^h + 1$. Let us first prove that a prime number can have the form $p = 2^h + 1$ **only when the exponent $h$ is itself a power of $2$, $h = 2^\mu$**.

First proof (by Fermat's Little Theorem): If $p$ is prime and $a$ is an integer not divisible by $p$, then $a^{p-1} \equiv +1 \pmod p$. If $s$ is the *least* positive exponent satisfying $a^s \equiv +1 \pmod p$, then $s$ is necessarily a divisor of $p - 1$. (In particular, when $s = p - 1$, $a$ is called a *primitive root* modulo $p$; every prime $p$ possesses primitive roots, a fact we shall use in Chapter IV.) Suppose now that $p = 2^h + 1$ is prime, and let $s$ be the least positive exponent such that

.. math::

   2^s \equiv +1 \pmod p.

Since $2^h = p - 1 < p < 2^s$, we have $s > h$. Moreover, $p = 2^h + 1$ gives

.. math::

   2^h \equiv -1 \pmod p.

Dividing $2^s \equiv +1$ by $2^h \equiv -1$ gives $2^{s-h} \equiv -1 \pmod p$, whence $s - h \ge h$, i.e., $s \ge 2h$. Conversely, squaring $2^h \equiv -1 \pmod p$ yields $2^{2h} \equiv +1 \pmod p$, so by minimality of $s$ we have $s \le 2h$, and consequently $s = 2h$. Now $s = 2h$ must divide $p - 1 = 2^h$; therefore $h$ divides $2^{h-1}$ and must itself be a power of $2$, $h = 2^\mu$. Hence primes of the form $2^h + 1$ are necessarily of the form $2^{2^\mu} + 1$.

**4.** Second proof (by elementary algebraic factorization): Suppose $h$ were divisible by an odd integer $2n + 1 > 1$, so that $h = h'(2n + 1)$. By the identity

.. math::

   x^{2n+1} + 1 = (x + 1)\!\left(x^{2n} - x^{2n-1} + \dots - x + 1\right)

evaluated at $x = 2^{h'}$, the number $p = 2^{h'(2n+1)} + 1$ is divisible by the proper factor $2^{h'} + 1 > 1$, and therefore cannot be prime!

§ 5. The Cyclotomic Equation
----------------------------

**5.** We now reach our fundamental proposition: *For an odd prime $p$, dividing the circle into $p$ equal parts with straightedge and compasses is impossible unless $p = 2^h + 1 = 2^{2^\mu} + 1$.*

Trace in the complex $z$-plane ($z = x + iy$) the circle of radius $1$ centered at the origin. Dividing this circle into $n$ equal parts starting at $z = 1$ is algebraically equivalent to solving $z^n - 1 = 0$. Suppressing the known initial vertex $z = 1$ by dividing out $z - 1$, we obtain the **cyclotomic equation**:

.. math::

   \frac{z^n - 1}{z - 1} = z^{n-1} + z^{n-2} + \dots + z + 1 = 0.

When $n = p$ is prime, the essential point of the proof is to show that this equation of degree $p - 1$ is **irreducible** over $\mathbb{Q}$. Once irreducibility is proved, Chapter I, § 15 requires its degree $p - 1$ to be a power of $2$, forcing $p = 2^h + 1 = 2^{2^\mu} + 1$ and explaining why :person:`Gauss's <gauss>` primes occupy their unique position.

§ 6. Gauss's Lemma
------------------

**6.** To establish irreducibility, we first prove **Gauss's Lemma**: *If a monic polynomial with integer coefficients,*

.. math::

   F(z) = z^m + A z^{m-1} + B z^{m-2} + \dots + L z + M,

*can be resolved into two monic factors $f(z)$ and $\varphi(z)$ with rational coefficients,*

.. math::

   F(z) = f(z)\,\varphi(z) = \left(z^{m'} + \alpha_1 z^{m'-1} + \dots\right)\!\left(z^{m''} + \beta_1 z^{m''-1} + \dots\right),

*then all the coefficients $\alpha_i$ and $\beta_j$ must actually be integers.*

*Proof.* Suppose the $\alpha$'s or $\beta$'s were fractional. Reduce the coefficients of $f(z)$ to their least common positive denominator $a_0$, and those of $\varphi(z)$ to their least common positive denominator $b_0$. Multiplying both sides by $a_0 b_0$ yields

.. math::

   a_0 b_0 F(z) = f_1(z)\,\varphi_1(z) = \left(a_0 z^{m'} + a_1 z^{m'-1} + \dots\right)\!\left(b_0 z^{m''} + b_1 z^{m''-1} + \dots\right),

where $a_0, a_1, \dots$ are coprime integers ($\gcd(a_0, a_1, \dots) = 1$) and likewise $b_0, b_1, \dots$ are coprime integers. If $a_0 b_0 > 1$, let $q$ be any prime divisor of $a_0 b_0$. Because neither all $a$'s nor all $b$'s are divisible by $q$, let $a_i$ be the *first* coefficient in $f_1(z)$ not divisible by $q$, and $b_k$ the *first* coefficient in $\varphi_1(z)$ not divisible by $q$. In the expanded product $f_1(z)\varphi_1(z)$, the coefficient of $z^{m' + m'' - i - k}$ equals

.. math::

   a_i b_k + a_{i-1} b_{k+1} + a_{i-2} b_{k+2} + \dots + a_{i+1} b_{k-1} + a_{i+2} b_{k-2} + \dots.

By construction, every term after $a_i b_k$ contains either an $a_{i-r}$ ($r \ge 1$) or a $b_{k-s}$ ($s \ge 1$) divisible by $q$, whereas $a_i b_k$ is *not* divisible by the prime $q$. Yet on the left-hand side $a_0 b_0 F(z)$, every coefficient is divisible by $a_0 b_0$ and hence by $q$—a contradiction! Therefore $a_0 b_0 = 1$, i.e., $a_0 = b_0 = 1$, and all $\alpha_i, \beta_j$ are integers.

§§ 7–8. Irreducibility of the Cyclotomic Equation for Primes and Prime Squares
------------------------------------------------------------------------------

**7.** By Gauss's Lemma, to prove $f(z) = z^{p-1} + z^{p-2} + \dots + z + 1$ irreducible for any prime $p$, we need only show it admits no factorization with *integer* coefficients. Following :person:`Eisenstein's <eisenstein>` remarkably simple method (:cite:`*Crelle's Journal*, Vol. XXXIX, 1850, p. 167 <eisenstein:1850>`), substitute $z = x + 1$:

.. math::

   f(x + 1) = \frac{(x + 1)^p - 1}{x} = x^{p-1} + p\,x^{p-2} + \frac{p(p-1)}{1\cdot 2} x^{p-3} + \dots + \frac{p(p-1)}{1\cdot 2} x + p = 0.

Every coefficient after the leading term $x^{p-1}$ is divisible by the prime $p$, and the constant term is $p$ itself (not divisible by $p^2$). **Any polynomial of this Eisenstein form is irreducible.** For if it factored over $\mathbb{Z}$ as

.. math::

   f(x + 1) = \left(x^m + a_1 x^{m-1} + \dots + a_{m-1} x + a_m\right)\!\left(x^{m'} + b_1 x^{m'-1} + \dots + b_{m'-1} x + b_{m'}\right),

the constant term $a_m b_{m'} = p$ would force one factor—say $a_m = \pm p$—to be divisible by $p$ and the other to be $b_{m'} = \pm 1$. Examining the coefficient of $x$, namely $a_{m-1} b_{m'} + a_m b_{m'-1} \equiv 0 \pmod p$, gives $p \mid a_{m-1}$ since $b_{m'} = \pm 1$; examining $x^2, x^3, \dots$ successively forces $p \mid a_{m-2}, \dots, p \mid a_1$, and finally $p \mid 1$ (the leading coefficient of $x^m$), which is absurd! Thus $\Phi_p(z) = 0$ is irreducible of degree $p - 1$. In particular, for $p = 7$ ($\deg = 6 \neq 2^h$), $p = 11$ ($\deg = 10$), and $p = 13$ ($\deg = 12$), **the regular $7$-gon, $11$-gon, and $13$-gon cannot be constructed with straightedge and compasses**.

**8.** Finally, consider a prime power $n = p^\alpha$ ($\alpha \ge 2$) for an odd prime $p > 2$. Since dividing the circle into $p^\alpha$ equal parts automatically divides it into $p^2$ equal parts, it suffices to prove that **division into $p^2$ equal parts is impossible whenever $p > 2$**. Suppressing from $z^{p^2} - 1 = 0$ all roots belonging to the $p$-division ($z^p - 1 = 0$) leaves the primitive $p^2$-cyclotomic equation:

.. math::

   \frac{z^{p^2} - 1}{z^p - 1} = z^{p(p-1)} + z^{p(p-2)} + \dots + z^p + 1 = 0.

Substituting $z = x + 1$ across these $p$ summands produces

.. math::

   (x + 1)^{p(p-1)} + (x + 1)^{p(p-2)} + \dots + (x + 1)^p + 1 = x^{p(p-1)} + p\cdot \chi(x) = 0,

where $\chi(x)$ is an integer polynomial with constant term $\chi(0) = 1$ (since $(x + 1)^{kp} \equiv x^{kp} + 1 \pmod p$ for every $k$). By § 7, this polynomial is **irreducible** over $\mathbb{Q}$, and its degree is $p(p - 1)$. Since $p > 2$ is an odd prime, $p(p - 1)$ contains the odd factor $p$ and can *never* be a power of $2$! Thus even for Gauss's primes ($p = 3 \implies p^2 = 9$ of degree $6$; $p = 5 \implies p^2 = 25$ of degree $20$), division into $p^2$ or $p^\alpha$ ($\alpha \ge 2$) parts is impossible; only $p = 2$ admits repeated powers $2^\alpha$.
