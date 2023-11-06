#!/usr/bin/python3
"""
    returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
        inherits_from - function that checks if the object is a subclass of
                        the specified class
        Arguements:
            obj: The obj to check
            a_class: the Class
        Return: return true, else false
    """
    return (issubclass(type(obj), a_class))
