import math

class MagicClass:
    """
    A class to represent a circle.

    ...

    Attributes
    ----------
    __radius : int or float
        radius of the circle

    Methods
    -------
    area():
        Returns the area of the circle.
    circumference():
        Returns the circumference of the circle.
    """

    def __init__(self, radius=0):
        """
        Constructs all the necessary attributes for the circle object.

        Parameters
        ----------
            radius : int or float, optional
                radius of the circle (default is 0)
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns the current circle area."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the current circle circumference."""
        return 2 * math.pi * self.__radius

