#!/usr/bin/python3
"""
class Square that defines a square by: (based on 2-square.py)
"""


class Square:
    """ defines the square, use public instance afterward
    returns the current square area
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ return the current square area """
        return self.__size * self.__size
