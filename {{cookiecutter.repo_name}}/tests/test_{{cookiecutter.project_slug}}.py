# pylint: disable=no-self-use, invalid-name, too-few-public-methods
"""Tests for {{ cookiecutter.project_slug }} package."""

import {{ cookiecutter.project_slug }}


class Test{{ cookiecutter.project_slug|replace('_', ' ')|title|replace(' ', '') }}:
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def test_000_run(self):
        """Test run"""
        # Assert false because no tests have actually been implemented.
        assert False
