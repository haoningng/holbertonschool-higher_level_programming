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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        Args:
        attrs: attributes of the student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    new_dict[i] = getattr(self, i)
            return new_dict
