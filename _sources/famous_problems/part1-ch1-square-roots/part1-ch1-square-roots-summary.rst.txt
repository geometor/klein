:title: Part I, Ch. I: Square-Root Equations — Analytical Summary
:layout: book

.. _fp-part1-ch1-square-roots-summary:

Part I, Chapter I — Analytical Summary
======================================

.. rubric:: Step-by-Step Logical Architecture of Klein's Degree-$2^h$ Theorem (§§ 1–15)

Logical Chain of Proof
----------------------

Without invoking abstract Galois group machinery prematurely, :person:`Klein <klein>` proves :person:`Wantzel's <wantzel>` (:cite:`1837 <wantzel:1837>`) theorem entirely by elementary polynomial algebra over a :term:`domain of rationality <domain-of-rationality>` $K_0$:

1. **Radical Order & Algebraic Independence (§§ 1–4):**
   Every constructible quantity $x$ has a finite :term:`radical order <radical-order>` $\mu$ and depends on $m$ square roots $Q_1, \dots, Q_m$, pruned from the bottom up so that no $Q_k$ is a rational function of the remaining $m - 1$ radicals over $K_0$.
2. **Rationalized Normal Form (§§ 5–6):**
   Successive conjugation $(c - d Q_k)$ eliminates every $Q_k$ from denominators ($c + d Q_k \neq 0$ by independence), expressing $x = \alpha + \beta Q_\mu$ and ultimately expanding $x$ as a $K_0$-linear combination of multilinear products $Q_{i_1}\cdots Q_{i_r}$.
3. **The $2^m$ Conjugate Branches & $F(x) = 0$ (§§ 7–9):**
   Flipping $\pm Q_k$ across all $m$ independent square roots yields $2^m$ formal :term:`conjugate values <conjugate-values>` $x_1, \dots, x_{2^m}$. Because flipping each highest-order radical permutes the linear factors $(x - x_i)$, the symmetric product $F(x) = \prod_{i=1}^{2^m} (x - x_i)$ has coefficients in $K_0$ and degree $2^m$.
4. **Conjugate Propagation Under Any Rational Polynomial (§ 10):**
   If $f(x) \in K_0[x]$ satisfies $f(x_1) = 0$, writing $f(\alpha + \beta Q_\mu) = A + B Q_\mu = 0$ forces $B = 0$ (otherwise $Q_\mu = -A/B$ violates § 4) and hence $A = 0$, so $f(\alpha - \beta Q_\mu) = A - B Q_\mu = 0$. Descending through all $m$ radicals proves $f(x_i) = 0$ for all $i = 1, \dots, 2^m$.
5. **Irreducible Minimal Polynomial & Power Factorization (§§ 11–14):**
   The monic minimal polynomial $\varphi(x) \in K_0[x]$ of $x_1$ divides every polynomial vanishing at $x_1$. Repeatedly dividing $F(x)$ by $\varphi(x)$ yields $F(x) = [\varphi(x)]^\nu$, whence $2^m = \deg(\varphi)\cdot\nu$ and $\deg(\varphi) = 2^h$.
6. **Contrapositive Obstruction & Galois Sufficiency Caveat (§ 15):**
   Any problem whose irreducible polynomial has degree $M \neq 2^h$ is **impossible** with straightedge and compasses. Conversely, $M = 2^h$ is necessary *but not sufficient* in general (e.g., an $S_4$ or $A_4$ quartic of degree $4 = 2^2$ fails because its cubic resolvent is irreducible).
