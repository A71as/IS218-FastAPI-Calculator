"""
Unit tests for calculator operations.
Tests all functions in app/operations.py
"""
import pytest

from app.operations import (
    CalculatorError,
    add,
    divide,
    modulo,
    multiply,
    power,
    subtract,
)


class TestAddition:
    """Test cases for addition operation."""

    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 5) == 15
        assert add(100, 200) == 300

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-2, -3) == -5
        assert add(-10, -5) == -15
        assert add(-100, -200) == -300

    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
        assert add(10, -10) == 0

    def test_add_zero(self):
        """Test adding zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0

    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)
        assert add(-1.5, 1.5) == 0.0


class TestSubtraction:
    """Test cases for subtraction operation."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6
        assert subtract(100, 50) == 50

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(-10, -15) == 5
        assert subtract(-100, -200) == 100

    def test_subtract_mixed_numbers(self):
        """Test subtracting mixed positive and negative numbers."""
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8
        assert subtract(0, 5) == -5

    def test_subtract_zero(self):
        """Test subtracting zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(0, 0) == 0

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        assert subtract(5.5, 2.5) == 3.0
        assert subtract(1.1, 0.1) == pytest.approx(1.0)
        assert subtract(-2.5, -1.5) == -1.0


class TestMultiplication:
    """Test cases for multiplication operation."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(4, 5) == 20
        assert multiply(10, 10) == 100

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-2, -3) == 6
        assert multiply(-4, -5) == 20
        assert multiply(-10, -10) == 100

    def test_multiply_mixed_numbers(self):
        """Test multiplying positive and negative numbers."""
        assert multiply(2, -3) == -6
        assert multiply(-4, 5) == -20
        assert multiply(-10, 10) == -100

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(0, 0) == 0
        assert multiply(-5, 0) == 0

    def test_multiply_by_one(self):
        """Test multiplying by one."""
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5
        assert multiply(-5, 1) == -5

    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        assert multiply(2.5, 4.0) == 10.0
        assert multiply(1.5, 2.0) == 3.0
        assert multiply(-2.5, 2.0) == -5.0


class TestDivision:
    """Test cases for division operation."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(6, 2) == 3
        assert divide(15, 3) == 5
        assert divide(100, 10) == 10

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide(-6, -2) == 3
        assert divide(-15, -3) == 5
        assert divide(-100, -10) == 10

    def test_divide_mixed_numbers(self):
        """Test dividing positive and negative numbers."""
        assert divide(6, -2) == -3
        assert divide(-15, 3) == -5
        assert divide(-100, 10) == -10

    def test_divide_by_one(self):
        """Test dividing by one."""
        assert divide(5, 1) == 5
        assert divide(-5, 1) == -5
        assert divide(0, 1) == 0

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0
        assert divide(0, -5) == 0
        assert divide(0, 1) == 0

    def test_divide_by_zero(self):
        """Test dividing by zero raises an error."""
        with pytest.raises(CalculatorError, match="Division by zero is not allowed"):
            divide(5, 0)

        with pytest.raises(CalculatorError, match="Division by zero is not allowed"):
            divide(-5, 0)

        with pytest.raises(CalculatorError, match="Division by zero is not allowed"):
            divide(0, 0)

    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        assert divide(7.5, 2.5) == 3.0
        assert divide(1.0, 4.0) == 0.25
        assert divide(-8.0, 2.0) == -4.0


class TestPower:
    """Test cases for power operation."""

    def test_power_positive_numbers(self):
        """Test power with positive numbers."""
        assert power(2, 3) == 8
        assert power(3, 2) == 9
        assert power(5, 2) == 25

    def test_power_with_zero_exponent(self):
        """Test power with zero exponent."""
        assert power(5, 0) == 1
        assert power(-5, 0) == 1
        assert power(0, 0) == 1

    def test_power_with_one_exponent(self):
        """Test power with exponent of one."""
        assert power(5, 1) == 5
        assert power(-5, 1) == -5
        assert power(0, 1) == 0

    def test_power_negative_base(self):
        """Test power with negative base."""
        assert power(-2, 2) == 4
        assert power(-2, 3) == -8
        assert power(-3, 2) == 9

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        assert power(2, -2) == 0.25
        assert power(4, -2) == 0.0625
        assert power(10, -1) == 0.1

    def test_power_fractional_exponent(self):
        """Test power with fractional exponent."""
        assert power(4, 0.5) == 2.0
        assert power(9, 0.5) == 3.0
        assert power(8, 1 / 3) == pytest.approx(2.0)


class TestModulo:
    """Test cases for modulo operation."""

    def test_modulo_positive_numbers(self):
        """Test modulo with positive numbers."""
        assert modulo(7, 3) == 1
        assert modulo(10, 4) == 2
        assert modulo(15, 5) == 0

    def test_modulo_negative_numbers(self):
        """Test modulo with negative numbers."""
        assert modulo(-7, 3) == 2
        assert modulo(7, -3) == -2
        assert modulo(-7, -3) == -1

    def test_modulo_by_one(self):
        """Test modulo by one."""
        assert modulo(5, 1) == 0
        assert modulo(-5, 1) == 0
        assert modulo(0, 1) == 0

    def test_modulo_zero(self):
        """Test modulo with zero dividend."""
        assert modulo(0, 5) == 0
        assert modulo(0, -5) == 0

    def test_modulo_by_zero(self):
        """Test modulo by zero raises an error."""
        with pytest.raises(CalculatorError, match="Modulo by zero is not allowed"):
            modulo(5, 0)

        with pytest.raises(CalculatorError, match="Modulo by zero is not allowed"):
            modulo(-5, 0)

        with pytest.raises(CalculatorError, match="Modulo by zero is not allowed"):
            modulo(0, 0)

    def test_modulo_floats(self):
        """Test modulo with floating point numbers."""
        assert modulo(7.5, 2.5) == pytest.approx(0.0)
        assert modulo(8.5, 3.0) == pytest.approx(2.5)
        assert modulo(10.7, 3.2) == pytest.approx(1.1, abs=1e-10)


class TestErrorHandling:
    """Test cases for error handling."""

    def test_calculator_error_type(self):
        """Test that CalculatorError is properly raised."""
        with pytest.raises(CalculatorError):
            divide(1, 0)

        with pytest.raises(CalculatorError):
            modulo(1, 0)

    def test_calculator_error_message(self):
        """Test that error messages are descriptive."""
        with pytest.raises(CalculatorError) as exc_info:
            divide(5, 0)
        assert "Division by zero is not allowed" in str(exc_info.value)

        with pytest.raises(CalculatorError) as exc_info:
            modulo(5, 0)
        assert "Modulo by zero is not allowed" in str(exc_info.value)
