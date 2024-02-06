#!/usr/bin/python3
"""This module creates MyList class"""


class MyList(list):
    """This defines MyList

    Attributes:
    None
    """
    def print_sorted(self):
        """Prints the list but sorted

        Args:
        self: the list
        """
        print(sorted(self))
