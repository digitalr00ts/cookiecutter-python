# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# TODO: Change paths from str to pathlib.Path

import importlib
import re
from datetime import datetime

import sphinx_rtd_theme


# importlib.metadata is implemented in Python 3.8
# Previous versions require the backport, https://pypi.org/project/importlib-metadata/
if not hasattr(importlib, "metadata"):
    setattr(importlib, "metadata", importlib.import_module("importlib_metadata"))

# -- Project information -----------------------------------------------------

metadata_ = importlib.metadata.metadata("{{- cookiecutter.project_slug -}}")
project = metadata_.get("Summary")
author = metadata_.get("Author")
copyright = f"{datetime.now().year}, {author}"

# The full version, including alpha/beta/rc tags
release = metadata_.get("Version")
# The short X.Y version
version = re.match(r"v?\d+(\.\d+)*", release)[0]


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxcontrib.mermaid",
    "sphinx_rtd_theme",
    "recommonmark",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"

# templates_path = ["_templates"]
# exclude_patterns = []

rst_epilog = "\n".join(
    [
        "\nBuild: |release|\n",
        f".. _{{ cookiecutter.project_name }}: {metadata_.get('url}')",
        f".. |project| replace:: {project}",
    ]
)

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_show_sphinx = False
html_static_path = ["_static"]
html_css_files = [
    "css/rtd_width.css",
    "css/mermaid_arch_diag.css",
]

# -- Extension configuration -------------------------------------------------

todo_include_todos = True
autosectionlabel_prefix_document = True
autodoc_default_options = {
    "members": None,
    "undoc-members": True,
    "inherited-members": True,
    "autodoc_typehints": "description",
}
mermaid_version = "8.5.0"
