#!/usr/bin/python3
"""
This module defines a Rectangle class
"""

class Rectangle:
    """
    Rectangle class with private instance attributes width and height
    """

    def __init__(self, width=0, height=0):
        """
        Initializes Rectangle instance with optional width and height

        Parameters:
        width (int): width of rectangle, defaults to 0
        height (int): height of rectangle, defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter - gets the value of width

        Returns:
        int: value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter - sets the value of width

        Parameters:
        value (int): value to set width to

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter - gets the value of height

        Returns:
        int: value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter - sets the value of height

        Parameters:
        value (int): value to set height to

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
        int: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns:
        int: perimeter of the rectangle, 0 if either width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
