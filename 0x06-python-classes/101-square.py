#!/usr/bin/python3
"""
A class that defines a square by:
private instance attributes size and position
instance method area and and my_print
"""

class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size
    
    @property
    def position(self):
        return self.__position
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2\
        or not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        print(self.__str__())
    
    def __str__(self):
        """String representation of the square for printing"""
        if self.__size == 0:
            return ""
        result = []
        for _ in range(self.__position[1]):
            result.append("")
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(result)
    