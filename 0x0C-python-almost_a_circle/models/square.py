#!/usr/bin/python3
""" modle  Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square: class square that inherit from rectangle.
            Args: Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor for initialization """
        super().__init__(size, size, x, y, id)

    def __self__(self):
        """
            overloading __str__ method should return [Square] (<id>) <x>/<y> 
            - <size> - in our case, width or height
        """
        return "[Square] {} {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """retrieve the height which is sme as the width or height in the square"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size.(note value is just a placeholder, any variable could be 
            used. use of the name value is just a common convention to make code
            more readable. value represent the new size been assigned to the square)
        """
        self.width = value
        self.height = value