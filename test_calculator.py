from calculator import add


def test_empty_string_returns_0():
    assert add("") == 0

def test_single_number_returns_itself():
    assert add("5") == 5

