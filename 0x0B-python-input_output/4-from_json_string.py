#!/usr/bin/python3
"""
function that returns an object (Python data structure)
represented by a JSON string:
"""


import json


def from_json_string(my_str):
    """
    from_json_string - return an object of python data structure
    Args:
        my_str: object to return.
    """
    return json.loads(my_str)
