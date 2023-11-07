#!/usr/bin/python3
"""
JASON representation of the object
"""


import json


def to_json_string(my_obj):
    """
    to_json_string - jason representation of an object
    Args:
        my_obj: object to return
    """
    return json.dumps(my_obj)
