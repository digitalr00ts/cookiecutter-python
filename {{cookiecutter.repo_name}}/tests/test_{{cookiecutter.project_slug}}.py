# pylint: disable=no-self-use, too-few-public-methods
"""Tests for `{{ cookiecutter.project_slug }}` package."""
import pytest

import {{ cookiecutter.project_slug }}


class Test{{ cookiecutter.project_slug|replace('_', ' ')|title|replace(' ', '') }}:
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def test_000_run(self):
        """First Test run."""
        pytest.fail("No tests have been implemented.")
