#!/usr/bin/python3
"""
A python file to demonstrate class and object
"""


class Square:
    """
    A python class that has a value
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return (self.__size)**2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        if self.position[1] != 0:
            for m in range(self.position[1]):
                print()
        for i in range(self.__size):
            if self.position[0] != 0:
                for n in range(self.position[0]):
                    print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
