#!/usr/bin/python3
"""
function that replaces all occurrences of an element
by another in a new list.
"""


def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
