#!/usr/bin/env python3
def no_c(my_string):
    """
    A function that removes all characters c and C from a string.

    Args:
    my_string (str): The string to modify

    Returns:
    The modified string
    """
    return "".join(char for char in my_string if char not in 'cC')
