#!/usr/bin/python3
"""
Module: 4-print_square.py

Function: print_square()
"""


def print_square(size):
    """
    Prints a square with character #

    Args:
    size(int): size length of the square
    """
    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
