#!/usr/bin/python3
"""Module that contains a function to check if object is instance."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of, or inherited from, a_class.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if obj is an instance of a_class or its subclass
    """
    return isinstance(obj, a_class)
