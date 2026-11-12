"""Codex apparatus, source manifest, and cross-corpus concordance utilities for ``geometor.klein``."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

__all__ = [
    "ERLANGEN_UNITS",
    "FAMOUS_PROBLEMS_UNITS",
    "REPO_ROOT",
    "SISTER_CORPORA",
    "TRACK_SUFFIXES",
    "CodexAuditReport",
    "audit_codex",
    "load_citations",
    "load_concordance",
    "load_glossary",
    "load_persons",
    "load_sources_manifest",
]

REPO_ROOT: Path = Path(__file__).resolve().parents[3]

TRACK_SUFFIXES: tuple[str, ...] = ("en", "de", "summary", "notes")

FAMOUS_PROBLEMS_UNITS: tuple[str, ...] = (
    "intro",
    "part1-ch1-square-roots",
    "part1-ch2-delian-trisection",
    "part1-ch3-cyclotomy",
    "part1-ch4-heptadecagon",
    "part1-ch5-higher-constructions",
    "part2-ch1-cantor",
    "part2-ch2-history-pi",
    "part2-ch3-hermite-e",
    "part2-ch4-lindemann-pi",
)

ERLANGEN_UNITS: tuple[str, ...] = (
    "prefatory-intro",
    "sec-01-02-principal-hierarchy",
    "sec-03-05-projective-transference",
    "sec-06-07-inversion-lie-spheres",
    "sec-08-10-higher-groups-manifolds",
    "notes-i-vii",
)

SISTER_CORPORA: tuple[str, ...] = (
    "euclid",
    "kepler",
    "hilbert",
    "bertrand-russell",
    "hoenen",
    "lemoine",
    "petersen",
    "pappus",
    "wildberger",
)


@dataclass(frozen=True)
class CodexAuditReport:
    """Structural verification report for the dual 4-track Book Codex and JSON apparatus."""

    famous_problems_units: int
    erlangen_units: int
    total_track_files: int
    missing_track_files: tuple[str, ...]
    persons_count: int
    citations_count: int
    glossary_count: int
    concordance_count: int
    linked_sister_corpora: tuple[str, ...]
    embedded_py_files_in_resources: tuple[str, ...]

    @property
    def is_valid(self) -> bool:
        """Return ``True`` iff all 64 track files and apparatus constraints pass."""
        return (
            not self.missing_track_files
            and not self.embedded_py_files_in_resources
            and self.persons_count > 0
            and self.citations_count > 0
            and self.glossary_count > 0
            and self.concordance_count > 0
        )


def _read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def load_persons(repo_root: Path = REPO_ROOT) -> dict[str, dict[str, str]]:
    """Load ``resources/persons.json``."""
    return dict(_read_json(repo_root / "resources" / "persons.json"))


def load_citations(repo_root: Path = REPO_ROOT) -> dict[str, dict[str, str]]:
    """Load ``resources/citations.json``."""
    return dict(_read_json(repo_root / "resources" / "citations.json"))


def load_glossary(repo_root: Path = REPO_ROOT) -> dict[str, dict[str, str]]:
    """Load ``resources/glossary.json``."""
    return dict(_read_json(repo_root / "resources" / "glossary.json"))


def load_concordance(repo_root: Path = REPO_ROOT) -> list[dict[str, Any]]:
    """Load ``resources/klein/concordance.json``."""
    data = _read_json(repo_root / "resources" / "klein" / "concordance.json")
    return list(data["entries"]) if isinstance(data, dict) and "entries" in data else list(data)


def load_sources_manifest(repo_root: Path = REPO_ROOT) -> dict[str, Any]:
    """Load ``resources/klein/sources_manifest.json``."""
    return dict(_read_json(repo_root / "resources" / "klein" / "sources_manifest.json"))


def audit_codex(repo_root: Path = REPO_ROOT) -> CodexAuditReport:
    """Validate 4-track parity, apparatus JSON integrity, and content/code separation."""
    docsrc = repo_root / "docsrc"
    missing: list[str] = []

    for slug in FAMOUS_PROBLEMS_UNITS:
        for suf in TRACK_SUFFIXES:
            f_path = docsrc / "famous_problems" / slug / f"{slug}-{suf}.rst"
            if not f_path.is_file():
                missing.append(str(f_path.relative_to(repo_root)))

    for slug in ERLANGEN_UNITS:
        for suf in TRACK_SUFFIXES:
            f_path = docsrc / "erlangen_program" / slug / f"{slug}-{suf}.rst"
            if not f_path.is_file():
                missing.append(str(f_path.relative_to(repo_root)))

    persons = load_persons(repo_root)
    citations = load_citations(repo_root)
    glossary = load_glossary(repo_root)
    concordance = load_concordance(repo_root)

    linked: set[str] = set()
    for entry in concordance:
        for rel in entry.get("sister_links", []):
            repo_id = rel.get("repo", "")
            if repo_id:
                linked.add(repo_id)

    res_dir = repo_root / "resources"
    py_in_res = tuple(
        sorted(str(p.relative_to(repo_root)) for p in res_dir.rglob("*.py"))
    )

    total_expected = (len(FAMOUS_PROBLEMS_UNITS) + len(ERLANGEN_UNITS)) * len(TRACK_SUFFIXES)
    return CodexAuditReport(
        famous_problems_units=len(FAMOUS_PROBLEMS_UNITS),
        erlangen_units=len(ERLANGEN_UNITS),
        total_track_files=total_expected - len(missing),
        missing_track_files=tuple(missing),
        persons_count=len(persons),
        citations_count=len(citations),
        glossary_count=len(glossary),
        concordance_count=len(concordance),
        linked_sister_corpora=tuple(sorted(linked)),
        embedded_py_files_in_resources=py_in_res,
    )
