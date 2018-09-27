# -*- coding: utf-8 -*-

"""Main module."""
from typing import List, Optional, Any, Union
import logging
import sys

_LOGGER = logging.getLogger(__package__)


def _config_logging(
    console_loglevel: Optional[str] = None,
    file_loglevel: Optional[str] = None,
    log_file: Optional[str] = None,
) -> None:
    """
    Configure logging

    Parameters
    ----------
    console_loglevel: str, optional
        Set console log level (Default: warning)
    file__loglevel: str, optional
        Set file log level (Default: debug)
    log_file: str, optional
        Name of log file. By default there is not fileHandler for logging
    """

    if console_loglevel is None:
        console_loglevel = logging.WARNING
    log_format: str = "%(levelname)s: %(message)s"

    logging.basicConfig(stream=sys.stderr, level=console_loglevel, format=log_format)

    if log_file:
        log_formatter: logging.Formatter = logging.Formatter(
            "[%(asctime)s:%(levelname)-7s:%(name)s.%(module)s:%(lineno)d] %(message)s"
        )
        filehandler: logging.FileHandler = logging.FileHandler(log_file)
        if not file_loglevel:
            filehandler.setLevel(logging.DEBUG)
        else:
            filehandler.setLevel(file_loglevel)
        filehandler.setFormatter(log_formatter)
        _LOGGER.addHandler(filehandler)

import logging

_LOGGER = logging.getLogger(__name__)


def main():
    """Main entry point"""
    _config_logging(log_file=".".join([__package__, "log"]))


if __name__ == "__main__":
    main()
