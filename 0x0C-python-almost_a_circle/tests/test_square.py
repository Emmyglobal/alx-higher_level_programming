#!/usr/bin/python3
"""Unittest for the Square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test case for the square"""
    def test_square_creation(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_square_with_all_args(self):
        s = Square(5, 2, 3, 99)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 99)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.size, 10)

    def test_str_output(self):
        s = Square(4, 2, 1, 42)
        self.assertEqual(str(s), "[Square] (42) 2/1 - 4")

    def test_update_args(self):
        s = Square(5)
        s.update(89, 10, 4, 2)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 2)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(size=7, y=9, x=6, id=101)
        self.assertEqual(s.id, 101)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 9)

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 5)
        expected = {'id': 5, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_invalid_size_type(self):
        with self.assertRaises(TypeError):
            Square("4")

    def test_invalid_size_value(self):
        with self.assertRaises(ValueError):
            Square(-4)

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Square(4, "1")

    def test_invalid_y_value(self):
        with self.assertRaises(ValueError):
            Square(4, 1, -2)

if __name__ == "__main__":
    unittest.main()
