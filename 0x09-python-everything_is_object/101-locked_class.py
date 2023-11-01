#!/usr/bin/python3
"""
This class enforces the instantiation of a single attribute, 'first_name.'
Users are restricted from creating any additional attributes during the
initialization process. This restriction is implemented to ensure a streamlined
and standardized approach to attribute handling within the class, promoting a
more organized and focused data structure.
"""


class LockedClass:
    """
    class enforces the instantiation of a single attribute, 'first_name.
    """
    __slots__ = ["first_name"]
