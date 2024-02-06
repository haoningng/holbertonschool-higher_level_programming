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
        """validates value

        name: name of value
        value: value to be validated
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This creates the Rectangle Class

    Args:
    width: Width of Rectangle
    height: Height of Rectangle
    """
    def __init__(self, width, height):
        """Initiates the Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Defines the str format of te Rectangle"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
