:title: Part I, Ch. I: Algebraic Equations Solvable by Square Roots (1897 English)
:layout: book
:canonical_id: Ch. I
:order: 1

.. _fp-part_1-ch_01-en:
.. _fp-part1-ch_01-en:
.. _fp-ch_01-en:
.. _fp-part1-ch1-square-roots-en:

Part I, Chapter I — Algebraic Equations Solvable by Square Roots
================================================================

.. rubric:: Part I: The Possibility of the Construction of Algebraic Expressions — Chapter I (§§ 1–15; :cite:`Ginn & Co., 1897, pp. 5–12 <klein:1897>`)

§§ 1–4. Structure of the Expression :math:`x` to be Constructed
---------------------------------------------------------------

**1.** Consider an algebraic expression :math:`x` capable of being constructed with straightedge and compasses from given segments. By our fundamental theorem (:ref:`Introduction <fp-intro-en>`), :math:`x` is derived from known quantities—which, upon choosing a unit segment, we may treat as rational numbers (or rational parameters defining a :term:`domain of rationality <domain-of-rationality>`)—by a finite number of rational operations and extractions of square roots.

**2.** In order to classify the complexity of such radical expressions, we assign to every square-root expression a definite :term:`order <radical-order>` :math:`\mu` according to the depth of superimposed radical signs:

* A purely rational quantity :math:`R` (involving no square roots) is said to be of **order** :math:`0`.
* An expression formed rationally from rational quantities and simple square roots :math:`\sqrt{R_1}, \sqrt{R_2}, \dots` (where :math:`R_1, R_2, \dots` are rational) is of **order** :math:`1`; for example,

  .. math::

     \frac{\alpha + \beta \sqrt{R_1} + \gamma \sqrt{R_2}}{\delta + \varepsilon \sqrt{R_3}}.

* An expression formed rationally from quantities of order :math:`\le 1` and square roots of expressions of order :math:`1`, such as :math:`\sqrt{p + q\sqrt{R_1}}`, is of **order** :math:`2`.
* In general, an expression :math:`x` is of **order** :math:`\mu` if the deepest chain of nested square roots occurring within :math:`x` superimposes :math:`\mu` radical signs, so that every square root of order :math:`\mu` extracts the root of an expression of order :math:`\mu - 1`.

**3.** Suppose that throughout the entire construction of :math:`x` there occur in all :math:`m` distinct square roots :math:`Q_1, Q_2, \dots, Q_m`, arranged in non-decreasing order of their radical depth (:math:`1 \le \text{ord}(Q_j) \le \mu`).

**4.** Before proceeding further, we stipulate that **none of the** :math:`m` **square roots** :math:`Q_1, \dots, Q_m` **can be expressed rationally in terms of the remaining square roots and known rational quantities**. For if any radical :math:`Q_k` were equal to a rational function of the previous radicals :math:`Q_1, \dots, Q_{k-1}`, we should simply replace :math:`Q_k` everywhere by that rational expression and thereby reduce the total number :math:`m` of independent square roots by one. By repeating such reductions from the lowest order upward, we ensure that the :math:`m` square roots :math:`Q_1, \dots, Q_m` are algebraically independent over the preceding stages.

§§ 5–6. Normal Form of :math:`x`
--------------------------------

**5.** Let :math:`Q_\mu` denote one particular square root among those of highest order :math:`\mu` appearing in :math:`x`. As a function of :math:`Q_\mu` alone, :math:`x` is a rational quotient whose numerator and denominator are polynomials in :math:`Q_\mu` with coefficients involving only the remaining :math:`m - 1` square roots. Since :math:`Q_\mu^2` is an expression of order :math:`\mu - 1`, every even power :math:`Q_\mu^{2k}` reduces to lower-order radicals, and every odd power :math:`Q_\mu^{2k+1}` reduces to :math:`Q_\mu` multiplied by lower-order radicals. Thus :math:`x` assumes the fractional linear form

.. math::

   x = \frac{a + b Q_\mu}{c + d Q_\mu},

where :math:`a, b, c, d` do not contain :math:`Q_\mu`.

**6.** Multiplying numerator and denominator by the conjugate factor :math:`c - d Q_\mu` (note that :math:`c + d Q_\mu \neq 0`, since otherwise :math:`Q_\mu = -c/d` would be rationally expressible through the remaining radicals, contrary to § 4), we clear :math:`Q_\mu` from the denominator:

.. math::

   x = \frac{(a + b Q_\mu)(c - d Q_\mu)}{c^2 - d^2 Q_\mu^2} = \alpha + \beta Q_\mu,

where :math:`\alpha` and :math:`\beta` contain at most the remaining :math:`m - 1` square roots. Applying the same rationalization successively to each of the remaining square roots :math:`Q_{m-1}, Q_{m-2}, \dots, Q_1`, we bring :math:`x` into a **normal form**: an integral linear combination of products of the :math:`m` independent square roots :math:`Q_1, \dots, Q_m` with rational coefficients:

.. math::

   x = A_0 + \sum_{i} A_i Q_i + \sum_{i < j} A_{ij} Q_i Q_j + \dots + A_{12\dots m} Q_1 Q_2 \cdots Q_m.

§§ 7–8. Conjugate Values
------------------------

**7.** Every square root :math:`Q_k = \sqrt{E_k}` is by nature two-valued, admitting the two opposite signs :math:`+Q_k` and :math:`-Q_k`. If in the normal form of :math:`x` we independently assign either the :math:`+` or the :math:`-` sign to each of the :math:`m` square roots :math:`Q_1, Q_2, \dots, Q_m` (updating any higher-order radicand :math:`E_\ell` whenever a lower-order root inside :math:`E_\ell` changes sign), we obtain in all :math:`2^m` expressions

.. math::

   x_1, \; x_2, \; \dots, \; x_{2^m},

which we call the :math:`2^m` :term:`conjugate values <conjugate-values>` of :math:`x`.

**8.** For instance, if :math:`x` is an expression of order :math:`\mu = 2` depending on two independent square roots :math:`Q_1 = \sqrt{R}` and :math:`Q_2 = \sqrt{p + q\sqrt{R}}` (:math:`m = 3` if :math:`\sqrt{p - q\sqrt{R}}` is independent of :math:`\sqrt{R}` and :math:`\sqrt{p + q\sqrt{R}}`, or :math:`m = 2` when only :math:`\pm\sqrt{p + q\sqrt{R}}` and :math:`\pm\sqrt{p - q\sqrt{R}}` appear), the four branches

.. math::

   +\sqrt{p + q\sqrt{R}}, \quad -\sqrt{p + q\sqrt{R}}, \quad +\sqrt{p - q\sqrt{R}}, \quad -\sqrt{p - q\sqrt{R}}

form a closed system of conjugate values. Note that the :math:`2^m` formal values :math:`x_1, \dots, x_{2^m}` need not all be numerically distinct from one another (for example, in :math:`\sqrt{p + q\sqrt{R}} + \sqrt{p - q\sqrt{R}}`, reversing the sign of :math:`\sqrt{R}` merely interchanges the two summands and reproduces the same value twice).

§ 9. The Corresponding Equation :math:`F(x) = 0`
------------------------------------------------

**9.** Let us now form the polynomial of degree :math:`2^m` whose roots are precisely all :math:`2^m` conjugate values :math:`x_1, x_2, \dots, x_{2^m}`:

.. math::

   F(x) = (x - x_1)(x - x_2)\cdots(x - x_{2^m}) = 0.

When we interchange :math:`+Q_m` and :math:`-Q_m` (one of the radicals of highest order, which therefore enters no other radical), the factors :math:`(x - x_i)` are simply permuted in pairs, leaving the product :math:`F(x)` unaltered; hence only even powers of :math:`Q_m` appear in the expanded coefficients of :math:`F(x)`, so :math:`Q_m` disappears altogether! Repeating the same permutation argument step-by-step down through all radicals of order :math:`\mu`, then :math:`\mu - 1`, down to order :math:`1`, every square root :math:`Q_k` disappears from the coefficients. Consequently:

* :math:`F(x) = 0` **is an algebraic equation of degree** :math:`2^m` **with purely rational coefficients**, satisfied by the constructible expression :math:`x = x_1` and by all its conjugates.

§ 10. Other Rational Equations :math:`f(x) = 0`
-----------------------------------------------

**10.** Suppose that our constructible quantity :math:`x_1` also satisfies *any other* algebraic equation with rational coefficients,

.. math::

   f(x) = x^n + a_1 x^{n-1} + \dots + a_{n-1} x + a_n = 0.

We prove the fundamental theorem: **Every conjugate value** :math:`x_1, x_2, \dots, x_{2^m}` **must likewise satisfy** :math:`f(x) = 0`.

*Proof.* Substitute :math:`x_1 = \alpha + \beta Q_\mu` into :math:`f(x)` and reduce all powers of :math:`Q_\mu` using :math:`Q_\mu^2 = E_{\mu-1}`. Since the coefficients of :math:`f` are rational, the result takes the form

.. math::

   f(x_1) = A + B Q_\mu = 0,

where :math:`A` and :math:`B` contain only the remaining :math:`m - 1` square roots. Now :math:`B` *must* vanish identically (:math:`B = 0`); for if :math:`B \neq 0`, we should obtain :math:`Q_\mu = -A/B`, expressing :math:`Q_\mu` rationally in terms of the remaining :math:`m - 1` square roots—in direct contradiction to our independence hypothesis (§ 4)! From :math:`B = 0` and :math:`A + B Q_\mu = 0`, it follows immediately that :math:`A = 0` as well. Hence

.. math::

   f(\alpha - \beta Q_\mu) = A - B Q_\mu = 0,

so the value obtained by reversing the sign of :math:`Q_\mu` also satisfies :math:`f(x) = 0`. Similarly, :math:`A(\dots) = 0` and :math:`B(\dots) = 0` are rational equations over the lower radicals; repeating the exact same reasoning for each of the remaining square roots :math:`Q_{m-1}, \dots, Q_1` in descending order proves that *all* :math:`2^m` conjugate values :math:`x_1, \dots, x_{2^m}` satisfy :math:`f(x) = 0`.

§§ 11–12. The Irreducible Equation :math:`\varphi(x) = 0`
---------------------------------------------------------

**11.** Among all equations with rational coefficients satisfied by :math:`x_1`, let

.. math::

   \varphi(x) = x^M + c_1 x^{M-1} + \dots + c_M = 0

be an equation of **lowest possible positive degree** :math:`M`. Clearly :math:`\varphi(x)` is **irreducible** over the rational domain (that is, :math:`\varphi(x)` cannot be factored into two polynomials of lower positive degree with rational coefficients); for if :math:`\varphi(x) = \varphi_1(x)\varphi_2(x)`, then :math:`\varphi(x_1) = 0` would imply either :math:`\varphi_1(x_1) = 0` or :math:`\varphi_2(x_1) = 0`, contradicting the minimality of :math:`M`.

**12.** Moreover, **every rational polynomial** :math:`\psi(x)` **vanishing at** :math:`x_1` **is exactly divisible by** :math:`\varphi(x)`, **and** :math:`\varphi(x)` **itself is uniquely determined**. For, dividing :math:`\psi(x)` by :math:`\varphi(x)` via Euclidean polynomial division over the rational domain gives

.. math::

   \psi(x) = q(x)\varphi(x) + r(x),

where :math:`q(x)` and :math:`r(x)` have rational coefficients and either :math:`r(x) \equiv 0` or :math:`\deg r < M`. Evaluating at :math:`x = x_1`, where :math:`\psi(x_1) = 0` and :math:`\varphi(x_1) = 0`, yields :math:`r(x_1) = 0`. If :math:`r(x)` did not vanish identically, :math:`r(x) = 0` would be a rational equation of degree :math:`< M` satisfied by :math:`x_1`, which is impossible. Therefore :math:`r(x) \equiv 0` and :math:`\varphi(x)` divides :math:`\psi(x)`. In particular, :math:`\varphi(x)` has only simple (distinct) roots—since otherwise :math:`\gcd(\varphi, \varphi')` would furnish a rational divisor of smaller degree—and by § 10 its roots are precisely the distinct values among :math:`x_1, \dots, x_{2^m}`.

§§ 13–15. The Degree of the Irreducible Equation a Power of :math:`2`
---------------------------------------------------------------------

**13.** Apply § 12 to the polynomial :math:`F(x)` of degree :math:`2^m` constructed in § 9: since :math:`F(x_1) = 0`, :math:`F(x)` is divisible by :math:`\varphi(x)`, so that

.. math::

   F(x) = \varphi(x) \cdot F_1(x),

where :math:`F_1(x)` again has rational coefficients and its roots (if :math:`\deg F_1 > 0`) are remaining conjugates :math:`x_k` from :math:`x_1, \dots, x_{2^m}`. Since any such conjugate :math:`x_k` satisfies :math:`F_1(x_k) = 0`, our theorem of §§ 10–12 (applied starting from :math:`x_k`) shows that :math:`F_1(x)` vanishes at :math:`x_1` as well and is therefore again divisible by :math:`\varphi(x)`: :math:`F_1(x) = \varphi(x) \cdot F_2(x)`. Continuing until the quotient reduces to the constant :math:`1`, we find that :math:`F(x)` is an exact integral power of the irreducible polynomial :math:`\varphi(x)`:

.. math::

   F(x) = [\varphi(x)]^\nu \qquad (\nu \ge 1),

showing incidentally that each of the :math:`M` distinct roots of :math:`\varphi(x) = 0` occurs precisely the same number :math:`\nu` of times among the :math:`2^m` formal branches :math:`x_1, \dots, x_{2^m}`.

**14.** Equating degrees on both sides of :math:`F(x) = [\varphi(x)]^\nu` yields

.. math::

   2^m = M \cdot \nu.

Since every divisor of a power of :math:`2` is itself a power of :math:`2`, both :math:`\nu` and :math:`M` must be powers of :math:`2`:

.. math::

   M = 2^h \qquad (h \ge 0).

We have thus established our decisive algebraic necessity theorem:

.. admonition:: Theorem (Degree of a Constructible Algebraic Quantity)

   **Every algebraic quantity** :math:`x` **constructible with straightedge and compasses satisfies an irreducible equation** :math:`\varphi(x) = 0` **over the domain of rationality whose degree** :math:`M` **is a power of** :math:`2` (:math:`M = 2^h`).

**15.** Taking the contrapositive, we obtain our fundamental **Impossibility Criterion**:

   *If an irreducible algebraic equation* :math:`\varphi(x) = 0` *is NOT of degree* :math:`2^h`, *then it CANNOT be solved by a finite number of square roots, and its roots CANNOT be constructed with straightedge and compasses*.

One must carefully guard against assuming the converse of § 14 without qualification: **not every irreducible equation of degree** :math:`2^h` **is solvable by square roots**! Already for :math:`h = 2` (:math:`M = 4`), the general irreducible quartic equation cannot be solved by square roots alone, because its classical resolution (Lagrange, Ferrari) depends upon a *cubic resolvent* of degree :math:`3`, which introduces cube roots unless that resolvent happens to be reducible over the rational domain (restricting the Galois group of the quartic to a subgroup of order :math:`2^\alpha`, rather than all :math:`24 = 4!` permutations). In cyclotomy (:ref:`Chapters III–IV <fp-part1-ch3-cyclotomy-en>`), however, :person:`Gauss <gauss>` proved that the abelian symmetry of the roots guarantees that degree :math:`2^h` *is* also sufficient!
