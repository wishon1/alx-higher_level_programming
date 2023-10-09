#!/usr/bin/python3
"""
function that deletes the item at a specific position in a list.
"""


def delete_at(my_list=[], idx=0):
    _len = int(len(my_list))
    if idx < 0 or idx > _len:
        return my_list

    for index in range(_len):
        if index == idx:
            del my_list[index]

    return my_list
