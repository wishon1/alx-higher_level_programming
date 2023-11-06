#!/usr/bin/python3
"""
function that returns True if the object is exactly an instance of the
specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
        is_same_class - function that returns True if the object is exactly
                        an instance of the specified class ; otherwise False.

        Arguements:
            obj: An object of instance-- of the class
            a_class: The class.

        Return: Return true if otherwise return false
    """
    return type(obj) is a_class
