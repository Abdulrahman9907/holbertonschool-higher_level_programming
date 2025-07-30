#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that defines a square with private size attribute."""

    def __init__(self, size):
        """Initialize a square with size.

        Args:
            size: The size of the square.
        """
        self.__size = size
