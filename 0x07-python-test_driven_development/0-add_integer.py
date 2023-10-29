#!/usr/bin/python3
"""  function that adds 2 integers. """


def add_integer(a, b=98):
    """
    add_integer: function that adds two numbers (interger or float)

    Args:
        a: The first number to add
        b: The second number to add

    Returns:
        Return the sum of a and b which must be an integer

    Example:
        >>>> aa_integer(2, 3)
        5
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    a = input("Enter first: ")
    b = input("Enter second: ")

    result = add_integer(a, b)

    print(result)
