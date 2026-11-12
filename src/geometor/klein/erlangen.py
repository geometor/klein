"""Exact symbolic verification of Felix Klein's *Erlangen Program* (1872 / 1893) group hierarchy.

Demonstrates Klein's foundational principle (*Vergleichende Betrachtungen*, §§ 1–2, § 6, § 10,
Note V): a geometry on a manifold :math:`M` is the invariant theory of a transformation group
:math:`G` acting on :math:`M`. As the transformation group widens along the chain

.. math::

    G_{\\text{Euclidean}} \\subset G_{\\text{Principal}} \\subset G_{\\text{Affine}}
    \\subset G_{\\text{Projective}},

and branches laterally from :math:`G_{\\text{Principal}}` into the **geometry of reciprocal radii**
(:math:`G_{\\text{M\\"{o}bius}}`, § 6), exact algebraic invariants are progressively shed while deeper
structural invariants survive. All calculations use 100% exact rational / symbolic SymPy arithmetic.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model.invariants import cross_ratio, line_spread, quadrance

__all__ = [
    "CayleyKleinReport",
    "ErlangenHierarchyReport",
    "ErlangenRungResult",
    "circular_quadrance_cross_ratio",
    "is_concyclic",
    "signed_area_ratio",
    "verify_cayley_klein_additivity",
    "verify_erlangen_invariants",
]


@dataclass(frozen=True)
class ErlangenRungResult:
    """Exact symbolic invariant audit for a single transformation group in Klein's hierarchy."""

    group_key: str
    group_name: str
    erlangen_section: str
    transformation_formula: str
    preserved: dict[str, bool]
    exact_values_before: dict[str, sp.Expr]
    exact_values_after: dict[str, sp.Expr]
    exact_differences: dict[str, sp.Expr]


@dataclass(frozen=True)
class ErlangenHierarchyReport:
    """Aggregate report across all four transformation groups in the Erlangen hierarchy."""

    collinear_quadruple: tuple[spg.Point2D, spg.Point2D, spg.Point2D, spg.Point2D]
    concyclic_quadruple: tuple[spg.Point2D, spg.Point2D, spg.Point2D, spg.Point2D]
    triangle_vertices: tuple[spg.Point2D, spg.Point2D, spg.Point2D, spg.Point2D]
    rungs: tuple[ErlangenRungResult, ...]

    def by_key(self) -> dict[str, ErlangenRungResult]:
        """Map ``group_key`` to its :class:`ErlangenRungResult`."""
        return {r.group_key: r for r in self.rungs}


@dataclass(frozen=True)
class CayleyKleinReport:
    """Symbolic verification of Cayley–Klein projective metric additivity (Note V & § 10)."""

    cross_ratio_ab: sp.Expr
    cross_ratio_bc: sp.Expr
    cross_ratio_ac: sp.Expr
    multiplicative_identity_residual: sp.Expr
    hyperbolic_sample_distance_ab: sp.Expr
    hyperbolic_sample_distance_bc: sp.Expr
    hyperbolic_sample_distance_ac: sp.Expr
    additive_residual: sp.Expr


def signed_twice_area(p1: spg.Point2D, p2: spg.Point2D, p3: spg.Point2D) -> sp.Expr:
    """Return twice the signed planar area :math:`\\det\\begin{pmatrix}x_2-x_1 & x_3-x_1\\\\y_2-y_1 & y_3-y_1\\end{pmatrix}`."""
    return sp.simplify((p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y))


def signed_area_ratio(
    p1: spg.Point2D,
    p2: spg.Point2D,
    p3: spg.Point2D,
    q1: spg.Point2D,
    q2: spg.Point2D,
    q3: spg.Point2D,
) -> sp.Expr:
    """Return the exact affine-invariant ratio of signed areas :math:`[P_1P_2P_3] / [Q_1Q_2Q_3]`."""
    return sp.simplify(signed_twice_area(p1, p2, p3) / signed_twice_area(q1, q2, q3))


def collinear_division_ratio(a: spg.Point2D, b: spg.Point2D, c: spg.Point2D) -> sp.Expr:
    """Return affine division ratio :math:`\\lambda` where :math:`C - A = \\lambda(B - A)` on line ``AB``."""
    if sp.simplify(b.x - a.x) != 0:
        return sp.simplify((c.x - a.x) / (b.x - a.x))
    return sp.simplify((c.y - a.y) / (b.y - a.y))


def circular_quadrance_cross_ratio(
    p1: spg.Point2D,
    p2: spg.Point2D,
    p3: spg.Point2D,
    p4: spg.Point2D,
) -> sp.Expr:
    """Compute the Möbius-invariant 4-point quadrance cross-ratio :math:`\\frac{Q(P_1,P_3)Q(P_2,P_4)}{Q(P_1,P_4)Q(P_2,P_3)}`.

    Under any Euclidean similarity or any circle inversion :math:`P \\mapsto O + R^2(P-O)/Q(O,P)`
    (whose center :math:`O` is distinct from :math:`P_1..P_4`), the squared chord length transforms
    as :math:`Q(P_i', P_j') = R^4 Q(P_i, P_j) / [Q(O, P_i) Q(O, P_j)]`, so all four denominator
    factors :math:`Q(O, P_k)` cancel identically! Furthermore, when :math:`A, B, C, D` are
    collinear, this coincides with the square :math:`(A, B; C, D)^2` of the projective cross-ratio.
    """
    num = quadrance(p1, p3) * quadrance(p2, p4)
    den = quadrance(p1, p4) * quadrance(p2, p3)
    return sp.simplify(num / den)


def cayley_menger_concyclic_det(
    p1: spg.Point2D,
    p2: spg.Point2D,
    p3: spg.Point2D,
    p4: spg.Point2D,
) -> sp.Expr:
    """Return the generalized-circle (circle-or-line) determinant :math:`\\det[x_i^2+y_i^2, x_i, y_i, 1]`."""
    rows = [[p.x**2 + p.y**2, p.x, p.y, sp.Integer(1)] for p in (p1, p2, p3, p4)]
    return sp.simplify(sp.Matrix(rows).det())


def is_concyclic(
    p1: spg.Point2D,
    p2: spg.Point2D,
    p3: spg.Point2D,
    p4: spg.Point2D,
) -> bool:
    """Return ``True`` iff ``p1, p2, p3, p4`` lie on a generalized circle (circle or straight line)."""
    return cayley_menger_concyclic_det(p1, p2, p3, p4) == 0


def _evaluate_configuration(
    collinear_pts: tuple[spg.Point2D, spg.Point2D, spg.Point2D, spg.Point2D],
    circle_pts: tuple[spg.Point2D, spg.Point2D, spg.Point2D, spg.Point2D],
    tri_pts: tuple[spg.Point2D, spg.Point2D, spg.Point2D, spg.Point2D],
    par_pts: tuple[spg.Point2D, spg.Point2D, spg.Point2D, spg.Point2D],
) -> dict[str, sp.Expr]:
    a, b, c, d = collinear_pts
    p1, p2, p3, p4 = circle_pts
    t1, t2, t3, t4 = tri_pts
    u1, u2, v1, v2 = par_pts

    collinear_det = signed_twice_area(a, b, c)
    is_col = collinear_det == 0

    # Parallelism residual (u2 - u1) x (v2 - v1)
    parallel_det = sp.simplify((u2.x - u1.x) * (v2.y - v1.y) - (u2.y - u1.y) * (v2.x - v1.x))

    # Spread between lines T1T2 and T1T3
    l12 = spg.Line(t1, t2)
    l13 = spg.Line(t1, t3)
    ang_spread = sp.simplify(line_spread(l12, l13))

    return {
        "quadrance_ab": sp.simplify(quadrance(a, b)),
        "quadrance_ratio": sp.simplify(quadrance(t1, t2) / quadrance(t1, t3)),
        "angle_spread": ang_spread,
        "parallelism_residual": parallel_det,
        "division_ratio": collinear_division_ratio(a, b, c) if is_col else sp.Symbol("non_collinear"),
        "area_ratio": signed_area_ratio(t1, t2, t3, t1, t2, t4),
        "collinearity_residual": collinear_det,
        "collinear_cross_ratio": sp.simplify(cross_ratio(a, b, c, d))
        if is_col
        else sp.Symbol("non_collinear"),
        "generalized_circle_residual": cayley_menger_concyclic_det(p1, p2, p3, p4),
        "circular_quadrance_cross_ratio": circular_quadrance_cross_ratio(p1, p2, p3, p4),
    }


def _compare_before_after(
    before: dict[str, sp.Expr],
    after: dict[str, sp.Expr],
) -> tuple[dict[str, bool], dict[str, sp.Expr]]:
    preserved: dict[str, bool] = {}
    diffs: dict[str, sp.Expr] = {}

    # 1. Exact value-equality invariants
    value_keys = (
        "quadrance_ab",
        "quadrance_ratio",
        "angle_spread",
        "division_ratio",
        "area_ratio",
        "collinear_cross_ratio",
        "circular_quadrance_cross_ratio",
    )
    for k in value_keys:
        if before[k].free_symbols or after[k].free_symbols:
            preserved[k] = False
            diffs[k] = sp.Symbol("undefined_non_collinear")
        else:
            diff = sp.simplify(after[k] - before[k])
            diffs[k] = diff
            preserved[k] = diff == 0

    # 2. Zero-locus incidences (parallelism, collinearity, generalized circles)
    locus_map = {
        "parallelism": "parallelism_residual",
        "collinearity": "collinearity_residual",
        "generalized_circles": "generalized_circle_residual",
    }
    for flag_name, res_key in locus_map.items():
        assert before[res_key] == 0
        diff = sp.simplify(after[res_key])
        diffs[flag_name] = diff
        preserved[flag_name] = diff == 0

    return preserved, diffs


def verify_erlangen_invariants() -> ErlangenHierarchyReport:
    """Execute an exact symbolic invariant audit across four groups of Klein's Erlangen Program.

    Applies four rational planar transformations to a shared exact rational point configuration:

    1. ``principal_similarity`` (*Hauptgruppe*, § 1): rational rotation :math:`(3/5, 4/5)`,
       isotropic scaling :math:`5/2`, and translation :math:`(3, -2)`.
    2. ``affine_shear`` (§ 2): equiaffine shear + translation :math:`(x, y) \\mapsto (x + 2y + 1, y - 3)`.
    3. ``projective_homography`` (§ 3): nonsingular projective collineation
       :math:`(x, y) \\mapsto \\left(\\frac{2x + y + 1}{x + y + 3}, \\frac{x + 3y + 2}{x + y + 3}\\right)`.
    4. ``moebius_circle_inversion`` (*Geometrie der reciproken Radien*, § 6): inversion in the
       circle centered at :math:`O_{\\mathrm{inv}}(-1, -2)` of squared radius :math:`R^2 = 5`.
    """
    # Collinear quadruple on y = x + 1 (does not pass through inversion center (-1, -2))
    collinear_pts = (
        spg.Point2D(0, 1),
        spg.Point2D(1, 2),
        spg.Point2D(3, 4),
        spg.Point2D(6, 7),
    )
    # Concyclic quadruple on standard Pythagorean circle x^2 + y^2 = 25
    circle_pts = (
        spg.Point2D(5, 0),
        spg.Point2D(4, 3),
        spg.Point2D(0, 5),
        spg.Point2D(-3, 4),
    )
    # Non-degenerate reference triangles T1T2T3 and T1T2T4 in general position
    tri_pts = (
        spg.Point2D(0, 0),
        spg.Point2D(2, 0),
        spg.Point2D(0, 3),
        spg.Point2D(2, 3),
    )
    # Parallel segment pair: U1U2 along (2, 1) and V1V2 along (4, 2)
    par_pts = (
        spg.Point2D(0, 0),
        spg.Point2D(2, 1),
        spg.Point2D(0, 2),
        spg.Point2D(4, 4),
    )

    before = _evaluate_configuration(collinear_pts, circle_pts, tri_pts, par_pts)

    def _principal(p: spg.Point2D) -> spg.Point2D:
        scale = sp.Rational(5, 2)
        rx = sp.Rational(3, 5) * p.x - sp.Rational(4, 5) * p.y
        ry = sp.Rational(4, 5) * p.x + sp.Rational(3, 5) * p.y
        return spg.Point2D(sp.simplify(scale * rx + 3), sp.simplify(scale * ry - 2))

    def _affine(p: spg.Point2D) -> spg.Point2D:
        return spg.Point2D(sp.simplify(p.x + 2 * p.y + 1), sp.simplify(p.y - 3))

    def _projective(p: spg.Point2D) -> spg.Point2D:
        denom = p.x + p.y + 3
        return spg.Point2D(
            sp.simplify((2 * p.x + p.y + 1) / denom),
            sp.simplify((p.x + 3 * p.y + 2) / denom),
        )

    o_inv = spg.Point2D(-1, -2)
    r_sq = sp.Integer(5)

    def _inversion(p: spg.Point2D) -> spg.Point2D:
        q = quadrance(o_inv, p)
        return spg.Point2D(
            sp.simplify(o_inv.x + r_sq * (p.x - o_inv.x) / q),
            sp.simplify(o_inv.y + r_sq * (p.y - o_inv.y) / q),
        )

    specs = (
        (
            "principal_similarity",
            "Principal Group (Euclidean Similarities / Hauptgruppe)",
            "Erlangen Program, § 1",
            "(x, y) -> (5/2)*((3/5)x - (4/5)y, (4/5)x + (3/5)y) + (3, -2)",
            _principal,
        ),
        (
            "affine_shear",
            "Affine / Equiaffine Group",
            "Erlangen Program, § 2",
            "(x, y) -> (x + 2y + 1, y - 3)",
            _affine,
        ),
        (
            "projective_homography",
            "Projective Group of Collineations",
            "Erlangen Program, §§ 2–3",
            "(x, y) -> ((2x + y + 1)/(x + y + 3), (x + 3y + 2)/(x + y + 3))",
            _projective,
        ),
        (
            "moebius_circle_inversion",
            "Geometry of Reciprocal Radii (Möbius Inversion Group)",
            "Erlangen Program, § 6",
            "P -> O + 5*(P - O)/Q(O, P) with O = (-1, -2)",
            _inversion,
        ),
    )

    rungs: list[ErlangenRungResult] = []
    for key, name, sec, formula, fn in specs:
        after = _evaluate_configuration(
            tuple(fn(p) for p in collinear_pts),  # type: ignore[arg-type]
            tuple(fn(p) for p in circle_pts),  # type: ignore[arg-type]
            tuple(fn(p) for p in tri_pts),  # type: ignore[arg-type]
            tuple(fn(p) for p in par_pts),  # type: ignore[arg-type]
        )
        preserved, diffs = _compare_before_after(before, after)
        rungs.append(
            ErlangenRungResult(
                group_key=key,
                group_name=name,
                erlangen_section=sec,
                transformation_formula=formula,
                preserved=preserved,
                exact_values_before=before,
                exact_values_after=after,
                exact_differences=diffs,
            )
        )

    return ErlangenHierarchyReport(
        collinear_quadruple=collinear_pts,
        concyclic_quadruple=circle_pts,
        triangle_vertices=tri_pts,
        rungs=tuple(rungs),
    )


def verify_cayley_klein_additivity() -> CayleyKleinReport:
    """Prove symbolic additivity of Klein's projective metric :math:`d(A, B) = c \\log(A, B; I_1, I_2)`.

    In Note V (*On the So-Called Non-Euclidean Geometry*) and § 10.2 of the *Erlangen Program*,
    Klein subsumes hyperbolic, elliptic, and parabolic metrics under projective geometry by
    adjoining an invariant second-degree Absolute (:math:`\\Omega = 0`). Along any line meeting
    the Absolute in :math:`I_1, I_2`, the cross-ratio multiplicativity
    :math:`(A, B; I_1, I_2) \\cdot (B, C; I_1, I_2) = (A, C; I_1, I_2)` converts into exact
    geodesic distance additivity :math:`d(A, B) + d(B, C) = d(A, C)`.
    """
    a, b, c, i1, i2 = sp.symbols("a b c i_1 i_2")

    def _cr_1d(x1: sp.Expr, x2: sp.Expr, x3: sp.Expr, x4: sp.Expr) -> sp.Expr:
        return ((x1 - x3) * (x2 - x4)) / ((x1 - x4) * (x2 - x3))

    cr_ab = _cr_1d(a, b, i1, i2)
    cr_bc = _cr_1d(b, c, i1, i2)
    cr_ac = _cr_1d(a, c, i1, i2)
    mult_res = sp.simplify(cr_ab * cr_bc - cr_ac)

    # Concrete rational sample inside the Klein disk (-1, 1) on the x-axis: I1 = -1, I2 = 1
    p_i1 = spg.Point2D(-1, 0)
    p_a = spg.Point2D(-sp.Rational(1, 2), 0)
    p_b = spg.Point2D(0, 0)
    p_c = spg.Point2D(sp.Rational(3, 5), 0)
    p_i2 = spg.Point2D(1, 0)

    scale = sp.Rational(1, 2)
    d_ab = sp.simplify(scale * sp.log(cross_ratio(p_a, p_b, p_i2, p_i1)))
    d_bc = sp.simplify(scale * sp.log(cross_ratio(p_b, p_c, p_i2, p_i1)))
    d_ac = sp.simplify(scale * sp.log(cross_ratio(p_a, p_c, p_i2, p_i1)))
    add_res = sp.simplify(sp.exp((d_ab + d_bc - d_ac) / scale) - 1)

    return CayleyKleinReport(
        cross_ratio_ab=cr_ab,
        cross_ratio_bc=cr_bc,
        cross_ratio_ac=cr_ac,
        multiplicative_identity_residual=mult_res,
        hyperbolic_sample_distance_ab=d_ab,
        hyperbolic_sample_distance_bc=d_bc,
        hyperbolic_sample_distance_ac=d_ac,
        additive_residual=add_res,
    )
