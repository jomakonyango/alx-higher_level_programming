#!/usr/bin/python3
"""
Module: 100-append_after

This module contains the definition of the append_after function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function: append_after

    This function inserts a line of text to a file, after each
    line containing
    a specific string.

    Parameters:
    - filename: The name of the file.
    - search_string: The string to search for in the file.
    - new_string: The new string to insert into the file.

    Returns:
    - None
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
