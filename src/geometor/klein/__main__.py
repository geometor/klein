"""CLI entry point for ``geometor-klein``."""

from __future__ import annotations

import argparse
import json

from . import __version__
from .codex import audit_codex
from .constructibility import analyze_constructibility, tabulate_polygon_constructibility
from .erlangen import verify_cayley_klein_additivity, verify_erlangen_invariants
from .heptadecagon import construct_gauss_17gon_periods


def main(argv: list[str] | None = None) -> int:
    """Run ``geometor-klein`` symbolic diagnostics and codex audits."""
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--json",
        action="store_true",
        default=False,
        help="Emit structured JSON output.",
    )

    parser = argparse.ArgumentParser(
        prog="geometor-klein",
        description="Felix Klein dual-treatise Book Codex & exact symbolic engine.",
        parents=[common],
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command")

    p_poly = sub.add_parser(
        "polygons",
        parents=[common],
        help="Tabulate regular n-gon constructibility",
    )
    p_poly.add_argument("--max-n", type=int, default=24)

    p_17 = sub.add_parser(
        "heptadecagon",
        parents=[common],
        help="Verify Gauss-Staudt-Klein 17-gon periods & model",
    )
    p_17.add_argument("--periods-only", action="store_true")

    sub.add_parser(
        "erlangen",
        parents=[common],
        help="Verify Erlangen Program group hierarchy invariants",
    )
    sub.add_parser(
        "audit",
        parents=[common],
        help="Audit 4-track bilingual codex & apparatus files",
    )

    args = parser.parse_args(argv)
    cmd = args.command or "erlangen"

    if cmd == "polygons":
        reports = tabulate_polygon_constructibility(args.max_n)
        if args.json:
            payload = [
                {
                    "target": rep.target,
                    "is_constructible": rep.is_constructible,
                    "euler_totient": rep.euler_totient,
                    "tower_depth": rep.tower_depth,
                    "fermat_primes": list(rep.fermat_primes),
                    "non_fermat_primes": list(rep.non_fermat_primes),
                    "repeated_odd_primes": list(rep.repeated_odd_primes),
                    "summary": rep.summary,
                }
                for rep in reports
            ]
            print(json.dumps(payload, indent=2))
        else:
            for rep in reports:
                mark = "YES" if rep.is_constructible else "NO "
                print(f"[{mark}] {rep.summary}")
        return 0

    if cmd == "heptadecagon":
        res = construct_gauss_17gon_periods(inscribe_polygon=not args.periods_only)
        if args.json:
            payload_17 = {
                "circles_count": len(res.model.circles),
                "vertices_count": len(res.vertices),
                "primitive_root": res.primitive_root,
                "x1": str(res.x1),
                "x2": str(res.x2),
                "y1": str(res.y1),
                "y2": str(res.y2),
                "y3": str(res.y3),
                "y4": str(res.y4),
                "z1": str(res.z_periods[0]),
                "cos_2pi_17": str(res.cos_2pi_17),
                "radical_dependence_residual": str(res.radical_dependence_residual),
            }
            print(json.dumps(payload_17, indent=2))
        else:
            print(f"Circles in model: {len(res.model.circles)} (Poncelet-Steiner fixed C0)")
            print(f"Vertices constructed: {len(res.vertices)}")
            print(f"x1 = {res.x1}")
            print(f"y1 = {res.y1}")
            print(f"y4 = {res.y4}")
            print(f"cos(2*pi/17) = {res.cos_2pi_17}")
        return 0

    if cmd == "audit":
        rep = audit_codex()
        payload_audit = {
            "is_valid": rep.is_valid,
            "famous_problems_units": rep.famous_problems_units,
            "erlangen_units": rep.erlangen_units,
            "total_track_files": rep.total_track_files,
            "missing_track_files": list(rep.missing_track_files),
            "persons_count": rep.persons_count,
            "citations_count": rep.citations_count,
            "glossary_count": rep.glossary_count,
            "concordance_count": rep.concordance_count,
            "linked_sister_corpora": list(rep.linked_sister_corpora),
        }
        print(json.dumps(payload_audit, indent=2))
        return 0 if rep.is_valid else 1

    # Default: erlangen + quick constructibility check
    erl = verify_erlangen_invariants()
    ck = verify_cayley_klein_additivity()
    rep17 = analyze_constructibility(17)
    rep7 = analyze_constructibility(7)
    if args.json:
        payload_erl = {
            "rungs": {
                rung.group_key: {
                    "group_name": rung.group_name,
                    "erlangen_section": rung.erlangen_section,
                    "preserved": rung.preserved,
                }
                for rung in erl.rungs
            },
            "cayley_klein_multiplicative_residual": str(ck.multiplicative_identity_residual),
            "cayley_klein_additive_residual": str(ck.additive_residual),
            "heptadecagon_constructible": rep17.is_constructible,
            "heptagon_constructible": rep7.is_constructible,
        }
        print(json.dumps(payload_erl, indent=2))
        return 0

    for rung in erl.rungs:
        kept = [k for k, v in rung.preserved.items() if v]
        print(f"{rung.group_name} ({rung.erlangen_section}): preserves {kept}")
    print(f"Cayley-Klein additivity residual: {ck.multiplicative_identity_residual}")
    print(rep17.summary)
    print(rep7.summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
