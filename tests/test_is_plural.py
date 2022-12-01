import pytest
from src.is_plural import is_plural


def test_is_plural1():
    assert is_plural("dishes") == True


def test_is_plural2():
    assert is_plural("dish") == False


def test_is_plural3():
    assert is_plural("brush") == False
