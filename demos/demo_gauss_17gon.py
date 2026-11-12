"""Runnable demonstration of Gauss's 17-gon periods & Klein's von Staudt-Schröter construction.

Constructs all four Gaussian period equations (xi), (eta), (eta'), (zeta) and all 17 exact
vertices V0..V16 on the single Poncelet-Steiner fixed circle C0: x^2 + y(y - 2) = 0 with
``len(model.circles) == 1`` and zero floats, then renders calibrated ``.euclid-graphic`` SVGs.
"""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
for _p in (str(_REPO_ROOT), str(_REPO_ROOT / "src")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import sympy as sp

from demos.demo_constructibility import SVG_STYLE
from geometor.klein.heptadecagon import (
    Gauss17GonPeriods,
    construct_gauss_17gon_periods,
)


def render_von_staudt_lemma_svg(out_path: Path) -> None:
    """Render Klein Part I, Ch. IV, § 8, Fig. 4: solving x^2 - px + q = 0 on fixed C0."""
    width, height = 560, 270
    # Map world x in [-2.6, 4.2], y in [-0.35, 2.35] -> SVG
    ox, oy, sc = 225.0, 225.0, 76.0

    def pt_svg(wx: float, wy: float) -> tuple[float, float]:
        return ox + sc * wx, oy - sc * wy

    # Illustrative quadratic x^2 - 3.2*x + 1.92 = 0 -> roots x1 = 2.4, x2 = 0.8
    # q/p = 0.6, 4/p = 1.25
    p_val, q_val = 3.2, 1.92
    qp = q_val / p_val  # 0.6
    fp = 4.0 / p_val  # 1.25
    r1, r2 = 2.4, 0.8

    def circle_preimage(r: float) -> tuple[float, float]:
        return (4.0 * r) / (r * r + 4.0), (2.0 * r * r) / (r * r + 4.0)

    u1, v1 = circle_preimage(r1)
    u2, v2 = circle_preimage(r2)

    cx, cy = pt_svg(0.0, 1.0)
    ax, ay = pt_svg(0.0, 2.0)
    o_x, o_y = pt_svg(0.0, 0.0)
    pqx, pqy = pt_svg(qp, 0.0)
    fpx, fpy = pt_svg(fp, 2.0)
    c1x, c1y = pt_svg(u1, v1)
    c2x, c2y = pt_svg(u2, v2)
    r1x, r1y = pt_svg(r1, 0.0)
    r2x, r2y = pt_svg(r2, 0.0)

    lines = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" height="{height}" class="euclid-graphic" '
            f'data-graphic-id="fig_von_staudt_quadratic">'
        ),
        SVG_STYLE,
        (
            '  <text x="280" y="20" text-anchor="middle" class="geom-title">'
            "Von Staudt–Schröter Quadratic Solver on Fixed Circle C₀: x² + y(y − 2) = 0 (Klein Fig. 4)"
            "</text>"
        ),
        f'  <line x1="25" y1="{o_y:.1f}" x2="535" y2="{o_y:.1f}" class="geom-line"/>',
        f'  <line x1="25" y1="{ay:.1f}" x2="535" y2="{ay:.1f}" class="geom-muted"/>',
        f'  <line x1="{o_x:.1f}" y1="32" x2="{o_x:.1f}" y2="255" class="geom-muted"/>',
        f'  <circle cx="{cx:.2f}" cy="{cy:.2f}" r="{sc:.2f}" class="geom-line"/>',
        # Secant connecting (q/p, 0) to (4/p, 2)
        f'  <line x1="{pqx:.2f}" y1="{pqy:.2f}" x2="{fpx:.2f}" y2="{fpy:.2f}" class="geom-accent"/>',
        # Stereographic projection rays from A(0, 2) through C1, C2 to roots x1, x2
        f'  <line x1="{ax:.2f}" y1="{ay:.2f}" x2="{r1x:.2f}" y2="{r1y:.2f}" class="geom-assert"/>',
        f'  <line x1="{ax:.2f}" y1="{ay:.2f}" x2="{r2x:.2f}" y2="{r2y:.2f}" class="geom-assert"/>',
    ]
    for px, py, cls in [
        (o_x, o_y, "geom-point"),
        (cx, cy, "geom-point"),
        (ax, ay, "geom-point"),
        (pqx, pqy, "geom-point-accent"),
        (fpx, fpy, "geom-point-accent"),
        (c1x, c1y, "geom-point-accent"),
        (c2x, c2y, "geom-point-accent"),
        (r1x, r1y, "geom-point-accent"),
        (r2x, r2y, "geom-point-accent"),
    ]:
        lines.append(f'  <circle cx="{px:.2f}" cy="{py:.2f}" r="3.6" class="{cls}"/>')

    lines.extend(
        [
            f'  <text x="{o_x - 14:.1f}" y="{o_y + 16:.1f}" class="geom-label">O(0,0)</text>',
            f'  <text x="{ax - 42:.1f}" y="{ay - 6:.1f}" class="geom-label">A(0,2)</text>',
            f'  <text x="{cx - 22:.1f}" y="{cy + 4:.1f}" class="geom-sub">C₀</text>',
            f'  <text x="{pqx - 16:.1f}" y="{pqy + 16:.1f}" class="geom-label">(q/p, 0)</text>',
            f'  <text x="{fpx + 6:.1f}" y="{fpy - 6:.1f}" class="geom-label">(4/p, 2)</text>',
            f'  <text x="{r2x - 6:.1f}" y="{r2y + 16:.1f}" class="geom-label">x₂</text>',
            f'  <text x="{r1x - 6:.1f}" y="{r1y + 16:.1f}" class="geom-label">x₁</text>',
            '  <text x="485" y="65" class="geom-sub">y = 2</text>',
            '  <text x="485" y="218" class="geom-sub">y = 0</text>',
            "</svg>\n",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def render_von_staudt_17gon_svg(res: Gauss17GonPeriods, out_path: Path) -> None:
    """Render exact von Staudt-Schröter 17-gon periods extracted directly from ``res.model``."""
    width, height = 660, 310
    ox, oy, sc = 335.0, 255.0, 70.0

    def pt_svg(pt) -> tuple[float, float]:
        return ox + sc * float(pt.x.evalf()), oy - sc * float(pt.y.evalf())

    m = res.milestones
    cx, cy = pt_svg(m["C0c"])
    ax, ay = pt_svg(m["A"])
    o_x, o_y = pt_svg(m["O"])

    lines = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" height="{height}" class="euclid-graphic" '
            f'data-graphic-id="fig_von_staudt_17gon">'
        ),
        SVG_STYLE,
        (
            '  <text x="330" y="22" text-anchor="middle" class="geom-title">'
            "Poncelet–Steiner Single-Circle Construction of Gauss’s 17-Gon Periods (Klein Ch. IV, § 9)"
            "</text>"
        ),
        f'  <line x1="20" y1="{o_y:.1f}" x2="640" y2="{o_y:.1f}" class="geom-line"/>',
        f'  <line x1="20" y1="{cy:.1f}" x2="640" y2="{cy:.1f}" class="geom-muted"/>',
        f'  <line x1="20" y1="{ay:.1f}" x2="640" y2="{ay:.1f}" class="geom-muted"/>',
        f'  <line x1="{o_x:.1f}" y1="36" x2="{o_x:.1f}" y2="288" class="geom-muted"/>',
        f'  <circle cx="{cx:.2f}" cy="{cy:.2f}" r="{sc:.2f}" class="geom-line"/>',
    ]

    # Projection rays from A(0, 2) to X1, X2, Y1, Y4, Z1
    for key, cls in [
        ("X2", "geom-muted"),
        ("X1", "geom-muted"),
        ("Y1", "geom-muted"),
        ("Y4", "geom-muted"),
        ("Z1", "geom-accent"),
    ]:
        px, py = pt_svg(m[key])
        lines.append(f'  <line x1="{ax:.2f}" y1="{ay:.2f}" x2="{px:.2f}" y2="{py:.2f}" class="{cls}"/>')

    # Vertical chord V1 - K1 - V16
    v1x, v1y = pt_svg(m["V1"])
    v16x, v16y = pt_svg(m["V16"])
    lines.append(f'  <line x1="{v1x:.2f}" y1="{v1y:.2f}" x2="{v16x:.2f}" y2="{v16y:.2f}" class="geom-assert"/>')

    # Period milestones along y = 0
    period_labels = [
        ("X2", "x₂", -16),
        ("Y3", "y₃", 16),
        ("Y2", "y₂", -10),
        ("O", "O", 16),
        ("Z2", "z₂", 16),
        ("Y4", "y₄", -10),
        ("X1", "x₁", 16),
        ("Z1", "z₁", -10),
        ("Y1", "y₁", 16),
    ]
    for key, lbl, dy in period_labels:
        px, py = pt_svg(m[key])
        p_cls = "geom-point-accent" if key in ("X1", "Y1", "Y4", "Z1") else "geom-point"
        lines.append(f'  <circle cx="{px:.2f}" cy="{py:.2f}" r="3.4" class="{p_cls}"/>')
        lines.append(
            f'  <text x="{px:.1f}" y="{py + dy:.1f}" text-anchor="middle" class="geom-label">{lbl}</text>'
        )

    for key, lbl, dx, dy in [
        ("A", "A(0,2)", -26, -6),
        ("V0", "V₀", 12, 4),
        ("K1", "K₁", -14, -5),
        ("V1", "V₁", 12, -4),
        ("V16", "V₁₆", 15, 11),
    ]:
        px, py = pt_svg(m[key])
        lines.append(f'  <circle cx="{px:.2f}" cy="{py:.2f}" r="3.8" class="geom-point-accent"/>')
        lines.append(f'  <text x="{px + dx:.1f}" y="{py + dy:.1f}" class="geom-label">{lbl}</text>')

    lines.append("</svg>\n")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def render_gauss_17gon_circle_svg(res: Gauss17GonPeriods, out_path: Path) -> None:
    """Render the inscribed regular 17-gon V0..V16 and conjugate 2-period chords."""
    width, height = 460, 420
    cx, cy, sc = 230.0, 222.0, 152.0

    def v_svg(pt) -> tuple[float, float]:
        wx = float(pt.x.evalf())
        wy = float(pt.y.evalf()) - 1.0
        return cx + sc * wx, cy - sc * wy

    verts_svg = [v_svg(v) for v in res.vertices]
    poly_pts = " ".join(f"{px:.2f},{py:.2f}" for px, py in verts_svg)

    lines = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" height="{height}" class="euclid-graphic" '
            f'data-graphic-id="fig_gauss_17gon_circle">'
        ),
        SVG_STYLE,
        (
            '  <text x="230" y="24" text-anchor="middle" class="geom-title">'
            "Exact Regular Heptadecagon (V₀..V₁₆) &amp; Gaussian 2-Period Chords"
            "</text>"
        ),
        f'  <line x1="45" y1="{cy:.1f}" x2="415" y2="{cy:.1f}" class="geom-muted"/>',
        f'  <line x1="{cx:.1f}" y1="46" x2="{cx:.1f}" y2="396" class="geom-muted"/>',
        f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{sc:.1f}" class="geom-line"/>',
        f'  <polygon points="{poly_pts}" class="geom-poly-ok"/>',
    ]

    # Vertical conjugate pairs (V_k, V_{17-k}) defining z_1..z_8 = 2*cos(2*pi*k/17)
    for k in range(1, 9):
        p_top = verts_svg[k]
        p_bot = verts_svg[17 - k]
        cls = "geom-accent" if k in (1, 4) else "geom-muted"
        lines.append(
            f'  <line x1="{p_top[0]:.2f}" y1="{p_top[1]:.2f}" '
            f'x2="{p_bot[0]:.2f}" y2="{p_bot[1]:.2f}" class="{cls}"/>'
        )

    for k, (px, py) in enumerate(verts_svg):
        wx = (px - cx) / sc
        wy = (py - cy) / sc
        lx = cx + (sc + 20.0) * wx
        ly = cy + (sc + 20.0) * wy + 4.0
        p_cls = "geom-point-accent" if k in (0, 1, 4, 13, 16) else "geom-point"
        lines.append(f'  <circle cx="{px:.2f}" cy="{py:.2f}" r="3.6" class="{p_cls}"/>')
        lines.append(
            f'  <text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" class="geom-label">V{k}</text>'
        )

    lines.append("</svg>\n")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    res = construct_gauss_17gon_periods()
    print("=== Gauss-Staudt-Schröter-Klein Regular 17-Gon ===")
    print("  Primitive root g =", res.primitive_root, "cycle =", res.exponent_cycle)
    print("  x1 =", res.x1, "≈", float(res.x1.evalf()))
    print("  x2 =", res.x2, "≈", float(res.x2.evalf()))
    print("  y1 =", res.y1, "≈", float(res.y1.evalf()))
    print("  y2 =", res.y2, "≈", float(res.y2.evalf()))
    print("  y4 =", res.y4, "≈", float(res.y4.evalf()))
    print("  y3 =", res.y3, "≈", float(res.y3.evalf()))
    print("  cos(2*pi/17) =", res.cos_2pi_17, "≈", float(res.cos_2pi_17.evalf()))
    print("  Radical dependence residual:", res.radical_dependence_residual)
    print("  Circles in geometor.model.Model:", len(res.model.circles))
    print("  Exact vertices constructed:", len(res.vertices))

    float_atoms = sum(len(pt.x.atoms(sp.Float)) + len(pt.y.atoms(sp.Float)) for pt in res.model.points)
    print("  Total sp.Float atoms across all model points:", float_atoms)

    fig_dir = _REPO_ROOT / "docsrc" / "_static" / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    render_von_staudt_lemma_svg(fig_dir / "fig_von_staudt_quadratic.svg")
    render_von_staudt_17gon_svg(res, fig_dir / "fig_von_staudt_17gon.svg")
    render_gauss_17gon_circle_svg(res, fig_dir / "fig_gauss_17gon_circle.svg")
    print("  Wrote 17-gon SVGs to", fig_dir)


if __name__ == "__main__":
    main()
