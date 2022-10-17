#!/usr/bin/python3
class Rectangle:
        def __init__(self, width=0, height=0):
                self.width = width
                self.height = height
        def width(self, value):
                if type(self.width) is not int:
                        raise TypeError
                elif self.width < 0:
                        raise ValueError
                else:
                        return self.width
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
		if (width = 0) or (height = 0):
			self.perimeter = 0
                return self.perimeter
