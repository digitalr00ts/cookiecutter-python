"""{{ cookiecutter.project_name }} CLI."""
import argparse
import logging
import sys
from typing import Optional

from {{ cookiecutter.project_slug }} import __version__


_LOGGER = logging.getLogger(__name__)
version: Optional[str] = None


def _create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="{{ cookiecutter.project_name }} CLI Help", allow_abbrev=False)

    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}",
    )

    return parser


def main():
    """Entrypoint for console."""
    parser = _create_parser()

    if len(sys.argv) == 1:
        sys.exit(parser.print_help())

    cli_params = parser.parse_args()

    print("Parameters recieved:")
    for param in cli_params:
        print(param)


if __name__ == "__main__":
    main()
