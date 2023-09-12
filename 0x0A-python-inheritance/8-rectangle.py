#!/usr/bin/python3
"""
a class that inherits from BaseGeometry with public instance"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle inherited from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        raise Exception('area() is not implemented')
