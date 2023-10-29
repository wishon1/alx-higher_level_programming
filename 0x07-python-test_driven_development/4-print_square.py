#!/usr/bin/python3
"""
function that prints a square with the character #.
"""


def print_square(size):
    """
    print_square - prints a square with the character #.

    Args:
        size: The size of the square (int or float)

    Return: returns a squre with character #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) < 0:
        raise TypeError("size must be an integer")
    
    count = 0
    while count < size:
        for _ in range(size):
            print("#", end="")
        print()
        count = count + 1
