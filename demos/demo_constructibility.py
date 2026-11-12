"""Runnable demonstration of Felix Klein's constructibility criteria & higher algebraic curves.

Executes ``analyze_constructibility`` across regular polygons (n = 3..24), the Delian cube
duplication (x^3 - 2 = 0), angle trisection (4x^3 - 3x - 1/2 = 0), regular heptagon
(u^3 + u^2 - 2u - 1 = 0), Galois quartic resolvents (x^4 - 2 vs. x^4 - x - 1), and
Hermite/Lindemann transcendental constants (e, pi), and renders dark/light-adaptive
``.euclid-graphic`` SVGs into ``docsrc/_static/figures/``.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT / "src"))

import sympy as sp

from geometor.klein.constructibility import (
    analyze_constructibility,
    tabulate_polygon_constructibility,
)

SVG_STYLE = """  <style>
    :root {
      --geom-fg: #18181b;
      --geom-bg: #ffffff;
      --geom-muted: #71717a;
      --geom-point-stroke: #ffffff;
      --geom-accent: #c88a1e;
      --geom-assert: #16a34a;
      --geom-danger: #dc2626;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --geom-fg: #d6cfc5;
        --geom-bg: #1e1e20;
        --geom-muted: #a1a1aa;
        --geom-point-stroke: #1e1e20;
        --geom-accent: #e8b85a;
        --geom-assert: #5ec27e;
        --geom-danger: #f87171;
      }
    }
    .euclid-graphic {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      background-color: var(--geom-bg);
    }
    .geom-line { stroke: var(--geom-fg); stroke-width: 1.6; fill: none; }
    .geom-muted { stroke: var(--geom-muted); stroke-width: 1.1; stroke-dasharray: 4, 3; fill: none; }
    .geom-accent { stroke: var(--geom-accent); stroke-width: 2.1; fill: none; }
    .geom-assert { stroke: var(--geom-assert); stroke-width: 2.0; fill: none; }
    .geom-danger { stroke: var(--geom-danger); stroke-width: 1.8; fill: none; }
    .geom-poly-ok { fill: var(--geom-assert); fill-opacity: 0.14; stroke: var(--geom-assert); stroke-width: 1.8; }
    .geom-poly-no { fill: var(--geom-danger); fill-opacity: 0.10; stroke: var(--geom-danger); stroke-width: 1.5; stroke-dasharray: 4, 2.5; }
    .geom-point { fill: var(--geom-fg); stroke: var(--geom-point-stroke); stroke-width: 1.1; }
    .geom-point-accent { fill: var(--geom-accent); stroke: var(--geom-point-stroke); stroke-width: 1.2; }
    .geom-title { fill: var(--geom-fg); font-size: 13px; font-weight: 700; }
    .geom-sub { fill: var(--geom-muted); font-size: 11px; font-weight: 600; }
    .geom-label { fill: var(--geom-fg); font-size: 11.5px; font-weight: 700; }
  </style>"""


def render_polygon_grid_svg(out_path: Path) -> None:
    """Render regular polygons n = 3..18 classifying Gauss-Wantzel constructibility."""
    reports = tabulate_polygon_constructibility(18, min_n=3)
    cols = 4
    cell_w, cell_h = 150, 128
    pad_top = 44
    width = cols * cell_w + 20
    rows = math.ceil(len(reports) / cols)
    height = pad_top + rows * cell_h + 16

    lines = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" height="{height}" class="euclid-graphic" '
            f'data-graphic-id="fig_constructibility_polygons">'
        ),
        SVG_STYLE,
        (
            f'  <text x="{width / 2:.1f}" y="24" text-anchor="middle" class="geom-title">'
            "Gauss–Wantzel Polygon Constructibility (n = 3..18): φ(n) = 2^k vs. Odd Obstructions"
            "</text>"
        ),
    ]

    r_rad = 34.0
    for idx, rep in enumerate(reports):
        n = idx + 3
        col = idx % cols
        row = idx // cols
        cx = 10 + col * cell_w + cell_w / 2
        cy = pad_top + row * cell_h + 48

        pts = []
        for k in range(n):
            ang = -math.pi / 2 + 2 * math.pi * k / n
            px = cx + r_rad * math.cos(ang)
            py = cy + r_rad * math.sin(ang)
            pts.append(f"{px:.2f},{py:.2f}")
        cls = "geom-poly-ok" if rep.is_constructible else "geom-poly-no"
        lines.append(f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r_rad:.1f}" class="geom-muted"/>')
        lines.append(f'  <polygon points="{" ".join(pts)}" class="{cls}"/>')
        badge = "✓ 2^" + str(rep.tower_depth) if rep.is_constructible else f"✗ φ={rep.euler_totient}"
        lines.append(
            f'  <text x="{cx:.1f}" y="{cy + 52:.1f}" text-anchor="middle" class="geom-label">'
            f"n = {n} ({badge})</text>"
        )

    lines.append("</svg>\n")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def render_conchoid_cissoid_svg(out_path: Path) -> None:
    """Render Klein's Cissoid of Diocles (Fig. 12) and Conchoid of Nicomedes (Fig. 13)."""
    width, height = 640, 280
    lines = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" height="{height}" class="euclid-graphic" '
            f'data-graphic-id="fig_conchoid_cissoid">'
        ),
        SVG_STYLE,
        (
            '  <text x="160" y="22" text-anchor="middle" class="geom-title">'
            "Cissoid of Diocles: (x² + y²)x − y² = 0</text>"
        ),
        (
            '  <text x="480" y="22" text-anchor="middle" class="geom-title">'
            "Conchoid of Nicomedes: (x² + y²)(x − a)² = b²x²</text>"
        ),
    ]

    # Left panel: Cissoid of Diocles with origin O(65, 150), unit diameter [0, 1] -> scale 140 px
    ox, oy, sc = 65.0, 150.0, 140.0
    lines.append(f'  <line x1="35" y1="{oy}" x2="285" y2="{oy}" class="geom-muted"/>')
    lines.append(f'  <line x1="{ox}" y1="40" x2="{ox}" y2="260" class="geom-muted"/>')
    lines.append(
        f'  <circle cx="{ox + 0.5 * sc:.2f}" cy="{oy:.2f}" r="{0.5 * sc:.2f}" class="geom-line"/>'
    )
    # Asymptote x = 1
    ax = ox + sc
    lines.append(f'  <line x1="{ax:.2f}" y1="36" x2="{ax:.2f}" y2="264" class="geom-danger"/>')

    ciss_pts = []
    for i in range(-38, 39):
        t = i / 28.0  # y = t*x, x = t^2 / (1 + t^2)
        x = (t * t) / (1.0 + t * t)
        y = t * x
        px = ox + sc * x
        py = oy - sc * y
        if 36 <= py <= 264:
            ciss_pts.append(f"{px:.2f},{py:.2f}")
    lines.append(f'  <polyline points="{" ".join(ciss_pts)}" class="geom-accent"/>')

    # On cissoid: (y/x)^3 = y / (1 - x). Line y = 2(1 - x) gives (y/x)^3 = 2!
    cbrt2 = 2.0 ** (1.0 / 3.0)
    t_del = cbrt2
    x_p = (t_del**2) / (1.0 + t_del**2)
    y_p = t_del * x_p
    px_d, py_d = ox + sc * x_p, oy - sc * y_p
    lines.append(
        f'  <line x1="{ox:.2f}" y1="{oy:.2f}" x2="{ox + sc:.2f}" '
        f'y2="{oy - sc * t_del:.2f}" class="geom-assert"/>'
    )
    lines.append(f'  <circle cx="{ox:.2f}" cy="{oy:.2f}" r="3.5" class="geom-point"/>')
    lines.append(f'  <circle cx="{px_d:.2f}" cy="{py_d:.2f}" r="4.0" class="geom-point-accent"/>')
    lines.append(f'  <text x="{ox - 12:.1f}" y="{oy + 15:.1f}" class="geom-label">O</text>')
    lines.append(f'  <text x="{ax + 5:.1f}" y="50" class="geom-sub">x = 1</text>')
    lines.append(f'  <text x="{px_d + 6:.1f}" y="{py_d - 5:.1f}" class="geom-label">P (y/x = ∛2)</text>')

    # Right panel: Conchoid of Nicomedes, origin O(445, 150), directrix x = a (a = 0.55, b = 0.95)
    ox2, oy2, sc2 = 445.0, 150.0, 95.0
    a_val, b_val = 0.65, 1.05
    lines.append(f'  <line x1="340" y1="{oy2}" x2="620" y2="{oy2}" class="geom-muted"/>')
    lines.append(f'  <line x1="{ox2}" y1="40" x2="{ox2}" y2="260" class="geom-muted"/>')
    dir_x = ox2 + sc2 * a_val
    lines.append(f'  <line x1="{dir_x:.2f}" y1="36" x2="{dir_x:.2f}" y2="264" class="geom-muted"/>')

    branch_pos = []
    branch_neg = []
    for i in range(-62, 63):
        th = (i / 63.0) * 1.22
        sec = 1.0 / math.cos(th)
        r1 = a_val * sec + b_val
        r2 = a_val * sec - b_val
        p1x, p1y = ox2 + sc2 * r1 * math.cos(th), oy2 - sc2 * r1 * math.sin(th)
        p2x, p2y = ox2 + sc2 * r2 * math.cos(th), oy2 - sc2 * r2 * math.sin(th)
        if 36 <= p1y <= 264 and 335 <= p1x <= 625:
            branch_pos.append(f"{p1x:.2f},{p1y:.2f}")
        if 36 <= p2y <= 264 and 335 <= p2x <= 625:
            branch_neg.append(f"{p2x:.2f},{p2y:.2f}")

    lines.append(f'  <polyline points="{" ".join(branch_pos)}" class="geom-accent"/>')
    lines.append(f'  <polyline points="{" ".join(branch_neg)}" class="geom-assert"/>')
    lines.append(f'  <circle cx="{ox2:.2f}" cy="{oy2:.2f}" r="3.5" class="geom-point"/>')
    lines.append(f'  <text x="{ox2 - 13:.1f}" y="{oy2 + 15:.1f}" class="geom-label">O</text>')
    lines.append(f'  <text x="{dir_x + 4:.1f}" y="50" class="geom-sub">x = a</text>')
    lines.append("</svg>\n")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    x = sp.Symbol("x")
    u = sp.Symbol("u")

    print("=== 1. Regular Polygons (Gauss-Wantzel Criterion) ===")
    for rep in tabulate_polygon_constructibility(20):
        print(" ", rep.summary)

    print("\n=== 2. Classical Problems & Galois Quartic Resolvents ===")
    samples = [
        ("Delian Cube Duplication", x**3 - 2),
        ("Angle Trisection (phi = pi/3)", 4 * x**3 - 3 * x - sp.Rational(1, 2)),
        ("Regular Heptagon Cosine (2*cos(2*pi/7))", u**3 + u**2 - 2 * u - 1),
        ("Constructible Quartic (D4)", x**4 - 2),
        ("Non-constructible Quartic (S4)", x**4 - x - 1),
        ("Euler's Number e (Hermite 1873)", sp.E),
        ("Archimedes' Constant pi (Lindemann 1882)", sp.pi),
    ]
    for label, item in samples:
        rep = analyze_constructibility(item)
        print(f"  [{label}] -> constructible={rep.is_constructible} | {rep.summary}")

    fig_dir = _REPO_ROOT / "docsrc" / "_static" / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    render_polygon_grid_svg(fig_dir / "fig_constructibility_polygons.svg")
    render_conchoid_cissoid_svg(fig_dir / "fig_conchoid_cissoid.svg")
    print("\nWrote SVGs to", fig_dir)


if __name__ == "__main__":
    main()
