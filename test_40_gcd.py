
import importlib

module = importlib.import_module("40_gcd")


def test_normal_numbers():
    assert module.gcd(12, 18) == 6


def test_coprime_numbers():
    assert module.gcd(7, 9) == 1


def test_equal_numbers():
    assert module.gcd(10, 10) == 10


def test_zero():
    assert module.gcd(15, 0) == 15


def test_negative_numbers():
    assert module.gcd(-12, 18) == 6


def test_both_zero():
    assert module.gcd(0, 0) == 0
