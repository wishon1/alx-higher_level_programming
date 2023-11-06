#!/usr/bin/python3
"""Rectangle that inherits from BaseGeometry (7-base_geometry.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """
        Constructor __init__ - A constructor for instantiation.
        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Calculate the area of the rectangle.
        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        String representation of the rectangle.
        Returns:
            A formatted string describing the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
