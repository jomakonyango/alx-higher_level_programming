#!/usr/bin/python3
"""
This is the "4-square" module.

The 4-square module defines the Square class that defines a square.
"""

class Square:
    """
    This is the Square class.
    
    The Square class defines a square by its private instance attribute 'size'.
    """
    def __init__(self, size=0):
        """
        This is the constructor method for the Square class.
        
        Args:
            size (int): The size of the square, defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        This is a getter for size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a setter for size.
        
        Args:
            value (int): The size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This is a public instance method that returns the current square area.
        """
        return self.__size ** 2

