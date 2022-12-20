import pytest
# from package_name.module_name import function_name
from series.series import fibonacci, lucas, sum_series


# pytest tests must start with "test_"

def fibonacci_exists_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def fibonacci_exists_two():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_lucas_exists_one():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_exists_two():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_sum_series_exists_one():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_series_exists_two():
    actual = sum_series(1)
    expected = 1
    assert actual == expected




