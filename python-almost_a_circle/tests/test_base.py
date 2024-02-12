#!/usr/bin/python3
"""unittest for Base Class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test case for Base Class"""
    def test_id(self):
        """Test id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
    
    def test_to_json_string(self):
        """Test to_json_string method"""
        pass


if __name__ == "__main__":
    unittest.main()
