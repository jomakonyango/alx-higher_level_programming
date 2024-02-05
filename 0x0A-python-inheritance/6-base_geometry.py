#!/usr/bin/python3
"""
This module contains a class called 'BaseGeometry'.
"""
class BaseGeometry:
    """
    A class BaseGeometry with a public instance method 'area'.
    """

    def area(self):
        """
        A public instance method that raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

