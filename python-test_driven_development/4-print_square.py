#!/usr/bin/python3
"""Module that provides square printing functionality.

This module contains a function to print a square pattern using
the '#' character with appropriate size validation.
"""


def print_square(size):
    """Print a square pattern with '#' characters.
    
    Args:
        size (int): The size length of the square
        
    Raises:
        TypeError: If size is not an integer or is a negative float
        ValueError: If size is less than 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        print("#" * size)