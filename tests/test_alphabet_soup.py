from src.alphabet_soup import alphabet_soup


def test_alphabet_soup1():
    assert alphabet_soup("javascript") == "aacijprstv"


def test_alphabet_soup2():
    assert alphabet_soup("python") == "hnopty"


def test_alphabet_soup3():
    assert alphabet_soup("") == ""


def test_alphabet_soup4():
    assert alphabet_soup("qwazqwaz") == "aaqqwwzz"
