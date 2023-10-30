#!/usr/bin/python3
"""
Class rectangle that defines a rectangle with application
of getters and setters
"""


class Rectangle:
    """ A rectangle that defines a class
            width: the width
            height: the height.
        """

    def __init__(self, width=0, height=0):
        """ __init__: used to initialize the the attributes
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ retrive the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width if all test conditions are met """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the heigt if all conditions are met """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
