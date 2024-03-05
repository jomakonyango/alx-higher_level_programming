#!/usr/bin/python3
"""
Module: 1-write_file

This module contains a function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Function: write_file

    This function writes a string to a text file (UTF8) and returns the
    number of characters written.

    Parameters:
    - filename: The name of the file to write to. If the file doesn't exist,
                it will be created. If it does exist, it will be overwritten.
    - text: The string to write to the file.

    Returns:
    - The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
