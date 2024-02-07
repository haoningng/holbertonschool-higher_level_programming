#!/usr/bin/python3
"""This modules define the save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation

    Args:
    my_obj: String object
    """
    with open(filename, "w", encoding='UTF-8') as f:
        json.dump(my_obj, f)
