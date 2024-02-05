#!/usr/bin/python3
"""This program creates the class Rectangle """


class Rectangle:
    """This defines a Rectangle

    Attributes:
        number_of_instances: Number of instances
        print_symbol: used as symbol for representation
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialise the rectangle

        Args:
        width: Width of the rectangle
        height: Height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """Define rectangle in a string format"""
        if (self.height == 0 or self.width == 0):
            return str('')
        return (str(self.print_symbol) * self.width + '\n') * (
            self.height - 1) + str(self.print_symbol) * self.width

    def __repr__(self):
        """Define rectangle in a string format"""
        if (self.height == 0 or self.width == 0):
            return str('')
        return str('Rectangle(') + str(
            self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        """Print statement when instance is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method to compare to rectangular areas"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 > area_2:
            return rect_1
        elif area_2 > area_1:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """class method to return a new rectangle instance"""
        return cls(size, size)
