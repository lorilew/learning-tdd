

from src.calculator import Add


def test_add_empty_string():
    result = Add('0')
    assert result == 0