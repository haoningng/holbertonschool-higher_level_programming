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
    if not (isinstance(text, str)):
        raise TypeError("text must be a string")
    
    start_index = 0
    for i in range(len(text)):
        if text[i] in (".", "?", ":"):
            print(text[start_index: i + 1].strip(), end="\n\n")
            start_index = i + 1
    print(text[start_index: len(text)].strip(), end="")
