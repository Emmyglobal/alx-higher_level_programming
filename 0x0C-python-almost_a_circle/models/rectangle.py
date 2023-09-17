#!/usr/bin/python3
from models.base import Base
"""A class that inherits from Base"""


class Rectangle(Base):
    """The first constructor of the class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id) #call the supperclass constructor
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if value <= 0:
                raise ValueError("Width must be greater than 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if value <= 0:
                raise ValueError('height must be greater than 0')
            self.height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            if value < 0:
                raise ValueError('X must be non-negative')
            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            if value < 0:
                raise ValueError("Y must be a non-negative")
            self.__y = value

        def area(self):
            return self.width * self.height

        def display(self):
            for _ in range(self.y):
                print()
            for _ in range(self.height):
                print(" " * self.x + "#" * self.width)

        def __str__(self):
            return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
