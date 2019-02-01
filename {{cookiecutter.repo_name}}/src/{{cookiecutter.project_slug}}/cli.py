"""{{ cookiecutter.project_name }}
{{ cookiecutter.description }}

Usage:
  {{ cookiecutter.project_slug }} (-h | --help)
  {{ cookiecutter.project_slug }} (-v | --version)

Options:
  -v --version     Show version
  -h --help     Show this screen
"""

import logging
from typing import Optional

import pkg_resources

from docopt import docopt

version: Optional[str] = None

try:
    version = pkg_resources.get_distribution(__package__).version
except pkg_resources.DistributionNotFound:
    version = None


def main():
    arguments = docopt(__doc__, version=version, options_first=False)
    logging.info("Arguments received: %s", arguments)


if __name__ == "__main__":
    main()
