#!/usr/bin/python3
"""
This module contains a function called 'lookup' that returns a list of available
attributes and methods of an object.
"""

def lookup(obj):
    """
    Function that returns the list of available attributes and methods of an object.

    Parameters:
    obj: The object whose attributes and methods we want to list.

    Returns:
    A list of the names of the attributes and methods of the object.
    """
    return dir(obj)

