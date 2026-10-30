
import importlib

module = importlib.import_module("38_missing_number_xor")


def test_missing_middle_number():
    assert module.find_missing_number([0, 1, 3, 4]) == 2


def test_missing_zero():
    assert module.find_missing_number([1, 2, 3]) == 0


def test_missing_last_number():
    assert module.find_missing_number([0, 1, 2, 3]) == 4


def test_single_element_range():
    assert module.find_missing_number([]) == 0
