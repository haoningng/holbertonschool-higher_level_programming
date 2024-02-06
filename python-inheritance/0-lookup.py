#!/usr/bin/python3
"""This is a module for lookup function"""


def lookup(obj):
    """Return the list of available attributes and methods of an object

    Args:
    obj: the object
    """
    return dir(obj)
