#!/usr/bin/python3
"""This module creates first class Base"""
import json


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

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
        list_dictionaries(list): list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
