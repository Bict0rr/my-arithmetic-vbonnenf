"""Configuration Sphinx pour my-arithmetic-vbonnenf."""

import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = "my-arithmetic-vbonnenf"
copyright = "2026, vbonnenf"
author = "vbonnenf"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

napoleon_google_docstring = False
napoleon_numpy_docstring = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "fr"

html_theme = "sphinx_rtd_theme"
