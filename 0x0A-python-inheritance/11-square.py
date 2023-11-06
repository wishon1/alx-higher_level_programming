#!/usr/bin/python3
"""
    class Square that inherits from Rectangle (9-rectangle.py).
    (task based on 10-square.py).
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Rep.resent a square"""

    def __init__(self, size):
        """Initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
