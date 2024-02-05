#!/usr/bin/python3
"""
This module imports the 'lookup' function from the '0-lookup' module and tests it
on a few classes.
"""

lookup = __import__('0-lookup').lookup

class MyClass1(object):
    """ An empty class """
    pass

class MyClass2(object):
    """ A class with an attribute and a method """
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

