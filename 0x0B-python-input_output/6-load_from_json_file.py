#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    def load_from_json_file(filename): creates an obj. from a json file.
    Args:
        filename: the name of the file
    """
    with open(filename) as file_pointer:
        return json.load(file_pointer)
