#!/usr/bin/python3
"""
writes an Object to a text file, using a JSON representation:
"""

import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - using Json representation to write an obj. file to a
                        text file
    Args:
        my_obj: the object to write.
        filename: The name of the file
    """
    with open(filename, mode="w") as file_pointer:
        json.dump(my_obj, file_pointer)
