""" config pytest """
import {{ cookiecutter.project_slug }}


def pytest_report_header():
    """ Additional report header """
    return f"version: {{{ cookiecutter.project_slug }}.__version__}"
