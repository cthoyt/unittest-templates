# -*- coding: utf-8 -*-

"""Generic test cases."""

import unittest
from typing import Any, ClassVar, Collection, Generic, Iterable, Mapping, MutableMapping, Optional, Type, TypeVar

__all__ = [
    'GenericTestCase',
    'TestsTestCase',
]

T = TypeVar('T')
X = TypeVar('X')


class GenericTestCase(Generic[T], unittest.TestCase):
    """Generic tests."""

    cls: ClassVar[Type[T]]
    kwargs: ClassVar[Optional[Mapping[str, Any]]] = None
    instance: T

    def setUp(self) -> None:
        """Set up the generic testing method."""
        self.pre_setup_hook()
        kwargs = self.kwargs or {}
        kwargs = self._pre_instantiation_hook(kwargs=dict(kwargs))
        self.instance = self.cls(**kwargs)  # type: ignore
        self.post_instantiation_hook()

    def pre_setup_hook(self) -> None:
        """Run before setUp."""

    def _pre_instantiation_hook(self, kwargs: MutableMapping[str, Any]) -> MutableMapping[str, Any]:
        """Perform actions before instantiation, potentially modyfing kwargs."""
        return kwargs

    def post_instantiation_hook(self) -> None:
        """Perform actions after instantiation."""


def get_subclasses(cls: Type[X]) -> Iterable[Type[X]]:
    """Get all subclasses.

    :param cls: The ancestor class
    :yields: Descendant classes of the ancestor class
    """
    for subclass in cls.__subclasses__():
        yield from get_subclasses(subclass)
        yield subclass


class TestsTestCase(Generic[T], unittest.TestCase):
    """A generic test for tests."""

    base_cls: ClassVar[Type[T]]
    base_test: ClassVar[Type[GenericTestCase[T]]]
    skip_cls: ClassVar[Optional[Collection[T]]] = None

    def test_testing(self):
        """Check that there is a test for all subclasses."""
        self.assertIsNotNone(getattr(self, 'base_cls'), msg=f'base_cls not set on {self.__class__}')
        to_test = set(get_subclasses(self.base_cls))
        if self.skip_cls is not None:
            to_test.difference_update(self.skip_cls)
        tested = {
            test_cls.cls
            for test_cls in get_subclasses(self.base_test)
            if hasattr(test_cls, "cls")  # avoid mid-level classes
        }
        not_tested = to_test.difference(tested)
        self.assertEqual(set(), not_tested, msg=f'Some subclasses of {self.base_cls} were not tested.')
