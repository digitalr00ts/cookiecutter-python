""" Package {{ cookiecutter.project_name }} top level """
import logging
import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("{{cookiecutter.project_slug}}").version
except Exception:  # pylint: disable=broad-except
    __version__ = None

logging.getLogger(__name__).addHandler(logging.NullHandler())
