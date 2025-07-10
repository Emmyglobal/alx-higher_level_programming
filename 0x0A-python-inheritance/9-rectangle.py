#!/usr/bin/python3
"""inherits from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """intatiation with with and height"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of a triangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints out the string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
