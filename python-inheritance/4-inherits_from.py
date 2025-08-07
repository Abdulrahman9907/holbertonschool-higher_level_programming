#!/usr/bin/python3
"""Module that contains a function to check inheritance only."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class inherited from a_class.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if obj inherits from a_class but is not exactly a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
