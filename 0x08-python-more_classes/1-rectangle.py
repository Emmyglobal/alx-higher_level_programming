#!/usr/bin/python3
class Rectangle:
	def __init__(self, width=0, height=0):
		self.width = _Rectangle__width
		self.height = _Rectangle__height
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
