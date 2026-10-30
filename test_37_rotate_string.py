
import importlib

module = importlib.import_module("37_rotate_string")


def test_normal_rotation():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_zero_rotation():
    assert module.rotate_string("hello", 0) == "hello"


def test_rotation_equal_to_length():
    assert module.rotate_string("hello", 5) == "hello"


def test_large_rotation():
    assert module.rotate_string("hello", 7) == "lohel"


def test_empty_string():
    assert module.rotate_string("", 3) == ""
