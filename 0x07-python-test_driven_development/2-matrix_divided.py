#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The number by which to divide the elements of the matrix.

    Returns:
        list: A new matrix with all elements divided by div, rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number and not equal to 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return a new matrix with all elements divided by div, rounded to 2 decimal places
    return [[round(el / div, 2) for el in row] for row in matrix]
