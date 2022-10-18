#!/usr/bin/python3
'''
a python class
'''


class Rectangle:
    '''
    that has value
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(self.__width) != int:
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >= 0")
        else:
            return self.__width

    @property
    def height(self)
	return self.__height

    @height.setter
    def height(self, value):
        if type(self.__height) != int:
            raise TypeError("height must be an integer")
        elif self.__height < 0:
            raise ValueError("height must be >= 0")
    def area(self,value):
        self.area = self.width * self.height
        return self.area
    def perimeter(self, value):
        self.perimeter = 2*(self.height + self.width)
	return self.perimeter
