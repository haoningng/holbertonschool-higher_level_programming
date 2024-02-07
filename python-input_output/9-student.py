#!/usr/bin/python3
"""This module defines the Student Class"""


class Student:
    """This defines the Student Class

    Attributes:
    None
    """
    def __init__(self, first_name, last_name, age):
        """Instatiation

        Args:
        first_name: First Name
        last_name: Last Name
        age: Age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance

        Args:
        None
        """
        return self.__dict__
