#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    function that returns the number of keys in a dictionary.
    """
    key_num = 0
    for key in range(len(a_dictionary)):
        key_num = key_num + key

    return key_num
