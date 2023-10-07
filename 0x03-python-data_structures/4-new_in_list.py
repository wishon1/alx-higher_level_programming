#!/usr/bin/python3
"""
 function that replaces an element in a list at a specific position
 without modifying the original list (like in C).
"""


def new_in_list(my_list, idx, element):
    _list = int(len(my_list))
    if not my_list:
        return
    else:
        if idx < 0 or idx > _list:
            return my_list
        else:
            for count in range(_list):
                if count == idx:
                    new_list = my_list.copy()
                    new_list[count] = element
    return new_list
