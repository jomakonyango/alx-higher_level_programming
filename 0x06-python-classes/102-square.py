#!/usr/bin/python3
"""
This module defines a class Square that defines a square by size and provides
methods to calculate its area. The Square instance can answer to comparators
based on the square area.
"""

class Square:
    """
    A class to represent a square.

    ...

    Attributes
    ----------
    size : int or float
        size of the square

    Methods
    -------
    area():
        Returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Constructs all the necessary attributes for the square object.

        Parameters
        ----------
            size : int or float, optional
                size of the square (default is 0)
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters
        ----------
            value : int or float
                size of the square

        Raises
        ------
        TypeError
            If size is not a number.
        ValueError
            If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Checks if two Square instances are equal in area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two Square instances are not equal in area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks if a Square instance is less than another in area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if a Square instance is less than or equal to another in area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checks if a Square instance is greater than another in area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if a Square instance is greater than or equal to another in area."""
        return self.area() >= other.area()

