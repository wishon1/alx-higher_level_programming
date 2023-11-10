#!/usr/bin/python3
"""
    Base module managing id attribute for all future classes, incrementing
    if not provided in the constructor
"""


class Base:
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Constructor for the Base class.

            Parameters:
            id (int, optional): Unique identifier. If provided, assigns it
                                to the id attribute.
                                If not provided, increments __nb_objects and
                                assigns the new value to id.
            """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
