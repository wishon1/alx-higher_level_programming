#!/usr/bin/python3

"""program that returns the square of a class"""


class Square:
    """its an  ampty class Square that defines a square without
    attributes nor properties.
    """

    def __init__(self, size=0):
        """Initialization method of the class
                Args:
                size (int): Size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Size property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private instance attribute __size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square instance
                Returns the square of the size(interger)
                """
        return (self.__size ** 2)
