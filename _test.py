import pytest
from app import calculate


def test_addition():
    assert calculate(2, 3, "Addition") == 5


def test_subtraction():
    assert calculate(10, 4, "Subtraction") == 6


def test_multiplication():
    assert calculate(3, 5, "Multiplication") == 15


def test_division():
    assert calculate(10, 2, "Division") == 5


def test_division_by_zero():
    assert calculate(10, 0, "Division") == "Error: Division by zero"


def test_invalid_operation():
    assert calculate(2, 3, "Modulo") == "Invalid operation"
