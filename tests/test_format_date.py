from src.format_date import format_date


def test_format_date1():
    assert format_date("13/05/2021") == "2021-05-13"


def test_format_date2():
    assert format_date("01/01/2021") == "2021-01-01"


def test_format_date3():
    assert format_date("01/01/2001") == "2001-01-01"
