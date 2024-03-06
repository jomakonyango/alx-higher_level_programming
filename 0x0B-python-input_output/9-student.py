#!/usr/bin/python3
"""
Module: 9-student

This module contains the definition of the Student class.
"""


class Student:
    """
    Class: Student

    This class defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Method: __init__

        This method initializes a Student instance.

        Parameters:
        - first_name: The first name of the student.
        - last_name: The last name of the student.
        - age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method: to_json

        This method retrieves a dictionary representation of a Student
        instance.

        Returns:
        - The dictionary representation of the Student instance.
        """
        return self.__dict__
