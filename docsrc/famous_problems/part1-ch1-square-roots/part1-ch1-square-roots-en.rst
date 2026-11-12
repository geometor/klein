:title: Part I, Ch. I: Algebraic Equations Solvable by Square Roots (1897 English)
:layout: book

.. _fp-part1-ch1-square-roots-en:

Part I, Chapter I — Algebraic Equations Solvable by Square Roots
================================================================

.. rubric:: Part I: The Possibility of the Construction of Algebraic Expressions — Chapter I (§§ 1–15; :cite:`Ginn & Co., 1897, pp. 5–12 <klein:1897>`)

§§ 1–4. Structure of the Expression $x$ to be Constructed
---------------------------------------------------------

**1.** Consider an algebraic expression $x$ capable of being constructed with straightedge and compasses from given segments. By our fundamental theorem (:ref:`Introduction <fp-intro-en>`), $x$ is derived from known quantities—which, upon choosing a unit segment, we may treat as rational numbers (or rational parameters defining a :term:`domain of rationality <domain-of-rationality>`)—by a finite number of rational operations and extractions of square roots.

**2.** In order to classify the complexity of such radical expressions, we assign to every square-root expression a definite :term:`order <radical-order>` $\mu$ according to the depth of superimposed radical signs:

* A purely rational quantity $R$ (involving no square roots) is said to be of **order $0$**.
* An expression formed rationally from rational quantities and simple square roots $\sqrt{R_1}, \sqrt{R_2}, \dots$ (where $R_1, R_2, \dots$ are rational) is of **order $1$**; for example,

  .. math::

     \frac{\alpha + \beta \sqrt{R_1} + \gamma \sqrt{R_2}}{\delta + \varepsilon \sqrt{R_3}}.

* An expression formed rationally from quantities of order $\le 1$ and square roots of expressions of order $1$, such as $\sqrt{p + q\sqrt{R_1}}$, is of **order $2$**.
* In general, an expression $x$ is of **order $\mu$** if the deepest chain of nested square roots occurring within $x$ superimposes $\mu$ radical signs, so that every square root of order $\mu$ extracts the root of an expression of order $\mu - 1$.

**3.** Suppose that throughout the entire construction of $x$ there occur in all $m$ distinct square roots $Q_1, Q_2, \dots, Q_m$, arranged in non-decreasing order of their radical depth ($1 \le \text{ord}(Q_j) \le \mu$).

**4.** Before proceeding further, we stipulate that **none of the $m$ square roots $Q_1, \dots, Q_m$ can be expressed rationally in terms of the remaining square roots and known rational quantities**. For if any radical $Q_k$ were equal to a rational function of the previous radicals $Q_1, \dots, Q_{k-1}$, we should simply replace $Q_k$ everywhere by that rational expression and thereby reduce the total number $m$ of independent square roots by one. By repeating such reductions from the lowest order upward, we ensure that the $m$ square roots $Q_1, \dots, Q_m$ are algebraically independent over the preceding stages.

§§ 5–6. Normal Form of $x$
--------------------------

**5.** Let $Q_\mu$ denote one particular square root among those of highest order $\mu$ appearing in $x$. As a function of $Q_\mu$ alone, $x$ is a rational quotient whose numerator and denominator are polynomials in $Q_\mu$ with coefficients involving only the remaining $m - 1$ square roots. Since $Q_\mu^2$ is an expression of order $\mu - 1$, every even power $Q_\mu^{2k}$ reduces to lower-order radicals, and every odd power $Q_\mu^{2k+1}$ reduces to $Q_\mu$ multiplied by lower-order radicals. Thus $x$ assumes the fractional linear form

.. math::

   x = \frac{a + b Q_\mu}{c + d Q_\mu},

where $a, b, c, d$ do not contain $Q_\mu$.

**6.** Multiplying numerator and denominator by the conjugate factor $c - d Q_\mu$ (note that $c + d Q_\mu \neq 0$, since otherwise $Q_\mu = -c/d$ would be rationally expressible through the remaining radicals, contrary to § 4), we clear $Q_\mu$ from the denominator:

.. math::

   x = \frac{(a + b Q_\mu)(c - d Q_\mu)}{c^2 - d^2 Q_\mu^2} = \alpha + \beta Q_\mu,

where $\alpha$ and $\beta$ contain at most the remaining $m - 1$ square roots. Applying the same rationalization successively to each of the remaining square roots $Q_{m-1}, Q_{m-2}, \dots, Q_1$, we bring $x$ into a **normal form**: an integral linear combination of products of the $m$ independent square roots $Q_1, \dots, Q_m$ with rational coefficients:

.. math::

   x = A_0 + \sum_{i} A_i Q_i + \sum_{i < j} A_{ij} Q_i Q_j + \dots + A_{12\dots m} Q_1 Q_2 \cdots Q_m.

§§ 7–8. Conjugate Values
------------------------

**7.** Every square root $Q_k = \sqrt{E_k}$ is by nature two-valued, admitting the two opposite signs $+Q_k$ and $-Q_k$. If in the normal form of $x$ we independently assign either the $+$ or the $-$ sign to each of the $m$ square roots $Q_1, Q_2, \dots, Q_m$ (updating any higher-order radicand $E_\ell$ whenever a lower-order root inside $E_\ell$ changes sign), we obtain in all $2^m$ expressions

.. math::

   x_1, \; x_2, \; \dots, \; x_{2^m},

which we call the **$2^m$** :term:`conjugate values <conjugate-values>` of $x$.

**8.** For instance, if $x$ is an expression of order $\mu = 2$ depending on two independent square roots $Q_1 = \sqrt{R}$ and $Q_2 = \sqrt{p + q\sqrt{R}}$ ($m = 3$ if $\sqrt{p - q\sqrt{R}}$ is independent of $\sqrt{R}$ and $\sqrt{p + q\sqrt{R}}$, or $m = 2$ when only $\pm\sqrt{p + q\sqrt{R}}$ and $\pm\sqrt{p - q\sqrt{R}}$ appear), the four branches

.. math::

   +\sqrt{p + q\sqrt{R}}, \quad -\sqrt{p + q\sqrt{R}}, \quad +\sqrt{p - q\sqrt{R}}, \quad -\sqrt{p - q\sqrt{R}}

form a closed system of conjugate values. Note that the $2^m$ formal values $x_1, \dots, x_{2^m}$ need not all be numerically distinct from one another (for example, in $\sqrt{p + q\sqrt{R}} + \sqrt{p - q\sqrt{R}}$, reversing the sign of $\sqrt{R}$ merely interchanges the two summands and reproduces the same value twice).

§ 9. The Corresponding Equation $F(x) = 0$
------------------------------------------

**9.** Let us now form the polynomial of degree $2^m$ whose roots are precisely all $2^m$ conjugate values $x_1, x_2, \dots, x_{2^m}$:

.. math::

   F(x) = (x - x_1)(x - x_2)\cdots(x - x_{2^m}) = 0.

When we interchange $+Q_m$ and $-Q_m$ (one of the radicals of highest order, which therefore enters no other radical), the factors $(x - x_i)$ are simply permuted in pairs, leaving the product $F(x)$ unaltered; hence only even powers of $Q_m$ appear in the expanded coefficients of $F(x)$, so $Q_m$ disappears altogether! Repeating the same permutation argument step-by-step down through all radicals of order $\mu$, then $\mu - 1$, down to order $1$, every square root $Q_k$ disappears from the coefficients. Consequently:

* **$F(x) = 0$ is an algebraic equation of degree $2^m$ with purely rational coefficients**, satisfied by the constructible expression $x = x_1$ and by all its conjugates.

§ 10. Other Rational Equations $f(x) = 0$
-----------------------------------------

**10.** Suppose that our constructible quantity $x_1$ also satisfies *any other* algebraic equation with rational coefficients,

.. math::

   f(x) = x^n + a_1 x^{n-1} + \dots + a_{n-1} x + a_n = 0.

We prove the fundamental theorem: **Every conjugate value $x_1, x_2, \dots, x_{2^m}$ must likewise satisfy $f(x) = 0$.**

*Proof.* Substitute $x_1 = \alpha + \beta Q_\mu$ into $f(x)$ and reduce all powers of $Q_\mu$ using $Q_\mu^2 = E_{\mu-1}$. Since the coefficients of $f$ are rational, the result takes the form

.. math::

   f(x_1) = A + B Q_\mu = 0,

where $A$ and $B$ contain only the remaining $m - 1$ square roots. Now $B$ *must* vanish identically ($B = 0$); for if $B \neq 0$, we should obtain $Q_\mu = -A/B$, expressing $Q_\mu$ rationally in terms of the remaining $m - 1$ square roots—in direct contradiction to our independence hypothesis (§ 4)! From $B = 0$ and $A + B Q_\mu = 0$, it follows immediately that $A = 0$ as well. Hence

.. math::

   f(\alpha - \beta Q_\mu) = A - B Q_\mu = 0,

so the value obtained by reversing the sign of $Q_\mu$ also satisfies $f(x) = 0$. Similarly, $A(\dots) = 0$ and $B(\dots) = 0$ are rational equations over the lower radicals; repeating the exact same reasoning for each of the remaining square roots $Q_{m-1}, \dots, Q_1$ in descending order proves that *all* $2^m$ conjugate values $x_1, \dots, x_{2^m}$ satisfy $f(x) = 0$.

§§ 11–12. The Irreducible Equation $\varphi(x) = 0$
---------------------------------------------------

**11.** Among all equations with rational coefficients satisfied by $x_1$, let

.. math::

   \varphi(x) = x^M + c_1 x^{M-1} + \dots + c_M = 0

be an equation of **lowest possible positive degree $M$**. Clearly $\varphi(x)$ is **irreducible** over the rational domain (that is, $\varphi(x)$ cannot be factored into two polynomials of lower positive degree with rational coefficients); for if $\varphi(x) = \varphi_1(x)\varphi_2(x)$, then $\varphi(x_1) = 0$ would imply either $\varphi_1(x_1) = 0$ or $\varphi_2(x_1) = 0$, contradicting the minimality of $M$.

**12.** Moreover, **every rational polynomial $\psi(x)$ vanishing at $x_1$ is exactly divisible by $\varphi(x)$, and $\varphi(x)$ itself is uniquely determined**. For, dividing $\psi(x)$ by $\varphi(x)$ via Euclidean polynomial division over the rational domain gives

.. math::

   \psi(x) = q(x)\varphi(x) + r(x),

where $q(x)$ and $r(x)$ have rational coefficients and either $r(x) \equiv 0$ or $\deg r < M$. Evaluating at $x = x_1$, where $\psi(x_1) = 0$ and $\varphi(x_1) = 0$, yields $r(x_1) = 0$. If $r(x)$ did not vanish identically, $r(x) = 0$ would be a rational equation of degree $< M$ satisfied by $x_1$, which is impossible. Therefore $r(x) \equiv 0$ and $\varphi(x)$ divides $\psi(x)$. In particular, $\varphi(x)$ has only simple (distinct) roots—since otherwise $\gcd(\varphi, \varphi')$ would furnish a rational divisor of smaller degree—and by § 10 its roots are precisely the distinct values among $x_1, \dots, x_{2^m}$.

§§ 13–15. The Degree of the Irreducible Equation a Power of $2$
---------------------------------------------------------------

**13.** Apply § 12 to the polynomial $F(x)$ of degree $2^m$ constructed in § 9: since $F(x_1) = 0$, $F(x)$ is divisible by $\varphi(x)$, so that

.. math::

   F(x) = \varphi(x) \cdot F_1(x),

where $F_1(x)$ again has rational coefficients and its roots (if $\deg F_1 > 0$) are remaining conjugates $x_k$ from $x_1, \dots, x_{2^m}$. Since any such conjugate $x_k$ satisfies $F_1(x_k) = 0$, our theorem of §§ 10–12 (applied starting from $x_k$) shows that $F_1(x)$ vanishes at $x_1$ as well and is therefore again divisible by $\varphi(x)$: $F_1(x) = \varphi(x) \cdot F_2(x)$. Continuing until the quotient reduces to the constant $1$, we find that $F(x)$ is an exact integral power of the irreducible polynomial $\varphi(x)$:

.. math::

   F(x) = [\varphi(x)]^\nu \qquad (\nu \ge 1),

showing incidentally that each of the $M$ distinct roots of $\varphi(x) = 0$ occurs precisely the same number $\nu$ of times among the $2^m$ formal branches $x_1, \dots, x_{2^m}$.

**14.** Equating degrees on both sides of $F(x) = [\varphi(x)]^\nu$ yields

.. math::

   2^m = M \cdot \nu.

Since every divisor of a power of $2$ is itself a power of $2$, both $\nu$ and $M$ must be powers of $2$:

.. math::

   M = 2^h \qquad (h \ge 0).

We have thus established our decisive algebraic necessity theorem:

.. admonition:: Theorem (Degree of a Constructible Algebraic Quantity)

   **Every algebraic quantity $x$ constructible with straightedge and compasses satisfies an irreducible equation $\varphi(x) = 0$ over the domain of rationality whose degree $M$ is a power of $2$ ($M = 2^h$).**

**15.** Taking the contrapositive, we obtain our fundamental **Impossibility Criterion**:

   *If an irreducible algebraic equation $\varphi(x) = 0$ is NOT of degree $2^h$, then it CANNOT be solved by a finite number of square roots, and its roots CANNOT be constructed with straightedge and compasses.*

One must carefully guard against assuming the converse of § 14 without qualification: **not every irreducible equation of degree $2^h$ is solvable by square roots!** Already for $h = 2$ ($M = 4$), the general irreducible quartic equation cannot be solved by square roots alone, because its classical resolution (Lagrange, Ferrari) depends upon a *cubic resolvent* of degree $3$, which introduces cube roots unless that resolvent happens to be reducible over the rational domain (restricting the Galois group of the quartic to a subgroup of order $2^\alpha$, rather than all $24 = 4!$ permutations). In cyclotomy (:ref:`Chapters III–IV <fp-part1-ch3-cyclotomy-en>`), however, :person:`Gauss <gauss>` proved that the abelian symmetry of the roots guarantees that degree $2^h$ *is* also sufficient!
