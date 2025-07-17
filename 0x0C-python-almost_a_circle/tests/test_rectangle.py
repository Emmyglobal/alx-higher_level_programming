#!/usr/bin/python3
"""test for rectangle"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """test cases"""

    def test_initialization(self):
        r = Rectangle(10, 20, 1, 2, 99)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 99)

    def test_setters_and_getters(self):
        r = Rectangle(1, 2)
        r.width = 5
        r.height = 6
        r.x = 7
        r.y = 8
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 8)

    def test_valid_initialization(self):
        r = Rectangle(10, 20, 1, 2, 99)
        assert r.width == 10
        assert r.height == 20
        assert r.x == 1
        assert r.y == 2
        assert r.id == 99

    def test_valid_default_xy(self):
        r = Rectangle(5, 6)
        assert r.x == 0
        assert r.y == 0

    def test_invalid_width_type(self):
        try:
            Rectangle("10", 20, 1, 2)
        except TypeError as e:
            assert str(e) == "width must be an integer"

    def test_invalid_width_value(self):
        try:
            Rectangle(0, 20, 1, 2)
        except ValueError as e:
            assert str(e) == "width must be > 0"

    def test_invalid_height_type(self):
        try:
            Rectangle(10, "20", 1, 2)
        except TypeError as e:
            assert str(e) == "height must be an integer"

    def tet_invalid_height_value(self):
        try:
            Rectangle(10, -1, 1, 2)
        except valueError as e:
            assert str(e) == "height must be > 0"

    def test_invalid_x_type(self):
        try:
            Rectangle(10, 20, x="1", y=4)
        except TypeError as e:
            assert str(e) == "x must be an integer"

    def test_invalid_x_value(self):
        try:
            Rectangle(10, 20, x=-1, y=2)
        except ValueError as e:
            assert str(e) == "x must be >= 0"

    def test_invalid_y_type(self):
        try:
            Rectangle(10, 20, 0, "2")
        except TypeError as e:
            assert str(e) == "y must be an integer"

    def test_invalid_y_value(self):
        try:
            Rectangle(10, 20, 1, -2)
        except ValueError as e:
            assert str(e) == "y must be >= 0"

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_display_output_correct(self):
        r = Rectangle(3, 2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "###\n###\n")

    def test_display_with_width_0(self):
        r = Rectangle(2, 2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")

    def test_display_with_height_0(self):
        r = Rectangle(1, 1)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "#\n")
        

if __name__ == '__main__':
    unittest.main()
