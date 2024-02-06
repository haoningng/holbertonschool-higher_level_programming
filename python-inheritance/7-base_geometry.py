#!/usr/bin/python3
"""This module creates the BaseGeometry class"""


class BaseGeometry:
    """This creates the BaseGeometry Class

    Attributes:
    None
    """
    def area(self):
        """Raises an exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
