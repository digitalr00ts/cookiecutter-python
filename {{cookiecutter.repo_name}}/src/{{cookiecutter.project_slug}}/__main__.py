"""Module interface for {{ cookiecutter.project_name }}"""
import logging
import sys


def main():
    """Module entry point"""
    module_args = sys.argv[1:]
    logging.debug("Module arguments received: %s", module_args)
    {{ cookiecutter.project_slug }}.cli.main()


if __name__ == "__main__":
    main()
