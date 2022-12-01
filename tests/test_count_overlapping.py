from src.count_overlapping import count_overlapping


def test_count_overlapping1():
    assert count_overlapping([[1, 2], [2, 3], [3, 4]], 5) == 0


def test_count_overlapping2():
    assert count_overlapping([[1, 2], [5, 6], [5, 7]], 5) == 2


def test_count_overlapping3():
    assert count_overlapping([[1, 2], [5, 8], [6, 9]], 7) == 2


def test_count_overlapping4():
    assert count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 5) == 5


def test_count_overlapping5():
    assert count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 1) == 1


