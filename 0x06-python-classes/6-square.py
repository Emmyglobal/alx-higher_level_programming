#!/usr/bin/python3
"""defines a square"""


class Square:
    """Defines a class: Square with a private attribute:
    size and raises exceptions and returns the area of
    the square @property and setter
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return pow(self.__size, 2)

    def my_print(self):
        for j in range(self.__position[1]):
            print()
        if self.__size == 0:
            return print()
        else:
            for i in range(pow(self.__size, 2)):
                for y in range(self.__position[0]):
                    print(" ", end="")
                if (i % self.__size == 0) and (i != 0):
                    print()
                print("#", end="")
        print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type((self.__position) != tuple) and (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
