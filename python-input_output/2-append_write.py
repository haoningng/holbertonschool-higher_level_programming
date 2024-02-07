#!/usr/bin/python3
"""This module defines the append_write function"""


def append_write(filename="", text=""):
    """Appends a stirng at the end of a text file and return num of char

    Args:
    filename: Name of the file
    text: Text to be appended
    """
    with open(filename, "a", encoding='UTF-8') as f:
        f.write(text)
        return len(text)
