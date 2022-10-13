#!/usr/bin/python3
"""
A python file to demonstrate class and object
"""


class Square:
    """
    A python class that has a value
    """
    def __init__(self, __size=0):
        if type(__size) != int:
            raise TypeError("size must be an integer")
        self.__size = __size
        if self.__size < 0:
            raise ValueError("size must be >= 0")
