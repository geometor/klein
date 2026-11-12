"""Runnable demonstration of Felix Klein's Erlangen Program group hierarchy & Cayley-Klein metric.

Executes ``verify_erlangen_invariants()`` and ``verify_cayley_klein_additivity()`` in exact
rational/symbolic SymPy arithmetic and renders ``.euclid-graphic`` SVGs for Book 2 & Part II Ch. V.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
for _p in (str(_REPO_ROOT), str(_REPO_ROOT / "src")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from demos.demo_constructibility import SVG_STYLE
from geometor.klein.erlangen import (
    verify_cayley_klein_additivity,
    verify_erlangen_invariants,
)


def render_erlangen_hierarchy_svg(out_path: Path) -> None:
    """Render 4-panel diagram of Klein's transformation-group hierarchy and surviving invariants."""
    width, height = 660, 320
    lines = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" height="{height}" class="euclid-graphic" '
            f'data-graphic-id="fig_erlangen_hierarchy">'
        ),
        SVG_STYLE,
        (
            '  <text x="330" y="22" text-anchor="middle" class="geom-title">'
            "Klein’s Erlangen Hierarchy: Progressive Shedding of Geometric Invariants"
            "</text>"
        ),
    ]

    panels = [
        ("1. Principal Group", "Similarities (§ 1)", "Angles &amp; Q-ratios", 88),
        ("2. Affine Group", "Linear Shears (§ 2)", "Parallelism &amp; Area ratio", 248),
        ("3. Projective Group", "Collineations (§ 3)", "Collinear Cross-Ratio", 408),
        ("4. Reciprocal Radii", "Möbius Inversion (§ 6)", "Generalized Circles &amp; Q-CR", 568),
    ]
    for title, sub, inv, cx in panels:
        lines.append(
            f'  <rect x="{cx - 72}" y="36" width="144" height="266" rx="6" class="geom-muted"/>'
        )
        lines.append(f'  <text x="{cx}" y="54" text-anchor="middle" class="geom-label">{title}</text>')
        lines.append(f'  <text x="{cx}" y="69" text-anchor="middle" class="geom-sub">{sub}</text>')
        lines.append(f'  <text x="{cx}" y="290" text-anchor="middle" class="geom-sub">{inv}</text>')

    # Panel 1: Similar square + circle + collinear ticks
    lines.extend(
        [
            '  <polygon points="52,195 112,175 132,115 72,135" class="geom-poly-ok"/>',
            '  <circle cx="92" cy="155" r="31.6" class="geom-line"/>',
            '  <line x1="42" y1="242" x2="136" y2="215" class="geom-accent"/>',
        ]
    )
    for t in (0.0, 0.28, 0.62, 1.0):
        px, py = 42 + 94 * t, 242 - 27 * t
        lines.append(f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="3.2" class="geom-point-accent"/>')

    # Panel 2: Sheared parallelogram + sheared ellipse + collinear ticks
    lines.extend(
        [
            '  <polygon points="196,195 256,195 298,120 238,120" class="geom-poly-ok"/>',
            '  <ellipse cx="247" cy="157" rx="44" ry="25" transform="rotate(-24 247 157)" class="geom-danger"/>',
            '  <line x1="194" y1="242" x2="302" y2="215" class="geom-accent"/>',
        ]
    )
    for t in (0.0, 0.28, 0.62, 1.0):
        px, py = 194 + 108 * t, 242 - 27 * t
        lines.append(f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="3.2" class="geom-point-accent"/>')

    # Panel 3: Projective quadrilateral (non-parallel) + projective conic + cross-ratio line
    lines.extend(
        [
            '  <polygon points="358,198 448,188 462,126 382,112" class="geom-poly-ok"/>',
            '  <ellipse cx="412" cy="156" rx="38" ry="27" transform="rotate(14 412 156)" class="geom-line"/>',
            '  <line x1="354" y1="244" x2="462" y2="212" class="geom-accent"/>',
        ]
    )
    for t in (0.0, 0.20, 0.54, 1.0):
        px, py = 354 + 108 * t, 244 - 32 * t
        lines.append(f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="3.2" class="geom-point-accent"/>')

    # Panel 4: Möbius circle inversion: circle -> circle, straight line -> circle through O_inv!
    lines.extend(
        [
            '  <circle cx="585" cy="142" r="34" class="geom-assert"/>',
            '  <circle cx="556" cy="212" r="36" class="geom-accent"/>',
            '  <circle cx="520" cy="212" r="3.6" class="geom-point"/>',
            '  <text x="520" y="230" text-anchor="middle" class="geom-sub">O_inv</text>',
        ]
    )
    for ang in (-0.9, -0.25, 0.45, 1.15):
        px = 556 + 36 * math.cos(ang)
        py = 212 + 36 * math.sin(ang)
        lines.append(f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="3.2" class="geom-point-accent"/>')

    lines.append("</svg>\n")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def render_cayley_klein_svg(out_path: Path) -> None:
    """Render Klein's projective model of hyperbolic geometry inside the Absolute conic Ω = 0."""
    width, height = 520, 270
    cx, cy, rx, ry = 260.0, 148.0, 165.0, 96.0
    lines = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" height="{height}" class="euclid-graphic" '
            f'data-graphic-id="fig_cayley_klein_metric">'
        ),
        SVG_STYLE,
        (
            '  <text x="260" y="22" text-anchor="middle" class="geom-title">'
            "Cayley–Klein Projective Metric Inside the Absolute Ω = 0: d(A,B) = c log(A, B; I₁, I₂)"
            "</text>"
        ),
        f'  <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" class="geom-line"/>',
    ]

    # Geodesic chord meeting Absolute Ω = 0 at I1, I2
    th1, th2 = 2.65, 0.35
    i1x, i1y = cx + rx * math.cos(th1), cy - ry * math.sin(th1)
    i2x, i2y = cx + rx * math.cos(th2), cy - ry * math.sin(th2)
    lines.append(f'  <line x1="{i1x:.2f}" y1="{i1y:.2f}" x2="{i2x:.2f}" y2="{i2y:.2f}" class="geom-accent"/>')

    # Second Lobachevskian parallel chord through I2 and external pole
    th3 = -1.95
    i3x, i3y = cx + rx * math.cos(th3), cy - ry * math.sin(th3)
    lines.append(f'  <line x1="{i3x:.2f}" y1="{i3y:.2f}" x2="{i2x:.2f}" y2="{i2y:.2f}" class="geom-muted"/>')
    lines.append(f'  <line x1="{i3x:.2f}" y1="{i3y:.2f}" x2="{i1x:.2f}" y2="{i1y:.2f}" class="geom-muted"/>')

    pts_info = [
        (0.0, "I₁", -14, -6),
        (0.28, "A", -4, -10),
        (0.55, "B", -4, -10),
        (0.78, "C", -4, -10),
        (1.0, "I₂", 8, -6),
    ]
    for t, lbl, dx, dy in pts_info:
        px = i1x + t * (i2x - i1x)
        py = i1y + t * (i2y - i1y)
        cls = "geom-point" if t in (0.0, 1.0) else "geom-point-accent"
        lines.append(f'  <circle cx="{px:.2f}" cy="{py:.2f}" r="3.8" class="{cls}"/>')
        lines.append(f'  <text x="{px + dx:.1f}" y="{py + dy:.1f}" class="geom-label">{lbl}</text>')

    lines.append('  <text x="392" y="232" class="geom-sub">Absolute Ω = 0</text>')
    lines.append(
        '  <text x="260" y="258" text-anchor="middle" class="geom-sub">'
        "(A, B; I₁, I₂) · (B, C; I₁, I₂) = (A, C; I₁, I₂)  ⇒  d(A, B) + d(B, C) = d(A, C)"
        "</text>"
    )
    lines.append("</svg>\n")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def render_integraph_svg(out_path: Path) -> None:
    """Render Klein Part II, Ch. V (Fig. 16): Abdank-Abakanowicz's Integraph quadrature of pi."""
    width, height = 560, 290
    ox, oy, sc = 280.0, 155.0, 74.0
    lines = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" height="{height}" class="euclid-graphic" '
            f'data-graphic-id="fig_integraph_quadrature">'
        ),
        SVG_STYLE,
        (
            '  <text x="280" y="22" text-anchor="middle" class="geom-title">'
            "Abdank-Abakanowicz’s Integraph: Mechanical Quadrature of x² + y² = r² (Klein Fig. 16)"
            "</text>"
        ),
        f'  <line x1="60" y1="{oy:.1f}" x2="500" y2="{oy:.1f}" class="geom-muted"/>',
        f'  <line x1="{ox:.1f}" y1="36" x2="{ox:.1f}" y2="275" class="geom-line"/>',
        f'  <line x1="{ox - sc:.1f}" y1="36" x2="{ox - sc:.1f}" y2="275" class="geom-muted"/>',
        f'  <line x1="{ox + sc:.1f}" y1="36" x2="{ox + sc:.1f}" y2="275" class="geom-muted"/>',
        f'  <circle cx="{ox:.1f}" cy="{oy:.1f}" r="{sc:.1f}" class="geom-line"/>',
    ]

    # Integral curve Y(x) = (r^2 / 2) * arcsin(x/r) + (x / 2) * sqrt(r^2 - x^2), r = 1
    upper_branch = []
    lower_branch = []
    for i in range(-60, 61):
        u = i / 60.0
        yv = 0.5 * math.asin(u) + 0.5 * u * math.sqrt(max(0.0, 1.0 - u * u))
        px = ox + sc * u
        upper_branch.append(f"{px:.2f},{oy - sc * yv:.2f}")
        # Second half of circle returns to -pi/2 on y-axis and +pi/4 -> +pi/2
        yv_ret = math.pi / 2.0 - yv
        lower_branch.append(f"{px:.2f},{oy - sc * yv_ret:.2f}")

    lines.append(f'  <polyline points="{" ".join(upper_branch)}" class="geom-accent"/>')
    lines.append(f'  <polyline points="{" ".join(lower_branch)}" class="geom-assert"/>')

    # Intercepts on y-axis and x = r
    y_pi4 = oy - sc * (math.pi / 4.0)
    y_pi2 = oy - sc * (math.pi / 2.0)
    y_mpi4 = oy + sc * (math.pi / 4.0)
    lines.extend(
        [
            f'  <circle cx="{ox:.1f}" cy="{oy:.1f}" r="3.5" class="geom-point"/>',
            f'  <circle cx="{ox + sc:.1f}" cy="{y_pi4:.2f}" r="3.8" class="geom-point-accent"/>',
            f'  <circle cx="{ox - sc:.1f}" cy="{y_mpi4:.2f}" r="3.8" class="geom-point-accent"/>',
            f'  <circle cx="{ox:.1f}" cy="{y_pi2:.2f}" r="4.0" class="geom-point-accent"/>',
            f'  <text x="{ox + 8:.1f}" y="{y_pi2 + 4:.1f}" class="geom-label">(0, πr²/2)</text>',
            f'  <text x="{ox + sc + 8:.1f}" y="{y_pi4 + 4:.1f}" class="geom-label">(r, πr²/4)</text>',
            f'  <text x="{ox - sc - 72:.1f}" y="{y_mpi4 + 4:.1f}" class="geom-label">(−r, −πr²/4)</text>',
            "</svg>\n",
        ]
    )
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rep = verify_erlangen_invariants()
    print("=== Felix Klein's Erlangen Program Invariant Matrix ===")
    for rung in rep.rungs:
        print(f"\n[{rung.group_name}] ({rung.erlangen_section})")
        print("  Formula:", rung.transformation_formula)
        for inv_name, ok in rung.preserved.items():
            mark = "PRESERVED" if ok else "BROKEN   "
            print(f"    {inv_name:30s}: {mark} (diff = {rung.exact_differences[inv_name]})")

    ck = verify_cayley_klein_additivity()
    print("\n=== Cayley-Klein Projective Metric Additivity (Note V) ===")
    print("  Multiplicative cross-ratio residual:", ck.multiplicative_identity_residual)
    print("  Hyperbolic sample additive residual:", ck.additive_residual)

    fig_dir = _REPO_ROOT / "docsrc" / "_static" / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    render_erlangen_hierarchy_svg(fig_dir / "fig_erlangen_hierarchy.svg")
    render_cayley_klein_svg(fig_dir / "fig_cayley_klein_metric.svg")
    render_integraph_svg(fig_dir / "fig_integraph_quadrature.svg")
    print("  Wrote Erlangen & Integraph SVGs to", fig_dir)


if __name__ == "__main__":
    main()
