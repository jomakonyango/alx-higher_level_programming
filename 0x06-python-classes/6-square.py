#!/usr/bin/python3
"""
This is the "6-square" module.

The 6-square module defines the Square class that defines a square.
"""

class Square:
    """
    This is the Square class.
    
    The Square class defines a square by its private instance attribute 'size'.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        This is the constructor method for the Square class.
        
        Args:
            size (int): The size of the square, defaults to 0.
            position (tuple): The position of the square, defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        This is a getter for position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This is a setter for position.
        
        Args:
            value (tuple): The position of the square.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        This is a public instance method that returns the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        This is a public instance method that prints the square with the character '#'.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

