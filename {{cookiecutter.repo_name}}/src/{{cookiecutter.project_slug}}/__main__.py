""" __main__ to load package {{ cookiecutter.project_name }} as module """
import logging
import sys


def main():
    """
    Main entry point.
    """
    module_args = sys.argv[1:]
    logging.debug("Module arguments received: %s", module_args)
    {{ cookiecutter.project_slug }}.cli.main()


if __name__ == "__main__":
    main()
