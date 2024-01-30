#!/usr/bin/python3
"""This program creates the class Square """


class Square:
    """This defines a square

    This is a simple implementation of a class

    Attributes:
        None

    """
    def __init__(self, size=0):
        """Docstring on the __init__ method.

        Args:
            size (int): size of the square
        """
        # if not (isinstance(size, int)):
        #     raise TypeError("size must be an integer")
        # elif size < 0:
        #     raise ValueError("size must be >= 0")
        # else:
        self.__size = size

    @property
    def size(self):
        """ Getter method for size private attribute """
        return self.__size

    @size.setter
    def size(self, size):
        """ Setter method size private attribute """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Returns the area of the square """
        return self.__size**2
