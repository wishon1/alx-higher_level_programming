#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # all elements present in only one set.
    new_set = set_1 ^ set_2

    return new_set
