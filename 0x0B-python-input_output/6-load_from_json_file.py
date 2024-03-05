#!/usr/bin/python3
"""
Module: 6-load_from_json_file

This module contains a function that creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Function: load_from_json_file

    This function creates an object from a JSON file.

    Parameters:
    - filename: The name of the JSON file to read from.

    Returns:
    - The object represented by the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
