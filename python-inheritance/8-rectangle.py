#!/usr/bin/python3
"""This module creates the BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This creates the Rectangle Class

    Args:
    width: Width of Rectangle
    height: Height of Rectangle
    """
    def __init__(self, width, height):
        """Initiates the Rectangle"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
