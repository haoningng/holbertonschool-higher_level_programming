#!/usr/bin/python3
"""This module creates Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """This defines Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiates the class
        
        Args:
        width(int): width
        height(int): height
        x(int): x-axis
        y(int): y-axis
        id(int): ID
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @property
    def width(self):
        """Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width
        
        Args:
        value: new value for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height
        
        Args:
        value: new value for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x
        
        Args:
        value: new value for x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y
        
        Args:
        value: new value for y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.height * self.width

    def display(self):
        """prints in stdout the Rectangle instance with the char #"""
        print((("#" * self.width) + '\n') * (self.height - 1) + "#" *
              self.width)
