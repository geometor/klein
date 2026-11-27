:title: Part I, Ch. III: The Division of the Circle into Equal Parts (1897 English)
:layout: book
:canonical_id: Ch. III
:order: 3
:tracks: English: ch_03-en | German: ch_03-de | Summary: ch_03-summary | Notes: ch_03-notes

.. _fp-part_1-ch_03-en:
.. _fp-part1-ch_03-en:
.. _fp-ch_03-en:
.. _fp-part1-ch3-cyclotomy-en:

Part I, Chapter III — The Division of the Circle into Equal Parts
=================================================================

.. rubric:: Part I, Chapter III (§§ 1–8; :cite:`Ginn & Co., 1897, pp. 16–23 <klein:1897>`)

§ 1. History of the Problem
---------------------------

**1.** The problem of dividing a given circle into :math:`n` equal parts has come down from antiquity; for more than two millennia mathematicians knew the possibility of solving it with straightedge and compasses only when :math:`n = 2^h`, :math:`3`, :math:`5`, or the product of any two or three of these numbers (:person:`Euclid <euclid>`, :cite:`*Elements*, Book IV <euclid:elements>`).

In his *Disquisitiones Arithmeticae* (:cite:`1801 <gauss:1801>`), :person:`Gauss <gauss>` extended this series of numbers at a single stroke by showing that the division into :math:`p` equal parts is **possible for every prime number of the form**

.. math::

   p = 2^{2^\mu} + 1,

**and impossible for all other odd prime numbers and their powers**.

* If in :math:`p = 2^{2^\mu} + 1` we set :math:`\mu = 0` and :math:`\mu = 1`, we obtain :math:`p = 3` and :math:`p = 5`, cases already known to the ancients.
* For :math:`\mu = 2` we obtain :math:`p = 2^{2^2} + 1 = 17`, the celebrated regular heptadecagon completely discussed by :person:`Gauss <gauss>` (discovered March 30, 1796).
* For :math:`\mu = 3` we obtain :math:`p = 2^{2^3} + 1 = 257`, likewise a :term:`Fermat prime <fermat-prime>`; the regular polygon of :math:`257` sides is constructible, and :person:`Richelot <richelot>` published an extended investigation of it in *Crelle's Journal*, Vol. IX (:cite:`1832, pp. 1–26, 146–161, 209–230, 337–357 <richelot:1832>`), entitled *De resolutione algebraica aequationis* :math:`X^{257} = 1`, *sive de divisione circuli per bisectionem anguli septies repetitam in partes* :math:`257` *inter se aequales commentatio coronata*.
* Similarly for :math:`\mu = 4`, since :math:`2^{2^4} + 1 = 65537` is a prime number. To the regular polygon of :math:`65537` sides :person:`Professor Hermes <hermes>` of Lingen devoted ten years of his life, examining with care all the roots furnished by Gauss's method; his manuscripts are preserved in the collection of the mathematical seminary at Göttingen (compare a communication of Professor Hermes in :cite:`No. 3 of the *Göttinger Nachrichten* for 1894 <hermes:1894>`).
* On the other hand, :math:`\mu = 5`, :math:`\mu = 6`, and :math:`\mu = 7` yield *no* prime numbers (for :math:`\mu = 5`, :person:`Euler <euler>` showed :math:`2^{32} + 1 = 641 \times 6700417`). For :math:`\mu = 8` no one has yet determined whether :math:`2^{256} + 1` is prime or composite. The proof that the huge numbers corresponding to :math:`\mu = 5, 6, 7` are composite has required a great expenditure of labor and ingenuity; it is therefore quite possible that :math:`\mu = 4` is the last exponent for which a prime solution exists.

.. picture:: /_static/figures/fig_constructibility_polygons.svg
   :alt: Gauss-Wantzel Polygon Constructibility (n = 3..18): Euler totient powers of 2 vs odd prime obstructions
   :caption: Gauss–Wantzel Polygon Constructibility (n = 3..18): Constructible regular polygons (green, totient phi(n) = 2^k) contrasted with non-constructible polygons n = 7, 9, 11, 13, 14, 18 (red dashed).

§§ 2–4. Reduction to Prime Powers and Gauss's Prime Numbers
-----------------------------------------------------------

**2.** We may immediately restrict the problem of dividing the circle into :math:`n` equal parts to the cases where :math:`n` is a prime number :math:`p` or a prime power :math:`p^\alpha`. For if :math:`n = \mu\nu` is composite with :math:`\mu` and :math:`\nu` relatively prime (:math:`\gcd(\mu, \nu) = 1`), Euclidean division furnishes integers :math:`a` and :math:`b` (one positive, one negative) such that

.. math::

   1 = a\mu + b\nu, \qquad \text{whence} \qquad \frac{1}{\mu\nu} = \frac{a}{\nu} + \frac{b}{\mu}.

To divide the circle into :math:`\mu\nu = n` equal parts, it therefore suffices to superpose :math:`a` parts of the :math:`\nu`-division with :math:`b` parts of the :math:`\mu`-division. Thus for :math:`n = 15 = 3 \cdot 5`, we have

.. math::

   \frac{1}{15} = \frac{2}{3} - \frac{3}{5},

which is precisely the arithmetic content of :person:`Euclid's <euclid>` construction of the regular pentadecagon (:cite:`*Elements* IV.16 <euclid:elements>`).

**3.** As will appear in § 5, division into :math:`p` equal parts (:math:`p` prime) is possible only when :math:`p = 2^h + 1`. Let us first prove that a prime number can have the form :math:`p = 2^h + 1` **only when the exponent** :math:`h` **is itself a power of** :math:`2`, :math:`h = 2^\mu`.

First proof (by Fermat's Little Theorem): If :math:`p` is prime and :math:`a` is an integer not divisible by :math:`p`, then :math:`a^{p-1} \equiv +1 \pmod p`. If :math:`s` is the *least* positive exponent satisfying :math:`a^s \equiv +1 \pmod p`, then :math:`s` is necessarily a divisor of :math:`p - 1`. (In particular, when :math:`s = p - 1`, :math:`a` is called a *primitive root* modulo :math:`p`; every prime :math:`p` possesses primitive roots, a fact we shall use in Chapter IV.) Suppose now that :math:`p = 2^h + 1` is prime, and let :math:`s` be the least positive exponent such that

.. math::

   2^s \equiv +1 \pmod p.

Since :math:`2^h = p - 1 < p < 2^s`, we have :math:`s > h`. Moreover, :math:`p = 2^h + 1` gives

.. math::

   2^h \equiv -1 \pmod p.

Dividing :math:`2^s \equiv +1` by :math:`2^h \equiv -1` gives :math:`2^{s-h} \equiv -1 \pmod p`, whence :math:`s - h \ge h`, i.e., :math:`s \ge 2h`. Conversely, squaring :math:`2^h \equiv -1 \pmod p` yields :math:`2^{2h} \equiv +1 \pmod p`, so by minimality of :math:`s` we have :math:`s \le 2h`, and consequently :math:`s = 2h`. Now :math:`s = 2h` must divide :math:`p - 1 = 2^h`; therefore :math:`h` divides :math:`2^{h-1}` and must itself be a power of :math:`2`, :math:`h = 2^\mu`. Hence primes of the form :math:`2^h + 1` are necessarily of the form :math:`2^{2^\mu} + 1`.

**4.** Second proof (by elementary algebraic factorization): Suppose :math:`h` were divisible by an odd integer :math:`2n + 1 > 1`, so that :math:`h = h'(2n + 1)`. By the identity

.. math::

   x^{2n+1} + 1 = (x + 1)\!\left(x^{2n} - x^{2n-1} + \dots - x + 1\right)

evaluated at :math:`x = 2^{h'}`, the number :math:`p = 2^{h'(2n+1)} + 1` is divisible by the proper factor :math:`2^{h'} + 1 > 1`, and therefore cannot be prime!

§ 5. The Cyclotomic Equation
----------------------------

**5.** We now reach our fundamental proposition: *For an odd prime* :math:`p`, *dividing the circle into* :math:`p` *equal parts with straightedge and compasses is impossible unless* :math:`p = 2^h + 1 = 2^{2^\mu} + 1`.

Trace in the complex :math:`z`-plane (:math:`z = x + iy`) the circle of radius :math:`1` centered at the origin. Dividing this circle into :math:`n` equal parts starting at :math:`z = 1` is algebraically equivalent to solving :math:`z^n - 1 = 0`. Suppressing the known initial vertex :math:`z = 1` by dividing out :math:`z - 1`, we obtain the **cyclotomic equation**:

.. math::

   \frac{z^n - 1}{z - 1} = z^{n-1} + z^{n-2} + \dots + z + 1 = 0.

When :math:`n = p` is prime, the essential point of the proof is to show that this equation of degree :math:`p - 1` is **irreducible** over :math:`\mathbb{Q}`. Once irreducibility is proved, Chapter I, § 15 requires its degree :math:`p - 1` to be a power of :math:`2`, forcing :math:`p = 2^h + 1 = 2^{2^\mu} + 1` and explaining why :person:`Gauss's <gauss>` primes occupy their unique position.

§ 6. Gauss's Lemma
------------------

**6.** To establish irreducibility, we first prove **Gauss's Lemma**: *If a monic polynomial with integer coefficients,*

.. math::

   F(z) = z^m + A z^{m-1} + B z^{m-2} + \dots + L z + M,

*can be resolved into two monic factors* :math:`f(z)` *and* :math:`\varphi(z)` *with rational coefficients*,

.. math::

   F(z) = f(z)\,\varphi(z) = \left(z^{m'} + \alpha_1 z^{m'-1} + \dots\right)\!\left(z^{m''} + \beta_1 z^{m''-1} + \dots\right),

*then all the coefficients* :math:`\alpha_i` *and* :math:`\beta_j` *must actually be integers*.

*Proof.* Suppose the :math:`\alpha`'s or :math:`\beta`'s were fractional. Reduce the coefficients of :math:`f(z)` to their least common positive denominator :math:`a_0`, and those of :math:`\varphi(z)` to their least common positive denominator :math:`b_0`. Multiplying both sides by :math:`a_0 b_0` yields

.. math::

   a_0 b_0 F(z) = f_1(z)\,\varphi_1(z) = \left(a_0 z^{m'} + a_1 z^{m'-1} + \dots\right)\!\left(b_0 z^{m''} + b_1 z^{m''-1} + \dots\right),

where :math:`a_0, a_1, \dots` are coprime integers (:math:`\gcd(a_0, a_1, \dots) = 1`) and likewise :math:`b_0, b_1, \dots` are coprime integers. If :math:`a_0 b_0 > 1`, let :math:`q` be any prime divisor of :math:`a_0 b_0`. Because neither all :math:`a`'s nor all :math:`b`'s are divisible by :math:`q`, let :math:`a_i` be the *first* coefficient in :math:`f_1(z)` not divisible by :math:`q`, and :math:`b_k` the *first* coefficient in :math:`\varphi_1(z)` not divisible by :math:`q`. In the expanded product :math:`f_1(z)\varphi_1(z)`, the coefficient of :math:`z^{m' + m'' - i - k}` equals

.. math::

   a_i b_k + a_{i-1} b_{k+1} + a_{i-2} b_{k+2} + \dots + a_{i+1} b_{k-1} + a_{i+2} b_{k-2} + \dots.

By construction, every term after :math:`a_i b_k` contains either an :math:`a_{i-r}` (:math:`r \ge 1`) or a :math:`b_{k-s}` (:math:`s \ge 1`) divisible by :math:`q`, whereas :math:`a_i b_k` is *not* divisible by the prime :math:`q`. Yet on the left-hand side :math:`a_0 b_0 F(z)`, every coefficient is divisible by :math:`a_0 b_0` and hence by :math:`q`—a contradiction! Therefore :math:`a_0 b_0 = 1`, i.e., :math:`a_0 = b_0 = 1`, and all :math:`\alpha_i, \beta_j` are integers.

§§ 7–8. Irreducibility of the Cyclotomic Equation for Primes and Prime Squares
------------------------------------------------------------------------------

**7.** By Gauss's Lemma, to prove :math:`f(z) = z^{p-1} + z^{p-2} + \dots + z + 1` irreducible for any prime :math:`p`, we need only show it admits no factorization with *integer* coefficients. Following :person:`Eisenstein's <eisenstein>` remarkably simple method (:cite:`*Crelle's Journal*, Vol. XXXIX, 1850, p. 167 <eisenstein:1850>`), substitute :math:`z = x + 1`:

.. math::

   f(x + 1) = \frac{(x + 1)^p - 1}{x} = x^{p-1} + p\,x^{p-2} + \frac{p(p-1)}{1\cdot 2} x^{p-3} + \dots + \frac{p(p-1)}{1\cdot 2} x + p = 0.

Every coefficient after the leading term :math:`x^{p-1}` is divisible by the prime :math:`p`, and the constant term is :math:`p` itself (not divisible by :math:`p^2`). **Any polynomial of this Eisenstein form is irreducible.** For if it factored over :math:`\mathbb{Z}` as

.. math::

   f(x + 1) = \left(x^m + a_1 x^{m-1} + \dots + a_{m-1} x + a_m\right)\!\left(x^{m'} + b_1 x^{m'-1} + \dots + b_{m'-1} x + b_{m'}\right),

the constant term :math:`a_m b_{m'} = p` would force one factor—say :math:`a_m = \pm p`—to be divisible by :math:`p` and the other to be :math:`b_{m'} = \pm 1`. Examining the coefficient of :math:`x`, namely :math:`a_{m-1} b_{m'} + a_m b_{m'-1} \equiv 0 \pmod p`, gives :math:`p \mid a_{m-1}` since :math:`b_{m'} = \pm 1`; examining :math:`x^2, x^3, \dots` successively forces :math:`p \mid a_{m-2}, \dots, p \mid a_1`, and finally :math:`p \mid 1` (the leading coefficient of :math:`x^m`), which is absurd! Thus :math:`\Phi_p(z) = 0` is irreducible of degree :math:`p - 1`. In particular, for :math:`p = 7` (:math:`\deg = 6 \neq 2^h`), :math:`p = 11` (:math:`\deg = 10`), and :math:`p = 13` (:math:`\deg = 12`), **the regular** :math:`7`-**gon**, :math:`11`-**gon, and** :math:`13`-**gon cannot be constructed with straightedge and compasses**.

**8.** Finally, consider a prime power :math:`n = p^\alpha` (:math:`\alpha \ge 2`) for an odd prime :math:`p > 2`. Since dividing the circle into :math:`p^\alpha` equal parts automatically divides it into :math:`p^2` equal parts, it suffices to prove that **division into** :math:`p^2` **equal parts is impossible whenever** :math:`p > 2`. Suppressing from :math:`z^{p^2} - 1 = 0` all roots belonging to the :math:`p`-division (:math:`z^p - 1 = 0`) leaves the primitive :math:`p^2`-cyclotomic equation:

.. math::

   \frac{z^{p^2} - 1}{z^p - 1} = z^{p(p-1)} + z^{p(p-2)} + \dots + z^p + 1 = 0.

Substituting :math:`z = x + 1` across these :math:`p` summands produces

.. math::

   (x + 1)^{p(p-1)} + (x + 1)^{p(p-2)} + \dots + (x + 1)^p + 1 = x^{p(p-1)} + p\cdot \chi(x) = 0,

where :math:`\chi(x)` is an integer polynomial with constant term :math:`\chi(0) = 1` (since :math:`(x + 1)^{kp} \equiv x^{kp} + 1 \pmod p` for every :math:`k`). By § 7, this polynomial is **irreducible** over :math:`\mathbb{Q}`, and its degree is :math:`p(p - 1)`. Since :math:`p > 2` is an odd prime, :math:`p(p - 1)` contains the odd factor :math:`p` and can *never* be a power of :math:`2`! Thus even for Gauss's primes (:math:`p = 3 \implies p^2 = 9` of degree :math:`6`; :math:`p = 5 \implies p^2 = 25` of degree :math:`20`), division into :math:`p^2` or :math:`p^\alpha` (:math:`\alpha \ge 2`) parts is impossible; only :math:`p = 2` admits repeated powers :math:`2^\alpha`.
