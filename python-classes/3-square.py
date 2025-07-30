#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that defines a square with size validation and area calc."""

    def __init__(self, size=0):
        """Initialize a square with optional size.

        Args:
            size (int): The size of the square (default: 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
