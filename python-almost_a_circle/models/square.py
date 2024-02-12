#!/usr/bin/python3
"""This module creates Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initiates the Square Class

        Args:
        size(int): Size of square
        x(int): x-axis
        y(int): y-axis
        id(int): id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of Square"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Returns the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets size

        Args:
        value: new value for size
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            attr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
