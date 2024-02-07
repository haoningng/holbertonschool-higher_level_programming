#!/usr/bin/python3
"""This modules define the load_from_json_file function"""
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”:

    Args:
    filename: Name of a JSON file
    """
    with open(filename, "r", encoding='UTF-8') as f:
        return json.load(f)
