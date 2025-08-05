#!/usr/bin/python3
"""Module that contains a function to list attributes and methods."""


def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect

    Returns:
        list: A list of strings containing the names of all attributes
    """
    return dir(obj)
