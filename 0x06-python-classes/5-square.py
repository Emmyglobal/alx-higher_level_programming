#!/usr/bin/python3
"""defines a square"""


class Square:
    """Defines a class: Square with a public attribute:
    size and raises exceptions and returns the area of the square @property and setter
    """
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return pow(self.__size, 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise valueError("size must be >= 0")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(pow(slf.__size, 2)):
                print('#', end='')
