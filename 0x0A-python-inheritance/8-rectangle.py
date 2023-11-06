#!/usr/bin/python3
"""Rectangle that inherits from BaseGeometry (7-base_geometry.py)"""


class BaseGeometry:
    """ class BaseGeometry """
    def area(self):
        """ raise exception error if area is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator that validates the value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle - class rectangle that inherit from BaseGeometry class.
        Args: BaseGeometry.
    """
    def __init__(self, width, height):
        """
            constructor  __init__ - A contructor for instantiation.
            Args:
                width: The width of the value.
                height: The height of the value.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
