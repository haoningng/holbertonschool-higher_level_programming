#!/usr/bin/python3
"""This module defines the is_same_class function"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class

    Args:
    obj: subclass
    a_class: superclass
    """
    if type(obj) is a_class:
        return True
    else:
        return False
