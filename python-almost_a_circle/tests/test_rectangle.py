#!/usr/bin/python3
"""unittest for Base Class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test case for Rectangle Class"""
    def test_id(self):
        """Test for id attribute"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 12)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 13)
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
        

    def test_height(self):
        """Test for height method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.height, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.height, 2)

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
        """Test for display method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.display(), None)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.display(), None)
        r3 = Rectangle(10, 2, 2, 0, 12)
        self.assertEqual(r3.display(), None)

if __name__ == "__main__":
    unittest.main()
