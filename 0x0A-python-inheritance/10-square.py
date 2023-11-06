#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size):
        """ constructor for instantiation of size """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """
            Area: calculates the area of the size.
            Return: returns the area of the size.
        """
        return self.__size ** 2
