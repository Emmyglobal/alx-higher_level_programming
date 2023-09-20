#!/usr/bin/python3
"""
A class that inherits from Base class with other methods
The rectangle depends on the base class for its id
"""
from models.base import Base


class Rectangle(Base):
    """
    This is a simple rectangle class
    This class inherits from the base class
    and relies on the base class for the validation of its id.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The first constructor of the rectangle class.
        Args:
            Width: This variable holds the width of a rectangle.
            height: This variable holds the height of a rectangle
            x: x-axis of the rectangle
            y: y-axis of the rectangle
            id: this variable holds the id of the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """
            This is the getter of the width variable
            this method returns the width of the rectangle.
            Args:
                value: sets the value for the width.
            """
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("Width must be > 0")
            self.__width = value

        @property
        def height(self):
            """
            This is a getter of the height variable.
            This method returns the height of the rectangle.
            Args:
                value: sets value for the height.
            """
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError('height must be > 0')
            self.__height = value

        @property
        def x(self):
            """
            This is a getter of the x-axis.
            This is the getter for the x-axis
            Args:
                value: sets value for x axis
            """
            return self.__x

        @x.setter
        def x(self, value):
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError('x must be >= 0')
            self.__x = value

        @property
        def y(self):
            """
            This is a getter of the y variable.
            This is the method for the y-axis
            Args:
                value: sets the value of y
            """
            return self.__y

        @y.setter
        def y(self, value):
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            return self.width * self.height

        def __str__(self):
            return (f"[Rectangle] ({self.id})"
                    f" {self.x}/{self.y} - {self.width}/{self.height}")
