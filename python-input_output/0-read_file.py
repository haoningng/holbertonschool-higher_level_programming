#!/usr/bin/python3
"""This modules defines the read_file function"""


def read_file(filename=""):
    """Read a text file and prints it to stdout

    Args:
    filename: Name of the text tile
    """
    with open(filename, "r", encoding='UTF-8') as f:
        print(f.read(), end="")
