#!/usr/bin/python3
"""Rectangle class that inherits from base"""
from models.base import Base
import sys


class Rectangle(Base):
    """private instances"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """private instances"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @staticmethod
    def __validate_positive_integer(name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    @staticmethod
    def __validate_neg_int(name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate_positive_integer("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate_positive_integer("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__validate_neg_int("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__validate_neg_int("y", value)
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prnts area to te standard output"""
        for _ in range(self.y):
            sys.stdout.write("\n")
        for i in range(self.height):
            sys.stdout.write(" " * self.x)
            sys.stdout.write("#" * self.width + "\n")

    def __str__(self):
        """returns Rectangle string"""
        t = self.width
        m = self.height
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {t}/{m}"

    def update(self, *args, **kwargs):
        """updates the Rectangle by adding the public method"""
        attr = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            if i < len(attr):
                setattr(self, attr[i], args[i])

        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
