#!/usr/bin/python3
"""Module that provides integer addition functionality.

This module contains a function to add two integers or floats,
with appropriate type checking and casting to ensure the result
is always an integer.
"""


def add_integer(a, b=98):
    """Add two integers.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98
        
    Returns:
        int: The sum of a and b as an integer
        
    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    if a != a:
        raise ValueError("cannot convert float NaN to integer")
    if b != b:
        raise ValueError("cannot convert float NaN to integer")
    
    if a == float('inf') or a == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if b == float('inf') or b == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer")
    
    return int(a) + int(b)