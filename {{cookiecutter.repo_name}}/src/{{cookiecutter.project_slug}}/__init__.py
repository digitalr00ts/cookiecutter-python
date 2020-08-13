"""{{ cookiecutter.project_name }} top level"""
import logging
from importlib import import_module

# importlib.metadata is implemented in Python 3.8
# Previous versions require the backport, https://pypi.org/project/importlib-metadata/
try:
    metadata = import_module("importlib.metadata")
except ModuleNotFoundError:
    metadata = import_module("importlib_metadata")

try:
    __version__ = metadata.version(__name__)
except metadata.PackageNotFoundError:
    __version__ = None

logging.getLogger(__name__).addHandler(logging.NullHandler())
