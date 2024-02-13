#!/usr/bin/python3
"""unittest for Square Class"""
import unittest
from models.square import Square
from io import StringIO
import sys
import os


class TestSquare(unittest.TestCase):
    """Test case for Square Class"""
    def test_id(self):
        """Test for id attribute"""
        r1 = Square(10)
        self.assertEqual(r1.id, 37)
        r2 = Square(2)
        self.assertEqual(r2.id, 38)
        r3 = Square(10, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_width(self):
        """Test for width method"""
        r1 = Square(10)
        self.assertEqual(r1.width, 10)
        r2 = Square(2)
        self.assertEqual(r2.width, 2)
        r3 = Square(10, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        with self.assertRaises(TypeError):
            r3 = Square("Hello")
        with self.assertRaises(TypeError):
            r3 = Square(2, "World")
        with self.assertRaises(TypeError):
            r3 = Square(2, 3, "World")
        with self.assertRaises(ValueError):
            r3 = Square(-3)
        with self.assertRaises(ValueError):
            r3 = Square(2, -3)
        with self.assertRaises(ValueError):
            r3 = Square(2, 3, -4)
        with self.assertRaises(ValueError):
            r1 = Square(0, 10)

    def test_x(self):
        """Test for x method"""
        r1 = Square(10)
        self.assertEqual(r1.x, 0)
        r3 = Square(10, 2, 0, 12)
        self.assertEqual(r3.x, 2)

    def test_y(self):
        """Test for y method"""
        r1 = Square(10)
        self.assertEqual(r1.y, 0)
        r3 = Square(10, 2, 4, 12)
        self.assertEqual(r3.y, 4)

    def test_area(self):
        """Test for area method"""
        r1 = Square(10)
        self.assertEqual(r1.area(), 100)
        r3 = Square(1, 2, 0, 12)
        self.assertEqual(r3.area(), 1)

    def test_display(self):
        """Test for display method - no x no y"""
        r1 = Square(2)
        display_1 = "##\n##\n"
        captured_input = StringIO()
        sys.stdout = captured_input
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_input.getvalue(), display_1)
        """Test for display method - no y"""
        r1 = Square(2, 2)
        display_1 = "  ##\n  ##\n"
        captured_input = StringIO()
        sys.stdout = captured_input
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_input.getvalue(), display_1)
        """Test for display method"""
        r1 = Square(2, 2, 1)
        display_1 = "\n  ##\n  ##\n"
        captured_input = StringIO()
        sys.stdout = captured_input
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_input.getvalue(), display_1)

    def test_str(self):
        """Test for __str__ method"""
        r1 = Square(4, 2, 1, 12)
        self.assertEqual(str(r1), "[Square] (12) 2/1 - 4")

    def test_update(self):
        """Test for update method - *args"""
        r1 = Square(10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Square] (89) 10/10 - 10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Square] (89) 10/10 - 2")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Square] (89) 3/10 - 2")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Square] (89) 3/4 - 2")
        """Test for update method - **kwargs"""
        r1 = Square(10, 10, 10)
        r1.update(size=1)
        self.assertEqual(str(r1), "[Square] (46) 10/10 - 1")
        r1.update(size=1, x=2)
        self.assertEqual(str(r1), "[Square] (46) 2/10 - 1")
        r1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(r1), "[Square] (89) 3/1 - 2")

    def test_create(self):
        """Test for create method"""
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_save_to_file(self):
        """Test for save_to_file method - working"""
        r1 = Square(10, 2, 8)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[{\"id\": 43, \"size\": 10, " +
                             "\"x\": 2, \"y\": 8}, " +
                             "{\"id\": 44, \"size\": 2, " +
                             "\"x\": 4, \"y\": 0}]")
        os.remove("Square.json")
        """Test for save_to_file method - None"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Square.json")
        """Test for save_to_file method - Empty"""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Square.json")

    def test_load_from_file(self):
        """Test for load_from_file method - File exists"""
        r1 = Square(10, 2, 8)
        r2 = Square(2, 4)
        list_squares_input = [r1, r2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output[0].width, 10)
        self.assertEqual(list_squares_output[1].width, 2)
        os.remove("Square.json")
        """Test for load_from_file method - File not exist"""
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])
        self.assertEqual(list_squares_output, [])


if __name__ == "__main__":
    unittest.main()
