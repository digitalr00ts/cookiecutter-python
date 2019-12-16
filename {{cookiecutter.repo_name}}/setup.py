#!/usr/bin/env python3
"""
Use setup.cfg to configure setuptools.
Use pyproject.toml to configure setuptools_scm.
"""

import sys

from pkg_resources import VersionConflict, require
from setuptools import setup

SETUPTOOLS_VER = "30.5.0"  # Minimum version that supports pyproject.toml

try:
    require("setuptools>=" + SETUPTOOLS_VER)
except VersionConflict:
    sys.exit(f"Error: version of setuptools is too old (<{SETUPTOOLS_VER})!")

setup(use_scm_version=True)
