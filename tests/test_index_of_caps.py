from src.index_of_caps import index_of_caps


def test_index_of_caps1():
    assert index_of_caps("eRrOr") == [1, 3]


def test_index_of_caps2():
    assert index_of_caps("error") == []


def test_index_of_caps3():
    assert index_of_caps("ERROR") == [0, 1, 2, 3, 4]
