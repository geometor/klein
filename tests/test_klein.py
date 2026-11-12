"""Comprehensive exact symbolic & Book Codex unit test suite for ``geometor.klein``."""

from __future__ import annotations

import json
import re

import pytest
import sympy as sp
from geometor.model.invariants import quadrance

from geometor.klein import (
    ERLANGEN_UNITS,
    FAMOUS_PROBLEMS_UNITS,
    SISTER_CORPORA,
    __version__,
    analyze_constructibility,
    audit_codex,
    canonicalize_17,
    construct_gauss_17gon_periods,
    cubic_resolvent,
    cyclotomic_real_minimal_poly,
    is_fermat_prime,
    is_power_of_two,
    load_citations,
    load_concordance,
    load_glossary,
    load_persons,
    load_sources_manifest,
    tabulate_polygon_constructibility,
    verify_cayley_klein_additivity,
    verify_erlangen_invariants,
)
from geometor.klein.__main__ import main
from geometor.klein.codex import REPO_ROOT, TRACK_SUFFIXES


def _extract_role_keys(rst_text: str, role: str) -> list[str]:
    """Extract target keys from ``:<role>:`label <key>``` or ``:<role>:`key```."""
    pattern = re.compile(rf":{role}:`([^`]+)`")
    keys: list[str] = []
    for raw in pattern.findall(rst_text):
        m = re.search(r"<([^>]+)>\s*$", raw)
        key = m.group(1).strip() if m else raw.strip()
        keys.append(key)
    return keys


def test_codex_audit_and_apparatus_integrity() -> None:
    """Verify all 64 4-track RST files, zero embedded .py in resources/, and apparatus keys."""
    assert __version__ == "0.1.0"
    rep = audit_codex()
    assert rep.is_valid is True
    assert rep.famous_problems_units == 10
    assert rep.erlangen_units == 6
    assert rep.total_track_files == 64
    assert rep.missing_track_files == ()
    assert rep.embedded_py_files_in_resources == ()
    assert set(rep.linked_sister_corpora) == set(SISTER_CORPORA)

    persons = load_persons()
    citations = load_citations()
    glossary = load_glossary()
    concordance = load_concordance()
    manifest = load_sources_manifest()

    assert len(persons) >= 50
    assert len(citations) >= 30
    assert len(glossary) >= 20
    assert len(concordance) >= 8
    assert "treatises" in manifest or "sources" in manifest or len(manifest) > 0

    docsrc = REPO_ROOT / "docsrc"

    # Verify every Book 1 and Book 2 track file has :layout: book and exact anchor
    for slug in FAMOUS_PROBLEMS_UNITS:
        for suf in TRACK_SUFFIXES:
            p = docsrc / "famous_problems" / slug / f"{slug}-{suf}.rst"
            txt = p.read_text(encoding="utf-8")
            assert ":layout: book" in txt, f"Missing :layout: book in {p}"
            assert f".. _fp-{slug}-{suf}:" in txt, f"Missing anchor .. _fp-{slug}-{suf}: in {p}"

    for slug in ERLANGEN_UNITS:
        for suf in TRACK_SUFFIXES:
            p = docsrc / "erlangen_program" / slug / f"{slug}-{suf}.rst"
            txt = p.read_text(encoding="utf-8")
            assert ":layout: book" in txt, f"Missing :layout: book in {p}"
            assert f".. _ep-{slug}-{suf}:" in txt, f"Missing anchor .. _ep-{slug}-{suf}: in {p}"

    # Verify every :person:, :cite:, and :term: across all RST files resolves cleanly
    for rst_file in sorted(docsrc.rglob("*.rst")):
        content = rst_file.read_text(encoding="utf-8")
        for p_key in _extract_role_keys(content, "person"):
            assert p_key in persons, f"Unknown :person: key '{p_key}' in {rst_file}"
        for c_key in _extract_role_keys(content, "cite"):
            assert c_key in citations, f"Unknown :cite: key '{c_key}' in {rst_file}"
        for t_key in _extract_role_keys(content, "term"):
            assert t_key in glossary, f"Unknown :term: key '{t_key}' in {rst_file}"


def test_constructibility_polygons_and_fermat_primes() -> None:
    """Test Gauss-Wantzel regular polygon classifier and Fermat primes F_0..F_4."""
    assert is_power_of_two(1) == (True, 0)
    assert is_power_of_two(16) == (True, 4)
    assert is_power_of_two(6) == (False, None)
    assert is_power_of_two(0) == (False, None)

    expected_fermat = [(3, 0), (5, 1), (17, 2), (257, 3), (65537, 4)]
    for fp, mu in expected_fermat:
        assert is_fermat_prime(fp) == (True, mu)

    for non_fp in (2, 4, 7, 9, 11, 13, 19, 25, 641):
        assert is_fermat_prime(non_fp) == (False, None)

    for n_yes in (3, 4, 5, 6, 8, 10, 12, 15, 16, 17, 20, 24, 51, 85, 255, 257):
        rep = analyze_constructibility(n_yes)
        assert rep.is_constructible is True, f"Expected {n_yes}-gon constructible"
        assert rep.is_power_of_two is True

    for n_no in (7, 9, 11, 13, 14, 18, 19, 21, 22, 25, 27):
        rep = analyze_constructibility(n_no)
        assert rep.is_constructible is False, f"Expected {n_no}-gon non-constructible"
        assert rep.galois_obstruction is not None

    # Repeated odd Fermat prime power (n = 9 = 3^2, n = 25 = 5^2)
    rep9 = analyze_constructibility(9)
    assert rep9.repeated_odd_primes == (3,)

    u = sp.Symbol("u")
    assert cyclotomic_real_minimal_poly(7, u) == sp.Poly(u**3 + u**2 - 2 * u - 1, u, domain="QQ")
    assert cyclotomic_real_minimal_poly(9, u) == sp.Poly(u**3 - 3 * u + 1, u, domain="QQ")

    table = tabulate_polygon_constructibility(18)
    assert len(table) == 16
    constructible_ns = [int(r.target.split()[1].split("-")[0]) for r in table if r.is_constructible]
    assert constructible_ns == [3, 4, 5, 6, 8, 10, 12, 15, 16, 17]


def test_constructibility_polynomials_and_transcendentals() -> None:
    """Test Delian cubic, angle-trisection cubic, D_4 vs. S_4 quartics, and e, pi."""
    x = sp.Symbol("x")

    # Irreducible cubics (Delian x^3 - 2 and trisection x^3 - 3x - 1)
    delian = analyze_constructibility(x**3 - 2)
    assert delian.is_constructible is False
    assert delian.degree == 3

    trisect = analyze_constructibility(x**3 - 3 * x - 1)
    assert trisect.is_constructible is False
    assert trisect.degree == 3

    # Constructible D_4 quartic x^4 - 2 (reducible cubic resolvent t^3 + 8t)
    q_yes = sp.Poly(x**4 - 2, x, domain="QQ")
    res_yes = cubic_resolvent(q_yes)
    assert any(fac.degree() == 1 for fac, _ in res_yes.factor_list()[1])
    rep_q_yes = analyze_constructibility(q_yes)
    assert rep_q_yes.is_constructible is True
    assert rep_q_yes.tower_depth == 2

    # Non-constructible S_4 quartic x^4 - x - 1 (irreducible cubic resolvent t^3 + 4t + 1)
    q_no = sp.Poly(x**4 - x - 1, x, domain="QQ")
    res_no = cubic_resolvent(q_no)
    assert all(fac.degree() != 1 for fac, _ in res_no.factor_list()[1])
    rep_q_no = analyze_constructibility(q_no)
    assert rep_q_no.is_constructible is False
    assert rep_q_no.galois_obstruction is not None
    assert "cubic resolvent" in rep_q_no.galois_obstruction

    # Closed-form nested square roots & golden ratio
    phi = (1 + sp.sqrt(5)) / 2
    assert analyze_constructibility(phi).is_constructible is True
    assert analyze_constructibility(sp.sqrt(2 + sp.sqrt(3))).is_constructible is True
    assert analyze_constructibility(sp.Integer(2) ** sp.Rational(1, 3)).is_constructible is False

    # Hermite (1873) & Lindemann (1882) transcendentals
    rep_e = analyze_constructibility(sp.E)
    assert rep_e.kind == "transcendental"
    assert rep_e.is_constructible is False
    assert "Hermite" in (rep_e.galois_obstruction or "")

    rep_pi = analyze_constructibility(sp.pi)
    assert rep_pi.kind == "transcendental"
    assert rep_pi.is_constructible is False
    assert "Lindemann" in (rep_pi.galois_obstruction or "")


def test_erlangen_hierarchy_and_cayley_klein() -> None:
    """Verify exact invariant preservation/breaking across Klein's 4 transformation groups."""
    erl = verify_erlangen_invariants()
    by_key = erl.by_key()
    assert set(by_key) == {
        "principal_similarity",
        "affine_shear",
        "projective_homography",
        "moebius_circle_inversion",
    }

    # 1. Principal Group (Euclidean similarities): scales quadrance, preserves everything else
    p_sim = by_key["principal_similarity"].preserved
    assert p_sim["quadrance_ab"] is False
    assert p_sim["quadrance_ratio"] is True
    assert p_sim["angle_spread"] is True
    assert p_sim["parallelism"] is True
    assert p_sim["division_ratio"] is True
    assert p_sim["area_ratio"] is True
    assert p_sim["collinearity"] is True
    assert p_sim["collinear_cross_ratio"] is True
    assert p_sim["generalized_circles"] is True
    assert p_sim["circular_quadrance_cross_ratio"] is True

    # 2. Affine shear: breaks spreads & circles, preserves parallelism, division & area ratios
    p_aff = by_key["affine_shear"].preserved
    assert p_aff["quadrance_ratio"] is False
    assert p_aff["angle_spread"] is False
    assert p_aff["generalized_circles"] is False
    assert p_aff["parallelism"] is True
    assert p_aff["division_ratio"] is True
    assert p_aff["area_ratio"] is True
    assert p_aff["collinearity"] is True
    assert p_aff["collinear_cross_ratio"] is True

    # 3. Projective homography: breaks parallelism & division ratios, preserves collinearity & CR
    p_proj = by_key["projective_homography"].preserved
    assert p_proj["parallelism"] is False
    assert p_proj["division_ratio"] is False
    assert p_proj["area_ratio"] is False
    assert p_proj["collinearity"] is True
    assert p_proj["collinear_cross_ratio"] is True

    # 4. Moebius circle inversion: breaks collinearity, preserves generalized circles & 4-pt Q-CR
    p_inv = by_key["moebius_circle_inversion"].preserved
    assert p_inv["collinearity"] is False
    assert p_inv["generalized_circles"] is True
    assert p_inv["circular_quadrance_cross_ratio"] is True

    # Cayley-Klein projective metric additivity
    ck = verify_cayley_klein_additivity()
    assert ck.multiplicative_identity_residual == 0
    assert ck.additive_residual == 0


def test_heptadecagon_exact_single_circle_model() -> None:
    """Verify Gauss's 17-gon periods and Poncelet-Steiner 1-circle Model with 0 Floats."""
    res = construct_gauss_17gon_periods(inscribe_polygon=True, add_sides=True)

    # 1. Exact Poncelet-Steiner single-circle count and 17 vertices
    assert len(res.model.circles) == 1
    assert len(res.vertices) == 17
    assert res.radical_dependence_residual == 0

    # 2. Strict prohibition of sp.Float across the entire geometor.model.Model
    for elem in res.model:
        assert not elem.atoms(sp.Float), f"Found floating-point atom in model element {elem}"

    # 3. Exact satisfaction of Klein's 4 quadratic equations (xi), (eta), (eta'), (zeta)
    assert sp.simplify(res.eq_xi.eval(res.x1)) == 0
    assert sp.simplify(res.eq_xi.eval(res.x2)) == 0
    assert sp.simplify(res.eq_eta.eval(res.y1)) == 0
    assert sp.simplify(res.eq_eta.eval(res.y2)) == 0
    assert sp.simplify(res.eq_eta_prime.eval(res.y4)) == 0
    assert sp.simplify(res.eq_eta_prime.eval(res.y3)) == 0
    assert canonicalize_17(res.eq_zeta.eval(res.z_periods[0])) == 0
    assert canonicalize_17(res.eq_zeta.eval(res.z_periods[1])) == 0

    # 4. Klein's inequality chain (§ 5): y3 < y2 < y4 < y1 and x2 < x1
    assert float(res.x2.evalf()) < float(res.x1.evalf())
    assert (
        float(res.y3.evalf())
        < float(res.y2.evalf())
        < float(res.y4.evalf())
        < float(res.y1.evalf())
    )

    # 5. All 17 vertices lie exactly on C0: x^2 + y(y - 2) = 0 with equal side quadrances
    side_q0 = canonicalize_17(quadrance(res.vertices[0], res.vertices[1]))
    assert side_q0 != 0
    for k, v_pt in enumerate(res.vertices):
        circle_res = canonicalize_17(v_pt.x**2 + v_pt.y * (v_pt.y - 2))
        assert circle_res == 0, f"Vertex V{k} does not lie exactly on C0"
        v_nxt = res.vertices[(k + 1) % 17]
        q_k = canonicalize_17(quadrance(v_pt, v_nxt) - side_q0)
        assert q_k == 0, f"Side {k} quadrance differs from Side 0 quadrance"


def test_cli_entrypoints_json(capsys: pytest.CaptureFixture[str]) -> None:
    """Test all CLI subcommands of ``geometor-klein`` with ``--json``."""
    rc_poly = main(["polygons", "--max-n", "18", "--json"])
    assert rc_poly == 0
    poly_data = json.loads(capsys.readouterr().out)
    assert len(poly_data) == 16
    assert poly_data[14]["target"] == "regular 17-gon"
    assert poly_data[14]["is_constructible"] is True

    rc_17 = main(["heptadecagon", "--periods-only", "--json"])
    assert rc_17 == 0
    h17_data = json.loads(capsys.readouterr().out)
    assert h17_data["circles_count"] == 1
    assert h17_data["vertices_count"] == 3
    assert h17_data["radical_dependence_residual"] == "0"

    rc_erl = main(["erlangen", "--json"])
    assert rc_erl == 0
    erl_data = json.loads(capsys.readouterr().out)
    assert erl_data["cayley_klein_multiplicative_residual"] == "0"
    assert erl_data["heptadecagon_constructible"] is True
    assert erl_data["heptagon_constructible"] is False

    rc_aud = main(["audit"])
    assert rc_aud == 0
    aud_data = json.loads(capsys.readouterr().out)
    assert aud_data["is_valid"] is True
    assert aud_data["total_track_files"] == 64
