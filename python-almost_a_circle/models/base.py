#!/usr/bin/python3
"""This module creates first class Base"""


class Base:
    """This class will be the “base” of all other classes in this project

    Attributes:
    __nb_objects(int): incrementer for public instance attribute - id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initiates the class

        Arg:
        id(int): id
        """
        if not (id is None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
