from calculator import add


def test_empty_string_returns_0():
    assert add("") == 0

def test_single_number_returns_itself():
    assert add("5") == 5

def test_two_numbers_comma_separated():
    assert add("1,2") == 3

def test_new_line_separated_numbers():
    assert add("1\n2,3") == 6

def test_custom_delimiter_semicolon():
    assert add("//;\n1;2") == 3
