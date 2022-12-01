from src.stutter import stutter


def test_stutter1():
    assert stutter("impossible") == "im... im... impossible?"


def test_stutter2():
    assert stutter("fantastic") == "fa... fa... fantastic?"
