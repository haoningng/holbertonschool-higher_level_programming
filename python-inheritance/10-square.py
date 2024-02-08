#!/usr/bin/python3
"""This module creates the BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """This creates the Square Class

    Attributes:
    None
    """
    def __init__(self, size):
        """Initiates the Square

        Args:
        width: Width of Square
        height: Height of Square
        """
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Returns the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """Defines the str format of te Square"""
        return str("[Rectangle] {}/{}".format(self.__size, self.__size))
