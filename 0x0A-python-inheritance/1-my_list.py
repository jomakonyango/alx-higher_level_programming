#!/usr/bin/python3
"""
This module contains a class called 'MyList' that
inherits from the built-in list class.
"""


class MyList(list):
    """
    A class that inherits from list and has a method to print
    the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        print(sorted(self))
