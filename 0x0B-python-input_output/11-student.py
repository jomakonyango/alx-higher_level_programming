#!/usr/bin/python3
"""
Module: 11-student

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

    def to_json(self, attrs=None):
        """
        Method: to_json

        This method retrieves a dictionary representation of a Student
        instance.

        Parameters:
        - attrs: List of strings representing the attribute names that should
        be retrieved. If attrs is None or not a list of strings, all
                 attributes are retrieved.

        Returns:
        - The dictionary representation of the Student instance.
        """
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Method: reload_from_json

        This method replaces all attributes of the Student instance.

        Parameters:
        - json: A dictionary where the key is the attribute name and the value
                is the new attribute value.

        Returns:
        - None
        """
        for key, value in json.items():
            setattr(self, key, value)
