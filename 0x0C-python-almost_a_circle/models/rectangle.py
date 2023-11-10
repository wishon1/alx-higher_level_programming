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
    def width(self, width):
        """ retrieve the width """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ retrieve the height """
        return self.__height

    @height.setter
    def height(self, height):
        """ set the height """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ retrieve the x """
        return self.__x

    @x.setter
    def x(self, x):
        """ set the x coordinate """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError(" x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ retrieve the y """
        return self.__y

    @y.setter
    def y(self, y):
        """ set y """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ returns the area value of the rectangle """
        return (self.width * self.height)

    def display(self):
        """  prints in stdout the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        for _ in range(self.y):
            print("")

        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width,
                self.height)
