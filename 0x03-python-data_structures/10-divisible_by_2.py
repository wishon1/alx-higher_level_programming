#!/usr/bin/python3
"""
function that finds all multiples of 2 in a list.
"""


def divisible_by_2(my_list=[]):
    # Initialize an empty list to store boolean values
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
