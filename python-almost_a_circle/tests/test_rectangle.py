#!/usr/bin/python3
"""unittest for Base Class"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import io, sys, os


class TestRectangle(unittest.TestCase):
    """Test case for Rectangle Class"""
    def test_id(self):
        """Test for id attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 13)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 14)
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

if __name__ == "__main__":
    unittest.main()
