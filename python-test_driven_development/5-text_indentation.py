#!/usr/bin/python3
"""Module that provides text indentation functionality.

This module contains a function to print text with specific formatting,
adding two new lines after certain punctuation marks.
"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?', and ':' characters.

    Args:
        text (str): The text to format and print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end="")
            i += 1
