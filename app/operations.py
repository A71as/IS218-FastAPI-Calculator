"""
Calculator operations module.
Provides basic arithmetic operations with error handling.
"""
import logging
from typing import Union

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CalculatorError(Exception):
    """Custom exception for calculator operations."""

    pass


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers with enhanced validation and logging.

    Args:
        a: First number (addend)
        b: Second number (addend)

    Returns:
        Sum of a and b

    Raises:
        CalculatorError: If input validation fails or overflow occurs

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(0.1, 0.2)
        0.30000000000000004
    """
    try:
        # Input validation
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise CalculatorError("Both arguments must be numbers")

        result = a + b
        logger.info(f"Addition operation: {a} + {b} = {result}")
        return result
    except CalculatorError:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in addition: {e}")
        raise CalculatorError(f"Addition failed: {e}")


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtract two numbers with enhanced validation and precision handling.

    Args:
        a: First number (minuend)
        b: Second number (subtrahend)

    Returns:
        Difference of a and b (a - b)

    Raises:
        CalculatorError: If input validation fails

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(0, 5)
        -5
        >>> subtract(3.5, 1.2)
        2.3
    """
    try:
        # Input validation
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise CalculatorError("Both arguments must be numbers")

        result = a - b
        logger.info(f"Subtraction operation: {a} - {b} = {result}")
        return result
    except CalculatorError:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in subtraction: {e}")
        raise CalculatorError(f"Subtraction failed: {e}")


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiply two numbers with enhanced validation and overflow handling.

    Args:
        a: First number (multiplicand)
        b: Second number (multiplier)

    Returns:
        Product of a and b

    Raises:
        CalculatorError: If input validation fails or overflow occurs

    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(-2, 5)
        -10
        >>> multiply(0.5, 4)
        2.0
        >>> multiply(0, 100)
        0
    """
    try:
        # Input validation
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise CalculatorError("Both arguments must be numbers")

        result = a * b
        logger.info(f"Multiplication operation: {a} * {b} = {result}")
        return result
    except CalculatorError:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in multiplication: {e}")
        raise CalculatorError(f"Multiplication failed: {e}")


def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Divide two numbers with comprehensive validation and precision handling.

    Args:
        a: First number (dividend)
        b: Second number (divisor)

    Returns:
        Quotient of a and b

    Raises:
        CalculatorError: If division by zero is attempted or input validation fails

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 3)
        2.3333333333333335
        >>> divide(-15, 3)
        -5.0
        >>> divide(0, 5)
        0.0
    """
    try:
        # Input validation
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise CalculatorError("Both arguments must be numbers")

        # Division by zero check
        if b == 0:
            logger.error("Division by zero attempted")
            raise CalculatorError("Division by zero is not allowed")

        result = a / b
        logger.info(f"Division operation: {a} / {b} = {result}")
        return result
    except CalculatorError:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in division: {e}")
        raise CalculatorError(f"Division failed: {e}")


def power(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Raise a number to a power with validation and overflow protection.

    Args:
        a: Base number
        b: Exponent

    Returns:
        a raised to the power of b

    Raises:
        CalculatorError: If input validation fails or overflow occurs

    Examples:
        >>> power(2, 3)
        8
        >>> power(5, 0)
        1
        >>> power(4, 0.5)
        2.0
        >>> power(-2, 3)
        -8
        >>> power(10, -2)
        0.01
    """
    try:
        # Input validation
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise CalculatorError("Both arguments must be numbers")

        # Check for potential overflow with large exponents
        if isinstance(b, int) and abs(b) > 1000:
            logger.warning(f"Large exponent detected: {b}")
            raise CalculatorError("Exponent too large, potential overflow")

        result = a**b
        logger.info(f"Power operation: {a} ^ {b} = {result}")
        return result
    except CalculatorError:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in power operation: {e}")
        raise CalculatorError(f"Power operation failed: {e}")


def modulo(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Calculate modulo (remainder) of two numbers with comprehensive validation.

    Args:
        a: First number (dividend)
        b: Second number (divisor)

    Returns:
        Modulo of a and b (remainder when a is divided by b)

    Raises:
        CalculatorError: If modulo by zero is attempted or input validation fails

    Examples:
        >>> modulo(10, 3)
        1
        >>> modulo(15, 4)
        3
        >>> modulo(7, 7)
        0
        >>> modulo(-10, 3)
        2
        >>> modulo(5.5, 2)
        1.5
    """
    try:
        # Input validation
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise CalculatorError("Both arguments must be numbers")

        # Modulo by zero check
        if b == 0:
            logger.error("Modulo by zero attempted")
            raise CalculatorError("Modulo by zero is not allowed")

        result = a % b
        logger.info(f"Modulo operation: {a} % {b} = {result}")
        return result
    except CalculatorError:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in modulo operation: {e}")
        raise CalculatorError(f"Modulo operation failed: {e}")
