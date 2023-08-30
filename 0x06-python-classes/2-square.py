#!/usr/bin/python3
"""defines a square"""


class Square:
    """Defines a class: Square with a private attribute:
    size and raises exception
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
