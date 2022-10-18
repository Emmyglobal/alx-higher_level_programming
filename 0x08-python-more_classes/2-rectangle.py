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
        if type(self.width) is not int:
            raise TypeError
        elif self.width < 0:
            raise ValueError
        else:
            return self.width

    @property
    def height(self)
	return self.__height

    @height.setter
    def height(self, value):
        if type(self.height) is not int:
            raise TypeError
        elif self.height < 0:
            raise ValueError
    def area(self,value):
        self.area = self.width * self.height
        return self.area
    def perimeter(self, value):
        self.perimeter = 2*(self.height + self.width)
	return self.perimeter
