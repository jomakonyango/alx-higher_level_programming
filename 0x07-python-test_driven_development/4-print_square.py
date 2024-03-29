#!/usr/bin/python3
def print_square(size):
    """
    Prints a square with the character #.
    
    >>> print_square(4)
    ####
    ####
    ####
    ####
    >>> print_square(1)
    #
    >>> print_square(0)
    <BLANKLINE>
    >>> print_square(-1)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0
    >>> print_square(2.5)
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
