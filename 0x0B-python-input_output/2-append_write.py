#!/usr/bin/python3
"""
Module: 2-append_write

This module contains a function that appends a string at the end of a text file
(UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Function: append_write

    This function appends a string at the end of a text file (UTF8) and returns
    the number of characters added.

    Parameters:
    - filename: The name of the file to append to. If the file doesn't exist,
                it will be created.
    - text: The string to append to the file.

    Returns:
    - The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
