#!/usr/bin/python3
"""
This module contains a class called 'BaseGeometry' with two public instance methods.
"""
class BaseGeometry:
    """
    A class BaseGeometry with a public instance method 'area' and 'integer_validator'.
    """

    def area(self):
        """
        A public instance method that raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A public instance method that validates 'value'.
        Raises a TypeError exception if 'value' is not an integer.
        Raises a ValueError exception if 'value' is less or equal to 0.

        Parameters:
        name: Always a string.
        value: The value to validate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

