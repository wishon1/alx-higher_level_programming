#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = dict()
    for key, digit in a_dictionary.items():
        if digit == value:
            print(key, digit)
            continue
        new_dict[key] = value

    a_dictionary = new_dict
    return a_dictionary
