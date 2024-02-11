#!/usr/bin/python3
"""This module creates Rectangle class"""
Base = __import__('base').Base


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
        self.__y = value
