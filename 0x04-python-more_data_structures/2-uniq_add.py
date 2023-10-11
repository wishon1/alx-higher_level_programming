#!/usr/bin/python3
"""
function that adds all unique integers in a
list (only once for each integer).
"""


def uniq_add(my_list=[]):
    new_list = []
# use set() to remove duplicate item from my_list
    new_list = set(my_list)
    added_item = 0
# iterate through new_list and store the added item
    for item in new_list:
        added_item = added_item + int(item)
    return added_item
