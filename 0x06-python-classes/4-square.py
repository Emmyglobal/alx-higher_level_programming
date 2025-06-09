#!/usr/bin/python3
"""
A class square thatdefines a square by:
private instance attribute size:
instantiation with optional size
public instance method
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
