#!/usr/bin/python3
"""
function that adds 2 tuples.
"""


def add_tuple(tuple_a=(), tuple_b=()):
    # If tuple_a has fewer than 2 elements, use 0 for missing elements
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0, 0)
    # If tuple_b has fewer than 2 elements, use 0 for missing elements
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0, 0)

    # Add the first elements of each tuple and store it in num
    num = tuple_a[0] + tuple_b[0]

    # Add the second elements of each tuple and store it in n
    n = tuple_a[1] + tuple_b[1]

    # Return a tuple containing the results
    return (num, n)
