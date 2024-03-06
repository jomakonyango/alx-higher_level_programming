#!/usr/bin/python3
"""
Module: 8-class_to_json

This module contains a function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object.
"""


def class_to_json(obj):
    """
    Function: class_to_json

    This function returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of
    an object.

    Parameters:
    - obj: An instance of a Class. All attributes of the obj Class are
           serializable: list, dictionary, string, integer and boolean.

    Returns:
    - The dictionary description of obj.
    """
    return obj.__dict__
