"""Module interface for {{ cookiecutter.project_name }}."""
import logging
import sys

from {{ cookiecutter.project_slug }}.cli import main as cli


def main():
    """Entrypoint to aoad as Python module."""
    module_args = sys.argv[1:]
    logging.debug("Module arguments received: %s", module_args)
    cli()


if __name__ == "__main__":
    main()
