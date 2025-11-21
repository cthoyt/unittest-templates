"""Tests using the intermediate test class."""

from typing import Any, ClassVar

import unittest_templates
from tests import constants
from tests.constants import A, B, BaseLetter


class TestA(constants.TestLetter):
    """Tests for A."""

    cls = A


class TestB(constants.TestLetter):
    """Tests for a B."""

    cls = B
    kwargs: ClassVar[dict[str, Any]] = {"name": "hello"}


class MetaLetterTestCase(unittest_templates.MetaTestCase[BaseLetter]):
    """A meta test for letters."""

    base_cls = BaseLetter
    base_test = constants.TestLetter


class SkipperTestCase(unittest_templates.GenericTestCase[BaseLetter]):
    """A test case that should automatically skip because no ``cls`` was defined."""
