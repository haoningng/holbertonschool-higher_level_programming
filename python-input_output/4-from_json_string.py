#!/usr/bin/python3
"""This modules define the from_json_string function"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string

    Args:
    my_str: object
    """
    return json.loads(my_str)
