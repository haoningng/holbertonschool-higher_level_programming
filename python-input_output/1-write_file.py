#!/usr/bin/python3
"""This modules defines the write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file and return the num of char

    Args:
    filename: Name of the text file
    text: Text to be written
    """
    with open(filename, "w", encoding='UTF-8') as f:
        return f.write(text)
