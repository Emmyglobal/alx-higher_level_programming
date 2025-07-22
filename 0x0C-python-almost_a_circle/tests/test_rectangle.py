#!/usr/bin/python3
"""test for rectangle"""
import unittest
import sys
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
       
    def test_str_method(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_without_xy(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        Rectangle(2, 3).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "##\n##\n##\n")

    def test_display_with_xy(self):
        r = Rectangle(2, 2, 2, 2)
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n  ##\n  ##\n")

    def test_output(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_zero_position(self):
        r = Rectangle(4, 6, 0, 0, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 0/0 - 4/6")

    def test_update_args(self):
        r = Rectangle(1, 2, 3, 4, 10)
        r.update(89, 4, 5, 6, 7)
        self.assertEqual(str(r), "[Rectangle] (89) 6/7 - 4/5")

    def test_update_with_fewer_position(self):
        r = Rectangle(1, 1, 1, 1, 5)
        r.update(99, 10)
        self.assertEqual(str(r), "[Rectangle] (99) 1/1 - 10/1")

    def test_with_key_args(self):
        r = Rectangle(1, 2, 3, 4, 8)
        r.update(height=10, width=20, y=5)
        self.assertEqual(str(r), "[Rectangle] (8) 3/5 - 20/10")

    def test_with_extra_key_args(self):
        r = Rectangle(2, 2, 0, 0, 99)
        r.update(a=1, width=5)
        self.assertEqual(str(r), "[Rectangle] (99) 0/0 - 5/2")

    def test_args_takes_precedence(self):
        r = Rectangle(2, 3, 1, 1, 100)
        r.update(200, 10, 10, 0, 0, height=50)
        self.assertEqual(str(r), "[Rectangle] (200) 0/0 - 10/10")

    def test_no_args_or_kwargs(self):
        r = Rectangle(5, 5, 2, 2, 300)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (300) 2/2 - 5/5")

    def test_dictionary(self):
        r = Rectangle(10, 2, 1, 9)
        result = {'width': 10, 'x': 1, 'y': 9, 'height': 2, 'id': 2}
        self.assertEqual(r.to_dictionary(), result)

if __name__ == '__main__':
    unittest.main()
