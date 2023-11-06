#!/usr/bin/python3
"""
    function that returns True if the object is an instance of, or if
    the object is an instance of a class that inherited from, the specified
    class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
        is_kind_of_class - Function that checks if the object is an instance
                            or a subclass of the specified class
        Arguements:
                obj: The object to check.
                a_class: The class.

        Return: Return True otherwise return false
    """
    return isinstance(obj, a_class)
