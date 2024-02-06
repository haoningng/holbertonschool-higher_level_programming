#!/usr/bin/python3
"""This module defines the inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class
    that inherited (directedly or indirectly) from the specified class

    Args:
    obj: subclass
    a_class: superclass
    """
    if isinstance(obj, a_class):
        if type(obj) != a_class:
            return True
    else:
        return False
