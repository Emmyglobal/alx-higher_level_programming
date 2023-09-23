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

    def update(self, *args, **kwargs):
        """Updating instance attributes using postional args
            and keyword arguments
        """
        if len(args) != 0:
            try:
                self.id = args[0]
            except IndexError:
                pass
            try:
                self.__width = args[1]
            except IndexError:
                pass
            try:
                self.__height = args[2]
            except IndexError:
                pass
            try:
                self.x = args[3]
            except IndexError:
                pass
            try:
                self.y = args[4]
            except IndexError:
                pass
        else:
            try:
                self.id = kwargs["id"]
            except KeyError:
                pass
            try:
                self.__width = kwargs["width"]
            except KeyError:
                pass
            try:
                self.__height = kwargs["height"]
            except KeyError:
                pass
            try:
                self.x = kwargs["x"]
            except KeyError:
                pass
            try:
                self.y = kwargs["y"]
            except KeyError:
                pass


    @property
    def width(self):
        """
        This is the getter of the width variable
        this method returns the width of the rectangle.
        Args:
            value: sets the value for the width.
        Return width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        This is a getter of the height variable.
        This method returns the height of the rectangle.
        Args:
            value: sets value for the height.
        Return height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
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
        Return x of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
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
        Return y of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle
        Returns the area
        """
        return self.width * self.height

    def display(self):
        """
        displays the area in form of a rectangle
        using #
        """
        for val_y in range(self.y):
            print()
        for val in range(self.height):
            print(f" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns the string representation of an object
        """
        return (f"[Rectangle] ({self.id})"
                f" {self.x}/{self.y} - {self.width}/{self.height}")

    def to_dictionary(self):
        """Returns a dictionary representation of a Rectangle."""
        return_dict = {}
        return_dict['id'] = self.id
        return_dict['width'] = self.width
        return_dict['height'] = self.height
        return_dict['x'] = self.x
        return_dict['y'] = self.y
        return return_dict
