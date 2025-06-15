import pytest
from calculator import add

def test_empty_string():
    assert add("") == 0

def test_single_number():
    assert add("1") == 1
    assert add("42") == 42

def test_two_numbers():
    assert add("1,2") == 3
    assert add("10,20") == 30

def test_multiple_numbers():
    assert add("1,2,3,4,5") == 15
    assert add("10,20,30") == 60

def test_newline_delimiter():
    assert add("1\n2,3") == 6
    assert add("1\n2\n3") == 6

def test_custom_delimiter():
    assert add("//;\n1;2") == 3
    assert add("//.\n1.2.3") == 6

def test_negative_numbers():
    with pytest.raises(ValueError) as exc_info:
        add("-1,2,-3")
    assert "negative numbers not allowed: -1,-3" in str(exc_info.value)

def test_mixed_delimiters():
    assert add("1,2\n3") == 6
    assert add("//;\n1;2\n3") == 6