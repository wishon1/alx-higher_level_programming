#!/usr/bin/python3
""" modle  Square that inherits from Rectangle """
from model.rectangle import Rectangle


class Square(Rectangle):
    """
        Square: class square that inherit from rectangle.
            Args: Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor for initialization """

