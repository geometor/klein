"""GEOMETOR • klein — Dual-treatise Book Codex & exact symbolic engine for Felix Klein.

Provides exact SymPy and :mod:`geometor.model` implementations accompanying:

1. *Famous Problems of Elementary Geometry* (*Vorträge über ausgewählte Fragen der
   Elementargeometrie*, 1895; trans. W. W. Beman & D. E. Smith, 1897).
2. *A Comparative Review of Recent Researches in Geometry ("The Erlangen Program")*
   (*Vergleichende Betrachtungen über neuere geometrische Forschungen*, 1872; trans.
   M. W. Haskell, 1893).
"""

from __future__ import annotations

from .codex import (
    ERLANGEN_UNITS,
    FAMOUS_PROBLEMS_UNITS,
    SISTER_CORPORA,
    CodexAuditReport,
    audit_codex,
    load_citations,
    load_concordance,
    load_glossary,
    load_persons,
    load_sources_manifest,
)
from .constructibility import (
    ConstructibilityReport,
    analyze_constructibility,
    cubic_resolvent,
    cyclotomic_real_minimal_poly,
    is_fermat_prime,
    is_power_of_two,
    tabulate_polygon_constructibility,
)
from .erlangen import (
    CayleyKleinReport,
    ErlangenHierarchyReport,
    ErlangenRungResult,
    circular_quadrance_cross_ratio,
    is_concyclic,
    signed_area_ratio,
    verify_cayley_klein_additivity,
    verify_erlangen_invariants,
)
from .heptadecagon import (
    Gauss17GonPeriods,
    canonicalize_17,
    construct_gauss_17gon_periods,
)

__version__ = "0.1.0"

__all__ = [
    "ERLANGEN_UNITS",
    "FAMOUS_PROBLEMS_UNITS",
    "SISTER_CORPORA",
    "CayleyKleinReport",
    "CodexAuditReport",
    "ConstructibilityReport",
    "ErlangenHierarchyReport",
    "ErlangenRungResult",
    "Gauss17GonPeriods",
    "__version__",
    "analyze_constructibility",
    "audit_codex",
    "canonicalize_17",
    "circular_quadrance_cross_ratio",
    "construct_gauss_17gon_periods",
    "cubic_resolvent",
    "cyclotomic_real_minimal_poly",
    "is_concyclic",
    "is_fermat_prime",
    "is_power_of_two",
    "load_citations",
    "load_concordance",
    "load_glossary",
    "load_persons",
    "load_sources_manifest",
    "signed_area_ratio",
    "tabulate_polygon_constructibility",
    "verify_cayley_klein_additivity",
    "verify_erlangen_invariants",
]
