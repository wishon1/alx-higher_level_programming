#!/usr/bin/python3
"""
function that removes all characters c and C from a string.
"""


def no_c(my_string):
    if not my_string:
        return

    new_str = ""
    _len = int(len(my_string))
    for count in range(_len):
        if my_string[count] == "c" or my_string[count] == "C":
            continue
        new_str += my_string[count]
    return new_str
