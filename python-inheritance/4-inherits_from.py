#!/usr/bin/python3
"""This module defines the inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class
    that inherited (directedly or indirectly) from the specified class

    Args:
    obj: subclass
    a_class: superclass
    """
    if type(obj) is not a_class:
        for base in type(obj).__mro__:
            if base is a_class:
                return True
    return False
