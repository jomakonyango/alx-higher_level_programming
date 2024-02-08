#!/usr/bin/python3
"""
The function takes two arguments, both of which must be integers or floats.
If either argument is a float, it is cast to an integer before addition.
If either argument is not integer or float,aTypeError is raised.
"""

def add_integer(a, b=98):
    """
    Adds two integers. Args: a:  Must be an integer or float. b: The second number to add. Must be an integer or float. Defaults to 98. Returns:    The sum of a and b, as an integer.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

