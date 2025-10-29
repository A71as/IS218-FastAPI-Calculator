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
    Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    try:
        result = a + b
        logger.info(f"Addition: {a} + {b} = {result}")
        return result
    except Exception as e:
        logger.error(f"Error in addition: {e}")
        raise CalculatorError(f"Addition failed: {e}")

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtract two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference of a and b
    """
    try:
        result = a - b
        logger.info(f"Subtraction: {a} - {b} = {result}")
        return result
    except Exception as e:
        logger.error(f"Error in subtraction: {e}")
        raise CalculatorError(f"Subtraction failed: {e}")

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
    """
    try:
        result = a * b
        logger.info(f"Multiplication: {a} * {b} = {result}")
        return result
    except Exception as e:
        logger.error(f"Error in multiplication: {e}")
        raise CalculatorError(f"Multiplication failed: {e}")

def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Divide two numbers.
    
    Args:
        a: First number (dividend)
        b: Second number (divisor)
        
    Returns:
        Quotient of a and b
        
    Raises:
        CalculatorError: If division by zero is attempted
    """
    try:
        if b == 0:
            logger.error("Division by zero attempted")
            raise CalculatorError("Division by zero is not allowed")
        
        result = a / b
        logger.info(f"Division: {a} / {b} = {result}")
        return result
    except CalculatorError:
        raise
    except Exception as e:
        logger.error(f"Error in division: {e}")
        raise CalculatorError(f"Division failed: {e}")

def power(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Raise a number to a power.
    
    Args:
        a: Base number
        b: Exponent
        
    Returns:
        a raised to the power of b
    """
    try:
        result = a ** b
        logger.info(f"Power: {a} ^ {b} = {result}")
        return result
    except Exception as e:
        logger.error(f"Error in power operation: {e}")
        raise CalculatorError(f"Power operation failed: {e}")

def modulo(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Calculate modulo of two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Modulo of a and b
        
    Raises:
        CalculatorError: If modulo by zero is attempted
    """
    try:
        if b == 0:
            logger.error("Modulo by zero attempted")
            raise CalculatorError("Modulo by zero is not allowed")
        
        result = a % b
        logger.info(f"Modulo: {a} % {b} = {result}")
        return result
    except CalculatorError:
        raise
    except Exception as e:
        logger.error(f"Error in modulo operation: {e}")
        raise CalculatorError(f"Modulo operation failed: {e}")