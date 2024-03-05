#!/usr/bin/python3
"""
Module: 5-save_to_json_file

This module contains a function that writes an object to a text file,
using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function: save_to_json_file

    This function writes an object to a text file, using a JSON representation.

    Parameters:
    - my_obj: The object to write to the file.
    - filename: The name of the file to write to.

    Returns:
    - None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
