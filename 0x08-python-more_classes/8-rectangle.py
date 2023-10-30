#!/usr/bin/python3
"""
class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
with applicaion of private and public instance attributes
"""


class Rectangle:
    """ A class rectangle
        Attributes:
                    Width : width of the rectangle which is an integer
                    height: height of the rectangle (integer)
        Methods:
                def area(self): public instance method to calculate the area
                def perimeter(self): public instance method to calculate the
                                    perimeter
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ __init__ method to initialize the attributes of the class"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ to retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width if all test cases are met"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ return the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of the height if all conditions are met """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public instance attribute that returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ calculates the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ prints the output """
        if self.__width == 0 or self.__height == 0:
            return ""
        _str = ""
        for counter in range(self.height):
            _str = _str + str(self.print_symbol) * self.width + "\n"
        return _str.rstrip()

    def __repr__(self):
        """Return a string representation that allows the recreation
            of the instance
        """
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        '''Prints the message when an instance of Rectangle is deleted'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2.area()
