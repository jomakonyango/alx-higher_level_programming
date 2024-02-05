#!/usr/bin/python3
"""
This module imports the 'BaseGeometry' class from the '5-base_geometry' module and tests it.
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))

