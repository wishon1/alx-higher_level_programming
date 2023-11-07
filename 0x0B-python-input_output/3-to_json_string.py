#!/usr/bin/python3
import json
"""
JASON representation of the object
"""


def to_json_string(my_obj):
    """
    to_json_string - jason representation of an object
    Args:
        my_obj: object to return
    """
    return json.dumps(my_obj)
