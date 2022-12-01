from src.pops import pops


def test_pops1():
    assert pops([0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0]) == [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]


def test_pops2():
    assert pops([0, 0, 0, 0, 4, 0, 0, 0, 0]) == [0, 1, 2, 3, 4, 3, 2, 1, 0]


def test_pops3():
    assert pops([0, 0, 0, 3, 0, 0, 0]) == [0, 1, 2, 3, 2, 1, 0]


def test_pops4():
    assert pops([0, 0, 2, 0, 0]) == [0, 1, 2, 1, 0]


def test_pops5():
    assert pops([0]) == [0]