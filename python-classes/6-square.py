#!/usr/bin/python3
"""This program creates the class Square """


class Square:
    """This defines a square

    This is a simple implementation of a class

    Attributes:
        None

    """
    def __init__(self, size=0, position=(0, 0)):
        """Docstring on the __init__ method.

        Args:
            size (int): size of the square
            position (tuple): position of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Get the size of the square """
        return self.__size

    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position of the square

        Args:
            value (tuple): A tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or not (len(value) == 2)
                or not isinstance(value[0], int)
                or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, size):
        """ Set the size of the square

        Args:
            size (int): Size of the square
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Returns the area of the square """
        return self.__size**2

    def my_print(self):
        """ Prints the square with the character # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
