#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size):
        """
        Constructor __init__ - A constructor for instantiation.
        Args:
            size: The size of the square.
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """
        Calculate the area of the square.
        Returns:
            The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        String representation of the square.
        Returns:
            A formatted string describing the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
