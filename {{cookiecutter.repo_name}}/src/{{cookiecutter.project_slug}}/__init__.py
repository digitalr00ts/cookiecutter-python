"""{{ cookiecutter.project_name }} top level"""
import importlib
import logging

# importlib.metadata is implemented in Python 3.8
# Previous versions require the backport, https://pypi.org/project/importlib-metadata/
if not hasattr(importlib, "metadata"):
    setattr(importlib, "metadata", importlib.import_module("importlib_metadata"))

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = None

logging.getLogger(__name__).addHandler(logging.NullHandler())
