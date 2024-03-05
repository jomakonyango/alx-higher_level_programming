#!/usr/bin/python3
"""
Module: 3-to_json_string

This module contains a function that returns the JSON representation of an
object (string).
"""

import json


def to_json_string(my_obj):
    """
    Function: to_json_string

    This function returns the JSON representation of an object (string).

    Parameters:
    - my_obj: The object to convert to a JSON string.

    Returns:
    - The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
