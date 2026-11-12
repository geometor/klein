"""Exact Gaussian period tower and von Staudt–Schröter–Klein construction of the regular 17-gon.

Implements Felix Klein's *Famous Problems of Elementary Geometry*, Part I, Chapter IV (§§ 1–9,
EN pp. 24–41 / DE S. 19–32):

1. **Gaussian Period Quadratic Tower (§§ 1–6)**:
   Using the primitive root :math:`g = 3 \\pmod{17}`, partitions the 16 primitive 17th roots of
   unity into:

   - Two 8-periods :math:`x_1, x_2` (DE: :math:`\\eta_0, \\eta_1`) solving
     :math:`(\\xi): x^2 + x - 4 = 0`;
   - Four 4-periods :math:`y_1, y_2` (DE: :math:`\\eta'_0, \\eta'_1`) solving
     :math:`(\\eta): y^2 - x_1 y - 1 = 0`, and :math:`y_4, y_3` (DE: :math:`(\\eta'_0), (\\eta'_1)`)
     solving :math:`(\\eta'): y^2 - x_2 y - 1 = 0`, satisfying Klein's inequality chain
     :math:`y_3 < y_2 < y_4 < y_1` and radical-dependence identity
     :math:`\\sqrt{x_1^2 + 4}\\,\\sqrt{x_2^2 + 4} = 2\\sqrt{17}`;
   - Eight real 2-periods :math:`z_1, \\dots, z_8` (:math:`z_1 = 2\\cos(2\\pi/17)`) with
     :math:`z_1, z_2` solving :math:`(\\zeta): z^2 - y_1 z + y_4 = 0`.

2. **Poncelet–Steiner Single-Circle Construction (von Staudt 1842 / Schröter 1872 / Klein §§ 8–9)**:
   Solves all four quadratic equations :math:`(\\xi), (\\eta), (\\eta'), (\\zeta)` geometrically inside
   :class:`geometor.model.Model` (``auto_intersect=False``) using **only straightedge lines and a
   single fixed circle** :math:`C_0: x^2 + y(y - 2) = 0`, then inscribes all **17 exact regular
   heptadecagon vertices** ``V0``..``V16`` on :math:`C_0` via Steiner straightedge parallels—using
   ``len(model.circles) == 1`` and **zero** ``float`` / ``sp.Float`` coordinates!
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction

import mpmath as mp
import sympy as sp
import sympy.geometry as spg
from geometor.model import Model
from sympy.polys.polytools import Poly, gcdex, rem

__all__ = [
    "A_MINUS",
    "A_PLUS",
    "B8_EXPRS",
    "PRIMITIVE_ROOT_3_CYCLE",
    "R1",
    "R2",
    "R3",
    "R4",
    "SQRT17",
    "Gauss17GonPeriods",
    "canonicalize_17",
    "construct_gauss_17gon_periods",
]

# Primitive root g = 3 (mod 17): 3^1, 3^2, ..., 3^16 (Klein Part I, Ch. IV, § 2, p. 25 / S. 20)
PRIMITIVE_ROOT_3_CYCLE: tuple[int, ...] = (
    3,
    9,
    10,
    13,
    5,
    15,
    11,
    16,
    14,
    8,
    7,
    4,
    12,
    2,
    6,
    1,
)

# --- Exact 4-Level Gaussian Radical Basis for K_8 = Q(cos(2*pi/17)) ---
SQRT17: sp.Expr = sp.sqrt(17)
A_MINUS: sp.Expr = sp.sqrt(34 - 2 * SQRT17)
A_PLUS: sp.Expr = sp.sqrt(34 + 2 * SQRT17)

R1: sp.Expr = sp.sqrt(17 + 3 * SQRT17 - A_MINUS - 2 * A_PLUS)
R2: sp.Expr = sp.sqrt(17 + 3 * SQRT17 + A_MINUS + 2 * A_PLUS)
R3: sp.Expr = sp.sqrt(17 - 3 * SQRT17 + 2 * A_MINUS - A_PLUS)
R4: sp.Expr = sp.sqrt(17 - 3 * SQRT17 - 2 * A_MINUS + A_PLUS)

B8_EXPRS: tuple[sp.Expr, ...] = (
    sp.Integer(1),
    SQRT17,
    A_MINUS,
    A_PLUS,
    R1,
    R2,
    R3,
    R4,
)

_t = sp.Symbol("t")
_M8 = Poly(_t**8 - 68 * _t**6 + 1088 * _t**4 - 5440 * _t**2 + 4352, _t, domain="QQ")
_ZERO_P = Poly(0, _t, domain="QQ")
_ONE_P = Poly(1, _t, domain="QQ")

K16Val = tuple[Poly, Poly]  # (a, b) representing a + b * sqrt(W2) in K_16 = K_8(sin(2*pi/17))


class _K16Engine:
    """Exact polynomial-quotient arithmetic engine in K_16 = K_8[sqrt(W2)] over QQ[t]/(M_8(t))."""

    def __init__(self) -> None:
        cols: list[list[sp.Expr]] = []
        self.b8_polys: list[Poly] = []
        for expr in B8_EXPRS:
            nf = sp.to_number_field(expr, R1)
            coeffs = nf.coeffs()
            p = Poly(coeffs, _t, domain="QQ")
            self.b8_polys.append(p)
            cols.append([sp.Integer(0)] * (8 - len(coeffs)) + list(coeffs))

        self.m_inv: sp.Matrix = sp.Matrix(cols).T.inv()

        with mp.workdps(85):
            self.roots_mp = [
                mp.mpf(str(r.evalf(85))) for r in sp.nroots(_M8.as_expr(), n=85)
            ]
            v_mp = mp.matrix([[r ** (7 - j) for j in range(8)] for r in self.roots_mp])
            self.v_inv_mp = v_mp ** (-1)

        self.r1_float = float(R1.evalf())
        self.sqrt_cache: dict[tuple[sp.Rational, ...], Poly | None] = {}
        for b_poly in self.b8_polys[1:]:
            sq = self.k8_mul(b_poly, b_poly)
            self.sqrt_cache[tuple(sq.all_coeffs())] = b_poly

        # Canonical W2 in K_8 proportional to sin^2(2*pi/17)
        p_cos1 = (
            -self.b8_polys[0]
            + self.b8_polys[1]
            + self.b8_polys[2]
            + Poly(2, _t, domain="QQ") * self.b8_polys[4]
        ) * Poly(sp.Rational(1, 16), _t, domain="QQ")
        raw_sin2 = _ONE_P - self.k8_mul(p_cos1, p_cos1)
        self.p_w2, _ = self.normalize_radicand(raw_sin2)
        self.p_w2_inv = self.k8_inv(self.p_w2)
        self.w2_expr = self.poly_to_b8_expr(self.p_w2)
        self.sqrt_w2_expr = sp.sqrt(self.w2_expr)

    @staticmethod
    def k8_mul(p1: Poly, p2: Poly) -> Poly:
        if p1.is_zero or p2.is_zero:
            return _ZERO_P
        return rem(p1 * p2, _M8, domain="QQ")

    @staticmethod
    def k8_inv(p: Poly) -> Poly:
        s, _, g = gcdex(p, _M8, domain="QQ")
        if not g.is_ground or g.LC() == 0:
            raise ValueError("Non-invertible element in K_8")
        return Poly(s / g.LC(), _t, domain="QQ")

    def poly_eval_at_r1(self, p: Poly) -> float:
        if p.is_zero:
            return 0.0
        c = p.all_coeffs()
        c_desc = [sp.Integer(0)] * (8 - len(c)) + list(c)
        return sum(float(c_desc[j]) * (self.r1_float ** (7 - j)) for j in range(8))

    def poly_to_b8_coords(self, p: Poly) -> list[sp.Rational]:
        if p.is_zero:
            return [sp.Rational(0)] * 8
        c = p.all_coeffs()
        vec = sp.Matrix([sp.Integer(0)] * (8 - len(c)) + list(c))
        return list(self.m_inv * vec)

    def poly_to_b8_expr(self, p: Poly) -> sp.Expr:
        coords = self.poly_to_b8_coords(p)
        return sum(coords[i] * B8_EXPRS[i] for i in range(8))

    def normalize_radicand(self, p: Poly) -> tuple[Poly, sp.Rational]:
        coords = self.poly_to_b8_coords(p)
        den_lcm = 1
        for q in coords:
            den_lcm = math.lcm(den_lcm, int(q.q))
        mult_d = 1
        for prime, exp in sp.factorint(den_lcm).items():
            if exp % 2 == 1:
                mult_d *= prime
        sq_den = den_lcm * mult_d
        root_den = math.isqrt(sq_den)

        int_nums = [int(q * sq_den) for q in coords]
        num_gcd = 0
        for n in int_nums:
            num_gcd = math.gcd(num_gcd, abs(n))
        root_num = 1
        if num_gcd > 1:
            for prime, exp in sp.factorint(num_gcd).items():
                if exp >= 2:
                    root_num *= prime ** (exp // 2)

        scale = sp.Rational(root_num, root_den)
        inv_scale_sq = Poly(sp.Rational(sq_den, root_num * root_num), _t, domain="QQ")
        return self.k8_mul(p, inv_scale_sq), scale

    def k8_sqrt(self, p: Poly) -> Poly | None:
        if p.is_zero:
            return _ZERO_P
        key = tuple(p.all_coeffs())
        if key in self.sqrt_cache:
            return self.sqrt_cache[key]

        c_desc = [sp.Integer(0)] * (8 - len(p.all_coeffs())) + list(p.all_coeffs())
        scale = 10**50
        with mp.workdps(85):
            c_mp = [mp.mpf(int(c.p)) / mp.mpf(int(c.q)) for c in c_desc]
            vals = []
            for r in self.roots_mp:
                v = sum(c_mp[j] * (r ** (7 - j)) for j in range(8))
                if v < mp.mpf("-1e-55"):
                    self.sqrt_cache[key] = None
                    return None
                vals.append(mp.sqrt(max(v, mp.mpf(0))))

            for mask in range(128):
                signed = [vals[0]] + [
                    (-vals[i + 1] if (mask >> i) & 1 else vals[i + 1])
                    for i in range(7)
                ]
                cand_vec = self.v_inv_mp * mp.matrix(signed)
                rats: list[sp.Rational] = []
                ok = True
                for i in range(8):
                    num = int(mp.nint(cand_vec[i] * scale))
                    frac = Fraction(num, scale).limit_denominator(10**20)
                    err = abs(
                        cand_vec[i]
                        - mp.mpf(frac.numerator) / mp.mpf(frac.denominator)
                    )
                    if err > mp.mpf("1e-30"):
                        ok = False
                        break
                    rats.append(sp.Rational(frac.numerator, frac.denominator))
                if not ok:
                    continue
                q = Poly(rats, _t, domain="QQ")
                if self.k8_mul(q, q) == p:
                    res = q if self.poly_eval_at_r1(q) >= 0 else -q
                    self.sqrt_cache[key] = res
                    return res

        self.sqrt_cache[key] = None
        return None

    def k16_mul(self, u: K16Val, v: K16Val) -> K16Val:
        a1, b1 = u
        a2, b2 = v
        aa = self.k8_mul(a1, a2)
        if b1.is_zero and b2.is_zero:
            return (aa, _ZERO_P)
        ab = self.k8_mul(a1, b2) + self.k8_mul(b1, a2)
        if b1.is_zero or b2.is_zero:
            return (aa, ab)
        bb = self.k8_mul(self.p_w2, self.k8_mul(b1, b2))
        return (aa + bb, ab)

    def k16_inv(self, u: K16Val) -> K16Val:
        a, b = u
        if b.is_zero:
            return (self.k8_inv(a), _ZERO_P)
        norm = self.k8_mul(a, a) - self.k8_mul(self.p_w2, self.k8_mul(b, b))
        inv_n = self.k8_inv(norm)
        return (self.k8_mul(a, inv_n), -self.k8_mul(b, inv_n))

    def k16_pow(self, base: K16Val, n: int) -> K16Val:
        if n == 0:
            return (_ONE_P, _ZERO_P)
        if n < 0:
            return self.k16_pow(self.k16_inv(base), -n)
        res: K16Val = (_ONE_P, _ZERO_P)
        cur = base
        exp = n
        while exp > 0:
            if exp & 1:
                res = self.k16_mul(res, cur)
            exp >>= 1
            if exp > 0:
                cur = self.k16_mul(cur, cur)
        return res

    def k16_sqrt(self, val: K16Val) -> K16Val | None:
        """Return exact positive square root in K_16 = K_8[sqrt(W2)], or None."""
        u0, u1 = val
        if u0.is_zero and u1.is_zero:
            return (_ZERO_P, _ZERO_P)
        if u1.is_zero:
            q_k8 = self.k8_sqrt(u0)
            if q_k8 is not None:
                return (q_k8, _ZERO_P)
            q_w2 = self.k8_sqrt(self.k8_mul(u0, self.p_w2_inv))
            if q_w2 is not None:
                return (_ZERO_P, q_w2)
            return None

        # Denest sqrt(u0 + u1 * sqrt(W2)) in K_16 via norm N = u0^2 - W2 * u1^2 in K_8
        norm_p = self.k8_mul(u0, u0) - self.k8_mul(self.p_w2, self.k8_mul(u1, u1))
        d_p = self.k8_sqrt(norm_p)
        if d_p is None:
            return None
        half_p = Poly(sp.Rational(1, 2), _t, domain="QQ")
        for cand_d in (d_p, -d_p):
            a2_p = self.k8_mul(u0 + cand_d, half_p)
            a_p = self.k8_sqrt(a2_p)
            if a_p is not None and not a_p.is_zero:
                b_p = self.k8_mul(u1, self.k8_inv(Poly(2, _t, domain="QQ") * a_p))
                cand: K16Val = (a_p, b_p)
                if self.k16_mul(cand, cand) == val:
                    num_val = self.poly_eval_at_r1(a_p) + self.poly_eval_at_r1(b_p) * math.sqrt(
                        max(0.0, self.poly_eval_at_r1(self.p_w2))
                    )
                    return cand if num_val >= 0 else (-a_p, -b_p)
        return None

    def eval_expr(self, expr: sp.Expr, *, _expanded: bool = False) -> K16Val | None:
        if isinstance(expr, sp.Rational):
            return (Poly(expr, _t, domain="QQ"), _ZERO_P)
        if isinstance(expr, int):
            return (Poly(sp.Integer(expr), _t, domain="QQ"), _ZERO_P)
        for idx, b_expr in enumerate(B8_EXPRS):
            if expr == b_expr:
                return (self.b8_polys[idx], _ZERO_P)
        if expr == self.sqrt_w2_expr:
            return (_ZERO_P, _ONE_P)
        if expr.is_Add:
            acc: K16Val = (_ZERO_P, _ZERO_P)
            for arg in expr.args:
                ev = self.eval_expr(arg)
                if ev is None:
                    return None
                acc = (acc[0] + ev[0], acc[1] + ev[1])
            return acc
        if expr.is_Mul:
            half_rads: list[sp.Expr] = []
            other_factors: list[sp.Expr] = []
            has_add = False
            for f in expr.args:
                if f.is_Add:
                    has_add = True
                if f.is_Pow and isinstance(f.args[1], sp.Rational) and f.args[1].q == 2:
                    base, exp = f.args
                    k = (int(exp.p) - 1) // 2
                    if k != 0:
                        other_factors.append(base**k)
                    half_rads.append(base)
                else:
                    other_factors.append(f)

            acc_m: K16Val = (_ONE_P, _ZERO_P)
            ok = True
            for f in other_factors:
                ev = self.eval_expr(f)
                if ev is None:
                    ok = False
                    break
                acc_m = self.k16_mul(acc_m, ev)

            if ok and half_rads:
                rad_prod = sp.Mul(*half_rads) if len(half_rads) > 1 else half_rads[0]
                rad_val = self.eval_expr(rad_prod)
                if rad_val is None and len(half_rads) > 1:
                    rad_val = self.eval_expr(sp.expand_mul(rad_prod), _expanded=True)
                if rad_val is not None:
                    sq_val = self.k16_sqrt(rad_val)
                    if sq_val is not None:
                        acc_m = self.k16_mul(acc_m, sq_val)
                    else:
                        ok = False
                else:
                    ok = False

            if ok:
                return acc_m
            if has_add and not _expanded:
                return self.eval_expr(sp.expand_mul(expr), _expanded=True)
            return None
        if expr.is_Pow:
            base_expr, exp_expr = expr.args
            ev_b = self.eval_expr(base_expr)
            if ev_b is None or not isinstance(exp_expr, sp.Rational):
                return None
            p_num, q_den = int(exp_expr.p), int(exp_expr.q)
            if q_den == 1:
                return self.k16_pow(ev_b, p_num)
            if q_den == 2:
                sq = self.k16_sqrt(ev_b)
                if sq is not None:
                    return self.k16_pow(sq, p_num)
        return None

    def to_expr(self, val: K16Val) -> sp.Expr:
        a, b = val
        ea = self.poly_to_b8_expr(a)
        if b.is_zero:
            return ea
        sgn = 1 if self.poly_eval_at_r1(b) >= 0 else -1
        sq_poly = self.k8_mul(self.k8_mul(b, b), self.p_w2)
        u_norm, scale = self.normalize_radicand(sq_poly)
        rad_term = sgn * scale * sp.sqrt(self.poly_to_b8_expr(u_norm))
        return ea + rad_term if not a.is_zero else rad_term


_ENGINE: _K16Engine | None = None


def _get_engine() -> _K16Engine:
    global _ENGINE
    if _ENGINE is None:
        _ENGINE = _K16Engine()
    return _ENGINE


def canonicalize_17(expr: sp.Expr) -> sp.Expr:
    """Canonicalize an exact cyclotomic-17 expression onto Gauss's radical basis in :math:`K_{16}`."""
    s_expr = sp.sympify(expr)
    if isinstance(s_expr, sp.Rational):
        return s_expr
    eng = _get_engine()
    val = eng.eval_expr(s_expr)
    if val is not None:
        return eng.to_expr(val)
    return sp.simplify(s_expr)


@dataclass(frozen=True)
class Gauss17GonPeriods:
    """Exact algebraic and geometric realization of Gauss's and Klein's regular 17-gon."""

    primitive_root: int
    exponent_cycle: tuple[int, ...]
    x1: sp.Expr
    x2: sp.Expr
    y1: sp.Expr
    y2: sp.Expr
    y3: sp.Expr
    y4: sp.Expr
    z_periods: tuple[sp.Expr, ...]
    cos_2pi_17: sp.Expr
    sin_2pi_17: sp.Expr
    eq_xi: sp.Poly
    eq_eta: sp.Poly
    eq_eta_prime: sp.Poly
    eq_zeta: sp.Poly
    radical_dependence_residual: sp.Expr
    model: Model
    fixed_circle: spg.Circle
    milestones: dict[str, spg.Point]
    vertices: tuple[spg.Point, ...]


def _compute_all_z_periods() -> tuple[sp.Expr, ...]:
    """Compute all 8 exact real 2-periods z_1 .. z_8 = 2*cos(2*pi*k/17) in K_8."""
    # In Klein Part I, Ch. IV, §§ 2–3 (EN p. 26 / DE S. 20):
    # z_1 = eps^1 + eps^16 = 2*cos(2*pi/17)
    # z_2 = eps^4 + eps^13 = 2*cos(8*pi/17)
    # z_3 = eps^2 + eps^15 = 2*cos(4*pi/17)
    # z_4 = eps^8 + eps^9  = 2*cos(16*pi/17)
    # z_5 = eps^5 + eps^12 = 2*cos(10*pi/17)
    # z_6 = eps^7 + eps^10 = 2*cos(14*pi/17)
    # z_7 = eps^6 + eps^11 = 2*cos(12*pi/17)
    # z_8 = eps^3 + eps^14 = 2*cos(6*pi/17)
    z1 = sp.Rational(1, 8) * (-1 + SQRT17 + A_MINUS + 2 * R1)

    # Monic Chebyshev polynomials C_k(z1) = 2*cos(2*k*pi/17) in K_8
    cheb: dict[int, sp.Expr] = {0: sp.Integer(2), 1: z1}
    for k in range(2, 9):
        cheb[k] = canonicalize_17(z1 * cheb[k - 1] - cheb[k - 2])

    klein_indices = (1, 4, 2, 8, 5, 7, 6, 3)
    return tuple(cheb[m] for m in klein_indices)


def construct_gauss_17gon_periods(
    model: Model | None = None,
    *,
    inscribe_polygon: bool = True,
    add_sides: bool = True,
) -> Gauss17GonPeriods:
    """Construct Gauss's 17-gon period tower and Klein's von Staudt–Schröter single-circle 17-gon.

    Solves all four quadratic period equations :math:`(\\xi), (\\eta), (\\eta'), (\\zeta)` on the
    single fixed circle :math:`C_0: x^2 + y(y - 2) = 0` (center ``C0c(0, 1)``, bottom ``O(0, 0)``,
    top ``A(0, 2)``) using **straightedge lines alone**, and (when ``inscribe_polygon=True``)
    inscribes all 17 exact regular heptadecagon vertices ``V0``..``V16`` on :math:`C_0` via
    Steiner's straightedge parallel theorem—keeping ``len(model.circles) == 1`` and ``0`` floats!

    Args:
        model: Optional existing :class:`~geometor.model.Model` (must have ``auto_intersect=False``
            or will be configured with ``canonicalize_17``). When ``None``, creates a fresh
            ``Model("klein_von_staudt_17gon", logger=False, auto_intersect=False)``.
        inscribe_polygon: If ``True`` (default), construct all 17 exact vertices ``V0``..``V16``.
        add_sides: If ``True`` (default) and ``inscribe_polygon=True``, add the 17 polygon sides.

    Returns:
        A frozen :class:`Gauss17GonPeriods` bundle containing the verified algebraic periods,
        minimal quadratic equations, and exact :class:`~geometor.model.Model`.
    """
    if model is None:
        model = Model("klein_von_staudt_17gon", logger=False, auto_intersect=False)
    model.set_simplifier(canonicalize_17)

    # --- 1. Exact Algebraic Period Tower (Klein Part I, Ch. IV, §§ 2–6) ---
    x1 = sp.Rational(-1, 2) + sp.Rational(1, 2) * SQRT17
    x2 = sp.Rational(-1, 2) - sp.Rational(1, 2) * SQRT17

    y1 = sp.Rational(1, 4) * (-1 + SQRT17 + A_MINUS)
    y2 = sp.Rational(1, 4) * (-1 + SQRT17 - A_MINUS)
    y4 = sp.Rational(1, 4) * (-1 - SQRT17 + A_PLUS)  # Klein's (eta'_0) > 0
    y3 = sp.Rational(1, 4) * (-1 - SQRT17 - A_PLUS)  # Klein's (eta'_1) < 0

    z_periods = _compute_all_z_periods()
    z1 = z_periods[0]
    cos_1 = canonicalize_17(sp.Rational(1, 2) * z1)

    x_sym = sp.Symbol("x")
    y_sym = sp.Symbol("y")
    z_sym = sp.Symbol("z")
    eq_xi = sp.Poly(x_sym**2 + x_sym - 4, x_sym)
    eq_eta = sp.Poly(y_sym**2 - x1 * y_sym - 1, y_sym)
    eq_eta_prime = sp.Poly(y_sym**2 - x2 * y_sym - 1, y_sym)
    eq_zeta = sp.Poly(z_sym**2 - y1 * z_sym + y4, z_sym)

    # Klein's radical-dependence identity (EN p. 30 / DE S. 23):
    # sqrt(x_1^2 + 4) * sqrt(x_2^2 + 4) = 2 * sqrt(17)
    rad_dep_res = canonicalize_17(sp.sqrt(x1**2 + 4) * sp.sqrt(x2**2 + 4) - 2 * SQRT17)

    # --- 2. Fixed Circle C0: x^2 + y(y - 2) = 0 and Rational Frame (Klein §§ 8–9, Figs. 4–9) ---
    O = model.set_point(0, 0, ID="O", classes=["given", "origin"])
    C0c = model.set_point(0, 1, ID="C0c", classes=["given", "center"])
    P10 = model.set_point(1, 0, ID="P10", classes=["given"], guide=True)
    P40 = model.set_point(4, 0, ID="P40", classes=["given"], guide=True)

    # Single fixed Poncelet-Steiner circle C0 centered at C0c(0, 1) through O(0, 0)
    C0 = model.construct_circle(C0c, O, ID="C0", classes=["given", "fixed"])

    # Vertical diameter line x = 0 and upper pole A(0, 2)
    line_y_axis = model.construct_line(O, C0c, ID="LineOA")
    A = model.intersect(line_y_axis, C0, other_than=O, ID="A", classes=["milestone"])

    # Lower tangent y = 0 (through O(0, 0) and P10(1, 0))
    line_x = model.construct_line(O, P10, ID="LineOX")

    # Construct horizontal diameter y = 1 and upper tangent y = 2 by pure straightedge on C0:
    # P10(1, 0) reflected or harmonic? Give rational frame point U12(1, 2) on upper tangent
    # (in Klein § 9, the two parallel tangents y = 0, y = 2 with unit scale are established on C0).
    U12 = model.set_point(1, 2, ID="U12", classes=["given"], guide=True)
    line_top = model.construct_line(A, U12, ID="LineTop")

    # Construct midpoint Mhalf(1/2, 1) = Line(O, U12) cap Line(A, P10) -> gives horizontal diameter y = 1!
    ray_OU12 = model.construct_line(O, U12, guide=True)
    ray_AP10 = model.construct_line(A, P10, guide=True)
    Mhalf = model.intersect(ray_OU12, ray_AP10, ID="Mhalf", guide=True)
    line_mid = model.construct_line(C0c, Mhalf, ID="LineMid")

    # East and West poles V0(1, 1) and W(-1, 1) on C0
    pts_horiz = model.intersect_all(line_mid, C0, classes=["milestone"])
    W_west, V0 = pts_horiz[0], pts_horiz[1]
    model[W_west].ID = "W0"
    model[V0].ID = "V0"
    model[V0].classes["vertex"] = ""

    # Rational 1/4-division center Hquarter(0, 2/5) on LineOA:
    # Line(P40(4, 0), Uneg1(-1, 2)) meets x = 0 at (0, 8/5); Line(P10(1, 0), Uneg4(-4, 2)) meets x = 0 at (0, 2/5)!
    # Construct Uneg4(-4, 2) in ONE straightedge line: P40(4, 0) through C0c(0, 1) meets y = 2 at (-4, 2)!
    line_xi_secant = model.construct_line(P40, C0c, ID="SecantXi", classes=["staudt"])
    Uneg4 = model.intersect(line_xi_secant, line_top, ID="Uneg4", guide=True)
    ray_quarter = model.construct_line(P10, Uneg4, guide=True)
    Hquarter = model.intersect(ray_quarter, line_y_axis, ID="Hquarter", guide=True)

    def _solve_staudt_quadratic(
        pt_lower_qp: spg.Point,
        pt_upper_4p: spg.Point,
        secant_id: str,
        id_neg: str,
        id_pos: str,
    ) -> tuple[spg.Point, spg.Point]:
        """Solve t^2 - p*t + q = 0 on C0 via Klein § 8 (join (q/p, 0) to (4/p, 2) and project from A)."""
        sec = model.construct_line(pt_lower_qp, pt_upper_4p, ID=secant_id, classes=["staudt"], guide=True)
        c_pts = model.intersect_all(sec, C0, guide=True)
        roots_on_x: list[spg.Point] = []
        for c_pt in c_pts:
            proj_ray = model.construct_line(A, c_pt, guide=True)
            r_pt = model.intersect(proj_ray, line_x, classes=["period"])
            roots_on_x.append(r_pt)
        roots_on_x.sort(key=lambda pt: float(pt.x.evalf()))
        r_left, r_right = roots_on_x[0], roots_on_x[1]
        model[r_left].ID = id_neg
        model[r_right].ID = id_pos
        return r_left, r_right

    # --- Step A: Solve (xi) x^2 + x - 4 = 0 (p = -1, q = -4 -> q/p = 4, 4/p = -4) ---
    # Note line_xi_secant ALREADY connects P40(4, 0) and Uneg4(-4, 2)!
    xi_cpts = model.intersect_all(line_xi_secant, C0, guide=True)
    xi_roots: list[spg.Point] = []
    for cpt in xi_cpts:
        ray = model.construct_line(A, cpt, guide=True)
        xi_roots.append(model.intersect(ray, line_x, classes=["period"]))
    xi_roots.sort(key=lambda pt: float(pt.x.evalf()))
    X2, X1 = xi_roots[0], xi_roots[1]
    model[X2].ID = "X2"
    model[X1].ID = "X1"

    # --- Step B: Solve (eta) y^2 - x1*y - 1 = 0 (q/p = -1/x1 = x2/4, 4/p = 4/x1 = -x2) ---
    ray_X2_center = model.construct_line(X2, C0c, guide=True)
    Q_eta_top = model.intersect(ray_X2_center, line_top, ID="QetaTop", guide=True)  # (-x2, 2) = (4/x1, 2)
    ray_eta_bot = model.construct_line(Q_eta_top, Hquarter, guide=True)
    P_eta_bot = model.intersect(ray_eta_bot, line_x, ID="PetaBot", guide=True)  # (x2/4, 0) = (-1/x1, 0)
    Y2, Y1 = _solve_staudt_quadratic(P_eta_bot, Q_eta_top, "SecantEta", "Y2", "Y1")

    # --- Step C: Solve (eta') y^2 - x2*y - 1 = 0 (q/p = -1/x2 = x1/4, 4/p = 4/x2 = -x1) ---
    ray_X1_center = model.construct_line(X1, C0c, guide=True)
    Q_etap_top = model.intersect(ray_X1_center, line_top, ID="QetapTop", guide=True)  # (-x1, 2) = (4/x2, 2)
    ray_etap_bot = model.construct_line(Q_etap_top, Hquarter, guide=True)
    P_etap_bot = model.intersect(ray_etap_bot, line_x, ID="PetapBot", guide=True)  # (x1/4, 0) = (-1/x2, 0)
    Y3, Y4 = _solve_staudt_quadratic(P_etap_bot, Q_etap_top, "SecantEtaPrime", "Y3", "Y4")

    def _solve_zeta_pair(
        pt_p: spg.Point,
        pt_p_inv_neg: spg.Point,
        pt_q: spg.Point,
        secant_id: str,
        id_left: str,
        id_right: str,
    ) -> tuple[spg.Point, spg.Point]:
        """Solve z^2 - p*z + q = 0 where p*p_inv_neg = -1 (so 4/p = -4*p_inv_neg)."""
        ray_top = model.construct_line(pt_p_inv_neg, Hquarter, guide=True)
        q_top = model.intersect(ray_top, line_top, guide=True)  # (-4*p_inv_neg, 2) = (4/p, 2)
        ray_hom = model.construct_line(P40, q_top, guide=True)
        h_ctr = model.intersect(ray_hom, line_y_axis, guide=True)
        ray_q = model.construct_line(h_ctr, pt_q, guide=True)
        u_qp = model.intersect(ray_q, line_top, guide=True)  # (q/p, 2)
        ray_mid = model.construct_line(O, u_qp, guide=True)
        m_qp = model.intersect(ray_mid, line_mid, guide=True)  # (q/(2*p), 1)
        ray_bot = model.construct_line(A, m_qp, guide=True)
        p_bot = model.intersect(ray_bot, line_x, guide=True)  # (q/p, 0)
        return _solve_staudt_quadratic(p_bot, q_top, secant_id, id_left, id_right)

    def _drop_vertical_chord_from_2c(
        pt_2c: spg.Point,
        k_id: str,
        v_bot_id: str,
        v_top_id: str,
        *,
        keep_chord: bool = False,
    ) -> tuple[spg.Point, spg.Point, spg.Point]:
        """Given Z = (2*c, 0), construct K = (c, 1) and vertical chord x = c meeting C0 at V_bot, V_top."""
        ray_az = model.construct_line(A, pt_2c, guide=not keep_chord)
        k_pt = model.intersect(
            ray_az,
            line_mid,
            ID=k_id,
            classes=["milestone"] if keep_chord else ["guide"],
            guide=not keep_chord,
        )
        ray_ok = model.construct_line(O, k_pt, guide=True)
        u_2c = model.intersect(ray_ok, line_top, guide=True)
        l_v2c = model.construct_line(u_2c, pt_2c, guide=True)
        m_2c = model.intersect(l_v2c, line_mid, guide=True)
        d1 = model.construct_line(O, m_2c, guide=True)
        d2 = model.construct_line(C0c, pt_2c, guide=True)
        q_hc = model.intersect(d1, d2, guide=True)
        chord = model.construct_line(
            k_pt,
            q_hc,
            ID="ChordV1V16" if keep_chord else "",
            classes=["staudt"] if keep_chord else ["guide"],
            guide=not keep_chord,
        )
        pair = model.intersect_all(chord, C0, classes=["vertex"])
        pair.sort(key=lambda pt: float(pt.y.evalf()))
        v_bot, v_top = pair[0], pair[1]
        model[v_bot].ID = v_bot_id
        model[v_top].ID = v_top_id
        return k_pt, v_bot, v_top

    # --- Step D: Solve (zeta_1) z^2 - y1*z + y4 = 0 -> Z2(2*cos(8*pi/17)), Z1(2*cos(2*pi/17)) ---
    Z2, Z1 = _solve_zeta_pair(Y1, Y2, Y4, "SecantZeta", "Z2", "Z1")

    # --- Step E: Construct K1(cos(2*pi/17), 1) and V1, V16 on C0 by pure straightedge ---
    K1, V16, V1 = _drop_vertical_chord_from_2c(Z1, "K1", "V16", "V1", keep_chord=True)
    sin_1 = canonicalize_17(V1.y - 1)

    vertices_map: dict[int, spg.Point] = {0: V0, 1: V1, 16: V16}

    if inscribe_polygon:
        # Drop Z2 = 2*cos(8*pi/17) -> V4, V13
        _, V13, V4 = _drop_vertical_chord_from_2c(Z2, "K4", "V13", "V4")
        vertices_map[4] = V4
        vertices_map[13] = V13

        # Solve (zeta_2) z^2 - y2*z + y3 = 0 -> Z4(2*cos(16*pi/17)), Z3(2*cos(4*pi/17))
        Z4, Z3 = _solve_zeta_pair(Y2, Y1, Y3, "SecantZeta2", "Z4", "Z3")
        _, V15, V2 = _drop_vertical_chord_from_2c(Z3, "K2", "V15", "V2")
        _, V9, V8 = _drop_vertical_chord_from_2c(Z4, "K8", "V9", "V8")
        vertices_map[2] = V2
        vertices_map[15] = V15
        vertices_map[8] = V8
        vertices_map[9] = V9

        # Solve (zeta_3) z^2 - y4*z + y2 = 0 -> Z5(2*cos(10*pi/17)), Z8(2*cos(6*pi/17))
        Z5, Z8 = _solve_zeta_pair(Y4, Y3, Y2, "SecantZeta3", "Z5", "Z8")
        _, V14, V3 = _drop_vertical_chord_from_2c(Z8, "K3", "V14", "V3")
        _, V12, V5 = _drop_vertical_chord_from_2c(Z5, "K5", "V12", "V5")
        vertices_map[3] = V3
        vertices_map[14] = V14
        vertices_map[5] = V5
        vertices_map[12] = V12

        # Solve (zeta_4) z^2 - y3*z + y1 = 0 -> Z6(2*cos(14*pi/17)), Z7(2*cos(12*pi/17))
        Z6, Z7 = _solve_zeta_pair(Y3, Y4, Y1, "SecantZeta4", "Z6", "Z7")
        _, V11, V6 = _drop_vertical_chord_from_2c(Z7, "K6", "V11", "V6")
        _, V10, V7 = _drop_vertical_chord_from_2c(Z6, "K7", "V10", "V7")
        vertices_map[6] = V6
        vertices_map[11] = V11
        vertices_map[7] = V7
        vertices_map[10] = V10

        ordered_vertices = tuple(vertices_map[k] for k in range(17))
        if add_sides:
            for k in range(17):
                nxt = (k + 1) % 17
                model.construct_segment(
                    ordered_vertices[k],
                    ordered_vertices[nxt],
                    ID=f"Side{k}",
                    classes=["polygon_side"],
                )
    else:
        ordered_vertices = (V0, V1, V16)

    milestones = {
        "O": O,
        "C0c": C0c,
        "A": A,
        "W0": W_west,
        "V0": V0,
        "X1": X1,
        "X2": X2,
        "Y1": Y1,
        "Y2": Y2,
        "Y3": Y3,
        "Y4": Y4,
        "Z1": Z1,
        "Z2": Z2,
        "K1": K1,
        "V1": V1,
        "V16": V16,
    }

    return Gauss17GonPeriods(
        primitive_root=3,
        exponent_cycle=PRIMITIVE_ROOT_3_CYCLE,
        x1=x1,
        x2=x2,
        y1=y1,
        y2=y2,
        y3=y3,
        y4=y4,
        z_periods=z_periods,
        cos_2pi_17=cos_1,
        sin_2pi_17=sin_1,
        eq_xi=eq_xi,
        eq_eta=eq_eta,
        eq_eta_prime=eq_eta_prime,
        eq_zeta=eq_zeta,
        radical_dependence_residual=rad_dep_res,
        model=model,
        fixed_circle=C0,
        milestones=milestones,
        vertices=ordered_vertices,
    )
