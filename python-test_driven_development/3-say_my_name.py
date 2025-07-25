#!/usr/bin/python3
"""Module that provides name printing functionality.

This module contains a function to print a formatted name string
with appropriate type checking for string inputs.
"""


def say_my_name(first_name, last_name=""):
    """Print a formatted name string.
    
    Args:
        first_name (str): The first name to print
        last_name (str): The last name to print (optional)
        
    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))