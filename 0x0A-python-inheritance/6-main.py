#!/usr/bin/python3
"""
This module imports the 'BaseGeometry' class from the '6-base_geometry' module and tests it.
"""
BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

