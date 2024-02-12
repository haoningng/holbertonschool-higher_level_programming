#!/usr/bin/python3
"""This module creates Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of Square"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
