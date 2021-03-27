# -*- coding: utf-8 -*-

"""Minimal example classes and test cases."""

import unittest_templates


class BaseLetter:
    """A base class."""


class A(BaseLetter):
    """A minimum child class."""


class B(BaseLetter):
    """A child class with a non-trivial `__init__`."""

    def __init__(self, name):
        """Initialize the class.

        :param name: A name
        """
        self.name = name


class TestLetter(unittest_templates.GenericTestCase[BaseLetter]):
    """A generic test class for letters."""

    def test_instance(self):
        """Test that the letter is a letter."""
        self.assertIsInstance(self.instance, BaseLetter)
