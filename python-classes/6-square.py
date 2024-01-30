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
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Getter method for size private attribute """
        return self.__size

    @property
    def position(self):
        """Getter method for position private attribute """
        return self.__position

    @position.setter
    def position(self, position):
        """ Setter method for position private attribute """
        if (not isinstance(self.position, tuple) and not (len(position) == 2)
                and position[0] < 0 and position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    def my_print(self):
        """ Prints the square with the character # """
        if self.size == 0:
            print()
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            for k in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
