#!/usr/bin/python3
"""This is the module for add_integer function"""


def add_integer(a, b=98):
    """
    Return the sum of a and b

    Args:
    a(int): first input
    b(int): second input

    Return:
    The sum of a and b as int
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
