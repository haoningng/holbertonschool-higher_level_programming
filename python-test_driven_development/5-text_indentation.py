#!/usr/bin/python3
"""
Module: 5-text_indentation.py

Function: text_indentation()
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these '.', '?', ':'

    Args:
    text(str): text input
    """
    skip = 0
    if not (isinstance(text, str)):
        raise TypeError("text must be a string")
    for char in text:
        if char == '.' or char == '?' or char == ':':
            print('\n')
            skip = 1
        elif char == ' ' and skip == 1:
            skip = 0
            pass
        else:
            print("{}".format(char), end="")
    print()
