from src.probability import probability


def test_probability1():
    assert probability([1, 2, 3, 4, 5, 6, 7, 8], 5) == 50.0


def test_probability2():
    assert probability([5, 6, 7, 8], 10) == 0.0


def test_probability3():
    assert probability([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 10.0


def test_probability4():
    assert probability([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 100.0
