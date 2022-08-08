

from src.calculator import Add


def test_add_zero():
    result = Add('0')
    assert result == 0


def test_add_empty_string():
    result = Add('')
    assert result == 0


def test_add_two_numbers():
    result = Add('1,2')
    assert result == 3


def test_add_unknown_numbers():
    result_1 = Add('90,18,1987,1,0')
    result_2 = Add('20,3,15,6,100')
    result_3 = Add('324567,21,43,17,901')
    assert result_1 == 2096
    assert result_2 == 144
    assert result_3 == 325549


def test_add_numbers_with_newlines():
    result = Add('1\n2,3')
    assert result == 6


def test_add_numbers_exception():
    try:
        result = Add('1,\n')
        assert False
    except:
        assert True


def test_add_numbers_different_delimiters():
    result = Add("//;\n1;2")
    assert result == 3


def test_negative_numbers():
    result = Add('90,-18,1987')
    assert result == "negatives not allowed"
