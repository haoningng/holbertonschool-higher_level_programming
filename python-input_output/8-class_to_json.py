#!/usr/bin/python3
"""This modules define the class_to_json function"""


def class_to_json(obj):
    """ returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:

    Args:
    obj: Instance of a Class
    """
    return obj.__dict__
