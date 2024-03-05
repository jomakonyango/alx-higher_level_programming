#!/usr/bin/python3
"""
Module: 4-from_json_string

This module contains a function that returns an object (Python data structure)
represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Function: from_json_string

    This function returns an object (Python data structure) represented by a
    JSON string.

    Parameters:
    - my_str: The JSON string to convert to an object.

    Returns:
    - The object represented by my_str.
    """
    return json.loads(my_str)
