class Square:
    """Defines a square by size and provides methods to calculate its area."""

    def __init__(self, size=0):
        """Initializes a new Square instance with a given size.

        Args:
            size (float or int): The size of the new Square instance.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the Square instance."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the Square instance.

        Args:
            value (float or int): The size to set for the Square instance.

        Raises:
            TypeError: If `value` is not a number.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Checks if two Square instances are equal in area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two Square instances are not equal in area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks if a Square instance is less than another in area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if a Square instance is less than or equal to another in area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checks if a Square instance is greater than another in area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if a Square instance is greater than or equal to another in area."""
        return self.area() >= other.area()

