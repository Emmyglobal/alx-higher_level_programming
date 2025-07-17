#!/usr/bin/python3
"""test for rectangle"""
import unittest
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

    def test_valid_initialization():
        r = Rectangle(10, 20, 1, 2, 99)
        assert r.width == 10
        assert r.height == 20
        assert r.x == 1
        assert r.y == 2
        assert r.id == 99

    def test_valid_default_xy():
        r = Rectangle(5, 6)
        assert r.x == 0
        assert r.y == 0

    def test_invalid_width_type():
        try:
            Rectangle

if __name__ == '__main__':
    unittest.main()
