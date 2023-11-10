#!/usr/bin/python3
""" modle with class rectangle that inherit from base """
from models.base import Base


class Rectangle(Base):
    """
        Rectangle: class that inherit from the Base class
        Args:
            base: the class- Base inherited from
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)


    @property
    def width(self):
        """ retrieve the width """
        return self.__width

    @width.setter
    def width(self):
        """ retrieve the width """
        self.__width = width

    @property
    def height(self):
        """ retrieve the height """
        return self.__height

    @height.setter
    def height(self):
        """ set the height """
        self.__height = height

    @property
    def x(self):
        """ retrieve the x """
        return self.__x

    @x.setter
    def x(self):
        """ set the x coordinate """
        self.__x = x

    @property
    def y(self):
        """ retrieve the y """
        return self.__y

    @y.setter
    def y(self):
        """ set y """
        self.__y = y
