from src.show_the_love import show_the_love


def test_show_the_love1():
    assert show_the_love([2, 100]) == [27, 75]


def test_show_the_love2():
    assert show_the_love([75, 64, 55]) == [56.25, 48.0, 89.75]


def test_show_the_love3():
    assert show_the_love([84, 94, 26, 80, 16]) == [63.0, 70.5, 19.5, 60.0, 87.0]


def test_show_the_love4():
    assert show_the_love([87, 29, 92, 57]) == [65.25, 88.0, 69.0, 42.75]


def test_show_the_love5():
    assert show_the_love([100, 26, 3, 28, 19]) == [75.0, 19.5, 46.25, 21.0, 14.25]
