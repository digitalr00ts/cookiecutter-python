"""{{ cookiecutter.project_name }}
{{ cookiecutter.description }}

Usage:
  {{ cookiecutter.project_slug }} (-h | --help)
  {{ cookiecutter.project_slug }} (-v | --version)

Options:
  -v --version     Show version
  -h --help     Show this screen
"""

import argparse
import logging
import sys
from typing import Optional

from . import __version__

_LOGGER = logging.getLogger(__name__)
version: Optional[str] = None


def _get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="{{ cookiecutter.project_name }} CLI Help",
        allow_abbrev=False,
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    return parser


def main():
    """ Main interface """
    parser = _get_parser()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    cli_params = parser.parse_args()

    from pprint import pprint
    pprint(cli_params)


if __name__ == "__main__":
    main()
