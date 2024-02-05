#!/usr/bin/python3
"""This program creates the class Rectangle """


class Rectangle:
    """This defines a Rectangle

    Attributes:
        None
    """

    def __init__(self, width=0, height=0):
        """Initialise the rectangle

        Args:
        width: Width of the rectangle
        height: Height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle

        Args
        value: value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle

        Args:
        value: value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if (self.height == 0 or self.width == 0):
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        return str(('#' * self.width) + '\n') * (
            self.height - 1) + str('#' * self.width)
