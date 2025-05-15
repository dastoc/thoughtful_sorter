from unittest import mock
import pytest
import sorter as sorter
from sorter import validate_inputs, is_bulky, is_heavy, sort
from exceptions import InvalidDimensionError, InvalidInputTypeError

# Test cases for the auxiliar functions
def test_validate_inputs_valid():
    # Should not raise any exceptions
    validate_inputs(10, 20, 30, 5)

def test_validate_inputs_negative_dimension():
    with pytest.raises(InvalidDimensionError):
        validate_inputs(-10, 20, 30, 5)

def test_validate_inputs_zero_dimension():
    with pytest.raises(InvalidDimensionError):
        validate_inputs(0, 20, 30, 5)

def test_validate_inputs_negative_mass():
    with pytest.raises(InvalidDimensionError):
        validate_inputs(10, 20, 30, -1)

def test_validate_inputs_non_numeric():
    with pytest.raises(InvalidInputTypeError):
        validate_inputs("10", 20, 30, 5)

def test_is_bulky_by_volume():
    assert is_bulky(100, 100, 100) is True  # 1,000,000 cm³

def test_is_bulky_by_dimension():
    assert is_bulky(151, 10, 10) is True

def test_is_not_bulky():
    assert is_bulky(50, 50, 50) is False  # 125,000 cm³

def test_is_heavy_true():
    assert is_heavy(20) is True
    assert is_heavy(25) is True

def test_is_heavy_false():
    assert is_heavy(19.9) is False

# Test cases with mock
def test_sort_rejected_with_mock():
    with mock.patch("thoughtful_sorter.sorter.validate_inputs"), \
         mock.patch("thoughtful_sorter.sorter.is_bulky", return_value=True), \
         mock.patch("thoughtful_sorter.sorter.is_heavy", return_value=True):
        assert sort(1, 1, 1, 1) == "REJECTED"

def test_sort_special_bulky_with_mock():
    with mock.patch("thoughtful_sorter.sorter.validate_inputs"), \
         mock.patch("thoughtful_sorter.sorter.is_bulky", return_value=True), \
         mock.patch("thoughtful_sorter.sorter.is_heavy", return_value=False):
        assert sort(1, 1, 1, 1) == "SPECIAL"

def test_sort_special_heavy_with_mock():
    with mock.patch("thoughtful_sorter.sorter.validate_inputs"), \
         mock.patch("thoughtful_sorter.sorter.is_bulky", return_value=False), \
         mock.patch("thoughtful_sorter.sorter.is_heavy", return_value=True):
        assert sort(1, 1, 1, 1) == "SPECIAL"

def test_sort_standard_with_mock():
    with mock.patch("thoughtful_sorter.sorter.validate_inputs"), \
         mock.patch("thoughtful_sorter.sorter.is_bulky", return_value=False), \
         mock.patch("thoughtful_sorter.sorter.is_heavy", return_value=False):
        assert sort(1, 1, 1, 1) == "STANDARD"

# Test cases for the sort function
def test_standard_package():
    assert sort(10, 20, 30, 5) == "STANDARD"

def test_heavy_package():
    assert sort(10, 20, 30, 25) == "SPECIAL"

def test_bulky_package_by_volume():
    assert sort(200, 100, 50, 10) == "SPECIAL"

def test_bulky_package_by_dimension():
    assert sort(150, 10, 10, 10) == "SPECIAL"

def test_rejected_package():
    assert sort(200, 100, 50, 25) == "REJECTED"

def test_invalid_negative_dimension():
    with pytest.raises(InvalidDimensionError):
        sort(-10, 20, 30, 5)

def test_invalid_zero_dimension():
    with pytest.raises(InvalidDimensionError):
        sort(0, 20, 30, 5)

def test_invalid_non_numeric_input():
    with pytest.raises(InvalidInputTypeError):
        sort("10", 20, 30, 5)

def test_edge_case_exact_thresholds():
    assert sort(100, 100, 100, 20) == "REJECTED"  # Exactly heavy and bulky (volume = 1,000,000)
    assert sort(150, 10, 10, 10) == "SPECIAL"   # Exactly bulky by dimension
    assert sort(100, 100, 100, 19.999) == "SPECIAL"  # # Bulky (volume = 1,000,000) but not heavy
    assert sort(100, 100, 99.999, 10) == "STANDARD"  # Just below bulky volume

def test_floating_point_precision():
    assert sort(100.1, 100.1, 99.9, 10) == "SPECIAL"  # Volume slightly above threshold
