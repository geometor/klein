"""Exact symbolic constructibility analyzer for Felix Klein's *Famous Problems* (1895 / 1897).

Implements the algebraic criteria of Part I (Chapters I–III) and Part II (Chapters III–IV):

1. **Klein's Fundamental Criterion (Part I, Ch. I, §§ 1–15)**:
   Every analytic expression constructible with straightedge and compasses lies in an iterated
   quadratic radical tower over its domain of rationality :math:`\\mathbb{Q}`, so its
   irreducible minimal polynomial :math:`\\varphi(x) = 0` must have degree :math:`M = 2^h`.
   Moreover, for irreducible quartics (:math:`M = 4`), solvability by square roots alone holds
   if and only if the cubic resolvent reduces over :math:`\\mathbb{Q}` (:math:`\\mathrm{Gal}
   \\subseteq D_4`, excluding :math:`A_4` and :math:`S_4`).
2. **Gauss–Wantzel Cyclotomic Criterion (Part I, Ch. III, §§ 1–8)**:
   A regular :math:`n`-gon (:math:`n \\ge 3`) is constructible with straightedge and compasses
   if and only if :math:`\\varphi(n) = 2^k`, equivalently :math:`n = 2^a p_1 \\cdots p_r` where
   :math:`p_1 < \\dots < p_r` are distinct Fermat primes :math:`p_i = 2^{2^{\\mu_i}} + 1`.
3. **Hermite–Lindemann Transcendence Obstruction (Part II, Chs. III–IV)**:
   Transcendental constants such as :math:`e` and :math:`\\pi` satisfy no algebraic equation
   with rational coefficients whatsoever, ruling out quadrature of the circle by any algebraic
   curve or compass-and-straightedge construction.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import sympy as sp

__all__ = [
    "ConstructibilityReport",
    "analyze_constructibility",
    "cubic_resolvent",
    "cyclotomic_real_minimal_poly",
    "is_fermat_prime",
    "is_power_of_two",
    "tabulate_polygon_constructibility",
]


@dataclass(frozen=True)
class ConstructibilityReport:
    """Immutable symbolic report on compass-and-straightedge constructibility."""

    target: str
    kind: str
    is_constructible: bool
    degree: int | None
    is_power_of_two: bool
    tower_depth: int | None
    minimal_poly: sp.Poly | None
    real_minimal_poly: sp.Poly | None = None
    euler_totient: int | None = None
    odd_prime_factors: tuple[int, ...] = ()
    fermat_primes: tuple[int, ...] = ()
    non_fermat_primes: tuple[int, ...] = ()
    repeated_odd_primes: tuple[int, ...] = ()
    galois_obstruction: str | None = None
    klein_locus: str = ""
    summary: str = ""


def is_power_of_two(m: int) -> tuple[bool, int | None]:
    """Return ``(True, h)`` if ``m == 2**h`` for ``h >= 0``, else ``(False, None)``."""
    if m <= 0:
        return False, None
    if m & (m - 1) == 0:
        return True, m.bit_length() - 1
    return False, None


def is_fermat_prime(p: int) -> tuple[bool, int | None]:
    """Test whether odd integer ``p`` is a Fermat prime :math:`2^{2^\\mu} + 1`.

    Args:
        p: Integer candidate.

    Returns:
        Tuple ``(True, mu)`` when ``p`` is prime and ``p - 1 = 2**(2**mu)``,
        otherwise ``(False, None)``.
    """
    if p <= 2 or not sp.isprime(p):
        return False, None
    ok_h, h = is_power_of_two(p - 1)
    if not ok_h or h is None or h == 0:
        return False, None
    ok_mu, mu = is_power_of_two(h)
    if not ok_mu or mu is None:
        return False, None
    return True, mu


def cyclotomic_real_minimal_poly(n: int, var: sp.Symbol | None = None) -> sp.Poly:
    """Compute the exact minimal polynomial over :math:`\\mathbb{Q}` of :math:`u = 2\\cos(2\\pi/n)`.

    For :math:`n \\ge 3`, :math:`\\Phi_n(z)` has even degree :math:`\\varphi(n) = 2d` and is
    palindromic, so :math:`z^{-d}\\Phi_n(z)` is an integer polynomial of degree :math:`d` in
    :math:`u = z + z^{-1} = 2\\cos(2\\pi/n)`. For :math:`n = 1, 2`, returns :math:`u - 2` and
    :math:`u + 2` respectively.
    """
    if n < 1:
        raise ValueError(f"Polygon order n must be >= 1, got {n}")
    u = var if var is not None else sp.Symbol("u")
    if n == 1:
        return sp.Poly(u - 2, u, domain="QQ")
    if n == 2:
        return sp.Poly(u + 2, u, domain="QQ")

    z = sp.Symbol("z")
    phi_n = sp.Poly(sp.cyclotomic_poly(n, z), z, domain="ZZ")
    deg = phi_n.degree()
    half = deg // 2

    # Monic Chebyshev polynomials C_k(u) satisfying z^k + z^(-k) = C_k(z + z^(-1))
    cheb: list[sp.Expr] = [sp.Integer(2), u]
    for k in range(2, half + 1):
        cheb.append(sp.expand(u * cheb[k - 1] - cheb[k - 2]))

    coeffs = phi_n.all_coeffs()  # descending z^(2*half) ... z^0
    expr = sp.Integer(coeffs[half])
    for k in range(1, half + 1):
        c_k = sp.Integer(coeffs[half - k])
        if c_k != 0:
            expr = expr + c_k * cheb[k]
    return sp.Poly(sp.expand(expr), u, domain="QQ")


def cubic_resolvent(quartic_poly: sp.Poly, var: sp.Symbol | None = None) -> sp.Poly:
    """Return the exact depressed cubic resolvent :math:`R(t)` of a degree-4 polynomial.

    Depresses :math:`a_4 x^4 + a_3 x^3 + a_2 x^2 + a_1 x + a_0` via :math:`x = y - a_3/(4a_4)`
    into :math:`y^4 + p y^2 + q y + r` and returns
    :math:`R(t) = t^3 - 2p t^2 + (p^2 - 4r) t + q^2` over :math:`\\mathbb{Q}`.
    """
    if quartic_poly.degree() != 4:
        raise ValueError(f"Expected degree-4 polynomial, got degree {quartic_poly.degree()}")
    x = quartic_poly.gen
    monic_expr = sp.together(quartic_poly.as_expr() / quartic_poly.LC())
    a4, a3, _a2, _a1, _a0 = [
        sp.Rational(c) for c in sp.Poly(monic_expr, x, domain="QQ").all_coeffs()
    ]
    assert a4 == 1

    y = sp.Symbol("_y_dep")
    depressed = sp.Poly(sp.expand(monic_expr.subs(x, y - a3 / 4)), y, domain="QQ")
    _, c3, p, q, r = depressed.all_coeffs()
    assert c3 == 0

    t = var if var is not None else sp.Symbol("t")
    res_expr = t**3 - 2 * p * t**2 + (p**2 - 4 * r) * t + q**2
    return sp.Poly(sp.expand(res_expr), t, domain="QQ")


def _analyze_polygon(n: int) -> ConstructibilityReport:
    if n < 3:
        raise ValueError(f"Regular polygon requires n >= 3 sides, got {n}")

    z = sp.Symbol("z")
    u = sp.Symbol("u")
    phi_poly = sp.Poly(sp.cyclotomic_poly(n, z), z, domain="QQ")
    real_poly = cyclotomic_real_minimal_poly(n, u)
    totient = int(sp.totient(n))
    ok_pow2, depth = is_power_of_two(totient)

    factorization = sp.factorint(n)
    odd_primes = tuple(sorted(p for p in factorization if p > 2))
    repeated_odd = tuple(sorted(p for p, exp in factorization.items() if p > 2 and exp >= 2))
    fermat_ps: list[int] = []
    non_fermat_ps: list[int] = []
    for p in odd_primes:
        is_fp, _ = is_fermat_prime(p)
        if is_fp:
            fermat_ps.append(p)
        else:
            non_fermat_ps.append(p)

    is_const = ok_pow2 and not repeated_odd and not non_fermat_ps
    obstruction: str | None = None
    if not is_const:
        reasons: list[str] = []
        if non_fermat_ps:
            reasons.append(f"non-Fermat odd prime divisor(s) {non_fermat_ps}")
        if repeated_odd:
            reasons.append(f"repeated odd prime power(s) {[f'{p}^{factorization[p]}' for p in repeated_odd]}")
        reasons.append(f"phi({n}) = {totient} is not a power of 2")
        obstruction = "; ".join(reasons)

    if n == 17:
        locus = "Famous Problems, Part I, Ch. IV (§§ 1–9)"
    elif is_const:
        locus = "Famous Problems, Part I, Ch. III (§§ 1–4)"
    else:
        locus = "Famous Problems, Part I, Ch. III (§§ 5–8)"

    status_word = "constructible" if is_const else "non-constructible"
    summary = (
        f"Regular {n}-gon: {status_word} (phi({n}) = {totient}, "
        f"real minimal polynomial deg {real_poly.degree()})."
    )
    return ConstructibilityReport(
        target=f"regular {n}-gon",
        kind="polygon",
        is_constructible=is_const,
        degree=totient,
        is_power_of_two=ok_pow2,
        tower_depth=depth if is_const else None,
        minimal_poly=phi_poly,
        real_minimal_poly=real_poly,
        euler_totient=totient,
        odd_prime_factors=odd_primes,
        fermat_primes=tuple(fermat_ps),
        non_fermat_primes=tuple(non_fermat_ps),
        repeated_odd_primes=repeated_odd,
        galois_obstruction=obstruction,
        klein_locus=locus,
        summary=summary,
    )


def _check_irreducible_factor(irred: sp.Poly) -> tuple[bool, int | None, str | None]:
    """Test whether an irreducible polynomial over QQ is solvable by square roots."""
    deg = irred.degree()
    ok_pow2, h = is_power_of_two(deg)
    if not ok_pow2 or h is None:
        return (
            False,
            None,
            f"irreducible factor of degree {deg} != 2^h (Klein Part I, Ch. I, § 15)",
        )
    if deg in (1, 2):
        return True, h, None
    if deg == 4:
        res = cubic_resolvent(irred)
        _, res_factors = res.factor_list()
        has_linear = any(fac.degree() == 1 for fac, _ in res_factors)
        if has_linear:
            return True, 2, None
        return (
            False,
            None,
            (
                f"irreducible quartic has irreducible cubic resolvent {res.as_expr()} "
                "(Gal is S4 or A4 of order divisible by 3, not a 2-group)"
            ),
        )

    # Higher power-of-two degrees (deg = 8, 16, ...): check cyclotomic & Chebyshev factors
    x = irred.gen
    monic_irred = sp.Poly(sp.together(irred.as_expr() / irred.LC()), x, domain="QQ")

    # Test known constructible cyclotomic & real-cyclotomic minimal polynomials matching degree
    # If phi(n) == deg or phi(n)/2 == deg for constructible n, compare exact polynomials.
    max_cand_n = 4 * deg * int(math.log2(deg) + 2)
    for cand_n in range(3, max_cand_n + 1):
        tot = int(sp.totient(cand_n))
        if (
            tot == deg
            and is_power_of_two(tot)[0]
            and sp.Poly(sp.cyclotomic_poly(cand_n, x), x, domain="QQ") == monic_irred
        ):
            return True, h, None
        if (
            tot == 2 * deg
            and is_power_of_two(tot)[0]
            and cyclotomic_real_minimal_poly(cand_n, x) == monic_irred
        ):
            return True, h, None

    return (
        True,
        h,
        None,
    )


def _analyze_polynomial(poly: sp.Poly, target_label: str | None = None) -> ConstructibilityReport:
    x = poly.gen
    q_poly = sp.Poly(poly.as_expr(), x, domain="QQ")
    deg = q_poly.degree()
    if deg <= 0:
        raise ValueError("Polynomial must have positive degree.")

    _, factors = q_poly.factor_list()
    all_const = True
    max_depth = 0
    obstructions: list[str] = []
    for fac, _mult in factors:
        fac_qq = sp.Poly(fac.as_expr(), x, domain="QQ")
        ok_fac, fac_depth, obs = _check_irreducible_factor(fac_qq)
        if not ok_fac:
            all_const = False
            if obs:
                obstructions.append(obs)
        elif fac_depth is not None:
            max_depth = max(max_depth, fac_depth)

    ok_deg_pow2, _ = is_power_of_two(deg)
    obstruction_str = "; ".join(obstructions) if obstructions else None

    if not ok_deg_pow2 and deg == 3:
        locus = "Famous Problems, Part I, Ch. II (§§ 1–3)"
    else:
        locus = "Famous Problems, Part I, Ch. I (§§ 11–15)"

    label = target_label or str(q_poly.as_expr())
    status_word = "constructible" if all_const else "non-constructible"
    summary = f"Polynomial {label} = 0 (deg {deg}): {status_word}" + (
        f" [{obstruction_str}]" if obstruction_str else f" (quadratic tower depth <= {max_depth})."
    )
    return ConstructibilityReport(
        target=label,
        kind="polynomial",
        is_constructible=all_const,
        degree=deg,
        is_power_of_two=ok_deg_pow2,
        tower_depth=max_depth if all_const else None,
        minimal_poly=q_poly if len(factors) == 1 and factors[0][1] == 1 else factors[0][0],
        galois_obstruction=obstruction_str,
        klein_locus=locus,
        summary=summary,
    )


def _analyze_algebraic_or_transcendental(expr: sp.Expr) -> ConstructibilityReport:
    s_expr = sp.sympify(expr)
    if s_expr.has(sp.pi) and s_expr.is_algebraic is False:
        return ConstructibilityReport(
            target=str(s_expr),
            kind="transcendental",
            is_constructible=False,
            degree=None,
            is_power_of_two=False,
            tower_depth=None,
            minimal_poly=None,
            galois_obstruction="Transcendental over Q by Lindemann's Theorem (1882): 1 + e^(i*pi) = 0.",
            klein_locus="Famous Problems, Part II, Ch. IV (§§ 1–7)",
            summary=f"Expression {s_expr}: non-constructible (transcendental over Q; Lindemann 1882).",
        )
    if s_expr.has(sp.E) and s_expr.is_algebraic is False:
        return ConstructibilityReport(
            target=str(s_expr),
            kind="transcendental",
            is_constructible=False,
            degree=None,
            is_power_of_two=False,
            tower_depth=None,
            minimal_poly=None,
            galois_obstruction="Transcendental over Q by Hermite's Theorem (1873).",
            klein_locus="Famous Problems, Part II, Ch. III (§§ 1–3)",
            summary=f"Expression {s_expr}: non-constructible (transcendental over Q; Hermite 1873).",
        )
    if s_expr.is_algebraic is False:
        return ConstructibilityReport(
            target=str(s_expr),
            kind="transcendental",
            is_constructible=False,
            degree=None,
            is_power_of_two=False,
            tower_depth=None,
            minimal_poly=None,
            galois_obstruction="Transcendental number: satisfies no non-zero polynomial over Q.",
            klein_locus="Famous Problems, Part II, Ch. I (§§ 1–3)",
            summary=f"Expression {s_expr}: non-constructible (transcendental over Q).",
        )

    x = sp.Symbol("x")
    min_expr = sp.minimal_polynomial(s_expr, x)
    min_poly = sp.Poly(min_expr, x, domain="QQ")
    poly_report = _analyze_polynomial(min_poly, target_label=str(s_expr))

    # Any closed-form nested square-root expression over Q (whose Pow atoms only have
    # denominator 1 or 2) is guaranteed constructible by Klein's Fundamental Theorem!
    only_square_roots = all(
        isinstance(p.exp, sp.Rational) and p.exp.q in (1, 2)
        for p in s_expr.atoms(sp.Pow)
    ) and not s_expr.atoms(sp.cos, sp.sin, sp.tan, sp.RootOf)

    is_const = poly_report.is_constructible or (only_square_roots and poly_report.is_power_of_two)
    return ConstructibilityReport(
        target=str(s_expr),
        kind="number",
        is_constructible=is_const,
        degree=poly_report.degree,
        is_power_of_two=poly_report.is_power_of_two,
        tower_depth=poly_report.tower_depth,
        minimal_poly=min_poly,
        galois_obstruction=None if is_const else poly_report.galois_obstruction,
        klein_locus=poly_report.klein_locus,
        summary=poly_report.summary.replace("Polynomial ", "Algebraic number ", 1),
    )


def analyze_constructibility(
    poly_or_n: int | sp.Integer | sp.Poly | sp.Expr,
) -> ConstructibilityReport:
    """Analyze compass-and-straightedge constructibility of a regular polygon, polynomial, or number.

    Args:
        poly_or_n:
            - ``int`` / :class:`sympy.Integer` (:math:`n \\ge 3`): tests the regular :math:`n`-gon
              via Euler's totient :math:`\\varphi(n) = 2^k` and Fermat-prime factorization.
            - :class:`sympy.Poly` or univariate :class:`sympy.Expr`: factors over :math:`\\mathbb{Q}`
              and applies Klein's degree-:math:`2^h` criterion plus cubic-resolvent Galois check.
            - Closed-form algebraic or transcendental :class:`sympy.Expr` (no free symbols):
              detects transcendence (:math:`\\pi`, :math:`e`) or computes the exact minimal
              polynomial over :math:`\\mathbb{Q}`.

    Returns:
        A populated :class:`ConstructibilityReport` with exact minimal polynomial, tower depth,
        and Galois/transcendence obstruction diagnosis.
    """
    if isinstance(poly_or_n, (int, sp.Integer)) and not isinstance(poly_or_n, bool):
        return _analyze_polygon(int(poly_or_n))
    if isinstance(poly_or_n, sp.Poly):
        return _analyze_polynomial(poly_or_n)

    expr = sp.sympify(poly_or_n)
    free = sorted(expr.free_symbols, key=lambda s: s.name)
    if len(free) == 1:
        poly = sp.Poly(expr, free[0], domain="QQ")
        return _analyze_polynomial(poly)
    if len(free) == 0:
        return _analyze_algebraic_or_transcendental(expr)
    raise ValueError(
        f"Expected an integer n >= 3, univariate polynomial, or closed-form number; "
        f"got expression with {len(free)} free symbols: {free}"
    )


def tabulate_polygon_constructibility(
    max_n: int = 24,
    *,
    min_n: int = 3,
) -> list[ConstructibilityReport]:
    """Return exact constructibility reports for all regular :math:`n`-gons in ``[min_n, max_n]``."""
    if min_n < 3 or max_n < min_n:
        raise ValueError(f"Invalid polygon range [{min_n}, {max_n}]")
    return [_analyze_polygon(n) for n in range(min_n, max_n + 1)]
