#!/usr/bin/python3
"""unittest for Base Class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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
        """Test to_json_string method - None"""
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")
        """Test to_json_string method - Not None"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary,
                         "[{\"id\": 5, \"width\": 10, " +
                         "\"height\": 7, \"x\": 2, \"y\": 8}]")

    def test_from_json_string(self):
        """Test from_json_string method - None"""
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])
        """Test from_json_string method - Empty"""
        list_output = Rectangle.from_json_string("[]")
        self.assertEqual(list_output, [])
        """Test from_json_string method - Not None"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89},
                                       {'height': 7, 'width': 1, 'id': 7}])


if __name__ == "__main__":
    unittest.main()
