#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-self-use, invalid-name

"""Tests for {{ cookiecutter.project_slug }} package."""

import logging
import unittest

import {{ cookiecutter.project_slug }}


_logger: logging.Logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
