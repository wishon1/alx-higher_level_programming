#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    function that prints a dictionary by ordered keys.
    """
    # sort the keys in the dictionary and store in sorted_key
    sorted_key = sorted(a_dictionary.keys())

    # access each of the sorted keys via a loop
    for key in sorted_key:
        print("{}: {}".format(key, a_dictionary[key]))
