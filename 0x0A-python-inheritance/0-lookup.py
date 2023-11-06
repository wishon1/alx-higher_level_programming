#!/usr/bin/python3
"""
function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
        lookup - function that returns the list of available attributes and
                methods.
        obj: the object to be checked.
        Return: returns a new list of all available attributes and methods

    """
    return dir(obj)
