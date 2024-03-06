#!/usr/bin/python3
"""
Module: 12-pascal_triangle

This module contains the definition of the pascal_triangle function.
"""


def pascal_triangle(n):
    """
    Function: pascal_triangle

    This function returns a list of lists of integers representing the Pascal’s
    triangle of n.

    Parameters:
    - n: The number of rows in the Pascal's triangle. It is always an integer.

    Returns:
    - A list of lists of integers representing the Pascal’s triangle of n.
      Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
        row.append(1)
        triangle.append(row)

    return triangle
