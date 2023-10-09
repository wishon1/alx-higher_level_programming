#!/usr/bin/python3
"""
function that finds the biggest integer of a list.
"""


def max_integer(my_list=[]):
    if not my_list:
        return None

    max_val = my_list[0]

    for count in my_list:
        if count > max_val:
            max_val = count

    return max_val
