#!/usr/bin/python3
"""A class MyInt that inherits from int"""


class MyInt(int):
    """Myint is a rebel that has operators inverted"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
