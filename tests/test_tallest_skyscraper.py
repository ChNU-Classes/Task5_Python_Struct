from src.tallest_skyscraper import tallest_skyscraper


def test_tallest_skyscraper1():
    assert tallest_skyscraper([
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [1, 1, 1, 1]
    ]) == 3


def test_tallest_skyscraper2():
    assert tallest_skyscraper([
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [1, 1, 1, 1]
    ]) == 4


def test_tallest_skyscraper3():
    assert tallest_skyscraper([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [1, 1, 1, 1]
    ]) == 2


def test_tallest_skyscraper4():
    assert tallest_skyscraper([
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]) == 4


def test_tallest_skyscraper5():
    assert tallest_skyscraper([
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1]
    ]) == 3


