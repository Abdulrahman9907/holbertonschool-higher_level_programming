#!/usr/bin/python3
"""Module that contains a class MyList that inherits from list."""


class MyList(list):
    """A class that inherits from list with additional functionality."""

    def print_sorted(self):
        """Prints the list sorted in ascending order.

        Assumes all elements are integers.
        """
        print(sorted(self))
