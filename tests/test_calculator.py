

from src.calculator import Add


def test_add_empty_string():
    result = Add('')
    assert result == 0