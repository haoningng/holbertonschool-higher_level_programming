#!/usr/bin/python3
"""unittest for Rectangle Class"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys
import os


class TestRectangle(unittest.TestCase):
    """Test case for Rectangle Class"""
    def test_id(self):
        """Test for id attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 15)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 16)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_width(self):
        """Test for width method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        with self.assertRaises(TypeError):
            r3 = Rectangle("Hello", 2)
        with self.assertRaises(TypeError):
            r3 = Rectangle(2, "World")
        with self.assertRaises(TypeError):
            r3 = Rectangle(2, 3, "World")
        with self.assertRaises(TypeError):
            r3 = Rectangle(2, 3, 4, "World")
        with self.assertRaises(ValueError):
            r3 = Rectangle(2, -3)
        with self.assertRaises(ValueError):
            r3 = Rectangle(-2, 3)
        with self.assertRaises(ValueError):
            r3 = Rectangle(2, 3, -4)
        with self.assertRaises(ValueError):
            r3 = Rectangle(2, 3, 4, -5)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 10)

    def test_height(self):
        """Test for height method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.height, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.height, 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 0)

    def test_x(self):
        """Test for x method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.x, 0)
        r3 = Rectangle(10, 2, 2, 0, 12)
        self.assertEqual(r3.x, 2)

    def test_y(self):
        """Test for y method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.y, 0)
        r3 = Rectangle(10, 2, 2, 4, 12)
        self.assertEqual(r3.y, 4)

    def test_area(self):
        """Test for area method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)
        r2 = Rectangle(3, 10)
        self.assertEqual(r2.area(), 30)
        r3 = Rectangle(1, 2, 2, 0, 12)
        self.assertEqual(r3.area(), 2)

    def test_display(self):
        """Test for display method - no x no y"""
        r1 = Rectangle(2, 2)
        display_1 = "##\n##\n"
        captured_input = StringIO()
        sys.stdout = captured_input
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_input.getvalue(), display_1)
        """Test for display method - no y"""
        r1 = Rectangle(2, 2, 2)
        display_1 = "  ##\n  ##\n"
        captured_input = StringIO()
        sys.stdout = captured_input
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_input.getvalue(), display_1)
        """Test for display method"""
        r1 = Rectangle(2, 2, 2, 1)
        display_1 = "\n  ##\n  ##\n"
        captured_input = StringIO()
        sys.stdout = captured_input
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_input.getvalue(), display_1)

    def test_str(self):
        """Test for __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """Test for update method - *args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        """Test for update method - **kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (24) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (24) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_create(self):
        """Test for create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_save_to_file(self):
        """Test for save_to_file method - working"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[{\"id\": 21, \"width\": 10, " +
                             "\"height\": 7, \"x\": 2, \"y\": 8}, " +
                             "{\"id\": 22, \"width\": 2, " +
                             "\"height\": 4, \"x\": 0, \"y\": 0}]")
        os.remove("Rectangle.json")
        """Test for save_to_file method - None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Rectangle.json")
        """Test for save_to_file method - Empty"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Rectangle.json")

    def test_load_from_file(self):
        """Test for load_from_file method - File exists"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].width, 10)
        self.assertEqual(list_rectangles_output[1].width, 2)
        os.remove("Rectangle.json")
        """Test for load_from_file method - File not exist"""
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])
        self.assertEqual(list_rectangles_output, [])


if __name__ == "__main__":
    unittest.main()
