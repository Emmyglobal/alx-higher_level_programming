#!/usr/bin/python3
"""
A class square that defines a square by:
private instance attribute: size
instantiation with optional size
public instance method
"""


class Square:
    "defines a square"

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
