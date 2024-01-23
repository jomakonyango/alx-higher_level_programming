#!/usr/bin/python3
"""
This is the "1-square" module.

The 1-square module defines the Square class that defines a square.
"""

class Square:
    """
    This is the Square class.
    
    The Square class defines a square by its private instance attribute 'size'.
    """
    def __init__(self, size):
        """
        This is the constructor method for the Square class.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size
