#!/usr/bin/python3
"""
This module defines a class Square that defines a square by size and position.
"""

class Square:
    """
    A class to represent a square.

    ...

    Attributes
    ----------
    size : int
        size of the square
    position : tuple of int
        position of the square in 2D space

    Methods
    -------
    area():
        Returns the area of the square.
    my_print():
        Prints the square with the character #.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructs all the necessary attributes for the square object.

        Parameters
        ----------
            size : int, optional
                size of the square (default is 0)
            position : tuple of int, optional
                position of the square in 2D space (default is (0, 0))
        """
        self.size = size
        self.position = position

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
            value : int
                size of the square

        Raises
        ------
        TypeError
            If size is not an integer.
        ValueError
            If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters
        ----------
            value : tuple of int
                position of the square in 2D space

        Raises
        ------
        TypeError
            If position is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.

        If size is equal to 0, print an empty line.
        Position is used by using space.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join(" " * self.__position[0] + "#" * self.__size for _ in range(self.__size)))

    def __str__(self):
        """
        Returns a string representation of the square with the character #.

        If size is equal to 0, return an empty string.
        Position is used by using space.
        """
        if self.__size == 0:
            return ""
        return "\n" * self.__position[1] + "\n".join(" " * self.__position[0] + "#" * self.__size for _ in range(self.__size))

