from src.filter_list import filter_list


def test_filter_list1():
    assert filter_list(["123", 123, "rtef", "4rt5", 546]) == [123, 546]


def test_filter_list2():
    assert filter_list(["123", "123", "rtef", "4rt5", "546"]) == []


def test_filter_list3():
    assert filter_list([123, 546, 54.6]) == [123, 546]


def test_filter_list4():
    assert filter_list([123, 546]) == [123, 546]
