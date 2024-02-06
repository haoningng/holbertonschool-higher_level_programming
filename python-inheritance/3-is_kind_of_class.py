#!/usr/bin/python3
"""This module defines the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of the specified class

    Args:
    obj: subclass
    a_class: superclass
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
