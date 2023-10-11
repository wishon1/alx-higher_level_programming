#!/usr/bin/python3
"""
function that returns a set of common elements in two sets.
"""


def common_elements(set_1, set_2):
    new_list = set()
    for item in set_1:
        if item not in set_2:
            continue
        new_list.add(item)
    return new_list
