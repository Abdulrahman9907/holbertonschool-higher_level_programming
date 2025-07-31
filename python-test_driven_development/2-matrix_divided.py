#!/usr/bin/python3
"""Module that provides matrix division functionality.

This module contains a function to divide all elements of a matrix
by a given number, with appropriate validation and error handling.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number.

    Args:
        matrix: List of lists containing integers or floats
        div: Number to divide by (integer or float)

    Returns:
        list: New matrix with all elements divided by div,
              rounded to 2 decimals

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                  or if rows have different sizes, or if div is not a number
        ZeroDivisionError: If div is 0
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(msg)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)

    if not all(isinstance(element, (int, float))
               for row in matrix for element in row):
        raise TypeError(msg)

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
