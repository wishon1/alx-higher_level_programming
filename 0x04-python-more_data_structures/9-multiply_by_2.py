#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    returns a new dictionary with all values multiplied by 2
    """
    # create a new dic, and store the items of a_dictionary in it
    new_dictionary = a_dictionary.copy()

    for key, values in a_dictionary.items():
        new_dictionary[key] = values * 2

    return new_dictionary
