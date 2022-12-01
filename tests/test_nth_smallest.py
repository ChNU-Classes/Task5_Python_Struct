from src.nth_smallest import nth_smallest


def test_nth_smallest1():
    assert nth_smallest([5, 3, 2, 1, 10], 2) == 2


def test_nth_smallest2():
    assert nth_smallest([5, 3, 2, 1, 10], 6) is None


def test_nth_smallest3():
    assert nth_smallest([5, 3, 2, 1, 10], 5) == 10


def test_nth_smallest4():
    assert nth_smallest([5, 3, 2, 1, 10], 1) == 1