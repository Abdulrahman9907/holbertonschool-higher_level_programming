#!/usr/bin/python3
"""Module that contains BaseGeometry class with area method."""


class BaseGeometry:
    """A geometry class with area method."""

    def area(self):
        """Calculate the area.

        Raises:
            Exception: Always, as area is not implemented
        """
        raise Exception("area() is not implemented")
