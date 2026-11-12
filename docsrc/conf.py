"""Sphinx configuration for GEOMETOR • klein."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _src_path in (
    _WORKSPACE_ROOT / "explorer" / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _REPO_ROOT / "src",
):
    if _src_path.exists() and str(_src_path) not in sys.path:
        sys.path.insert(0, str(_src_path))
_VENV_SITE = _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages"
if _VENV_SITE.exists() and str(_VENV_SITE) not in sys.path:
    sys.path.append(str(_VENV_SITE))

from photon_platform.publish.global_conf import *

import geometor.klein as module

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "klein"
repo_name = "klein"

setup_globals(org, org_name, repo, repo_name)

project = "GEOMETOR • klein"
author = "Felix Klein • Digital Edition GEOMETOR"
copyright = (
    "1872 A. Deichert · 1893 NYMS · 1895 B. G. Teubner · 1897 Ginn & Co. · Digital Codex GEOMETOR"
)

html_static_path = ["_static"]

# Restrict AutoAPI strictly to `src/geometor` and avoid duplicate root index with modules/index.rst
autoapi_dirs = [str(_REPO_ROOT / "src" / "geometor")]
autoapi_add_toctree_entry = False
_pkg_api_index = "modules/api/geometor/klein/index.rst"
if _pkg_api_index not in exclude_patterns:
    exclude_patterns.append(_pkg_api_index)
suppress_warnings = ["autoapi.python_import_resolution"]

# Register offline-first local intersphinx inventories across the GEOMETOR sister canon
for _sister_repo in (
    "euclid",
    "elements",
    "kepler",
    "hilbert",
    "bertrand-russell",
    "hoenen",
    "lemoine",
    "petersen",
    "pappus",
    "wildberger",
    "model",
):
    _local_inv = (_WORKSPACE_ROOT / _sister_repo / "docs" / "objects.inv").resolve()
    if _local_inv.is_file():
        intersphinx_mapping[_sister_repo] = (
            f"https://geometor.github.io/{_sister_repo}",
            (str(_local_inv), None),
        )

# Retain only locally cached intersphinx inventories so offline builds emit zero network warnings
intersphinx_mapping = {
    name: target
    for name, target in intersphinx_mapping.items()
    if isinstance(target, tuple) and len(target) == 2 and target[1] is not None
}
